# Notes/WORKFLOWS/audits.md

本文件规定双审查门和 manuscript verdict。

## 1. 两道审查独立

1. Contract Audit：packet-aware，检查数学、claims、depth 与合同。
2. Blind Cold-Read：blind，检查真实阅读、mainline latency、比例性与 optional skip test。

Blind Reader 首次 verdict 前不得看到 Contract Audit。

## 2. Final gate

Gatekeeper 读取两份审查与相同 draft revision，输出 `MANUSCRIPT_VERDICT.md`。两者都 pass 才能 manuscript pass。

Manuscript pass 只授权 `INTEGRATION_PREVIEW.md`，不直接授权写正式文件。

## 3. 返修路由

| 问题 | 返回 |
|---|---|
| 数学、来源、detail owner | mapping |
| learner facet | learner model |
| premise、definition、depth、placement、mainline、比例 | didactic design |
| packet 污染 | Packet Builder |
| 局部语言与公式执行 | Writer |
| 仓库适配 | Integration Preview / Integrator |

## 4. 重审规则

Draft 改动后两道审查都重跑；不得只改旧结论。相同 major 三轮未闭合则 blocked。

## 5. v5 回归测试

Final gate 至少确认：

- concept/role 分离；
- claim premises 闭合；
- definitions 在首次依赖前闭合且句法自然；
- evidence state 未决定 full depth；
- mainline latency 与比例性通过；
- optional detail 可跳过；
- 中文术语统一；
- Writer/Blind Reader 隔离；
- Writer 未写正式文件。
