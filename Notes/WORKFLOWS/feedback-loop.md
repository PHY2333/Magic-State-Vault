# Notes/WORKFLOWS/feedback-loop.md

读者反馈是学习证据，不是教材审批表。

## 1. 用户只需正常提问

例如：

- “这个词第一次出现时我没有概念”；
- “公式会算，但不知道为什么要算”；
- “局部看懂了，整体目标丢了”；
- “这句解释其实默认了另一个事实”；
- “这个定义像同义反复”；
- “这一段像维基或 AI 技术说明”；
- “中英混在一起读起来很断”。

不得要求用户先判断应该拆文件、换模式或补哪个前置。

## 2. 失败类型

- `learner-state-mismatch`
- `concept-role-collapse`
- `term-too-early`
- `hidden-claim-premise`
- `circular-or-thin-definition`
- `missing-motivation`
- `lost-global-map`
- `pattern-mismatch`
- `load-overflow`
- `derivation-gap`
- `example-failure`
- `language-register-mismatch`
- `source-or-math-error`
- `repository-leakage`
- `type-or-entry-mode-mismatch`

## 3. 路由

| 反馈 | 返回 |
|---|---|
| 模型错误假设读者已知；概念与角色混淆 | learner model |
| 术语太早、隐含 premise、定义问题、缺动机、丢整体、负荷过高 | didactic design |
| 局部推导、中文表达或术语渲染 | Writer |
| 数学或来源错误 | Mapper |
| wikilink、ownership、索引 | Integrator |
| note type / entry mode 根本不匹配 | Didactic Architect + Integrator |

## 4. 记录

稳定问题记录在 `Notes/LEARNER/QUESTIONS.md`，包括位置、用户原问题、失败类型、相关 capability facet、返回阶段和处理状态。

不得把问题原句直接追加到正式正文。

## 5. Reopen

若反馈暴露结构问题，将已发布任务标为 `reopened`，只重开受影响层级。
