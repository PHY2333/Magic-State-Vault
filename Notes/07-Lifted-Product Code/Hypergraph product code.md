---
note_type: reference
entry_mode: guided
status: reviewed
---

超图乘积构造是一种从两张经典二进制奇偶校验矩阵构造 CSS 量子码的方法。这类矩阵的每一行规定一条模 2 的奇偶校验条件。由这种构造得到的量子码称为 HGP 码：超图乘积构造是产生量子码的方法，HGP 码则是所得对象。

在构造一个 HGP 码时，把作为输入的两张经典二进制奇偶校验矩阵记为 \(A\) 和 \(B\)，它们就是构造所用的两份经典种子输入。构造以它们为数据产生两张量子校验矩阵，并把这两张量子校验输出记为 \(H_X\) 和 \(H_Z\)。因此，\(H_X\)、\(H_Z\) 是由输入生成的输出，而不是 \(A\)、\(B\) 的别名。

\(H_X\) 与 \(H_Z\) 的列对应同一组物理量子比特。对于这两张输出矩阵，一行中取值为 1 的列指出该行所表示的校验作用的物理量子比特位置，这些位置构成该行的支撑；具体而言，\(H_X\) 的每一行给出一条 X 型校验的支撑，\(H_Z\) 的每一行给出一条 Z 型校验的支撑。在这里，CSS 的当前要求是所有 X 型校验都与所有 Z 型校验彼此对易。怎样由构造本身保证两类校验彼此对易？

### 从局部交换到矩阵条件

要回答上一节的问题，第一步是把输出必须满足的对易要求化成一个可检验的矩阵条件。\(H_X\) 与 \(H_Z\) 的列对应同一组物理量子比特，每一行给出一条相应类型校验的支撑。把 \(H_X\) 的一行记为 \(x\)，把 \(H_Z\) 的一行记为 \(z\)。对列坐标 \(q\)，\(x_q=1\) 表示 X 型校验在该量子比特上作用 \(X\)，\(x_q=0\) 表示作用 \(I\)；相应地，\(z_q=1\) 表示作用 \(Z\)，\(z_q=0\) 表示作用 \(I\)。因此两条完整校验所对应的泡利算符为
$$
X(x)=\bigotimes_q X^{x_q},
\qquad
Z(z)=\bigotimes_q Z^{z_q}.
$$
符号 \(\bigotimes_q\) 表示把每个量子比特上的 \(I\)、\(X\) 或 \(Z\) 作用组合成整条校验。支撑本身只记录一行中的非零列；该行来自 \(H_X\) 还是 \(H_Z\)，才决定这些位置上分别作用 \(X\) 还是 \(Z\)。

先看两条校验在同一个量子比特上分别作用 \(X\) 和 \(Z\) 时会发生什么。在计算基上，
$$
X|0\rangle=|1\rangle,
\quad X|1\rangle=|0\rangle,
\qquad
Z|0\rangle=|0\rangle,
\quad Z|1\rangle=-|1\rangle.
$$
于是
$$
XZ|0\rangle=|1\rangle=-ZX|0\rangle,
\qquad
XZ|1\rangle=-|0\rangle=-ZX|1\rangle.
$$
\(XZ\) 与 \(ZX\) 在这组基上的作用始终相差一个整体负号，所以同一量子比特上的这两种作用满足 \(XZ=-ZX\)。

如果 \(X\) 和 \(Z\) 分处不同的量子比特，交换次序则不会产生负号。当前所需的张量因子等式是
$$
(X\otimes I)(I\otimes Z)
=X\otimes Z
=(I\otimes Z)(X\otimes I).
$$
更多量子比特的情形只是在其余位置插入 \(I\)，因此不同量子比特上的作用彼此对易。

> [!note]- 补充推导：直接核对 \(XZ=-ZX\)
> $$
> X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
> \qquad
> Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
> $$
> $$
> XZ=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
> \qquad
> ZX=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-XZ.
> $$

回到整条校验：每个共同位置都会贡献一个负号。非共同位置至少有一条校验作用 \(I\)，而分处不同位置的作用又彼此对易，因此交换两条完整校验时，
$$
X(x)Z(z)
=(-1)^{\sum_q x_qz_q}Z(z)X(x)
=(-1)^wZ(z)X(x),
$$
其中 \(w\) 是两条支撑共同位置的整数个数。\(w\) 为偶数时，局部负号成对抵消，两条校验对易；\(w\) 为奇数时，它们反对易。

现在逐对汇总所有 X 型行与 Z 型行。第 \(i\) 条 X 型校验和第 \(j\) 条 Z 型校验对应的矩阵元为
$$
(H_XH_Z^T)_{ij}
=\sum_q(H_X)_{iq}(H_Z)_{jq}
\pmod 2.
$$
其中每一项只在两行的第 \(q\) 列都为 \(1\) 时贡献 \(1\)，所以这个矩阵元正是两行共同非零列数的奇偶。覆盖所有 \(i,j\) 后便得到
$$
H_XH_Z^T=0
\quad\Longleftrightarrow\quad
\text{每一对 X 型与 Z 型校验的重叠数均为偶数}
\quad\Longleftrightarrow\quad
\text{每条 X 型校验都与每条 Z 型校验对易}.
$$
共享物理列本身并不保证这个条件。例如，
$$
H_X=\begin{bmatrix}1\end{bmatrix},
\qquad
H_Z=\begin{bmatrix}1\end{bmatrix},
\qquad
H_XH_Z^T=\begin{bmatrix}1\end{bmatrix}\ne0,
$$
此时唯一的 X 型校验与 Z 型校验在同一位置重叠，因而不对易。

### 三个空间与两支映射

现在把同一个零矩阵条件换成整体映射的视角：
$$
C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0.
$$
这里，\(C_2\) 是以 Z 型校验为坐标的二进制向量空间，\(C_1\) 是以物理量子比特为坐标的二进制向量空间，\(C_0\) 是以 X 型校验为坐标的二进制向量空间。

第一支映射 \(H_Z^T\) 把一组 Z 型校验的选择映到物理量子比特坐标上。它将所选 Z 型校验的行按模 \(2\) 相加；所得二进制向量中取值为 \(1\) 的物理坐标构成其支撑。

第二支映射 \(H_X\) 接收一个物理支撑，并把它映成以 X 型校验为坐标的向量。输出的每个分量都记录该物理支撑与相应 X 型校验支撑的重叠奇偶。

沿两支箭头连续作用得到的正是 \(H_XH_Z^T\)。当这个连续复合为零时，任意一组 Z 型校验的选择经过两步都会得到零；结合前面的逐行解释，这统一表达了每条 X 型校验都与每条 Z 型校验对易。

这样一段由向量空间和线性映射组成、并满足连续两步复合为零的序列，就是这里所说的链复形。下一步就是由 \(A,B\) 构造这两支映射，并证明它们的复合恒为零。

### 从两张经典校验矩阵开始

取

$$
A\in\mathbb F_2^{m_A\times n_A},
\qquad
B\in\mathbb F_2^{m_B\times n_B},
$$

并把它们看成两个二项链复形

$$
\mathcal A:\quad
\mathbb F_2^{n_A}\xrightarrow{A}\mathbb F_2^{m_A},
\qquad
\mathcal B:\quad
\mathbb F_2^{n_B}\xrightarrow{B}\mathbb F_2^{m_B}.
$$

矩阵的列标记 degree-$1$ 的经典变量，行标记 degree-$0$ 的经典校验。于是 $A$ 的变量和校验指标分别写成

$$
j\in[n_A],
\qquad
i\in[m_A],
$$

而 $B$ 的变量和校验指标分别写成

$$
m\in[n_B],
\qquad
\ell\in[m_B].
$$

对三项链复形

$$
C_2\xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0,
$$

本库固定

$$
H_X=\partial_1,
\qquad
H_Z=\partial_2^T.
$$

### 乘积中间项与物理比特扇区

在 $\mathbb F_2$ 上取 $\mathcal A\otimes\mathcal B$。Total degree 为 $2,1,0$ 的链群是

$$
C_2=\mathbb F_2^{n_An_B},
$$

$$
C_1=
\mathbb F_2^{n_Am_B}
\oplus
\mathbb F_2^{m_An_B},
$$

$$
C_0=\mathbb F_2^{m_Am_B}.
$$

中间项 $C_1$ 的两个直和分量就是两类物理量子比特：

| 链群 | 基向量标签 | CSS 对应 |
|---|---|---|
| $C_2$ | $A$-变量 $j$ $\times$ $B$-变量 $m$ | $Z$-校验标签 |
| $C_1$ 第一扇区 | $A$-变量 $j$ $\times$ $B$-校验 $\ell$ | 物理量子比特 |
| $C_1$ 第二扇区 | $A$-校验 $i$ $\times$ $B$-变量 $m$ | 物理量子比特 |
| $C_0$ | $A$-校验 $i$ $\times$ $B$-校验 $\ell$ | $X$-校验标签 |

两个物理扇区不是额外加入的分类，而是 total degree $1=1+0=0+1$ 的两个分量。后文的四类 Tanner 边都在这四组指标之间连接。

### HGP 校验矩阵与对易

乘积边界为

$$
\partial_1=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right],
$$

$$
\partial_2=
\begin{bmatrix}
I_{n_A}\otimes B\\
A\otimes I_{n_B}
\end{bmatrix}.
$$

从 $C_2$ 到 $C_0$ 有两条 product paths。第一条先作用 $B$、再作用 $A$，第二条先作用 $A$、再作用 $B$；两条路径都给出 $A\otimes B$。在特征 $2$ 中，

$$
\partial_1\partial_2
=
A\otimes B+A\otimes B
=0.
$$

按本库的 chain convention，

$$
\boxed{
H_X=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right]
},
$$

$$
\boxed{
H_Z=
\left[
I_{n_A}\otimes B^T
\;\middle|\;
A^T\otimes I_{n_B}
\right]
}.
$$

因为 $H_Z^T=\partial_2$，

$$
H_XH_Z^T
=
\partial_1\partial_2
=0.
$$

HGP 的 CSS 对易因此来自乘积边界平方为零，而不是两张事先猜出的矩阵碰巧正交。

### 与 S007 式 (1) 的记号转换

S007 第 2.2 节从两张经典种子校验矩阵

$$
H_1\in\mathbb F_2^{r_1\times n_1},
\qquad
H_2\in\mathbb F_2^{r_2\times n_2}
$$

出发。它把第二个种子按与本库相反的链方向放入乘积。两套记号的转换是

$$
A=H_1,
\qquad
B=H_2^T,
$$

$$
(m_A,n_A,m_B,n_B)
=
(r_1,n_1,n_2,r_2).
$$

代入 HGP blocks 后，

$$
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right]
=
\left[
H_1\otimes I_{n_2}
\;\middle|\;
I_{r_1}\otimes H_2^T
\right],
$$

$$
\left[
I_{n_A}\otimes B^T
\;\middle|\;
A^T\otimes I_{n_B}
\right]
=
\left[
I_{n_1}\otimes H_2
\;\middle|\;
H_1^T\otimes I_{r_2}
\right].
$$

这正是 S007 的式 (1)。在同一转换下，四组链群基向量成为

| 本库 chain 标签 | S007 标签 | 指标集合 |
|---|---|---|
| $A$-变量 $\times$ $B$-校验 | $q^A_{j,\ell}$ | $(j,\ell)\in[n_1]\times[n_2]$ |
| $A$-校验 $\times$ $B$-变量 | $q^B_{i,m}$ | $(i,m)\in[r_1]\times[r_2]$ |
| $A$-校验 $\times$ $B$-校验 | $x_{i,\ell}$ | $(i,\ell)\in[r_1]\times[n_2]$ |
| $A$-变量 $\times$ $B$-变量 | $z_{j,m}$ | $(j,m)\in[n_1]\times[r_2]$ |

本库中的“$B$-校验 $\ell$”是矩阵 $B=H_2^T$ 的行指标，所以它对应原始种子 $H_2$ 的变量指标；“$B$-变量 $m$”则对应 $H_2$ 的校验指标。这个转置是两套扇区命名看似不同的唯一原因。

### 四类 Tanner 边

Kronecker blocks 可以逐项展开为数据量子比特与校验辅助量子比特之间的边。先取一个非零矩阵元

$$
H_1(i,j)=1.
$$

在 $\mathcal H_X$ 的第一块 $H_1\otimes I_{n_2}$ 中，恒等矩阵固定 $\ell$，所以对每个 $\ell\in[n_2]$ 都有

$$
(x_{i,\ell},q^A_{j,\ell}).
$$

在 $\mathcal H_Z$ 的第二块 $H_1^T\otimes I_{r_2}$ 中，恒等矩阵固定 $m$，所以对每个 $m\in[r_2]$ 都有

$$
(z_{j,m},q^B_{i,m}).
$$

再取

$$
H_2(m,\ell)=1.
$$

在 $\mathcal H_X$ 的第二块 $I_{r_1}\otimes H_2^T$ 中，恒等矩阵固定 $i$，所以对每个 $i\in[r_1]$ 都有

$$
(x_{i,\ell},q^B_{i,m}).
$$

在 $\mathcal H_Z$ 的第一块 $I_{n_1}\otimes H_2$ 中，恒等矩阵固定 $j$，所以对每个 $j\in[n_1]$ 都有

$$
(z_{j,m},q^A_{j,\ell}).
$$

四类边合并为

$$
H_1(i,j)=1
\Longrightarrow
\left\{
(x_{i,\ell},q^A_{j,\ell}),
(z_{j,m},q^B_{i,m})
\right\},
$$

$$
H_2(m,\ell)=1
\Longrightarrow
\left\{
(x_{i,\ell},q^B_{i,m}),
(z_{j,m},q^A_{j,\ell})
\right\},
$$

其中第一行分别对所有 $\ell\in[n_2]$、$m\in[r_2]$ 成立，第二行分别对所有 $i\in[r_1]$、$j\in[n_1]$ 成立。

### 行与列的乘积方向

对 $H_1$ 产生的边，固定 $\ell$ 后，$x_{i,\ell}$ 与 $q^A_{j,\ell}$ 之间的连接就是一份 $H_1$ Tanner 图；固定 $m$ 后，$z_{j,m}$ 与 $q^B_{i,m}$ 之间又是一份 $H_1$ Tanner 图。不同固定坐标给出的副本使用互不相交的节点组，因此同一方向的相容副本可以并行处理。

对 $H_2$ 产生的边，固定 $i$ 后，$x_{i,\ell}$ 与 $q^B_{i,m}$ 之间是一份 $H_2$ Tanner 图；固定 $j$ 后，$z_{j,m}$ 与 $q^A_{j,\ell}$ 之间又是一份 $H_2$ Tanner 图。

所以每条边都固定一个乘积坐标，只改变另一个坐标：

| 种子边 | 固定坐标 | 变化坐标 | S007 图 1(b) 中的方向 |
|---|---|---|---|
| $H_1(i,j)=1$ 作用于 $x,q^A$ | $\ell$ | $i,j$ | 水平 |
| $H_1(i,j)=1$ 作用于 $z,q^B$ | $m$ | $i,j$ | 水平 |
| $H_2(m,\ell)=1$ 作用于 $x,q^B$ | $i$ | $m,\ell$ | 竖直 |
| $H_2(m,\ell)=1$ 作用于 $z,q^A$ | $j$ | $m,\ell$ | 竖直 |

不存在同时改变两个乘积坐标的对角边。这里的“一维分解”表示整个相互作用边集精确分成 $H_1$ Tanner 图副本与 $H_2$ Tanner 图副本；它不表示水平门和竖直门必须同时执行。S007 的执行协议先并行处理一个方向中的相容一维副本，再切换到另一个方向。

### 长度、秩与可选逻辑空间分解

物理比特来自 $C_1$ 的两个扇区，所以

$$
\boxed{
N=n_Am_B+m_An_B
}.
$$

$H_X$ 有 $m_Am_B$ 行，$H_Z$ 有 $n_An_B$ 行；这些是写出的生成元数，不必等于各自的秩。任意有限实例都可直接用

$$
K=N-\operatorname{rank}_{\mathbb F_2}H_X
-\operatorname{rank}_{\mathbb F_2}H_Z
$$

计算逻辑比特数。这一步不需要 Künneth 分解。

若要把逻辑空间进一步分成两个 product sectors，域上的 [[Künneth 分解#二项复形与 HGP 逻辑空间|Künneth 分解]] 给出

$$
H_1(\mathcal A\otimes\mathcal B)
\cong
\ker A\otimes\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes\ker B.
$$

记

$$
k_A=\dim\ker A,
\qquad
k_A^T=\dim\ker A^T,
$$

并类似定义 $k_B,k_B^T$。有限维对偶给出

$$
\dim\operatorname{coker}A=\dim\ker A^T,
\qquad
\dim\operatorname{coker}B=\dim\ker B^T,
$$

所以

$$
\boxed{
K=k_Ak_B^T+k_A^Tk_B
}.
$$

这个公式解释两个逻辑扇区及转置码 kernel 的作用；它不是写出 HGP 校验矩阵、证明 CSS 对易或得到行／列分解的条件。

### qLDPC 条件

HGP 构造本身只保证 CSS 对易。若一族 $A,B$ 的行重和列重都有与码长无关的统一上界，那么 Kronecker 块只复制这些局部关联，$H_X,H_Z$ 的行重和列重也统一有界；此时得到的是 qLDPC 码族。

### 标准的 $\sqrt N$ 参数基准

对一般 $A,B$，距离由四个经典码扇区共同控制。若把核为零的码距约定为 $\infty$，标准 HGP 距离界包含

$$
d_{\mathrm{HGP}}
\ge
\min\{d_A,d_B,d_A^T,d_B^T\}.
$$

因此“$d=\Theta(\sqrt N)$”不是任意 HGP 输入的统一结论，而是等尺度、经典距离线性且转置码扇区不引入更短逻辑算符时的典型参数格局。

一个干净的基准是令 $B=A^T$，并假设

$$
A\in\mathbb F_2^{m\times n}
$$

满行秩，且其经典码满足

$$
k=n-m=\Theta(n),
\qquad
d_A=\Theta(n),
\qquad
m=\Theta(n).
$$

此时 $k_A=k$、$k_A^T=0$，所以

$$
N=n^2+m^2,
\qquad
K=k^2.
$$

非平凡逻辑算符可由一个经典码字与另一个因子的短 cokernel 代表元形成，重量为 $d_A$；结合上述下界可得

$$
d=d_A=\Theta(n)=\Theta(\sqrt N).
$$

若 $A$ 还是经典 LDPC 校验矩阵，这就给出常数编码率、距离 $\Theta(\sqrt N)$ 的 qLDPC 家族。[[Lifted product code]] 要突破的正是这个等尺度乘积中的长度—距离格局，而不是否定 HGP 的对易构造。

### 从 HGP 到 LP

HGP 中每个矩阵元素只是 $0$ 或 $1$。元素 $1$ 表示相应经典变量与校验之间有一条边，元素 $0$ 表示没有边；两个乘积坐标彼此独立。

[[Lifted product code]] 保留三项乘积复形、两个物理量子比特扇区、HGP 型校验矩阵排列和两路径抵消，同时增加 lift 数据：

| HGP 中的数据 | LP 中的替换 |
|---|---|
| 系数域 $\mathbb F_2$ | 记录 lift 的有限维代数 $R$ |
| 矩阵条目 $0/1$ | 携带副本 permutation 的环元素 |
| ordinary tensor product | 识别 lift 坐标的 balanced tensor product $\otimes_R$ |
| 两个完全独立的因子坐标 | 外层 product 坐标与被 balancing 后保留的 lift 坐标 |

因此进入 LP 时仍沿用

$$
C_2\xrightarrow{\partial_2}
C_1^{(A\text{-变量},B\text{-校验})}
\oplus
C_1^{(A\text{-校验},B\text{-变量})}
\xrightarrow{\partial_1}C_0,
$$

$$
H_X=\partial_1,
\qquad
H_Z=\partial_2^T.
$$

新增的问题是环值矩阵的条目如何在每个 lift 内指定副本之间的连接；这由下一篇笔记的 cyclic-shift 表示处理。

### 来源

- Jean-Pierre Tillich, Gilles Zémor, [*Quantum LDPC codes with positive rate and minimum distance proportional to the square root of the blocklength*](https://arxiv.org/abs/0903.0566), IEEE Transactions on Information Theory 60, 1193–1202 (2014)：HGP 构造及其常数率、平方根距离家族。
- Pavel Panteleev, Gleb Kalachev, [*Quantum LDPC Codes with Almost Linear Minimum Distance*](https://arxiv.org/abs/2012.04068), IEEE Transactions on Information Theory 68, 213–229 (2022), Sections II–III：本库采用的 $\mathrm{HP}(A,B)$ chain convention、块矩阵、长度、维数与距离记号。
- Adrian Liu, Wan-Hsuan Lin, Daniel Bochen Tan, Qian Xu, Jason Cong, [S007 全文译本](../../Translations/S007.full.zh-CN.md)，§2.2、式 (1) 与图 1；对应本地 PDF pp.2–3：S007 convention、四类 Tanner 边及水平／竖直一维分解。
