---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: wp-template
wp: nfr-catalog
---
<!-- 实例化说明同 system-context 模板。 -->

```yaml
---
wp: nfr-catalog
version: 1
status: draft
supersedes: null
superseded_by: null
blocked_on: []
created: <date>
updated: <date>
generated_from: system-arch-base@<commit>/templates/work-products/nfr-catalog.v1.md
---
```

<!-- TEMPLATE-BODY -->
# NFR Catalog — <系统名>

> 读者：全员。回答"多好才算够"。分类沿 ISO 25010。铁律：**写不出可度量指标的 NFR 不收**（"高性能"不是需求，是愿望）。优先级是人的裁定——agent 起草时一律先标 `proposed`，经 gate/OQ 裁定后转正。

## NFR 条目

<!-- product 模式加"现状实测"列（摸底时填）。验证方式：负载测试/混沌演练/审计/监控告警阈值等。 -->

| ID | 分类（ISO 25010） | 陈述 | 可度量指标 | 优先级（must/should/could） | 现状实测（product） | 验证方式 |
|---|---|---|---|---|---|---|
| NFR-001 | performance-efficiency | <如：搜索接口在常规负载下快速响应> | <P95 < 300ms @ 100 rps> | must (proposed) | | <负载测试> |
| NFR-002 | reliability | | | | | |

<!-- 分类速查：functional-suitability / performance-efficiency / compatibility / usability(interaction-capability) /
     reliability / security / maintainability / portability(flexibility) / safety。 -->

## 取舍记录

<!-- NFR 之间打架（一致性 vs 可用性、性能 vs 成本）时：冲突写在这，裁定走 AD/OQ，此处放指针。 -->

| 冲突 | 涉及条目 | 裁定 |
|---|---|---|
| | | AD-NNN / OQ-NNN |
