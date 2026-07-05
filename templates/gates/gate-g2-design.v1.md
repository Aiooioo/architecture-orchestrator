---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: gate-checklist-template
gate: G2
---
<!-- /arch-gate 实例化到项目仓 gates/G2-<date>.md。 -->

<!-- TEMPLATE-BODY -->
# G2 · design 出口门禁 — <date>

## 1. 确定性检查（gate.py）

```
<粘贴 python3 tools/gate.py --gate G2 输出>
```

## 2. 语义 checklist（agent 自查 + 面板复核）

- [ ] AOD 图中每个元素在正文有职责说明；每项技术选型有 AD 编号
- [ ] component-model 覆盖全部 must 级 key-scenario 的时序
- [ ] operational-model 给 component-model 每个组件安排了落点
- [ ] 全部 must 级 NFR 已有人裁定（无 proposed 残留）
- [ ] 每个 decided 的 AD：alternatives ≥2 且无稻草人、Implications 非空
- [ ] 静态/动态视图互证：时序图里出现的组件都在静态图里，反之亦然

## 3. 评审面板 findings

| 视角 | finding | 严重度 | disposition |
|---|---|---|---|
| | | | |

## 4. 签核请求（/arch-gate 生成，人复述确认）

- **scope**：
- **完成度摘要**：
- **未裁 OQ**：
- **建议 verdict**：
- **人签核**：<日期 + 原话>（确认后 LEDGER 落 GATE-G2，WP 升 baselined@G2）
