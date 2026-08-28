# Notes/NOTE_TYPES.md

正式 Notes 有两个独立维度：`note_type` 决定长期知识职责，`entry_mode` 决定读者怎样进入正文。

## 1. Frontmatter

新建或被实质修改的正式笔记至少写：

```yaml
---
note_type: reference | lesson | derivation | paper-guide | index
entry_mode: guided | direct | lookup
status: draft | reviewed | stable | deprecated
---
```

旧笔记不批量迁移。只有在 v4 任务中被实质修改、拆分或纳入新路线时才补字段。

## 2. `note_type`

### `reference`

保存一个概念、构造、定理、协议或判断标准的 canonical 表述。以准确、完整、可检索和可复用为首要目标。

- 可以包含短小 guided onboarding；
- 不要求整篇都采用第一次学习者节奏；
- 一个 reference 通常只承担一个稳定对象或一组不可分割结论。

### `lesson`

让读者完成一次明确的学习状态转移：

```text
入口能力 → 讲解、示范与推导 → 出口能力
```

- 可以跨越多个 canonical concepts；
- 可以局部重述 reference 内容；
- 不成为多个概念的唯一正式来源；
- 优先进入面向读者的学习路线。

### `derivation`

保存一条完整证明、推导、计算或算法论证。

- 复杂推导可先给结果和证明地图；
- 中间构造必须说明解决哪一步困难；
- 条件、映射、指标和符号必须连续可核对。

### `paper-guide`

帮助读者完成一个明确的来源阅读任务。

- 保留来源版本、约定和位置；
- 区分来源事实、仓库知识与推断；
- 只补足返回来源所需的背景；
- 不把来源特例升级为一般定义。

### `index`

只负责导航、顺序和入口，不承担定义、证明或 canonical ownership。

## 3. `entry_mode`

### `guided`

正文承担第一次或不稳定接触的入口责任。

- 开头先建立对象类别、基本数据或当前问题；
- 不以依赖清单、wikilinks 或维护边界开头；
- 必要上游内容在当前用法处局部重述。

### `direct`

正文面向已有明确操作能力的读者，允许较快进入正式构造或推导。

- 依赖必须在 learner snapshot 中有 `operational` 或 `fluent` 证据；
- 不能仅因读者“可能学过”而使用 direct。

### `lookup`

正文主要供查询，不承诺连续的首次阅读体验。

- 可以定义优先、边界优先；
- `00-index` 不应把它作为没有替代入口的第一站。

## 4. 两个维度不能互相替代

```yaml
note_type: reference
entry_mode: guided
```

表示文件仍是 canonical reference，但开头承担读者第一次进入该对象的责任。

`reference` 不等于维基式开头，`guided` 也不等于整篇都写成慢速教程。

## 5. 拆分判断

只有在以下情况考虑拆分：

- 一个文件长期承担两个互相冲突的 note type；
- guided onboarding 已扩展成完整、可独立阅读的 lesson；
- 一个推导足够长，已经压倒 reference 主体；
- paper-specific 约定开始污染一般定义；
- 两种 entry mode 无法在同一文件中清楚共存。

短小 onboarding 不自动触发拆分。
