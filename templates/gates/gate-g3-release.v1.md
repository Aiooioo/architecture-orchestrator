---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: gate-checklist-template
gate: G3
---
<!-- /arch-gate 实例化到项目仓 gates/G3-<date>.md。释放类门禁：含 viability 强制章节（MD-005），签核后产出 handoff manifest。 -->

<!-- TEMPLATE-BODY -->
# G3 · assure-and-release 出口门禁 — <date>

## 1. 确定性检查（gate.py）

```
<粘贴 python3 tools/gate.py --gate G3 输出>
```

## 2. Viability Assessment（强制章节，IBM 可行性评估的落点）

- [ ] **技术可行**：每个 decided AD 的 Assumptions 逐条复核仍成立；存疑的列出
- [ ] **风险归并**：LEDGER 全部 open RSK 逐条给出 disposition（接受/缓解/移交实现仓），无"悬着"
- [ ] **交付可行**：blueprint 对实现团队自足——不依赖"问架构师才知道"的口头上下文
- [ ] **PoC 对账**：凡 AD 里承诺过验证的（spike/PoC），有结果记录或降级为显式假设

## 3. 语义 checklist

- [ ] 范围内 WP 全部达到 baselined，无 `[BLOCKED-ON]`/`[ASSUMES]` 残留
- [ ] AD 无 proposed 残留（要么 decided 要么显式移交下游）
- [ ] handoff manifest 草案完整（路径/版本/状态/钉版/gate 引用）

## 4. 评审面板 findings

| 视角 | finding | 严重度 | disposition |
|---|---|---|---|
| | | | |

## 5. 签核请求（/arch-gate 生成，人复述确认）

- **scope**：
- **完成度摘要**：
- **未裁 OQ**：
- **建议 verdict**：
- **人签核**：<日期 + 原话>（确认后 LEDGER 落 GATE-G3，范围内 WP 升 released，写 handoff/manifest.yaml，engagement 项目终结）
