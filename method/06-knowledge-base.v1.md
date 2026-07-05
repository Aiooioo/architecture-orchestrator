---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
updated: 2026-07-05
---

# 06 · 架构知识库（knowledge base）

> 项目仓的**事实层**：Obsidian 原生的 markdown vault，承载"系统里有什么、谁连谁、部署在哪、哪里有债"这类可盘点事实。观点层（WP/AD，人签核的判断与叙事）建在其上、按 wikilink 引用它。设计渊源：Karpathy LLM Wiki（增量编译、索引优先、矛盾显式）+ 2026 Obsidian agent-KB 实践（wikilink 图谱、MOC、Bases、断言级溯源）+ 本生态组合律（事实只存一份、投影生成、确定性守卫）。

## 1. 三层模型

```
观点层  WP 文档 + AD          人签核 · 走门禁 · 引用 atom
投影层  MOC 围栏块 · Bases 视图 · kb-index.json/graph.json    生成 · 勿手改
事实层  kb/atoms/<domain>/<kind>-<slug>.md                    SoT · 单写者
```

事实与判断分离的原因：事实不需要签核，只需要新鲜度语义（`observed | verified | stale`）；判断必须人裁。同一事实**不得**在 WP 里复述展开——WP 引用并给出判断（冻结接口精神）。

## 2. 目录与 atom schema

```
kb/
├── _meta/taxonomy.md          # 受控词表（状态层，见 §3）
├── _meta/kb-index.json        # 生成：平铺表 + facet 倒排
├── _meta/graph.json           # 生成：类型化邻接表
├── _raw/                      # ingest 暂存（不算知识，可清理）
├── atoms/<domain>/<kind前缀>-<slug>.md
├── mocs/domain-<name>-moc.md · plane-<name>-moc.md
└── bases/*.base               # Obsidian Bases 实时视图（定义层投影）
```

atom frontmatter（kb-index.py 机器解析，必填：id/kind/domain/planes/status/last-verified/summary）：

```yaml
id: CMP-0012                # 前缀见 taxonomy kinds，三/四位零填充，只增不复用
kind: component
domain: billing             # 物理主轴（目录名 = 此值）
planes: [application, data] # 逻辑 facet，多值
summary: 一句话（索引 cheap-pass 用）
aliases: [invoice-svc]
status: verified            # observed(agent 摸到) | verified(有证据钉) | stale(超龄)
last-verified: 2026-07-05
sources: [backend/services/invoice/]   # 证据锚：代码路径/配置/监控/文档
writes: ["[[sto-orders]]"]  # typed edge = 含 wikilink 的字段，词表见 taxonomy edges
```

正文纪律：一段话事实陈述 + 自由 `[[wikilink]]` 互链；推断/存疑断言标 `^[inferred]` / `^[ambiguous]`（摸底忠实度的断言级落点）；与既有 atom 冲突用 `[!contradiction]` callout 显式标记并登 OQ，**不静默改写**。slug 全库唯一（lint 查重），wikilink 一律指 slug。

## 3. taxonomy 治理

`kb/_meta/taxonomy.md` 是受控词表（planes / kinds+ID 前缀 / edge 类型 / tags）。**planes 与 kinds 的增改是方法级决策**（回中枢 LEDGER 记 MD，随升版下发）；tags 与 edge 细分项目内可增（记项目 CHANGELOG）。lint 对越界词表 fail。初始 planes：`business / application / data / deployment / enterprise`；初始 kinds：component(CMP) / interface(IFC) / datastore(STO) / dataflow(FLW) / deployment-node(NOD) / capability(CAP) / debt(DBT) / constraint(CST)。

## 4. 读取协议（所有 skill 与会话通用；出口是协议，不是入口）

- **Tier 0 直读**（已知条目、≤3 跳）：`kb-index.json` summary cheap-pass → 直读目标 atom → 必要时沿 typed edge 走一两跳。禁止全库扫描式 grep。
- **Tier 1 委派 `kb-retriever`**（开放式/多跳问题）：只读 subagent 在独立上下文走 index → graph 邻域 → 正文，回传压缩 digest + 逐条 `[[atom]]` 引用。
- retriever 三条硬约束：只读；**每条结论带 atom 引用，库中没有就明说，禁止训练常识补位**；不做取舍判断（指回 OQ/AD）。

## 5. 写入协议（单写者纪律）

只有入口 skill 的主 agent 写 vault；一切 subagent（extractor/retriever/评审面板）只读。ingest 四段管线（Ingest→Extract→Resolve→Write-back）是共享能力：`/kb-ingest`（外来材料）与 `/arch-change`（摸底周期，源=代码/配置/监控）共用一份实现；材料大时 Extract 段 fan-out 只读 extractor，各回传结构化候选，主 agent 合并落盘。

**完成定义（M1）**：任何触碰 atoms 的入口收尾必跑 `python3 tools/kb-index.py`（重建索引/图 + 刷新 MOC 围栏 + lint）；lint FAIL = 本次工作未完成。

## 6. lint 八查（kb-index.py，确定性）

① 死链（wikilink 无对应 slug）② 词表越界（kind/plane/edge）③ 必填 frontmatter 缺失 / id-slug 重复 / alias 冲突 ④ 孤儿 atom（无入边且无 MOC 收录，warn）⑤ 陈旧（last-verified 超阈值，warn，gate 可升级）⑥ `[!contradiction]` 引用的 OQ 不在 LEDGER ⑦ 索引/图与盘上 frontmatter 漂移（--check 模式）⑧ MOC 围栏块漂移。机器查形；语义质量（事实对不对）归摸底忠实度与评审面板。

## 7. 与门禁/覆盖的挂钩

- gate.py 第⑥查 = 调用 `kb-index.py --check`（项目无 kb/ 时跳过——engagement 仓可不建 KB）。
- domain-map 覆盖判据挂 atoms：`mapped` = 域目录有 atoms；`baselined` = 该域 atoms 全 `verified` + 无死链 + 域 MOC 围栏最新（经 baseline 周期 GC 签核后翻转）；`stale` = 超龄 atom 占比过阈值。
- MOC 的策展叙事部分随汇报需要自由写；围栏块（`<!-- kb:generated:start/end -->`）只由 kb-index.py 刷新。

## 8. 刻意不做（AD 级裁定，动机见中枢 LEDGER MD-009）

图数据库/Obsidian 专有插件依赖/MCP server（跨应用共享时再议）/文件锁（单写者已结构性消灭并发写）/`wiki-query` 式检索入口（检索是工具不是目的）。
