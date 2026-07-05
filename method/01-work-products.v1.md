---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
updated: 2026-07-05
---

# 01 · 工作产品目录（work products）

> 8 类工作产品（WP）。每类：它回答什么问题 / DoD（完成定义）/ RACI。所有 WP 实例放项目仓 `work-products/NN-<slug>/<slug>.vN.md`，模板见中枢 `templates/work-products/`。
> RACI 统一为：**Agent = Responsible（起草、修订、自查），Human = Accountable（签核）**；下表只标注每类 WP 额外的人裁点。

## WP-1 `system-context`（系统上下文）

- **回答**：系统边界在哪？谁在用它、它依赖谁？为什么立项（brief）？
- **内容**：engagement brief（目标/范围/干系人/约束/时间盒）+ C4 L1 上下文图 + actors 与外部系统清单（含每条交互的方向与契约性质）。
- **DoD**：每个 actor/外部系统有一行职责描述；范围外事项显式列出（out-of-scope）；brief 的成功判据可度量。
- **人裁点**：范围（in/out）与成功判据。

## WP-2 `architecture-overview`（架构总览 AOD）

- **回答**：整体长什么样？一张图能否给新人讲清系统？
- **内容**：总览图（C4 L2 容器级或自由形式）+ 每个构件一段职责说明 + 关键技术选型指针（指向对应 AD）。
- **DoD**：图中每个元素在正文有说明；每项技术选型都有 AD 编号可溯。
- **人裁点**：（经 AD 间接裁定，无独立裁点）

## WP-3 `component-model`（组件模型）

- **回答**：静态——有哪些组件、各自职责与接口？动态——关键场景下它们如何协作？
- **内容**：C4 L3 组件图 + 组件职责/接口表 + 每个 key-scenario 一张 Mermaid sequence。
- **DoD**：每个组件有单一职责陈述；每条组件间依赖有接口说明；覆盖全部 `key-scenario` 中 priority=must 的场景。
- **人裁点**：（经 AD 间接裁定）

## WP-4 `operational-model`（运行模型）

- **回答**：部署到哪、怎么连、怎么活下来（可用性/容量/运维）？
- **内容**：部署拓扑 Mermaid 图（节点/区域/连接）+ 环境矩阵（dev/staging/prod 差异）+ 容量与可用性假设。
- **DoD**：component-model 中每个组件都有部署落点；每条跨区连接标注协议与安全边界。
- **人裁点**：成本敏感的部署选型（经 AD）。

## WP-5 `nfr-catalog`（非功能需求目录）

- **回答**：这个系统"好"的标准是什么，多好才算够？
- **内容**：按 ISO 25010 分类的 NFR 条目（`NFR-NNN`）：陈述 / 可度量指标 / 优先级（must/should/could）/ 验证方式。product 模式加"现状实测"列。
- **DoD**：每条 must 级 NFR 的指标可度量、可验证；无"高性能""高可用"式空话。
- **人裁点**：优先级排序是人的裁定（gate 时集中确认）。

## WP-6 `key-scenario`（关键场景）

- **回答**：哪些用例在架构上是决定性的（architecturally significant）？
- **内容**：场景卡片：触发者 / 前置条件 / 主流程步骤 / 涉及的 NFR / priority。
- **DoD**：每张卡片能独立读懂；数量克制（一般 3–7 个，多了说明没选出"关键"）。
- **人裁点**：哪些场景算"关键"。

## WP-7 `architectural-decision`（架构决策 AD）

- **回答**：面对一个架构问题，考虑过什么，选了什么，为什么，代价是什么？
- **内容**：`decisions/AD-NNN-<slug>.md`，IBM AD 全字段：Issue / Assumptions / Motivation / Alternatives（每项含利弊）/ Decision / Justification / Implications。
- **DoD**：至少 2 个 alternatives 且各有真实利弊（没有稻草人）；Implications 写明这个决定"买了什么、欠了什么"。
- **人裁点**：**Decision 字段只能由人裁定**（agent 准备 alternatives + 推荐，经 OQ 队列或 gate 由人拍板）。这是本方法最硬的一条人裁线。

## WP-8 `evolution-roadmap`（演进路线图，product 模式）

- **回答**：as-is 与 to-be 的差距是什么，按什么顺序、什么过渡态走过去？
- **内容**：gap 清单（现状 vs 目标，按 WP 溯源）+ 过渡步骤（每步对应未来的 CYC 候选）+ 排序理由。
- **DoD**：每个 gap 可溯源到具体 WP 章节或 RSK/NFR 条目；步骤间依赖显式。
- **人裁点**：演进优先级。
- **特性**：唯一**跨周期滚动维护**的 WP——每次 GC 门禁后更新，不随周期冻结。

## 不设为 WP 的三样东西（MD-005）

| 经典产物 | 归宿 |
|---|---|
| RAID Log | Risks/Dependencies/技术债 → 项目 LEDGER `RSK-NNN`；Assumptions → AD 字段；Issues → `OQ-NNN` |
| Viability Assessment | G0/G3/GC 门禁 checklist 的强制章节 |
| 评审报告 | `/arch-gate` 评审面板的 findings 直接落 gate 实例文件 + 语义问题登 OQ |
