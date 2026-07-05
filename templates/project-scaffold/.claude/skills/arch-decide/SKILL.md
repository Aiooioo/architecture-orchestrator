---
name: arch-decide
description: 清空人的决断队列：当你说"有什么要我决定的""裁决""清队列"、要批准演进周期章程、或刚打开仓库想知道下一步时使用。读取 LEDGER 全部 open 的 OQ（含待批 CYC 章程），逐条以 2-4 个选项端给人决断，收集后落地裁定并做涟漪销账。要做架构起草/修订用 /arch-change；过门禁用 /arch-gate；只读查询用 /arch-status。
---
<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/.claude/skills/arch-decide/SKILL.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影；改进回中枢升版后经 /arch-init sync 重投影。
触发模式（与其它 skill 互斥）：人要清 LEDGER 里等他裁的事（OQ 队列 + proposed 章程）。
-->

# /arch-decide — 决断队列协作

> 本 skill 负责**清人的决断队列**。落地动作复用 `/arch-change` 的涟漪纪律。LEDGER 条目格式见 `AGENTS.md` §三。

## 步骤

1. 读 `LEDGER.md`「待人决断」区 + `cycles/` 里 `status: proposed` 的章程，按严重度排序列摘要（每条 ≤2 行），先让人选**本次清哪几条**（可以只清一条）。

2. 对选中的每一条：
   - 给背景（涉及 WP 相对路径 + 问题本质，≤5 行）；
   - 用 AskUserQuestion 给 2–4 个具体选项（推荐项放第一位并标理由）；允许"跳过，下次再说"；
   - **AD 类**（OQ 指向某 AD 的 Decision）：选项即 alternatives；人裁后填 AD 的 Decision + Justification（人的原话为准），decision_status → decided；
   - **章程类**：选项为 approve / approve-with-changes / defer / reject；approve 后章程 status → open，LEDGER 登 `### CYC-NNN` 块（status: open / charter: / approved: 日期）。

3. 全部收集后**复述一遍决断清单**让人确认，再执行。

4. 执行落地（每条）：
   - LEDGER 该 OQ → `status: closed(=<选项>)`，移入「已关闭」区；
   - **涟漪销账**：按 OQ id 全库 grep——`[BLOCKED-ON: OQ-NNN]` 处按裁定补内容删标记、frontmatter `blocked_on` 同步；`[ASSUMES: OQ-NNN=X]` 押对删标记、押错修正内容（当场改不完 → 登新 LEDGER 条目，绝不沉默）；
   - INDEX / CHANGELOG 登账。

5. 收尾：输出清账摘要——裁了 N 条、落盘文件清单、剩余队列长度（open OQ X · proposed 章程 Y · open RSK Z）。

## 红线

- 人未明确决断的条目保持 open，不得替人猜。
- 决策性文本（AD Decision / 章程批准）**逐字念给人确认后才写入**。
