# CHANGELOG — 方法演进史（append-only）

## 2026-07-05 · v1 初版建仓

- 方法内核：8 类工作产品（IBM GS Method/UMF 骨架 + C4/Mermaid/ADR 表达）、WP 版本化状态机（`draft → review → baselined@<gate> → released` / `superseded`）、OQ 决策队列 + `[BLOCKED-ON]`/`[ASSUMES]` 押注机制、确定性门禁 gate.py + 人签核双层门。
- 双剖面生命周期：engagement（G1–G3 线性）/ product（G0 摸底 + CYC-NNN 演进周期循环）。
- 投影体系：`templates/project-scaffold/` 为项目仓投影源，`/arch-init`（init|sync）实例化 landing-procedure.v2 双向完整性校验。
- 入口集：中枢 `/arch-init` + 项目仓 `/arch-change` `/arch-decide` `/arch-gate` `/arch-status`（动词键控 MECE）。
- 兼容声明：首版，无旧产物。

## 2026-07-05 · 勘误：gate.py project.yaml 解析

- 剥引号与行内注释（arch-demo 端到端干跑发现）；勘误级，不升版。验证记录：engagement 全链路（G1 拦截→裁决→PASS→签核→G2 前置链）+ product GC 动态章程解析 + sync 双向守卫（漂移预检/2a/2b）均通过。

## 2026-07-05 · v2：渐进式摸底 + 架构知识库（事实层）+ 接口层

- **渐进式摸底**（method/02.v2）：G0 重构为 bootstrap 门（domain-map + 产品级 system-context，签"划分与负空间"）；摸底以 baseline 型周期按域切片进行；change 型周期受覆盖规则约束（domains 必须 baselined，gate.py 机检）；域覆盖状态/新鲜度入 domain-map（WP-9，滚动文档）。
- **知识库**（method/06.v1）：三层模型（事实 atoms / 生成投影 / 签核观点）；Obsidian 原生存储（wikilink typed edges、MOC 策展+围栏生成、Bases 实时视图、受控词表、断言级溯源、矛盾 callout→OQ）；tools/kb-index.py 八查为确定性守卫；gate.py 升六查。
- **接口层**：新增项目仓入口 /kb-ingest（四段管线）；kb-retriever/kb-extractor 只读 subagent；分层读取协议 + 单写者纪律入 AGENTS；检索刻意不设入口（EF-10）。
- **兼容声明：提供迁移**。① 既有项目仓：/arch-init sync 定义层 + 一次性加性迁移（建 kb/{atoms,mocs,_raw}、播 kb/_meta/taxonomy.md、product 仓补 domain-map 实例；项目内旧 v1 模板文件属显式退役，可删）。② v1 时代的全量 G0 记录仍有效（= "一次摸完全部域"特例，域覆盖可按其 scope 回填 baselined）。③ 无 kind 的 v1 章程 grandfather：gate.py 跳过覆盖规则并 WARN，建议下个周期起用 charter v2。
