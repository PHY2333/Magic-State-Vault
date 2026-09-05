# Lifted product code

HGP 的两张量子校验矩阵由两份经典矩阵按四个块拼成。两类稳定子之所以交换，关键是沿两个因子先后作用时，两条路径给出相同的贡献，在二进制中相消。

现在把每个原型节点换成 $\ell$ 个副本。一条原来的连接不再只表示“连或不连”，还可以指定“第 $t$ 个副本连接对面的第 $t+s$ 个副本”。这些配对能否放进 HGP 的四个块，同时保留对易性？提升积码（lifted-product code，LP）的一个基本答案是：**保留 HGP 的外层乘积坐标，把矩阵条目换成作用在同一个内部坐标上的算子，并让两个因子的算子交叉对易。** 循环移位给出最容易计算的一种实现。[^PK20]

本文先用循环移位构造一个六比特码，再恢复一般的长方形输入矩阵。随后解释为什么这种构造只保留一份内部坐标，而不是先展开两个因子、再做普通 HGP 所得到的两份内部坐标。一般表示、非阿贝尔群和特定子族的参数定理放在选读部分。

## 循环 lift 的环表示

### 一条连接怎样变成副本之间的配对

令 $\ell$ 为正整数，把一个原型变量节点和一个原型校验节点分别复制为

$$
v_0,\ldots,v_{\ell-1},
\qquad
c_0,\ldots,c_{\ell-1}.
$$

固定列是变量、行是校验，并约定循环移位矩阵 $P$ 满足

$$
Pe_t=e_{t+1\bmod\ell},
\qquad
P^\ell=I_\ell.
$$

这里 $e_t$ 是只有第 $t$ 个坐标为 $1$ 的二进制列向量。因此，块 $P^s$ 的第 $t$ 列在第 $t+s$ 行有一个 $1$，所表示的 Tanner 邻接是

$$
v_t\longleftrightarrow c_{t+s\bmod\ell}.
$$

例如 $\ell=3$ 时，

$$
P=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}.
$$

块 $I_3+P$ 表示每个 $v_t$ 同时连接 $c_t$ 和 $c_{t+1}$：

$$
I_3+P=
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&1&1
\end{pmatrix}.
$$

因此，一个条目可以记录不止一种移位。这里的相加始终是模 $2$ 相加；同一连接重复出现两次会抵消，并不是在二进制 Tanner 图中保留两条重边。

### 用多项式记住这些循环矩阵

与其反复书写 $\ell\times\ell$ 的块，不如用 $x$ 代表一次移位，用 $x^s$ 代表 $s$ 次移位。因为 $P^\ell=I_\ell$，对应的符号运算应满足 $x^\ell=1$。这给出循环系数环

$$
R_\ell=\mathbb F_2[x]/\langle x^\ell-1\rangle.
$$

商环在这里的作用很具体：两个多项式相差 $x^\ell-1$ 的倍数时，把它们视为同一元素。每个元素都能唯一写成

$$
a(x)=\sum_{s=0}^{\ell-1}a_sx^s,
\qquad a_s\in\mathbb F_2.
$$

加法逐系数模 $2$ 计算；乘法先相乘，再用 $x^\ell=1$ 把指数按模 $\ell$ 折回。例如在 $R_3$ 中，$x^2x^2=x$。模去 $x^\ell-1$ 是为了表达周期条件，并不是为了保证得到一个域。当 $\ell>1$ 时，$x^\ell-1$ 有真因子 $x+1$，所得商环不是域，不能当作二元扩域 $\mathbb F_{2^\ell}$。

从环元素到二进制矩阵的映射为

$$
\Phi:R_\ell\longrightarrow
\operatorname{Mat}_{\ell\times\ell}(\mathbb F_2),
\qquad
\Phi(a)=\sum_{s=0}^{\ell-1}a_sP^s.
$$

它保留加法、乘法和单位元：

$$
\Phi(a+b)=\Phi(a)+\Phi(b),
\qquad
\Phi(ab)=\Phi(a)\Phi(b),
\qquad
\Phi(1)=I_\ell.
$$

因此 $x^s$ 不是一个额外的物理量，而是二进制块 $P^s$ 的紧凑记号。条目 $1+x^s$ 对应 $I_\ell+P^s$；一般多项式对应若干移位块的模 $2$ 和。把条目画成带标签的基图时，每个非零单项式给出一条带移位标签的连接；同一对原型端点可以有多个这样的标签。

### 为什么一个环坐标恰好对应 $\ell$ 个二进制坐标

还要区分“环元素的坐标向量”和“环元素所代表的线性算子”。定义

$$
\gamma(a)=(a_0,\ldots,a_{\ell-1})^{\mathsf T}
\in\mathbb F_2^\ell.
$$

$\gamma(a)$ 是一个列向量，而 $\Phi(a)$ 是一个方阵。二者满足

$$
\gamma(ar)=\Phi(a)\gamma(r).
$$

也就是说，$\Phi(a)$ 正是环内乘法 $r\mapsto ar$ 在基 $1,x,\ldots,x^{\ell-1}$ 下的矩阵。这种用环作用于自身得到的表示称为**正则表示**。

特别地，$\Phi(a)e_0=\gamma(a)$，所以 $\Phi(a)=0$ 只能发生在 $a=0$ 时；这个表示是忠实的，即不同环元素给出不同矩阵。更重要的是，$\gamma$ 本身给出二进制向量空间同构

$$
R_\ell\cong\mathbb F_2^\ell,
\qquad
R_\ell^n\cong\mathbb F_2^{\ell n}.
$$

以后所谓“展开一个环坐标”，使用的是这组确定的系数坐标。它不是从任意一个忠实块表示的尺寸推断出来的。[^PK20]

## 反对合与二进制转置

循环块的转置会把移位方向反过来，因为

$$
P^{\mathsf T}=P^{-1}.
$$

因此，环中对应二进制转置的操作应当把 $x^s$ 换成 $x^{-s}$。定义

$$
a^*(x)=a(x^{-1})
=\sum_{s=0}^{\ell-1}a_sx^{-s}
\quad\text{在 }R_\ell\text{ 中计算}.
$$

负指数仍按模 $\ell$ 化简。例如在 $R_3$ 中，

$$
x^*=x^2,
\qquad
(1+x)^*=1+x^2.
$$

这个操作满足 $(a^*)^*=a$ 和 $(ab)^*=b^*a^*$，称为反对合。在当前交换环中，反转乘法次序不会改变乘积，但这个写法能保留与转置相同的次序规则。

若 $M=(m_{ij})\in R_\ell^{r\times c}$，定义其共轭转置

$$
M^*=(m_{ji}^*)\in R_\ell^{c\times r}.
$$

它同时做两件事：交换外层行列，把每个条目的内部移位取逆。令 $\mathbb B(M)$ 表示逐条目用 $\Phi$ 展开的二进制块矩阵，则

$$
\mathbb B(M)\in\mathbb F_2^{\ell r\times\ell c},
\qquad
\boxed{\mathbb B(M^*)=\mathbb B(M)^{\mathsf T}}.
$$

只交换外层行列而不反转内部移位，一般不是整个二进制矩阵的转置。沿一条标签为 $x^s$ 的边，原来是列端 $t$ 连到行端 $t+s$；转置后以原行端为新的列端，配对方向就是 $t\mapsto t-s$。后面 $H_Z$ 中的星号正是由这一步产生的。[^PK20]

## 先构造一个六比特码

把 HGP 的两个输入都简化为 $1\times1$，但让它们的条目来自 $R_3$：

$$
A=[a],\qquad B=[b],
\qquad a=b=1+x.
$$

四个 HGP 块在这个尺寸下只剩下

$$
\widehat H_X=[a\mid b],
\qquad
\widehat H_Z=[b^*\mid a^*].
$$

帽子表示尚未展开的环值矩阵。两个列位置是两类物理坐标的原型；每个位置再展开成三个副本。按

$$
q^{(1)}_0,q^{(1)}_1,q^{(1)}_2
\;\mid\;
q^{(2)}_0,q^{(2)}_1,q^{(2)}_2
$$

排列物理量子比特，令 $D=I_3+P$，便得到

$$
H_X=\mathbb B(\widehat H_X)
=[D\mid D]
=
\left(
\begin{array}{ccc|ccc}
1&0&1&1&0&1\\
1&1&0&1&1&0\\
0&1&1&0&1&1
\end{array}
\right),
$$

$$
H_Z=\mathbb B(\widehat H_Z)
=[D^{\mathsf T}\mid D^{\mathsf T}]
=
\left(
\begin{array}{ccc|ccc}
1&1&0&1&1&0\\
0&1&1&0&1&1\\
1&0&1&1&0&1
\end{array}
\right).
$$

每张矩阵有三个校验行、六个物理列。例如第一条 $X$ 校验作用于 $q^{(1)}_0,q^{(1)}_2,q^{(2)}_0,q^{(2)}_2$，第一条 $Z$ 校验作用于 $q^{(1)}_0,q^{(1)}_1,q^{(2)}_0,q^{(2)}_1$。它们恰好重叠在两个量子比特上，因而交换。

全部异型校验的对易性则由一次块乘法验证：

$$
H_XH_Z^{\mathsf T}
=[D\mid D]
\begin{bmatrix}D\\D\end{bmatrix}
=D^2+D^2=0.
$$

这里的抵消不是因为 $D^2=0$，而是因为两条路径各贡献一次 $D^2$。

两张矩阵的前两行各自线性无关，第三行都是前两行之和，所以

$$
N=6,
\qquad
\operatorname{rank}H_X
=\operatorname{rank}H_Z=2,
\qquad
K=6-2-2=2.
$$

这个例子已经完成了从移位标签到实际二进制 CSS 码的全过程。选择 $a=b$ 只是为了让计算最短；一般构造并不要求两个因子相同。它真正使用的是：两个因子的系数作用在同一个三维副本空间上，并且彼此交换。

## 从小例恢复一般的四个块

### 外层坐标与内部坐标分别是什么

现在取

$$
A=(a_{ij})\in R_\ell^{m_A\times n_A},
\qquad
B=(b_{\alpha\beta})\in R_\ell^{m_B\times n_B}.
$$

$i,j$ 分别标记 $A$ 的行、列，$\alpha,\beta$ 分别标记 $B$ 的行、列。$R_\ell^n$ 是由 $n$ 个环元素组成的列向量集合，可以逐分量相加，并用环元素逐分量相乘；它称为秩 $n$ 的自由 $R_\ell$-模。其“自由”表示标准基展开唯一，不表示 $R_\ell$ 是域。

沿用 [[Hypergraph product code]] 的链方向，先在环上安排三个坐标模：

$$
\begin{aligned}
C_2&=R_\ell^{n_An_B},\\
C_1&=Q_1\oplus Q_2
=R_\ell^{n_Am_B}\oplus R_\ell^{m_An_B},\\
C_0&=R_\ell^{m_Am_B}.
\end{aligned}
$$

$C_2$ 标记 $Z$ 校验，$C_0$ 标记 $X$ 校验，$C_1$ 的两个直和分量标记两类物理坐标。展开后，物理量子比特分别记作

$$
q^{(1)}_{j,\alpha,t},
\qquad
q^{(2)}_{i,\beta,t},
\qquad t\in\mathbb Z_\ell.
$$

其中 $(j,\alpha)$ 或 $(i,\beta)$ 是**外层乘积坐标**，$t$ 是**内部 lift 坐标**。每个外层坐标只有一份 $t$，不是一对独立的 $t_A,t_B$。两类物理量子比特数相加给出

$$
\boxed{N=\ell(n_Am_B+m_An_B)}.
$$

同样，二进制 $X$ 校验行由 $(i,\alpha,t)$ 标记，$Z$ 校验行由 $(j,\beta,t)$ 标记。校验行数分别为 $\ell m_Am_B$ 和 $\ell n_An_B$，不一定等于独立校验数。

### 环矩阵中的 $\otimes$ 怎样读

以下四个块中的 $\otimes$ 是**环值矩阵的 Kronecker 积**：

$$
(M\otimes N)_{(i,\alpha),(j,\beta)}
=M_{ij}N_{\alpha\beta},
$$

右边的乘法在 $R_\ell$ 中进行。因此一个新条目仍是一个环元素，展开后仍是 $\ell\times\ell$ 的块，不是两个二进制块的 $\ell^2\times\ell^2$ Kronecker 积。

例如

$$
(A\otimes I_{m_B})_{(i,\alpha),(j,\alpha')}
=a_{ij}\delta_{\alpha,\alpha'}.
$$

$A$ 改变外层的 $A$ 坐标，恒等矩阵固定外层的 $B$ 坐标；$a_{ij}$ 再决定内部副本怎样连接。这里还没有用 $\otimes$ 来表示模上的张量积；那个操作会在解释“为什么只有一份内部坐标”时引入。

### 两个边界和四块校验矩阵

保持 HGP 的两个物理扇区顺序，定义

$$
\partial_1:C_1\longrightarrow C_0,
\qquad
\partial_1=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right],
$$

$$
\partial_2:C_2\longrightarrow C_1,
\qquad
\partial_2=
\begin{bmatrix}
I_{n_A}\otimes B\\
A\otimes I_{n_B}
\end{bmatrix}.
$$

$\partial_1$ 的第一块把 $Q_1$ 送到 $C_0$，尺寸为 $(m_Am_B)\times(n_Am_B)$；第二块把 $Q_2$ 送到 $C_0$，尺寸为 $(m_Am_B)\times(m_An_B)$。它们具有相同目标，所以横向拼接。

$\partial_2$ 的第一块从 $C_2$ 落入 $Q_1$，尺寸为 $(n_Am_B)\times(n_An_B)$；第二块落入 $Q_2$，尺寸为 $(m_An_B)\times(n_An_B)$。它们具有相同来源、不同输出分量，所以竖直堆叠。

为把 $Z$ 校验改排成“校验为行、物理量子比特为列”，必须对第二个边界作共轭转置。因此环值校验为

$$
\boxed{
\widehat H_X=
\left[
A\otimes I_{m_B}
\;\middle|\;
I_{m_A}\otimes B
\right]
},
$$

$$
\boxed{
\widehat H_Z=
\left[
I_{n_A}\otimes B^*
\;\middle|\;
A^*\otimes I_{n_B}
\right]
}.
$$

实际的二进制 CSS 校验矩阵是

$$
H_X=\mathbb B(\partial_1)
\in\mathbb F_2^{\ell m_Am_B\times N},
$$

$$
H_Z=\mathbb B(\partial_2^*)
=\mathbb B(\partial_2)^{\mathsf T}
\in\mathbb F_2^{\ell n_An_B\times N}.
$$

这就是循环环上的 LP 构造。它使用与 HGP 相同的四个外层块，但每个环条目都控制同一内部坐标上的移位。[^PK20]

### 为什么任意循环条目都保留 CSS 对易

固定 $C_2$ 中的外层坐标 $(j,\beta)$ 和 $C_0$ 中的外层坐标 $(i,\alpha)$。经过第一物理扇区的路径先作用 $b_{\alpha\beta}$，再作用 $a_{ij}$；经过第二物理扇区的路径次序相反。因此

$$
(\partial_1\partial_2)_{(i,\alpha),(j,\beta)}
=a_{ij}b_{\alpha\beta}+b_{\alpha\beta}a_{ij}=0.
$$

这里分开用了两件事：$R_\ell$ 交换，保证两条路径的乘积相同；特征为 $2$，保证相同贡献相加为零。对更一般的系数块，前一点只需所有 $A$ 方向块与所有 $B$ 方向块交叉对易，不要求同一因子内部的块两两交换。特别是，“每条边用了置换”本身并不能保证对易，因为一般置换矩阵未必交换。

逐项展开保留矩阵乘法，所以

$$
\begin{aligned}
H_XH_Z^{\mathsf T}
&=\mathbb B(\partial_1)\mathbb B(\partial_2)\\
&=\mathbb B(\partial_1\partial_2)\\
&=0.
\end{aligned}
$$

于是二进制链复形确实是

$$
C_2^{\mathrm{bin}}
\xrightarrow{\ H_Z^{\mathsf T}\ }
C_1^{\mathrm{bin}}
\xrightarrow{\ H_X\ }
C_0^{\mathrm{bin}},
$$

其中 $C_i^{\mathrm{bin}}$ 表示把 $C_i$ 的每个环坐标展开成二进制坐标。这里省略乘积边界中的负号只因为系数为 $\mathbb F_2$；不能在一般特征下照抄两个加号。

### 四类 Tanner 边如何读取

把二进制校验节点记为 $c^X_{i,\alpha,t}$ 和 $c^Z_{j,\beta,t}$。若 $a_{ij}$ 的约化多项式中含有 $x^s$，则对应两类连接：

$$
q^{(1)}_{j,\alpha,t}
\longleftrightarrow c^X_{i,\alpha,t+s},
\qquad
q^{(2)}_{i,\beta,t}
\longleftrightarrow c^Z_{j,\beta,t-s}.
$$

若 $b_{\alpha\beta}$ 中含有 $x^r$，则对应另外两类连接：

$$
q^{(2)}_{i,\beta,t}
\longleftrightarrow c^X_{i,\alpha,t+r},
\qquad
q^{(1)}_{j,\alpha,t}
\longleftrightarrow c^Z_{j,\beta,t-r}.
$$

所有内部下标都按模 $\ell$ 计算。$Z$ 校验中的负移位来自星号，不是另加的图形规则。外层仍然是一条边只改变一个因子坐标；内部则按该边的标签改变 $t$。这分别是 outer product 和 inner lift 所记录的数据。校验节点在此只是矩阵行标签，并未指定测量电路使用几个辅助量子比特。

## 为什么这不是“先展开，再做普通 HGP”

### 两种构造的长度已经不同

先展开两个输入时，得到

$$
A_{\mathrm{bin}}=\mathbb B(A)
\in\mathbb F_2^{\ell m_A\times\ell n_A},
\qquad
B_{\mathrm{bin}}=\mathbb B(B)
\in\mathbb F_2^{\ell m_B\times\ell n_B}.
$$

把这两张大矩阵直接作为普通 HGP 的输入，物理比特数是

$$
N_{\mathrm{ordinary}}
=(\ell n_A)(\ell m_B)+(\ell m_A)(\ell n_B)
=\ell^2(n_Am_B+m_An_B).
$$

而前面构造的 LP 是

$$
N_{\mathrm{LP}}=\ell(n_Am_B+m_An_B).
$$

对于六比特例子，先展开得到两张 $3\times3$ 的 $D$，再做 HGP 会得到 $18$ 个物理量子比特，而不是 $6$ 个。这不是列重排或另一种画图方式，因为坐标数本身不同。

普通乘积把两个因子的副本编号独立保留，形成 $(t_A,t_B)$。LP 则对两份内部坐标施加了一项识别。要说明这项识别，才需要引入模上的张量积。

### Balanced relation 把一份中间作用移到另一侧

暂记 $R=R_\ell$。把第一份自由模 $M=R^p$ 作为右 $R$-模，第二份 $W=R^q$ 作为左 $R$-模。在当前交换环中，右乘和左乘数值相同，但它们在下面关系中的位置仍然不同。

普通二进制张量积 $M\otimes_{\mathbb F_2}W$ 只要求对二进制标量双线性；它不会自动认为

$$
(ur)\otimes v
\quad\text{与}\quad
u\otimes(rv)
$$

相等。若要求两个因子共享同一个环作用，就应把这两个向量的差商掉。由此定义 balanced tensor product：

$$
M\otimes_RW
=
\frac{M\otimes_{\mathbb F_2}W}
{\operatorname{span}_{\mathbb F_2}
\{(ur)\otimes v-u\otimes(rv)\}}.
$$

分母取遍所有 $u\in M,v\in W,r\in R$ 所产生的差。下标 $R$ 表示额外施加了关系

$$
(ur)\otimes_Rv=u\otimes_R(rv).
$$

这不是从两个因子中随意删去一些坐标，而是规定：同一个中间系数放在左因子的右侧，或放在右因子的左侧，应当给出同一个张量类。

最关键的计算只需在一对环坐标上完成。乘法给出同构

$$
\mu:R\otimes_RR\longrightarrow R,
\qquad
u\otimes_Rv\longmapsto uv.
$$

它尊重 balanced relation，因为 $(ur)v=u(rv)$。逆映射是 $r\mapsto1\otimes_Rr$；反向复合为恒等映射，是因为

$$
u\otimes_Rv=1\otimes_Ruv.
$$

于是

$$
R^p\otimes_RR^q\cong R^{pq}.
$$

一对外层基方向仍然配成一个新方向，但其系数只剩一个 $R$ 元素。因此其二进制维数是 $\ell pq$，不是普通二进制张量积的 $\ell^2pq$。

这里的 $\otimes_R$ 是对模施加关系得到的新对象；前面四个块中的 $\otimes$ 是计算矩阵条目的规则。两者的联系是：**选择自由模的标准基，并用 $R\otimes_RR\cong R$ 合并系数后，balanced tensor 上的诱导映射就由那些环值 Kronecker 块表示。**

具体地，把两个二项自由模链复形写成

$$
\mathcal A:
R^{n_A}\xrightarrow{\ A\ }R^{m_A},
\qquad
\mathcal B:
R^{n_B}\xrightarrow{\ B\ }R^{m_B},
$$

其非零项位于次数 $1,0$。按总次数形成 $\mathcal A\otimes_R\mathcal B$，再用上述标准基同构合并环坐标，其三项恰好是前面的 $C_2,C_1,C_0$。边界为

$$
\partial(u\otimes_Rv)
=\partial_{\mathcal A}u\otimes_Rv
+u\otimes_R\partial_{\mathcal B}v.
$$

它能作用在张量类上，是因为 $A,B$ 对相应的 $R$-作用线性。例如

$$
\partial_{\mathcal A}(ur)\otimes_Rv
=(\partial_{\mathcal A}u)r\otimes_Rv
=\partial_{\mathcal A}u\otimes_R(rv),
$$

第二因子同样使用 $\partial_{\mathcal B}(rv)=r\partial_{\mathcal B}v$。因此被识别的代表元，其边界也被识别。上面的构造是链复形层面的商，不是先算普通 HGP 的逻辑空间，再随意商掉一些逻辑算符。一般定义和良定义性见 [[Balanced tensor product 与 coinvariant quotient]]；当前自由循环基作用下与 LP 矩阵的对应见 Breuckmann–Eberhardt 的 §IV-D3。[^BE20]

### 在副本编号上看见这个商

$R_\ell\otimes_{\mathbb F_2}R_\ell$ 的二进制基由

$$
x^{t_A}\otimes x^{t_B}
\quad\leftrightarrow\quad(t_A,t_B)
$$

标记。循环群 $\mathbb Z_\ell$ 在基对上的反对角作用是

$$
s\cdot(t_A,t_B)=(t_A-s,t_B+s).
$$

一边减、另一边加，正对应把同一次移位从一个因子移到另一个因子。该作用保持 $t_A+t_B$，每个轨道都恰有 $\ell$ 个基对，并有唯一一个形如 $(0,t)$ 的代表元。因此 $\ell^2$ 个基对变成 $\ell$ 个轨道类，剩余坐标是

$$
t=t_A+t_B\pmod\ell.
$$

例如 $\ell=3$ 时，$(0,0),(2,1),(1,2)$ 属于同一个轨道；它们在 $R_3\otimes_{R_3}R_3$ 中都对应系数 $1$。第一因子乘 $x^s$ 或第二因子乘 $x^s$，都会使这个剩余坐标增加 $s$，这正是两个因子共用同一个循环块空间的原因。

把“同一轨道的基向量之差”商掉，称为取该作用的 coinvariant quotient（余不变量商）。它是商空间，不是挑出不动向量的子空间。这里能精确按 $\ell$ 倍计数，是因为每个内部坐标都是完整的正则群坐标，反对角作用在这些基对上自由。**Balanced relation 本身不要求自由作用；对一般基作用，轨道可能有不同大小，不能直接把总数除以群阶。**[^BE20]

## 参数：对易以后还需要知道什么

### 逻辑比特数来自二进制秩，而不是环矩阵的行数

对于已经展开并满足 CSS 对易的矩阵，总有

$$
\boxed{
K=N-\operatorname{rank}_{\mathbb F_2}H_X
-\operatorname{rank}_{\mathbb F_2}H_Z
}.
$$

在本文的链方向下，逻辑 $Z$ 支撑类是

$$
\mathcal L_Z
=H_1(C^{\mathrm{bin}})
=\ker H_X/\operatorname{im}H_Z^{\mathsf T}.
$$

对偶上链复形的两支箭头是 $H_X^{\mathsf T}$ 和 $H_Z$，因而逻辑 $X$ 支撑类是

$$
\mathcal L_X
=\ker H_Z/\operatorname{im}H_X^{\mathsf T}.
$$

两个商空间的维数均为 $K$。它们不是先前物理扇区 $Q_1,Q_2$ 的二进制展开：物理扇区在取核、取商以前就存在，逻辑类则是在整个物理支撑空间中经过这两步之后得到的。

普通 HGP 可用域上的 Künneth 定理进一步化简 $K$。但 LP 的乘积是 $\otimes_{R_\ell}$，不是 $\otimes_{\mathbb F_2}$；两个自由链模的核与同调模也不必具有域上向量空间那样的分裂性质。因此不能把 HGP 的核维数乘积公式无条件搬过来。具体边界见 [[Künneth 分解#提升积码（lifted-product, LP）的安全接口]]。这不表示每个环上实例都难算；后面的 $B=[1+x]$ 就有可以直接证明的简化公式。

### qLDPC 要检查展开后的行重和列重

对约化多项式 $a=\sum_s a_sx^s$，令

$$
\operatorname{wt}_R(a)=\#\{s:a_s=1\}.
$$

因为不同的 $P^s$ 在任何固定行或列中的 $1$ 都落在不同位置，$\Phi(a)$ 的每一行、每一列的重量都等于 $\operatorname{wt}_R(a)$。定义输入的加权行重、列重上界

$$
r_A=\max_i\sum_j\operatorname{wt}_R(a_{ij}),
\qquad
c_A=\max_j\sum_i\operatorname{wt}_R(a_{ij}),
$$

并类似定义 $r_B,c_B$。四个块随即给出

$$
\begin{aligned}
H_X\text{ 的最大行重}&\le r_A+r_B,\\
H_Z\text{ 的最大行重}&\le c_A+c_B,\\
H_X\text{ 的最大列重}&\le\max(c_A,c_B),\\
H_Z\text{ 的最大列重}&\le\max(r_A,r_B).
\end{aligned}
$$

所以，让 $r_A,c_A,r_B,c_B$ 随码长增长仍统一有界，是得到 qLDPC 码族的充分条件。只有“每个条目是单项式”还不够：一行若含有越来越多的非零条目，展开后的校验重量仍会增长。[^PK20]

这些条件限制每条校验作用于多少比特、每个比特参与多少校验；它们不限制这些比特在二维平面上相距多远。qLDPC 稀疏性不等于二维几何局域性。

### 长度压缩不等于距离增长

当 $K>0$ 时，距离由最轻的非平凡逻辑支撑决定：

$$
\begin{aligned}
d_Z&=
\min_{z\in\ker H_X\setminus\operatorname{im}H_Z^{\mathsf T}}
\operatorname{wt}(z),\\
d_X&=
\min_{u\in\ker H_Z\setminus\operatorname{im}H_X^{\mathsf T}}
\operatorname{wt}(u).
\end{aligned}
$$

$$
d=\min(d_X,d_Z).
$$

前面的六比特码提供了一个可以完全算清的提醒。向量

$$
z=(e_0,e_0)
$$

重量为 $2$，而 $H_Xz=De_0+De_0=0$。任何 $Z$ 稳定子支撑都形如 $(Dw,Dw)$；$Dw$ 的坐标和为零，而 $e_0$ 的坐标和为 $1$，所以 $z$ 不是稳定子。另一方面，$H_X,H_Z$ 都没有零列，不存在重量 $1$ 的非平凡纯 $Z$ 或纯 $X$ 逻辑支撑。因此这个例子的完整参数是

$$
[\![6,2,2]\!].
$$

事实上，把同样的 $A=B=[1+x]$ 用于任意 $\ell\ge2$，上述论证仍给出重量 $2$ 的非平凡逻辑算符。这个码族虽然始终具有低重量校验、长度也从普通乘积的 $2\ell^2$ 变成 $2\ell$，距离却不随 $\ell$ 增长。

移位标签能够改变闭合条件：沿带方向的基图路径走一遍，回到原副本还要求累计移位为零；反向经过一条边时，应使用该标签的逆移位。但 Tanner 路径的闭合条件本身不是距离证明。要保证所有低重量闭合支撑都是稳定子，还必须控制两种逻辑商空间，通常需要对种子约束、图的扩张性和标签选择作额外设计。LP 提供这种设计的空间，而不是自动保留普通 HGP 的距离。

## 选读：$B=[1+x]$ 时为什么只需计算 $A(1)$

设 $A\in R_\ell^{m\times n}$，第二因子固定为 $1\times1$ 矩阵 $B=[1+x]$。四块公式化为

$$
\begin{aligned}
\widehat H_X&=[A\mid(1+x)I_m],\\
\widehat H_Z&=[(1+x^{-1})I_n\mid A^*],\\
N&=\ell(n+m).
\end{aligned}
$$

令 $A(1)$ 表示逐条目把 $x$ 代为 $1$ 得到的二进制 $m\times n$ 矩阵；每个条目就是原多项式的系数和模 $2$。这个操作在 $R_\ell$ 上良定义，因为 $x^\ell-1$ 在 $x=1$ 处为零。

此时有

$$
\boxed{
\begin{aligned}
K&=\dim_{\mathbb F_2}\ker A(1)
+\dim_{\mathbb F_2}\ker A(1)^{\mathsf T}\\
&=n+m-2\operatorname{rank}_{\mathbb F_2}A(1)
\end{aligned}
}.
$$

这是 Panteleev–Kalachev 的 Lemma 1 在 $b=1+x$ 下的特例；下面直接由二进制行依赖证明它，而不使用一般环上的 Künneth 分解。[^PK20]

记 $D_\ell=I_\ell+P$，$\mathbf1=(1,\ldots,1)^{\mathsf T}$。条件 $D_\ell y=0$ 等价于 $Py=y$，迫使一个循环中的所有坐标相同。因此

$$
\ker D_\ell=\ker D_\ell^{\mathsf T}
=\operatorname{span}_{\mathbb F_2}\{\mathbf1\}.
$$

所有移位都固定 $\mathbf1$，所以对任意 $a\in R_\ell$，

$$
\Phi(a)\mathbf1
=\Phi(a)^{\mathsf T}\mathbf1
=a(1)\mathbf1.
$$

先数 $X$ 校验行之间的依赖。$y\in\ker H_X^{\mathsf T}$ 必须满足

$$
\mathbb B(A)^{\mathsf T}y=0,
\qquad
(I_m\otimes D_\ell^{\mathsf T})y=0.
$$

第二个条件使每一块 $y_i$ 都等于某个二进制数 $c_i$ 乘 $\mathbf1$；第一个条件随即化成 $A(1)^{\mathsf T}c=0$。所以

$$
\dim\ker H_X^{\mathsf T}
=\dim\ker A(1)^{\mathsf T}.
$$

同理，$z\in\ker H_Z^{\mathsf T}$ 满足

$$
(I_n\otimes D_\ell)z=0,
\qquad
\mathbb B(A)z=0.
$$

这次每块 $z_j=d_j\mathbf1$，剩下的条件是 $A(1)d=0$，故

$$
\dim\ker H_Z^{\mathsf T}
=\dim\ker A(1).
$$

$H_X,H_Z$ 的总行数在这个特例中恰好等于 $N=\ell m+\ell n$。从行数减去行依赖数求秩，再代入 CSS 秩公式，便得到所宣称的 $K$。

这段证明对每个正整数 $\ell$ 都成立，不要求 $\ell$ 为奇数，也不要求 $A$ 满行秩。它只是在这个特定的 $B$ 下，把行依赖限制到常数副本方向；不能据此断言一般 $A,B$ 的逻辑数也由 $A(1),B(1)$ 决定。

## 选读：一般表示与非阿贝尔群的边界

### 忠实块表示不一定是自由模的正则展开

设 $R$ 是有限维含幺 $\mathbb F_2$-代数，给定含幺忠实表示

$$
\Psi:R\hookrightarrow\operatorname{Mat}_{s\times s}(\mathbb F_2).
$$

在两个输入的表示块交叉对易时，可以按同样的外层四块排列它们，并对第二个二进制边界直接取转置，得到长度

$$
N=s(n_Am_B+m_An_B)
$$

的 CSS 码。但此时每个外层坐标承载的是表示空间 $\mathbb F_2^s$，不一定是环 $R$ 自身。

例如 $R=\mathbb F_2$，表示 $a\mapsto aI_2$ 是忠实的，但表示空间是二维，$\dim_{\mathbb F_2}R$ 只有 $1$。因此不能仅由“忠实”就宣称 $R^n\cong\mathbb F_2^{sn}$。前文能够这样数维数，是因为明确使用了作用在 $R_\ell$ 自身上的正则表示。[^PK21]

此外，要继续把二进制转置写成环内的星号，还需要指定一个反对合并验证

$$
\Psi(a^*)=\Psi(a)^{\mathsf T}.
$$

没有这项相容性时，二进制边界仍然可以直接转置，但不能擅自假定转置块对应某个预先给定的环内 $a^*$。

### 从循环群到一般群

循环环也可以写成 $R_\ell\cong\mathbb F_2[\mathbb Z_\ell]$。一般有限群 $G$ 的群代数

$$
\mathbb F_2[G]
=\left\{\sum_{g\in G}a_g g:a_g\in\mathbb F_2\right\}
$$

以群元素为二进制基，乘法按群乘法分配展开。它的二进制维数为 $|G|$。当 $G$ 阿贝尔时，环仍然交换，前述构造可以用群元素的正则置换矩阵代替循环移位矩阵。

对一份右正则群坐标和一份左正则群坐标，反对角作用为

$$
h\cdot(g_1,g_2)=(g_1h^{-1},hg_2).
$$

它保持乘积 $g_1g_2$，每个轨道大小为 $|G|$。因此，在各次数都由自由正则群坐标组成、边界与相应群作用相容的情形，普通二进制乘积中的两份群坐标合并成一份，得到 $|G|^2$ 与 $|G|$ 的精确计数差别。自由基作用与 LP 的对应不需要群阶为奇数；奇数阶条件会出现在另外一些同调或平均化结论中，不是这个轨道计数的条件。[^BE20][^PK21]

### 非阿贝尔时必须改变算子的作用侧

若 $G$ 非阿贝尔，令 $R=\mathbb F_2[G]$。环元素未必交换，不能把两份输入都按同一种左乘展开后，继续使用 $ab=ba$ 的证明。要保持前述自由坐标构造，取第一因子为自由右 $R$-模链复形，第二因子为自由左 $R$-模链复形，且边界分别满足

$$
\partial_{\mathcal A}(ur)=(\partial_{\mathcal A}u)r,
\qquad
\partial_{\mathcal B}(rv)=r\partial_{\mathcal B}v.
$$

这些条件使 $\mathcal A\otimes_R\mathcal B$ 的边界良定义。结果首先是二进制链复形；用来形成 balanced relation 的这两侧作用，不自动成为结果上的 $R$-作用。若还要保留外侧的 $R$-作用，需要另外给出与边界相容的双模结构。[^PK21]

把第一因子的系数写成列坐标时，右 $R$-线性的单坐标映射是左乘

$$
\lambda_a(u)=au,
\qquad
\lambda_a(ur)=\lambda_a(u)r.
$$

第二因子中，左 $R$-线性的单坐标映射是右乘

$$
\rho_b(v)=vb,
\qquad
\rho_b(rv)=r\rho_b(v).
$$

因此，按“第一因子右模、第二因子左模”的这个坐标约定，在合并后的一个环坐标上，$A$ 方向使用左乘块，$B$ 方向使用右乘块。尤其第二个因子的映射是 $v_\beta\mapsto v_\beta b_{\alpha\beta}$，不能把它误读为同一套普通左乘列矩阵规则。

两条路径现在仍然相等，但理由是结合律：

$$
\lambda_a\rho_b(u)=a(ub)=(au)b=\rho_b\lambda_a(u).
$$

按四个外层块排列这些二进制算子，再对第二个边界取二进制转置，就得到 CSS 对易。群基下还有

$$
\lambda_g^{\mathsf T}=\lambda_{g^{-1}},
\qquad
\rho_g^{\mathsf T}=\rho_{g^{-1}},
$$

所以逆元继续控制转置。重点不是多加一个星号，而是先保证共享坐标上的两族算子交叉对易，并与选定的模侧别相容。不同文献可以交换两族块的角色；模的右线性与“系数在右边相乘”不是同一句话。[^PK21]

## 选读：哪些参数和译码结论属于特定子族

专门设计的循环 LP 能够具有近线性距离，但不是任取 $A,B$ 都会如此。Panteleev–Kalachev 的近线性距离构造使用专门设计的扩张图种子与重复码因子，得到一族

$$
K=\Theta(\log N),
\qquad
d=\Theta\!\left(\frac{N}{\log N}\right)
$$

的 qLDPC 码。这里 $\Theta$ 表示上下界只差与 $N$ 无关的常数因子；这族码的编码率仍趋于零。该结论是论文 Theorem 1 中构造出的子族的性质，不是 $B=[1+x]$ 本身的性质。[^PK20]

Panteleev–Kalachev 后来利用非阿贝尔群上的特定扩张图和满足所需乘积扩张性质的局部码，构造了同时具有 $K=\Theta(N)$、$d=\Theta(N)$ 的渐近良好 qLDPC 族。Theorem 2 是这种特定构造的存在性和参数结论，不表示一般群代数 LP、一般稀疏输入或随机移位标签都具有线性距离。[^PK21]

译码还需要另一层论证。BP-OSD 把信念传播与有序统计后处理结合起来，Panteleev–Kalachev 对若干有限长度码给出了去极化信道下的数值表现；这种实验结果不等于对所有 LP 的最坏情形纠错保证。[^PK19] Leverrier–Zémor 则对其满足扩张性与局部码条件的量子 Tanner 码及对应 LP 子族，证明了纠正线性重量对抗性错误的线性时间译码结果；适用范围是那些经过分析的子族。[^LZ22]

对前述近线性距离的循环子族，Golowich–Guruswami 给出了多项式时间随机译码：在其构造与假设下，可高概率纠正 $\Theta(N/\log N)$ 个对抗性错误。其 Theorem 32 明确取 $\ell$ 为 $2$ 的幂，并要求经典种子复形及其转置对偶复形具有所需的含噪综合征译码能力；这不是所有 $\ell$、所有 $A$ 的统一结论。经典子程序能够处理综合征噪声，也不等于最终量子码已经获得含噪测量下的单次纠错保证。[^GG24]

因此，低重量校验、距离下界、有效译码和线路级容错性能是四项不同的结论；不能从 LP 的四块公式一次性推出它们。

## 从代数定义到 S007 的执行实例

S007 的 arXiv v1 第 6 节、式 (2) 展示了一张 $3\times7$ 单项式种子矩阵。按本文约定，已确定连接上的条目 $x^s$ 可以读成内部副本的循环配对；外层乘积坐标和内部移位坐标仍是两层不同的数据。但该节没有同时展示完整的第二因子，不能仅由这张矩阵补出完整的两个输入、全部物理／校验扇区，或推导完整码参数。来源见 [S007 全文译本第 6 节](../../Translations/S007.full.zh-CN.md)。

具体的提升间重排、提升内重排与门执行见 [[S007 中 LP 码的分层执行]]。那篇笔记使用本文的循环移位与转置约定，把已经给定的校验连接交给硬件执行；硬件布局和调度不参与这里的 LP 定义。

## 来源

[^PK20]: Pavel Panteleev and Gleb Kalachev, [*Quantum LDPC Codes with Almost Linear Minimum Distance*, arXiv:2012.04068v2](https://arxiv.org/abs/2012.04068v2)。§III 的群代数正则表示与二进制展开；§III-D，式 (12)–(13) 的 LP 四块及交叉对易条件；§III-F，Lemma 1 与 Remark 3 的特殊维数公式；Theorem 1 及 §V 的近线性距离构造。

[^BE20]: Nikolas P. Breuckmann and Jens N. Eberhardt, [*Balanced Product Quantum Codes*, arXiv:2012.09271v3](https://arxiv.org/abs/2012.09271v3)。§IV-A、§IV-C 的 balanced relation 与群商；§IV-D1 的乘积复形；§IV-D3 的自由阿贝尔基作用、正则表示和 LP 的对应。一般左右模与 coinvariant 的局部解释另见 [[Balanced tensor product 与 coinvariant quotient]]。

[^PK21]: Pavel Panteleev and Gleb Kalachev, [*Asymptotically Good Quantum and Locally Testable Classical LDPC Codes*, arXiv:2111.03654v2](https://arxiv.org/abs/2111.03654v2)。§1.2 的自由右／左模定义；Appendix B 的二进制块交叉对易与左右正则算子构造；Theorem 2 的渐近良好量子码族。本文非阿贝尔段按第一因子右模、第二因子左模写出系数列作用；该文 Appendix B 另采用 $A$ 方向右乘、$B$ 方向左乘的直接块约定，两种分配各自都由结合律保证交叉对易。

[^PK19]: Pavel Panteleev and Gleb Kalachev, [*Degenerate Quantum LDPC Codes With Good Finite Length Performance*, arXiv:1904.02703v3](https://arxiv.org/abs/1904.02703v3)。§3，特别是 §3.3 的 BP-OSD 算法，以及文中的有限长度数值比较；其结果不构成任意 LP 的通用译码定理。

[^LZ22]: Anthony Leverrier and Gilles Zémor, [*Efficient decoding up to a constant fraction of the code length for asymptotically good quantum codes*, arXiv:2206.07571v2](https://arxiv.org/abs/2206.07571v2)。Theorem 2 及 §7，特别是 §7.3 的 LP 译码转化；需要该文的码构造和局部码条件。

[^GG24]: Louis Golowich and Venkatesan Guruswami, [*Decoding Quasi-Cyclic Quantum LDPC Codes*, arXiv:2411.04464v1](https://arxiv.org/abs/2411.04464v1)。Theorem 1、§6.1 的 Theorem 32 与 Example 33 给出特定循环 LP 的随机译码保证；§1.4 区分经典含噪综合征子程序与量子综合征噪声问题。
