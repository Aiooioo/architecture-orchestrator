---
name: arch-init
description: 中枢唯一入口——把架构方法投影进项目仓：当你要新建一个架构项目/产品仓（init），或要把中枢的模板/规程/技能更新同步到既有项目仓（sync）时使用。只在 system-arch-base 中枢仓运行。项目内的起草/裁决/门禁/查询不归它管——去项目仓用 /arch-change /arch-decide /arch-gate /arch-status。
---

# /arch-init — 投影器（init | sync，landing-procedure.v2 的实例）

> 投影纪律见中枢 `AGENTS.md` §五。定义层/状态层的权威清单 = `templates/project-scaffold/scaffold-manifest.yaml`（下称 manifest）。

## Step 0 · 准备（两模式通用）

1. 确认当前在中枢仓根目录，且**工作树 clean**（否则钉版无意义）——不 clean 就停，请人先提交。
2. 取钉：`HUB=system-arch-base@$(git rev-parse --short HEAD)`。
3. **问人目标路径**（LG-015：不猜、不硬编码、不从历史记录复用）。
4. 判模式：目标不存在或为空目录 → **init**；目标含 `project.yaml`（有 `hub_ref:`）→ **sync**；其它情况（有文件但不是项目仓）→ 停，问人。

## init 模式

1. 问人：项目名（kebab-case）、mode（engagement=有起止的项目型 / product=长周期产品型，判据："做完就散"选前者、"做完还要养"选后者）。
2. 建目录，`git init -b main`。
3. 按 manifest 投影：
   - `definition` 每项：复制 source → target，把文件内 `generated_by: system-arch-base@<commit>` 的 `<commit>` 占位替换为真实钉（仅此一处替换，正文逐字不动）；
   - `state_seed` 每项：复制并填充占位符 `{{PROJECT_NAME}}` `{{MODE}}` `{{HUB_COMMIT}}` `{{DATE}}`；
   - `state_dirs` 每项：`mkdir -p` + `.gitkeep`。
4. **完整性校验（2a）**：对每个 definition target，`规范化 diff`（双方剥去含 `generated_by:` 的行后 diff）必须为空；非空 = 复制出错，修复后重验。
5. 项目仓首次提交：`init(<项目名>): 由 ${HUB} 投影初始化（mode=<mode>）`。
6. **中枢侧登记**：在中枢 `REPOS.md`「项目仓登记」表加一行（名称/mode/日期/active）；提示人中枢也需提交。
7. 收尾输出：项目路径、mode、钉版、下一步指引（进项目仓读 HUMAN-GUIDE，engagement → `/arch-change` 起草 system-context；product → `/arch-change` 开始摸底）。

## sync 模式

1. 读目标 `project.yaml` 的 `hub_ref` 旧钉（`OLD`）。
2. **漂移预检（2a 前半：抓"就地改语义"）**：对每个 definition target，规范化对比 目标现有文件 vs `git show ${OLD#*@}:<source>`；**非空 diff = 项目仓被就地改过** → 🔴 停，逐文件列出漂移，交人裁决（合法出路只有两条：改动有价值 → 先回中枢升版；改动无价值 → 同意被覆盖）。人未裁不得继续。
3. 快照状态层基线：`git -C <目标> status` 须 clean（不 clean 请人先提交——这是 2b 的对账基线）。
4. 重投影：definition 每项复制覆盖 + 重打新钉；`state_seed`/`state_dirs` **一律不动**。
5. 更新目标 `project.yaml` 的 `hub_ref` 为新钉（该文件此行是唯一合法触碰的状态层内容）。
6. **双向完整性校验**：
   - (2a) 每个 definition target 规范化 diff vs 中枢现源 = 空；
   - (2b) `git -C <目标> diff --name-only` 的文件集 ⊆ {definition targets} ∪ {project.yaml}——出现任何状态层文件（LEDGER/INDEX/work-products/decisions/cycles/gates/handoff/README/REPOS/CHANGELOG）即 🔴 停并回滚。
7. 项目仓提交：`sync: 定义层重投影 ${OLD} → ${HUB}`；输出变更文件清单 + 提示（若 gate-config 语义有变，建议项目跑一次 `python3 tools/gate.py --gate <当前门>` 看新缺口）。

## 红线

- 部署 = 逐字复制 + 占位替换，**绝不在投影过程中"顺手改进"**——发现 scaffold 不满足需要，停下来回中枢升版（本仓 CHANGELOG/INDEX 同步），再投影。
- 状态层永不覆盖；2a/2b 任一不过 = 落地未完成，不得报成功。
- 目标路径每次运行时问人；不写进任何文件（REPOS.md 只记名称）。
