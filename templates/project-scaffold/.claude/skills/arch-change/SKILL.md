---
name: arch-change
description: 推进架构工作：当你要起草或修订工作产品（system-context/AOD/组件模型/运行模型/NFR/场景/AD/roadmap）、要把新需求新约束落成架构产物、或要开演进周期章程时使用。工作单元是"带影响半径的变更"而非单份文档——含涟漪闭合与 OQ 登记。裁决人决队列用 /arch-decide；过阶段/周期门禁用 /arch-gate；只读查询用 /arch-status。
---
<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/.claude/skills/arch-change/SKILL.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影；改进回中枢升版后经 /arch-init sync 重投影。
触发模式（与其它 skill 互斥）：有具体架构工作要做——起草/修订 WP、落新输入、开周期章程。
-->

# /arch-change — 架构变更（流程操作权威）

> 结构 schema、状态机、标记语法、红线见 `AGENTS.md`（不重复定义；结构从 AGENTS，流程照本 skill 执行）。

## 固定步骤

1. **认领变更 + 挂靠**：确认变更来源（人的输入 / gate 条件 / OQ 裁定的返工 / roadmap 过渡步骤 / domain-map 待摸切片）。
   - product 模式：实质变更必须挂靠一个 `status: open` 的 CYC——没有就先起草章程（`templates/cycles/cycle-charter.v2.md` 实例化，填 `kind: baseline|change` 与 `domains`；change 型先自查覆盖规则：domains 是否全部 baselined，不满足则改提 baseline 型或混合），**停**，提示人走 `/arch-decide` 批准后再继续。
   - engagement 模式：确认变更属于当前阶段（由 LEDGER 最后一条 GATE 推导）；跨阶段的记 OQ 问人。
   - **baseline 型周期的主工作 = 摸底**：源材料是代码/配置/监控，走与 /kb-ingest 相同的四段管线（大范围时 fan-out 只读 `kb-extractor` 按模块切片）产出该域 atoms；as-is WP 域实例（`<slug>.<domain>.vN.md`）在 atoms 就绪后按需起草（叙事视图，引用 atoms 不复述）。

2. **定影响半径**（按规则，不凭感觉）：
   - 目标 WP 本体 + 引用它的其它 WP 章节（按 WP 名/AD 编号/NFR 编号 grep）；
   - 涉及事实变化 → 相关 atoms（经 kb-index.json/graph.json 邻域定位）+ 引用这些 atoms 的 WP 章节；
   - 动组件 → component-model 静态+动态视图 + operational-model 落点 + AOD 构件段；
   - 动 NFR → 引用该 NFR-NNN 的场景/AD/运行模型假设；
   - 动 AD 的 Assumptions → 该 AD 全体 + 其 Implications 波及处。
   - **回显受影响清单给人确认后再动手**（变更琐碎时可省，拿不准不省）。

3. **起草/修订**：
   - 新 WP：从 `templates/work-products/<slug>.v1.md` 实例化（TEMPLATE-BODY 以下为正文，yaml 块为实例 frontmatter），落 `work-products/NN-<slug>/<slug>.v1.md`。
   - 改已 `baselined/released` 的 WP：**起 vN+1**（frontmatter `supersedes` 指旧版；旧版此时不动，待新版升 released 时才标 `superseded`）。
   - 改 `draft/review` 的 WP：就地改，`updated` 刷新。
   - AD：实例化到 `decisions/AD-NNN-<slug>.md`；agent 只写到 Recommendation，**Decision 留给人**（decision_status: proposed）。

4. **不确定点三档处置**（见 AGENTS §三/§四）：能押注 → `[ASSUMES: OQ-NNN=X]` + LEDGER 反登 bets；推进不了 → `[BLOCKED-ON: OQ-NNN]` + frontmatter `blocked_on`；方向性问题 → severity: blocking，当场问人。所有 OQ 按决策就绪格式登 LEDGER（四键齐全）。

5. **涟漪闭合铁律**：步骤 2 清单内所有引用在**本次变更内**清理完毕；当场做不完的登 LEDGER（RSK 或 OQ）——不许沉默漂移。

6. **轻量自查**（抓形不抓义，深评审在 gate 面板）：frontmatter 完整、version==文件名、blocked_on↔内联一致、无死链、引导注释在 review 前已删。可跑 `python3 tools/gate.py --gate <下一个 gate>` 提前看缺口（fail 是常态，只看清单）。

7. **销账登记**（必做）：INDEX.md（每个动过的实例一行，version/status 同步）+ CHANGELOG.md（append 一行：日期/改了什么/影响哪些产物）+ LEDGER（新登/销账）；**触碰过 atoms 则必跑 `python3 tools/kb-index.py`**（完成定义，FAIL=未完成）。收尾输出摘要：动了哪些文件、登了哪些 OQ/RSK、下一步建议。

## 红线

- 不碰定义层（templates/ tools/ .claude/ AGENTS 等）——诉求登 LEDGER，回中枢处理。
- 不替人裁决（AD Decision / NFR 优先级 / 章程批准）。
- 不写实现代码——那是实现仓的事，架构产物到 handoff 为止。
