<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/HUMAN-GUIDE.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影。
-->

# HUMAN GUIDE — 你只做三件事

你是 Chief Architect。agent 起草一切、自查一切、打包一切；**你的全部工作只有三件**：

## 1. 裁决 —— `/arch-decide`

打开仓库不知道干嘛时，敲这个就对了。它列出所有等你裁的事（OQ 队列 + 待批的周期章程），每条给 2–4 个选项和推荐，你选，它落地并把涟漪清干净。

- 遇到 agent 当场问你的"blocking"问题：那是方向性大事，值得停下来想。
- 你没裁的事 agent 不会替你决定——最多押注（留痕、可回滚）。

## 2. 签核 —— `/arch-gate`

阶段或周期感觉做完了就敲它。机器检查 + 4 视角评审面板跑完后，它给你一份签核请求（完成度/发现的问题/风险）。你说 pass / pass-with-conditions（带条件）/ fail。

- 你批准的是**工作产品的版本**，不用逐段确认。
- 有没裁完的问题它会先把你带回 `/arch-decide`。

## 3. 给输入

新需求、新约束、事故、想法——直接在会话里说，agent 会经 `/arch-change` 落成工作产品的变更，拿不准的自动进 OQ 队列等你裁。

---

**看进度**：`/arch-status`（当前阶段/周期、在途工作、欠你几条裁决）。
**别做的事**：不要直接改 `templates/` `tools/` `.claude/` 和 AGENTS/CLAUDE/HUMAN-GUIDE（它们是中枢投影，改了会被 sync 覆盖；诉求让 agent 登记后回中枢改）。
