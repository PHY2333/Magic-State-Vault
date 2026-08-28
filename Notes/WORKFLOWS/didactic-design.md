# Notes/WORKFLOWS/didactic-design.md

Didactic Architect 把 domain model 与 faceted learner snapshot 转成可审查的学习过程。本阶段不写正文。

## 1. 输入

- `BRIEF.md`；
- `DOMAIN_MODEL.md`、`SOURCE_PACKET.md`；
- `LEARNER_SNAPSHOT.md`；
- `Notes/NOTE_TYPES.md`；
- `Notes/LANGUAGE_PROFILE.md`；
- `pedagogy-patterns.md`；
- `explanation-contract.md`；
- 必要的目标正文结构信息。

## 2. 文件决策

对每个目标文件明确：

- `note_type`；
- `entry_mode`；
- action；
- 是否拆分；
- draft strategy：`new-file | whole-file | unit-fragments`。

## 3. 目标表现

每个目标写成读者能够执行的动作，不得只写“理解 X”。

## 4. Unit 设计

### 4.1 Entry 与 exit

- `entry_capabilities`：写 capability id、subject、facet 和 evidence state；
- `exit_capability`：本 unit 后可观察的能力；
- `why_now`：为什么此时需要。

### 4.2 Pattern 与 phases

- 主要模式；
- 必要辅助模式；
- phase 顺序；
- 每个 phase 的认知动作。

### 4.3 Concept action ledger

```md
| capability_id | subject | facet | evidence_state | action | first_allowed_phase | local_treatment |
```

`action`：`use | remind | introduce | delay | omit`。

概念本身与当前角色必须分别列项。

### 4.4 Definition cards

按 `explanation-contract.md` 为所有 `introduce` 术语建立 definition card，并通过 non-circular、discriminative、operational hook、appropriate depth 和 dependency closure。

### 4.5 Explanation claim ledger

登记所有承担 category、role、mechanism、equivalence、inference、motivation 或 boundary 的关键 claims。

每个 claim 必须有 capability dependencies、claim dependencies、closure method、source anchor 和首次允许 phase。

### 4.6 Load profile

每个 phase 记录：

- new entities；
- new relations；
- new notation；
- holding set；
- consolidation。

### 4.7 Opening contract

- first sentence job；
- first paragraph job；
- stable referent；
- allowed vocabulary；
- notation budget；
- link budget；
- forbidden terms/topics；
- closing/transition job。

### 4.8 Language contract

从 `LANGUAGE_PROFILE.md` 选出当前 unit 的：

- primary language；
- permitted abbreviations；
- preferred terms；
- English exceptions；
- prohibited mixed-language forms；
- heading style。

### 4.9 Math 与来源

- 必须写出的对象、公式、推导和例子；
- 只作定位、不要求操作的内容；
- source anchors；
- 不可承诺内容。

### 4.10 Reader card

为每个 unit 预先定义 Blind Reader 所需的最小信息：

- reading situation；
- assumed entry capabilities；
- explicitly not assumed；
- expected exit capability；
- language register。

不得包含设计答案、claim ledger 或 packet 指令。

## 5. 设计原则

- `unverified` 不可直接假设，但不自动长篇从零讲解；
- 概念 identity 与当前 context role 分开；
- 工具名称的时机由对象、问题或整体图景决定；
- 维护语言不进入 packet；
- 一个 unit 可有 phases，避免把复杂度误解为必须拆文件；
- explanation claims 的前提必须在设计阶段闭合；
- 默认不要求用户审批教学细节。

## 6. 完成条件

只有以下条件满足才能写 `status: designed`：

- 文件类型和 entry mode 明确；
- 目标表现映射到 units；
- capability facets 与 actions 完整；
- definition cards 通过；
- explanation claims 闭合；
- 每个 phase 有负荷与 consolidation；
- 术语延后和语言合同明确；
- 来源承诺有锚点；
- reader card 自足且不泄露设计答案；
- 可供 Design Auditor 独立检查。
