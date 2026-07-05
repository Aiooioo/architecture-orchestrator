---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
kind: kb-atom-template
---
<!-- 事实原子模板。实例化到 kb/atoms/<domain>/<kind前缀小写>-<slug>.md，slug 全库唯一。
     frontmatter 必填：id/kind/domain/planes/status/last-verified/summary（kb-index.py 八查③）。
     typed edge 字段取值必须是 "[[slug]]" 形式；词表见 kb/_meta/taxonomy.md。 -->

```yaml
---
id: CMP-0001                 # 前缀对应 kind（见 taxonomy），只增不复用
kind: component              # taxonomy kinds 枚举
domain: <domain>             # = 所在目录名
planes: [application]        # taxonomy planes 枚举，可多值
summary: <一句话，索引 cheap-pass 用>
aliases: []
status: observed             # observed | verified | stale
last-verified: <date>
sources: []                  # 证据锚：代码路径/配置/监控/文档 URL
# —— typed edges（按需选用，taxonomy edges 枚举）——
# calls: ["[[cmp-xxx]]"]
# writes / reads: ["[[sto-xxx]]"]
# exposes / consumes: ["[[ifc-xxx]]"]
# deploys-on: ["[[nod-xxx]]"]
# realizes: ["[[cap-xxx]]"]
# depends-on / owned-by: []
---
```

<!-- TEMPLATE-BODY -->
一段话事实陈述（这是什么、干什么、关键行为特征）。正文可自由 [[wikilink]] 互链。
推断标 `^[inferred]`，存疑标 `^[ambiguous]`；有实测/代码证据的断言不用标。

<!-- 与既有 atom 矛盾时（不静默改写）：
> [!contradiction]
> 本源称 X，但 [[某-atom]] 记录为 Y → 已登 OQ-NNN
-->
