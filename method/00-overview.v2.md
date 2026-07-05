---
version: 2
status: active
supersedes: 00-overview.v1.md
superseded_by: null
created: 2026-07-05
updated: 2026-07-05
---

# 00 · 方法总纲（overview）· v2

## 1. 这是什么

一套面向**人机协作时代**的软件架构工作方法：工作产品分类学承自 IBM 咨询体系经典骨架（GS Method / UMF / RUP 时代），表达换成现代轻量记法（C4、Mermaid、ADR、Obsidian 原生 wiki），执行重构为 **agent 起草 + 人在决策点裁定**。

四条设计公理（v2 增第 4 条）：

1. **工作产品是活文档**——生命周期在版本与状态里，不在目录位置里。
2. **agent 不替人做架构决策**——不确定就登记（OQ），可押注（ASSUMES）但留痕可回滚。
3. **门禁双层**——确定性检查（机器）+ 签核（人），缺一不算过。
4. **事实与判断分离**——事实层（kb atoms，可盘点可陈旧）单写者生长；观点层（WP/AD，人签核）引用不复述。

## 2. IBM/经典渊源 → 本方法映射

| 经典 | 本方法落地 |
|---|---|
| System Context / AOD / Component Model / Operational Model / NFR / 关键用例 / AD 表格 | WP-1…WP-7 模板（详见 method/01.v2，承 v1） |
| Gap Analysis / Transition Architecture（TOGAF E/F） | WP-8 evolution-roadmap |
| **TOGAF Architecture Repository / Landscape** | **WP-9 domain-map + kb 事实层（method/06）** |
| Current IT Environment / Baseline Architecture | G0 bootstrap + baseline 型周期（渐进式，method/02.v2） |
| RAID / Viability | LEDGER RSK / 释放类门禁强制章节（MD-005） |
| 阶段评审 | G0/G1/G2/G3/GC 门禁 |
| （非 IBM）Karpathy LLM Wiki + 2026 Obsidian agent-KB 实践 | kb 存储层与 ingest/检索协议（method/06） |

## 3. 双剖面选型（初始化时二选一）

| | engagement（项目型） | product（产品型） |
|---|---|---|
| 适用 | 有目标、起止日期的一次性交付 | 长周期 SaaS 持续演进 |
| 入场 | 直接 `01-context`（棕地可选 baseline 周期） | **G0 bootstrap**（domain-map + 产品级 system-context，一两天） |
| 编排 | 线性 01→G1→02→G2→03→G3 | `CYC-NNN` 周期循环：baseline 型摸切片 / change 型做演进，覆盖规则防在盲区决策 |
| 摸底 | 可选、一次性 | **渐进式**：摸到哪改到哪，永不要求全貌 |
| 交接 | G3 一次性 blueprint 包 | 每周期 GC 变更包 |
| 方向/覆盖文档 | （不需要） | evolution-roadmap + domain-map 滚动维护 |

判据："做完就散"选 engagement，"做完还要养"选 product。

## 4. 与 agents-orchestrator 的边界

同 v1（AGENTS.md §一）：本仓是 architecture-method 域独立 SoT，显式正交，已登记其 registry 组合关系表。

## 5. 阅读顺序

`01-work-products.v2`（产出什么）→ `02-lifecycles-and-gates.v2`（何时产出、如何过关）→ `03-collaboration-protocol.v1`（人机分工）→ `06-knowledge-base.v1`（事实层怎么长）→ `04-notation-and-style.v1`（写成什么样）→ `05-glossary.v2`（术语）。
