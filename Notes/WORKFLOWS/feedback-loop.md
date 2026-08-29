# Notes/WORKFLOWS/feedback-loop.md

用户的正常阅读问题是 learner evidence，不是要求用户承担教材审计。

## 1. 记录

在 `Notes/LEARNER/QUESTIONS.md` 记录：

- 位置；
- 用户原问题；
- 当时已知内容；
- 失败类型；
- 影响范围；
- 返回角色。

## 2. 路由

| 反馈 | 返回 |
|---|---|
| 数学、来源、约定或范围错误 | Codex Sol mapping/source verification |
| 读者前提判断错误 | Sol learner snapshot，再交 Pro design |
| 整篇像百科、视角错误、目标丢失、难度断崖 | ChatGPT Pro architecture |
| 局部概念解释、证明地图或过渡失败 | ChatGPT Pro author |
| 错字、链接、公式排版、机械表格 | Codex Sol |
| 文件职责、拆分或 source-specific/general 冲突 | Pro design；需要结构操作时再询问用户 |

## 3. 禁止

- 不把用户问题直接附加为 FAQ 式正文；
- 不要求用户填写 unit map、depth 或审查表；
- 不因一处局部问题重跑无关的全部 mapping；
- 不让 Sol 在 Pro-required 反馈后自行重写主线。
