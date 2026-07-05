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

## 待决

（无）
