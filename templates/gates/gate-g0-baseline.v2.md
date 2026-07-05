---
version: 2
status: active
supersedes: gate-g0-baseline.v1.md
superseded_by: null
created: 2026-07-05
kind: gate-checklist-template
gate: G0
---
<!-- v2 变更：G0 从"全量摸底门"重构为 bootstrap 门——只签"划分方式与负空间"，
     现状真相按域经 baseline 型周期逐步确立。/arch-gate 实例化到 gates/G0-<date>.md。 -->

<!-- TEMPLATE-BODY -->
# G0 · bootstrap 门禁（建索引，不是建全书）— <date>

## 1. 确定性检查（gate.py）

```
<粘贴 python3 tools/gate.py --gate G0 输出>
```

## 2. 划分合理性（本门禁的灵魂）

- [ ] domain-map 划分依据成文且自洽（业务能力/团队/数据所有权，不混用无说明）
- [ ] **负空间显式**：所有已知域都在台账里，包括打算长期不摸的（附可接受理由）
- [ ] 域间关系表足以计算任一域的摸底最小闭包（strong 依赖无缺漏的明显嫌疑）
- [ ] 产品级 system-context：产品边界、核心 actors、out-of-scope 清楚

## 3. 摸底策略

- [ ] 首刀选择有真实诉求倒逼（不是"从左到右按目录摸"）
- [ ] 覆盖台账初始状态如实（unmapped/mapped 与 kb 实况一致；此时通常尚无 baselined）

## 4. 评审面板 findings

| 视角 | finding | 严重度 | disposition |
|---|---|---|---|
| | | | |

## 5. 签核请求（/arch-gate 生成，人复述确认）

- **scope**：domain-map.v1 + system-context.v1
- **未裁 OQ**：
- **建议 verdict**：
- **人签核**：<日期 + 原话>（确认后 LEDGER 落 GATE-G0，二者升 baselined@G0，产品进入周期循环）
