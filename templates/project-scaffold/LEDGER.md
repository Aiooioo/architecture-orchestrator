# LEDGER — 单一台账（OQ · RSK · CYC · GATE）

> 条目格式（gate.py 机器解析，勿改结构）：`### <ID> · 标题` + `- key: value` 行。
> ID 三位零填充、只增不复用。当前阶段 = 最后一条 GATE 记录推导。
>
> 各类条目的键：
> - **OQ**（open 时四键必齐）：`status: open|closed(=<选项>)` / `severity: blocking|normal` / `scope: G0|G1|G2|G3|CYC-NNN|global` / `options:` / `recommend:` / `impact-if-unruled:` / `affected:` / `bets:`
> - **RSK**：`status: open|accepted|mitigated|handed-over` / `kind: risk|dependency|debt` / `impact:` / `mitigation:`
> - **CYC**（章程获批时登）：`status: open|closed` / `charter: cycles/CYC-NNN-<slug>.md` / `approved:` 
> - **GATE**（签核时登）：`date:` / `verdict: pass|pass-with-conditions|fail` / `conditions:` / `scope:`

## 待人决断（OQ open）

## 风险·依赖·技术债（RSK）

## 周期（CYC）

## 门禁记录（GATE）

## 已关闭
