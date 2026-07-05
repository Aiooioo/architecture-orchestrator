# INDEX — 中枢资产登记（版本真相源）

> 任何定义文件的版本/状态变化必须同步本表（承 CONVENTIONS §8）。本仓不设 VERSION 标量文件——对外钉版一律 `system-arch-base@<commit-or-tag>`。

## method/

| 文件 | active 版本 | 状态 |
|---|---|---|
| method/00-overview | v2 | active（v1 deprecated） |
| method/01-work-products | v2 | active（v1 deprecated；v2 为增量文档，WP1-8 承 v1 原文） |
| method/02-lifecycles-and-gates | v2 | active（v1 deprecated） |
| method/03-collaboration-protocol | v1 | active |
| method/04-notation-and-style | v1 | active |
| method/05-glossary | v2 | active（v1 deprecated） |
| method/06-knowledge-base | v1 | active |

## templates/work-products/

| 模板 | active 版本 | 状态 |
|---|---|---|
| system-context | v1 | active |
| architecture-overview | v1 | active |
| component-model | v1 | active |
| operational-model | v1 | active |
| nfr-catalog | v1 | active |
| key-scenario | v1 | active |
| architectural-decision | v1 | active |
| evolution-roadmap | v1 | active |
| domain-map | v1 | active |

## templates/cycles/ + templates/gates/

| 模板 | active 版本 | 状态 |
|---|---|---|
| cycle-charter | v2 | active（v1 deprecated） |
| gate-g0-baseline | v2 | active（v1 deprecated；语义改为 bootstrap 门） |
| gate-g1-context | v1 | active |
| gate-g2-design | v1 | active |
| gate-g3-release | v1 | active |
| gate-gc-cycle | v2 | active（v1 deprecated） |
| gates/perspectives/（4 视角） | —（随 commit 钉版） | active |
| gates/handoff-manifest.yaml | —（随 commit 钉版） | active |

## 工具与投影源

| 资产 | 版本 | 状态 |
|---|---|---|
| tools/gate.py + gate-config.json | —（随 commit 钉版）· 六查 | active |
| tools/kb-index.py | —（随 commit 钉版）· kb 八查 | active |
| templates/project-scaffold/（含 5 项目技能 + 2 只读 agents + scaffold-manifest.yaml） | —（随 commit 钉版） | active |
| .claude/skills/arch-init | —（随 commit 钉版） | active |

## templates/kb/

| 模板 | active 版本 | 状态 |
|---|---|---|
| atom | v1 | active |
| domain-moc / plane-moc | v1 | active |
| taxonomy.md（状态种子源） | —（随 commit 钉版） | active |
| bases/（3 个 .base 视图） | —（随 commit 钉版） | active |
