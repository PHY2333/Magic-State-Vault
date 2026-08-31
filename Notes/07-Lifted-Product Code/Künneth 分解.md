# Künneth 分解

给定两个链复形 $C_\bullet$ 和 $D_\bullet$，有两条看起来都很合理的计算路线：

$$
C,D
\xrightarrow{\text{先分别取同调}}
H(C),H(D)
\xrightarrow{\text{再作 tensor product}}
H(C)\otimes H(D),
$$

以及

$$
C,D
\xrightarrow{\text{先作 tensor product}}
C\otimes D
\xrightarrow{\text{再取同调}}
H(C\otimes D).
$$

Künneth 问题就是：**这两条路线什么时候给出同一个结果？**

本文采用降低 degree 的 chain convention。对齐次元素 $c\in C_p$、$d\in D_q$，乘积复形按 total degree 分层，边界为

$$
(C\otimes_kD)_n
=
\bigoplus_{p+q=n}C_p\otimes_kD_q,
$$

$$
\partial(c\otimes d)
=
\partial_Cc\otimes d
+(-1)^p c\otimes\partial_Dd.
$$

这与 [[Cochain complex 的 tensor product]] 中升 degree 的写法是同一条 Koszul 符号规则；乘积边界满足 $\partial^2=0$ 的证明也在那里完成。只有在 $\mathbb F_2$ 上，$-1=1$，才可以无说明地省略符号。

## 先看域上的答案

> [!theorem] 域上的 Künneth 定理
> 设 $k$ 是域，$C_\bullet,D_\bullet$ 是 $k$ 上有界的有限维链复形。对每个 $n$，映射
>
> $$
> \kappa_n:
> \bigoplus_{p+q=n}H_p(C)\otimes_kH_q(D)
> \longrightarrow
> H_n(C\otimes_kD),
> $$
>
> $$
> \kappa_n([c]\otimes[d])=[c\otimes d]
> $$
>
> 是自然同构。

左边表示“先分别取同调，再把次数相加”；右边表示“先组成乘积复形，再取同调”。因此，域上的答案非常干净：乘积复形中没有隐藏在因子同调之外的额外类，也没有两个不同的因子同调类在乘积中被意外识别。

对两个二项链复形

$$
\mathcal A:
0\longrightarrow A_1\xrightarrow{A}A_0\longrightarrow0,
\qquad
\mathcal B:
0\longrightarrow B_1\xrightarrow{B}B_0\longrightarrow0,
$$

degree $1$ 只有 $1=1+0$ 与 $1=0+1$ 两种来源，所以定理立刻给出

$$
\boxed{
H_1(\mathcal A\otimes_k\mathcal B)
\cong
\ker A\otimes_k\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes_k\ker B
}.
$$

在 $k=\mathbb F_2$ 的 HGP 中，令

$$
k_A=\dim\ker A,
\qquad
k_A^{\mathsf T}=\dim\ker A^{\mathsf T},
$$

并对 $B$ 使用同样的记号。这两个直和项正是两类逻辑来源，并给出

$$
\boxed{
K=k_Ak_B^{\mathsf T}+k_A^{\mathsf T}k_B
}.
$$

这些结论为什么成立，要分成两个问题：先证明 $\kappa_n$ 不依赖 cycle 代表元的选择，再证明它在域上可逆。

## 一个先看到成功结果的例子

取二项复形

$$
\mathcal E:
0\longrightarrow k^2
\xrightarrow{A}
k^2
\longrightarrow0,
$$

选择 degree-$1$ 的基 $e_1,e_2$ 和 degree-$0$ 的基 $f_1,f_2$，令

$$
A(e_1)=f_1,
\qquad
A(e_2)=0.
$$

于是

$$
H_1(\mathcal E)=\operatorname{span}_k\{[e_2]\},
\qquad
H_0(\mathcal E)=\operatorname{span}_k\{\overline{f_2}\},
$$

其中 $\overline{f_2}$ 是 $f_2$ 在 $k^2/\operatorname{span}\{f_1\}$ 中的商类。Künneth 同构在 degree $1$ 给出

$$
\begin{aligned}
H_1(\mathcal E\otimes_k\mathcal E)
&\cong
H_1(\mathcal E)\otimes_kH_0(\mathcal E)
\oplus
H_0(\mathcal E)\otimes_kH_1(\mathcal E)\\
&\cong
\operatorname{span}_k\{[e_2\otimes f_2]\}
\oplus
\operatorname{span}_k\{[f_2\otimes e_2]\}.
\end{aligned}
$$

所以乘积的一阶同调是二维的。这里可以提前看见后面证明的机制：$e_1\mapsto f_1$ 是一对由同构连接的方向，对同调没有贡献；真正留下的是 cycle 但不是 boundary 的 $e_2$ 与 $f_2$，它们在两个因子之间按 total degree 配对。

## 比较映射为什么有定义

记

$$
Z_p(C)=\ker\partial_p^C,
\qquad
B_p(C)=\operatorname{im}\partial_{p+1}^C,
\qquad
H_p(C)=Z_p(C)/B_p(C).
$$

若 $c\in Z_p(C)$、$d\in Z_q(D)$，则

$$
\partial(c\otimes d)
=
\partial_Cc\otimes d
+(-1)^pc\otimes\partial_Dd
=0,
$$

所以 $c\otimes d$ 是 total degree $p+q$ 的 cycle。于是可以尝试定义

$$
[c]\otimes[d]
\longmapsto
[c\otimes d].
$$

问题在于 $[c]$ 和 $[d]$ 是商类，同一个类可以有许多 cycle 代表元。必须检查改变代表元只会给 $c\otimes d$ 增加一个 boundary。

若用 $c+\partial_Cx$ 代替 $c$，其中 $x\in C_{p+1}$，因为 $d$ 是 cycle，

$$
(\partial_Cx)\otimes d
=
\partial(x\otimes d).
$$

因此第一因子的代表元变化只增加一个乘积 boundary。若用 $d+\partial_Dy$ 代替 $d$，其中 $y\in D_{q+1}$，因为 $c$ 是 cycle，

$$
\partial(c\otimes y)
=
(-1)^pc\otimes\partial_Dy,
$$

也就是

$$
c\otimes\partial_Dy
=
(-1)^p\partial(c\otimes y).
$$

第二因子的代表元变化同样只增加一个 boundary。由双线性，这个规则先下降为

$$
\kappa_{p,q}:
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_{p+q}(C\otimes_kD),
$$

再把所有 $p+q=n$ 的分量合并成 $\kappa_n$。

这一步只证明了 **良定义性**：$\kappa_n$ 是一个不依赖代表元选择的线性映射。它还没有证明该映射是单射或满射；可逆性正是域上 Künneth 定理的实质内容。

## 域上证明的整体地图

域上证明只做一件事：把每个链复形分成“真正承载同调的部分”和“成对相消的部分”。具体分为四步：

1. 在每个 degree 选择补空间，把 $C_n$ 拆成 boundary、同调代表元和非 cycle 三部分；
2. 把 boundary 与非 cycle 配成一个可缩子复形 $Q(C)$；
3. 证明 tensor product 中只要有一个可缩因子，整个分量仍然可缩；
4. 因而 $C\otimes D$ 的同调只来自两个同调代表元部分的 tensor product。

补空间的选择一般不唯一，所以这是一种证明工具，不是 Künneth 同构本身的定义。

### 把一个复形拆成同调代表元与可缩部分

固定 $C_\bullet$。在每个 degree 都有

$$
B_n(C)\subseteq Z_n(C)\subseteq C_n.
$$

因为 $k$ 是域，这些都是向量子空间，可以选择直和补空间。先选 $\widetilde H_n(C)$ 使

$$
Z_n(C)=B_n(C)\oplus\widetilde H_n(C),
$$

再选 $L_n(C)$ 使

$$
C_n=Z_n(C)\oplus L_n(C).
$$

于是

$$
C_n
=
B_n(C)\oplus\widetilde H_n(C)\oplus L_n(C).
$$

商映射在 $\widetilde H_n(C)$ 上给出同构

$$
\rho_n:
\widetilde H_n(C)
\xrightarrow{\sim}
H_n(C),
\qquad
h\longmapsto[h].
$$

它是满射，因为每个 cycle 都能唯一写成 boundary 加上 $\widetilde H_n(C)$ 中的元素；它是单射，因为

$$
B_n(C)\cap\widetilde H_n(C)=0.
$$

因此 $\widetilde H_n(C)$ 可以看作选定的一组同调类代表元。令 $\widetilde{\mathcal H}(C)$ 是以 $\widetilde H_n(C)$ 为 degree-$n$ 分量、微分恒为零的链复形。

另一方面，边界映射限制为

$$
\delta_n
:=
\left.\partial_n\right|_{L_n(C)}:
L_n(C)
\longrightarrow
B_{n-1}(C).
$$

这个限制是同构。若 $\delta_n(\ell)=0$，则 $\ell$ 同时属于 $L_n(C)$ 与 $Z_n(C)$，所以 $\ell=0$；而任意 $b\in B_{n-1}(C)$ 都可写成 $b=\partial x$，将 $x$ 分解为 cycle 与 $L_n(C)$ 分量后，只有后者贡献边界，所以 $b$ 落在 $\delta_n$ 的像中。

定义

$$
Q(C)_n=B_n(C)\oplus L_n(C).
$$

边界在 $B_n(C)$ 上为零，并通过同构 $\delta_n$ 把 $L_n(C)$ 送到 $B_{n-1}(C)$，因此 $Q(C)$ 是链子复形，而且

$$
C_\bullet
=
\widetilde{\mathcal H}(C)_\bullet
\oplus
Q(C)_\bullet
$$

是链复形的直和分解。

### 为什么 $Q(C)$ 没有同调

定义 degree $+1$ 的映射

$$
s_n:Q(C)_n\longrightarrow Q(C)_{n+1}
$$

如下：若 $b\in B_n(C)$、$\ell\in L_n(C)$，令

$$
s_n(b+\ell)=\delta_{n+1}^{-1}(b).
$$

也就是说，$s$ 把 boundary 送回它在下一层 $L_{n+1}(C)$ 中的唯一原像，并在 $L_n(C)$ 上取零。于是

$$
\partial s(b+\ell)=b,
\qquad
s\partial(b+\ell)=\ell,
$$

从而

$$
\boxed{
\partial s+s\partial=\operatorname{id}_{Q(C)}
}.
$$

满足这个等式的 $s$ 称为收缩同伦（contracting homotopy），$Q(C)$ 称为可缩复形。这个等式直接说明其同调为零：若 $q$ 是 cycle，那么

$$
q=(\partial s+s\partial)q=\partial(sq),
$$

所以每个 cycle 都是 boundary。

### 可缩因子在 tensor product 中仍然不贡献同调

这一步必须保留 Koszul 符号。先让可缩部分位于第一因子。若 $u\in Q(C)_p$、$d\in D_q$，定义

$$
S_C(u\otimes d)=s_C(u)\otimes d.
$$

因为 $s_C(u)$ 的 degree 是 $p+1$，展开得到

$$
\begin{aligned}
(\partial S_C+S_C\partial)(u\otimes d)
&=
(\partial s_C+s_C\partial)u\otimes d\\
&\quad+
\bigl((-1)^{p+1}+(-1)^p\bigr)s_C(u)\otimes\partial_Dd\\
&=u\otimes d.
\end{aligned}
$$

交叉项正是靠两个相反的 Koszul 符号抵消。因此 $Q(C)\otimes_kD$ 可缩。

若可缩部分位于第二因子，不能直接写 $\operatorname{id}\otimes s_D$；需要让符号随第一因子的 degree 改变。对齐次 $x\in X_p$、$q\in Q(D)$，定义

$$
S_D(x\otimes q)=(-1)^p x\otimes s_D(q).
$$

展开后，含 $\partial_Xx\otimes s_D(q)$ 的两项系数分别为 $(-1)^p$ 与 $(-1)^{p-1}$，所以相消；剩余部分为

$$
\begin{aligned}
(\partial S_D+S_D\partial)(x\otimes q)
&=
x\otimes(\partial s_D+s_D\partial)q\\
&=x\otimes q.
\end{aligned}
$$

因此 $X\otimes_kQ(D)$ 也可缩。

### Tensor 后只有同调代表元部分留下

对 $C,D$ 分别作上述分解：

$$
C=
\widetilde{\mathcal H}(C)\oplus Q(C),
\qquad
D=
\widetilde{\mathcal H}(D)\oplus Q(D).
$$

Tensor product 对有限直和分配，于是

$$
\begin{aligned}
C\otimes_kD
\cong{}&
\widetilde{\mathcal H}(C)\otimes_k\widetilde{\mathcal H}(D)\\
&\oplus
\widetilde{\mathcal H}(C)\otimes_kQ(D)\\
&\oplus
Q(C)\otimes_k\widetilde{\mathcal H}(D)\\
&\oplus
Q(C)\otimes_kQ(D).
\end{aligned}
$$

后三项都含有可缩因子，所以同调为零。第一项的两个微分都为零，因此其乘积微分也为零。它在 total degree $n$ 的部分是

$$
\bigoplus_{p+q=n}
\widetilde H_p(C)\otimes_k\widetilde H_q(D).
$$

再用 $\rho_p$ 与 $\rho_q$ 把选定代表元空间识别为真正的同调空间，便得到

$$
H_n(C\otimes_kD)
\cong
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D).
$$

存活分量嵌入 $C\otimes D$ 时，把 $h\otimes h'$ 送到同调类 $[h\otimes h']$。在 $\widetilde H_p(C)\cong H_p(C)$ 与 $\widetilde H_q(D)\cong H_q(D)$ 的识别下，这正是比较映射 $\kappa_n$。所以证明的不只是“左右两边维数相同”，而是先前已经定义好的 $\kappa_n$ 本身可逆。

## 自然的比较同构与不自然的证明选择

设 $f:C\to C'$、$g:D\to D'$ 是链映射。比较映射满足

$$
H_n(f\otimes g)\circ\kappa_n^{C,D}
=
\kappa_n^{C',D'}\circ
\bigoplus_{p+q=n}
\bigl(H_p(f)\otimes H_q(g)\bigr).
$$

对纯张量 $[c]\otimes[d]$，等式两边都得到

$$
[f(c)\otimes g(d)].
$$

纯张量张成各个 tensor-product 分量，所以整个等式成立。这就是自然性：沿链映射移动输入，不会改变“先比较还是后比较”的结果。

这里必须区分两件事：

- $\kappa_n([c]\otimes[d])=[c\otimes d]$ 的定义没有选择补空间，并且与链映射相容；
- 证明中选择的 $\widetilde H_n(C)$、$L_n(C)$、收缩 $s$ 与链级直和分解一般不唯一，链映射也未必保持这些选择。

因此，**自然的是比较同构 $\kappa_n$；一般不自然的是用来证明它可逆的链级分裂。** 补空间负责证明逆映射存在，却不应被误认为 Künneth 同构的定义。

## 二项复形与 HGP 的两类逻辑来源

再次取

$$
\mathcal A:
0\longrightarrow A_1\xrightarrow{A}A_0\longrightarrow0,
$$

$$
\mathcal B:
0\longrightarrow B_1\xrightarrow{B}B_0\longrightarrow0.
$$

因为 degree $1$ 上没有来自更高 degree 的 boundary，

$$
H_1(\mathcal A)=\ker A,
\qquad
H_1(\mathcal B)=\ker B.
$$

在 degree $0$，所有元素都是 cycles，而来自 degree $1$ 的 boundaries 分别是 $\operatorname{im}A$ 与 $\operatorname{im}B$，所以

$$
H_0(\mathcal A)=A_0/\operatorname{im}A=\operatorname{coker}A,
$$

$$
H_0(\mathcal B)=B_0/\operatorname{im}B=\operatorname{coker}B.
$$

Total degree $1$ 只有 $(1,0)$ 与 $(0,1)$，于是

$$
H_1(\mathcal A\otimes_k\mathcal B)
\cong
\ker A\otimes_k\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes_k\ker B.
$$

在 [[Hypergraph product code]] 使用的 chain convention 中，乘积复形的中间链群是物理支撑空间，并且

$$
H_1(\mathcal A\otimes\mathcal B)
=
\frac{\ker H_X}{\operatorname{im}H_Z^{\mathsf T}}
$$

表示逻辑 $Z$ 支撑类（logical $Z$ support classes）。第一项可以先在物理子空间 $A_1\otimes B_0$ 中选代表元，第二项可以先在 $A_0\otimes B_1$ 中选代表元；但这里描述的是逻辑类的两种来源，不是两个物理比特扇区本身。给代表元加上乘积 boundary 后，同一个逻辑类的支撑可能同时占据两个物理扇区。

现在令

$$
A:\mathbb F_2^{n_A}\longrightarrow\mathbb F_2^{m_A},
\qquad
B:\mathbb F_2^{n_B}\longrightarrow\mathbb F_2^{m_B},
$$

并定义

$$
k_A=\dim_{\mathbb F_2}\ker A,
\qquad
k_A^{\mathsf T}=\dim_{\mathbb F_2}\ker A^{\mathsf T},
$$

以及相应的 $k_B,k_B^{\mathsf T}$。有限维线性代数给出

$$
\dim_{\mathbb F_2}\operatorname{coker}A
=m_A-\operatorname{rank}A
=\dim_{\mathbb F_2}\ker A^{\mathsf T}
=k_A^{\mathsf T},
$$

对 $B$ 同理。因此两个 Künneth 直和项的维数分别为 $k_Ak_B^{\mathsf T}$ 与 $k_A^{\mathsf T}k_B$，从而

$$
\boxed{
K=k_Ak_B^{\mathsf T}+k_A^{\mathsf T}k_B
}.
$$

这条公式揭示逻辑比特的两个同调来源。HGP 的物理比特扇区、校验矩阵分块、CSS 对易与距离问题仍由 [[Hypergraph product code]] 负责。

## PID 与一般系数环

只研究二进制 HGP 的读者可以先跳过本节；准备把域上的公式搬到环系数 LP 时，本节给出必须检查的边界。

域上的直和公式依赖一个关键事实：向量空间中的短正合列在选择补空间后可以分裂，而且所有向量空间都是平坦模。换成一般环上的模后，tensor product 可能不再保持正合，补空间也未必存在。此时需要分三层判断：PID 上出现 $\operatorname{Tor}_1$ 短正合列；一般交换环上要看导出张量积与谱序列；具体 LP 参数最终仍可回到展开后的二进制秩。

### PID：比较映射嵌入短正合列

设 $R$ 是主理想整环（principal ideal domain, PID）。一个 $R$-模 $F$ 称为平坦模，如果 tensor functor $F\otimes_R-$ 保持短正合列。现在令 $C,D$ 是有界 $R$-链复形，并且至少一个因子逐项平坦，也就是该因子的每个链模都平坦；要求两个因子逐项自由是更强、但常用而安全的充分条件，不是必要条件。

在这些假设下，May 的 Künneth 定理给出自然短正合列

$$
0
\longrightarrow
\bigoplus_{p+q=n}
H_p(C)\otimes_RH_q(D)
\xrightarrow{\ \kappa_n\ }
H_n(C\otimes_RD)
\longrightarrow
\bigoplus_{p+q=n-1}
\operatorname{Tor}_1^R\bigl(H_p(C),H_q(D)\bigr)
\longrightarrow0.
$$

$\operatorname{Tor}_1^R(M,N)$ 衡量 ordinary tensor product 没有保持短正合列的程度。这里它不是凭空附加的第三种因子，而是描述 $H_n(C\otimes_RD)$ 除去 $\kappa_n$ 的像后还剩下什么。

这个短正合列可以分裂，所以抽象地存在某个模同构，把中间项写成左右两项的直和；但是分裂一般不自然。也就是说，通常没有一个对所有链映射都相容的首选方式，把每个 $\operatorname{Tor}_1$ 类提升成乘积同调类。因此不能把该直和写成与域上 $\kappa_n$ 同样自然的分解。

若对所有满足 $p+q=n-1$ 的 $(p,q)$，$H_p(C)$ 与 $H_q(D)$ 中至少一个是平坦模，则相应的 $\operatorname{Tor}_1$ 消失，$\kappa_n$ 便在该 degree 恢复为同构。这个条件是充分条件，不是 $\operatorname{Tor}_1=0$ 的必要条件。域是特殊情形，因为域上的每个模都平坦。

### 一般交换环：目标先变成导出张量积

设 $R$ 是一般交换环，$C,D$ 是有界 $R$-链复形。一个复形若同调全为零，称为无同调复形。复形 $P$ 称为 K-flat，如果它与任意无同调复形作 total tensor product 后仍然无同调。这个条件的作用是保证：用准同构替换另一个因子时，tensor product 的同调不会被改变。

导出张量积（derived tensor product）的做法是先把至少一个因子替换为与它准同构的 K-flat 复形，再作 ordinary tensor product；这里准同构是指在每个 degree 上都诱导同调同构的链映射。所得对象记为

$$
C\otimes_R^{\mathbf L}D.
$$

若 $C$ 或 $D$ 本身已经 K-flat，就可以直接用 ordinary tensor product 表示这个导出张量积。有界且逐项自由的复形是 K-flat 的安全充分条件。若两个因子都没有经过 K-flat 验证，就不能把下面谱序列的收敛目标直接改写成 $H(C\otimes_RD)$。还必须注意：**K-flat 只保证 ordinary tensor product 算对了导出张量积，并不保证下面的谱序列在第二页退化。**

[The Stacks Project, Tag 0H7Z](https://stacks.math.columbia.edu/tag/0H7Z) 使用上同调指标。把它按 $H_p(C)=H^{-p}(C^\bullet)$ 重编号为同调指标后，得到有界 Künneth 谱序列

$$
E^2_{s,t}
=
\bigoplus_{p+q=t}
\operatorname{Tor}_s^R\bigl(H_p(C),H_q(D)\bigr)
\Longrightarrow
H_{s+t}\bigl(C\otimes_R^{\mathbf L}D\bigr),
$$

其第 $r$ 页微分方向为

$$
d_r:
E^r_{s,t}
\longrightarrow
E^r_{s-r,t+r-1}.
$$

这里 $E^2$ 只是计算的起点。一般环相对域上的简单直和结论有三层额外问题：

1. **高阶 $\operatorname{Tor}$：** $s>0$ 的位置可能已经非零；
2. **后续微分：** $E^2$ 上的项还可能被某个 $d_r$ 杀掉，或成为别的项的边界；
3. **扩张（extension）问题：** 即使到 $E^\infty$ 已经稳定，它也只给出目标同调的伴随分次，而不是目标同调的首选直和分解。

第三点具体表示：对 $H_n=H_n(C\otimes_R^{\mathbf L}D)$，存在一个有限滤过

$$
0=F_{-1}H_n
\subseteq
F_0H_n
\subseteq
F_1H_n
\subseteq
\cdots
\subseteq
H_n,
$$

并且

$$
F_sH_n/F_{s-1}H_n
\cong
E^\infty_{s,n-s}.
$$

把这些相邻层之商并列起来，称为 $H_n$ 的伴随分次：

$$
\operatorname{gr}H_n
:=
\bigoplus_sF_sH_n/F_{s-1}H_n
\cong
\bigoplus_sE^\infty_{s,n-s}.
$$

$E^\infty$ 告诉我们每一相邻层之商是什么；要把这些商重新拼成 $H_n$，还要解相应的扩张问题。即使每个商都已知，也不能未经证明就写成它们的直和。

因此，在一般交换环上，不能把 $E^2$ 页的高阶 $\operatorname{Tor}$ 直接当作额外逻辑直和项，也不能把 $E^\infty$ 的各格直接相加成一个自然分解。另一方面，“系数环不是域”只表示域上的结论不再自动成立，并不表示每个非域实例都会出现非零 $\operatorname{Tor}$、非平凡微分或失败的比较映射。

### 一个直接计算的失败例子

下面的反例是本文中的直接计算。它也是最小循环系数环的一个例子：令 $\varepsilon=x+1$，则

$$
R_2
=
\mathbb F_2[x]/\langle x^2-1\rangle
\cong
\mathbb F_2[\varepsilon]/\langle\varepsilon^2\rangle,
$$

因为在 $\mathbb F_2$ 上有 $x^2-1=(x+1)^2$。

取两个相同的二项自由 $R_2$-复形

$$
C=D=
\left(
0\longrightarrow R_2
\xrightarrow{\ \varepsilon\ }
R_2\longrightarrow0
\right),
$$

其中边界映射是乘以 $\varepsilon$。若 $u=a+b\varepsilon$，其中 $a,b\in\mathbb F_2$，则

$$
\varepsilon u=a\varepsilon,
$$

所以

$$
H_1(C)=\ker(\varepsilon)=(\varepsilon),
\qquad
H_0(C)=R_2/\langle\varepsilon\rangle,
$$

对 $D$ 也一样。作为 $R_2$-模，

$$
(\varepsilon)\cong R_2/\langle\varepsilon\rangle,
$$

而

$$
\bigl(R_2/\langle\varepsilon\rangle\bigr)
\otimes_{R_2}
\bigl(R_2/\langle\varepsilon\rangle\bigr)
\cong
R_2/\langle\varepsilon\rangle.
$$

所以 $\kappa_1$ 的定义域

$$
H_1(C)\otimes_{R_2}H_0(D)
\oplus
H_0(C)\otimes_{R_2}H_1(D)
$$

由两个一维 $\mathbb F_2$ 分量组成。

按

$$
(C_1\otimes_{R_2}D_0)
\oplus
(C_0\otimes_{R_2}D_1)
$$

排列 degree-$1$ 项，并使用 $R_2\otimes_{R_2}R_2\cong R_2$，乘积复形为

$$
R_2
\xrightarrow{\partial_2}
R_2^2
\xrightarrow{\partial_1}
R_2,
$$

其中特征 $2$ 使两个 Koszul 符号相同，并且

$$
\partial_2(r)=(\varepsilon r,\varepsilon r),
\qquad
\partial_1(a,b)=\varepsilon(a+b).
$$

以 $\{1,\varepsilon\}$ 为 $R_2$ 的 $\mathbb F_2$-基，直接得到

$$
\ker\partial_1
=
\operatorname{span}_{\mathbb F_2}
\{(1,1),(\varepsilon,0),(0,\varepsilon)\},
$$

$$
\operatorname{im}\partial_2
=
\operatorname{span}_{\mathbb F_2}
\{(\varepsilon,\varepsilon)\}.
$$

因此

$$
\dim_{\mathbb F_2}H_1(C\otimes_{R_2}D)=3-1=2.
$$

$\kappa_1$ 的两个源生成元

$$
[\varepsilon]\otimes[1],
\qquad
[1]\otimes[\varepsilon]
$$

分别映到

$$
[(\varepsilon,0)],
\qquad
[(0,\varepsilon)].
$$

这两个类都非零，因为 $\operatorname{im}\partial_2$ 只由 $(\varepsilon,\varepsilon)$ 张成；但它们代表同一个非零类，因为

$$
(\varepsilon,0)+(0,\varepsilon)
=(\varepsilon,\varepsilon)
=\partial_2(1).
$$

事实上可以取

$$
[(\varepsilon,0)],
\qquad
[(1,1)]
$$

作为 $H_1(C\otimes_{R_2}D)$ 的一组 $\mathbb F_2$-基。第二个类与第一个类线性无关，所以不在 $\kappa_1$ 的像中。于是

$$
\operatorname{rank}_{\mathbb F_2}\kappa_1=1.
$$

比较映射的定义域和目标都具有二进制维数 $2$，但 $\kappa_1$ 既非单射也非满射：一个非零源方向被压成零，同时一个非零目标方向没有原像。失败发生在映射结构本身，而不是因为两端维数预先不同。

这里 $\varepsilon^2=0$，所以 $R_2$ 有零因子，不是整环，更不是 PID；因此不能把前一小节的 PID 短正合列套到这个例子上。这个反例只证明域上的直和公式不能无条件推广到 $R_2$，并不证明所有非域系数环或所有环系数乘积都会失败。

### 环系数 LP 的安全判断

循环 LP 常用交换环

$$
R_\ell=
\mathbb F_2[x]/\langle x^\ell-1\rangle.
$$

它通常不是域，也不能默认为 PID。LP 输入的二项复形逐项自由且有界，所以 ordinary tensor product 可以代表相应的导出张量积；但是这并不自动消除高阶 $\operatorname{Tor}$，也不自动保证谱序列退化或扩张分裂。

因此，除非已经用相关同调模的平坦性或其他结构证明所需的谱序列退化，并解决可能的扩张问题，否则不能把域上的

$$
K=k_Ak_B^{\mathsf T}+k_A^{\mathsf T}k_B
$$

无条件用于环系数 LP。即使某个模级 Künneth 分解成立，$\dim_{\mathbb F_2}(M\otimes_RN)$ 也一般不等于 $\dim_{\mathbb F_2}M$ 与 $\dim_{\mathbb F_2}N$ 的乘积。

对一个具体的有限 LP 实例，安全而直接的做法是先按 [[Lifted product code]] 展开得到二进制 CSS 校验矩阵，再计算

$$
\boxed{
K
=
N
-
\operatorname{rank}_{\mathbb F_2}H_X
-
\operatorname{rank}_{\mathbb F_2}H_Z
}.
$$

非交换群代数情形还必须区分右模与左模，并检查两侧作用的相容性；这些 convention 属于 [[Lifted product code]]，不由本篇交换环版本的 Künneth 讨论代替。

## 回收主线

Künneth 分解回答的不是“tensor product 怎样分层”，而是“取同调与作 tensor product 能否交换”。

在域上，比较映射

$$
[c]\otimes[d]
\longmapsto
[c\otimes d]
$$

是自然同构。它的良定义性来自改变 cycle 代表元只会增加乘积 boundary；它的可逆性来自每个复形都能非典范地拆成零微分的同调代表元部分与可缩部分，而所有含可缩因子的 tensor summands 都不贡献同调。

对两个二项复形，degree-$1$ 同调因此分成

$$
\ker A\otimes\operatorname{coker}B
\quad\text{与}\quad
\operatorname{coker}A\otimes\ker B
$$

两类逻辑来源，并在二进制 HGP 中给出 $K=k_Ak_B^{\mathsf T}+k_A^{\mathsf T}k_B$。

一旦系数从域换成环，首先要问的是所处层级：PID 上由 $\operatorname{Tor}_1$ 短正合列控制；一般交换环上由导出张量积与 Künneth 谱序列控制；具体 LP 若没有额外退化或平坦性证明，就回到展开后的二进制矩阵秩。这样才能知道哪一步仍然成立，而不是把域上的直和公式当成无条件恒等式。

## 来源与延伸

- J. P. May, [*A Concise Course in Algebraic Topology*](https://math.uchicago.edu/~chicagotopology2/ConciseRevised.pdf), Chapter 17, “The Künneth theorem”：PID 上的自然短正合列、一般不自然的分裂与域上的自然同构。
- The Stacks Project, [*Derived tensor product*, Tag 06XY](https://stacks.math.columbia.edu/tag/06XY)：K-flat 复形与导出张量积。
- The Stacks Project, [*Künneth Spectral Sequence*, Tag 0H7Z](https://stacks.math.columbia.edu/tag/0H7Z)：一般环上有界的导出 Künneth 谱序列。
- [[Chain complex 与 cochain complex]]：cycle、boundary 与同调商空间。
- [[Cochain complex 的 tensor product]]：total degree、product differential 与 Koszul sign。
- [[二进制空间性质]]：向量子空间补空间的存在性与非唯一性。
- [[Hypergraph product code]]：HGP 的物理比特扇区、逻辑支撑商空间、校验矩阵与参数记号。
- [[Lifted product code]]：环值分块、balanced tensor product、二进制展开与 LP 参数计算。
