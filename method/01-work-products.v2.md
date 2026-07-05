---
version: 2
status: active
supersedes: 01-work-products.v1.md
superseded_by: null
created: 2026-07-05
updated: 2026-07-05
---

# 01 · 工作产品目录（work products）· v2

> 相对 v1 的变更：新增 **WP-9 `domain-map`**（渐进式摸底的覆盖台账）；声明 WP 与事实层（kb atoms，method/06）的关系。WP-1…WP-8 的定义/DoD/RACI 承袭 v1 原文（继续有效，不重复），本文件只载增量。

## WP 与事实层的关系（新）

WP/AD 是**观点层**：判断、取舍、叙事，人签核。kb atoms 是**事实层**：可盘点、可验证、可陈旧。纪律：

- WP 引用事实必须 `[[wikilink]]` 到 atom，**不复述展开**（复述 = rival 副本，违 C3）。
- WP 的 DoD 隐含"其引用的 atoms 处于 `verified`"——引用 observed/stale atom 的 WP 章节视为待验证（评审面板专查）。
- product 模式下 as-is WP 域实例是"该域 atoms 的叙事视图"，可在域 atoms 就绪后低成本起草。

## WP-9 `domain-map`（领域地图与覆盖台账，product 模式核心）

- **回答**：产品划分为哪些域？域之间什么关系？每个域我们**知道多少、多新鲜**？
- **内容**：域清单（bounded context 粒度）+ 关系列（上下游/共享数据，用于计算摸底最小闭包）+ 覆盖台账表（每域一行：`coverage: unmapped|mapped|baselined|stale` / `last-verified` / atoms 计数 / 域 MOC 指针）。
- **DoD**：**负空间显式**——没摸过的域也必须出现在表里；覆盖状态与 kb 实况一致（`mapped`=域目录有 atoms；`baselined`=经 baseline 周期 GC 签核；`stale`=超龄比例过阈值，由 kb-index 判据支撑）。
- **人裁点**：域的划分方式（G0 签核的核心语义）；重新划分 = 升大版本。
- **特性**：滚动文档（同 evolution-roadmap，见 method/02.v2 §3）；覆盖台账表为 gate.py 机器解析（行格式固定，勿改列序）。
- **机器契约**：表行 `| <domain> | <coverage> | <last-verified> | <atoms数> | <moc 链接> |`。
