# system-arch-base — 架构师工作方法中枢

软件架构师的**方法中枢（method hub）**：以 IBM 经典工作产品体系（GS Method / UMF）为骨架、现代记法（C4 / Mermaid / ADR）为表达，定义架构工作的产出物、生命周期、门禁与人机协作协议，并把它们**投影**进每个架构项目仓。

- 人 = Chief Architect：只做三件事——裁决 OQ 队列、签核门禁、给输入。
- Agent = Staff Architect：起草全部工作产品、交叉评审、登记待决事项、打包交接。

## 快速开始

**新的项目型交付（engagement：有明确起止的一次性架构设计）**

1. 在本仓开一个 Claude 会话，运行 `/arch-init`，选 `engagement` 模式，给出新项目仓路径。
2. 进入新项目仓，读 `HUMAN-GUIDE.md`（一页纸），然后 `/arch-change` 开始起草 System Context。
3. 生命周期：`01-context` → G1 → `02-design` → G2 → `03-assure-and-release` → G3（产出 `handoff/manifest.yaml` 交实现仓）。

**长周期 SaaS 产品（product：摸底入场 + 持续演进）**

1. `/arch-init` 选 `product` 模式。
2. `00-baseline` 摸底：对现有系统逆向产出 as-is 工作产品 → G0 签核，"现状真相"确立。
3. 之后以演进周期（`CYC-NNN`）循环：章程获批开工 → 压缩版 context→design→assure → GC 门禁 → 交接该周期变更。

## 读什么

| 想了解 | 去哪 |
|---|---|
| 治理规则 / 结构 schema | `AGENTS.md` |
| 方法总纲与 IBM 渊源 | `method/00-overview.v1.md` |
| 8 类工作产品的定义与 DoD | `method/01-work-products.v1.md` |
| 双剖面生命周期与门禁 | `method/02-lifecycles-and-gates.v1.md` |
| 人机协作协议（OQ / 押注 / 涟漪） | `method/03-collaboration-protocol.v1.md` |
| 记法 / 状态机 / frontmatter | `method/04-notation-and-style.v1.md` |
| 术语中英对照 | `method/05-glossary.v1.md` |
| 资产与版本登记 | `INDEX.md` |
| 生态拓扑 | `REPOS.md` |
