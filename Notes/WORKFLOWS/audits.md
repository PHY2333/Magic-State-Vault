# Notes/WORKFLOWS/audits.md

本文件规定双审查门和最终 manuscript verdict。

## 1. 两道审查必须独立

1. `CONTRACT_AUDIT.md`：packet-aware，检查数学、来源、claims 与合同。
2. `COLD_READ_AUDIT.md`：blind，检查真实教材阅读体验。

Blind Reader 在形成首次 verdict 前不得看到 Contract Audit。

## 2. Final gate

Manuscript Gatekeeper 只有在两份审查都完成后读取：

- Contract Audit；
- Cold-Read Audit；
- 当前 draft revision 标识。

输出 `MANUSCRIPT_VERDICT.md`：

```yaml
status: pass | changes_required | blocked
contract_audit_status:
cold_read_audit_status:
reviewed_draft_revision:
```

两者都为 `pass` 才能得到最终 `pass`。

## 3. 返修路由

| 问题 | 返回 |
|---|---|
| 数学、来源、约定 | mapping |
| learner facet 错配 | learner model |
| 隐含 premise、定义、claim 顺序、负荷 | didactic design |
| packet 污染或缺项 | Packet Builder |
| 局部语言、术语渲染、公式执行 | Writer |
| 文件与索引 | Integrator |

## 4. 重审规则

Draft 改动后：

- Contract Audit 必须重新运行；
- Blind Cold-Read 必须在新的干净上下文中重新运行；
- 不得只修改旧审查结论；
- 同类 major 两轮仍未闭合则标记 blocked，并说明根因。

## 5. v4 回归测试

Final gate 至少确认：

- concept identity 与 context role 未混淆；
- explanation claims 的事实前提闭合；
- 定义非循环且有 operational hook；
- 第一对象稳定，不是词典多义开头；
- 中文术语统一；
- Blind Reader 没有读取 packet/design；
- Writer 没有直接写正式文件。
