# Notes/WORKFLOWS/explanation-contract.md

本文件规定 explanation claim ledger、definition cards 与 closure deadline。

## 1. Explanation claim

登记承担解释作用的 category、definition、role、mechanism、equivalence、inference、motivation 和 boundary claims，尤其含“因为、所以、意味着、等价、保证、来自”等句子。

## 2. Claim ledger

```md
| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | closure_deadline | source_anchor | first_allowed_phase |
```

`closure_method`：`use | remind | define | derive | demonstrate | delay`。

`closure_deadline`：

- `immediate_label`：符号、指代或对象类别若不立即说明会无法继续读；
- `before_first_dependency`：默认，在首次依赖它推理之前闭合；
- `preview_then_close`：可先作为定位标签出现，但在任何操作、等价或因果 claim 前闭合。

同一句闭合不是默认要求。相邻句或相邻段只要在首次 dependent use 前完成即可。

## 3. Claim dependency closure

每个 claim 必须由 reader entry capabilities、前文已闭合 claims 与当前位置的定义／推导／示范推出。没有新术语不等于没有新前提。

## 4. Definition card

```md
### D01 — <term>
- definition_depth:
- category:
- basic_data:
- current_function:
- discriminates_from:
- capability_dependencies:
- prohibited_shortcuts:
- preview_allowed:
- closure_deadline:
- first_allowed_phase:
```

## 5. Definition adequacy

必须 non-circular、discriminative、有 operational hook、appropriate depth、dependency closure，并在首次 dependent use 前完成。

允许自然的两三句定义；不得为了 same-sentence closure 写出过载长句。

## 6. First-sentence contract

Guided 第一段建立稳定对象和最小数据。第一句不必同时完成所有局部定义；只要后续句在首次推理前闭合即可。

## 7. Concept 与 role

Definition card 管概念本身；role claim 管当前任务中的作用。二者不得替代。
