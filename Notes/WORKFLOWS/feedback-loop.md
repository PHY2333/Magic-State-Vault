# Notes/WORKFLOWS/feedback-loop.md

读者反馈是学习证据，不是教材审批表。

## 1. 用户只需正常提问

例如：术语没概念、公式会算但不知道为何、局部懂却目标丢了、解释默认了事实、定义同义反复、这一段太长、补充推导压过主线、像维基或中英混杂。

## 2. 失败类型

`learner-state-mismatch | concept-role-collapse | term-too-early | hidden-claim-premise | circular-or-thin-definition | missing-motivation | lost-global-map | explanation-depth-mismatch | mainline-latency | proportionality-failure | duplication-cost | pattern-mismatch | load-overflow | derivation-gap | language-register-mismatch | source-or-math-error | repository-leakage | type-or-entry-mode-mismatch`

## 3. 路由

- Learner 假设／concept-role：learner model；
- premise、definition、动机、depth、mainline、比例：didactic design；
- 局部推导／中文：Writer；
- 数学／来源：Mapper；
- duplication、links、index：Integration Preview / Integrator；
- type/entry mode：Architect + Integrator。

## 4. 记录与 reopen

稳定问题写入 `Notes/LEARNER/QUESTIONS.md`，记录位置、原问题、失败类型、facet、返回阶段和状态。不得把问题原句直接追加到正文。
