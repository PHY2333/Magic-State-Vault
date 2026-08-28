# 已实际读取

- `TASK.md`、`BRIEF.md`。
- `Notes/NOTE_TYPES.md`、`Notes/LANGUAGE_PROFILE.md` 与 Notes v4 的 domain、learner、explanation、didactic、audit、writer contracts。
- 目标文件 `Notes/07-Lifted-Product Code/Hypergraph product code.md`，重点核对第 1–165 行。
- `Notes/06-CCZ Distillation/CSS码中的cochain complex.md`，重点核对第 5–21、110–140 行。
- `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`，重点核对第 4–24 行。
- `Notes/01-量子纠错基础/逻辑基态的表示.md`，重点核对第 168–200 行。
- `Notes/03-Magic State基础/Clifford Twirling 与魔态错误模型.md`，重点核对第 777–791、1402–1410 行。
- `CANONICAL_KNOWLEDGE.md` 中 chain complex、CSS cochain complex 与 HGP 的登记段落。
- `Notes/00-index.md` 中 HGP 的现有路线位置；本任务只读，不修改。
- `Notes/LEARNER/PROFILE.md`、`KNOWLEDGE_STATE.md`、`QUESTIONS.md`；均无可升级本任务能力状态的长期证据。

# 知识单元

## K01 — 经典二进制奇偶校验矩阵的局部含义

- formal_statement: 对二进制矩阵 `A`，每一行规定一条模 2 的奇偶校验条件；本任务只需要这一行级读取，不需要经典码的 kernel、距离或编码过程。
- conditions: 矩阵与向量运算在 `\mathbb F_2` 上。
- canonical_owner: 本任务不新定 canonical owner；HGP 正式笔记已经把 `A,B` 登记为经典种子校验矩阵。
- source_anchors: `Hypergraph product code.md:169–175` 称其为两张经典种子校验矩阵；局部行级解释按显式线性代数读取登记为 `LD04` 的同类计算。
- verification: `repository-derived` + `calculation-verified`。

## K02 — 超图乘积构造的类别

- formal_statement: 超图乘积构造是从两张经典二进制奇偶校验矩阵构造一对 CSS 量子校验矩阵、因而构造 CSS 量子码的方法。
- conditions: 本任务不展开具体 Kronecker blocks、矩阵尺寸或距离参数。
- canonical_owner: `Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- source_anchors: 目标文件第 1、102–165 行；`CANONICAL_KNOWLEDGE.md:267–299`。
- verification: `repository-derived`。

## K03 — 构造与 HGP 码的关系

- formal_statement: 由超图乘积构造得到的量子码称为 HGP 码；“构造”是方法，“HGP 码”是该方法所得对象，二者不是同一类别。
- conditions: 只作类别与产物关系区分，不涉及不同文献的命名史。
- canonical_owner: `Hypergraph product code.md`。
- source_anchors: 目标文件第 1 行及 `CANONICAL_KNOWLEDGE.md:267–289`。
- verification: `repository-derived`。

## K04 — `A,B` 与 `H_X,H_Z` 的角色区分

- formal_statement: `A,B` 是构造的两份经典种子输入；`H_X,H_Z` 是所得量子码的两张校验矩阵输出。输入矩阵不能与输出矩阵混同。
- conditions: U01/U02 不需要写出输出矩阵的 Kronecker block 公式。
- canonical_owner: `Hypergraph product code.md`。
- source_anchors: 目标文件第 5–20、132–153、169–175 行；`CANONICAL_KNOWLEDGE.md:271–288`。
- verification: `source-verified`（仓库来源）。

## K05 — CSS 的当前局部含义

- formal_statement: `H_X,H_Z` 的列对应同一组物理量子比特；`H_X` 的一行给出一条 X 型校验的支撑，`H_Z` 的一行给出一条 Z 型校验的支撑。当前只要求两类校验彼此对易。
- conditions: 不引入 stabilizer group、logical quotient、syndrome 或 metacheck。
- canonical_owner: `Notes/06-CCZ Distillation/CSS码中的cochain complex.md`。
- source_anchors: 该文件第 5–21 行；矩阵同有 `n` 列且行给出两类支撑。
- verification: `repository-derived`。

## K06 — 单比特 Pauli 局部反对易

- formal_statement: 同一量子比特上的 Pauli `X` 与 `Z` 满足 `XZ=-ZX`；交换次序贡献一个负号。
- conditions: 采用标准 `2\times2` Pauli 矩阵。
- canonical_owner: 本任务只登记解释 premise，不改变 canonical。
- source_anchors: `Clifford Twirling 与魔态错误模型.md:1402–1410`；`SOURCE_PACKET.md` 的 `LD01` 显式矩阵乘法。
- verification: `source-verified` + `calculation-verified`。

## K07 — 不同量子比特上的局部作用对易

- formal_statement: 作用在不同张量因子上的 Pauli 算符彼此对易，例如 `(X\otimes I)(I\otimes Z)=(I\otimes Z)(X\otimes I)`。
- conditions: 只使用张量积乘法规则，不要求读者掌握一般 Pauli 群。
- canonical_owner: 本任务的局部推导锚点。
- source_anchors: `SOURCE_PACKET.md` 的 `LD02`。
- verification: `calculation-verified`。

## K08 — 总交换符号由共同支撑位置数决定

- formal_statement: 对一条 X 型校验与一条 Z 型校验，若共同作用位置数为 `w`，交换两条校验的总符号为 `(-1)^w`。
- conditions: 非共同位置上的算符为恒等作用或位于不同量子比特，不贡献负号。
- canonical_owner: 本任务的局部推导锚点。
- source_anchors: `SOURCE_PACKET.md` 的 `LD03`。
- verification: `calculation-verified`。

## K09 — 偶数重叠与成对对易

- formal_statement: 一对 X 型与 Z 型校验对易，当且仅当其支撑的共同位置数为偶数。
- conditions: 由 `(-1)^w=+1` 当且仅当 `w=0 mod 2`。
- canonical_owner: CSS 解释范围由 `CSS码中的cochain complex.md` 承担。
- source_anchors: K06–K08；`SOURCE_PACKET.md:LD03`。
- verification: `calculation-verified`。

## K10 — 矩阵乘积记录所有行对的重叠奇偶

- formal_statement: `(H_XH_Z^T)_{ij}=\sum_q(H_X)_{iq}(H_Z)_{jq}`，在 `\mathbb F_2` 上等于 `H_X` 第 `i` 行与 `H_Z` 第 `j` 行共同非零列数的奇偶。因此 `H_XH_Z^T=0` 等价于所有异型校验对易。
- conditions: `H_X,H_Z` 共享列坐标；等式取值于 `\mathbb F_2`。
- canonical_owner: CSS 条件由 `CSS码中的cochain complex.md` 承担；本任务采用其转置等价写法。
- source_anchors: `CSS码中的cochain complex.md:9–21` 给出共享列与 `H_ZH_X^T=0`；目标文件第 156–165 行给出 `H_XH_Z^T=0`；`SOURCE_PACKET.md:LD04` 给出矩阵元展开。
- verification: `source-verified` + `calculation-verified`。

## K11 — 三项箭头的对象与映射

- formal_statement: 在 `C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0` 中，`C_2` 以 Z 型校验为坐标，`C_1` 以物理量子比特为坐标，`C_0` 以 X 型校验为坐标；`H_Z^T` 把 Z 型校验的选择映成物理支撑，`H_X` 把物理支撑映成其与各 X 型校验的重叠奇偶向量。
- conditions: 三个空间均为二进制向量空间；不引入 homology、degree 或 product complex。
- canonical_owner: 目标 HGP 笔记固定 chain convention；一般 chain complex 由相应主笔记承担。
- source_anchors: 目标文件第 39–51、91–99、156–162 行；`CSS码中的cochain complex.md:48–75,110–140` 的转置方向可交叉核对。
- verification: `repository-derived` + `calculation-verified`。

## K12 — 链复形的当前局部含义

- formal_statement: 一串向量空间和线性映射若任意连续两步的复合为零，就构成链复形；在本三项箭头中，连续复合是 `H_XH_Z^T`，因此“连续两步为零”统一表达全部异型校验对易。
- conditions: 这是本任务所需的局部含义；不承诺 cycle、boundary、homology 或 Künneth。
- canonical_owner: `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`。
- source_anchors: 该文件第 4–24 行；目标文件第 39–51、156–165 行。
- verification: `source-verified`。

## K13 — 任意矩阵 pair 的边界

- formal_statement: 两张共享列的二进制矩阵只有在 `H_XH_Z^T=0` 时才能同时作为这里的 X 型与 Z 型校验矩阵；任意矩阵 pair 不自动满足该条件。
- conditions: 这是必要的 CSS 对易边界，不声称它单独刻画码的所有性质。
- canonical_owner: CSS 局部解释范围。
- source_anchors: K09–K10；`CSS码中的cochain complex.md:15–21`。
- verification: `inference`，由已核对条件的逻辑否定得到。

# Formal dependencies

| dependent | requires | reason |
|---|---|---|
| K04 | K02, K03 | 只有区分方法与所得对象，才能区分构造输入和量子码输出 |
| K05 | K04 | 行支撑和共享列解释针对输出 `H_X,H_Z` |
| K08 | K06, K07 | 总符号由每个共同位置的反对易负号以及不同位置的对易共同决定 |
| K09 | K08 | 偶数重叠等价于 `(-1)^w=+1` |
| K10 | K05, K09 | 矩阵元的行对读取把逐对偶数重叠汇总为矩阵条件 |
| K11 | K05, K10 | 两个映射的坐标意义来自校验支撑与重叠奇偶读取 |
| K12 | K10, K11 | 零复合的具体矩阵是 `H_XH_Z^T`，其 CSS 含义由 K10 给出 |
| K13 | K10 | 任意矩阵 pair 的失败点正是可能存在非零重叠奇偶元素 |

# Explanatory dependencies

| target_explanation | requires_reader_capability | reason |
|---|---|---|
| `A,B` 是输入而 `H_X,H_Z` 是输出 | 能分别识别奇偶校验矩阵的一般含义（identity）与 HGP 中的输入角色（context_role） | 防止把概念身份与当前角色合并 |
| 一对异型校验为何由偶数重叠而对易 | 能读取两行支撑（representation）；能接受或由局部计算得到单比特反对易、异比特对易（rationale） | 这三项是 `(-1)^w` 推导的事实前提 |
| `H_XH_Z^T` 为何记录全部对易条件 | 能把矩阵元展开读成一对行的点积与重叠奇偶（representation） | 否则矩阵等式只是未解释的结论 |
| 三项箭头为何统一表达 CSS 对易 | 能读取三个坐标空间和两个映射（representation）；能识别零复合的当前角色（context_role） | 必须知道复合的输入、输出和各分量意义 |

# Motivational relations

| predecessor_problem_or_result | motivates | reason |
|---|---|---|
| `A,B` 与 `H_X,H_Z` 容易混同 | K04 的角色区分 | 明确构造的数据流与所得码对象 |
| CSS 要求 X 型与 Z 型校验彼此对易 | K06–K10 的局部到矩阵机制 | 需要一个可检查的二进制条件，而不是只宣称“自动对易” |
| 逐行检查所有异型校验对繁琐 | K10 的单一矩阵等式 | 一个零矩阵条件汇总所有行对 |
| 矩阵零乘积看似只是代数约束 | K11–K12 的三项箭头 | 给出该零乘积作为连续映射复合的整体位置 |
| 任意矩阵 pair 可能不对易 | HGP 构造需要内建零复合 | 说明构造不能只产生两张形状相容的矩阵 |

# Reference relations

| knowledge_unit | owner | owned_scope |
|---|---|---|
| K02–K04 | `Hypergraph product code.md` | HGP 构造、输入种子、输出校验矩阵与所得码 |
| K05, K10, K13 | `CSS码中的cochain complex.md` | CSS 矩阵支撑与零乘积条件的一般解释 |
| K12 | `Chain complex 与 cochain complex.md` | 链复形与连续复合为零的一般定义 |
| K06 | `Clifford Twirling 与魔态错误模型.md` + 本地计算 | 单比特 `X,Z` 交换符号 |
| K07–K09 | 本任务 `SOURCE_PACKET.md` local derivations | 异比特张量因子对易、总符号与偶数重叠机制 |
| K11 | HGP/CSS/chain 三个既有 owner 的局部重述 | 当前三项箭头的 CSS 坐标解释 |

# Explanatory premise inventory

| premise_id | statement | supports_claims | source_anchor | verification |
|---|---|---|---|---|
| PR01 | 同一量子比特上的 `X` 与 `Z` 满足 `XZ=-ZX` | 共同位置交换产生负号 | `Clifford Twirling…:1402–1410`; `SOURCE_PACKET.md:LD01` | `source-verified`, `calculation-verified` |
| PR02 | 不同量子比特上的 Pauli 作用彼此对易 | 非共同位置不产生交换负号 | `SOURCE_PACKET.md:LD02` | `calculation-verified` |
| PR03 | 一对 X 型与 Z 型校验交换时，总符号为每个共同作用位置负号之积，即 `(-1)^w` | 偶数重叠对应对易 | `SOURCE_PACKET.md:LD03` | `calculation-verified` |
| PR04 | `(H_XH_Z^T)_{ij}` 是相应两行的重叠数模 2 | 矩阵零乘积等价于所有行对偶数重叠 | `SOURCE_PACKET.md:LD04`; `CSS码中的cochain complex.md:9–21` | `calculation-verified`, `source-verified` |
| PR05 | `H_X,H_Z` 共享物理量子比特列，行分别表示 X 型和 Z 型校验支撑 | 把矩阵行对连接到 Pauli 校验对 | `CSS码中的cochain complex.md:9–18` | `repository-derived` |
| PR06 | 链复形的连续映射复合为零 | 把 `H_XH_Z^T=0` 命名为三项链复形条件 | `Chain complex 与 cochain complex.md:4–24` | `source-verified` |
| PR07 | 二进制行 `x` 表示 X 型校验在 `x_q=1` 的位置作用 `X`、其余位置作用 `I`；Z 型行 `z` 类似表示 `Z(z)` | 把矩阵行支撑连接到整条泡利校验的交换符号 | `SOURCE_PACKET.md:LD03`; `CSS码中的cochain complex.md:23–29` 的 X 支撑表示，Z 型按同一 CSS 约定 | `calculation-verified`, `repository-derived` |

# 约定与边界

- 全部二进制支撑、矩阵乘积与重叠奇偶在 `\mathbb F_2` 上。
- 本任务使用目标 HGP 笔记的 chain 方向：`C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0`，所以零复合写作 `H_XH_Z^T=0`。
- `CSS码中的cochain complex.md` 使用对偶方向并写 `H_ZH_X^T=0`；两式互为转置，表达同一行对正交条件，不是来源冲突。
- U01/U02 范围不含 Kronecker blocks、`A/B` 尺寸、total degree、两路径抵消、homology、Künneth、stabilizer group 或 logical quotient。
- U01/U02 只说明保证条件及其链复形包装，不展开 HGP block 公式如何具体实现该条件。

# 缺失与冲突

- 仓库没有找到一句可直接、独立承担“不同量子比特上的 Pauli 作用对易”的自然中文来源；已按用户授权用 `LD02` 的显式张量积计算闭合，不留作模型常识。
- 仓库现有 CSS 来源偏向 `H_ZH_X^T=0` 的 cochain 方向，目标 HGP 来源采用 `H_XH_Z^T=0` 的 chain 方向；二者经转置严格一致。
- 未发现会阻止 U01/U02 设计的来源冲突或未核对关键承诺。

# 可供设计使用的结论

- 构造类别、所得码、种子输入与量子校验输出可以分别陈述，不需要借助 Künneth 或维护性链接。
- PR01–PR04 已为 Pauli 局部规则、总符号与矩阵重叠解释提供完整来源／局部计算闭包。
- 三项箭头的三个空间、两个映射和零复合均有仓库约定支撑，可只在对象与用途闭合后使用“链复形”名称。
- 所有用户指定的禁止主题都可延后，不影响本次出口能力。
