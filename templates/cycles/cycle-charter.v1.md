---
version: 1
status: deprecated
supersedes: null
superseded_by: cycle-charter.v2.md
created: 2026-07-05
kind: cycle-charter-template
---
<!-- product 模式专属。实例化到 cycles/CYC-NNN-<slug>.md。
     frontmatter 被 gate.py 机器解析（GC 门禁按 affected_wps 动态确定必备项）——键名与结构不得改。
     生命周期：proposed（agent 起草）→ open（人经 /arch-decide 批准，LEDGER 记 CYC-NNN opened）→ closed（GC 签核）。
     红线：status=proposed 时不得用 /arch-change 挂靠本周期做实质变更。 -->

```yaml
---
cycle: CYC-001
slug: <kebab-slug>
status: proposed        # proposed | open | closed
created: <date>
updated: 2026-07-05
affected_wps:           # GC 门禁的动态必备矩阵（gate.py 解析）
  - wp: component-model
    target_version: 3   # 本周期要产出的版本号
    min_status: review  # GC 运行前须达到的最低状态（通常 review）
  - wp: operational-model
    target_version: 2
    min_status: review
---
```

<!-- TEMPLATE-BODY -->
# CYC-001 · <周期标题>

## 触发源

<!-- 三选一并给指针：新需求（外部输入）/ NFR 压力或事故（RSK-NNN）/ 技术债（RSK-NNN）/ roadmap 过渡步骤（GAP-NNN）。 -->

## 范围

- **做**：
- **不做**（本周期显式推迟的，写明去向：下周期候选 / roadmap）：

## 受影响 WP 与理由

<!-- frontmatter affected_wps 的人话版：为什么这些 WP 要动、动到什么程度。漏列 = GC 查不到 = 涟漪逃逸，评审面板会专查。 -->

| WP | 目标版本 | 变更性质 |
|---|---|---|
| | | |

## 完成判据

<!-- 本周期"做完"的可判定标准，GC 签核时对照。 -->

## 批准记录

<!-- /arch-decide 批准后由 agent 填：日期 + LEDGER 条目指针。 -->
