---
name: arch-status
description: 只读查询项目现状：当你问"到哪了""现在什么阶段""欠我什么""上次干了什么"时使用。只读 LEDGER/INDEX/CHANGELOG/project.yaml 推导汇报，不改任何文件。要干活用 /arch-change；要裁决用 /arch-decide；要过门禁用 /arch-gate。
---
<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/.claude/skills/arch-status/SKILL.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影；改进回中枢升版后经 /arch-init sync 重投影。
触发模式（与其它 skill 互斥）：只想了解现状，不做任何变更。
-->

# /arch-status — 只读状态报告

## 步骤

1. 读 `project.yaml`（name/mode/hub_ref）+ `LEDGER.md` + `INDEX.md` + `CHANGELOG.md` 最近几条。**不读不必要的 WP 正文，不改任何文件。**

2. 推导并汇报（简洁，一屏内）：
   - **当前位置**：LEDGER 最后一条 GATE 记录 + mode → engagement 报"当前阶段"；product 报"baseline 状态 + 在途周期（open CYC）+ baseline 年龄（GATE-G0 距今）"；
   - **在途工作**：INDEX 中 status ∈ draft/review 的实例；product 模式加报 as-is（released）/ to-be（在途）分布；
   - **欠人的账**：open OQ 数（blocking 单列）+ proposed 章程数 → 提示 `/arch-decide`；
   - **风险敞口**：open RSK 数与最重一条；
   - **最近动态**：CHANGELOG 最近 2–3 行；
   - **下一步建议**：一句话（如"清 2 条 OQ 后可试 G2"）。

3. 发现台账互相矛盾（INDEX vs frontmatter、GATE 链断裂）→ 如实报告并建议跑 `python3 tools/gate.py` 定位，**不顺手修**（修改属 /arch-change）。
