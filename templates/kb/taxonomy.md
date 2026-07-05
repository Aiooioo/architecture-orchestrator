# KB Taxonomy — 受控词表（kb-index.py 校验依据）

> **planes 与 kinds 的增改是方法级决策**：回中枢 LEDGER 记 MD、随中枢升版下发；项目内私改 = lint fail。
> edges 细分与 tags 项目内可增（记项目 CHANGELOG）。条目格式 `- <token>` 开头，kb-index.py 按此解析，勿改结构。

## planes

- business
- application
- data
- deployment
- enterprise

## kinds

- component (CMP)
- interface (IFC)
- datastore (STO)
- dataflow (FLW)
- deployment-node (NOD)
- capability (CAP)
- debt (DBT)
- constraint (CST)

## edges

- calls
- writes
- reads
- exposes
- consumes
- deploys-on
- realizes
- depends-on
- owned-by

## tags

<!-- 项目自增，kebab-case -->
