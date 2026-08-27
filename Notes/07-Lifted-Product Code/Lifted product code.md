Lifted-product code（LP 码）保留 [[Hypergraph product code]] 的三项乘积复形、两个物理比特扇区和 HGP 型校验矩阵排列，但把二进制矩阵条目提升为带副本置换信息的环元素。构造所需的直接前置是 HGP blocks 与 [[Balanced tensor product 与 coinvariant quotient]] 中的 balanced relation；[[Künneth 分解]] 只在分析逻辑空间、维数公式和一般系数边界时使用，不是定义 cyclic lift 或写出 LP 校验矩阵的条件。

### 从 HGP 边到 lift 标签

在 HGP 中，经典校验矩阵的一个非零条目只表示一个变量节点和一个校验节点之间有边。LP 改用

$$
A\in R^{m_A\times n_A},
\qquad
B\in R^{m_B\times n_B},
$$

其中 $R$ 是有限维 $\mathbb F_2$-代数。固定一个忠实的二进制块表示

$$
\Phi:R\longrightarrow
\operatorname{Mat}_{\ell\times\ell}(\mathbb F_2).
$$

一个 $R$-坐标展开成 $\ell$ 个二进制坐标。若原型节点记作 $u$，它展开后的副本写成

$$
u_0,u_1,\ldots,u_{\ell-1};
$$

这 $\ell$ 个副本合称节点 $u$ 的一个 lift，$\ell$ 称为 lift size。环值条目 $a_{ij}\in R$ 仍表示原型列 $j$ 与原型行 $i$ 之间的一条 base edge，同时用二进制块 $\Phi(a_{ij})$ 指定两端副本怎样配对。

HGP 的乘积指标决定哪一组 data/check lifts 之间允许有边；环值条目再决定每组 lift 内哪些副本相连。前者是 outer product 坐标，后者是 inner lift 坐标。量子比特在硬件中的位置和移动方式不属于 LP 码的定义。

### 循环 lift 的环表示

先看最常见的循环 lift。令

$$
R_\ell=\mathbb F_2[x]/(x^\ell-1),
$$

并给 $\mathbb F_2^\ell$ 的基向量编号 $e_0,\ldots,e_{\ell-1}$。固定循环移位矩阵 $P$ 满足

$$
Pe_t=e_{t+1\bmod\ell}.
$$

显式地，

$$
P=
\begin{bmatrix}
0&0&\cdots&0&1\\
1&0&\cdots&0&0\\
0&1&\ddots&0&0\\
\vdots&&\ddots&&\vdots\\
0&0&\cdots&1&0
\end{bmatrix}.
$$

定义系数的二进制表示

$$
\Phi(x^s)=P^s,
$$

并按 $\mathbb F_2$ 线性延拓。例如

$$
\Phi(1+x^s)=I+P^s.
$$

因为 $P^\ell=I$，代入 $x\mapsto P$ 保持商关系 $x^\ell=1$，所以 $\Phi$ 是代数同态：

$$
\Phi(rs)=\Phi(r)\Phi(s).
$$

它正是循环群自然基上的正则表示（regular representation），因而相应的二进制块展开也保持矩阵乘法。

在图上，一个原型变量 $v$ 和一个原型校验 $c$ 分别复制成 $v_0,\ldots,v_{\ell-1}$ 与 $c_0,\ldots,c_{\ell-1}$；环值边的单项式标签决定这些副本如何配对。

若矩阵列对应变量 $v_t$、行对应校验 $c_t$，那么 $(P^s)_{t+s,t}=1$。因此标签 $x^s$ 表示

$$
v_t\longleftrightarrow c_{t+s},
$$

等价地，

$$
c_t\longleftrightarrow v_{t-s}.
$$

这个符号方向会在转置时变成逆移位，不能任意互换。若 $s\not\equiv0\pmod\ell$，$1+x^s$ 表示不移位和移位 $s$ 的两组边；若 $s\equiv0$，两项在 $\mathbb F_2$ 中抵消。

#### $R_3$ 中的 $1+x^2$

取 $\ell=3$。上述约定给出

$$
P=
\begin{bmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{bmatrix},
\qquad
\Phi(1+x^2)=I+P^2=
\begin{bmatrix}
1&1&0\\
0&1&1\\
1&0&1
\end{bmatrix}.
$$

每个变量 $v_t$ 连接 $c_t$ 与 $c_{t+2}$；等价地，每个校验 $c_t$ 连接 $v_t$ 与 $v_{t+1}$。原型 Tanner 图（protograph）中的一条环值边因而展开成三个不移位连接和三个移位连接。

### 环值矩阵与二进制展开

若

$$
A=(a_{ij})\in R_\ell^{m\times n},
$$

就把每个 $a_{ij}$ 替换为 $\Phi(a_{ij})$，得到 $\ell m\times\ell n$ 的二进制块矩阵，记为 $\mathbb B(A)$。所以 $R_\ell$-矩阵不是把大矩阵的信息删掉，而是用一个原型图指标和一个循环群标签压缩记录整个 lift。

若

$$
a_{ij}=x^{s_1}+\cdots+x^{s_w},
$$

那么

$$
\Phi(a_{ij})=P^{s_1}+\cdots+P^{s_w}.
$$

每个单项式给出同一条 base edge 上的一组 cyclic-shift connections；多项式的和把这些连接按 $\mathbb F_2$ 相加。原型行列指标 $(i,j)$ 与副本指标 $t$ 因而分开保存：前者选择 base edge，后者由各个指数 $s_a$ 平移。

### 反对合与二进制转置

循环移位满足

$$
(P^s)^T=P^{-s}.
$$

因此在 $R_\ell$ 上定义

$$
r^*(x)=r(x^{-1}),
\qquad
(x^s)^*=x^{-s}=x^{\ell-s},
$$

这个映射满足

$$
(r^*)^*=r,
\qquad
(rs)^*=s^*r^*.
$$

第二条等式说明它是反对合；在交换环 $R_\ell$ 中，次序反转不会改变乘积。

它与二进制转置的相容性为

$$
\Phi(r^*)=\Phi(r)^T.
$$

对环值矩阵 $M=(m_{ij})$，共轭转置是

$$
M^*=(m_{ji}^*),
$$

从而

$$
\boxed{
\mathbb B(M^*)=\mathbb B(M)^T
}.
$$

有限阿贝尔群代数 $R=\mathbb F_2[G]$ 完全类似：在群基上取

$$
\left(\sum_{g\in G}\alpha_g g\right)^*
=
\sum_{g\in G}\alpha_g g^{-1}.
$$

以下矩阵公式采用最常用的交换情形：$R$ 是特征 $2$ 的有限维 $\mathbb F_2$-代数，并具有一个忠实、保持乘法且与转置相容的 $\ell\times\ell$ 二进制块表示。循环环和有限阿贝尔群代数都满足这些条件。

### HGP 型 LP blocks

取环值矩阵

$$
A\in R^{m_A\times n_A},
\qquad
B\in R^{m_B\times n_B},
$$

并把它们看成自由 $R$-模之间的映射：

$$
\mathcal A:\quad
R^{n_A}\xrightarrow{A}R^{m_A},
\qquad
\mathcal B:\quad
R^{n_B}\xrightarrow{B}R^{m_B}.
$$

LP 在这里取的是 $\mathcal A\otimes_R\mathcal B$，不是先把 $A,B$ 展开后再在 $\mathbb F_2$ 上取 ordinary tensor product。其三项链复形为

$$
C_2=R^{n_An_B}
\xrightarrow{\partial_2}
C_1=R^{n_Am_B}\oplus R^{m_An_B}
\xrightarrow{\partial_1}
C_0=R^{m_Am_B},
$$

其中

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

这里块公式中的 $\otimes$ 是环值矩阵的 Kronecker 积；背后的模张量积是 $\otimes_R$。因为 $R$ 交换，$A$ 的系数与 $B$ 的系数逐项对易，所以

$$
\partial_1\partial_2
=A\otimes B+A\otimes B
=0.
$$

沿用 [[Hypergraph product code]] 的 chain convention，$C_1$ 是物理量子比特模，并在环值层面取

$$
\widehat H_X=\partial_1,
\qquad
\widehat H_Z=\partial_2^*.
$$

也就是

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

真正的二进制 CSS 校验矩阵是

$$
H_X=\mathbb B(\widehat H_X),
\qquad
H_Z=\mathbb B(\widehat H_Z).
$$

这个二进制码记为

$$
\mathrm{LP}(A,B).
$$

### 二进制 CSS 对易

相对于 HGP，只需检查三个新条件：$A$ 与 $B$ 的系数交叉对易；$*$ 对应二进制转置；$\mathbb B$ 保持矩阵乘法。于是

$$
\widehat H_Z^*=\partial_2
=
\begin{bmatrix}
I_{n_A}\otimes B\\
A\otimes I_{n_B}
\end{bmatrix},
$$

并且

$$
\widehat H_X\widehat H_Z^*
=
(A\otimes I)(I\otimes B)
+
(I\otimes B)(A\otimes I)
=0.
$$

展开后，

$$
\begin{aligned}
H_XH_Z^T
&=\mathbb B(\widehat H_X)\,
  \mathbb B(\widehat H_Z)^T\\
&=\mathbb B(\widehat H_X)\,
  \mathbb B(\widehat H_Z^*)\\
&=\mathbb B(\widehat H_X\widehat H_Z^*)\\
&=0.
\end{aligned}
$$

转置后同样得到本库 cochain convention 使用的 $H_ZH_X^T=0$。按 [[Hypergraph product code#从两张经典校验矩阵开始]] 固定的 convention，展开后的 chain homology 与对偶 cochain cohomology 分别给出 logical $Z$ 与 logical $X$ classes。LP 没有改变这套对应，只把 product complex 的系数从 $\mathbb F_2$ 提升到 $R$。

### Outer product 与 inner lift

先给 $A$ 的行、列指标记作 $i,j$，给 $B$ 的行、列指标记作 $\alpha,\beta$。环值乘积复形中的四类坐标仍由 HGP 的 total degree 决定：

| 环值链群 | outer product 坐标 | 二进制展开后的集合 |
|---|---|---|
| $C_1$ 第一扇区 | $(j,\alpha)\in[n_A]\times[m_B]$ | $\{q^{(1)}_{j,\alpha,t}:t\in\mathbb Z_\ell\}$ |
| $C_1$ 第二扇区 | $(i,\beta)\in[m_A]\times[n_B]$ | $\{q^{(2)}_{i,\beta,t}:t\in\mathbb Z_\ell\}$ |
| $C_0$ | $(i,\alpha)\in[m_A]\times[m_B]$ | $\{x_{i,\alpha,t}:t\in\mathbb Z_\ell\}$ |
| $C_2$ | $(j,\beta)\in[n_A]\times[n_B]$ | $\{z_{j,\beta,t}:t\in\mathbb Z_\ell\}$ |

固定一个 outer product 坐标并让 $t$ 遍历 $\mathbb Z_\ell$，就得到一个 data lift、$X$-check lift 或 $Z$-check lift。HGP blocks 决定哪些 outer product 坐标之间可能相连；$A$、$B$ 中的环值系数决定相连 lifts 内部的副本配对。

在循环情形中，某个 block coefficient 为 $x^k$ 时，二进制块是 $P^k$。若该 block 的列副本编号为 $t$，则非零元落在行副本 $t+k\bmod\ell$。所以同一个 LP 校验边同时包含两份数据：

$$
\text{outer product 的 base edge}
\quad+\quad
\text{inner lift 的 shift label }k.
$$

这一区分只描述校验矩阵中的节点与边。把一个 lift 放到哪一行、如何移动到相互作用位点，以及何时在两个乘积方向之间切换，属于具体硬件上的执行方案。

### 二进制长度、行数、秩与 LDPC 条件

记

$$
Q=n_Am_B+m_An_B.
$$

环值矩阵的尺寸是

$$
\widehat H_X\in R^{m_Am_B\times Q},
\qquad
\widehat H_Z\in R^{n_An_B\times Q}.
$$

每个 $R$-坐标展开成 $\ell$ 个二进制坐标，故

$$
H_X\in
\mathbb F_2^{\ell m_Am_B\times\ell Q},
\qquad
H_Z\in
\mathbb F_2^{\ell n_An_B\times\ell Q}.
$$

因此物理比特数为

$$
\boxed{
N=\ell(n_Am_B+m_An_B)
}.
$$

写出的 $X$-校验行恰有 $\ell m_Am_B$ 条，$Z$-校验行恰有 $\ell n_An_B$ 条。独立生成元数分别是二进制秩，可能小于行数，但不必然存在大量冗余。一般实例的逻辑比特数应按

$$
\boxed{
K=N-\operatorname{rank}_{\mathbb F_2}H_X
-\operatorname{rank}_{\mathbb F_2}H_Z
}
$$

计算；一般 $R,A,B$ 没有一个像域上 HGP 那样统一的简洁维数公式。[[Künneth 分解#PID 与一般系数环]] 说明了这里与域上 HGP 的差别：一般环上的 product homology 可能涉及高阶 $\operatorname{Tor}$、谱序列微分与 extension，不能无条件套用域上的两个扇区公式。

LP 构造本身只保证 CSS 对易，不自动保证 LDPC。对准循环（quasi-cyclic, QC）或群代数输入，一个简单的充分条件是：

- 每个环元素只含有统一有界数目的群基元素；
- $A,B$ 基矩阵的每行、每列中，所有系数的群基支持大小之和统一有界。

此时 $H_X,H_Z$ 的二进制行重和列重也统一有界，才得到 qLDPC 码族。稠密的 $A$、$B$ 或稠密环元素仍可定义 LP 码，但展开后未必低密度。

### 与 S007 第 6 节的连接

[S007 全文译本](../../Translations/S007.full.zh-CN.md) 第 6 节的式 (2) 展示了一个 $3\times 7$ 单项式 seed base matrix $A$。按本节约定，其中每个 $x^k$ 只能直接读成一条 base edge 携带的 cyclic-shift label：它把该边的列副本 $t$ 连到行副本 $t+k\bmod\ell$。S007 没有在该处展示完整的第二因子，因此不能只凭这个矩阵重建完整 LP 两因子数据，也不能据此给出完整的 data、$X$-check、$Z$-check sector 映射或推导实例参数。

图 12 与相邻正文进一步说明了这个具体实例怎样把 outer product 层和 inner lift 层映射到硬件执行；详见 [[S007 中 LP 码的分层执行]]。其中 data lift、$X$-check lift、$Z$-check lift 的角色只按图 12 和 S007 正文明示的范围解释，不反推未展示的码构造数据。

### 自由反对角商与长度压缩

现在专门取

$$
R=\mathbb F_2[G],
\qquad
|G|=\ell,
$$

并假设两个 lifted complexes 的选定基都带有相容、自由的正则 $G$-作用。若先把 $A,B$ 展开成二进制矩阵，再对两个展开后的经典码做 ordinary HGP，每个乘积基向量同时带两个独立群坐标 $(g_1,g_2)\in G^2$，长度是

$$
N_{\mathrm{expanded\ HGP}}
=
\ell^2Q.
$$

在 $R$ 上取 balanced tensor product 时，使用的是

$$
(m r)\otimes n
\sim
m\otimes(r n).
$$

对群基，这与反对角作用

$$
h\cdot(g_1,g_2)
=
(g_1h^{-1},hg_2)
$$

的 coinvariant quotient 相同。每条轨道中的有序乘积 $g_1g_2$ 不变；自由正则作用使每条轨道恰有 $\ell$ 个元素，所以 $G^2$ 坐标被压成一个 $G$ 坐标：

$$
\ell^2Q
\longrightarrow
\ell Q.
$$

这正好给出

$$
N_{\mathrm{LP}}=\ell Q.
$$

因此在这一精确适用范围内，

$$
\boxed{
\mathrm{LP}
\cong
\frac{\text{HGP complex of the two lifted complexes}}
{\text{free anti-diagonal }G\text{-action}}
}.
$$

商发生在链复形本身，之后才在新复形中取 homology；它不是对最终码空间随意做一个向量空间商。自由作用也只是这里得到精确 $\ell$ 压缩因子的条件，不是 balanced tensor product 定义的一部分。允许非自由作用时，balanced-product 构造比这一类 LP 表述更一般。

### 最常见的 QC 特例：$B=[1+x]$

令

$$
R_\ell=\mathbb F_2[x]/(x^\ell-1),
\qquad
A\in R_\ell^{m\times n},
$$

并取 $1\times1$ 环值矩阵

$$
B=[b],
\qquad
b=1+x.
$$

此时

$$
\widehat H_X=
\left[
A
\;\middle|\;
(1+x)I_m
\right],
$$

$$
\widehat H_Z=
\left[
(1+x^{-1})I_n
\;\middle|\;
A^*
\right],
$$

而

$$
N=\ell(n+m).
$$

$1+x$ 展开成 $I+P$，是长度 $\ell$ 的循环重复码校验算子：它把相邻的提升层连接起来，kernel 是由全 $1$ 向量张成的一维子空间。$A$ 则决定不同原型变量与校验之间携带哪些移位。

一般 LP 的 $K$ 没有统一闭式，但这个特例有。把 $A$ 的每个多项式系数在 $x=1$ 处求值，得到二进制矩阵 $A(1)$。由于 $1+x$ 是 $x^\ell-1$ 的一次不可约因子，原始 LP 论文的特殊维数公式化为

$$
\boxed{
K=\dim_{\mathbb F_2}\ker A(1)
+\dim_{\mathbb F_2}\ker\!\bigl(A(1)^T\bigr)
}.
$$

这里的 $A(1)^T$ 与先转置再求值的 $A^T(1)$ 相同。公式只属于 $B=[1+x]$ 这一特殊情形，不能替代一般 LP 的二进制秩计算。

### Lift 与距离标度

在标准等尺度 HGP 中，一个逻辑算符可以由某个经典码字乘上另一个因子的短代表元得到。它的支撑可留在一个乘积切片内；当总长度约为两个因子尺寸的乘积时，这自然产生 $d=\Theta(\sqrt N)$ 的基准。

Lift 后，沿 Tanner 图路径经过的群标签会累积。对循环 lift，一条基图环只有在所有移位之和为 $0\pmod\ell$ 时才在原提升层闭合；一般群 lift 则要求有序标签乘积回到单位元。因此基图中看似局部的支撑不一定能停留在少数提升层。

Balanced quotient 同时把两个群坐标压成一个，令物理长度少一个 $|G|$ 因子。若所选 lift 还具有足够的扩张性，局部 syndrome 约束会迫使非平凡 cycle 的支撑穿过许多基图顶点和提升层。于是码长被压缩，逻辑支撑却不会按同一因子缩短。

这只是证明思路的图像，不是任意 LP 的距离定理。真正的下界依赖

$$
\text{基图扩张性}
+\text{局部经典码}
+\text{lift 标签}
+\text{群作用}
$$

的共同条件。随意选择 $A,B$ 完全可能得到常数重量逻辑算符。

Panteleev–Kalachev 对精心选择、具有扩张性的稀疏准循环矩阵 $A$ 与 $b=1+x$ 证明了

$$
K=\Theta(\log N),
\qquad
d=\Theta\!\left(\frac{N}{\log N}\right).
$$

这把当时常见的 HGP 平方根距离格局推进到近线性距离。该结论属于论文构造出的特定码族，不是 “QC” 或 “LP” 三个字自动蕴含的性质。

### 非阿贝尔情形的左右模

若

$$
R=\mathbb F_2[G]
$$

且 $G$ 非阿贝尔，$A$ 与 $B$ 的系数一般不再逐项交换。此时不能把上面的交换环矩阵公式原样展开，并指望反对合单独保证 CSS 对易。

抽象层面的侧别是：第一条链复形由自由右 $R$-模组成，第二条由自由左 $R$-模组成，balanced relation 为

$$
(ua)\otimes v
=
u\otimes(av).
$$

二进制层面不沿用前面交换环中统一的列向量环矩阵记法，而直接采用原论文 Appendix B 的块替换：

$$
\widehat A=(\rho_{a_{ij}}),
\qquad
\rho_a(u)=ua,
$$

$$
\widehat B=(\lambda_{b_{st}}),
\qquad
\lambda_b(u)=bu.
$$

这里 $\rho_a$、$\lambda_b$ 只是 $\mathbb F_2$-线性的二进制块；不能把 $\rho_a$ 误称为右模微分的统一列向量表示。结合律给出

$$
\rho_a\lambda_b(u)
=(bu)a
=b(ua)
=\lambda_b\rho_a(u),
$$

这才替代交换环中的“系数相互对易”。群反演 $g\mapsto g^{-1}$ 仍负责转置和对偶，但它不能替代左右模的侧别条件。

在这一更一般的 lifted-product/Tanner-code 构造中，再加入论文要求的局部乘积扩张和全局扩张条件，Panteleev–Kalachev 得到显式 qLDPC 码族

$$
K=\Theta(N),
\qquad
d=\Theta(N),
$$

即常数编码率与常数相对距离。这正是渐近良好 qLDPC 码族所要求的参数，并由此解决了 qLDPC 猜想。好参数来自这些额外性质，而不是来自“群非交换”本身。

### 与相邻构造的关系

| 系数或群作用的选择 | 得到的构造 | 需要保留的边界 |
|---|---|---|
| $R=\mathbb F_2$，即 $\ell=1$ | [[Hypergraph product code]] | ordinary tensor product，没有非平凡 lift 坐标 |
| $A,B$ 都是 $1\times1$ 环值矩阵 | generalized bicycle code | 两个循环块算子必须满足相容对易条件 |
| $R=\mathbb F_2[x]/(x^\ell-1)$ | 准循环 LP | 移位标签属于循环群 |
| $R=\mathbb F_2[G]$，$G$ 为有限阿贝尔群 | quasi-Abelian LP | 交换环公式可直接配合自由正则 balanced quotient |
| $R=\mathbb F_2[G]$，$G$ 为非阿贝尔群 | 左右模 LP/Tanner 构造 | 必须区分右乘和左乘，不能只加一个 $*$ |
| 群对基的作用非自由 | balanced-product code | [[Balanced tensor product 与 coinvariant quotient]] 比 free-lift LP 更一般 |
| 三个二项链复形做两次 balancing | [[Tricycle complex 的 balanced-product 构造]] | 是三因子下游构造，不等同于本篇二因子 LP |

特别地，若 $A=[a]$、$B=[b]$ 都是 $1\times1$ 环值矩阵，LP 公式直接化为

$$
\widehat H_X=[a\mid b],
\qquad
\widehat H_Z=[b^*\mid a^*],
$$

即 generalized bicycle 的标准块形式。

所以 LP 更像统一的乘积语言，而不是与 HGP、generalized bicycle、balanced product 完全并列且互不相干的一个码族。

### 有限实例中的实际问题

首先，qLDPC 不等于几何局域。即使每个稳定子只有常数重量，它接触的量子比特仍可能在二维布局中相距很远；LP 构造本身不提供二维局域嵌入。

其次，一般实例的 $K$ 应从 $\mathbb B(\widehat H_X)$、$\mathbb B(\widehat H_Z)$ 的二进制秩计算。距离则要分析

$$
\ker H_X\setminus\operatorname{im}H_Z^T,
\qquad
\ker H_Z\setminus\operatorname{im}H_X^T
$$

中的最小重量，有限长度时常结合精确搜索、上下界或启发式搜索；不能只从基矩阵尺寸读出。

解码结论也要按子族区分：

- BP-OSD 在多类有限长度退化 qLDPC 码上有良好数值表现；OSD 后处理可缓解普通 BP 因量子简并而出现的错误判断。单独考察 $H_X$ 或 $H_Z$ 时，其 Tanner 图是否含长度 $4$ 的环取决于具体 $A,B$，不能把它说成每个 LP 的必然性质。
- Leverrier–Zémor 为特定渐近良好量子 Tanner 码给出线性时间、可纠正线性重量对抗性错误的解码器，并说明它可适配相应 LP 码族。
- Golowich–Guruswami 针对上述近线性距离 QC 码族给出高效解码器，可纠正 $\Theta(N/\log N)$ 重量的对抗性错误。

这些结果说明“LP 解码”不是一个统一算法问题；可证明阈值与复杂度都依赖构造中额外的扩张性与对称性。

### Lift、商与扩张性的分工

Lift 用群标签提供扭曲，反对角 quotient 把两个群坐标压成一个，扩张性则阻止逻辑支撑按同一比例缩短。LP 的乘积形式自动给出相容的 CSS 校验；低密度、好距离和解码保证仍分别需要稀疏性、扩张性与具体解码定理，不能从 LP 的定义单独推出。

### 来源

- Pavel Panteleev, Gleb Kalachev, [*Quantum LDPC Codes with Almost Linear Minimum Distance*](https://arxiv.org/abs/2012.04068), IEEE Transactions on Information Theory 68, 213–229 (2022)：交换代数上的 LP 定义、QC/QA 特例、$R_3$ 块例、$B=1+x$ 维数公式与近线性距离码族。
- Nikolas P. Breuckmann, Jens N. Eberhardt, [*Balanced Product Quantum Codes*](https://arxiv.org/abs/2012.09271), IEEE Transactions on Information Theory 67, 6653–6674 (2021)：反对角 quotient、自由群作用下的长度压缩，以及阿贝尔自由作用情形与 LP 的对应。
- Pavel Panteleev, Gleb Kalachev, [*Asymptotically Good Quantum and Locally Testable Classical LDPC Codes*](https://arxiv.org/abs/2111.03654), 2021：非阿贝尔群上的左右模构造与渐近良好 qLDPC 码族。
- Pavel Panteleev, Gleb Kalachev, [*Degenerate Quantum LDPC Codes With Good Finite Length Performance*](https://arxiv.org/abs/1904.02703), Quantum 5, 585 (2021)：BP-OSD 与有限长度 generalized bicycle / generalized HGP codes。
- Anthony Leverrier, Gilles Zémor, [*Efficient decoding up to a constant fraction of the code length for asymptotically good quantum codes*](https://arxiv.org/abs/2206.07571), SODA 2023：量子 Tanner 码及相应 LP 码族的线性时间解码。
- Louis Golowich, Venkatesan Guruswami, [*Decoding Quasi-Cyclic Quantum LDPC Codes*](https://arxiv.org/abs/2411.04464), 2024：近线性距离 QC LP 码族的高效对抗性错误解码器。
