#!/usr/bin/env python3
"""architecture-method 门禁六查（审查者≠作者 · 只读 · 真相在 system-arch-base tools/）。

用法（在项目仓根目录）:
    python3 tools/gate.py --gate <G0|G1|G2|G3|CYC-NNN>
    python3 tools/gate.py --check-config          # 仅校验配置可解析（中枢自检用）
退出码: 0=pass, 1=fail。词表与矩阵权威=同目录 gate-config.json。

六查: ①frontmatter/枚举 ②必备 WP 达标（GC 按章程动态；change 型加 domain-map 覆盖规则）
      ③阻塞扫描（BLOCKED-ON/ASSUMES/孤儿 OQ/域内 open OQ）④INDEX 对账 ⑤前置 GATE/CYC 记录
      ⑥kb 八查（kb-index.py --check；无 kb/ 跳过）。
刻意不做: Mermaid 语法（引 node 破坏零依赖）、跨 WP 语义一致（评审面板职责）。
"""
import json, pathlib, re, subprocess, sys

STATUS_RE = re.compile(r"^(draft|review|released|superseded|baselined@(G0|G1|G2|G3|CYC-\d{3}))$")
MARK_BLOCKED = re.compile(r"\[BLOCKED-ON:\s*(OQ-\d{3})\]")
MARK_ASSUMES = re.compile(r"\[ASSUMES:\s*(OQ-\d{3})\s*=[^\]]*\]")
OQ_REF = re.compile(r"\bOQ-\d{3}\b")
LEDGER_BLOCK = re.compile(r"^### (OQ-\d{3}|RSK-\d{3}|CYC-\d{3}|GATE-\S+)", re.M)


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-", "#")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def parse_affected_wps(text):
    """章程 frontmatter 的 affected_wps 列表（仅识别固定三键缩进结构）。"""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return []
    items, cur, in_list = [], None, False
    for line in m.group(1).splitlines():
        if re.match(r"^affected_wps:\s*$", line):
            in_list = True
            continue
        if in_list:
            if re.match(r"^\S", line):  # 回到顶层键，列表结束
                break
            mi = re.match(r"^\s*-\s*wp:\s*(\S+)", line)
            if mi:
                cur = {"wp": mi.group(1), "target_version": None, "min_status": "review", "instance": None}
                items.append(cur)
                continue
            for key in ("target_version", "min_status", "instance"):
                mk = re.match(rf"^\s+{key}:\s*(\S+)", line)
                if mk and cur is not None:
                    cur[key] = mk.group(1)
    return items


def parse_domain_map(path):
    """domain-map 覆盖台账行 → {domain: coverage}（列序固定 | domain | coverage | ... |）。"""
    out = {}
    for line in path.read_text().splitlines():
        m = re.match(r"^\|\s*([\w-]+)\s*\|\s*(unmapped|mapped|baselined|stale)\s*\|", line)
        if m and m.group(1) not in ("domain",):
            out[m.group(1)] = m.group(2)
    return out


def parse_ledger_blocks(text):
    """{ID: {字段: 值}} — `### ID` 块 + `- key: value` 行。"""
    blocks, ids = {}, [(m.group(1), m.start()) for m in LEDGER_BLOCK.finditer(text)]
    for i, (bid, start) in enumerate(ids):
        end = ids[i + 1][1] if i + 1 < len(ids) else len(text)
        fields = {}
        for line in text[start:end].splitlines():
            mk = re.match(r"^- (\S+?):\s*(.+)$", line.strip())
            if mk:
                fields[mk.group(1)] = mk.group(2).strip()
        blocks[bid] = fields
    return blocks


def status_base(status):
    return status.split("@", 1)[0]


def latest(root, wp_dir, slug, want_version=None, instance=None):
    """该 WP（或其域实例）的目标文件：want_version 指定版本，否则取最大 vN。返回 (path|None, N)。"""
    d = root / wp_dir
    stem = f"{slug}.{instance}" if instance else slug
    best, best_n = None, -1
    for p in sorted(d.glob(f"{stem}.v*.md")) if d.is_dir() else []:
        mv = re.match(rf"{re.escape(stem)}\.v(\d+)\.md$", p.name)
        if not mv:
            continue
        n = int(mv.group(1))
        if want_version is not None:
            if n == int(want_version):
                return p, n
        elif n > best_n:
            best, best_n = p, n
    return (None, int(want_version)) if want_version is not None else (best, best_n)


def main():
    args = sys.argv[1:]
    here = pathlib.Path(__file__).parent
    cfg = json.loads((here / "gate-config.json").read_text())

    if "--check-config" in args:
        for prof, gates in cfg["profiles"].items():
            print(f"profile {prof}: gates = {', '.join(gates)}")
        print("== CONFIG OK ==")
        sys.exit(0)

    if "--gate" not in args:
        print(__doc__)
        sys.exit(1)
    gate_id = args[args.index("--gate") + 1]
    root = pathlib.Path.cwd()

    fails, warns = [], []
    order = cfg["status_order"]

    # 项目元数据（mode 选 profile）
    py = root / "project.yaml"
    if not py.is_file():
        print("FAIL 项目根缺 project.yaml（须在项目仓根目录运行）")
        sys.exit(1)
    meta = {}
    for l in py.read_text().splitlines():
        l = l.split("#", 1)[0]
        if ":" in l:
            k, v = l.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")
    mode = meta.get("mode", "")
    profile = cfg["profiles"].get(mode)
    if not profile:
        print(f"FAIL project.yaml mode 非法: {mode!r}")
        sys.exit(1)

    # gate 规格（GC 动态）
    charter = None
    if re.match(r"^CYC-\d{3}$", gate_id):
        spec = profile.get("GC")
        if not spec:
            print(f"FAIL profile {mode} 无 GC 门禁")
            sys.exit(1)
        hits = list((root / "cycles").glob(f"{gate_id}-*.md"))
        if len(hits) != 1:
            print(f"FAIL 章程文件不唯一/缺失: cycles/{gate_id}-*.md 命中 {len(hits)}")
            sys.exit(1)
        charter = hits[0]
    else:
        spec = profile.get(gate_id)
        if not spec:
            print(f"FAIL profile {mode} 无门禁 {gate_id}（可用: {', '.join(profile)}）")
            sys.exit(1)

    # ① frontmatter 完整 + 枚举合法 + version==文件名（全部 WP 实例与 AD）
    wp_files = sorted(root.glob("work-products/*/*.v*.md"))
    ad_files = sorted(root.glob("decisions/AD-*.md"))
    fm_cache = {}
    for p in wp_files + ad_files:
        fm = parse_frontmatter(p.read_text())
        fm_cache[p] = fm
        req = cfg["required_fm_ad"] if p.parent.name == "decisions" else cfg["required_fm_wp"]
        for k in req:
            if not fm.get(k):
                fails.append(f"①{p.relative_to(root)} frontmatter 缺 {k}")
        st = fm.get("status", "")
        if st and not STATUS_RE.match(st):
            fails.append(f"①{p.relative_to(root)} status 非法: {st}")
        mv = re.search(r"\.v(\d+)\.md$", p.name)
        if mv and fm.get("version") and fm["version"] != mv.group(1):
            fails.append(f"①{p.relative_to(root)} frontmatter version={fm['version']} ≠ 文件名 v{mv.group(1)}")
        ds = fm.get("decision_status", "")
        if p.parent.name == "decisions" and ds and ds not in cfg["decision_status_enum"]:
            fails.append(f"①{p.relative_to(root)} decision_status 非法: {ds}")

    # ② 必备 WP 达标（GC: 章程 affected_wps 动态解析）
    scope_files = []
    if spec.get("dynamic_from_charter"):
        cfm = parse_frontmatter(charter.read_text())
        if cfm.get("status") != "open":
            fails.append(f"②章程 {charter.name} status={cfm.get('status')!r} ≠ open（未获批或已关闭）")
        # 覆盖规则（v2）：change 型的 domains 必须全部 baselined；baseline 型豁免；无 kind 视作 v1 章程 grandfather
        ckind = cfm.get("kind", "")
        if ckind == "change":
            cdomains = re.findall(r"[\w-]+", cfm.get("domains", "")) or []
            if not cdomains:
                fails.append(f"②change 型章程 {charter.name} 未声明 domains")
            dm_path, _ = latest(root, cfg["wp_dirs"].get("domain-map", "work-products/00-domain-map"), "domain-map")
            if dm_path is None:
                fails.append("②覆盖规则无从检查：缺 domain-map")
            else:
                coverage = parse_domain_map(dm_path)
                for d in cdomains:
                    if coverage.get(d) != "baselined":
                        fails.append(f"②覆盖规则: 域 {d} coverage={coverage.get(d, '不在台账')} ≠ baselined（先开 baseline 周期）")
        elif ckind == "baseline":
            pass
        else:
            warns.append(f"②章程 {charter.name} 无 kind 字段（v1 格式 grandfather，跳过覆盖规则）")
        awps = parse_affected_wps(charter.read_text())
        if not awps:
            fails.append(f"②章程 {charter.name} affected_wps 为空/不可解析")
        for it in awps:
            wp_dir = cfg["wp_dirs"].get(it["wp"])
            if not wp_dir:
                fails.append(f"②章程引用未知 WP: {it['wp']}")
                continue
            label = f"{it['wp']}{'.' + it['instance'] if it['instance'] else ''}"
            p, n = latest(root, wp_dir, it["wp"], it["target_version"], it["instance"])
            if p is None:
                fails.append(f"②{label} 目标版本 v{it['target_version']} 不存在")
                continue
            scope_files.append(p)
            st = status_base(fm_cache.get(p, parse_frontmatter(p.read_text())).get("status", "draft"))
            if order.get(st, -1) < order.get(it["min_status"], 99):
                fails.append(f"②{p.relative_to(root)} status={st} 低于章程要求 {it['min_status']}")
    else:
        for slug, min_st in spec["requires"].items():
            wp_dir = cfg["wp_dirs"][slug]
            p, n = latest(root, wp_dir, slug)
            if p is None:
                fails.append(f"②必备 WP 缺失: {slug}（{wp_dir}/）")
                continue
            scope_files.append(p)
            fm = fm_cache.get(p) or parse_frontmatter(p.read_text())
            st = status_base(fm.get("status", "draft"))
            if order.get(st, -1) < order.get(min_st, 99):
                fails.append(f"②{p.relative_to(root)} status={st} 低于门禁要求 {min_st}")

    # proposed AD 纪律（按 gate 配置 fail/warn/ignore）
    mode_ad = spec.get("proposed_ad", "warn")
    if mode_ad != "ignore":
        for p in ad_files:
            if fm_cache[p].get("decision_status") == "proposed":
                msg = f"AD 仍为 proposed: {p.relative_to(root)}"
                (fails if mode_ad == "fail" else warns).append(("②" if mode_ad == "fail" else "②") + msg)

    # ③ 阻塞扫描
    ledger_path = root / "LEDGER.md"
    ledger = parse_ledger_blocks(ledger_path.read_text()) if ledger_path.is_file() else {}
    known_oq = {k for k in ledger if k.startswith("OQ-")}
    #   域内 open OQ / blocking OQ 阻断
    for oq, f in ledger.items():
        if not oq.startswith("OQ-") or f.get("status", "open").startswith("closed"):
            continue
        scope = f.get("scope", "")
        if f.get("severity") == "blocking":
            fails.append(f"③blocking 级 OQ 仍 open: {oq}")
        elif scope in (gate_id, "global"):
            fails.append(f"③域内 OQ 仍 open: {oq}（scope={scope}）")
        for k in cfg["required_oq_fields_when_open"]:
            if k not in f:
                fails.append(f"③open OQ 未达决策就绪: {oq} 缺 {k}")
    #   gate 域文件不得残留内联标记；全库 blocked_on ↔ 内联一致；孤儿 OQ
    for p in wp_files + ad_files:
        text = p.read_text()
        inline = set(MARK_BLOCKED.findall(text))
        fm_raw = fm_cache[p].get("blocked_on", "[]")
        fm_list = set(re.findall(r"OQ-\d{3}", fm_raw))
        if inline != fm_list:
            fails.append(f"③{p.relative_to(root)} blocked_on={sorted(fm_list)} ≠ 内联 BLOCKED-ON={sorted(inline)}")
        for oq in set(OQ_REF.findall(text)) - known_oq:
            fails.append(f"③{p.relative_to(root)} 引用 LEDGER 不存在的 {oq}（孤儿）")
    for p in scope_files:
        text = p.read_text()
        for kind, rx in (("BLOCKED-ON", MARK_BLOCKED), ("ASSUMES", MARK_ASSUMES)):
            for oq in rx.findall(text):
                fails.append(f"③域内 {p.relative_to(root)} 残留 [{kind}: {oq}]")

    # ④ INDEX 对账（每个盘上实例有行、version/status 相符；行不指向不存在的文件）
    idx_path = root / "INDEX.md"
    idx_rows = {}
    if idx_path.is_file():
        for line in idx_path.read_text().splitlines():
            mrow = re.match(r"^\|\s*((?:work-products|decisions|cycles)/\S+)\s*\|\s*(\S+)\s*\|\s*v?(\d+)\s*\|\s*(\S+)\s*\|", line)
            if mrow:
                idx_rows[mrow.group(1)] = (mrow.group(3), mrow.group(4))
    else:
        fails.append("④缺 INDEX.md")
    for p in wp_files + ad_files:
        rel = str(p.relative_to(root))
        fm = fm_cache[p]
        if rel not in idx_rows:
            fails.append(f"④INDEX 无 {rel} 行")
        else:
            iv, ist = idx_rows[rel]
            if fm.get("version") and iv != fm["version"]:
                fails.append(f"④INDEX {rel} version={iv} ≠ frontmatter {fm['version']}")
            if fm.get("status") and ist != fm["status"]:
                fails.append(f"④INDEX {rel} status={ist} ≠ frontmatter {fm['status']}")
    for rel in idx_rows:
        if not (root / rel).is_file():
            fails.append(f"④INDEX 指向不存在的文件: {rel}")

    # ⑤ 前置记录（GATE 链 + GC 的 CYC 登记）
    prereq = spec.get("prereq")
    if prereq:
        rec = ledger.get(prereq)
        if not rec:
            fails.append(f"⑤LEDGER 无前置 {prereq} 记录")
        elif rec.get("verdict") not in ("pass", "pass-with-conditions"):
            fails.append(f"⑤前置 {prereq} verdict={rec.get('verdict')!r} 非通过")
    if charter is not None and gate_id not in ledger:
        fails.append(f"⑤LEDGER 无 {gate_id} 开启登记（章程须经 /arch-decide 批准）")
    if ledger.get(f"GATE-{gate_id}"):
        warns.append(f"⑤GATE-{gate_id} 已有记录（重跑门禁？签核前请人知悉）")

    # ⑥ kb 八查（无 kb/ 跳过）
    if (root / "kb").is_dir():
        kb_tool = pathlib.Path(__file__).parent / "kb-index.py"
        r = subprocess.run([sys.executable, str(kb_tool), "--check"], capture_output=True, text=True, cwd=root)
        for line in r.stdout.splitlines():
            if line.startswith("WARN"):
                warns.append("⑥" + line[5:])
        if r.returncode != 0:
            for line in r.stdout.splitlines():
                if line.startswith("FAIL"):
                    fails.append("⑥" + line[5:])
            if not any(f.startswith("⑥") for f in fails):
                fails.append("⑥kb-index.py --check 失败: " + (r.stderr.strip()[:120] or "未知错误"))

    for w in warns:
        print(f"WARN {w}")
    if fails:
        for f in fails:
            print(f"FAIL {f}")
        print(f"== GATE FAIL ({len(fails)} 项) ==")
        sys.exit(1)
    print(f"== GATE PASS ({gate_id} 六查全过；promote_to={spec.get('promote_to')}，晋升由 /arch-gate 在人签核后执行) ==")
    sys.exit(0)


if __name__ == "__main__":
    main()
