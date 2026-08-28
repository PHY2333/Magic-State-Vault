# Mapping scope

- task_id: 20260828-hgp-v5-pilot
- repository version: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6
- target: Notes/07-Lifted-Product Code/Hypergraph product code.md
- mapped units: U01、U02-P1、U02-P2 所需事实，以及它们与正式 HGP 后续段落的边界。
- role boundary: 本文件只登记事实、来源、premise、owner 和已有 detail；不决定教学顺序、解释深度、主线／optional placement 或整合范围。

# 已实际读取并核对

- Notes/AGENTS.md、Notes/NOTE_TYPES.md、Notes/WORKFLOWS/domain-contract.md。
- 本任务 TASK.md、BRIEF.md。
- 正式目标 Notes/07-Lifted-Product Code/Hypergraph product code.md，完整读取并逐行核对第 1–180 行及全部后续标题。
- CANONICAL_KNOWLEDGE.md 的 chain/CSS 段（第 75–140 行）与 HGP 段（第 267–300 行）。
- Notes/06-CCZ Distillation/CSS码中的cochain complex.md，完整读取；重点复核第 5–32、48–75、110–140 行。
- Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md，完整读取；重点复核第 4–24、173–210 行。
- Notes/03-Magic State基础/Clifford Twirling 与魔态错误模型.md 第 770–795、1395–1415 行。
- Notes/01-量子纠错基础/逻辑基态的表示.md 第 168–200 行。
- Notes/00-index.md 的 HGP 路线项与维护区；只读。
- v4 历史任务的 DOMAIN_MODEL.md 与 SOURCE_PACKET.md；其中所有仍用于 v5 的仓库锚点均已在当前 commit 重新打开核对，历史任务本身不作为数学权威。

# Knowledge units

## K01 — 经典二进制奇偶校验矩阵的一般含义

- formal statement: 若 H 的第 i 行为 h_i，则该行规定二进制向量 c 应满足的模 2 条件

  $$
  h_i c=\sum_q (h_i)_q c_q=0\pmod 2.
  $$

  因而“一行规定一条模 2 的奇偶校验条件”是本任务所需的一般含义。
- conditions: H 与 c 均在 \(\mathbb F_2\) 上；本任务不需要经典码的编码过程、距离或 kernel 结构。
- canonical owner: 仓库没有独立承担该一句级定义的正式 owner；目标 HGP 笔记把 A、B 称为经典种子校验矩阵并把行标为经典校验。
- source anchors: Hypergraph product code.md:8–23；SOURCE_PACKET.md 的 LD00。
- verification: calculation-verified；“A、B 为经典种子校验矩阵”另为 source-verified。

## K02 — 超图乘积构造的类别

- formal statement: 超图乘积构造是一种从两张经典二进制奇偶校验矩阵产生一对 CSS 量子校验矩阵、从而构造 CSS 量子码的方法。
- conditions: U01/U02 不要求写出 Kronecker blocks、尺寸或距离参数。
- canonical owner: Notes/07-Lifted-Product Code/Hypergraph product code.md。
- source anchors: 目标第 1、5–20、102–165 行；CANONICAL_KNOWLEDGE.md:267–299。
- verification: source-verified。

## K03 — HGP 码与构造的关系

- formal statement: 由超图乘积构造得到的量子码称为 HGP 码；构造是方法，HGP 码是该方法的产物。
- conditions: 只作 category 与 product-of-construction 区分，不处理术语史。
- canonical owner: Hypergraph product code.md。
- source anchors: 目标第 1 行与 CANONICAL_KNOWLEDGE.md:267–288。
- verification: source-verified。

## K04 — A、B 与 H_X、H_Z 的角色

- formal statement: A、B 是 HGP 构造的两份经典种子输入；H_X、H_Z 是构造所得量子码的 X 型、Z 型校验矩阵输出。输入与输出不可混同。
- conditions: 当前 unit 只需角色与数据流，不需输出 block 公式。
- canonical owner: Hypergraph product code.md。
- source anchors: 目标第 5–20、102–165、169–175 行；CANONICAL_KNOWLEDGE.md:271–288。
- verification: source-verified。

## K05 — CSS 的当前局部含义

- formal statement: H_X 与 H_Z 的列对应同一组物理量子比特；H_X 的一行给出一条 X 型校验的支撑，H_Z 的一行给出一条 Z 型校验的支撑。作为这里的 CSS 校验输出，所有 X 型与 Z 型校验必须彼此对易。
- conditions: 当前局部含义不需要 stabilizer group、logical quotient、syndrome 或 metacheck。
- canonical owner: Notes/06-CCZ Distillation/CSS码中的cochain complex.md。
- source anchors: CSS码中的cochain complex.md:7–21；两矩阵同有 n 列，行给出两类支撑并满足零乘积。
- verification: source-verified。

## K06 — 二进制行支撑到逐位置作用

- formal statement: 对二进制行 x，一条 X 型校验在 x_q=1 的位置作用 X，在 x_q=0 的位置作用 I；Z 型行 z 类似使用 Z 与 I。可写为

  $$
  X(x)=\bigotimes_q X^{x_q},\qquad
  Z(z)=\bigotimes_q Z^{z_q}.
  $$
- conditions: 只用 X、Z、I；不需要一般 Pauli group。
- canonical owner: CSS码中的cochain complex.md 对 X support 有稳定表示；Z 型由同一 CSS 行支撑约定对称得到。
- source anchors: CSS码中的cochain complex.md:15–29；SOURCE_PACKET.md:LD03。
- verification: source-verified + calculation-verified。

## K07 — 同一量子比特上的局部反对易

- formal statement: 同一量子比特上的 X 与 Z 满足 XZ=-ZX；交换次序贡献一个负号。
- conditions: 采用标准 \(2\times2\) Pauli 矩阵。
- canonical owner: Clifford Twirling 与魔态错误模型.md 给出稳定乘法恒等式；完整逐项矩阵乘法仅作为本任务可复算 local derivation。
- source anchors: Clifford Twirling 与魔态错误模型.md:1402–1410；SOURCE_PACKET.md:LD01。
- verification: source-verified + calculation-verified。

## K08 — 不同量子比特上的作用对易

- formal statement: 作用在不同张量因子上的局部 Pauli 作用彼此对易，例如

  $$
  (X\otimes I)(I\otimes Z)
  =(I\otimes Z)(X\otimes I).
  $$
- conditions: 只使用张量积乘法规则；不需要一般 Pauli 群。
- canonical owner: 未找到一句直接承担此事实的稳定中文 owner；本任务提供显式 local derivation。
- source anchors: SOURCE_PACKET.md:LD02。
- verification: calculation-verified。

## K09 — 总交换符号

- formal statement: 对一条 X 型校验与一条 Z 型校验，若共同作用位置数为 w，则交换两条校验的总符号为 \((-1)^w\)。
- conditions: 每个共同位置按 K07 贡献一个负号；不同位置的重排按 K08 不贡献额外符号。
- canonical owner: 本任务 local derivation；CSS 一般职责仍由 CSS码中的cochain complex.md 承担。
- source anchors: K06–K08；SOURCE_PACKET.md:LD04。
- verification: calculation-verified。

## K10 — 偶数重叠与一对异型校验的对易

- formal statement: 一条 X 型与一条 Z 型校验彼此对易，当且仅当两条行支撑的共同位置数为偶数。
- conditions: \((-1)^w=+1\) 当且仅当 \(w=0\pmod2\)。
- canonical owner: CSS 局部矩阵条件由 CSS码中的cochain complex.md 承担；机制由本任务 local derivation 闭合。
- source anchors: K09；SOURCE_PACKET.md:LD04。
- verification: calculation-verified。

## K11 — 矩阵元记录重叠奇偶

- formal statement:

  $$
  (H_XH_Z^T)_{ij}
  =\sum_q(H_X)_{iq}(H_Z)_{jq}
  $$

  是 H_X 第 i 行与 H_Z 第 j 行共同非零列数的模 2 奇偶。因此 \(H_XH_Z^T=0\) 等价于每一对异型行均有偶数重叠，也等价于所有异型校验彼此对易。
- conditions: H_X、H_Z 共享物理量子比特列；矩阵运算在 \(\mathbb F_2\) 上。
- canonical owner: CSS码中的cochain complex.md；目标 HGP 笔记采用其转置等价的 chain 方向。
- source anchors: CSS码中的cochain complex.md:9–21；目标第 156–165 行；SOURCE_PACKET.md:LD05。
- verification: source-verified + calculation-verified。

## K12 — 共享列不自动保证 CSS 条件

- formal statement: 两张共享列的二进制矩阵并不自动满足 \(H_XH_Z^T=0\)；最小反例 \(H_X=H_Z=[1]\) 的乘积为 [1]。
- conditions: 该反例只否定“共享列自动推出对易”，不刻画 CSS 码的其它性质。
- canonical owner: CSS 条件的一般 owner；反例为本任务 local derivation。
- source anchors: SOURCE_PACKET.md:LD06。
- verification: calculation-verified。

## K13 — 三项箭头中的空间与映射

- formal statement: 在

  $$
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0
  $$

  中，\(C_2=\mathbb F_2^{r_Z}\) 以 Z 型校验为坐标，\(C_1=\mathbb F_2^n\) 以物理量子比特为坐标，\(C_0=\mathbb F_2^{r_X}\) 以 X 型校验为坐标。H_Z^T 把 Z 型校验选择映成物理支撑；H_X 把物理支撑映成与各 X 型校验的重叠奇偶向量。
- conditions: 三个空间均为二进制向量空间；这里只解释坐标和映射，不引入 homology 或 product degree。
- canonical owner: HGP 目标固定 chain 方向；CSS owner 提供对偶 cochain 方向。
- source anchors: 目标第 39–51、91–99、156–162 行；CSS码中的cochain complex.md:48–75、110–140；SOURCE_PACKET.md:LD07。
- verification: source-verified + calculation-verified。

## K14 — 链复形的当前局部含义

- formal statement: 一串向量空间与线性映射若连续两步复合为零，就构成链复形。对 K13 的三项箭头，连续复合为 \(H_XH_Z^T\)，所以零复合统一表达全部异型校验对易。
- conditions: 只承诺当前三项箭头所需含义；不承诺 degree、cycle、boundary、homology 或 Künneth。
- canonical owner: Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md。
- source anchors: 该文件第 4–24 行；目标第 39–51、156–165 行。
- verification: source-verified。

## K15 — HGP 后续怎样实际保证零复合

- formal statement: 正式 HGP 构造在后续用 A、B 写出

  $$
  H_X=[A\otimes I_{m_B}\mid I_{m_A}\otimes B],
  \qquad
  H_Z=[I_{n_A}\otimes B^T\mid A^T\otimes I_{n_B}],
  $$

  并由两条 product paths 均为 \(A\otimes B\)，在特征 2 中相加为零，得到 \(H_XH_Z^T=0\)。
- conditions: 这是 U01/U02 之后正式正文已有的下一层 canonical detail，不是本次 unit 要展开的 Kronecker-block 证明。
- canonical owner: Hypergraph product code.md。
- source anchors: 目标第 102–165 行；CANONICAL_KNOWLEDGE.md:271–288。
- verification: source-verified。

# Formal dependencies

| dependent | requires | reason |
|---|---|---|
| K04 | K02, K03 | 先区分方法与所得对象，才能精确区分输入与输出 |
| K05 | K04 | 共享列和行支撑针对输出 H_X、H_Z，而不是种子 A、B |
| K09 | K06, K07, K08 | 总符号需要逐位置作用、同位置负号和异位置对易 |
| K10 | K09 | 偶数重叠由总符号为正得到 |
| K11 | K05, K10 | 矩阵元读取把逐对重叠汇总为全部校验条件 |
| K12 | K11 | 非零矩阵元即给出失败的行对 |
| K13 | K05, K11 | 空间坐标与两个映射的用途来自支撑和重叠奇偶 |
| K14 | K11, K13 | 需要先识别具体复合及其 CSS 含义 |
| K15 | K04, K14 | 后续 HGP block 构造具体实现前述零复合要求 |

# Explanatory dependencies

| target_explanation | requires_reader_capability | reason |
|---|---|---|
| A、B 是输入而 H_X、H_Z 是输出 | 分别识别奇偶校验矩阵的一般含义与 HGP 中的 context role | concept identity 与 context role 不可合并 |
| 为什么输出不能是任意矩阵 pair | 能读取 H_X、H_Z 的共享列和各行支撑；知道 CSS 当前要求异型校验对易 | 否则零乘积只是无动机的附加式子 |
| 一对异型校验为何由偶数重叠而对易 | 能把一行读成逐位置 X/Z/I；能依据 K07、K08 处理局部交换 | 这些是 \((-1)^w\) 的事实 premises |
| 为什么矩阵积汇总全部对易条件 | 能展开一个矩阵元并读成一对行的重叠奇偶 | 否则从逐对条件跳到零矩阵不闭合 |
| 三项箭头为何统一表达 CSS 对易 | 能识别三个坐标空间、两个映射和它们的连续复合 | 名称本身不能替代对象与用途 |
| 下一步怎样由 HGP 构造保证条件 | 已理解 K14 的零复合目标 | K15 才回答 A、B 如何具体产生满足条件的映射 |

# Motivational relations

| predecessor_problem_or_result | motivates | reason |
|---|---|---|
| “超图乘积构造”与“HGP 码”类别容易混同 | K02–K03 | 建立稳定第一对象与构造—产物关系 |
| A、B 与 H_X、H_Z 都是矩阵，角色容易混同 | K04 | 明确构造的数据流 |
| CSS 输出要求异型校验彼此对易 | K06–K11 | 把要求变成可检查的二进制机制 |
| 逐行检查所有异型校验对繁琐 | K11 | 单个零矩阵条件汇总所有行对 |
| 共享列只说明同一坐标集 | K12 | 显示仍需额外的零乘积保证 |
| 零矩阵条件看似孤立 | K13–K14 | 把它放进“选择 → 支撑 → 重叠奇偶”的连续映射 |
| 零复合给出应满足的结构目标 | K15 | 后续用 A、B 构造两支映射并证明复合恒为零 |

# Reference relations

| knowledge_unit | owner | owned_scope |
|---|---|---|
| K02–K04, K15 | Hypergraph product code.md | HGP 构造、种子输入、输出 blocks、乘积零复合 |
| K05, K06, K11 | CSS码中的cochain complex.md | CSS 行支撑、共享物理坐标、矩阵到 complex 的转换及零乘积 |
| K14 | Chain complex 与 cochain complex.md | 链复形与连续两步为零的一般定义 |
| K07 | Clifford Twirling 与魔态错误模型.md | 单比特 Pauli 乘法恒等式与交换符号 |
| K08–K10, K12 | 本任务 SOURCE_PACKET.md local derivations | 异比特对易、总符号、偶数重叠与最小反例 |
| K13 | HGP、CSS、chain 三个 owner 的当前局部重述 | 当前三项箭头的 CSS 坐标解释 |

# Explanatory premise inventory

| premise_id | statement | supports_claims | source_anchor | verification |
|---|---|---|---|---|
| PR01 | 经典二进制奇偶校验矩阵的一行 h_i 规定 \(h_ic=0\pmod2\) | K01 | SOURCE_PACKET.md:LD00；目标:8–23 | calculation-verified |
| PR02 | H_X、H_Z 共享 n 个物理列，行分别给出 X 型与 Z 型支撑 | K05, K06, K11 | CSS码中的cochain complex.md:7–21 | source-verified |
| PR03 | 二进制行可读成支撑处 X/Z、其余位置 I 的逐位置作用 | K06, K09 | CSS码中的cochain complex.md:23–29；SOURCE_PACKET.md:LD03 | source-verified + calculation-verified |
| PR04 | 同一量子比特上的 X、Z 满足 XZ=-ZX | K07, K09 | Clifford Twirling…:1402–1410；SOURCE_PACKET.md:LD01 | source-verified + calculation-verified |
| PR05 | 不同量子比特上的作用彼此对易 | K08, K09 | SOURCE_PACKET.md:LD02 | calculation-verified |
| PR06 | 交换整条校验时，每个共同位置恰贡献一个负号，其余位置不贡献 | K09, K10 | SOURCE_PACKET.md:LD04 | calculation-verified |
| PR07 | \((H_XH_Z^T)_{ij}\) 是对应两行点积，即共同非零列数模 2 | K11 | SOURCE_PACKET.md:LD05 | calculation-verified |
| PR08 | 零矩阵表示每一个 i,j 分量均为零 | K11 | 线性代数定义；SOURCE_PACKET.md:LD05 | calculation-verified |
| PR09 | H_Z^T 把校验选择映成行支撑的模 2 叠加，H_X 的输出分量是与相应 X 行的点积 | K13 | CSS码中的cochain complex.md:48–75、110–140；SOURCE_PACKET.md:LD07 | source-verified + calculation-verified |
| PR10 | 链复形要求任意连续两步复合为零 | K14 | Chain complex 与 cochain complex.md:4–24 | source-verified |
| PR11 | HGP 两条 product paths 都给出 \(A\otimes B\)，在 \(\mathbb F_2\) 上相加为零 | K15 | 目标:102–165；CANONICAL:271–288 | source-verified |

# Canonical detail inventory

本表只报告“已有多少 detail”；evidence state 与 available depth 均不替 Architect 选择本次 explanation depth 或 placement。

| detail_id | topic | canonical_owner | available_depth | stable_anchor | local_restatement_allowed | notes |
|---|---|---|---|---|---|---|
| D01 | 奇偶校验矩阵一行的模 2 条件 | 无独立 owner；目标仅给 seed/check 语境 | statement | 目标:8–23；LD00 | yes | 可作局部提醒；仓库没有一篇需复制的长定义 |
| D02 | CSS 的共享物理列、两类行支撑与零乘积 | CSS码中的cochain complex.md | compact_derivation | 该文:7–32、110–140 | yes | 当前 unit 可保留必要 local bridge；原文的 stabilizer/syndrome 语言不必随之带入 |
| D03 | CSS logical quotient、syndrome 与 metacheck | CSS码中的cochain complex.md | full_derivation | 该文:40–166、240 以后 | no | 不是 U01/U02 出口能力；不得为“自足”而复制 |
| D04 | 同比特 Pauli 交换符号 | Clifford Twirling 与魔态错误模型.md | statement | 该文:777–791、1402–1410 | yes | 稳定来源给出符号与乘法恒等式 |
| D05 | 显式 \(2\times2\) Pauli 矩阵逐项相乘 | 无独立 canonical owner；本任务 LD01 | full_derivation | SOURCE_PACKET.md:LD01 | yes | 用户明确：完整矩阵计算不是当前出口能力；是否使用及放置由 Architect 决定，不能因 learner 状态 unverified 自动占据主线 |
| D06 | 异比特作用的张量因子对易 | 无直接稳定中文 owner；本任务 LD02 | compact_derivation | SOURCE_PACKET.md:LD02 | yes | 局部计算可复算，不得伪称来源原文已有完整证明 |
| D07 | 一般二进制辛对易判据 | 逻辑基态的表示.md | statement | 该文:168–200 | no | 只作 Contract Auditor 交叉核对；一般辛矩阵会显著超出当前局部 CSS 语言 |
| D08 | chain/cochain 的零复合及 (co)homology | Chain complex 与 cochain complex.md | full_derivation | 该文:4–24、28–210 | yes | 当前 unit 允许只重述三项箭头与零复合；几何例子、cycle、homology 由 owner 承担 |
| D09 | HGP blocks 与两路径抵消 | Hypergraph product code.md | compact_derivation | 目标:102–165；CANONICAL:271–288 | no for U01/U02 | 这是本次结尾之后的 canonical next detail；U01/U02 不完整复制 |
| D10 | HGP 具体 product spaces 与两物理扇区 | Hypergraph product code.md | compact_derivation | 目标:72–100 | no for U01/U02 | 与一般三项箭头相邻但属于后续 HGP-specific 实例化 |
| D11 | HGP logical quotient 与 Künneth 分解 | HGP、CSS 与 Künneth 各 owner | full_derivation | 目标:53–70、309–362 | no | 明确超出 U01/U02；Künneth 不进入开头 |

# 正式 HGP 中与 U01/U02 的重复／竞争 inventory

此表只报告整合风险，不决定 replace、insert 或保留。

| target range | existing content | relation to staged U01/U02 | unique content that must not be silently lost | fit question for Integration Preview |
|---|---|---|---|---|
| 第 1 行 | 旧 opening 同时压入 HGP、输入、自动对易、三个链接与 Künneth 边界 | 与 U01 的第一对象、构造—所得码关系直接竞争 | “自动对易”是后续需解释的承诺；链接与 Künneth 维护边界不是新开头内容 | old opening 与 new opening 不能并列竞争 |
| 第 3–23 行 | A、B 的尺寸、二项链复形与行／列 degree 标签 | 与 U01 的“两个经典输入”部分重复；细节深度更高 | A、B 尺寸、二项链复形表示及变量／校验 convention 是后续 blocks 所需 | 若替换开头，需明确这些 HGP-specific 数据放在何处 |
| 第 39–51 行 | 一般三项链复形与 \(H_X=\partial_1,H_Z=\partial_2^T\) | 与 U02-P2 的三项箭头和两映射角色直接重复 | 本库固定的 \(\partial_1,\partial_2\) convention | 新旧表达应合并为一个稳定说明，不能重复命名 |
| 第 53–70 行 | logical Z quotient、对偶 cochain 与 logical X owner link | 不属于 U01/U02 出口，但位于可能被替换的开头范围 | logical quotient 与 chain/cochain convention 边界 | 任何范围替换都必须保留或有明确迁移位置 |
| 第 72–100 行 | product 的具体 C_2、C_1、C_0 及两个物理比特扇区 | 与 U02-P2 的一般坐标空间存在术语回声，但内容是 HGP-specific 实例化 | 两个物理扇区、product degree 与四类指标 | 需检查一般箭头到具体 product spaces 的过渡，避免同义重述 |
| 第 102–165 行 | HGP blocks、两路径抵消、\(H_XH_Z^T=0\) 与“不碰巧正交” | U02 先解释条件；这里给出 HGP 实现和证明。第 156–165 行会重复零复合结论 | 具体 block 公式与两路径抵消正是后续 canonical detail | 保留必要的 result return，但避免再次从头解释 Pauli／重叠机制 |
| 第 167 行以后 | S007 convention、Tanner 边、参数、LP 过渡 | 与 U01/U02 无直接正文重复 | 全部为正式 HGP 后续职责 | pilot 不设计或改写这些段落 |

# 范围与 detail 约束

- 用户明确指定：完整 Pauli \(2\times2\) 矩阵逐项计算不是当前出口能力。
- “unverified” learner evidence 不自动要求 full derivation；本 mapping 不从 evidence state 推导 explanation depth。
- 上游 CSS owner 已有共享列、行支撑、零乘积、三项 cochain 映射和更深 logical detail。
- 上游 Pauli owner 有交换符号及 \(ZX=iY,\ XZ=-iY\)；异比特作用的直接中文证明缺失，由 LD02 局部计算闭合。
- U01/U02 所需 local bridges 与 canonical owner 的长证明可以分开：是否 mainline、optional 或 upstream bridge 由 Architect 在 depth/placement ledger 决定。
- Künneth、Kronecker blocks、A/B 尺寸、total degree、两路径抵消、homology 与 logical quotient 均不是 U01/U02 要展开的 detail；K15 只登记后续 canonical 事实以支持主线返回。

# Convention reconciliation

- 本任务采用目标 HGP 的 chain 方向：

  $$
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0,
  \qquad H_XH_Z^T=0.
  $$

- CSS码中的cochain complex.md 使用对偶方向

  $$
  C^0\xrightarrow{H_X^T}C^1\xrightarrow{H_Z}C^2,
  \qquad H_ZH_X^T=0.
  $$

- 两个矩阵等式互为转置，表达同一组 X 行与 Z 行的二进制正交条件，不构成来源冲突。

# Missing, conflict, blocker

- missing direct source: 未找到一句直接证明“不同量子比特上的 Pauli 作用对易”的稳定中文正文；LD02 以张量积乘法显式闭合。
- missing standalone owner: “奇偶校验矩阵一行规定模 2 条件”没有独立 canonical note；LD00 可复算，目标文件确认 A、B 的 seed-check 身份。
- source limitation: 上游 Pauli 来源给出乘法恒等式而非完整 \(2\times2\) 逐项计算；LD01 可供核对，但完整计算不是当前出口能力。
- convention conflict: 无；chain/cochain 两个零乘积式经转置一致。
- blocker: 无。Architect 无需重新遍历仓库即可建立 definition/claim、depth/mainline 与 duplication ledgers。
