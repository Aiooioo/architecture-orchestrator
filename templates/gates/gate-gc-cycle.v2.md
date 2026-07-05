---
version: 2
status: active
supersedes: gate-gc-cycle.v1.md
superseded_by: null
created: 2026-07-05
kind: gate-checklist-template
gate: GC
---
<!-- v2 变更：按章程 kind 分两套对账重点；增 kb/覆盖检查项。/arch-gate 实例化到 gates/GC-CYC-NNN-<date>.md。 -->

<!-- TEMPLATE-BODY -->
# GC(CYC-NNN, kind=<baseline|change>) · 周期出口门禁 — <date>

## 1. 确定性检查（gate.py，含 kb 八查与覆盖规则）

```
<粘贴 python3 tools/gate.py --gate CYC-NNN 输出>
```

## 2. 周期对账

- [ ] 章程"完成判据"逐条对照，达成/未达成如实标注
- [ ] 章程范围外没有被顺手改的 WP/atoms（越权变更 = 涟漪逃逸）
- [ ] affected_wps 之外被波及的引用已闭合或登 LEDGER

## 2a. baseline 型专属（摸底忠实度，承 v1 G0 的灵魂）

- [ ] atoms 描述的是盘上真实存在的东西——sources 锚可指认；现状丑陋如实记录并登 RSK，不美化
- [ ] 推断/存疑断言已标 `^[inferred]` / `^[ambiguous]`；与既有 atom 的矛盾走了 `[!contradiction]` + OQ
- [ ] 域覆盖判据达成：atoms 全 verified、无死链、域 MOC 围栏最新 → **签核后 domain-map 该域翻 baselined**

## 2b. change 型专属

- [ ] 覆盖规则满足（gate.py 已机检；此处人眼复核 domains 列表没漏写实际动到的域）
- [ ] 新增/修改 AD：Assumptions 复核成立；Implications 技术债登 RSK
- [ ] to-be 版本对实现团队自足；evolution-roadmap 已更新

## 3. Viability（释放类强制章节）

- [ ] 本周期交付物的可行性：假设成立 / 风险有 disposition / 无"悬着"的 open RSK 属本周期域

## 4. 评审面板 findings

| 视角 | finding | 严重度 | disposition |
|---|---|---|---|
| | | | |

## 5. 签核请求（/arch-gate 生成，人复述确认）

- **scope**（章程 affected_wps 目标版本）：
- **完成判据对账结果**：
- **未裁 OQ**：
- **建议 verdict**：
- **人签核**：<日期 + 原话>（确认后 LEDGER 落 GATE-CYC-NNN + 章程转 closed，范围内 WP 升 released，domain-map 覆盖行翻转/刷新 last-verified，写本周期 handoff manifest）
