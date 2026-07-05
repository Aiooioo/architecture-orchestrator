---
version: 2
status: active
supersedes: 05-glossary.v1.md
superseded_by: null
created: 2026-07-05
updated: 2026-07-05
---

# 05 · 术语表（glossary）· v2

| 术语 | 英文 | 定义 |
|---|---|---|
| 工作产品 | Work Product (WP) | 架构工作的一类标准化产出物，本方法定义 8 类 |
| 方法中枢 | method hub | 本仓库：方法定义与投影源的 SoT |
| 项目仓 | project repo | 每个架构项目/产品一个，由 `/arch-init` 从中枢投影初始化 |
| 剖面 | profile / mode | 生命周期编排的两种形态：engagement（项目型）/ product（产品型） |
| 摸底 | baseline assessment | product 模式入场动作：逆向产出 as-is WP 并经 G0 确立"现状真相" |
| 演进周期 | evolution cycle (CYC) | product 模式的工作单位：章程获批 → 变更 → GC 门禁 |
| 门禁 | gate | 阶段/周期出口：gate.py（机器）+ 评审面板（agent）+ 签核（人）三层 |
| 签核 | sign-off | 人在会话内复述确认后落 LEDGER 的 `GATE-*` 记录 |
| 基线化 | baselined | WP 版本经 gate 人签核后的状态，`baselined@<gate>` |
| 释放 | released | 可被下游（实现仓）消费的终态；as-is 真相 |
| 决策队列 | OQ queue | agent 登记、人裁决的开放问题队列（LEDGER `OQ-NNN`） |
| 押注 | bet / ASSUMES | agent 在未裁 OQ 上按推荐选项继续推进的留痕机制 `[ASSUMES: OQ-NNN=X]` |
| 阻塞标记 | BLOCKED-ON | 无法押注时的内联标记，gate 前必须清除 |
| 涟漪闭合 | ripple closure | 变更/裁决后，影响半径内所有引用在本次内清理完毕（或显式登账） |
| 架构决策 | Architectural Decision (AD) | IBM AD 表格传统 + ADR 编号的决策记录；Decision 字段只能人裁 |
| 评审面板 | review panel | gate 内强制运行的 4 视角只读 subagent（security/performance/operability/data） |
| 交接清单 | handoff manifest | 释放类 gate 产出的纯清单（路径+版本+状态+钉版），下游按引用消费，无审批语义 |
| 冻结接口 | frozen interface | 跨仓消费契约：只引用特定 status 的产物，不复述不自存副本 |
| 投影 | projection | 定义层文件从中枢到项目仓的逐字复制，带 `generated_by` 钉版 |
| 定义层 / 状态层 | definition / state layer | sync 可覆盖的 vs 项目自有、永不覆盖的文件集（清单见 scaffold-manifest.yaml） |
| 双向完整性校验 | two-way integrity check | sync 收尾：投影侧无漂移 + 状态侧只有保全/加性 |
| 台账 | LEDGER | 单一决策/风险/周期/门禁记录文件；"当前阶段"由其推导 |
| 方向持有文档 | direction-holding doc | evolution-roadmap：唯一跨周期滚动维护的 WP |
| 组合律 | composition law (C1–C4) | 生态母不变量：单一 SoT / 投影或接口 / 无 rival 权威 / 联合 MECE |
| 事实层 / 观点层 | fact / judgment layer | kb atoms（可盘点可陈旧）vs WP/AD（人签核的判断）；引用不复述 |
| 原子条目 | atom | 事实层最小单元：一个架构事实一个文件，frontmatter 承载全部坐标 |
| 领域地图 | domain-map (WP-9) | 域划分 + 覆盖台账（unmapped/mapped/baselined/stale + last-verified），负空间显式 |
| 渐进式摸底 | progressive baseline | G0 只建索引；baseline 型周期按需摸切片；摸到哪改到哪 |
| bootstrap 门 | G0 (v2) | 签核语义="划分方式与负空间被人认可"，非全量现状确立 |
| 周期类型 | cycle kind | baseline（摸切片）/ change（做演进）；覆盖规则：change 域必须已 baselined |
| 域实例 | domain instance | WP 的域切片文件 `<slug>.<domain>.vN.md`，章程 affected_wps 以 instance 指定 |
| 受控词表 | taxonomy | kb/_meta/taxonomy.md：planes/kinds/edges 枚举；planes/kinds 增改=方法级决策 |
| MOC | Map of Content | 每组织轴一张策展页：叙事自由写 + 围栏块由 kb-index.py 生成 |
| Bases 视图 | Obsidian Bases | .base 声明式实时表格视图，人侧筛选浏览，无生成漂移 |
| 分层读取协议 | tiered reading protocol | Tier0 直读（index cheap-pass→atom→边遍历）/ Tier1 委派 kb-retriever |
| 单写者纪律 | single-writer discipline | 只有入口 skill 主 agent 写 vault，一切 subagent 只读 |
| 断言级溯源 | claim-level provenance | 正文断言标 ^[inferred] / ^[ambiguous]，摸底忠实度的微观落点 |
| 矛盾标注 | contradiction callout | [!contradiction] 显式标记 + 登 OQ，不静默改写 |
| kb 八查 | kb lint | kb-index.py 确定性检查：死链/词表/必填/孤儿/陈旧/OQ 引用/索引漂移/围栏漂移 |
