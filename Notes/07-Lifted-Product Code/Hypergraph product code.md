Hypergraph-product code（HGP 码）把两张经典校验矩阵组织成一对自动对易的 CSS 校验矩阵。它不是一组固定参数，而是一种乘积构造；[[Lifted product code]] 会保留同一张乘积骨架，只把系数从 $\mathbb F_2$ 换成带 lift 对称性的代数。

前置笔记是 [[Chain complex 与 cochain complex]]、[[CSS码中的cochain complex]]、[[Cochain complex 的 tensor product]] 和 [[Künneth 分解]]。一般乘积复形的定义与证明沿用这些笔记；product homology 与两个因子 homology 的关系见 Künneth 分解，本篇把两个二项链复形的乘积翻译成 HGP 校验矩阵。

### 从两张经典校验矩阵开始

取

$$
A\in\mathbb F_2^{m_A\times n_A},
\qquad
B\in\mathbb F_2^{m_B\times n_B}.
$$

把它们看成两个二项链复形：

$$
\mathcal A:\quad
\mathbb F_2^{n_A}\xrightarrow{A}\mathbb F_2^{m_A},
\qquad
\mathcal B:\quad
\mathbb F_2^{n_B}\xrightarrow{B}\mathbb F_2^{m_B}.
$$

这里 degree-$1$ 基向量对应经典变量，degree-$0$ 基向量对应经典校验。

先固定与本库一致的 CSS 方向。对一条三项链复形

$$
C_2\xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0,
$$

本文取

$$
H_X=\partial_1,
\qquad
H_Z=\partial_2^T.
$$

因此 chain homology

$$
H_1(C)=\frac{\ker H_X}{\operatorname{im}H_Z^T}
$$

表示 logical $Z$ support classes。对偶以后得到本库 [[CSS码中的cochain complex]] 使用的方向

$$
C_0^*
\xrightarrow{H_X^T}
C_1^*
\xrightarrow{H_Z}
C_2^*,
$$

其 $H^1$ 表示 logical $X$ support classes。后文的 $H_1$ 与已有笔记的 $H^1$ 因此不是冲突，而是同一 CSS 码的 chain/cochain 两个方向。

### 乘积中间项与物理比特

在 $\mathbb F_2$ 上取 $\mathcal A\otimes\mathcal B$。Total degree 为 $2,1,0$ 的三项分别是

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

它们的基向量可按下表读取：

| 链群 | 基向量标签 | CSS 对应 |
|---|---|---|
| $C_2$ | $A$-变量 $\times$ $B$-变量 | $Z$-校验标签 |
| $C_1$ 第一扇区 | $A$-变量 $\times$ $B$-校验 | 物理量子比特 |
| $C_1$ 第二扇区 | $A$-校验 $\times$ $B$-变量 | 物理量子比特 |
| $C_0$ | $A$-校验 $\times$ $B$-校验 | $X$-校验标签 |

乘积边界映射是

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

两条从 $C_2$ 到 $C_0$ 的路径给出同一个 $A\otimes B$。在 $\mathbb F_2$ 中相加后抵消：

$$
\partial_1\partial_2
=
A\otimes B+A\otimes B
=0.
$$

这条等式就是 HGP 的 CSS 对易条件来源。

### HGP 校验矩阵

按上面的 chain convention，

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

由于 $H_Z^T=\partial_2$，

$$
H_XH_Z^T
=\partial_1\partial_2
=0.
$$

转置以后也有 $H_ZH_X^T=0$，正是本库 cochain convention 中的写法。这里不是先猜两张稀疏矩阵再检查正交性；正交性已经包含在乘积边界平方为零这件事里。

### 长度和逻辑比特数

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

计算逻辑比特数。

HGP 还因为系数域是 $\mathbb F_2$ 而有一个简洁的同调公式。记

$$
k_A=\dim\ker A,
\qquad
k_A^T=\dim\ker A^T,
$$

并类似定义 $k_B,k_B^T$。按照 [[Künneth 分解#二项复形与 HGP 逻辑空间]]，两个二项复形的 degree-$1$ homology 分解为

$$
H_1(\mathcal A\otimes\mathcal B)
\cong
\ker A\otimes\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes\ker B.
$$

有限维对偶给出

$$
\dim\operatorname{coker}A=\dim\ker A^T,
\qquad
\dim\operatorname{coker}B=\dim\ker B^T.
$$

对两个扇区取维数，从而

$$
\boxed{
K=k_Ak_B^T+k_A^Tk_B
}.
$$

这个公式也说明为什么转置码的 kernel 不能随意忽略：它决定第二个逻辑扇区是否存在。

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

HGP 中每个矩阵元素只是 $0$ 或 $1$，每个乘积基向量带有两个完全独立的因子坐标。LP 保留本篇的三项复形、两个物理量子比特扇区和两路径抵消，但做两项替换：

1. 把 $\mathbb F_2$ 换成记录群 lift 的有限维代数 $R$；
2. 把 ordinary tensor product 换成 $\otimes_R$，识别两个因子的群坐标。

所以继续阅读 LP 时，真正需要保留的是

$$
\boxed{
C_2\xrightarrow{\partial_2}
C_1^{(A\text{-变量},B\text{-校验})}
\oplus
C_1^{(A\text{-校验},B\text{-变量})}
\xrightarrow{\partial_1}C_0
}
$$

以及

$$
H_X=\partial_1,
\qquad
H_Z=\partial_2^T.
$$

### 来源

- Jean-Pierre Tillich, Gilles Zémor, [*Quantum LDPC codes with positive rate and minimum distance proportional to the square root of the blocklength*](https://arxiv.org/abs/0903.0566), IEEE Transactions on Information Theory 60, 1193–1202 (2014)：HGP 构造及其常数率、平方根距离家族。
- Pavel Panteleev, Gleb Kalachev, [*Quantum LDPC Codes with Almost Linear Minimum Distance*](https://arxiv.org/abs/2012.04068), IEEE Transactions on Information Theory 68, 213–229 (2022), Sections II–III：本文采用的 $\mathrm{HP}(A,B)$ 块矩阵、长度、维数与距离记号。
