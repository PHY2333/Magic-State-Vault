# Notes/WORKFLOWS/explanation-contract.md

本文件规定教学设计中的 explanation claim ledger 与 definition cards。它解决“术语都定义了，但解释仍依赖读者不知道的事实”这一问题。

## 1. Explanation claim

需要登记的不是每个普通陈述，而是承担解释作用的命题，尤其包含：

```text
因为、所以、意味着、对应、等价、保证、来自、只要……就……
```

Claim 类型：

- `category`：对象属于什么类别；
- `definition`：对象当前如何定义；
- `role`：对象在当前构造中的作用；
- `mechanism`：为什么某个过程产生某个结果；
- `equivalence`：两个条件为何等价；
- `inference`：由前文推出新结论；
- `motivation`：为什么此时需要新对象或工具；
- `boundary`：当前结论能推出什么、不能推出什么。

## 2. Claim ledger

```md
| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | source_anchor | first_allowed_phase |
```

`closure_method` 只能是：

- `use`：entry capability 已 operational/fluent；
- `remind`：短提醒即可恢复；
- `define`：在当前位置给局部定义；
- `derive`：写出推导；
- `demonstrate`：用最小例子或计算展示；
- `delay`：前提未闭合，延后。

每个 claim 必须能由以下集合推出：

```text
Reader entry capabilities
+ 当前 phase 更早已闭合 claims
+ 当前句提供的定义、推导或示范
```

## 3. Claim dependency closure

Design Auditor 逐 claim 检查：

1. capability dependencies 是否按 facet 建模；
2. claim dependencies 是否先于当前 claim；
3. closure method 是否真实可执行；
4. source anchor 或局部计算是否足够；
5. 是否把“没有新术语”误当成“没有新前提”。

例如：

```text
“偶数重叠使 X 型与 Z 型校验对易”
```

至少依赖：

- 同一量子比特上的 X 与 Z 反对易；
- 不同量子比特上的 Pauli 作用彼此对易；
- 总交换符号是各共同作用位置符号的乘积。

## 4. Definition card

每个需要 `introduce` 的术语或对象建立：

```md
### D01 — <term>
- definition_depth:
- category:
- basic_data:
- current_function:
- discriminates_from:
- capability_dependencies:
- prohibited_shortcuts:
- first_allowed_phase:
```

## 5. Definition adequacy

局部定义必须通过：

- **non-circular**：不用同义反复解释自己；
- **discriminative**：能与相邻对象区分；
- **operational hook**：读者知道怎样识别、读取或使用；
- **appropriate depth**：只讲当前需要的深度；
- **dependency closure**：不使用未引入专名或事实。

不合格示例：

> 奇偶校验矩阵是用于记录奇偶校验关系的矩阵。

较合格的局部提醒：

> 奇偶校验矩阵的每一行规定一条模 2 的奇偶校验条件。

## 6. First-sentence contract

Guided entry 的第一句通常应：

- 建立一个稳定对象；
- 给出类别和最小来源数据；
- 不同时处理多义性、历史、边界和下游用途。

除非术语多义就是当前问题，不以“X 既指 A，也指 B”开头。需要区分构造与所得对象时，优先用连续两句建立关系。

## 7. Concept 与 role

Definition card 负责概念本身；role claim 负责当前任务中的作用。二者不得相互替代。

例如：

```text
奇偶校验矩阵是什么          → definition card
A、B 在 HGP 中是两份种子输入 → role claim
```
