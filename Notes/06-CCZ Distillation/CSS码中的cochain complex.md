CSS 码中的 cochain complex 是把 stabilizer、logical operator、syndrome 和 syndrome redundancy 组织进同一串线性映射的 linear-algebraic framework。第一次读 [[Menon 2025 Magic Tricycles]] 时，只需要先把每个 $\ker$、$\operatorname{im}$ 和 quotient 翻译回熟悉的 CSS 码对象。

基本术语见 [[Chain complex 与 cochain complex]]；前置线性代数见 [[二进制空间性质]]；CSS 逻辑基态和 stabilizer 商空间图像见 [[逻辑基态的表示]]。Balanced tensor 与 coinvariant quotient 见 [[Balanced tensor product 与 coinvariant quotient]]；tricycle 矩阵的来源见 [[Tricycle complex 的 balanced-product 构造]]。

### CSS 码先给出两张矩阵

取一个二进制 CSS 码：

$$
H_X\in\mathbb F_2^{r_X\times n},
\qquad
H_Z\in\mathbb F_2^{r_Z\times n}.
$$

$H_X$ 的行给出 $X$-type stabilizers 的 supports，$H_Z$ 的行给出 $Z$-type stabilizers 的 supports。对易条件是

$$
H_ZH_X^T=0.
$$

这条式子已经是 cochain complex 的核心：先由 $X$ checks 生成一个 support，再拿它去算 $Z$ syndrome，结果必为零。

把一个 $X$ operator 写成二进制 support

$$
x\in\mathbb F_2^n,
\qquad
X(x)=\prod_{j=1}^n X_j^{x_j}.
$$

它和所有 $Z$ checks 对易，当且仅当

$$
H_Zx=0.
$$

所以

$$
\ker H_Z
$$

是所有通过 $Z$ checks 的 $X$ supports。这里面既包含非平凡 logical $X$，也包含平凡的 $X$ stabilizers。

---
### stabilizer 方向要商掉

若用

$$
u\in\mathbb F_2^{r_X}
$$

表示选择哪些 $X$ checks 相乘，那么得到的 $X$ stabilizer support 是

$$
H_X^Tu.
$$

所有 $X$ stabilizer supports 组成

$$
\operatorname{im}H_X^T.
$$

由 CSS 对易条件，

$$
H_Z(H_X^Tu)=0,
$$

所以

$$
\operatorname{im}H_X^T\subseteq\ker H_Z.
$$

物理含义是：$X$ stabilizer 当然不会触发 $Z$ checks。

如果两个通过检查的 supports 只相差一个 stabilizer，

$$
x'=x+H_X^Tu,
$$

那么 $X(x')$ 和 $X(x)$ 在 code space 上代表同一个 logical action。因此 logical $X$ 不是单个向量，而是等价类

$$
[x]=x+\operatorname{im}H_X^T.
$$

所有 logical $X$ classes 组成商空间

$$
\boxed{
\ker H_Z/\operatorname{im}H_X^T
}.
$$

先把这个式子读成：

$$
\text{logical }X
=
\frac{\text{通过所有 }Z\text{ checks 的 }X\text{ supports}}
{\text{乘上 }X\text{ stabilizer 不算改变}}.
$$

---
### 把 CSS 商空间写成 cochain 语言

现在定义三项 cochain complex：

$$
C^0\xrightarrow{\delta^0}C^1\xrightarrow{\delta^1}C^2,
$$

并在本文约定下取

$$
C^0=\mathbb F_2^{r_X},
\qquad
C^1=\mathbb F_2^n,
\qquad
C^2=\mathbb F_2^{r_Z},
$$

$$
\delta^0=H_X^T,
\qquad
\delta^1=H_Z.
$$

complex 条件

$$
\delta^1\delta^0=0
$$

就是 CSS 对易条件 $H_ZH_X^T=0$。

落在 $C^1$ 这一项时，刚才的 kernel、image 和 quotient 可以按下面的名字读：

| cochain 术语                                      | CSS 码翻译                     |
| ----------------------------------------------- | --------------------------- |
| $1$-cocycle $x\in\ker\delta^1$                  | 通过 $Z$ checks 的 $X$ support |
| $1$-coboundary $x\in\operatorname{im}\delta^0$  | $X$ stabilizer support      |
| $H^1(C)=\ker\delta^1/\operatorname{im}\delta^0$ | logical $X$ support 的等价类    |

具体地，$x\in C^1$ 先被后一张映射 $\delta^1$ 送去算 syndrome。若

$$
\delta^1x=H_Zx=0,
$$

它就是一个 $1$-cocycle：$X(x)$ 不触发任何 $Z$ syndrome。若同一个 support 还能写成

$$
x=\delta^0u=H_X^Tu,
$$

它就是一个 $1$-coboundary：$x$ 是若干 $X$ checks 相乘得到的 stabilizer support。complex 条件保证每个 coboundary 都自动是 cocycle：

$$
\delta^1(\delta^0u)=0.
$$

这句话翻回 CSS 码，就是 $X$ stabilizer 不会触发 $Z$ syndrome。

因此

$$
H^1(C)
=
\ker\delta^1/\operatorname{im}\delta^0
=
\ker H_Z/\operatorname{im}H_X^T.
$$

这就是后面 cup-product 和 logical $CCZ$ 构造要作用的对象。

后面遇到这些词时，先回到这三个 CSS 对象：cocycle 是“通过检查”，coboundary 是“平凡 stabilizer 方向”，cohomology 是“通过检查后再商掉平凡方向”。

---
### $[\![4,2,2]\!]$ CSS 码的小例子

取

$$
H_X=
\begin{bmatrix}
1&1&1&1
\end{bmatrix},
\qquad
H_Z=
\begin{bmatrix}
1&1&1&1
\end{bmatrix}.
$$

因为

$$
H_ZH_X^T=1+1+1+1=0\pmod2,
$$

这是一个 CSS 码。

$\ker H_Z$ 是所有偶重量向量：

$$
\ker H_Z
=
\{x\in\mathbb F_2^4:|x|\equiv0\pmod2\}.
$$

它的维数是 $3$。$X$ stabilizer 方向为

$$
\operatorname{im}H_X^T
=
\{0000,1111\},
$$

维数是 $1$。因此

$$
\dim\left(\ker H_Z/\operatorname{im}H_X^T\right)=2.
$$

这正对应 $[\![4,2,2]\!]$ 的两个 logical $X$ classes。例如

$$
1100\sim0011,
$$

因为二者相差 $1111$，也就是乘了同一个 $X$ stabilizer。

---
### metacheck 是 syndrome 的检查

普通 CSS 码只需要

$$
C^0\xrightarrow{\delta^0}C^1\xrightarrow{\delta^1}C^2.
$$

Menon 的 tricycle code 还多出一项：

$$
C^0
\xrightarrow{\delta^0}
C^1
\xrightarrow{\delta^1}
C^2
\xrightarrow{\delta^2}
C^3.
$$

在 CSS 语言里，这一项通常写成

$$
\mathbb F_2^{r_X}
\xrightarrow{H_X^T}
\mathbb F_2^n
\xrightarrow{H_Z}
\mathbb F_2^{r_Z}
\xrightarrow{H_{\mathrm{meta}}}
\mathbb F_2^{r_{\mathrm{meta}}}.
$$

其中

$$
\delta^2=H_{\mathrm{meta}},
\qquad
H_{\mathrm{meta}}H_Z=0.
$$

若 data error support 为

$$
e\in\mathbb F_2^n,
$$

则 $Z$ checks 给出的 syndrome 是

$$
s=H_Ze.
$$

由于 $H_{\mathrm{meta}}H_Z=0$，任何真实 data error 产生的 syndrome 都满足

$$
H_{\mathrm{meta}}s=0.
$$

所以 $H_{\mathrm{meta}}$ 不是新的 quantum stabilizer。它是作用在 syndrome bits 上的 classical parity check，用来检查一组 syndrome 是否自洽。

如果实际测量得到 noisy syndrome

$$
\tilde s=s+m,
$$

其中 $m$ 是 syndrome measurement error，那么可能出现

$$
H_{\mathrm{meta}}\tilde s\ne0.
$$

这时 metacheck 直接指出 syndrome 记录本身有错。Menon 的 single-shot state preparation 正是利用同一轮 syndrome 内部的这些冗余，而不是主要依赖多轮时间历史。

---
### metacheck 不能单独保证 single-shot

由

$$
\operatorname{im}H_Z\subseteq\ker H_{\mathrm{meta}}
$$

可知，metacheck 至少不会拒绝真实 data error 的 syndrome。但反过来一般不必成立：

$$
\ker H_{\mathrm{meta}}
\neq
\operatorname{im}H_Z.
$$

也就是说，有些 syndrome strings 可能通过 metachecks，却不一定来自某个小重量 data error。这个差别由

$$
H^2(C)
=
\ker\delta^2/\operatorname{im}\delta^1
=
\ker H_{\mathrm{meta}}/\operatorname{im}H_Z
$$

衡量。

因此 metacheck 的存在只是 single-shot 的入口。真正的 single-shot 保证还需要距离和 soundness 条件：小的 syndrome defect 应该能由小的 measurement error 或小的 data correction 解释，否则 decoder 可能在一轮 noisy syndrome 后留下大残余错误。Menon 论文中关于 $D_Z^{\mathrm{SS}}$ 和 soundness 的讨论属于后续 factory 分析，不是这篇 CSS 翻译笔记的前置。

---
### 注意 convention：$H^1$ 可能指 $X$，也可能指 $Z$

本文采用的方向是

$$
\mathbb F_2^{r_X}
\xrightarrow{H_X^T}
\mathbb F_2^n
\xrightarrow{H_Z}
\mathbb F_2^{r_Z},
$$

所以

$$
H^1(C)=\ker H_Z/\operatorname{im}H_X^T
$$

表示 logical $X$ classes。

有些段落或文献会采用对偶方向：

$$
\mathbb F_2^{r_Z}
\xrightarrow{H_Z^T}
\mathbb F_2^n
\xrightarrow{H_X}
\mathbb F_2^{r_X}.
$$

这时

$$
\ker H_X/\operatorname{im}H_Z^T
$$

表示 logical $Z$ classes。

所以不要只看符号 $H^1$ 就判断它是 $X$ logical 还是 $Z$ logical。先看中间的 $C^1$ 是 qubits，后一张检查矩阵到底是 $H_Z$ 还是 $H_X$。

---
### 为什么 CCZ 构造需要 $H^1$

Menon 的物理 $CCZ$ circuit 可以抽象成一个三线性函数：

$$
f_{\mathrm{CCZ}}:
C^1\times C^1\times C^1
\longrightarrow
\mathbb F_2.
$$

这里 $C^1=\mathbb F_2^Q$ 是 physical qubit support 空间。要从这个三线性函数读出 physical circuit，先固定 physical qubit basis $\{e_q:q\in Q\}$。在基三元组上

$$
A_{abc}
=
f_{\mathrm{CCZ}}(e_a,e_b,e_c)
$$

才是 physical $CCZ$ hyperedge 的指示函数。若

$$
A_{abc}=1,
$$

就在三条输入腿上的单个 physical qubits $a,b,c$ 上放一个 $CCZ_{a,b,c}$。因此物理线路是

$$
U_f
=
\prod_{a,b,c:\ A_{abc}=1}
CCZ_{a,b,c}.
$$

对一般 supports $x,y,z\in C^1$，同一个符号 $f_{\mathrm{CCZ}}$ 表示这个 incidence tensor 的三线性奇偶扩张：

$$
f_{\mathrm{CCZ}}(x,y,z)
=
\bigoplus_{a,b,c\in Q}
A_{abc}x_ay_bz_c.
$$

所以多比特 support 作为输入时，它只是在统计相关 physical $CCZ$ hyperedges 的奇偶性，不是在线性组合 support 上放一扇新的多比特 $CCZ$ 门。

这条线路要成为 well-defined logical gate，不能依赖 logical operator representative 的任意选择。这里 logical $X$ support 先要是 cocycle：

$$
x,y,z\in\ker\delta^1,
$$

因为它们必须通过 $Z$ checks。两个 representatives 表示同一个 logical $X$，当且仅当它们相差一个 $X$ stabilizer support，也就是 coboundary。若

$$
x+\delta^0u
=
x+H_X^Tu,
$$

物理上只是乘了一个 $X$ stabilizer，逻辑作用不应改变。因此需要 $f_{\mathrm{CCZ}}$ 对 coboundary 方向不敏感。精确地说，对任意 $u\in C^0$ 和任意 cocycles $y,z\in\ker\delta^1$，要求

$$
f_{\mathrm{CCZ}}(\delta^0u,y,z)=0,
$$

$$
f_{\mathrm{CCZ}}(y,\delta^0u,z)=0,
$$

$$
f_{\mathrm{CCZ}}(y,z,\delta^0u)=0.
$$

这样才能定义一个只依赖 logical classes 的三线性函数

$$
\bar f_{\mathrm{CCZ}}:
H^1(C)\times H^1(C)\times H^1(C)
\longrightarrow
\mathbb F_2,
$$

其中

$$
H^1(C)
=
\ker\delta^1/\operatorname{im}\delta^0,
\qquad
[x]=x+\operatorname{im}\delta^0.
$$

具体定义为

$$
\bar f_{\mathrm{CCZ}}([x],[y],[z])
=
f_{\mathrm{CCZ}}(x,y,z).
$$

这不是额外的新函数，而是原来的 physical $CCZ$ incidence tensor 在 logical quotient 上诱导出的函数。良定义性来自三线性性和 coboundary 消失条件；例如换代表元 $x\mapsto x+\delta^0u$ 时，

$$
f_{\mathrm{CCZ}}(x+\delta^0u,y,z)
=
f_{\mathrm{CCZ}}(x,y,z)
+
f_{\mathrm{CCZ}}(\delta^0u,y,z)
=
f_{\mathrm{CCZ}}(x,y,z).
$$

其它输入同理。这就是 cochain complex 在 transverse / constant-depth $CCZ$ 构造中的作用：它把“同一个 logical operator 的不同 representatives”系统地商掉，留下作用在 $H^1(C)$ 上的 logical 三体相位。

---
### 第一遍阅读保留什么

读 [[Menon 2025 Magic Tricycles]] 前，只需要保留下面这张翻译表：

| Menon / cochain 术语 | CSS 码翻译 |
|---|---|
| $C^0$ | $X$ check 组合 |
| $C^1$ | physical qubit / Pauli support |
| $C^2$ | $Z$ syndrome bits |
| $C^3$ | syndrome relation / metacheck bits |
| $\delta^0$ | $H_X^T$ |
| $\delta^1$ | $H_Z$ |
| $\delta^2$ | $H_{\mathrm{meta}}$ |
| cocycle | 通过后一张检查的对象 |
| coboundary | 前一张映射生成的平凡方向 |
| $H^1(C)$ | logical $X$ support 的等价类 |
| metacheck | syndrome bits 上的 classical parity check |

暂时可以跳过：

- group algebra 元素 $a,b,c$ 如何生成稀疏循环矩阵；
- balanced product 如何从三个 seed codes 给出 $R\to R^3\to R^3\to R$；
- cup product 和 Leibniz rule 如何让乘法下降到 cohomology；
- Künneth theorem 和 soundness 的严格证明。

这些内容分别放在 [[Balanced tensor product 与 coinvariant quotient]]、[[Tricycle complex 的 balanced-product 构造]]、[[Cup product 与 Leibniz rule]]、[[Symmetric triple cup-product]] 和 [[Menon 2025 Magic Tricycles]] 中。入门阶段先把 CSS 码、logical quotient 和 metacheck 三件事连起来，后面的 balanced product、cup product 与 physical $CCZ$ 判据才有落点。

---
### 来源

- Varun Menon, J. Pablo Bonilla Ataides, Rohan Mehta, Andi Gu, Daniel Bochen Tan, Mikhail D. Lukin, [*Magic tricycles: Efficient magic state generation with finite block-length quantum LDPC codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), arXiv:2508.10714v2, 2025, Supplementary Material and Appendix A.
