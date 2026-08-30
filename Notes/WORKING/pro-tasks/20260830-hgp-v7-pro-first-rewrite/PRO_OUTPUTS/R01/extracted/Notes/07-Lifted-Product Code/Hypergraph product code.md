---
note_type: reference
entry_mode: guided
status: draft
---

超图乘积（hypergraph product, HGP）构造从两张经典二进制校验矩阵出发，产生一对共享同一组物理量子比特列的 CSS 校验矩阵。本文要做的不只是写出最终公式，而是沿着一条可检查的路线把它们构造出来：

$$
\text{经典矩阵}
\longrightarrow
\text{两个二项链复形}
\longrightarrow
\text{三项乘积链复形}
\longrightarrow
H_X,H_Z
\longrightarrow
\text{对易与 Tanner 图}.
$$

前半部分完成一般 HGP 主线：先解释为什么经典矩阵可以放进链复形，再由总次数得到三个链群，由乘积边界逐块推出 $H_X,H_Z$，最后从四个 Kronecker 块读出 Tanner 邻接。后半部分讨论长度、逻辑支撑、qLDPC 条件和参数边界。S007 记号、Künneth 分解、平方根距离基准以及 HGP 到 LP 的接口分别放在独立的选读节；跳过任一选读节都不影响一般构造。

## 从 CSS 对易条件确定构造目标

先取任意一对二进制 CSS 校验矩阵

$$
H_X\in\mathbb F_2^{r_X\times N},
\qquad
H_Z\in\mathbb F_2^{r_Z\times N}.
$$

两张矩阵的列都由同一组 $N$ 个物理量子比特编号。$H_X$ 的一行给出一个 $X$ 型校验的支撑，$H_Z$ 的一行给出一个 $Z$ 型校验的支撑。

设第 $a$ 个 $X$ 型校验和第 $b$ 个 $Z$ 型校验共同作用于 $w_{ab}$ 个量子比特。每个共同位置贡献一次 $XZ=-ZX$，因此两者交换当且仅当 $w_{ab}$ 为偶数。另一方面，

$$
(H_XH_Z^{\mathsf T})_{ab}
=
\sum_{q=1}^N H_X(a,q)H_Z(b,q)
\pmod 2
$$

正是这两个行支撑的重叠数模 $2$。所以全部异型校验彼此对易等价于

$$
\boxed{
H_XH_Z^{\mathsf T}=0
}.
$$

这个条件可以重新组织成一串线性映射。令

$$
C_2=\mathbb F_2^{r_Z},
\qquad
C_1=\mathbb F_2^N,
\qquad
C_0=\mathbb F_2^{r_X},
$$

并取

$$
C_2
\xrightarrow{\ \partial_2=H_Z^{\mathsf T}\ }
C_1
\xrightarrow{\ \partial_1=H_X\ }
C_0.
$$

这里三个空间各有直接的 CSS 含义：

- $C_2$ 的坐标标记写出的 $Z$ 型校验；
- $C_1$ 的坐标标记物理量子比特；
- $C_0$ 的坐标标记写出的 $X$ 型校验。

若 $u\in C_2$ 选择若干个 $Z$ 型校验相乘，那么 $H_Z^{\mathsf T}u\in C_1$ 是所得 $Z$ 型稳定子的物理支撑。再乘以 $H_X$，就是检查这个支撑与每个 $X$ 型校验的重叠奇偶性。于是

$$
\partial_1\partial_2=0
$$

翻译回 CSS 语言就是：任意 $Z$ 型稳定子都与全部 $X$ 型校验交换。

因此 HGP 的核心任务可以说得很具体：从两张经典矩阵构造出三个空间和两支映射，使

$$
C_2\xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0
$$

自动满足 $\partial_1\partial_2=0$，然后取

$$
H_X=\partial_1,
\qquad
H_Z=\partial_2^{\mathsf T}.
$$

## 两张经典校验矩阵为什么能成为二项链复形

取两张任意二进制矩阵

$$
A\in\mathbb F_2^{m_A\times n_A},
\qquad
B\in\mathbb F_2^{m_B\times n_B}.
$$

把 $A$ 看成线性映射时，它从列坐标空间送到行坐标空间：

$$
A:\mathbb F_2^{n_A}\longrightarrow\mathbb F_2^{m_A}.
$$

经典编码语言中，定义域的 $n_A$ 个基向量标记变量节点，陪域的 $m_A$ 个基向量标记校验节点。若 $v\in\mathbb F_2^{n_A}$ 是一个变量取值向量，那么 $Av$ 给出各行校验的奇偶结果。

现在只给这两个空间添加次数，并在两端补零空间：

$$
\mathcal A:\qquad
0
\longrightarrow
A_1=\mathbb F_2^{n_A}
\xrightarrow{\ A\ }
A_0=\mathbb F_2^{m_A}
\longrightarrow
0.
$$

这里下标 $1,0$ 是次数标签，不是维数。矩阵 $A$ 把次数降低一阶，从 $A_1$ 送到 $A_0$。两端没有别的非零映射，所以所有“连续取两次边界”的复合都是

$$
A\circ 0=0,
\qquad
0\circ A=0.
$$

因此任意矩阵都可以这样成为二项链复形；不需要先对 $A$ 施加额外方程。矩阵本身仍然做原来的事情，新增的只是“列坐标在次数 $1$、行坐标在次数 $0$”这一层组织。

同样，把 $B$ 写成

$$
\mathcal B:\qquad
0
\longrightarrow
B_1=\mathbb F_2^{n_B}
\xrightarrow{\ B\ }
B_0=\mathbb F_2^{m_B}
\longrightarrow
0.
$$

为什么选择从次数 $1$ 指向次数 $0$，而不把箭头反过来？原因不是形式偏好，而是我们想让两份二项复形的乘积恰好产生前一节需要的三层结构：

$$
C_2\longrightarrow C_1\longrightarrow C_0.
$$

在这个方向下，最高层来自“变量坐标乘变量坐标”，最低层来自“校验坐标乘校验坐标”，而中间层有“变量乘校验”和“校验乘变量”两种来源。后者正好会成为 HGP 的两类物理量子比特坐标。

为便于后面展开指标，固定以下记号：

$$
i\in[m_A],\qquad j\in[n_A],
$$

分别标记 $A$ 的行和列；并令

$$
\alpha\in[m_B],\qquad \beta\in[n_B],
$$

分别标记 $B$ 的行和列。这里 $[s]=\{1,\ldots,s\}$。

## 总次数如何产生三个链群

### 先看总次数的定义

令乘积链复形为

$$
\mathcal C=\mathcal A\otimes\mathcal B.
$$

普通张量积先产生双指标空间 $A_p\otimes B_q$。为了把这些方格重新排成一条链，给简单张量规定总次数

$$
\deg(a_p\otimes b_q)=p+q.
$$

于是乘积链复形在次数 $r$ 的链群定义为

$$
C_r
=
\bigoplus_{p+q=r}A_p\otimes B_q.
$$

这里内层的张量积把两个因子的基方向两两配对；外层的直和把总次数相同、但来源不同的空间并列保存。总次数是乘积复形的分层规则，不是由维数计算倒推出的结论。

两份种子复形都只在次数 $1$ 和 $0$ 非零，所以可能出现的总次数只有 $2,1,0$。

### 次数 $2$：变量坐标乘变量坐标

总次数 $2$ 只有一种分解：

$$
2=1+1.
$$

因此

$$
\begin{aligned}
C_2
&=A_1\otimes B_1\\
&=\mathbb F_2^{n_A}\otimes\mathbb F_2^{n_B}\\
&\cong\mathbb F_2^{n_An_B}.
\end{aligned}
$$

它的一组基由成对指标

$$
(j,\beta)\in[n_A]\times[n_B]
$$

标记。按照本文的 CSS 约定，$C_2$ 最终标记 $Z$ 型校验；把相应基标签记为

$$
z_{j,\beta}.
$$

这里的 $z_{j,\beta}$ 首先只是一个校验坐标名，不是已经写出的 Pauli 算符。它对应哪一些物理量子比特，要由稍后的 $\partial_2$ 决定。

### 次数 $1$：两种来源形成直和

总次数 $1$ 有两种分解：

$$
1=1+0,
\qquad
1=0+1.
$$

所以

$$
\begin{aligned}
C_1
&=(A_1\otimes B_0)\oplus(A_0\otimes B_1)\\
&\cong
\mathbb F_2^{n_Am_B}
\oplus
\mathbb F_2^{m_An_B}.
\end{aligned}
$$

把第一分量记为

$$
Q_1=A_1\otimes B_0,
$$

它的基标签为

$$
q^{(1)}_{j,\alpha},
\qquad
(j,\alpha)\in[n_A]\times[m_B].
$$

把第二分量记为

$$
Q_2=A_0\otimes B_1,
$$

它的基标签为

$$
q^{(2)}_{i,\beta},
\qquad
(i,\beta)\in[m_A]\times[n_B].
$$

按照链复形到 CSS 码的解释，$C_1$ 是物理支撑空间。因此每个 $q^{(1)}_{j,\alpha}$ 和 $q^{(2)}_{i,\beta}$ 都标记一个物理量子比特，物理比特总数为

$$
\boxed{
N=n_Am_B+m_An_B
}.
$$

这里必须区分“物理扇区”和“逻辑扇区”。直和

$$
C_1=Q_1\oplus Q_2
$$

在施加任何闭合条件、也没有商掉任何稳定子之前就已经存在。它只是说一个物理支撑向量可以唯一写成

$$
v=(v_1,v_2),
\qquad
v_1\in Q_1,\quad v_2\in Q_2.
$$

所以 $Q_1,Q_2$ 是两类物理坐标。逻辑算符则要先满足校验，再把相差稳定子的支撑视为同一类；那是后面由核与商空间得到的对象。两者都可能出现“两个分量”，但它们处在完全不同的构造阶段。

### 次数 $0$：校验坐标乘校验坐标

总次数 $0$ 也只有一种分解：

$$
0=0+0.
$$

于是

$$
\begin{aligned}
C_0
&=A_0\otimes B_0\\
&=\mathbb F_2^{m_A}\otimes\mathbb F_2^{m_B}\\
&\cong\mathbb F_2^{m_Am_B}.
\end{aligned}
$$

它的基由

$$
(i,\alpha)\in[m_A]\times[m_B]
$$

标记。按照本文约定，$C_0$ 最终标记 $X$ 型校验；相应标签记为

$$
x_{i,\alpha}.
$$

至此，三个空间已经逐项得到：

$$
\boxed{
C_2=\mathbb F_2^{n_An_B}
}
$$

$$
\boxed{
C_1=
\mathbb F_2^{n_Am_B}
\oplus
\mathbb F_2^{m_An_B}
}
$$

$$
\boxed{
C_0=\mathbb F_2^{m_Am_B}
}.
$$

下一步不是猜测两张量子校验矩阵，而是把种子边界 $A,B$ 合成为乘积边界。

## 从乘积边界逐块导出 $H_X$ 和 $H_Z$

这一节的目标是从同一条乘积边界公式推出四个 Kronecker 块。推导顺序如下：

1. 写出链复形张量积的边界公式；
2. 分别计算 $\partial_1:C_1\to C_0$ 在两个物理扇区上的作用；
3. 计算 $\partial_2:C_2\to C_1$ 落入两个物理扇区的分量；
4. 令 $H_X=\partial_1$，再把 $\partial_2$ 转置成以校验为行、物理量子比特为列的 $H_Z$。

### 乘积边界公式与符号

对齐次元素 $a_p\in A_p$、$b_q\in B_q$，一般系数下的乘积边界是

$$
\partial(a_p\otimes b_q)
=
\partial_{\mathcal A}a_p\otimes b_q
+
(-1)^p a_p\otimes\partial_{\mathcal B}b_q.
$$

第一项沿 $A$ 因子降低次数，第二项沿 $B$ 因子降低次数。系数 $(-1)^p$ 是 Koszul 符号；它保证两条先后次序相反的路径带相反符号。

本文在 $\mathbb F_2$ 上工作，而

$$
-1=1
\qquad\text{in }\mathbb F_2.
$$

所以最终二进制矩阵里正负号相同。这个省略只在特征 $2$ 中成立；不能把它推广成一般系数下的乘积边界公式。

### Kronecker 积的指标读法

若

$$
M\in\mathbb F_2^{r\times c},
\qquad
N\in\mathbb F_2^{s\times t},
$$

那么

$$
M\otimes N:
\mathbb F_2^c\otimes\mathbb F_2^t
\longrightarrow
\mathbb F_2^r\otimes\mathbb F_2^s
$$

的尺寸为 $rs\times ct$，并满足

$$
(M\otimes N)_{(a,u),(b,v)}
=
M_{a,b}N_{u,v}.
$$

当其中一个因子是恒等矩阵时，它给出一个 Kronecker delta。例如

$$
(A\otimes I_{m_B})_{(i,\alpha),(j,\alpha')}
=
A_{i,j}\delta_{\alpha,\alpha'}.
$$

这意味着 $A$ 改变第一因子的坐标 $j\to i$，而 $I_{m_B}$ 强制第二因子的坐标保持 $\alpha=\alpha'$。后面所有“固定哪个坐标”的结论都来自这种 delta，而不是从图形方向猜出。

### $\partial_1$ 的第一块：作用于 $Q_1=A_1\otimes B_0$

先取第一物理扇区中的基向量

$$
q^{(1)}_{j,\alpha}
=
e_j^A\otimes e_\alpha^B
\in A_1\otimes B_0.
$$

因为 $B_0$ 后面只有零映射，乘积边界只沿 $A$ 因子作用：

$$
\partial_1
\bigl(e_j^A\otimes e_\alpha^B\bigr)
=
Ae_j^A\otimes e_\alpha^B.
$$

因此这一扇区到 $C_0=A_0\otimes B_0$ 的矩阵是

$$
A\otimes I_{m_B}.
$$

它的完整类型为

$$
A\otimes I_{m_B}:
A_1\otimes B_0
\longrightarrow
A_0\otimes B_0,
$$

尺寸为

$$
(m_Am_B)\times(n_Am_B).
$$

其矩阵元为

$$
(A\otimes I_{m_B})_{(i,\alpha),(j,\alpha')}
=
A_{i,j}\delta_{\alpha,\alpha'}.
$$

所以这块有三层含义：

- 它只作用于第一物理扇区 $q^{(1)}_{j,\alpha'}$；
- 它按 $A_{i,j}$ 把 $A$ 的列坐标 $j$ 连接到行坐标 $i$；
- 它固定 $B$ 的行坐标 $\alpha$。

### $\partial_1$ 的第二块：作用于 $Q_2=A_0\otimes B_1$

再取第二物理扇区中的基向量

$$
q^{(2)}_{i,\beta}
=
e_i^A\otimes e_\beta^B
\in A_0\otimes B_1.
$$

这次 $A_0$ 后面只有零映射，所以边界只沿 $B$ 因子作用：

$$
\partial_1
\bigl(e_i^A\otimes e_\beta^B\bigr)
=
e_i^A\otimes Be_\beta^B.
$$

因此第二块是

$$
I_{m_A}\otimes B.
$$

它的类型为

$$
I_{m_A}\otimes B:
A_0\otimes B_1
\longrightarrow
A_0\otimes B_0,
$$

尺寸为

$$
(m_Am_B)\times(m_An_B).
$$

指标展开为

$$
(I_{m_A}\otimes B)_{(i,\alpha),(i',\beta)}
=
\delta_{i,i'}B_{\alpha,\beta}.
$$

所以它只作用于第二物理扇区，按 $B_{\alpha,\beta}$ 改变 $B$ 坐标 $\beta\to\alpha$，并固定 $A$ 的行坐标 $i$。

由于 $C_1$ 按

$$
C_1=Q_1\oplus Q_2
$$

排列，两个分量上的映射要横向拼接。于是

$$
\partial_1
=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right].
$$

按本文的 CSS 约定，

$$
\boxed{
H_X=\partial_1
=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right]
}.
$$

它的行由 $x_{i,\alpha}$ 标记，列先由所有 $q^{(1)}_{j,\alpha}$ 标记，再由所有 $q^{(2)}_{i,\beta}$ 标记；总尺寸为

$$
H_X\in
\mathbb F_2^{m_Am_B\times(n_Am_B+m_An_B)}.
$$

### $\partial_2$ 的第一分量：从 $C_2$ 落入 $Q_1$

取

$$
z_{j,\beta}
=
e_j^A\otimes e_\beta^B
\in A_1\otimes B_1.
$$

若先沿 $B$ 因子取边界，就得到

$$
e_j^A\otimes Be_\beta^B
\in A_1\otimes B_0=Q_1.
$$

在一般系数下，这一项带 $(-1)^1=-1$；在 $\mathbb F_2$ 中负号消失。因此落入第一物理扇区的块是

$$
I_{n_A}\otimes B.
$$

其类型为

$$
I_{n_A}\otimes B:
A_1\otimes B_1
\longrightarrow
A_1\otimes B_0,
$$

尺寸为

$$
(n_Am_B)\times(n_An_B).
$$

矩阵元是

$$
(I_{n_A}\otimes B)_{(j,\alpha),(j',\beta)}
=
\delta_{j,j'}B_{\alpha,\beta}.
$$

所以它固定 $A$ 的列坐标 $j$，按 $B$ 改变第二因子的坐标 $\beta\to\alpha$。

### $\partial_2$ 的第二分量：从 $C_2$ 落入 $Q_2$

若沿 $A$ 因子取边界，则

$$
Ae_j^A\otimes e_\beta^B
\in A_0\otimes B_1=Q_2.
$$

对应块为

$$
A\otimes I_{n_B}.
$$

其类型为

$$
A\otimes I_{n_B}:
A_1\otimes B_1
\longrightarrow
A_0\otimes B_1,
$$

尺寸为

$$
(m_An_B)\times(n_An_B).
$$

矩阵元为

$$
(A\otimes I_{n_B})_{(i,\beta),(j,\beta')}
=
A_{i,j}\delta_{\beta,\beta'}.
$$

所以它按 $A$ 改变第一因子的坐标 $j\to i$，并固定 $B$ 的列坐标 $\beta$。

两个结果落入 $C_1$ 的两个直和分量，因此要竖直堆叠：

$$
\partial_2
=
\begin{bmatrix}
I_{n_A}\otimes B\\
A\otimes I_{n_B}
\end{bmatrix}
\qquad
\text{over }\mathbb F_2.
$$

若保留一般系数下的 Koszul 符号，并继续采用当前直和顺序，则第一块应写成 $-I_{n_A}\otimes B$。二进制 HGP 中这与上式相同。

### 为什么 $H_Z$ 是 $\partial_2$ 的转置

矩阵 $\partial_2$ 的列由 $C_2$ 的 $Z$ 型校验标签 $z_{j,\beta}$ 编号，行由 $C_1$ 的物理量子比特编号。稳定子校验矩阵采用相反的排布：每一行是一条校验，每一列是一个物理量子比特。因此必须取转置：

$$
H_Z=\partial_2^{\mathsf T}.
$$

逐块转置给出

$$
\boxed{
H_Z
=
\left[
I_{n_A}\otimes B^{\mathsf T}
\;\middle|\;
A^{\mathsf T}\otimes I_{n_B}
\right]
}.
$$

第一块的类型和尺寸为

$$
I_{n_A}\otimes B^{\mathsf T}:
Q_1
\longrightarrow
C_2,
$$

$$
(n_An_B)\times(n_Am_B),
$$

并且

$$
(I_{n_A}\otimes B^{\mathsf T})_{(j,\beta),(j',\alpha)}
=
\delta_{j,j'}B_{\alpha,\beta}.
$$

它作用于第一物理扇区，固定 $A$ 的列坐标 $j$，并用 $B^{\mathsf T}$ 把 $B$ 的行坐标 $\alpha$ 与列坐标 $\beta$ 相连。

第二块的类型和尺寸为

$$
A^{\mathsf T}\otimes I_{n_B}:
Q_2
\longrightarrow
C_2,
$$

$$
(n_An_B)\times(m_An_B),
$$

并且

$$
(A^{\mathsf T}\otimes I_{n_B})_{(j,\beta),(i,\beta')}
=
A_{i,j}\delta_{\beta,\beta'}.
$$

它作用于第二物理扇区，固定 $B$ 的列坐标 $\beta$，并用 $A^{\mathsf T}$ 把 $A$ 的行坐标 $i$ 与列坐标 $j$ 相连。

最终，

$$
H_Z\in
\mathbb F_2^{n_An_B\times(n_Am_B+m_An_B)}.
$$

两张矩阵现在拥有完全相同的 $N$ 列，而且每一块的来源、目标、尺寸和固定坐标都由乘积边界确定，而不是事后补上的规则。

## 两条乘积路径为什么保证 CSS 对易

这一节要证明

$$
H_XH_Z^{\mathsf T}=0.
$$

由于

$$
H_X=\partial_1,
\qquad
H_Z^{\mathsf T}=\partial_2,
$$

只需证明

$$
\partial_1\partial_2=0.
$$

### 先看证明地图

从 $C_2=A_1\otimes B_1$ 到 $C_0=A_0\otimes B_0$ 有两条路径：

$$
\begin{array}{ccccc}
&&A_1\otimes B_1&&\\
&\overset{I\otimes B}{\swarrow}&&
\overset{A\otimes I}{\searrow}&\\
A_1\otimes B_0&&&&A_0\otimes B_1\\
&\underset{A\otimes I}{\searrow}&&
\underset{I\otimes B}{\swarrow}&\\
&&A_0\otimes B_0&&
\end{array}
$$

左路先沿 $B$ 因子，再沿 $A$ 因子；右路的次序相反。因为两张矩阵作用在不同张量因子上，两条路径得到同一个线性映射 $A\otimes B$。一般系数下，Koszul 符号让两份贡献一正一负；在 $\mathbb F_2$ 中，正负相同，但同一个二进制贡献出现两次仍然等于零。

### 用块矩阵计算

代入前面的两个边界矩阵：

$$
\begin{aligned}
\partial_1\partial_2
&=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right]
\begin{bmatrix}
I_{n_A}\otimes B\\
A\otimes I_{n_B}
\end{bmatrix}\\
&=
(A\otimes I_{m_B})(I_{n_A}\otimes B)
+
(I_{m_A}\otimes B)(A\otimes I_{n_B}).
\end{aligned}
$$

Kronecker 积满足

$$
(M\otimes N)(P\otimes Q)
=
(MP)\otimes(NQ)
$$

，只要普通矩阵乘法的尺寸相容。因此

$$
(A\otimes I_{m_B})(I_{n_A}\otimes B)
=
A\otimes B,
$$

并且

$$
(I_{m_A}\otimes B)(A\otimes I_{n_B})
=
A\otimes B.
$$

在 $\mathbb F_2$ 中，

$$
A\otimes B+A\otimes B=0,
$$

所以

$$
\boxed{
\partial_1\partial_2=0
}
$$

以及

$$
\boxed{
H_XH_Z^{\mathsf T}=0
}.
$$

### 用单个指标检查两条路径

块计算可以再落到一个具体矩阵元上。固定起点 $z_{j,\beta}$ 和终点 $x_{i,\alpha}$。

沿第一条路径，$B$ 先把 $\beta$ 连到 $\alpha$，贡献 $B_{\alpha,\beta}$；随后 $A$ 把 $j$ 连到 $i$，贡献 $A_{i,j}$。总贡献是

$$
A_{i,j}B_{\alpha,\beta}.
$$

沿第二条路径，$A$ 先贡献 $A_{i,j}$，$B$ 再贡献 $B_{\alpha,\beta}$，总贡献仍是

$$
A_{i,j}B_{\alpha,\beta}.
$$

因此每个起点—终点对都收到两份相同贡献。模 $2$ 相加后它们逐项消失。这正是“乘积复形的边界连续作用两次为零”在 HGP 指标中的具体内容，也是 HGP 构造自动保证 CSS 对易的原因。

## 从四个 Kronecker 块读出 Tanner 图

现在矩阵已经构造完成，可以把非零矩阵元翻译成 Tanner 邻接。这里讨论的是抽象校验图：一侧是物理量子比特节点，另一侧是校验节点。具体综合征提取电路是否为每条校验配置一个辅助量子比特、使用几个辅助量子比特以及怎样调度门，是额外的实现选择。

回顾四类节点：

$$
q^{(1)}_{j,\alpha}
\in Q_1,
\qquad
q^{(2)}_{i,\beta}
\in Q_2,
$$

$$
x_{i,\alpha}
\in C_0,
\qquad
z_{j,\beta}
\in C_2.
$$

### 由 $A_{i,j}=1$ 产生的两类边

第一类来自 $H_X$ 的块 $A\otimes I_{m_B}$。其非零条件是

$$
A_{i,j}=1,
\qquad
\alpha=\alpha'.
$$

所以对每个固定的 $\alpha\in[m_B]$，

$$
x_{i,\alpha}
\longleftrightarrow
q^{(1)}_{j,\alpha}.
$$

这条边改变 $A$ 坐标 $j\leftrightarrow i$，固定 $B$ 的行坐标 $\alpha$。

第二类来自 $H_Z$ 的块 $A^{\mathsf T}\otimes I_{n_B}$。对每个固定的 $\beta\in[n_B]$，

$$
z_{j,\beta}
\longleftrightarrow
q^{(2)}_{i,\beta}.
$$

它仍由同一个非零元 $A_{i,j}=1$ 决定，只是 $A^{\mathsf T}$ 使校验矩阵的行由 $j$ 编号、列由 $i$ 编号。它改变 $A$ 坐标，固定 $B$ 的列坐标 $\beta$。

因此一条种子 Tanner 边 $i\leftrightarrow j$ 在 HGP 中复制成两族边：一族进入 $X$ 型校验与第一物理扇区之间，另一族进入 $Z$ 型校验与第二物理扇区之间。

### 由 $B_{\alpha,\beta}=1$ 产生的两类边

第三类来自 $H_X$ 的块 $I_{m_A}\otimes B$。对每个固定的 $i\in[m_A]$，

$$
x_{i,\alpha}
\longleftrightarrow
q^{(2)}_{i,\beta}.
$$

这条边改变 $B$ 坐标 $\beta\leftrightarrow\alpha$，固定 $A$ 的行坐标 $i$。

第四类来自 $H_Z$ 的块 $I_{n_A}\otimes B^{\mathsf T}$。对每个固定的 $j\in[n_A]$，

$$
z_{j,\beta}
\longleftrightarrow
q^{(1)}_{j,\alpha}.
$$

它也由 $B_{\alpha,\beta}=1$ 决定，改变 $B$ 坐标并固定 $A$ 的列坐标 $j$。

把四类边合在一起，可以写成紧凑的索引规则：

$$
A_{i,j}=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\alpha}&\longleftrightarrow q^{(1)}_{j,\alpha}
&&\text{for every }\alpha,\\
z_{j,\beta}&\longleftrightarrow q^{(2)}_{i,\beta}
&&\text{for every }\beta,
\end{aligned}
\right.
$$

$$
B_{\alpha,\beta}=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\alpha}&\longleftrightarrow q^{(2)}_{i,\beta}
&&\text{for every }i,\\
z_{j,\beta}&\longleftrightarrow q^{(1)}_{j,\alpha}
&&\text{for every }j.
\end{aligned}
\right.
$$

### 种子图副本与两个乘积方向

固定 $\alpha$ 时，节点

$$
\{x_{i,\alpha}\}_i
\quad\text{和}\quad
\{q^{(1)}_{j,\alpha}\}_j
$$

之间的邻接就是 $A$ 的 Tanner 图的一份副本。固定 $\beta$ 时，

$$
\{z_{j,\beta}\}_j
\quad\text{和}\quad
\{q^{(2)}_{i,\beta}\}_i
$$

之间也具有同一个 $A$ 关联模式。

同理，固定 $i$ 或固定 $j$ 时，另外两类边分别给出 $B$ Tanner 图的副本。因此一般 HGP 图天然分成两个乘积方向：

- $A$ 方向：只改变 $A$ 坐标，固定一个 $B$ 坐标；
- $B$ 方向：只改变 $B$ 坐标，固定一个 $A$ 坐标。

“水平”和“竖直”只是把这两个抽象方向画到平面上以后选取的布局名称，并不是 HGP 码的内禀数据。

四个块中总有一个恒等矩阵，所以每条边都固定一个坐标。不存在一条基本 Tanner 边同时把

$$
(j,\alpha)
\longrightarrow
(i,\beta)
$$

中的两个坐标都改变。换句话说，HGP 的四类边没有相对于乘积坐标的“对角边”。这项结构正是把大图拆成种子图副本的原因。

## 选读：与 S007 式 (1) 的记号转换

本节只用于阅读 S007，可直接跳到“长度、校验数与逻辑支撑”。一般 HGP 构造已经在 $A,B$ 记号下闭合。

S007 把两张经典种子矩阵写成

$$
H_1^{\mathrm{S007}}
\in\mathbb F_2^{r_1\times n_1},
\qquad
H_2^{\mathrm{S007}}
\in\mathbb F_2^{r_2\times n_2}.
$$

论文的式 (1) 是

$$
\mathcal H_X
=
\left[
H_1^{\mathrm{S007}}\otimes I_{n_2}
\;\middle|\;
I_{r_1}\otimes
\left(H_2^{\mathrm{S007}}\right)^{\mathsf T}
\right],
$$

$$
\mathcal H_Z
=
\left[
I_{n_1}\otimes H_2^{\mathrm{S007}}
\;\middle|\;
\left(H_1^{\mathrm{S007}}\right)^{\mathsf T}
\otimes I_{r_2}
\right].
$$

要与本文的公式逐块一致，应取

$$
A=H_1^{\mathrm{S007}},
\qquad
B=\left(H_2^{\mathrm{S007}}\right)^{\mathsf T}.
$$

于是尺寸对应为

$$
m_A=r_1,
\qquad
n_A=n_1,
\qquad
m_B=n_2,
\qquad
n_B=r_2.
$$

注意第二因子的方向发生了转置：本文把 $B$ 本身视为次数 $1$ 到次数 $0$ 的边界，而 S007 在 $H_X$ 的第二块中直接写 $H_2^{\mathsf T}$。

在这组转换下，本文的节点标签对应为

$$
q^{(1)}_{j,\alpha}
\longleftrightarrow
q^A_{j,\ell},
\qquad
\alpha=\ell\in[n_2],
$$

$$
q^{(2)}_{i,\beta}
\longleftrightarrow
q^B_{i,m},
\qquad
\beta=m\in[r_2],
$$

$$
x_{i,\alpha}
\longleftrightarrow
x_{i,\ell},
\qquad
z_{j,\beta}
\longleftrightarrow
z_{j,m}.
$$

因此 S007 的四类边正是前一节规则的改名：

$$
H_1^{\mathrm{S007}}(i,j)=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\ell}&\longleftrightarrow q^A_{j,\ell},\\
z_{j,m}&\longleftrightarrow q^B_{i,m},
\end{aligned}
\right.
$$

$$
H_2^{\mathrm{S007}}(m,\ell)=1
\Longrightarrow
\left\{
\begin{aligned}
x_{i,\ell}&\longleftrightarrow q^B_{i,m},\\
z_{j,m}&\longleftrightarrow q^A_{j,\ell}.
\end{aligned}
\right.
$$

S007 的图 1(b) 进一步把 $H_1$ 方向画成水平组，把 $H_2$ 方向画成竖直组，并把校验节点实现为综合征提取中的校验辅助量子比特。这些都是论文所选中性原子布局和电路模型中的物理语义。ONEX 怎样分别求解行、列一维重排，属于从 Tanner 图到硬件执行计划的下一层问题；它不改变 HGP 的代数定义，也不能反过来说明一般 HGP 必须采用水平／竖直布局或一校验一辅助量子比特的实现。

S007 第 6 节的 LP 示例同样是来源特定的执行案例。它展示的单项式种子矩阵可以用来读取循环移位标签，但没有同时展示一般 LP 记号中的完整第二因子；因此不能只凭该矩阵重建完整 LP 校验矩阵、全部扇区或实例参数。具体执行层次见 [[S007 中 LP 码的分层执行]]。

## 长度、校验数与逻辑支撑

从 $C_1=Q_1\oplus Q_2$ 已经得到物理比特数

$$
N=n_Am_B+m_An_B.
$$

写出的 $X$ 型校验行数和 $Z$ 型校验行数分别为

$$
R_X=m_Am_B,
\qquad
R_Z=n_An_B.
$$

这里是“写出的行数”，不一定等于独立稳定子数。若校验行之间存在二进制线性关系，矩阵秩会小于行数。

因为 $X$ 型与 $Z$ 型生成元在二进制辛表示中占据不同分量，而两类生成元又满足 CSS 对易，独立稳定子数为

$$
\operatorname{rank}H_X+\operatorname{rank}H_Z.
$$

所以逻辑比特数可以直接由展开后的二进制矩阵计算：

$$
\boxed{
K
=
N-\operatorname{rank}H_X-\operatorname{rank}H_Z
}.
$$

这个秩公式对任意有限 HGP 实例都可直接使用，不需要先知道 Künneth 分解。

### 一阶同调表示 logical-$Z$ 支撑类

取一个 $Z$ 型 Pauli 支撑向量

$$
v\in C_1=\mathbb F_2^N.
$$

它与全部 $X$ 型校验交换，当且仅当

$$
H_Xv=0.
$$

所以允许的 $Z$ 型支撑组成

$$
\ker H_X.
$$

若两个允许支撑相差一个 $Z$ 型稳定子，那么它们在编码子空间上代表同一个逻辑作用。所有 $Z$ 型稳定子支撑组成

$$
\operatorname{im}H_Z^{\mathsf T}.
$$

链条件保证

$$
\operatorname{im}H_Z^{\mathsf T}
\subseteq
\ker H_X.
$$

因此 logical-$Z$ 支撑等价类组成

$$
\boxed{
H_1(\mathcal C)
=
\frac{\ker H_X}
{\operatorname{im}H_Z^{\mathsf T}}
}.
$$

这里的 $H_1(\mathcal C)$ 是一阶同调，是一个二进制向量空间。它不是编码 Hilbert 空间本身。若其维数为 $K$，编码子空间的复维数才是 $2^K$。

对偶地，logical-$X$ 支撑类为

$$
\frac{\ker H_Z}
{\operatorname{im}H_X^{\mathsf T}}.
$$

它可以视为对偶上链复形的一阶上同调 $H^1$。所以只看到符号 $H_1$ 或 $H^1$ 时不能先猜它代表哪一种逻辑 Pauli；必须同时检查箭头方向和后一张检查矩阵。

再次强调，$Q_1,Q_2$ 是 $C_1$ 在取核和商空间之前的物理坐标分解；$H_1(\mathcal C)$ 则是在整个 $C_1$ 中先取闭合支撑、再商掉稳定子得到的逻辑支撑类。二者不是同一个“扇区”概念。

## 选读：Künneth 如何分解逻辑支撑并给出 $K$

本节回答一个已经自然出现的问题：能否不对大矩阵直接求秩，而是从两份种子复形的核与余核看出逻辑支撑来自哪里？只关心一般构造、Tanner 图或 qLDPC 条件时，可以跳过本节。

在域 $\mathbb F_2$ 上，Künneth 同构把乘积复形的一阶同调分成

$$
H_1(\mathcal A\otimes\mathcal B)
\cong
H_1(\mathcal A)\otimes H_0(\mathcal B)
\oplus
H_0(\mathcal A)\otimes H_1(\mathcal B).
$$

对二项复形

$$
0\longrightarrow A_1\xrightarrow{A}A_0\longrightarrow0,
$$

次数 $1$ 没有更高层边界，所以

$$
H_1(\mathcal A)=\ker A.
$$

次数 $0$ 的全部向量都被后面的零映射送到零，而从次数 $1$ 来的边界是 $\operatorname{im}A$，因此

$$
H_0(\mathcal A)
=
A_0/\operatorname{im}A
=
\operatorname{coker}A.
$$

对 $\mathcal B$ 同理。于是

$$
\boxed{
H_1(\mathcal A\otimes\mathcal B)
\cong
\ker A\otimes\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes\ker B
}.
$$

第一项由 $A$ 方向的闭合变量向量和 $B$ 行空间中未被 $B$ 的像覆盖的商类组成；它可以在第一物理扇区 $A_1\otimes B_0$ 中选择代表元。第二项交换两个因子的作用，可以在第二物理扇区 $A_0\otimes B_1$ 中选择代表元。

这两个同调直和项仍然不是原始的两个物理扇区。物理扇区包含所有坐标，而同调项只保留通过检查、再商掉边界后的类。给一个逻辑类加上 $\partial_2$ 的像还可能得到同时占据两个物理扇区的等价代表元。

定义

$$
k_A=\dim\ker A,
\qquad
k_A^{\mathsf T}=\dim\ker A^{\mathsf T},
$$

$$
k_B=\dim\ker B,
\qquad
k_B^{\mathsf T}=\dim\ker B^{\mathsf T}.
$$

有限维线性代数给出

$$
\dim\operatorname{coker}A
=
m_A-\operatorname{rank}A
=
\dim\ker A^{\mathsf T}
=
k_A^{\mathsf T},
$$

以及相同的 $B$ 公式。对 Künneth 直和取维数，得到

$$
\boxed{
K
=
k_Ak_B^{\mathsf T}
+
k_A^{\mathsf T}k_B
}.
$$

这条公式与前面的秩公式计算同一个 $K$，但揭示了逻辑支撑的两个来源。

这里使用“系数是域”这一条件很重要。提升乘积码通常在环或群代数上先作模张量积；一般环上的乘积同调可能出现额外的 $\operatorname{Tor}$ 项、谱序列微分和扩张问题，不能把上式原样套到 LP 码。完整的域上证明和一般系数边界见 [[Künneth 分解]]。

## HGP 何时形成 qLDPC 码族

HGP 构造对任意 $A,B$ 都给出一个 CSS 码，但“是 CSS 码”不等于“是量子低密度奇偶校验码”。

对一族种子矩阵，定义最大行重和最大列重：

$$
r_A=\max_i\operatorname{wt}(A_{i,*}),
\qquad
c_A=\max_j\operatorname{wt}(A_{*,j}),
$$

$$
r_B=\max_\alpha\operatorname{wt}(B_{\alpha,*}),
\qquad
c_B=\max_\beta\operatorname{wt}(B_{*,\beta}).
$$

先看量子校验的行重。一个 $X$ 型校验 $x_{i,\alpha}$ 在第一扇区沿 $A$ 的第 $i$ 行取邻居，在第二扇区沿 $B$ 的第 $\alpha$ 行取邻居。两个扇区不重叠，所以

$$
\operatorname{wt}(H_X\text{ row }(i,\alpha))
=
\operatorname{wt}(A_{i,*})
+
\operatorname{wt}(B_{\alpha,*})
\le r_A+r_B.
$$

一个 $Z$ 型校验 $z_{j,\beta}$ 在第一扇区读取 $B$ 的第 $\beta$ 列，在第二扇区读取 $A$ 的第 $j$ 列，因此

$$
\operatorname{wt}(H_Z\text{ row }(j,\beta))
=
\operatorname{wt}(B_{*,\beta})
+
\operatorname{wt}(A_{*,j})
\le c_B+c_A.
$$

再看每个物理量子比特参与多少校验。对第一扇区的 $q^{(1)}_{j,\alpha}$：

$$
\operatorname{wt}(H_X\text{ column }(j,\alpha))
=
\operatorname{wt}(A_{*,j})
\le c_A,
$$

$$
\operatorname{wt}(H_Z\text{ column }(j,\alpha))
=
\operatorname{wt}(B_{\alpha,*})
\le r_B.
$$

对第二扇区的 $q^{(2)}_{i,\beta}$：

$$
\operatorname{wt}(H_X\text{ column }(i,\beta))
=
\operatorname{wt}(B_{*,\beta})
\le c_B,
$$

$$
\operatorname{wt}(H_Z\text{ column }(i,\beta))
=
\operatorname{wt}(A_{i,*})
\le r_A.
$$

因此，一个直接且透明的充分条件是：随着码长增长，$A,B$ 的行重和列重都由与规模无关的常数统一限制。此时 $H_X,H_Z$ 的校验重量和每个物理量子比特的校验度数也都统一有界，所得 HGP 家族才是 qLDPC 家族。

若种子矩阵稠密，HGP 仍然是合法 CSS 构造，但输出一般不是 qLDPC。稀疏性本身也不推出正编码率或大码距；这些还取决于种子秩、核维数和距离。

## 选读：标准的 $\sqrt N$ 距离基准

本节说明文献中常见的

$$
d=\Theta(\sqrt N)
$$

是怎样在一组明确条件下出现的。它不是任意 HGP 输入的结论，也不是仅由四块公式自动推出的性质。

取一族矩阵

$$
A\in\mathbb F_2^{m\times n},
\qquad
m<n,
$$

并作对称选择

$$
B=A^{\mathsf T}.
$$

假设：

1. $A$ 满行秩，因此 $\operatorname{rank}A=m$；
2. $m=\Theta(n)$，并且 $k=n-m=\Theta(n)$；
3. 经典码 $\ker A$ 的距离满足 $d_A=\Theta(n)$；
4. 使用标准 HGP 距离下界；在当前满行秩、$B=A^{\mathsf T}$ 的情形，它给出量子距离 $d\ge d_A$；
5. 若还要得到 qLDPC 家族，则 $A$ 的行重和列重需统一有界。

先计算长度。此时

$$
m_A=m,
\qquad
n_A=n,
\qquad
m_B=n,
\qquad
n_B=m,
$$

所以

$$
N=n^2+m^2=\Theta(n^2).
$$

再计算逻辑比特数。$H_X$ 的第一块是 $A\otimes I_n$，其行秩为

$$
\operatorname{rank}(A\otimes I_n)
=
\operatorname{rank}A\cdot n
=
mn.
$$

它已经等于 $H_X$ 的总行数，因此

$$
\operatorname{rank}H_X=mn.
$$

同理，$H_Z$ 的第一块是 $I_n\otimes A$，也有满行秩 $mn$，故

$$
\operatorname{rank}H_Z=mn.
$$

于是

$$
K
=
n^2+m^2-2mn
=
(n-m)^2
=
k^2.
$$

由 $k=\Theta(n)$ 可得

$$
K=\Theta(n^2)=\Theta(N),
$$

也就是这一条件化家族具有常数量级的编码率。

还可以显式看见一个重量为 $d_A$ 的非平凡 logical-$Z$ 支撑。取最小重量非零码字

$$
c\in\ker A,
\qquad
\operatorname{wt}(c)=d_A.
$$

因为 $\operatorname{im}A^{\mathsf T}$ 是 $\mathbb F_2^n$ 的真子空间，至少有一个标准基向量 $e_\alpha$ 不属于它。又因为 $(\operatorname{im}A^{\mathsf T})^\perp=\ker A$，线性分离给出某个 $y\in\ker A$，使 $y_\alpha=1$。把

$$
v=c\otimes e_\alpha
$$

放在第一物理扇区，并在第二物理扇区取零。由于 $Ac=0$，

$$
H_Xv
=
(Ac)\otimes e_\alpha
=
0.
$$

所以 $v$ 与所有 $X$ 型校验交换。它不是 $Z$ 型稳定子支撑。再取线性函数 $\lambda$ 满足 $\lambda(c)=1$，并令下面的函数在第二物理扇区上取零：

$$
\lambda\otimes y^{\mathsf T}
$$

会消去所有 $(I_n\otimes A^{\mathsf T})w$，因为 $Ay=0$，但在 $v$ 上取值为 $1$。因此 $v\notin\operatorname{im}H_Z^{\mathsf T}$，它确实代表非平凡逻辑类，并给出

$$
d\le d_A.
$$

结合假设中的标准 HGP 距离下界 $d\ge d_A$，得到

$$
d=d_A=\Theta(n)=\Theta(\sqrt N).
$$

这段推导同时说明哪些条件不能被省略：

- 若经典距离不是线性的，就不能得到平方根量子距离；
- 若 $m$ 与 $n$ 的尺度关系不同，$N$ 与 $n^2$ 的比较会改变；
- 若 $k$ 不是线性的，就不能据此得到常数编码率；
- 若种子行重或列重增长，所得家族不一定是 qLDPC；
- 对一般 $A,B$，不能把这个对称满秩例子的 $K$ 或 $d$ 公式直接照搬。

因此 $\Theta(\sqrt N)$ 应被读成标准条件化基准，而不是 HGP 三字自带的参数定律。

## 选读：从 HGP 到 LP 的安全接口

HGP 的四块结构是理解 lifted-product（LP）码的入口，但“把二进制条目换成环元素”这句话需要分层解释，不能把所有环元素都叫作置换。

在 HGP 中，矩阵条目属于 $\mathbb F_2$。条目 $1$ 只表示相应原型节点之间有一条边。LP 则取某个有限维 $\mathbb F_2$-代数 $R$，并用环值矩阵

$$
A\in R^{m_A\times n_A},
\qquad
B\in R^{m_B\times n_B}.
$$

要得到真正的二进制 CSS 矩阵，还需选择保持加法和乘法的二进制块表示

$$
\Phi:R\longrightarrow
\operatorname{Mat}_{\ell\times\ell}(\mathbb F_2).
$$

一个环值坐标由此展开成 $\ell$ 个二进制坐标，每个系数被替换为一个 $\ell\times\ell$ 块。

### 什么时候一个系数对应单个置换块

在循环 lift 中常取

$$
R_\ell=\mathbb F_2[x]\big/\langle x^\ell-1\rangle
$$

，并令循环移位矩阵 $P$ 满足

$$
Pe_t=e_{t+1\bmod\ell}.
$$

单项式给出

$$
\Phi(x^s)=P^s,
$$

这确实是一个置换矩阵。因此，一个循环单项式或更一般的群基元素可以表示一组一一配对的副本连接。

但一般多项式

$$
r(x)=\sum_s c_sx^s
$$

展开为

$$
\Phi(r)=\sum_s c_sP^s.
$$

它是若干置换块在 $\mathbb F_2$ 中的和，不必仍是单个置换矩阵。不同项重合时还可能模 $2$ 抵消。

若 $R$ 只是一般有限维代数，那么一个元素通过 $\Phi$ 只保证给出某个线性块；它甚至未必能分解成具有直接图论含义的置换之和。因此下面三句话不能混用：

$$
\text{群基元素}
\longrightarrow
\text{一个置换块},
$$

$$
\text{群代数元素}
\longrightarrow
\text{置换块的二进制和},
$$

$$
\text{一般代数元素}
\longrightarrow
\text{一般线性块}.
$$

### 哪些 HGP 骨架可以保留

LP 仍可保留 HGP 的三项乘积形状、两个中间物理扇区以及四块排列。区别在于，背后的张量积通常是模上的 balanced tensor product，而不是先把所有系数展开成大二进制矩阵后再作普通 HGP。

在交换、特征为 $2$ 的系数代数中，若块表示保持乘法，并且反对合与二进制转置相容，就可以把 HGP 的两路径证明提升到环值层：两条路径产生相同的系数乘积，特征 $2$ 使它们相消。

非交换情形需要更多结构。一个因子通常要作为右模，另一个作为左模；左右作用必须以适当方式交换，矩阵系数的乘法次序也必须与所选转置或反对合约定相容。仅仅写下一个形式符号 $*$，并不能无条件推出展开后的二进制矩阵满足 CSS 对易。

同样，LP 构造的存在不自动推出：

- 展开后的行重和列重有界；
- 编码率为常数；
- 码距良好；
- 域上 HGP 的 Künneth 维数公式仍成立。

这些性质都需要对系数支持、种子族、模结构和所选 LP 子族添加条件。循环 LP 的具体块展开、反对合和长度计算见 [[Lifted product code]]。

S007 第 6 节展示的矩阵条目都是单项式，所以每个已展示条目可以安全地读成一条原型边携带的循环移位标签。但该节没有同时展示完整的第二因子，因此不能从那张矩阵单独推出完整 LP 的两因子数据、全部校验扇区或参数。它的提升间重排、提升内重排、门执行和定向转移是该中性原子案例的编译步骤，不是一般 LP 定义的一部分。

## 回收整条构造链

HGP 的结构现在可以按下面的因果顺序读取。

两张经典矩阵先被放进

$$
0\longrightarrow A_1\xrightarrow{A}A_0\longrightarrow0,
\qquad
0\longrightarrow B_1\xrightarrow{B}B_0\longrightarrow0.
$$

总次数把它们的张量积排成

$$
C_2=A_1\otimes B_1,
$$

$$
C_1=(A_1\otimes B_0)\oplus(A_0\otimes B_1),
$$

$$
C_0=A_0\otimes B_0.
$$

中间直和给出两类物理量子比特坐标。乘积边界在两个因子上分别作用，得到

$$
H_X
=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right],
$$

$$
H_Z
=
\left[
I_{n_A}\otimes B^{\mathsf T}
\;\middle|\;
A^{\mathsf T}\otimes I_{n_B}
\right].
$$

从 $C_2$ 到 $C_0$ 的两条路径都给出 $A\otimes B$；一般系数下它们符号相反，在 $\mathbb F_2$ 中则是两份相同贡献相加为零。因此

$$
H_XH_Z^{\mathsf T}=0.
$$

四个块中的恒等矩阵固定一个乘积坐标，另一张种子矩阵只改变另一个坐标，于是 Tanner 图分成 $A$ 方向和 $B$ 方向的种子图副本，并且没有同时改变两个坐标的基本边。

这套构造自动给出 CSS 对易。qLDPC、正编码率、平方根距离和 LP 的良好参数都不是自动结果；每一项都需要在相应位置加入额外假设。

## 来源与延伸

- [[Chain complex 与 cochain complex]]：链复形、边界和同调的基础解释。
- [[Cochain complex 的 tensor product]]：总次数、直和展开和乘积微分；其中采用升次数写法，本文使用其降次数链版本。
- [[Künneth 分解]]：域上的完整证明、HGP 逻辑支撑分解以及一般系数环的边界。
- [[Lifted product code]]：环值块、循环 lift、反对合、二进制展开和 balanced tensor product。
- [[S007 中 LP 码的分层执行]]：S007 的 outer-product 与 inner-lift 两层执行语义。
- [S007 全文译本](../../Translations/S007.full.zh-CN.md)：式 (1)、四类边、图 1(b)、第 3.1 节和第 6 节。
- [S007 来源登记](../../Papers/SOURCES.md#S007)：arXiv:2608.20164 v1 的版本与本地文件信息。
- Jean-Pierre Tillich and Gilles Zémor, [Quantum LDPC Codes With Positive Rate and Minimum Distance Proportional to the Square Root of the Blocklength](https://arxiv.org/abs/0903.0566)：原始 HGP 构造与标准参数基准。
