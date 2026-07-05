---
version: 2
status: active
supersedes: cycle-charter.v1.md
superseded_by: null
created: 2026-07-05
kind: cycle-charter-template
---
<!-- v2 变更：新增 kind（baseline|change）与 domains 字段；affected_wps 条目可带 instance（域实例）。
     frontmatter 被 gate.py 机器解析——键名与结构不得改。
     生命周期：proposed → open（人经 /arch-decide 批准）→ closed（GC 签核）。
     覆盖规则（gate.py 机检）：kind=change 的 domains 必须全部在 domain-map 中 coverage=baselined；
     kind=baseline 无此约束（它就是去建立覆盖的）。混合周期（先摸后改）拆两条 affected_wps 或直接用 change+前置 baseline 周期。 -->

```yaml
---
cycle: CYC-001
slug: <kebab-slug>
kind: baseline          # baseline=摸切片 | change=做演进
domains: [billing]      # 本周期涉及的域（对照 domain-map；覆盖规则据此机检）
status: proposed        # proposed | open | closed
created: <date>
updated: <date>
affected_wps:           # GC 动态必备矩阵（gate.py 解析）
  - wp: component-model
    instance: billing   # 可选：域实例 → 解析 component-model.billing.vN.md；缺省=产品级文件
    target_version: 1
    min_status: review
---
```

<!-- TEMPLATE-BODY -->
# CYC-001 · <周期标题>

## 触发源

<!-- baseline 型：哪个诉求/事故倒逼摸这个切片 + domain-map 最小闭包计算结果。
     change 型：新需求 / RSK-NNN / GAP-NNN。 -->

## 范围

- **做**：
- **不做**（显式推迟，写明去向）：

## 受影响 WP 与理由

<!-- baseline 型同时写明：预计产出的 atoms 范围（kinds×域）。漏列 = 涟漪逃逸，评审面板专查。 -->

| WP（含 instance） | 目标版本 | 变更性质 |
|---|---|---|
| | | |

## 完成判据

<!-- baseline 型默认含：域 atoms 全 verified、无死链、域 MOC 围栏最新（kb 八查兜底）+ 该域覆盖可翻 baselined。 -->

## 批准记录

<!-- /arch-decide 批准后由 agent 填：日期 + LEDGER 条目指针。 -->
