---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: gate-checklist-template
gate: G1
---
<!-- /arch-gate 实例化到项目仓 gates/G1-<date>.md。三层门禁的第 2 层载体：
     gate.py 结果 → 面板 findings → 签核请求，全记在实例里。 -->

<!-- TEMPLATE-BODY -->
# G1 · context 出口门禁 — <date>

## 1. 确定性检查（gate.py）

```
<粘贴 python3 tools/gate.py --gate G1 输出>
```

## 2. 语义 checklist（agent 自查 + 面板复核）

- [ ] out-of-scope 显式且非空——"什么都做"不是范围
- [ ] 每条 must 级 NFR 的指标可度量（抽 3 条读：能写成监控告警阈值吗？）
- [ ] key-scenario 数量克制（3–7），每个的"架构显著性一句话"成立
- [ ] 干系人表里有决策权列，且至少一人能对范围说"不"
- [ ] brief 成功判据与 NFR 目录不互相矛盾

## 3. 评审面板 findings

<!-- 4 视角并行运行（perspectives/），此处汇总。disposition ∈ fixed（机械问题当场修）| OQ-NNN | RSK-NNN。 -->

| 视角 | finding | 严重度 | disposition |
|---|---|---|---|
| | | | |

## 4. 签核请求（/arch-gate 生成，人复述确认）

- **scope**（本次冻结的 WP 版本）：
- **完成度摘要**：
- **未裁 OQ**（应为空，否则 gate 拒绝出此请求）：
- **建议 verdict**：pass | pass-with-conditions（条件列出） | fail
- **人签核**：<日期 + 原话>（确认后 LEDGER 落 GATE-G1，WP 升 baselined@G1）
