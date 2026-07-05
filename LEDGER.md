# LEDGER — 方法级决策台账（MD-NNN）

> 记录 architecture-method 域的方法设计决策（不是项目决策——项目决策在各项目仓自己的 LEDGER）。格式：`### MD-NNN · 一句话` + status / date / decision / why。

## 已决

### MD-001 · 本仓定位为 architecture-method 独立域 SoT，不作 agents-orchestrator 的投影
- status: decided
- date: 2026-07-05
- decision: 独立 SoT + 全面继承生态共享惯例（版本化 / 投影 / LEDGER / gate / LG-015）；在 orchestrator registry 登记为显式正交。
- why: 方法域与 workflow-engine 域内容不重叠（C1 可分）；作投影会把方法演进耦合进 engine 升版节奏。保留未来经 ef-define 迁移为 scenario 的可能。

### MD-002 · 项目仓按工作产品组织目录，不按阶段组织
- status: decided
- date: 2026-07-05
- decision: `work-products/NN-<name>/<name>.vN.md`，生命周期在 frontmatter status，gate 冻结"版本@状态"而非目录。
- why: WP 是活文档，阶段目录会迫使"改已封目录"或"复制前滚"（违 C3）；且 WP 中心布局是 product 模式长周期演进的必要基座。

### MD-003 · 生命周期收敛为双剖面：engagement 3 阶段 / product 摸底+周期循环
- status: decided
- date: 2026-07-05
- decision: 砍掉独立的 00-intake（并入 System Context 的 brief 章节）与 03-decision 阶段（AD 随设计累积、gate 时集中裁）；product 模式以 CYC-NNN 为工作单位。
- why: AI 速度下 intake 是半天工作量、决策与设计天然交错；"保障"类工作归入释放前门禁。

### MD-004 · 评审能力不设独立入口，降为 /arch-gate 的强制内部面板
- status: decided
- date: 2026-07-05
- decision: security/performance/operability/data 四视角只读 subagent 面板在 gate 内必跑；视角冲突自动登记 OQ，不由 agent 调停。
- why: 生态实证（EF-10/M1）：可选的独立评审入口会被静默跳过；守卫须强制+正交+在路径上+独立（作者≠审查者）。

### MD-005 · RAID 与 Viability 不单独成文件
- status: decided
- date: 2026-07-05
- decision: Risks/Dependencies/技术债 → 项目 LEDGER `RSK-NNN`；Assumptions → AD 模板字段；Issues → `OQ-NNN`；Viability → 释放类门禁（G3/GC/G0）checklist 强制章节。
- why: 独立 RAID 文件与 LEDGER 构成 rival 台账（违 C3）；单人架构师无独立可行性评审会，并入门禁更在路径上。

### MD-006 · 4 个项目技能的真相只存 scaffold 一份
- status: decided
- date: 2026-07-05
- decision: `arch-change/decide/gate/status` 的 SKILL.md 存于 `templates/project-scaffold/.claude/skills/`（投影源）；中枢 `.claude/skills/` 只放 `arch-init`。
- why: 中枢与 scaffold 各存一份必然漂移（违 C3）；这些技能也不该在中枢会话被触发。

### MD-007 · product 剖面重构为渐进式摸底
- status: decided
- date: 2026-07-05
- decision: G0 瘦身为 bootstrap 门（签"划分与负空间"）；摸底 = baseline 型周期按域切片；change 型周期受覆盖规则机检约束；domain-map（WP-9）为覆盖台账（滚动文档）。
- why: 复杂 SaaS 的全量摸底是大爆炸式前置成本；Karpathy LLM Wiki 的增量编译思路 + 生态 frontier 负空间模式证明"索引先行、按需生长"可行。摸到哪改到哪，但绝不在盲区做设计决策。

### MD-008 · 事实层/观点层分离 + Obsidian 原生存储
- status: decided
- date: 2026-07-05
- decision: kb atoms（事实，单写者、新鲜度语义）与 WP/AD（判断，人签核）分离；存储采用 Obsidian 原生约定——wikilink typed edges、MOC（策展+围栏生成）、Bases 实时视图、受控词表、断言级溯源 ^[inferred]、[!contradiction]→OQ。
- why: 架构知识是 plane×domain 矩阵，文件树单轴不够——单一物理主轴（domain）+ facet + 生成投影守 C1/C3；2026 Obsidian agent-KB 实践证明 wikilink 图谱人机两用，Bases 消灭视图漂移。

### MD-009 · KB 刻意不采用的技术（AD 级裁定）
- status: decided
- date: 2026-07-05
- decision: 不用图数据库/Obsidian 专有插件依赖/MCP server/文件锁/wiki-query 式检索入口。
- why: 单机+git 可 diff+确定性可校验前提下，markdown+生成式 JSON 索引帕累托最优；图库引入不可 diff 的第二真相（违 C3）；单写者纪律结构性消灭并发写；检索是工具不是目的（EF-10）。MCP 留作跨应用场景可选项。

### MD-010 · KB 接口设计四原则
- status: decided
- date: 2026-07-05
- decision: 入口=skill 动词（新增 /kb-ingest，共 5 项目入口）；能力=入口内部管线（ingest 四段两入口共享一份实现）；并发与隔离=只读 subagent（extractor/retriever/panel）；检索=分层协议非入口。
- why: MECE 治入口不治能力（EF-10）；守卫焊进完成定义（M1：触 atoms 必跑 kb-index.py）；单写者防冲突。

## 待决

（无）
