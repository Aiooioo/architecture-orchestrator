---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: wp-template
wp: domain-map
---
<!-- product 模式核心（G0 bootstrap 的主产物）。滚动文档：覆盖翻转/计数刷新属勘误级就地修订，
     重新划分域才升大版本。§2 覆盖台账表为 gate.py 机器解析——列序与取值枚举不得改。 -->

```yaml
---
wp: domain-map
version: 1
status: draft
supersedes: null
superseded_by: null
blocked_on: []
created: <date>
updated: <date>
generated_from: system-arch-base@<commit>/templates/work-products/domain-map.v1.md
---
```

<!-- TEMPLATE-BODY -->
# Domain Map — <产品名>

> 读者：Chief Architect + 所有 agent。回答：产品分为哪些域、域间什么关系、每个域我们知道多少/多新鲜。
> 铁律：**负空间显式**——没摸过的域也必须出现在台账里，哪怕只有一个名字。

## 1. 划分依据

<!-- 一段话：按什么原则切域（业务能力/团队边界/数据所有权），为什么。重新划分 = 升大版本 + G0 复签。 -->

## 2. 覆盖台账（gate.py 机器解析，列序勿改）

<!-- coverage 枚举：unmapped（只有名字）| mapped（域目录有 atoms）| baselined（经 baseline 周期 GC 签核）| stale（超龄）。
     atoms 数与 last-verified 由 kb-index.py 输出对照填写。 -->

| domain | coverage | last-verified | atoms | moc |
|---|---|---|---|---|
| billing | unmapped | — | 0 | — |
| ordering | unmapped | — | 0 | — |

## 3. 域间关系（摸底最小闭包的依据）

<!-- 每行一条关系：上下游 / 共享数据 / 同步调用。选摸底切片时按此算最小依赖闭包（目标域 + 强依赖域）。 -->

| from | to | 关系 | 强度（strong/weak） |
|---|---|---|---|
| ordering | billing | 下单触发计费 | strong |

## 4. 摸底策略备注

<!-- 首刀怎么选（诉求倒逼）、哪些域明确长期不摸（写明为什么可接受）。 -->
