# INDEX — 中枢资产登记（版本真相源）

> 任何定义文件的版本/状态变化必须同步本表（承 CONVENTIONS §8）。本仓不设 VERSION 标量文件——对外钉版一律 `system-arch-base@<commit-or-tag>`。

## method/

| 文件 | active 版本 | 状态 |
|---|---|---|
| method/00-overview | v1 | active |
| method/01-work-products | v1 | active |
| method/02-lifecycles-and-gates | v1 | active |
| method/03-collaboration-protocol | v1 | active |
| method/04-notation-and-style | v1 | active |
| method/05-glossary | v1 | active |

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

## templates/cycles/ + templates/gates/

| 模板 | active 版本 | 状态 |
|---|---|---|
| cycle-charter | v1 | active |
| gate-g0-baseline | v1 | active |
| gate-g1-context | v1 | active |
| gate-g2-design | v1 | active |
| gate-g3-release | v1 | active |
| gate-gc-cycle | v1 | active |
| gates/perspectives/（4 视角） | —（随 commit 钉版） | active |
| gates/handoff-manifest.yaml | —（随 commit 钉版） | active |

## 工具与投影源

| 资产 | 版本 | 状态 |
|---|---|---|
| tools/gate.py + gate-config.json | —（随 commit 钉版） | active |
| templates/project-scaffold/（含 4 项目技能 + scaffold-manifest.yaml） | —（随 commit 钉版） | active |
| .claude/skills/arch-init | —（随 commit 钉版） | active |
