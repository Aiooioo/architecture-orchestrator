---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: gate-checklist-template
gate: GC
---
<!-- /arch-gate 实例化到项目仓 gates/GC-CYC-NNN-<date>.md。周期出口门（释放类）：
     必备项由章程 affected_wps 动态解析（gate.py --gate CYC-NNN）。 -->

<!-- TEMPLATE-BODY -->
# GC(CYC-NNN) · 周期出口门禁 — <date>

## 1. 确定性检查（gate.py）

```
<粘贴 python3 tools/gate.py --gate CYC-NNN 输出>
```

## 2. 周期对账

- [ ] 章程"完成判据"逐条对照，达成/未达成如实标注
- [ ] 章程范围外**没有**被顺手改的 WP（越权变更 = 涟漪逃逸；确有必要 → 补进章程升版或起新周期）
- [ ] affected_wps 之外被本周期波及的引用已闭合或登 LEDGER

## 3. Viability（对本周期变更）

- [ ] 新增/修改的 AD：Assumptions 复核成立；Implications 中的技术债已登 RSK
- [ ] to-be 版本对实现团队自足（同 G3 判据）
- [ ] evolution-roadmap 已更新（滚动记录 + gap 消化情况）

## 4. 评审面板 findings

| 视角 | finding | 严重度 | disposition |
|---|---|---|---|
| | | | |

## 5. 签核请求（/arch-gate 生成，人复述确认）

- **scope**（章程 affected_wps 的目标版本）：
- **完成判据对账结果**：
- **未裁 OQ**：
- **建议 verdict**：
- **人签核**：<日期 + 原话>（确认后 LEDGER 落 GATE-CYC-NNN + 章程转 closed，范围内 WP 升 released 并 supersede 旧版，写本周期 handoff manifest）
