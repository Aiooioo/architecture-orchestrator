# REPOS — 拓扑（角色与关系，不记路径）

> 路径纪律（LG-015）：本文件只记**角色 / 关系 / 数据流**。任何仓库的本机路径都不写死——需要时由 agent 在运行时向人询问。

```
agents-orchestrator            system-arch-base（本仓）
  workflow-engine 域 SoT   ⟂    architecture-method 域 SoT
  （显式正交，互不定义对方内容）        │
                                      │ /arch-init 投影（定义层，generated_by 钉版）
                                      ▼
                              架构项目仓（每项目/产品一仓）
                              mode: engagement | product
                                      │
                                      │ 冻结接口：handoff/manifest.yaml
                                      │（下游只按引用消费 status=released 的产物）
                                      ▼
                              实现仓（代码仓库，各自独立）
```

## 关系说明

| 边 | 性质 | 契约 |
|---|---|---|
| 本仓 → 项目仓 | 定义→投影 | 定义层逐字投影 + `generated_by: system-arch-base@<commit>` 钉版；状态层永不覆盖；sync 走双向完整性校验 |
| 项目仓 → 实现仓 | 冻结接口 | 实现仓只消费 `handoff/manifest.yaml` 清单中 `released` 的工作产品，按引用不复述 |
| 本仓 ⟂ agents-orchestrator | 显式正交 | 已在其 `registry.md` 组合关系表登记；如未来把本方法迁移为 orchestrator scenario，走其 `ef-define` 入场检查 |

## 项目仓登记

| 项目仓（名称） | mode | 初始化日期 | 状态 |
|---|---|---|---|
| （尚无，`/arch-init` 成功后在此登记） | | | |
