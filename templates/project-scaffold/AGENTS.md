<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/AGENTS.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影；改进回中枢升版后经 /arch-init sync 重投影。
-->

# AGENTS — 架构项目仓治理（结构权威）

> 本仓是一个**架构项目仓**：身份与模式见 `project.yaml`（mode: engagement=项目型线性 | product=产品型周期循环）。
> 方法全文在中枢 system-arch-base（本仓不存路径，需要时问人——LG-015）；**日常操作所需的一切规则已内嵌于本文件与 4 个 skill**，不依赖中枢在场。

## 一、入口路由（4 个，动词键控 MECE）

| 入口 | 动词 | tie-breaker |
|---|---|---|
| `/arch-change` | 推进架构（起草/修订 WP、登记 OQ/RSK、涟漪闭合） | 想"做架构工作"→ 它 |
| `/arch-decide` | 清人决队列（裁 OQ、批 CYC 章程、落裁定+销账） | 想"知道欠我什么决断/裁事"→ 它；刚打开仓库不知道干嘛 → 先它 |
| `/arch-gate` | 过门禁（gate.py + 评审面板 + 签核请求） | "阶段/周期感觉做完了"→ 它 |
| `/arch-status` | 只读查询现状 | "只是问问"→ 它 |

定义层的修改（本文件 / skills / templates / tools）**不属于任何入口**——那是中枢的事，回中枢升版再 sync。

## 二、结构 schema

| 路径 | 层 | 说明 |
|---|---|---|
| `work-products/NN-<slug>/<slug>.vN.md` | 状态 | 8 类 WP 实例（evolution-roadmap 仅 product 模式用） |
| `decisions/AD-NNN-<slug>.md` | 状态 | 架构决策（Decision 字段只能人裁） |
| `cycles/CYC-NNN-<slug>.md` | 状态 | 演进周期章程（product 模式） |
| `gates/<gate>-<date>.md` | 状态 | 门禁实例（checklist + findings + 签核请求） |
| `handoff/manifest-*.yaml` | 状态 | 释放类门禁产出的交接清单（冻结接口） |
| `LEDGER.md` | 状态 | **单一台账**：OQ / RSK / CYC / GATE 记录；"当前阶段"由 GATE 记录推导，不二存 |
| `INDEX.md` / `CHANGELOG.md` / `REPOS.md` | 状态 | 实例登记 / 变更史 / 本项目拓扑 |
| `project.yaml` | 状态（init 后） | 只存身份 + mode + hub_ref 钉，别的不放 |
| `templates/` `tools/` `.claude/skills/` 本文件等 | 定义 | 中枢投影，勿就地改语义；权威清单=中枢 scaffold-manifest.yaml |

## 三、WP 状态机与标记（操作必需的最小集）

- 状态：`draft → review → baselined@<gate> → released`，另有 `superseded`。只前进不后退；要改已 baselined/released 的内容 → 起 `vN+1`。下游只消费 `released`。
- product 模式解读：as-is = 最新 `released`；to-be = 在途 `draft/review/baselined`。
- 内联标记仅两种（大写可 grep）：`[BLOCKED-ON: OQ-NNN]`（推进不了）、`[ASSUMES: OQ-NNN=<选项>]`（押注推进，须反登 LEDGER 该 OQ 的 bets）。WP frontmatter `blocked_on` 与内联 BLOCKED-ON **双向一致**（gate.py 查）。
- LEDGER 条目格式（gate.py 机器解析，**不得改成表格或散文**）：`### <ID> · 标题` + `- key: value` 行。open 的 OQ 必须决策就绪：`severity / scope / options / recommend` 四键齐全。

## 四、红线

1. AD 的 Decision、NFR 优先级、CYC 章程批准、gate 签核——只能出自人的会话内明确确认（复述确认后落笔）。
2. 人未裁的 OQ 保持 open，不得替人猜；押注必须留痕。
3. 涟漪铁律：影响半径内的引用清理在本次变更内完成，做不完的登 LEDGER——不许沉默漂移。
4. 每次变更收尾必登账：INDEX（实例状态）+ CHANGELOG（append 一行）+ LEDGER（新登/销账）。
5. 跨仓引用只用仓库名 + ID/钉版；本机路径运行时问人（LG-015）。
