# Notes/WORKFLOWS/learner-model.md

Learner model 记录“有什么证据表明读者能在什么面向上做到什么”，不决定本处讲解深度。

## 1. Evidence state

- `unseen`：有明确第一次接触证据。
- `named`：见过名称，无含义或操作证据。
- `introduced`：有基本定义或局部图像。
- `operational`：能在当前类型问题中正确使用。
- `fluent`：能跨情境迁移。
- `unverified`：没有足够证据；默认状态，不等于第一次接触。

## 2. Capability facets

`identity | basic_data | context_role | representation | procedure | rationale | transfer`

不得用一条宽泛状态覆盖整个概念。

## 3. Evidence state 与 explanation depth 分离

- Evidence state 说明证据；
- explanation depth 由 Didactic Architect 根据当前目标选择；
- `unverified` 可能对应 reminder、compact derivation、optional derivation、upstream bridge 或 delay；
- 不得将 `unverified` 自动翻译为 full derivation。

## 4. Evidence

有效证据包括用户明确描述、正确复述、具体计算、迁移应用和近期问题。每项记录范围、置信度、日期和风险。

## 5. 风险标记

`misconception | unstable | transfer-gap | notation-overload | role-confusion | claim-gap | over-explanation-risk`

## 6. Task snapshot

至少包含当前目标、capability id/subject/facet/state、证据与范围、可直接使用、不得直接假设、近期问题和真正会改变路线的不确定项。

## 7. 用户负担与更新

不要求用户填写能力表。发布不自动升级状态；只有实际出口表现才升级。
