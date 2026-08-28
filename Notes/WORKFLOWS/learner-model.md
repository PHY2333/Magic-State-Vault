# Notes/WORKFLOWS/learner-model.md

Learner model 记录“有什么证据表明读者能在什么面向上做到什么”，而不是模型认为读者应该知道什么。

## 1. Evidence state

- `unseen`：有明确证据表明第一次接触该能力。
- `named`：见过名称，没有含义或操作证据。
- `introduced`：有基本定义或局部图像，尚不能独立使用。
- `operational`：能在当前类型问题中正确应用、计算或解释。
- `fluent`：能跨情境迁移、比较或独立调用。
- `unverified`：没有足够证据；缺证据时的默认状态，不等于第一次接触。

## 2. Capability facets

同一个概念必须按需要拆成不同能力面向：

| facet | 问题 |
|---|---|
| `identity` | 它是什么类别的对象？ |
| `basic_data` | 它由哪些数据给出？ |
| `context_role` | 它在当前构造中承担什么？ |
| `representation` | 怎样读取其符号、矩阵、图或坐标？ |
| `procedure` | 怎样计算、构造或操作？ |
| `rationale` | 为什么成立、为什么需要？ |
| `transfer` | 能否迁移到新语境？ |

不得用一条宽泛状态覆盖整个概念。

示例：

```text
经典奇偶校验矩阵 / identity       / unverified
A、B 是 HGP 的两份输入 / context_role / unseen
从矩阵行列读变量与校验 / representation / unverified
```

## 3. 重要区别

- 仓库中存在笔记，不是 learner evidence；
- 用户提到名称，最多支持 `named`；
- 没有证据，不得标为 `unseen`；
- 当前角色是新的，不代表基础概念本身也是新的；
- `unverified` 不能被正文直接假设，但可由 Didactic Architect 选择 `remind`、`introduce` 或 `delay`。

## 4. Evidence

有效证据包括：

- 用户明确说“第一次看到”“没有概念”；
- 用户正确复述定义；
- 用户完成具体计算或推导；
- 用户在新问题中迁移概念；
- 近期真实问题暴露某一步不稳定。

每项记录 `evidence`、`scope`、`confidence`、日期和风险。

## 5. 风险标记

- `misconception`
- `unstable`
- `transfer-gap`
- `notation-overload`
- `role-confusion`：混淆概念本身与当前任务角色
- `claim-gap`：能识别术语，但某个解释命题的前提不足

## 6. Task snapshot

`LEARNER_SNAPSHOT.md` 至少包含：

- 当前目标；
- capability id、subject、facet；
- evidence state；
- 证据、范围、置信度、风险；
- 可以直接使用的能力；
- 不得直接假设的能力；
- 近期问题；
- 可能真正改变路线的不确定项。

Task snapshot 不直接决定正文 action；Didactic Architect 根据当前用途选择。

## 7. 用户负担

不得要求用户逐项填写能力表。只有一个关键不确定项会导致完全不同路线时，才提出一个具体问题。

## 8. 更新

- Lesson 发布不自动升级状态；
- 出口能力得到实际证据后才升级；
- 同一点再次卡住时降低状态或拆细 facet；
- 跨情境稳定应用后才标 `fluent`。
