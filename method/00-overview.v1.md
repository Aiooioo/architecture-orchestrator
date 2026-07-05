---
version: 1
status: deprecated
supersedes: null
superseded_by: 00-overview.v2.md
created: 2026-07-05
updated: 2026-07-05
---

# 00 · 方法总纲（overview）

## 1. 这是什么

一套面向**人机协作时代**的软件架构工作方法：工作产品的分类学承自 IBM 咨询体系的经典骨架（GS Method / Unified Method Framework / RUP 时代），表达方式换成现代轻量记法（C4 模型、Mermaid、ADR），执行方式重构为 **agent 起草 + 人在决策点裁定**。

三条设计公理：

1. **工作产品是活文档**，生命周期记在版本与状态里，不记在目录位置里。
2. **agent 不替人做架构决策**——不确定就登记（OQ），可押注（ASSUMES）但必须留痕、可回滚。
3. **门禁双层**：确定性检查（gate.py，机器）+ 签核（人），缺一不算过。

## 2. IBM 渊源 → 本方法映射

| IBM/TOGAF 经典 | 本方法落地 | 说明 |
|---|---|---|
| System Context（GS Method） | `system-context` 模板 | 并入 engagement brief（立项要素），C4 L1 |
| Architecture Overview Diagram | `architecture-overview` 模板 | 自由总览 + C4 L2 |
| Component Model（静态+动态） | `component-model` 模板 | C4 L3 + Mermaid sequence |
| Operational Model（LOM/SOM/POM） | `operational-model` 模板 | v1 轻量化为单级部署拓扑；分级留作模板 v2 演进 |
| Non-Functional Requirements | `nfr-catalog` 模板 | ISO 25010 分类 + 可度量指标 |
| Architecturally Significant Use Cases | `key-scenario` 模板 | 场景卡片，驱动组件动态模型 |
| Architectural Decisions（AD 表格，ADR 前身） | `architectural-decision` 模板 | ADR 编号 + IBM 全字段 |
| Gap Analysis / Transition Architecture（TOGAF E/F）、IBM 转型路线图 | `evolution-roadmap` 模板 | product 模式的方向持有文档 |
| Current IT Environment / TOGAF Baseline Architecture | `00-baseline` 摸底阶段 | as-is 工作产品 + G0 签核 |
| RAID Log | 项目 LEDGER 的 `RSK-NNN` + AD 假设字段 + `OQ-NNN` | 不设独立文件（MD-005） |
| Viability Assessment / TDA 评审 | 释放类门禁 checklist 强制章节 + 评审面板 | 并入路径（MD-004/005） |
| 阶段评审（Solution Outline → Macro Design） | 双剖面生命周期 + G0/G1/G2/G3/GC 门禁 | 见 `02-lifecycles-and-gates.v1.md` |

## 3. 双剖面选型（初始化时二选一）

| | engagement（项目型） | product（产品型） |
|---|---|---|
| 适用 | 有明确目标、起止日期的一次性架构交付 | 长周期 SaaS 产品的持续架构演进 |
| 入场 | 直接 `01-context`（棕地可选先做 `00-baseline`） | **必经** `00-baseline` 摸底 |
| 编排 | 线性：01→G1→02→G2→03→G3，G3 后项目终结 | 循环：G0 后以 `CYC-NNN` 演进周期为单位 |
| 交接 | G3 一次性 blueprint 包 | 每周期 GC 产出该周期的变更包 |
| 方向文档 | （不需要） | `evolution-roadmap` 滚动维护 |

判据拿不准时：**"做完就散"选 engagement，"做完还要一直养"选 product。**

## 4. 与 agents-orchestrator 的边界（C1–C4 答卷）

见 `AGENTS.md` §一。一句话：本仓是 architecture-method 域的独立 SoT，与 workflow-engine 域显式正交；已在其 registry 组合关系表登记；未来若需把本方法纳入 engine 管理，走其 `ef-define` 入场检查，本仓整体降为该 scenario 的定义源。

## 5. 阅读顺序

`01-work-products`（产出什么）→ `02-lifecycles-and-gates`（何时产出、如何过关）→ `03-collaboration-protocol`（人与 agent 怎么分工）→ `04-notation-and-style`（写成什么样）→ `05-glossary`（术语）。
