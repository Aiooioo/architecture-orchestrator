---
name: kb-ingest
description: 喂材料进架构知识库（事实层）：当你说"把这份材料吃进去/入库"，给出事故报告、厂商文档、会议纪要、监控截图、一段口述现状时使用。走 Ingest→Extract→Resolve→Write-back 四段管线产出 atoms，只动 kb/ 事实层不动工作产品。要做架构判断/动 WP 用 /arch-change（摸底周期的代码盘点也在那）；问知识不用任何入口（读取协议直接答）；裁决用 /arch-decide。
---
<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/.claude/skills/kb-ingest/SKILL.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影；改进回中枢升版后经 /arch-init sync 重投影。
触发模式（与其它 skill 互斥）：人给了一份外来材料要沉淀进事实层。
-->

# /kb-ingest — 材料入库（四段管线）

> atom schema、taxonomy、单写者纪律见 `AGENTS.md` §KB；模板在 `templates/kb/atom.v1.md`。

## 固定步骤

1. **Ingest**：材料落 `kb/_raw/<date>-<slug>/`（原样暂存，不算知识）；确认材料讲的是哪些域（对照 domain-map；提到台账外的新域 → 先补 domain-map 一行 unmapped，这是负空间纪律）。

2. **Extract**：从材料提取候选 atoms（实体/关系/断言）。材料大（>数百行或多文件）时**fan-out 只读 `kb-extractor` subagent**（按章节/模块切），各回传结构化候选（拟 id/kind/domain/planes/summary/edges/sources + 断言列表含 inferred/ambiguous 标注）；主 agent 只接摘要，不整卷加载。

3. **Resolve**（对照 `kb/_meta/kb-index.json` 逐条裁决去向）：
   - 新事实 → 新 atom（id 取该前缀下一号；slug 全库唯一）；
   - 命中既有 atom（slug/alias 或语义同一）→ 增量更新该 atom（补 sources、刷 last-verified、必要时 status 升 verified）；
   - **与既有 atom 矛盾 → 不静默改写**：在既有 atom 加 `[!contradiction]` callout + 登 OQ（决策就绪四键，scope=global 或所属域的下一个 gate）；
   - 与 taxonomy 冲突（新 kind/plane 诉求）→ 停，登 OQ 提示回中枢走方法级决策。

4. **Write-back**（单写者：只有本 skill 主 agent 落笔）：写/改 atoms；材料证据锚写进 `sources`；正文断言按忠实度标 `^[inferred]` / `^[ambiguous]`。

5. **收尾（完成定义，不可省）**：跑 `python3 tools/kb-index.py`（重建索引/图 + 刷新 MOC 围栏 + 八查）——FAIL = 本次未完成，修到绿；CHANGELOG append 一行（入库了什么、产出/更新几个 atoms、登了几条 OQ）；输出摘要 + 若材料暗示架构判断待做（如"该拆了"），建议接 `/arch-change`。

## 红线

- 只动 `kb/`（及 LEDGER 登 OQ/RSK、CHANGELOG 登账）；不碰 work-products/decisions——那是 /arch-change 的地界。
- 不做取舍判断；材料里的观点作为断言记录并标注来源，不转写成"事实"。
- subagent 一律只读。
