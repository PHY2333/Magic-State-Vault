# Notes/WORKFLOWS/didactic-design.md

Didactic Architect 把 domain model 与 learner snapshot 转成可审查学习过程。本阶段不写正文。

## 1. 输入

BRIEF、DOMAIN_MODEL、SOURCE_PACKET、LEARNER_SNAPSHOT、NOTE_TYPES、LANGUAGE_PROFILE、pedagogy patterns、explanation contract、depth-and-mainline contract 与必要目标结构。

## 2. 文件决策

明确 note type、entry mode、action、是否拆分及 draft strategy。

## 3. 目标表现

写成读者能够执行的动作，不只写“理解 X”。

## 4. Unit 设计

### Entry / exit / why now

使用 capability id、facet 与 evidence state。

### Pattern 与 phases

每个 phase 记录认知动作、load profile 和 consolidation。

### Concept action ledger

```md
| capability_id | subject | facet | evidence_state | action | first_allowed_phase | local_treatment |
```

`action` 使用 `use | remind | introduce | delay | omit`。它描述概念处理动作，不替代 definition depth、`depth-and-mainline.md` 的 explanation depth 或 detail placement；`compact` 只可作为局部处理说明，机制或推导的紧凑深度写为 `compact_derivation`。

### Definition cards 与 claim ledger

按 `explanation-contract.md`，使用 closure deadline，而非强制 same-sentence closure。

### Depth and placement ledger

按 `depth-and-mainline.md` 为所有 `unverified`、supporting premise、长推导和已有 canonical detail 选择 depth/placement。不得默认 full derivation。

### Mainline contract

每个 unit/phase 写 main question、mainline result、supporting details、return point、latency budget、optional skip test 和 proportionality rationale。

### Opening / language / math / sources

明确首句、术语、记号、链接、不可承诺内容和 language contract。

### Reader card

只包含 reading situation、assumed/not-assumed、expected exit 和 language register；不泄露设计答案。

## 5. 设计原则

- `unverified` 不可直接假设，也不自动长篇重讲；
- concept identity 与 context role 分开；
- 定义在首次 dependent use 前闭合，句法自然优先；
- 工具名称时机由问题／对象／整体决定；
- 支持性细节必须标 depth 与 placement；
- guided reference 默认 local bridge + canonical detail 分工清楚；
- 主线预算与返回点必须明确；
- 默认不要求用户审批教学细节。

## 6. 完成条件

只有 note type/entry mode、目标映射、capability actions、definitions/claims、depth/placement、mainline contract、load、语言、来源、reader card 全部闭合，才能 `status: designed`。
