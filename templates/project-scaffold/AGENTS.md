<!--
generated_by: system-arch-base@<commit>/templates/project-scaffold/AGENTS.md
真相源（勿就地改语义）：方法中枢 system-arch-base。本文件是其投影；改进回中枢升版后经 /arch-init sync 重投影。
-->

# AGENTS — 架构项目仓治理（结构权威）

> 本仓是一个**架构项目仓**：身份与模式见 `project.yaml`（mode: engagement=项目型线性 | product=产品型周期循环）。
> 方法全文在中枢 system-arch-base（本仓不存路径，需要时问人——LG-015）；**日常操作所需的一切规则已内嵌于本文件与 4 个 skill**，不依赖中枢在场。

## 一、入口路由（5 个，动词键控 MECE）

| 入口 | 动词 | tie-breaker |
|---|---|---|
| `/kb-ingest` | 喂材料进事实层（atoms） | "把这份材料吃进去/入库"→ 它；材料引出架构判断时它会建议接 /arch-change |
| `/arch-change` | 推进架构（WP/AD/atoms；摸底周期在此） | 想"做判断、动产物"→ 它 |
| `/arch-decide` | 清人决队列（裁 OQ、批 CYC 章程、落裁定+销账） | 想"知道欠我什么决断/裁事"→ 它；刚打开仓库不知道干嘛 → 先它 |
| `/arch-gate` | 过门禁（gate.py 六查 + 评审面板 + 签核请求） | "阶段/周期感觉做完了"→ 它 |
| `/arch-status` | 只读查询：进程态 + 知识覆盖概览 | "项目到哪了"→ 它 |

**知识问答不设入口**：任何会话按 §KB 读取协议直接答。定义层的修改（本文件 / skills / agents / templates / tools）**不属于任何入口**——那是中枢的事，回中枢升版再 sync。

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
| `kb/atoms/<domain>/<kind前缀>-<slug>.md` | 状态 | 事实层原子（SoT，单写者）；schema 见 §KB |
| `kb/_meta/{taxonomy.md, kb-index.json, graph.json}` | 状态 / 生成 | 受控词表（planes/kinds 增改=方法级决策）；索引与图由 kb-index.py 生成勿手改 |
| `kb/mocs/` `kb/bases/` `kb/_raw/` | 状态 / 定义 / 暂存 | MOC 策展页（围栏块生成）；Bases 实时视图（投影）；ingest 暂存 |
| `project.yaml` | 状态（init 后） | 只存身份 + mode + hub_ref 钉，别的不放 |
| `templates/` `tools/` `.claude/` 本文件等 | 定义 | 中枢投影，勿就地改语义；权威清单=中枢 scaffold-manifest.yaml |

## 三、WP 状态机与标记（操作必需的最小集）

- 状态：`draft → review → baselined@<gate> → released`，另有 `superseded`。只前进不后退；要改已 baselined/released 的内容 → 起 `vN+1`。下游只消费 `released`。
- product 模式解读：as-is = 最新 `released`；to-be = 在途 `draft/review/baselined`。
- 内联标记仅两种（大写可 grep）：`[BLOCKED-ON: OQ-NNN]`（推进不了）、`[ASSUMES: OQ-NNN=<选项>]`（押注推进，须反登 LEDGER 该 OQ 的 bets）。WP frontmatter `blocked_on` 与内联 BLOCKED-ON **双向一致**（gate.py 查）。
- LEDGER 条目格式（gate.py 机器解析，**不得改成表格或散文**）：`### <ID> · 标题` + `- key: value` 行。open 的 OQ 必须决策就绪：`severity / scope / options / recommend` 四键齐全。

## 三之二、KB 事实层纪律（§KB）

- **三层模型**：事实层（kb atoms，可盘点可陈旧）⊂ 投影层（索引/图/MOC 围栏/Bases，生成勿手改）⊂ 观点层（WP/AD，人签核）。**WP 引用事实必须 `[[wikilink]]` 到 atom，不复述展开**。
- **读取协议**（所有会话与 skill 通用）：Tier 0 直读——`kb/_meta/kb-index.json` summary cheap-pass → 目标 atom → 沿 typed edge 走一两跳，禁止全库扫描；Tier 1——开放式/多跳问题委派只读 `kb-retriever`（digest + 逐条 `[[引用]]`；库中没有就明说，禁止训练常识补位）。
- **单写者纪律**：只有入口 skill 的主 agent 写 vault；`kb-retriever`/`kb-extractor`/评审面板一律只读。
- **完成定义**：任何触碰 atoms 的入口收尾必跑 `python3 tools/kb-index.py`（索引/图/MOC 围栏 + 八查）；FAIL = 未完成。
- **矛盾不静默**：与既有 atom 冲突 → `[!contradiction]` callout + 登 OQ。
- **product 模式覆盖规则**：change 型周期的 domains 必须在 domain-map 中 `baselined`（gate.py 机检）——不在盲区做设计决策。

## 四、红线

1. AD 的 Decision、NFR 优先级、CYC 章程批准、gate 签核——只能出自人的会话内明确确认（复述确认后落笔）。
2. 人未裁的 OQ 保持 open，不得替人猜；押注必须留痕。
3. 涟漪铁律：影响半径内的引用清理在本次变更内完成，做不完的登 LEDGER——不许沉默漂移。
4. 每次变更收尾必登账：INDEX（实例状态）+ CHANGELOG（append 一行）+ LEDGER（新登/销账）。
5. 跨仓引用只用仓库名 + ID/钉版；本机路径运行时问人（LG-015）。
