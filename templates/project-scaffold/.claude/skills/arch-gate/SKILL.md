---
name: arch-gate
description: 过阶段/周期门禁：当阶段（context/design/release/baseline 摸底）或演进周期感觉做完了、要冻结成果并请人签核时使用。三层顺序固定：gate.py 确定性检查 → 强制 4 视角评审面板 → 人签核落 LEDGER；释放类门禁（G0/G3/GC）签核后产出 handoff manifest。有未决 OQ 会被拒并转 /arch-decide；要继续改产物用 /arch-change；只读查询用 /arch-status。
---
<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/.claude/skills/arch-gate/SKILL.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影；改进回中枢升版后经 /arch-init sync 重投影。
触发模式（与其它 skill 互斥）：一个阶段/周期到出口，要过门禁拿签核。
-->

# /arch-gate — 门禁（三层，顺序固定，缺一不过）

> 门禁语义（verdict/批准粒度/晋升规则）已编码在 `tools/gate-config.json` 与本 skill；背景见中枢 method/02。

## 步骤

1. **定门**：由 LEDGER 最后一条 GATE 记录 + `project.yaml` mode 推导本次该过哪个门（engagement: G1→G2→G3；product: G0→GC(CYC-NNN)）。GC 需指明周期号。与人确认。

2. **第一层 · 确定性检查**：`python3 tools/gate.py --gate <G0|G1|G2|G3|CYC-NNN>`。
   - FAIL 项含"域内 OQ 仍 open"→ **停**，转引 `/arch-decide` 清账后重跑；
   - 其它 FAIL → 逐项修（机械问题直接修，语义问题登 OQ/RSK 后按上一条处理）；
   - 全绿才进第二层。

3. **第二层 · 评审面板（强制，作者≠审查者）**：
   - 从 `templates/gates/gate-<gate>.v1.md` 实例化 `gates/<gate>-<date>.md`，粘贴 gate.py 输出，过语义 checklist；
   - **并行委派 4 个只读 subagent**（Task/Agent 工具），提示词分别用 `templates/gates/perspectives/{security,performance,operability,data}.md` + 本次 gate 范围文件清单；
   - findings 汇总进 gate 实例：mechanical → 当场修（重跑 gate.py 确认仍绿）；semantic → 登 OQ/RSK；**视角间冲突不调停，自动登 OQ**；
   - 新登了域内 OQ → 回到步骤 2 的拒绝逻辑（先 `/arch-decide`）。

4. **第三层 · 签核请求**：在 gate 实例里生成——scope（冻结的 WP 版本清单）/ 完成度摘要 / findings 处置 / 建议 verdict。**复述给人**，人给 verdict：
   - `pass`：直接落账；
   - `pass-with-conditions`：条件逐条登 OQ（needs 人裁）或 RSK（needs agent，带 due），落账；
   - `fail`：记录缺口，回 `/arch-change`，本次不落 GATE 记录。

5. **落账与晋升**（仅 pass 类）：
   - LEDGER 登 `### GATE-<gate>` 块（date/verdict/conditions/scope）；GC 同时把章程与 LEDGER 的 CYC 块转 closed；
   - 按 gate-config `promote`/`promote_to` 晋升 WP 状态（frontmatter + INDEX 同步；升 released 时把被 supersede 的旧版标 `superseded`）；
   - **释放类门禁（promote_to=released）**：从 `templates/gates/handoff-manifest.yaml` 生成 `handoff/manifest-<gate>-<date>.yaml`（纯清单，引用 GATE 记录，无二次审批语义）；product 模式提醒更新 evolution-roadmap 滚动记录；
   - CHANGELOG append；输出收尾摘要（过了什么门、晋升了什么、交接物在哪、下一步）。

## 红线

- 三层顺序不可跳、面板不可省——哪怕"就差一点点"。
- 签核记录只能在人会话内明确确认后落笔；agent 不得自签。
- gate.py 与 checklist 冲突时以 gate.py 为准，checklist 缺陷登 LEDGER 回流中枢。
