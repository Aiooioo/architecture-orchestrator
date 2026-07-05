---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: wp-template
wp: key-scenario
---
<!-- 实例化说明同 system-context 模板。 -->

```yaml
---
wp: key-scenario
version: 1
status: draft
supersedes: null
superseded_by: null
blocked_on: []
created: <date>
updated: <date>
generated_from: system-arch-base@<commit>/templates/work-products/key-scenario.v1.md
---
```

<!-- TEMPLATE-BODY -->
# Key Scenarios — <系统名>

> 读者：架构师自己 + 实现团队。只收 **architecturally significant** 的场景：它要么压强某条 must 级 NFR，要么穿过多个组件边界，要么代表最大业务价值路径。一般 3–7 个——超过说明没选出"关键"。每个 must 场景必须在 component-model 动态视图有对应时序（DoD 联动）。

## SCN-001 · <场景名>

- **触发者**：
- **前置条件**：
- **主流程**：
  1.
  2.
- **压强的 NFR**：NFR-NNN（为什么这个场景对它是压力测试）
- **priority**：must | should
- **架构显著性一句话**：<它为什么配进这个清单>

## SCN-002 · <场景名>

<!-- 同上结构。异常流只在"异常处理本身架构显著"时写（如补偿事务、降级路径）。 -->
