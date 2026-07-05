---
version: 1
status: active
supersedes: null
superseded_by: null
created: 2026-07-05
updated: 2026-07-05
---

# 03 · 人机协作协议（collaboration protocol）

## 1. 角色

| 角色 | 承担者 | 职责 | 不做什么 |
|---|---|---|---|
| Chief Architect | 人 | 裁决 OQ、批准 CYC 章程、签核门禁、裁定 AD Decision 与 NFR 优先级、给输入 | 不亲自起草（可以，但不是义务） |
| Staff Architect | agent | 起草与修订全部 WP、登记 OQ/RSK、自查与涟漪闭合、运行门禁与打包 | **不替人做架构决策**（见 §2 红线） |
| 评审面板 | 只读 subagent × 4 | gate 内按视角审查，产出 findings | 不修改任何文件；不调停视角冲突 |

## 2. 红线（违反即为方法缺陷，须回流中枢）

1. AD 的 `Decision` 字段、NFR 的优先级、CYC 章程的批准、gate 签核——**只能出自人的会话内明确确认**。agent 不得以"合理默认"名义代填。
2. 人未裁的 OQ 保持 open，**不得替人猜**；可押注（§4）但必须留痕。
3. 决策类文本落笔前**复述确认**：agent 把将写入的裁定内容念给人，人确认后才写。
4. 涟漪铁律：影响半径内的引用清理必须**在本次变更内**完成；当场做不完的必须登 LEDGER——不许沉默漂移。

## 3. OQ 决策队列（异步决策的核心机制）

agent 遇到需人裁定的点 → **登记，不决定**。登记必须"决策就绪"（decision-ready），否则 gate 时批量裁决会退化成读论文：

```
### OQ-007 · 会话缓存放 Redis 还是内存？
- status: open            # open | closed(=<选项>)
- severity: normal        # blocking=当场暂停问人 | normal=攒到 gate 批量裁
- scope: G2               # 哪个 gate/周期的辖域（G1|G2|G3|G0|CYC-NNN|global）
- options: A) Redis（独立部署） B) 进程内存+粘性会话 C) 不缓存
- recommend: A — 水平扩展是 must 级 NFR-003 的前提
- impact-if-unruled: operational-model 无法定稿；押注见 bets
- affected: work-products/03-component-model（§缓存层）, work-products/04-operational-model
- bets: component-model.v2 §缓存层 [ASSUMES: OQ-007=A]
```

- `severity: blocking` 的判据：**裁定结果会推翻已有工作方向**（如单租户 vs 多租户）。此时暂停会话直接问人，不入队等待。
- 裁决入口：`/arch-decide`（人随时可来清账；gate 前必清域内账）。

## 4. 阻塞与押注（BLOCKED-ON / ASSUMES）

不确定点的三档处置，由轻到重：

1. **能推进就押注**：在依赖该裁定的章节标 `[ASSUMES: OQ-007=A]` 继续干，并把押注**反向登记**到 LEDGER 该 OQ 行的 `bets`。押注不是决策——可审计、可回滚；人若裁了 B，押 A 的章节就是现成的返工清单。
2. **推进不了就阻塞**：无法合理押注的点位标 `[BLOCKED-ON: OQ-007]`，同时在该 WP frontmatter `blocked_on: [OQ-007]` 聚合（gate.py 校验内联↔frontmatter 一致）。
3. **方向性问题就暂停**：severity=blocking，当场问人。

**裁决后的涟漪**：`/arch-decide` 落一条裁定时，按 OQ id 全库 grep，关闭每一处 `[BLOCKED-ON]`/`[ASSUMES]` 标记：押对的删标记即可；押错的章节修正内容（当场改，或改不完登 LEDGER 新条目）。LEDGER 该 OQ 移入已关闭区，记 `closed(=A)`。

## 5. 交叉评审（作者≠审查者）

- 深度评审**只在 gate 内强制发生**（4 视角面板，见 `02-lifecycles-and-gates.v1.md` §3）——不是独立入口，不可跳过。
- `/arch-change` 收尾自带轻量自查（frontmatter 完整 / 引用不死链 / OQ 已登记 / INDEX+CHANGELOG 已登账），抓"形"不抓"义"。
- 面板 findings 的两出口：机械问题当场修；**语义问题登 OQ/RSK，不在 gate 里盲改**。

## 6. 升级路径（异常时找谁）

| 情况 | 处置 |
|---|---|
| agent 与人对方法本身有分歧 | 登本仓（中枢）LEDGER `MD-NNN` 待决区，人裁 |
| scaffold/模板不够用 | **停止就地改语义**，回中枢升版 → sync 重投影（可先在项目仓以 OQ 记录诉求） |
| 跨仓路径找不到 | 问人（LG-015），不猜不硬编码 |
| gate.py 与 checklist 冲突 | gate.py（机器判定）为准，checklist 缺陷回流中枢 |

## 7. 一天的样子（示例，engagement 中段）

1. 人早上打开项目仓，`/arch-status` 30 秒了解现状：02-design 在途，OQ 队列 3 条（1 blocking）。
2. `/arch-decide` 清账：blocking 那条当场裁，2 条 normal 顺手裁掉 1 条。agent 落裁定 + 涟漪销账。
3. 人离开。agent 按人给的输入 `/arch-change` 推进 component-model v2，遇到新不确定点：1 条押注（ASSUMES）、1 条登 OQ。
4. 傍晚人回来觉得设计差不多了 → `/arch-gate` G2：gate.py 因 1 条 open OQ 拒绝 → 转 `/arch-decide` 裁掉 → 重跑 gate → 面板出 2 条 findings（1 修 1 登 RSK）→ 人复述确认签核 → G2 落账，设计类 WP 升 `baselined@G2`。
