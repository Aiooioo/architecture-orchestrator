#!/usr/bin/env python3
"""kb 事实层索引器 + 八查 lint（审查者≠作者 · 真相在 system-arch-base tools/）。

用法（项目仓根目录）:
    python3 tools/kb-index.py            # 重建 _meta/kb-index.json、graph.json、MOC 围栏 + lint
    python3 tools/kb-index.py --check    # 只读校验：重算与盘上比对（⑦⑧漂移）+ lint，供 gate ⑥ 调用
    python3 tools/kb-index.py --stale-days 90
退出码: 0=pass, 1=fail（FAIL 级 lint 或漂移）。词表权威=kb/_meta/taxonomy.md。

八查: ①死链 ②词表越界 ③必填 frontmatter/枚举/id-slug-目录一致 ④slug/id/alias 重复
      ⑤孤儿 atom（warn）⑥陈旧（warn）⑦contradiction 的 OQ 不在 LEDGER ⑧索引/图/MOC 围栏漂移。
"""
import datetime, json, pathlib, re, sys

STATUS_ENUM = {"observed", "verified", "stale"}
REQUIRED_FM = ["id", "kind", "domain", "planes", "status", "last-verified", "summary"]
NON_EDGE_KEYS = set(REQUIRED_FM) | {"aliases", "sources", "tags"}
WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
FENCE = re.compile(r"(<!-- kb:generated:start ([^>]*?) -->)(.*?)(<!-- kb:generated:end -->)", re.S)
OQ_RE = re.compile(r"OQ-\d{3}")


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line or line.startswith((" ", "-")):
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, m.group(2)


def as_list(raw):
    """inline 列表解析：[a, b] / ["[[x]]", "[[y]]"] / 空。"""
    if not raw or raw in ("[]", "null"):
        return []
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        items = [i.strip().strip("\"'") for i in raw[1:-1].split(",")]
        return [i for i in items if i]
    return [raw.strip("\"'")]


def link_targets(values):
    out = []
    for v in values:
        m = WIKILINK.search(v)
        out.append(m.group(1).strip() if m else v)
    return out


def parse_taxonomy(path):
    tax = {"planes": [], "kinds": {}, "edges": [], "tags": []}
    if not path.is_file():
        return tax
    sec = None
    for line in path.read_text().splitlines():
        mh = re.match(r"^## (\w+)", line)
        if mh:
            sec = mh.group(1)
            continue
        mi = re.match(r"^- ([\w-]+)(?:\s*\((\w+)\))?", line)
        if mi and sec in tax:
            if sec == "kinds":
                tax["kinds"][mi.group(1)] = mi.group(2) or ""
            else:
                tax[sec].append(mi.group(1))
    return tax


def build(root, stale_days):
    kb = root / "kb"
    tax = parse_taxonomy(kb / "_meta" / "taxonomy.md")
    fails, warns = [], []
    atoms, edges = [], []
    slugs, ids, alias_owner = {}, {}, {}

    for p in sorted(kb.glob("atoms/*/*.md")):
        slug = p.stem
        rel = str(p.relative_to(root))
        fm, body = parse_frontmatter(p.read_text())
        # ③ 必填/枚举/一致性
        for k in REQUIRED_FM:
            if not fm.get(k):
                fails.append(f"③{rel} 缺 {k}")
        status = fm.get("status", "")
        if status and status not in STATUS_ENUM:
            fails.append(f"③{rel} status 非法: {status}")
        kind = fm.get("kind", "")
        if kind and tax["kinds"] and kind not in tax["kinds"]:
            fails.append(f"②{rel} kind 越界: {kind}")
        prefix = tax["kinds"].get(kind, "")
        if prefix and fm.get("id") and not fm["id"].startswith(prefix + "-"):
            fails.append(f"③{rel} id={fm['id']} 前缀 ≠ kind({kind}) 的 {prefix}-")
        if prefix and not slug.startswith(prefix.lower() + "-"):
            fails.append(f"③{rel} 文件名前缀 ≠ {prefix.lower()}-")
        if fm.get("domain") and fm["domain"] != p.parent.name:
            fails.append(f"③{rel} domain={fm['domain']} ≠ 目录 {p.parent.name}")
        planes = as_list(fm.get("planes", ""))
        for pl in planes:
            if tax["planes"] and pl not in tax["planes"]:
                fails.append(f"②{rel} plane 越界: {pl}")
        # ④ 重复
        if slug in slugs:
            fails.append(f"④slug 重复: {slug}（{rel} 与 {slugs[slug]}）")
        slugs[slug] = rel
        if fm.get("id"):
            if fm["id"] in ids:
                fails.append(f"④id 重复: {fm['id']}（{rel} 与 {ids[fm['id']]}）")
            ids[fm["id"]] = rel
        for al in as_list(fm.get("aliases", "")):
            if al in alias_owner and alias_owner[al] != slug:
                fails.append(f"④alias 冲突: {al!r}（{slug} 与 {alias_owner[al]}）")
            alias_owner[al] = slug
        # edges（frontmatter 未知键 = 应为 taxonomy edge）
        atom_edges = []
        for k, v in fm.items():
            if k in NON_EDGE_KEYS:
                continue
            if tax["edges"] and k not in tax["edges"]:
                fails.append(f"②{rel} edge 越界: {k}")
                continue
            for tgt in link_targets(as_list(v)):
                atom_edges.append((slug, tgt, k))
        for tgt in WIKILINK.findall(body):
            atom_edges.append((slug, tgt.strip(), "mentions"))
        edges.extend(atom_edges)
        # ⑦ contradiction → OQ
        for block in re.findall(r"> \[!contradiction\][^\n]*(?:\n>[^\n]*)*", body):
            if not OQ_RE.search(block):
                fails.append(f"⑦{rel} contradiction 块未引用 OQ")
        # ⑥ 陈旧
        try:
            age = (datetime.date.today() - datetime.date.fromisoformat(fm.get("last-verified", ""))).days
            if age > stale_days and status != "stale":
                warns.append(f"⑥{rel} last-verified 超 {stale_days} 天（{age}d）但 status={status}")
        except ValueError:
            pass
        atoms.append({
            "id": fm.get("id", ""), "slug": slug, "path": rel, "kind": kind,
            "domain": fm.get("domain", ""), "planes": planes,
            "status": status, "summary": fm.get("summary", ""),
            "aliases": as_list(fm.get("aliases", "")), "last_verified": fm.get("last-verified", ""),
        })

    moc_stems = {p.stem for p in kb.glob("mocs/*.md")}
    known = set(slugs) | moc_stems
    # ① 死链（atom 侧的全部 wikilink 目标须可解析为 slug/alias/moc）
    for frm, tgt, typ in edges:
        if tgt not in known and tgt not in alias_owner:
            fails.append(f"①死链: {frm} -[{typ}]-> [[{tgt}]]")
    # ⑤ 孤儿（无入边且未被任何 MOC 正文链接）
    inbound = {t for _, t, ty in edges if ty != "mentions"} | {alias_owner.get(t) for _, t, _ in edges}
    moc_linked = set()
    for p in kb.glob("mocs/*.md"):
        moc_linked |= {t.strip() for t in WIKILINK.findall(p.read_text())}
    for a in atoms:
        if a["slug"] not in inbound and a["slug"] not in moc_linked and not any(
                e for e in edges if e[0] == a["slug"] and e[2] != "mentions"):
            warns.append(f"⑤孤儿 atom: {a['slug']}（无 typed 边且未被 MOC 收录）")
    # ⑦ LEDGER 对账（contradiction 引用的 OQ 必须存在）
    ledger = (root / "LEDGER.md").read_text() if (root / "LEDGER.md").is_file() else ""
    for p in sorted(kb.glob("atoms/*/*.md")):
        for oq in set(OQ_RE.findall(p.read_text())) - set(OQ_RE.findall(ledger)):
            fails.append(f"⑦{p.stem} 引用 LEDGER 不存在的 {oq}")

    index = {"atoms": atoms, "facets": {
        "by_domain": facet(atoms, "domain"), "by_kind": facet(atoms, "kind"),
        "by_status": facet(atoms, "status"),
        "by_plane": facet_multi(atoms, "planes")}}
    graph = {"edges": [{"from": f, "to": alias_owner.get(t, t), "type": ty}
                       for f, t, ty in sorted(set(edges))]}
    return index, graph, atoms, graph["edges"], fails, warns


def facet(atoms, key):
    out = {}
    for a in atoms:
        out.setdefault(a[key] or "?", []).append(a["slug"])
    return {k: sorted(v) for k, v in sorted(out.items())}


def facet_multi(atoms, key):
    out = {}
    for a in atoms:
        for v in a[key]:
            out.setdefault(v, []).append(a["slug"])
    return {k: sorted(v) for k, v in sorted(out.items())}


def moc_fence_content(spec, atoms, edges):
    kv = dict(re.findall(r"(\w+)=([\w-]+)", spec))
    if "domain" in kv:
        sel = [a for a in atoms if a["domain"] == kv["domain"]]
        title = f"domain={kv['domain']}"
    elif "plane" in kv:
        sel = [a for a in atoms if kv["plane"] in a["planes"]]
        title = f"plane={kv['plane']}"
    else:
        return "\n（未知围栏 spec）\n"
    lines = ["", f"<!-- 由 kb-index.py 生成（{title}），勿手改 -->", "",
             "| atom | kind | domain | planes | status | last-verified | summary |",
             "|---|---|---|---|---|---|---|"]
    for a in sorted(sel, key=lambda x: (x["kind"], x["slug"])):
        lines.append(f"| [[{a['slug']}]] | {a['kind']} | {a['domain']} | {', '.join(a['planes'])} "
                     f"| {a['status']} | {a['last_verified']} | {a['summary']} |")
    sel_slugs = {a["slug"] for a in sel}
    rel = [e for e in edges if e["type"] != "mentions" and (e["from"] in sel_slugs or e["to"] in sel_slugs)]
    if rel:
        lines += ["", "```mermaid", "flowchart LR"]
        for e in rel:
            lines.append(f"    {e['from']} -- {e['type']} --> {e['to']}")
        lines += ["```"]
    return "\n".join(lines) + "\n"


def main():
    args = sys.argv[1:]
    check = "--check" in args
    stale_days = int(args[args.index("--stale-days") + 1]) if "--stale-days" in args else 90
    root = pathlib.Path.cwd()
    kb = root / "kb"
    if not kb.is_dir():
        print("== KB SKIP（无 kb/ 目录）==")
        sys.exit(0)

    index, graph, atoms, edges, fails, warns = build(root, stale_days)
    idx_txt = json.dumps(index, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    gr_txt = json.dumps(graph, ensure_ascii=False, indent=1, sort_keys=True) + "\n"

    targets = {kb / "_meta" / "kb-index.json": idx_txt, kb / "_meta" / "graph.json": gr_txt}
    moc_new = {}
    for p in sorted(kb.glob("mocs/*.md")):
        old = p.read_text()
        new = FENCE.sub(lambda m: m.group(1) + moc_fence_content(m.group(2), atoms, edges) + m.group(4), old)
        moc_new[p] = (old, new)

    if check:
        for p, txt in targets.items():
            if not p.is_file() or p.read_text() != txt:
                fails.append(f"⑧漂移: {p.relative_to(root)}（需重跑 kb-index.py）")
        for p, (old, new) in moc_new.items():
            if old != new:
                fails.append(f"⑧MOC 围栏漂移: {p.relative_to(root)}")
    else:
        (kb / "_meta").mkdir(parents=True, exist_ok=True)
        for p, txt in targets.items():
            p.write_text(txt)
        for p, (old, new) in moc_new.items():
            if old != new:
                p.write_text(new)

    for w in warns:
        print(f"WARN {w}")
    if fails:
        for f in fails:
            print(f"FAIL {f}")
        print(f"== KB {'CHECK ' if check else ''}FAIL ({len(fails)} 项) ==")
        sys.exit(1)
    print(f"== KB {'CHECK ' if check else ''}PASS（atoms={len(atoms)}, edges={len(edges)}, 八查过）==")
    sys.exit(0)


if __name__ == "__main__":
    main()
