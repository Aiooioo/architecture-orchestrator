---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: wp-template
wp: architectural-decision
---
<!-- 实例化到 decisions/AD-NNN-<slug>.md（不放 work-products/，AD 是多实例一等目录）。
     这是本方法最重要的教学模板：IBM AD 表格是现代 ADR 的前身，字段比 ADR 多且更严格。
     人机分工红线：Alternatives/Justification 由 agent 准备，Decision 只能人裁（decision_status 才能转 decided）。 -->

```yaml
---
wp: architectural-decision
ad: AD-001
version: 1
status: draft
decision_status: proposed   # proposed | decided | superseded；decided 只能经人裁定产生
supersedes: null
superseded_by: null
blocked_on: []
created: <date>
updated: <date>
generated_from: system-arch-base@<commit>/templates/work-products/architectural-decision.v1.md
---
```

<!-- TEMPLATE-BODY -->
# AD-001 · <决策标题：一句话说清"选了什么">

## Issue（问题）

<!-- 面对的架构问题是什么。好的 Issue 不预设答案："如何在多可用区间保持会话？"而非"要不要用 Redis？" -->

## Assumptions（假设）

<!-- 本决策成立所依赖的前提，每条可被证伪。前提翻了 = 触发本 AD 复议（这就是 IBM 把 Assumptions 设为一等字段的原因）。 -->

-

## Motivation（动因）

<!-- 为什么现在必须决策：哪个 NFR/场景/约束逼出来的（放指针）。 -->

## Alternatives（备选方案）

<!-- ≥2 个真实备选，禁止稻草人。每个备选的利弊都要真诚——评审面板会专查这一点。 -->

### A) <方案>
- 利：
- 弊：

### B) <方案>
- 利：
- 弊：

## Recommendation（agent 推荐）

<!-- agent 的推荐 + 一行理由。这不是 Decision——只是给人裁定的输入。 -->

## Decision（裁定）

<!-- 只能由人裁定后填写（经 /arch-decide 或 gate 复述确认）。未裁时留空 + [BLOCKED-ON: OQ-NNN] 或 [ASSUMES: OQ-NNN=X]。 -->

## Justification（裁定理由）

<!-- 为什么选它而不是其它备选——这是未来复议时最值钱的字段。 -->

## Implications（影响）

<!-- 这个决定"买了什么、欠了什么"：连带的技术债（登 RSK-NNN）、被约束的后续决策、受影响的 WP 章节。 -->

-
