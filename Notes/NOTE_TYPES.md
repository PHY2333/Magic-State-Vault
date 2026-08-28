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

旧笔记不批量迁移。只有在 v5 任务中被实质修改、拆分或纳入新路线时才补字段。

## 2. `note_type`

### `reference`

保存一个概念、构造、定理、协议或判断标准的 canonical 表述。

- 可以包含短小 guided onboarding；
- 不要求整篇都采用第一次学习者节奏；
- 一个 reference 通常只承担一个稳定对象或一组不可分割结论；
- 若完整辅助推导已有 canonical owner，当前 reference 默认保留必要 local bridge，而不是无条件重复整段证明。

### `lesson`

让读者完成一次明确的学习状态转移：

```text
入口能力 → 讲解、示范与推导 → 出口能力
```

可以跨越多个 canonical concepts，也可以局部重述 reference 内容。

### `derivation`

保存一条完整证明、推导、计算或算法论证。复杂推导可先给结果与证明地图。

### `paper-guide`

帮助读者完成一个明确的来源阅读任务；保留版本、约定和 source-specific 边界。

### `index`

只负责导航、顺序和入口，不承担定义、证明或 canonical ownership。

## 3. `entry_mode`

### `guided`

正文承担第一次或不稳定接触的入口责任。开头先建立对象、问题或必要整体，不以维护路由开头。

### `direct`

面向已有 `operational` 或 `fluent` 证据的读者，可较快进入正式构造或推导。

### `lookup`

主要供查询，不承诺连续首次阅读体验；不应作为没有替代入口的首站。

## 4. 两个维度不能互相替代

```yaml
note_type: reference
entry_mode: guided
```

表示文件仍是 canonical reference，但开头承担读者进入该对象的责任。`guided` 不等于所有上游事实都要在主线完整重证。

## 5. 拆分判断

考虑拆分的情况：

- 一个文件长期承担互相冲突的 note type；
- guided onboarding 已扩展成完整 lesson；
- 一个推导足够长，压倒 reference 主体；
- paper-specific 约定污染一般定义；
- detail placement 无法在同一文件中保持清楚。

短小 onboarding 或 optional derivation 不自动触发拆分。
