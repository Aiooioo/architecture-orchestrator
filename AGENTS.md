# AGENTS — system-arch-base 治理总纲（结构权威）

> 本仓库是 **architecture-method 领域的单一真相源（SoT）**：定义软件架构师的工作产品、生命周期、门禁与人机协作协议，并把它们投影进各架构项目仓。
> 结构与规则以本文件为准；方法语义以 `method/` 各规程为准；流程操作以各 skill 为准（冲突时：结构从本文件、语义从 method、操作从 skill）。

## 一、定位与边界（组合律答卷）

按 agents-orchestrator `CONVENTIONS.md` §13 组合律 C1–C4 自查：

- **C1 单一权威**：architecture-method 域（工作产品定义 / 生命周期 / 门禁 / 协作协议）的 SoT = 本仓库。workflow-engine 域的 SoT = `agents-orchestrator`，两域**显式正交**，互不定义对方内容。
- **C2 投影或接口**：各架构项目仓的定义层（AGENTS/skills/gate.py/HUMAN-GUIDE 等）是本仓 `templates/project-scaffold/` 的**逐字投影**（带 `generated_by` 钉版）；实现仓经**冻结接口**消费项目仓的 `handoff/manifest.yaml`（只引用 `released` 产物，不复述不自存）。
- **C3 无 rival 权威**：项目仓不得就地改投影语义（改进回本仓升版再 sync）；"当前阶段/在途周期"只存在于项目 LEDGER 的 GATE/CYC 记录（推导，不二存）；方法文件在本仓只此一份（4 个项目技能的真相在 `templates/project-scaffold/.claude/skills/`，本仓 `.claude/skills/` 只放中枢专属的 `arch-init`，不留第二份副本）。
- **C4 联合 MECE**：项目仓 4 入口 + 中枢 1 入口按动词键控互斥（见"三、入口路由"），tie-breaker 编入各 SKILL description。
- **注册**：本仓已在 agents-orchestrator `registry.md` 组合关系表登记为 independent-domain-SoT（显式正交）。

## 二、目录结构（schema）

| 路径 | 层 | 说明 |
|---|---|---|
| `method/*.vN.md` | 定义 | 方法规程（版本化，见"四"） |
| `templates/work-products/*.vN.md` | 定义 | 8 类工作产品模板 |
| `templates/cycles/cycle-charter.vN.md` | 定义 | 演进周期章程模板（product 模式） |
| `templates/gates/*.vN.md` + `perspectives/` + `handoff-manifest.yaml` | 定义 | 门禁 checklist / 评审视角 / 交接清单模板 |
| `templates/project-scaffold/` | 定义（投影源） | 项目仓全套骨架，含 4 个项目技能与 `scaffold-manifest.yaml`（定义层/状态层清单） |
| `tools/gate.py` + `gate-config.json` | 定义（投影源） | 确定性门禁，双剖面 profile |
| `.claude/skills/arch-init/` | 定义 | 中枢唯一入口技能 |
| `INDEX.md` / `CHANGELOG.md` / `LEDGER.md` / `REPOS.md` | 状态 | 资产登记 / 演进史 / 方法级决策台账 / 拓扑 |

## 三、入口路由（MECE，动词键控）

| 入口 | 在哪运行 | 动词 | tie-breaker |
|---|---|---|---|
| `/arch-init` | 仅本仓 | 投影：初始化新项目仓（init）或同步定义层更新（sync） | 凡"新开项目 / 把中枢更新推下去"→ 这里；项目内的一切工作 → 项目仓 4 入口 |
| `/arch-change`（项目仓） | 项目仓 | 推进架构：起草/修订工作产品（带影响半径与涟漪闭合） | 想"做架构工作"→ 它 |
| `/arch-decide`（项目仓） | 项目仓 | 清人决队列：裁 OQ、批 CYC 章程 | 想"知道欠我什么决断 / 裁事"→ 它 |
| `/arch-gate`（项目仓） | 项目仓 | 过门禁：gate.py + 评审面板 + 人签核 | "阶段/周期感觉做完了"→ 它 |
| `/arch-status`（项目仓） | 项目仓 | 只读查询 | "只是问问现状"→ 它 |

本仓方法演进**没有专用入口**：直接按"四"的规则改文件（治理者同受 C1–C4 约束——升版、登账、重投影缺一不可）。

## 四、版本化纪律（承 CONVENTIONS §1–§8）

- 定义文件命名 `<name>.v<N>.md`，frontmatter：`version / status(draft|active|deprecated) / supersedes / superseded_by / created / updated`。
- **历史不可变**：`active/deprecated` 只允许勘误级修订；语义变更必升大版本；旧版**永不删除**。同名 artifact 任一时刻最多一个 `active`。
- 升 `active` 前必须在 `CHANGELOG.md` 声明旧产物处理（完全兼容 / 提供迁移 / 显式不迁移），并同步 `INDEX.md`。
- 项目仓每个投影文件头部带 `generated_by: system-arch-base@<commit>/<源路径>`，钉到本仓具体提交。本仓**不设 VERSION 标量文件**——版本真相 = INDEX.md + git commit/tag。
- 方法级决策记 `LEDGER.md`（`MD-NNN`）。

## 五、投影纪律（承 CONVENTIONS §11 + landing-procedure.v2）

1. 部署 = 从 `templates/project-scaffold/` 逐字复制；**绝不在项目仓就地改编译产物语义**。
2. 发现 scaffold 不满足需要 → 停，回本仓升版，再 sync；永不现场打补丁。
3. 项目仓状态层（`project.yaml`〔初始化后〕/ LEDGER / INDEX / CHANGELOG / REPOS / work-products / decisions / cycles / gates / handoff）**只加性迁移、绝不被 sync 覆盖**。定义层/状态层的权威清单 = `templates/project-scaffold/scaffold-manifest.yaml`。
4. sync 收尾必跑**双向完整性校验**：(2a) 投影 vs 源规范化 diff 为空（规范化 = 剥去 `generated_by` 行）；(2b) 状态层文件只有保全/加性。任一不过 = 落地未完成。
5. **路径纪律（LG-015）**：本仓与项目仓互相引用一律用仓库名与 `generated_by` 钉，不写本机绝对/相对路径；需要真实路径时运行时问人。`REPOS.md` 只记角色与关系。

## 六、语言与记法

中文正文 + 英文术语/文件名/ID/frontmatter 键；目录与 slug kebab-case；图一律 Mermaid（不用 PlantUML）；ID 体系：`AD-NNN`（架构决策）/ `OQ-NNN`（待人决断）/ `RSK-NNN`（风险·依赖·技术债）/ `CYC-NNN`（演进周期）/ `GATE-<G0|G1|G2|G3|CYC-NNN>`（门禁记录）/ `MD-NNN`（方法级决策，仅本仓）。完整记法规范见 `method/04-notation-and-style.v1.md`。
