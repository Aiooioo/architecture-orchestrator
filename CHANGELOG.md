# CHANGELOG — 方法演进史（append-only）

## 2026-07-05 · v1 初版建仓

- 方法内核：8 类工作产品（IBM GS Method/UMF 骨架 + C4/Mermaid/ADR 表达）、WP 版本化状态机（`draft → review → baselined@<gate> → released` / `superseded`）、OQ 决策队列 + `[BLOCKED-ON]`/`[ASSUMES]` 押注机制、确定性门禁 gate.py + 人签核双层门。
- 双剖面生命周期：engagement（G1–G3 线性）/ product（G0 摸底 + CYC-NNN 演进周期循环）。
- 投影体系：`templates/project-scaffold/` 为项目仓投影源，`/arch-init`（init|sync）实例化 landing-procedure.v2 双向完整性校验。
- 入口集：中枢 `/arch-init` + 项目仓 `/arch-change` `/arch-decide` `/arch-gate` `/arch-status`（动词键控 MECE）。
- 兼容声明：首版，无旧产物。
