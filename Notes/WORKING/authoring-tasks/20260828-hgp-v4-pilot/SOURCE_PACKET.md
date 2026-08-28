# 来源范围

## S01 — 目标 HGP 笔记

- source: `Notes/07-Lifted-Product Code/Hypergraph product code.md`
- version: Git `800575575cd2cb4f110869120b50c91b06ce5e78` 工作树版本。
- location: 第 1–20、39–51、91–99、102–165、169–175 行。
- classification: `repository-derived`。
- supported_claim: HGP 从两张经典种子矩阵出发；`A,B` 是输入；目标约定为 `H_X=\partial_1,H_Z=\partial_2^T`；三项箭头的坐标角色；输出满足 `H_XH_Z^T=0`。
- unsupported_or_missing: 第 1 行把构造、所得码、自动对易、前置链接和 Künneth 维护边界压在一起，不作为开头语言样板；具体 Kronecker blocks 与两路径抵消超出 U01/U02。
- intended_use: 核对对象、角色和本库 chain 方向；仅向 Writer 提供任务需要的授权摘录或重述。

## S02 — CSS 矩阵与对易条件

- source: `Notes/06-CCZ Distillation/CSS码中的cochain complex.md`
- version: Git `800575575cd2cb4f110869120b50c91b06ce5e78` 工作树版本。
- location: 第 5–21、48–75、110–140 行。
- classification: `repository-derived`。
- supported_claim: `H_X,H_Z` 共享 `n` 个物理坐标；行分别给出 X 型、Z 型支撑；CSS 对易条件可写成零矩阵乘积；校验选择经转置映成支撑。
- unsupported_or_missing: 原文使用 `H_ZH_X^T=0` 的 cochain 方向，并含 stabilizer、logical、syndrome 等 U01/U02 禁止内容；不得把这些术语带入 staged draft。
- intended_use: 支撑 CSS 的局部矩阵解释；通过转置核对 `H_XH_Z^T=0`。

## S03 — 链复形

- source: `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`
- version: Git `800575575cd2cb4f110869120b50c91b06ce5e78` 工作树版本。
- location: 第 4–24 行。
- classification: `source-derived`（仓库稳定主笔记）。
- supported_claim: 链复形是一串向量空间和线性映射，连续两步的复合为零。
- unsupported_or_missing: degree、cycle、boundary、homology 及几何类比均不属于本次所需局部定义。
- intended_use: 只在三个空间与两个映射用途已解释后给出“链复形”的当前局部名称。

## S04 — 单比特 Pauli 交换

- source: `Notes/03-Magic State基础/Clifford Twirling 与魔态错误模型.md`
- version: Git `800575575cd2cb4f110869120b50c91b06ce5e78` 工作树版本。
- location: 第 777–791、1402–1410 行。
- classification: `repository-derived`。
- supported_claim: Pauli 对易／反对易对应交换符号 `+1/-1`；`ZX=iY` 与 `XZ=-iY` 给出 `XZ=-ZX`。
- unsupported_or_missing: 没有在任务需要的局部范围内直接解释异比特张量因子对易，也不讨论整条 CSS 校验的总交换符号。
- intended_use: 与 `LD01` 一起锚定同一量子比特的 `X,Z` 反对易。

## S05 — 一般二进制辛表示（交叉核对）

- source: `Notes/01-量子纠错基础/逻辑基态的表示.md`
- version: Git `800575575cd2cb4f110869120b50c91b06ce5e78` 工作树版本。
- location: 第 168–200 行。
- classification: `repository-derived`。
- supported_claim: 二进制 Pauli 支撑存在矩阵化对易判据，逻辑 X/Z 的交换符号按配对决定。
- unsupported_or_missing: 一般辛矩阵 `\Lambda`、稳定子与逻辑算符均超出本次局部 CSS 解释，不授权 Writer 引入。
- intended_use: Contract Auditor 的一致性交叉核对；不作为 Writer 必写内容。

## S06 — canonical 与 index（只读定位）

- source: `CANONICAL_KNOWLEDGE.md:75–140,267–300`; `Notes/00-index.md` 的 HGP 路线项。
- version: Git `800575575cd2cb4f110869120b50c91b06ce5e78` 工作树版本。
- location: 上述稳定段落。
- classification: `repository-derived`。
- supported_claim: owner、chain/CSS 方向、HGP 固定公式与路线位置没有冲突。
- unsupported_or_missing: 不是 Writer 上下文；不授权把 ownership、前置清单、路线或 wikilink 写入正文。
- intended_use: Mapper 核对和最终“未修改”验证，绝不传入 Writer packet。

# 术语与约定

- 标量域为 `\mathbb F_2`；加法和矩阵元求和都按模 2。
- 当前正文术语：奇偶校验矩阵、X 型校验、Z 型校验、行、列、支撑、重叠、重叠奇偶、对易、反对易、物理量子比特、二进制向量空间、链复形、映射。
- 可保留缩写与符号：HGP、CSS、`A`、`B`、`H_X`、`H_Z`、`C_2`、`C_1`、`C_0`、`X`、`Z`。
- 不得以英文速记替代中文：`X-type checks`、`row pair`、`support space`、`check matrix` 等均不授权。
- 本任务采用 chain 方向 `C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0`。来源 S02 的 `H_ZH_X^T=0` 转置为 `H_XH_Z^T=0`，不改变条件。

# 公式、图表、定理和局部计算锚点

## LD01 — 同一量子比特上的 `X,Z` 反对易

采用显式矩阵

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

直接相乘得到

$$
XZ=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
ZX=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-XZ.
$$

因此 `XZ=-ZX`。这与 S04 的 `ZX=iY, XZ=-iY` 一致。classification: `local-derivation`，逐项可核对。

## LD02 — 不同量子比特上的作用对易

使用张量积乘法规则 `(M\otimes N)(P\otimes Q)=MP\otimes NQ`：

$$
(X\otimes I)(I\otimes Z)=XI\otimes IZ=X\otimes Z,
$$

$$
(I\otimes Z)(X\otimes I)=IX\otimes ZI=X\otimes Z.
$$

两种次序相同，所以作用在这两个不同量子比特上的 `X` 与 `Z` 对易。更一般的不同坐标情形由在其余张量因子插入 `I` 得到。classification: `local-derivation`。

## LD03 — 从局部负号到总交换符号

令二进制向量 `x,z\in\mathbb F_2^n` 分别表示一条 X 型与一条 Z 型校验的支撑：

$$
X(x)=\bigotimes_{q=1}^nX^{x_q},
\qquad
Z(z)=\bigotimes_{q=1}^nZ^{z_q}.
$$

在第 `q` 个位置，只有 `x_q=z_q=1` 时交换次序贡献 `-1`；其余位置至少有一个恒等作用，且不同位置按 LD02 对易。因此

$$
X(x)Z(z)=(-1)^{\sum_qx_qz_q}Z(z)X(x)=(-1)^wZ(z)X(x),
$$

其中 `w` 是两条支撑的共同位置数。`w` 为偶数时符号为 `+1`，两条校验对易。classification: `local-derivation`。

## LD04 — 矩阵元就是行支撑的重叠奇偶

设 `h_i` 是 `H_X` 第 `i` 行，`g_j` 是 `H_Z` 第 `j` 行。按矩阵乘法，

$$
(H_XH_Z^T)_{ij}
=\sum_{q=1}^{n}(H_X)_{iq}(H_Z)_{jq}
=\sum_{q=1}^{n}(h_i)_q(g_j)_q
\pmod 2.
$$

乘积项仅在两行的第 `q` 列都为 `1` 时贡献 `1`，故该和是共同非零列数的模 2 奇偶。于是

$$
H_XH_Z^T=0
\quad\Longleftrightarrow\quad
\text{每一对 X 型与 Z 型校验的重叠数均为偶数}
\quad\Longleftrightarrow\quad
\text{所有异型校验彼此对易},
$$

最后一个等价使用 LD03。classification: `local-derivation`。

## LD05 — 三项箭头的复合

取

$$
C_2=\mathbb F_2^{r_Z},
\qquad C_1=\mathbb F_2^n,
\qquad C_0=\mathbb F_2^{r_X}.
$$

对 Z 型校验选择向量 `z\in C_2`，`H_Z^Tz\in C_1` 是被选行支撑的模 2 叠加。对物理支撑 `v\in C_1`，`H_Xv\in C_0` 的第 `i` 个分量是 `H_X` 第 `i` 行与 `v` 的重叠奇偶。因此连续复合为

$$
z\longmapsto H_Z^Tz\longmapsto H_XH_Z^Tz.
$$

若 `H_XH_Z^T=0`，每个 Z 型校验选择都被送到零；特别地，每一条 Z 型校验与每一条 X 型校验的重叠奇偶均为零。classification: `local-derivation`。

## LD06 — 共享列不自动推出零乘积

取最小的共享列矩阵

$$
H_X=\begin{bmatrix}1\end{bmatrix},
\qquad
H_Z=\begin{bmatrix}1\end{bmatrix}.
$$

它们都有同一个物理量子比特列，但

$$
H_XH_Z^T=\begin{bmatrix}1\end{bmatrix}\ne0.
$$

因此“共享列”只让两张矩阵谈论同一组坐标，并不自动保证 CSS 对易条件。classification: `local-derivation`。

# 禁止补猜

- 不得凭模型常识省略 LD01–LD04 中任一 premise，再直接宣称“偶数重叠所以对易”。
- 不得把 `H_XH_Z^T=0` 写成任意共享列矩阵自动拥有的性质。
- 不得把 `A,B` 称为 HGP 的最终 X/Z 校验矩阵；它们是经典种子输入。
- 不得在 U01/U02 引入 Kronecker blocks、`A/B` 尺寸、total degree、两路径抵消、homology、Künneth、stabilizer group、logical quotient、syndrome 或 metacheck。
- 不得把 S06 的 canonical/index/前置关系传入 Writer 或读者正文。
- 不得把 S01 的旧首段当作语言样板，也不得用 wikilink 代替局部解释。
