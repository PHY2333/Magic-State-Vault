---
task_id: 20260827-s007-lp-learning-path
based_on_context_version: 1
approval: approved
planner: chatgpt-pro
---

# S007-LP 学习路径写作计划

# 上下文检查

- 已采用：
  - `Notes/WORKING/note-tasks/20260827-s007-lp-learning-path/TASK.md`；
  - `Notes/WORKING/note-tasks/20260827-s007-lp-learning-path/CONTEXT.md`；
  - `Notes/WORKFLOWS/planning-contract.md`；
  - `Notes/WORKFLOWS/note-writing.md`；
  - `Notes/WRITING_GUIDE.md`；
  - `CANONICAL_KNOWLEDGE.md` 中 cochain tensor、Künneth、balanced tensor、HGP、LP 的 ownership；
  - `Notes/00-index.md` 第 7 条及目录归属；
  - 三篇 legacy candidate notes；
  - `Cochain complex 的 tensor product.md`、`Balanced tensor product 与 coinvariant quotient.md`、`CSS码中的cochain complex.md` 的相关部分；
  - `Translations/S007.full.zh-CN.md` 的图 1、§2.2、§3.1、§4.2.1、§6、图 12、表 3；
  - `Papers/S007_2026_Liu_architecture_compilation_codesign.pdf` pp.12–13；
  - `Papers/SOURCES.md` 中 S007 的来源登记。
- 上下文结论：现有材料足以规划一条“先理解 HGP 外层乘积，再理解 LP 的 lift 数据，最后读取 S007 四阶段执行”的学习路径。
- 仍有但不阻塞规划的不确定项：
  1. S007 §6 只写出一个 `3×7` 环值矩阵 `A`，没有给出具体 LP 实例的第二个因子、adjoint convention 或 self-product 声明；本任务不得补猜。
  2. $[\![2610,744,d\le 16]\!]$ 是 S007 引用文献 [6] 后直接给出的参数；现有材料不足以从式 (2) 独立推导 `2610`、`744` 或距离界。
  3. S007 只说明 `x^k` 诱导 cyclic shift，没有固定与本库 `Pe_t=e_{t+1}` 完全相同的正负方向；正文必须把方向写成“本库采用的 convention”，不能冒充原文额外结论。
  4. 现有 Künneth、HGP、LP 笔记中的部分一般性来源尚未纳入本地 `Papers/SOURCES.md`；本任务不新增或强化这些一般性主张，只重组已有内容并补足 S007 已核对的连接。
- Planner 额外实际读取的文件：
  - `AGENTS.md`；
  - `Notes/WORKFLOWS/execution-contract.md`；
  - `Notes/WORKFLOWS/subagents.md`。
- 本计划不要求先补入 S007 参考文献 [6]。只有后续任务要求完整重建该具体 LP 码或独立验证 `k=744` 时，才返回 Context Builder 补充来源。

# 与现有知识库的衔接

## 直接复用的 canonical 内容

- `[[Chain complex 与 cochain complex]]`：chain/cochain、cycle、boundary、homology quotient。
- `[[CSS码中的cochain complex]]`：CSS 的 row/column convention 与 logical quotient。
- `[[Cochain complex 的 tensor product]]`：total degree、product differential、两条路径抵消。
- `[[Balanced tensor product 与 coinvariant quotient]]`：right/left module、balanced relation、anti-diagonal coinvariant quotient。

这些定义和一般证明不在第 7 目录的笔记中重新展开；当前笔记只写它们在 HGP 或 LP 中怎样被具体使用。

## 文件处理方案

| 文件 | 处理方式 | 主要目的 |
|---|---|---|
| `Notes/07-Lifted-Product Code/Künneth 分解.md` | 本任务不修改正文 | 只在 HGP、LP、`Notes/00-index.md` 和 `CANONICAL_KNOWLEDGE.md` 中把它标记为逻辑空间、维数公式和一般系数边界的可选数学支线 |
| `Notes/07-Lifted-Product Code/Hypergraph product code.md` | 大段重写 | 从两张经典校验矩阵推导两个物理扇区、CSS blocks、四类 Tanner 边与行／列一维分解；显式对齐 S007 式 (1) |
| `Notes/07-Lifted-Product Code/Lifted product code.md` | 大段重写并重排 | 先建立“外层 HGP product skeleton + 内层 lift permutation”的核心图像，再放置 balanced quotient、一般群、距离和解码等后续内容 |
| `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md` | 新建 | 只解释 S007 §6 已展示的 seed base matrix、图 12 和四阶段执行；不由矩阵 `A` 补建完整两因子数据或 data/X/Z-check sector 映射 |
| `Notes/00-index.md` | 最小更新 | 把第 7 条改为核心路径 `HGP → LP → S007 应用`，把 Künneth 标成逻辑空间与系数边界的可选数学支线 |
| `CANONICAL_KNOWLEDGE.md` | 只更新相关条目 | 修正 HGP/LP 的强制前置，登记 S007 应用笔记的 source-specific ownership，并记录 convention 与来源边界 |

## 本任务不做的结构变更

- 不删除三篇 legacy candidate notes。
- 不重命名三篇现有主笔记。
- 不修改 `Künneth 分解.md` 正文，也不在本任务中移动、改写或拆分其中的 PID、derived tensor、谱序列、`R_2` 反例或证明主线。
- 不修改 `Translations/S007.full.zh-CN.md`、S007 PDF、截图、`Papers/SOURCES.md` 或 `Papers/RELATIONS.md`。
- 不把 ONEX 的 SMT/MILP 算法写成新的编译器教程；只保留理解四阶段所需的输入／输出含义。

## 必须避免的重复

- 不重新定义 chain/cochain complex、homology quotient 或 CSS logical quotient。
- 不重新证明 ordinary tensor-product complex 的一般 differential 平方为零。
- 不在 LP 笔记重新证明 balanced relation 与 anti-diagonal coinvariant quotient 的一般同构。
- 不在 S007 应用笔记重新推导完整 HGP 或一般 LP blocks；只实例化已经建立的结论。
- 不把 S007 的具体 diagonal parking、执行时长或单项式实例推广成任意 LP 码的定义或定理。

# 正文主线

核心阅读路径从 HGP 开始。读者先看到两张经典校验矩阵如何产生两个物理量子比特扇区和两张自动对易的 CSS 校验矩阵，再把 Kronecker blocks 展开成四类 Tanner 边。每类边固定一个乘积坐标，只改变另一个坐标，因此综合征提取严格分成水平与竖直的一维子问题。

LP 笔记随后保留这张外层 product skeleton，但把 HGP 中的二进制 `0/1` 边替换成带 lift 标签的环元素。循环情形下，每个原型节点展开成 `ℓ` 个副本，单项式 `x^k` 变成这些副本之间的循环 permutation。这样，外层 product coordinate 决定处理哪一组 data/check lifts，内层 lift coordinate 决定组内哪些具体副本配对。

S007 应用笔记最后把这两个数学层级翻译成物理执行：先在 lift-level graph 上做提升间调度，再按多项式标签做提升内重排，随后对齐并执行门，完成一个乘积方向后再转移到另一个方向。该笔记以 S007 的式 (2)、图 12 和四阶段为终点，不尝试补出论文没有给出的第二因子或参数推导。

Künneth 笔记从核心路径中标记为可选支线。它回答的是乘积复形的逻辑同调如何由两个因子的同调组成，以及域上 HGP 的简洁 `K` 公式为何成立；它不负责 HGP blocks、CSS 对易、行／列分解、LP 的 cyclic shift 或 S007 的执行阶段。本任务只在 HGP、LP、`Notes/00-index.md` 与 `CANONICAL_KNOWLEDGE.md` 中建立这一定位，不修改 `Künneth 分解.md` 正文。

# 分节计划

## `Hypergraph product code.md`

| 章节 | 必须推进的内容 | 本节结束后可使用 | 不在本节重复 |
|---|---|---|---|
| 两张经典校验矩阵与 convention | 保留本库 `A,B` chain convention，并立即给出与 S007 的转换 `A=H_1`、`B=H_2^T` 及尺寸对应 | 后文能无歧义地在两套记号间转换 | CSS logical quotient 的一般解释 |
| 乘积中间项与物理扇区 | 从两个二项 complex 的 total degree 推出 `C_1=F_2^{n_A m_B}⊕F_2^{m_A n_B}`，给每个扇区明确的变量／校验坐标 | 两类 data-qubit sectors | ordinary tensor product 的一般分配律证明 |
| CSS 校验矩阵与对易 | 写出 `H_X=∂_1`、`H_Z=∂_2^T`，用两条 product paths 得到 `H_XH_Z^T=0` | 自动对易的 HGP blocks | Künneth 或 logical dimension |
| S007 convention 下的式 (1) | 代入 `B=H_2^T`，逐块恢复 S007 的 `\mathcal H_X,\mathcal H_Z`，并列出 `q^A,q^B,x,z` 的指标集合 | 可以直接读取 S007 §2.2 | 把两套同名矩阵混用 |
| 四类 Tanner 边 | 从四个 Kronecker blocks 逐项推出 S007 的两组边公式；说明每条边固定哪个坐标、改变哪个坐标 | “无对角支撑”的精确含义 | 只靠图像声称存在行／列分解 |
| 行与列的一维分解 | 将 `H_1` Tanner copies 与 `H_2` Tanner copies 分别组织为水平／竖直相容组，说明为何可先并行所有行，再切换到所有列 | ONEX 所接收的一维子问题 | SMT、MILP 和硬件时长细节 |
| 长度、秩与逻辑空间 | 先给总是成立的 `K=N-rank H_X-rank H_Z`；再把 Künneth 的两个扇区公式放入明确标注的可选小节 | 构造与逻辑空间的依赖边界 | 在主线开头强制读 Künneth |
| qLDPC、距离与 HGP→LP | 现有 qLDPC、距离与 family 参数段落只允许移动、连接和去重，不进行语义重写；在其后列出 LP 保留与改变的内容 | 进入 LP 所需的外层 product skeleton | 改写既有参数主张或新增 S007 未支持的 family claims |

## `Lifted product code.md`

| 章节 | 必须推进的内容 | 本节结束后可使用 | 不在本节重复 |
|---|---|---|---|
| 从 HGP 边到 lift 标签 | 先说明 HGP 的 `0/1` 条目只决定有无边；LP 的环值条目还携带副本 permutation。定义 base node、一个 node 的 `ℓ` 个副本和“data/check lift” | 外层节点与内层副本的区分 | 完整 HGP 推导 |
| 循环 lift 的环表示 | 定义 `R_ℓ=F_2[x]/(x^ℓ-1)`、`Pe_t=e_{t+1}` 和 `Φ(x^k)=P^k`，说明列变量与行校验之间的连接方向及转置后的逆移位 | 单项式可以被直接读成 cyclic shift | balanced quotient 的一般定义 |
| 环值矩阵与二进制展开 | 对 `A=(a_ij)` 说明每个条目替换为 `Φ(a_ij)`，得到大二进制块矩阵；多项式和表示多组 permutation edges | 从紧凑 seed matrix 恢复 lift graph | 将环值矩阵误解为删去信息 |
| HGP 型 LP blocks | 写出一般 `A,B` 的环值 `\widehat H_X,\widehat H_Z`、反对合与二进制展开，并完整核对 CSS 对易所用条件 | 一般交换循环／阿贝尔情形的 LP CSS code | right/left module 的一般证明 |
| 外层 product 与内层 lift | 用一张对照表区分：乘积坐标、lift-level data/check nodes、单个 lift 内的副本指标、最终硬件位置；说明前两者来自 HGP skeleton，第三项由 `x^k` 决定，第四项属于编译 | S007 分层执行的数学接口 | 把硬件布局说成 LP 定义的一部分 |
| 长度与逻辑维数边界 | 给出 `N=ℓ(n_A m_B+m_A n_B)` 与二进制秩公式；把 Künneth／一般环问题放在后置边界中 | 可以区分码构造与参数计算 | 无条件套用域上 `K` 公式 |
| quotient、QC 与一般群边界 | 现有 anti-diagonal quotient、`B=[1+x]`、非阿贝尔、距离、渐近参数和解码段落只允许移动、连接和去重，不进行语义重写；统一置于核心构造之后 | 后续研究 LP 子族时的扩展入口 | 改写既有数学主张或重复 balanced tensor 主笔记 |
| 与 S007 的连接 | 只写一段短接口：S007 给出一个 `3×7` 单项式矩阵和四阶段执行，详细解释链接到新应用笔记 | 从一般 LP 跳转到论文特例 | 在一般 LP 主笔记中塞入完整论文执行流程 |

## `S007 中 LP 码的分层执行.md`

| 章节 | 必须推进的内容 | 本节结束后可使用 | 不在本节重复 |
|---|---|---|---|
| 来源、实例与已知边界 | 登记 S007 v1、§6、式 (2)、图 12、表 3；式 (2) 的 `3×7` 矩阵只作为 S007 已展示的 seed base matrix；把 `ℓ=45` 与 $[\![2610,744,d\le 16]\!]$ 只记为论文给定参数；把译文“示例 LP 码 [2]”按英文原文解释为“式 (2)”，但不修改译文 | 后文可以安全使用的实例数据与来源边界 | 猜测 self-product、补建第二因子或推导 `2610`、`744`、距离界 |
| 外层乘积方向 | 用链接继承 HGP 的两类数据扇区、四类边和 row/column decomposition，只写它们如何成为 S007 的 outer product directions | 水平／竖直方向的来源 | 重写 HGP blocks 全部推导 |
| lift-level graph 与式 (2) | 每个单项式只解释为一条 base edge 携带的 cyclic-shift label；data lift、X-check lift、Z-check lift 的具体角色只采用图 12 和 S007 正文明示的内容，不把矩阵 `A` 的行、列自行指派为完整 data/X/Z-check sectors | 提升间图与提升内标签的来源内区分 | 仅凭矩阵 `A` 重建完整 LP 两因子数据或完整 data/X/Z-check sector 映射 |
| 单项式与提升内配对 | 采用本库 `Pe_t=e_{t+1}` convention，解释 `x^k` 作为某条已给 base edge 的 cyclic-shift label 如何作用于副本指标；明确图 12(b) 的 `ℓ=6,x^2` 是机制示意，而实例为 `ℓ=45` | 可读取单条 base edge 的 inner-lift shift 含义 | 把方向 convention 冒充原文唯一约定，或据此补出未展示的完整连接图 |
| 四阶段执行 | 依次解释提升间重排、提升内重排、门执行、定向转移；每阶段都写清处理的节点集合、使用的数据和产生的结果，并说明前三阶段在另一个 product direction 上重复 | 完整读取图 12(a)–(d) | 展开 ONEX 求解器内部算法 |
| 层级关系与性能分解 | 用一张总结表对应 outer product、inter-lift、intra-lift、gate alignment、direction transfer；用表 3 只验证论文确实分别统计这些时长，不把数值结果写成一般定律 | 能解释 S007 §6 的理论构造与执行接口 | 泛化 diagonal parking 或 ONEX-Z 优势 |
| 回到一般 LP | 最后一节明确哪些结论来自一般 LP，哪些只属于该实例和中性原子布局，并链接回 `[[Lifted product code]]` | 避免论文特例污染 canonical 定义 | 新增未核对的 LP 定理 |

# 数学承诺

## HGP convention 与四类边

必须显式写出

```text
A = H_1,
B = H_2^T,
(m_A,n_A,m_B,n_B)=(r_1,n_1,n_2,r_2).
```

从而

```text
[A⊗I_{m_B} | I_{m_A}⊗B]
= [H_1⊗I_{n_2} | I_{r_1}⊗H_2^T],
```

```text
[I_{n_A}⊗B^T | A^T⊗I_{n_B}]
= [I_{n_1}⊗H_2 | H_1^T⊗I_{r_2}].
```

同时逐项写出：

```text
H_1(i,j)=1
⇒ (x_{i,ℓ},q^A_{j,ℓ}) 和 (z_{j,m},q^B_{i,m}),
```

```text
H_2(m,ℓ)=1
⇒ (x_{i,ℓ},q^B_{i,m}) 和 (z_{j,m},q^A_{j,ℓ}).
```

每组关系必须说明量化的自由指标，以及固定／变化的坐标；“无对角支撑”必须由这四类边推出，而不是只引用图 1。

## HGP 的构造与 Künneth 边界

必须区分：

- HGP blocks、CSS 对易、四类边和 row/column decomposition 只需要 tensor-product complex 与索引展开；
- `K=N-rank H_X-rank H_Z` 可直接用于有限实例；
- Künneth 提供 `H_1` 的两个逻辑扇区及简洁维数公式，但不是构造校验矩阵的条件。

## 循环 lift 与 shift convention

必须写出

```text
R_ℓ=F_2[x]/(x^ℓ-1),
Pe_t=e_{t+1 mod ℓ},
Φ(x^k)=P^k.
```

若列表示变量副本 `v_t`、行表示校验副本 `c_t`，则在本库 convention 下

```text
v_t ↔ c_{t+k mod ℓ},
```

等价地

```text
c_t ↔ v_{t-k mod ℓ}.
```

转置必须对应逆移位。S007 应用笔记采用这套 convention 时，应明确说明这是仓库固定记号；原文只要求 cyclic shift。

## LP blocks 与二进制 CSS 对易

在交换循环／阿贝尔情形，必须保留并核对

```text
\widehat H_X=[A⊗I_{m_B} | I_{m_A}⊗B],
\widehat H_Z=[I_{n_A}⊗B^* | A^*⊗I_{n_B}],
H_X=\mathbb B(\widehat H_X),
H_Z=\mathbb B(\widehat H_Z).
```

对易证明必须明确使用：

1. 两个因子的系数交叉对易；
2. `\mathbb B(M^*)=\mathbb B(M)^T`；
3. `\mathbb B` 保持乘法；
4. 特征 `2` 中两条相同路径相加为零。

若涉及非阿贝尔段落，只保留现有 right/left module 与 `ρ_aλ_b=λ_bρ_a` 的边界，不把交换情形公式无条件推广。

## S007 实例的来源边界

必须明确写出：

- 式 (2) 的 `3×7` 矩阵 `A` 只作为 S007 已展示的 seed base matrix 使用；
- 每个单项式只解释为一条 base edge 携带的 cyclic-shift label；
- 不得仅凭矩阵 `A` 重建完整 LP 两因子数据；
- 不得仅凭矩阵 `A` 给出完整 data/X/Z-check sector 映射；
- data lift、X-check lift、Z-check lift 的具体角色只采用图 12 和 S007 正文明示的内容；
- `ℓ=45` 与 $[\![2610,744,d\le 16]\!]$ 只作为来源给定参数，不推导 `2610`、`744` 或距离界；
- 不从 `2610/45=58=7^2+3^2` 推断 self-product；
- 译文中的“示例 LP 码 [2]”按 PDF 英文原文解释为“式 (2)”，但本任务不修改译文；
- 图 12(b) 的 `ℓ=6,x^2` 只是可视化示意。

# 例子安排

## HGP 的单个非零矩阵元

- 具体对象：分别取一个 `H_1(i,j)=1` 和一个 `H_2(m,ℓ)=1`。
- 计算：列出它们在所有固定副本坐标上产生的四类 data-check edges。
- 只说明：Kronecker identity block 如何复制 Tanner 图，以及为什么每条边只改变一个 product coordinate。
- 不承担：距离、码率或 ONEX 优化算法。

## `ℓ=6,x^2` 的循环移位

- 具体对象：图 12(b) 的示意参数。
- 计算：在本库 convention 下列出 `0→2,1→3,2→4,3→5,4→0,5→1`，区分界内与回绕。
- 只说明：单项式如何变成副本 permutation，以及 overflow 只是模 `ℓ` 回绕。
- 不承担：实际 `ℓ=45` 码的完整连接图。

## 式 (2) 中一个条目

- 具体对象：例如 `A_{1,1}=x^{29}`。
- 计算：在本库 convention 下把副本 `t` 配到 `t+29 mod 45`；随后说明这只是该 base edge 的 inner-lift matching。
- 只说明：如何从环值矩阵的一个条目进入第二阶段的提升内重排。
- 不承担：第二因子、完整 stabilizer matrix、`N/K/d` 推导或门 schedule 的全部边。

# 索引与 canonical ownership 更新

## `Notes/00-index.md`

只修改第 7 条和对应目录描述，不重排其它主线。第 7 条应表达：

1. `[[Hypergraph product code]]`：核心入口，建立 HGP blocks、两个物理扇区、四类边与行／列分解；
2. `[[Lifted product code]]`：在 HGP 外层骨架上加入 lift 标签、循环 permutation 和环值 blocks；
3. `[[S007 中 LP 码的分层执行]]`：把 outer product、inter-lift 与 intra-lift 结构翻译成图 12 的四阶段；
4. `[[Künneth 分解]]`：标明为“逻辑空间、维数公式和一般系数边界的可选数学支线”，不放在构造主线最前。

## `CANONICAL_KNOWLEDGE.md`

只改主路线图及 Künneth、HGP、LP 三个条目，并新增一个 S007 应用条目：

- Künneth：保留 canonical ownership；增加“不作为 HGP/LP 构造或 S007 执行的强制前置”。
- HGP：前置依赖移除强制 Künneth；新增 S007 convention 转换、四类 Tanner 边和 row/column decomposition；把 Künneth 标成逻辑空间小节的可选依赖。
- LP：前置依赖以 HGP、balanced tensor、CSS convention 为主；Künneth只用于逻辑维数与一般环边界；新增 outer product／inner lift 的长期区分。
- S007 应用：登记为论文特例，不作为一般 LP 定义；来源固定为 S007 v1 的译文 §2.2、§3.1、§6、图 1、图 12、表 3及 PDF pp.12–13；边界中写明第二因子和参数推导缺失。
- 不机械重写未触及条目，不把单次任务状态写入 canonical index。

# 执行批次

各批次依次门控；本批次的 blocker 未解决、数学与来源检查未通过或需要超出授权范围时，必须停止并升级，不得进入下一批次。

## 批次 1：HGP 核心主线

- 只修改 `Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- 完成两个物理扇区、CSS blocks、S007 convention、四类 Tanner 边与行／列一维分解。
- qLDPC、距离与 family 参数段落只允许移动、连接和去重，不进行语义重写。
- 完成后运行数学与来源检查。
- blocker 未解决前不得进入批次 2。

## 批次 2：LP 核心主线

- 只修改 `Notes/07-Lifted-Product Code/Lifted product code.md`。
- 修改 cyclic lift、环值矩阵、HGP 型 LP blocks、outer product / inner lift 接口。
- anti-diagonal quotient、`B=[1+x]`、非阿贝尔、距离、渐近参数和解码段落只允许移动、连接和去重，不进行语义重写。
- 完成后运行数学与来源检查。
- blocker 未解决前不得进入批次 3。

## 批次 3：S007 应用笔记

- 新建 `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md`。
- 严格遵守式 (2)、图 12、具体参数和 data/X/Z-check roles 的来源边界。
- 运行三类只读检查：仓库一致性、数学与来源、正文与格式。
- blocker 未解决前不得进入批次 4。

## 批次 4：索引收尾

- 最小更新 `Notes/00-index.md` 和 `CANONICAL_KNOWLEDGE.md`。
- 只同步已完成正文所需的阅读入口、ownership、前置和来源边界。
- 做最终仓库一致性检查。

# 执行边界

## Executor 可自行决定

- 不改变数学含义的局部措辞、段落连接和标题短语。
- 只在 HGP、LP 两篇目标笔记内按本计划移动现有章节、删除重复过渡、统一局部 LaTeX；不得触碰 `Künneth 分解.md` 正文。
- 保留 HGP、LP 与 Künneth 的现有文件名，创建已批准的新应用笔记。
- 按计划增加或修复 wikilinks、section anchors、`00-index` 和相关 canonical entries。
- 在新应用笔记中复用现有图 12 snapshot 的链接，但不得复制或修改图片文件。
- HGP 中 qLDPC、距离与 family 参数段落，以及 LP 中 anti-diagonal quotient、`B=[1+x]`、非阿贝尔、距离、渐近参数和解码段落，只做必要的移动、连接和去重，不进行语义重写。

## 必须停止并升级

- 试图仅凭式 (2) 的矩阵 `A` 猜测或重建具体码的第二个因子、adjoint/self-product convention 或完整 LP 两因子数据。
- 试图仅凭矩阵 `A` 给出完整 data/X/Z-check sector 映射，或给 data lift、X-check lift、Z-check lift 添加图 12 和 S007 正文没有明示的具体角色。
- 试图从矩阵 `A` 或现有段落推导 `2610`、`744`、距离界或完整 stabilizer matrix。
- 需要把译文中的“示例 LP 码 [2]”解释成“式 (2)”之外的含义，或需要修改译文本身。
- 需要新增 S007 参考文献 [6] 或其它外部资料才能兑现正文承诺。
- 发现本库 shift convention 与现有公式不能一致对齐。
- 需要删除、重命名或再拆出本计划未列出的正式笔记。
- 需要修改翻译、PDF、截图或 Papers 管理文件。
- 需要修改 `Künneth 分解.md` 正文，包括证明策略、证明链、例子或一般系数边界。
- 需要改变 LP 的适用环条件、非阿贝尔左右模条件或任何定理条件。
- 当前工作树或 canonical ownership 已发生使 `context_version: 1` 失效的实质变化。
- 来源与 legacy note 的数学主张冲突；不得以模型常识静默裁决。

# 验收条件

## 内容

完成后，读者应能依次回答：

1. HGP 的两个物理量子比特扇区从 total degree 的哪两个分量产生；
2. S007 式 (1) 与本库 `A,B` convention 如何逐块对应；
3. 四类 Tanner 边分别由哪个 Kronecker block产生；
4. 为什么每条边固定一个乘积坐标，从而产生行／列一维子问题；
5. LP 相对 HGP 保留什么外层骨架、增加什么 lift 数据；
6. `R_ℓ` 和 `x^k` 如何表示 `ℓ` 个副本之间的 cyclic permutation；
7. S007 图 12 的提升间重排、提升内重排、门执行、定向转移分别处理什么；
8. 为什么 Künneth 对 HGP 逻辑空间有用，却不是 S007 构造与执行的强制前置；
9. 哪些关于具体 $[\![2610,744,d\le 16]\!]$ 码的数据是来源直接给定，哪些不能从现有材料推出。

## 数学

- HGP 两套 convention、尺寸和四类边逐项一致。
- 所有 index 的范围、固定坐标和变化坐标明确。
- `x^k` 的正负方向与转置关系按一个固定 convention 使用。
- LP CSS 对易所用的交换性、反对合和二进制展开条件没有遗漏。
- `Künneth 分解.md` 正文保持不变；HGP、LP、索引和 canonical 对其可选支线定位彼此一致。
- 域上结论、一般环边界与 S007 的来源给定参数没有混淆。

## 仓库一致性

- `Künneth 分解.md` 正文无改动；HGP、LP 与 Künneth 之间无失效互链。
- 新应用笔记只引用正式笔记和稳定来源，不引用 `WORKING` 任务文件。
- `Notes/00-index.md` 反映核心路径与可选支线。
- `CANONICAL_KNOWLEDGE.md` 的 ownership、前置和边界与正文一致。
- 不修改无关主题，不出现大范围格式化。

## 正文

- 全部正式笔记符合 `Notes/WRITING_GUIDE.md`。
- 正文中不出现“任务目标、解决卡点、本节输入、验收条件、Planner、Executor”等流程语言。
- 每篇笔记只有一个主对象；S007 特例不污染一般 HGP/LP 定义。
- 删除旧的补丁式解释、重复背景和冲突表述。
- 三类只读检查均通过：仓库一致性、数学与来源、正文与格式。

# 下一步

请用户审阅本计划，重点确认：

1. 是否同意把核心阅读顺序改为 `HGP → LP → S007 中 LP 码的分层执行`；
2. 是否同意本任务不修改 `Künneth 分解.md` 正文，只在 HGP、LP、`Notes/00-index.md` 和 `CANONICAL_KNOWLEDGE.md` 中将其标为可选数学支线；
3. 是否同意新建 `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md`；
4. 是否接受本任务不补猜第二因子、不重建完整 data/X/Z-check sector 映射、不推导 `2610`、`744` 或距离界，也不修改翻译和 Papers 管理文件。

批准时回复：

```text
批准任务 20260827-s007-lp-learning-path 的 PLAN，进入执行。
```

计划保存到任务目录后，只把 `TASK.md` 状态改为 `plan_proposed`；在用户明确批准前，`PLAN.md` 的 `approval` 必须保持 `pending`，不得修改正式笔记。

# 后续独立任务候选：Künneth 证明主线重写

本节只保存从本计划移出的想法，不属于本任务的 `target_files`、执行批次或验收条件。即使用户批准当前 PLAN，也不授权修改 `Künneth 分解.md`；若要实施，必须另建任务、重新构造 CONTEXT、生成独立 PLAN 并单独获得用户批准。

- 候选目标：在不改变定理条件的前提下，让比较映射、域上的链级分裂、可缩部分和 Künneth 同构形成连续证明，再把 HGP 逻辑空间与一般系数边界放到后置部分。
- 候选分节：比较映射及良定义；域上的补空间分裂；可缩部分；域上的 Künneth 同构；二项复形与 HGP 逻辑空间；自然性；PID 与一般系数环边界。
- 候选证明链：`κ_n` 良定义 → `C=\widetilde{\mathcal H}(C)⊕Q(C)` → `Q(C)` 具有 contracting homotopy → tensor 展开 → 含 `Q` 的 summands 可缩 → 只剩 homology-representative summand → `κ_n` 为同构。
- 候选最小例子：`E: 0→k·e_1 --id→ k·e_0→0`，以 `s(e_0)=e_1`、`s(e_1)=0` 验证 `∂s+s∂=id_E`，只用于解释可缩部分为何不贡献同调。
- 候选验收重点：比较映射的定义与自然性不依赖补空间选择；补空间只服务于域上可逆性证明；HGP 特化、PID／一般环边界和 `R_2` 反例的位置清楚；来源与现有 canonical ownership 重新核验。
