---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: wp-template
wp: evolution-roadmap
---
<!-- product 模式专属。唯一跨周期滚动维护的 WP：每次 GC 门禁后更新，不随周期冻结。
     版本语义特殊：它的 vN 升版 = 方向的重大调整，日常滚动更新属于勘误级就地修订。 -->

```yaml
---
wp: evolution-roadmap
version: 1
status: draft
supersedes: null
superseded_by: null
blocked_on: []
created: <date>
updated: <date>
generated_from: system-arch-base@<commit>/templates/work-products/evolution-roadmap.v1.md
---
```

<!-- TEMPLATE-BODY -->
# Evolution Roadmap — <产品名>

> 读者：Chief Architect + 产品干系人。TOGAF gap 分析 + 过渡架构的轻量版：回答"现状与目标差在哪、按什么顺序走过去"。它孕育 CYC 章程（每个过渡步 ≈ 一个未来周期的候选）。

## 1. 目标态一句话

<!-- 北极星：一段话描述架构要演进成什么样、为什么。 -->

## 2. Gap 清单

<!-- 每个 gap 必须可溯源（DoD）：指向具体 WP 章节 / NFR 条目 / RSK 条目。凭感觉的 gap 不收。 -->

| Gap ID | 现状（as-is 溯源） | 目标（to-be） | 严重度 | 溯源 |
|---|---|---|---|---|
| GAP-001 | | | | NFR-NNN / RSK-NNN / <WP §> |

## 3. 过渡步骤

<!-- 步骤间依赖显式；每步注明"完成判据"。已开周期的步骤填 CYC 编号。 -->

| 步骤 | 覆盖的 Gap | 依赖 | 完成判据 | 对应周期 |
|---|---|---|---|---|
| 1. <标题> | GAP-001 | — | | CYC-001 / （未开） |

## 4. 排序理由

<!-- 为什么是这个顺序：风险前置/价值前置/依赖倒逼……一段话 + 必要的 AD 指针。 -->

## 5. 滚动记录

<!-- 每次 GC 后 append 一行：日期 / 本周期消化了哪些 gap / 新增哪些 gap。 -->

| 日期 | 周期 | 消化 | 新增 |
|---|---|---|---|
| | | | |
