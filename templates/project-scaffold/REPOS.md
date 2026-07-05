# REPOS — 本项目拓扑（角色与关系，不记路径）

> 路径纪律（LG-015）：只记角色/关系/数据流；本机路径运行时问人。

| 仓库（名称） | 角色 | 契约 |
|---|---|---|
| system-arch-base | 方法中枢（上游定义源） | 定义层投影，钉版见 project.yaml `hub_ref`；sync 经 /arch-init |
| {{PROJECT_NAME}}（本仓） | 架构项目仓 | 产出 WP / AD / handoff manifest |
| <实现仓，接入时登记> | 下游消费者 | 只消费 handoff/manifest 所列 `released` 产物，按引用不复述 |
