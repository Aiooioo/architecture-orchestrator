---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: gate-checklist-template
gate: G0
---
<!-- /arch-gate 实例化到项目仓 gates/G0-<date>.md。product 模式入场门（engagement 棕地可选）。
     释放类：签核后 as-is WP 直升 released（"现状真相"确立）。 -->

<!-- TEMPLATE-BODY -->
# G0 · baseline 摸底门禁 — <date>

## 1. 确定性检查（gate.py）

```
<粘贴 python3 tools/gate.py --gate G0 输出>
```

## 2. 摸底忠实度（本门禁的灵魂：as-is 必须是"现状"，不是"愿望"）

- [ ] as-is WP 描述的是**盘上真实存在**的东西——每个组件/连接可指认到代码/配置/基础设施证据
- [ ] 现状的丑陋如实记录（临时方案/单点/裸奔连接），**不美化**；每处丑陋登 RSK 或注明"接受"
- [ ] nfr-catalog 的"现状实测"列有数据来源（监控/压测/事故记录），无实测的显式标"未测"
- [ ] 技术债清单（RSK）与 as-is WP 互相引用可溯

## 3. Viability（对"演进底座"的可行性）

- [ ] 摸底覆盖面足以支撑第一个演进周期的规划（不要求 100% 覆盖——未摸的区域显式列为 RSK）
- [ ] evolution-roadmap 初版（gap 可以粗，但溯源要实）

## 4. 评审面板 findings

| 视角 | finding | 严重度 | disposition |
|---|---|---|---|
| | | | |

## 5. 签核请求（/arch-gate 生成，人复述确认）

- **scope**：
- **未摸区域（如实列出）**：
- **未裁 OQ**：
- **建议 verdict**：
- **人签核**：<日期 + 原话>（确认后 LEDGER 落 GATE-G0，as-is WP 升 released，产品进入周期循环）
