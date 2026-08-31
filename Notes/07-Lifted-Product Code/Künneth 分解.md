# Künneth 分解

令 $k$ 为一个域，$C_\bullet,D_\bullet$ 为 $k$ 上有界的有限维链复形。本文采用降低 degree 的 chain convention：

$$
\partial_C:C_p\longrightarrow C_{p-1},
\qquad
\partial_D:D_q\longrightarrow D_{q-1}.
$$

在 degree $p$，闭链（cycle）、边界（boundary）与同调分别是

$$
Z_p(C)
=
\ker\bigl(\partial_C:C_p\to C_{p-1}\bigr),
$$

$$
B_p(C)
=
\operatorname{im}
\bigl(\partial_C:C_{p+1}\to C_p\bigr),
$$

$$
H_p(C)
=
Z_p(C)/B_p(C).
$$

记号

$$
H(C)
=
\bigoplus_pH_p(C)
$$

表示把各个 $H_p(C)$ 保留在原 degree 后组成的分次向量空间（graded vector space），不是把不同 degree 忘掉后混成一个普通空间。

符号 $\otimes_k$ 表示在系数域 $k$ 上取张量积（tensor product）。乘积复形按总次数（total degree）分层：

$$
(C\otimes_kD)_n
=
\bigoplus_{p+q=n}
C_p\otimes_kD_q.
$$

对齐次元素 $c\in C_p$、$d\in D_q$，乘积边界是

$$
\partial(c\otimes d)
=
\partial_Cc\otimes d
+
(-1)^p c\otimes\partial_Dd.
$$

这正是 [[Cochain complex 的 tensor product]] 中升次数公式的降次数版本。符号 $(-1)^p$ 是 Koszul 符号；只有在 $\mathbb F_2$ 上，因为 $-1=1$，才可以把它省略。本文不重复证明 $\partial^2=0$。

现在，计算乘积同调有两条路线。第一条路线先分别取同调，再把同调 degree 配成总次数 $n$：

$$
C,D
\longrightarrow
H(C),H(D)
\longrightarrow
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D).
$$

第二条路线先组成乘积复形，再取 degree-$n$ 同调：

$$
C,D
\longrightarrow
C\otimes_kD
\longrightarrow
H_n(C\otimes_kD).
$$

Künneth 问题问的是：

$$
\boxed{
\text{什么时候可以只用 }H(C)\text{ 与 }H(D)
\text{，恢复 }H(C\otimes_kD)\text{？}
}
$$

要比较这两条路线，不能只比较维数；需要先构造一张从第一条路线的结果指向第二条路线的映射。

## 比较映射：两条计算路线怎样相遇

Künneth 定理不是先声称左右两边维数相等，而是先构造一个有明确方向的映射。

取

$$
c\in Z_p(C),
\qquad
d\in Z_q(D).
$$

记 $[c]$、$[d]$ 分别为它们在同调商空间中的类。因为 $c,d$ 都是 cycles，

$$
\partial(c\otimes d)
=
\partial_Cc\otimes d
+
(-1)^pc\otimes\partial_Dd
=0,
$$

所以 $c\otimes d$ 是 $C\otimes_kD$ 中总次数为 $p+q$ 的 cycle。于是有一个候选规则

$$
[c]\otimes[d]
\longmapsto
[c\otimes d].
$$

这里必须先检查代表元无关性，因为 $[c]$、$[d]$ 是商空间中的类，而不是指定的向量。

若把 $c$ 换成同一个同调类的另一个代表元 $c+\partial_Cx$，其中 $x\in C_{p+1}$，那么

$$
(\partial_Cx)\otimes d
=
\partial(x\otimes d),
$$

因为 $\partial_Dd=0$。因此第一因子的代表元变化只给 $c\otimes d$ 增加一个 boundary。

若把 $d$ 换成 $d+\partial_Dy$，其中 $y\in D_{q+1}$，那么

$$
\partial(c\otimes y)
=
(-1)^pc\otimes\partial_Dy,
$$

所以

$$
c\otimes\partial_Dy
=
(-1)^p\partial(c\otimes y).
$$

第二因子的代表元变化也只增加一个 boundary。这个候选规则对两个同调类分别线性，因此由张量积的泛性质得到线性映射

$$
\kappa_{p,q}:
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_{p+q}(C\otimes_kD),
$$

$$
\kappa_{p,q}([c]\otimes[d])
=
[c\otimes d].
$$

把所有满足 $p+q=n$ 的分量相加，得到 degree $n$ 的比较映射

$$
\boxed{
\kappa_n:
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_n(C\otimes_kD)
}.
$$

良定义性只说明 $\kappa_n$ 确实是一张映射。Künneth 问题还要分别回答：

- $\kappa_n$ 是否单射：若若干因子同调类的张量和在乘积复形中变成 boundary，它在源空间中是否已经为零？
- $\kappa_n$ 是否满射：乘积复形的每个 degree-$n$ 同调类，是否都能写成若干 $[c\otimes d]$ 之和？
- 若两者都成立，$\kappa_n$ 才是同构。

### 自然性在这里是什么意思

设

$$
f:C_\bullet\longrightarrow C'_\bullet,
\qquad
g:D_\bullet\longrightarrow D'_\bullet
$$

是链映射，即它们保持 degree，并与边界交换：

$$
f\partial_C=\partial_{C'}f,
\qquad
g\partial_D=\partial_{D'}g.
$$

因此 $f$ 把 cycles 送到 cycles、把 boundaries 送到 boundaries，并诱导

$$
H_p(f):H_p(C)\longrightarrow H_p(C'),
\qquad
H_p(f)([c])=[f(c)].
$$

$H_q(g)$ 同理。两张链映射还诱导乘积链映射

$$
f\otimes g:
C\otimes_kD
\longrightarrow
C'\otimes_kD',
$$

$$
(f\otimes g)(c\otimes d)
=
f(c)\otimes g(d).
$$

比较映射的自然性是下面的交换关系：

$$
H_n(f\otimes g)\circ\kappa_n^{C,D}
=
\kappa_n^{C',D'}
\circ
\bigoplus_{p+q=n}
\bigl(H_p(f)\otimes H_q(g)\bigr).
$$

对纯张量 $[c]\otimes[d]$，等式两边都得到

$$
[f(c)\otimes g(d)].
$$

纯张量张成比较映射的整个源空间，所以这个等式对任意元素成立。因此，无论先用 $f,g$ 移动两个因子，再作比较，还是先作比较，再用 $f\otimes g$ 移动乘积复形，结果相同。“自然”在这里不是“看起来合理”，而是这张图对所有链映射都交换。

## 域上的 Künneth 定理

现在所有符号都已经落地，可以陈述结论。

**定理（域上的 Künneth 定理）.** 设 $k$ 是域，$C_\bullet,D_\bullet$ 是 $k$ 上有界的有限维链复形。对每个整数 $n$，比较映射

$$
\kappa_n:
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_n(C\otimes_kD)
$$

是自然同构。

这条定理同时给出三个可执行结论：

1. 乘积同调中的每个类都能由两个因子的同调类张量生成，即 $\kappa_n$ 满射；
2. 不同的源类不会仅仅因为进入乘积复形就被额外识别，即 $\kappa_n$ 单射；
3. 这个识别由公式 $[c]\otimes[d]\mapsto[c\otimes d]$ 给出，并与链映射相容，而不是依赖某组基或补空间。

因此在域上，

$$
\boxed{
H_n(C\otimes_kD)
\cong
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D)
}.
$$

右边不是没有映射含义的抽象维数公式；它是比较映射 $\kappa_n$ 给出的自然同构。

## 一个先看到证明机制的有限维例子

取二项复形

$$
\mathcal E:
0\longrightarrow k^2
\xrightarrow{A}
k^2
\longrightarrow0,
$$

其中左、右两项的 degree 分别为 $1,0$。选择基 $e_1,e_2$ 与 $f_1,f_2$，并令

$$
A(e_1)=f_1,
\qquad
A(e_2)=0.
$$

于是

$$
H_1(\mathcal E)
=
\operatorname{span}_k\{[e_2]\},
$$

$$
H_0(\mathcal E)
=
k^2/\operatorname{span}_k\{f_1\}
=
\operatorname{span}_k\{\overline{f_2}\}.
$$

这里 $\overline{f_2}$ 表示 $f_2$ 在 cokernel 中的商类。两个同调空间都是一维。Künneth 定理逐个总次数给出

$$
\dim_k H_2(\mathcal E\otimes_k\mathcal E)=1,
$$

$$
\dim_k H_1(\mathcal E\otimes_k\mathcal E)=2,
$$

$$
\dim_k H_0(\mathcal E\otimes_k\mathcal E)=1.
$$

例如 degree $1$ 的两个生成方向是

$$
[e_2]\otimes\overline{f_2},
\qquad
\overline{f_2}\otimes[e_2].
$$

这个例子预告了证明的核心：方向 $e_1\mapsto f_1$ 由同构连接，会成对相消；$e_2$ 与 $f_2$ 才承载同调。它说明域上分裂证明如何工作，却不能单凭这个例子推广到一般系数环，因为一般模未必能选出同样的直和补空间，张量积也未必保持正合。

## 域上定理的完整证明

证明要把每个复形分成两部分：

$$
\text{同调代表元部分}
\quad\oplus\quad
\text{可缩部分}.
$$

随后证明，只要张量积的一个因子可缩，整个分量就不贡献同调。证明路线是：

1. 在每个 degree 选择同调代表元和非-cycle 的补空间；
2. 把 boundaries 与非-cycles 配成可缩子复形；
3. 写出第一因子与第二因子上的收缩同伦，并检查 Koszul 符号；
4. 展开 $C\otimes D$ 的四个直和分量，只留下两个同调代表元部分的张量积；
5. 核对留下的同构正是先前定义的 $\kappa_n$。

### 第一步：把链群拆成三部分

先固定 $C_\bullet$。每个 degree 都有

$$
B_n(C)\subseteq Z_n(C)\subseteq C_n.
$$

因为 $k$ 是域，这些对象是向量子空间，因而存在直和补空间。先选

$$
\widetilde H_n(C)\subseteq Z_n(C)
$$

使

$$
Z_n(C)
=
B_n(C)\oplus\widetilde H_n(C),
$$

再选

$$
L_n(C)\subseteq C_n
$$

使

$$
C_n
=
Z_n(C)\oplus L_n(C).
$$

于是

$$
\boxed{
C_n
=
B_n(C)
\oplus
\widetilde H_n(C)
\oplus
L_n(C)
}.
$$

商映射限制在 $\widetilde H_n(C)$ 上，给出同构

$$
\rho_n:
\widetilde H_n(C)
\xrightarrow{\sim}
H_n(C),
\qquad
h\longmapsto[h].
$$

它是满射，因为每个 cycle 都能写成 boundary 加上 $\widetilde H_n(C)$ 中的元素；它是单射，因为

$$
B_n(C)\cap\widetilde H_n(C)=0.
$$

令 $\widetilde{\mathcal H}(C)$ 表示这样的链复形：其 degree-$n$ 链群是 $\widetilde H_n(C)$，所有边界映射都为零。它是 $C$ 的链子复形。

接着考察边界在 $L_n(C)$ 上的限制：

$$
\lambda_n
:=
\left.\partial_C\right|_{L_n(C)}:
L_n(C)
\longrightarrow
B_{n-1}(C).
$$

这张映射是同构。

若 $\lambda_n(\ell)=0$，则 $\ell\in L_n(C)\cap Z_n(C)$，所以 $\ell=0$，故 $\lambda_n$ 单射。

另一方面，任取 $b\in B_{n-1}(C)$。存在 $x\in C_n$ 使 $b=\partial_Cx$。把 $x$ 按

$$
C_n=Z_n(C)\oplus L_n(C)
$$

写成 $x=z+\ell$，则

$$
b=\partial_Cx=\partial_C\ell.
$$

所以 $\lambda_n$ 满射。

现在定义

$$
Q(C)_n
=
B_n(C)\oplus L_n(C).
$$

边界在 $B_n(C)$ 上为零，并通过 $\lambda_n$ 把 $L_n(C)$ 同构地送到 $B_{n-1}(C)$。因此 $Q(C)$ 是链子复形，而且

$$
\boxed{
C_\bullet
=
\widetilde{\mathcal H}(C)_\bullet
\oplus
Q(C)_\bullet
}
$$

是链复形的直和分解。

### 第二步：证明 $Q(C)$ 可缩

定义 degree $+1$ 的线性映射

$$
s_n:
Q(C)_n
\longrightarrow
Q(C)_{n+1}
$$

如下。对 $b\in B_n(C)$、$\ell\in L_n(C)$，令

$$
s_n(b+\ell)
=
\lambda_{n+1}^{-1}(b).
$$

也就是说，$s$ 把 boundary $b$ 送回它在 $L_{n+1}(C)$ 中的唯一原像，并在 $L_n(C)$ 上取零。于是

$$
\partial_Cs(b+\ell)=b,
$$

而

$$
s\partial_C(b+\ell)
=
s(\partial_C\ell)
=
\ell.
$$

因此

$$
\boxed{
\partial_Cs+s\partial_C
=
\operatorname{id}_{Q(C)}
}.
$$

满足这个等式的 degree-$+1$ 映射称为收缩同伦（contracting homotopy），而 $Q(C)$ 称为可缩复形。

这个等式立即推出 $Q(C)$ 无同调。若 $q\in Q(C)$ 是 cycle，则

$$
q
=
(\partial_Cs+s\partial_C)q
=
\partial_C(sq),
$$

所以每个 cycle 都是 boundary。

### 第三步：含有可缩因子的张量分量仍可缩

令 $X_\bullet$ 是任意链复形。这里的 $X$ 只是“任意另一个链复形”的占位符，与量子码记号中的 $X$ 型校验无关。

先让可缩复形位于第一因子。设 $q\in Q(C)_p$、$x\in X_r$ 都是齐次元素，定义

$$
S_1(q\otimes x)
=
s(q)\otimes x.
$$

因为 $s(q)$ 的 degree 是 $p+1$，

$$
\partial S_1(q\otimes x)
=
\partial_Cs(q)\otimes x
+
(-1)^{p+1}s(q)\otimes\partial_Xx,
$$

而

$$
S_1\partial(q\otimes x)
=
s\partial_C(q)\otimes x
+
(-1)^ps(q)\otimes\partial_Xx.
$$

两式相加时，交叉项的系数为

$$
(-1)^{p+1}+(-1)^p=0,
$$

所以

$$
(\partial S_1+S_1\partial)(q\otimes x)
=
(\partial_Cs+s\partial_C)q\otimes x
=
q\otimes x.
$$

因此

$$
Q(C)\otimes_kX
$$

可缩。

再让可缩复形位于第二因子。对齐次元素 $x\in X_p$、$q\in Q(D)$，不能直接使用 $\operatorname{id}\otimes s$，而要定义

$$
S_2(x\otimes q)
=
(-1)^p x\otimes s(q).
$$

这一次

$$
\partial S_2(x\otimes q)
=
(-1)^p\partial_Xx\otimes s(q)
+
x\otimes\partial_Ds(q),
$$

并且

$$
S_2\partial(x\otimes q)
=
(-1)^{p-1}\partial_Xx\otimes s(q)
+
x\otimes s\partial_D(q).
$$

含有 $\partial_Xx\otimes s(q)$ 的两项系数相反，因此

$$
(\partial S_2+S_2\partial)(x\otimes q)
=
x\otimes(\partial_Ds+s\partial_D)q
=
x\otimes q.
$$

所以

$$
X\otimes_kQ(D)
$$

也可缩。第二因子上的额外符号 $(-1)^p$ 正是保证交叉项抵消所必需的 Koszul 符号。

### 第四步：乘积同调只来自代表元部分

对 $C,D$ 分别作上述分解：

$$
C
=
\widetilde{\mathcal H}(C)\oplus Q(C),
$$

$$
D
=
\widetilde{\mathcal H}(D)\oplus Q(D).
$$

张量积对有限直和分配，因此

$$
\begin{aligned}
C\otimes_kD
\cong{}&
\widetilde{\mathcal H}(C)
\otimes_k
\widetilde{\mathcal H}(D)
\\
&\oplus
\widetilde{\mathcal H}(C)
\otimes_k
Q(D)
\\
&\oplus
Q(C)
\otimes_k
\widetilde{\mathcal H}(D)
\\
&\oplus
Q(C)
\otimes_k
Q(D).
\end{aligned}
$$

后三项都含有可缩因子，所以同调为零。第一项的两个因子边界都为零，因此它的乘积边界也为零。其总次数 $n$ 的链群是

$$
\bigoplus_{p+q=n}
\widetilde H_p(C)\otimes_k\widetilde H_q(D).
$$

于是

$$
H_n(C\otimes_kD)
\cong
\bigoplus_{p+q=n}
\widetilde H_p(C)\otimes_k\widetilde H_q(D).
$$

再用

$$
\rho_p:
\widetilde H_p(C)\xrightarrow{\sim}H_p(C),
\qquad
\rho_q:
\widetilde H_q(D)\xrightarrow{\sim}H_q(D)
$$

识别同调代表元空间，就得到

$$
H_n(C\otimes_kD)
\cong
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D).
$$

更重要的是，存活分量中的 $h\otimes h'$ 进入原乘积复形后代表

$$
[h\otimes h'].
$$

在 $\rho_p,\rho_q$ 的识别下，这正是

$$
\kappa_n([h]\otimes[h'])
=
[h\otimes h'].
$$

因此证明的是先前已经定义好的 $\kappa_n$ 本身可逆，而不只是源与目标维数相等。

从证明中还可直接读出单射与满射：

- 每个乘积同调类都可以消去含 $Q(C)$ 或 $Q(D)$ 的部分，只留下代表元张量之和，所以 $\kappa_n$ 满射；
- 留下的代表元张量位于零边界的直和分量中，若其同调类为零，它本身只能为零，所以 $\kappa_n$ 单射。

### 第五步：自然同构与非自然分裂不能混为一谈

证明中选择了

$$
\widetilde H_n(C),
\qquad
L_n(C),
\qquad
\widetilde H_n(D),
\qquad
L_n(D).
$$

这些补空间通常不唯一，也没有理由被任意链映射保持。由它们构造的链级投影、收缩同伦和显式分裂，一般都不自然。

但是比较映射

$$
\kappa_n([c]\otimes[d])
=
[c\otimes d]
$$

在选择补空间之前就已经定义，而且前面已经直接验证它满足自然性交换关系。补空间只用于证明这张既定映射是双射，并不参与它的定义。

因此要区分：

$$
\boxed{
\text{自然的是比较同构 }\kappa_n;
\quad
\text{一般不自然的是证明中选出的链级分裂。}
}
$$

既然 $\kappa_n$ 是自然同构，它的逆映射族 $\kappa_n^{-1}$ 也自然。对每个固定对象，用任意一组补空间算出的同调级逆映射，最终都等于这个唯一的 $\kappa_n^{-1}$；不自然的是补空间、链级投影和收缩同伦本身无法随对象统一选择成一个与所有链映射相容的链级构造。

## 二项复形与超图乘积码（hypergraph product, HGP）的两类逻辑来源

取两个二项链复形

$$
\mathcal A:
0\longrightarrow A_1
\xrightarrow{A}
A_0
\longrightarrow0,
$$

$$
\mathcal B:
0\longrightarrow B_1
\xrightarrow{B}
B_0
\longrightarrow0,
$$

其中非零项位于 degree $1,0$。因为 degree $1$ 上没有更高一层提供 boundaries，

$$
H_1(\mathcal A)=\ker A,
\qquad
H_1(\mathcal B)=\ker B.
$$

在 degree $0$，所有元素都是 cycles，而 boundaries 分别是 $\operatorname{im}A$、$\operatorname{im}B$，所以

$$
H_0(\mathcal A)
=
A_0/\operatorname{im}A
=
\operatorname{coker}A,
$$

$$
H_0(\mathcal B)
=
B_0/\operatorname{im}B
=
\operatorname{coker}B.
$$

总次数 $1$ 只有

$$
1=1+0
\qquad\text{与}\qquad
1=0+1
$$

两种来源。域上的 Künneth 定理因此给出

$$
\boxed{
H_1(\mathcal A\otimes_k\mathcal B)
\cong
\ker A\otimes_k\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes_k\ker B
}.
$$

这就是后面量子码应用中的两个 Künneth 直和项。

以下专门取 $k=\mathbb F_2$。

### 从乘积复形翻译到 HGP

HGP 把两份二项复形的乘积组织成三项链复形

$$
C_2
\xrightarrow{H_Z^{\mathsf T}}
C_1
\xrightarrow{H_X}
C_0.
$$

这里三个空间的角色不同：

- $C_1$ 是物理量子比特支撑的坐标空间；
- 对支撑向量 $z\in C_1$，条件 $H_Xz=0$ 检查它是否与全部 $X$ 型校验交换；
- $\operatorname{im}H_Z^{\mathsf T}$ 是 $Z$ 型稳定子支撑。

因此

$$
\boxed{
H_1
=
\frac{\ker H_X}
{\operatorname{im}H_Z^{\mathsf T}}
}
$$

是逻辑 $Z$ 支撑类空间：先在整个物理支撑空间中取通过 $X$ 检查的向量，再把相差一个 $Z$ 稳定子的支撑视为同一类。

这里必须区分两种直和。原始中间链群具有物理坐标分解

$$
C_1
=
(A_1\otimes_{\mathbb F_2} B_0)
\oplus
(A_0\otimes_{\mathbb F_2} B_1).
$$

它在取核与商空间之前就存在，描述两类物理比特坐标。相比之下，

$$
\ker A\otimes\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes\ker B
$$

是 $H_1$ 的分解，描述逻辑类的两个 Künneth 来源。可以在相应物理分量中为每个来源选择初始代表元，但给代表元加上 boundary 后，同一个逻辑类可能同时占据两个物理分量。因此，Künneth 直和项不是物理扇区本身。

现在专门取有限维二进制映射

$$
A:\mathbb F_2^{n_A}\longrightarrow\mathbb F_2^{m_A},
\qquad
B:\mathbb F_2^{n_B}\longrightarrow\mathbb F_2^{m_B}.
$$

定义

$$
k_A
=
\dim_{\mathbb F_2}\ker A,
\qquad
k_A^{\mathsf T}
=
\dim_{\mathbb F_2}\ker A^{\mathsf T},
$$

以及 $k_B,k_B^{\mathsf T}$。有限维秩—零化度关系给出

$$
\dim_{\mathbb F_2}\operatorname{coker}A
=
m_A-\operatorname{rank}A
=
\dim_{\mathbb F_2}\ker A^{\mathsf T}
=
k_A^{\mathsf T},
$$

对 $B$ 同理。

令

$$
K
=
\dim_{\mathbb F_2}H_1
$$

表示 HGP 编码的逻辑量子比特数。两个 Künneth 直和项的维数分别为

$$
k_Ak_B^{\mathsf T},
\qquad
k_A^{\mathsf T}k_B,
$$

所以

$$
\boxed{
K
=
k_Ak_B^{\mathsf T}
+
k_A^{\mathsf T}k_B
}.
$$

这条公式说明 HGP 的逻辑空间为什么有两个同调来源。HGP 校验矩阵的四个分块、CSS 对易与距离分析见 [[Hypergraph product code]]；它们不需要在这里重新推导。

## PID 与一般系数环

这里的 PID 指主理想整环（principal ideal domain）：它是每个理想都由一个元素生成的整环。

离开域以后，比较映射仍然可以按

$$
[c]\otimes[d]\longmapsto[c\otimes d]
$$

定义，但它不再自动是同构。“系数不是域”只表示域上的定理失去自动保证，并不表示每个非域实例都会失败。

需要区分三个层次：

1. 在 PID 上，比较映射进入一个自然短正合列，右端的修正量将在下一小节定义；
2. 在一般交换环上，不能期待单个直和公式，而要逐步追踪候选项、相消关系以及最后的拼接方式；
3. 对具体提升积码，逻辑量子比特数可以直接由展开后的二进制校验矩阵秩计算。

### 主理想整环：比较映射为何不一定满射

整数环 $\mathbb Z$ 是 PID 的标准例子。

一个 $R$-模 $F$ 称为平坦模（flat module），若张量运算

$$
F\otimes_R-
$$

保持短正合列。自由模一定平坦。

$\operatorname{Tor}_1^R(M,N)$ 是张量积不保持正合性的第一阶修正量。可以先取 $M$ 的自由分解

$$
0\longrightarrow F_1
\xrightarrow{u}
F_0
\longrightarrow M
\longrightarrow0,
$$

再由

$$
\operatorname{Tor}_1^R(M,N)
=
\ker(u\otimes\operatorname{id}_N)
$$

计算；换用另一份自由分解会得到自然同构的结果。这个定义说明：$\operatorname{Tor}_1$ 记录原来单射的 $u$ 在张量后可能出现的新核。

设 $R$ 是 PID，$C,D$ 是有界 $R$-链复形，并假设至少一个因子逐项平坦，即该因子的每个链模都是平坦模。要求两个因子都逐项自由是更强、但常用而安全的充分条件。

在这些假设下，[May 的 Chapter 17](https://math.uchicago.edu/~may/CONCISE/ConciseRevised.pdf) 对每个 $n$ 给出自然短正合列

$$
0
\longrightarrow
\bigoplus_{p+q=n}
H_p(C)\otimes_RH_q(D)
\xrightarrow{\ \kappa_n\ }
H_n(C\otimes_RD)
\xrightarrow{\ \tau_n\ }
\bigoplus_{p+q=n-1}
\operatorname{Tor}_1^R
\bigl(H_p(C),H_q(D)\bigr)
\longrightarrow
0.
$$

三个位置及两张箭头的意义是：

- 比较映射 $\kappa_n$ 是单射；
- 右侧映射 $\tau_n$ 是满射；
- 中间位置的正合性给出

  $$
  \operatorname{im}\kappa_n
  =
  \ker\tau_n,
  $$

  因而右端正是 $\kappa_n$ 的 cokernel，精确测量比较映射离满射还差多少；
- $\operatorname{Tor}_1$ 项的指标条件是 $p+q=n-1$，不是 $p+q=n$。

这个短正合列总能分裂，因此对每个固定对象，抽象地存在某个模同构

$$
H_n(C\otimes_RD)
\cong
\left(
\bigoplus_{p+q=n}
H_p(C)\otimes_RH_q(D)
\right)
\oplus
\left(
\bigoplus_{p+q=n-1}
\operatorname{Tor}_1^R(H_p(C),H_q(D))
\right).
$$

但是分裂一般不自然：没有一个对所有链映射都相容的首选方式，把右端的每个 $\operatorname{Tor}_1$ 类提升回中间项。因此，自然结论是短正合列，不是上面这个依赖选择的直和分解。

若 degree $n$ 所涉及的全部 $\operatorname{Tor}_1$ 都为零，则 $\kappa_n$ 恢复为同构。特别地，对每个满足 $p+q=n-1$ 的配对，只要 $H_p(C)$ 与 $H_q(D)$ 至少有一项平坦，相应的 $\operatorname{Tor}_1$ 就消失；这是充分条件，不是必要条件。域是特殊情形，因为域上的所有模都平坦。

### 一般交换环：先校正计算目标，再逐页计算

> [!note] 选读层
> 只需要 HGP 公式或具体提升积码（lifted-product, LP）的二进制参数时，可以先跳到“一个直接计算的失败例子”或“LP 的安全接口”。本小节解释一般环上为什么候选修正项还要继续经历相消与拼接，不能直接当作直和公式。

设 $R$ 是一般交换环，$C,D$ 是有界 $R$-链复形。

普通张量积的第一个困难是：把一个复形换成准同构的复形后，张量积的同调可能改变。链映射称为准同构，是指它在每个 degree 都诱导同调同构。

若一个复形 $A$ 在所有 degree 上的同调都为零，就称 $A$ 为无同调复形（acyclic complex）。一个复形 $P$ 称为 K-flat，若对任意这样的 $A$，乘积复形

$$
P\otimes_RA
$$

仍然无同调。这个条件保证 $P\otimes_R-$ 把准同构送到准同构。

导出张量积（derived tensor product）记作

$$
C\otimes_R^{\mathbf L}D.
$$

它的构造是：把至少一个因子用 K-flat 复形作准同构替换，再取普通张量积。不同 K-flat 替换在导出意义下给出同构对象，因此所得同调不依赖这次替换。

若 $C$ 或 $D$ 本身已经 K-flat，则普通乘积

$$
C\otimes_RD
$$

就代表导出张量积。对本文的有界复形而言，逐项平坦，尤其逐项自由，是 K-flat 的安全充分条件。

但 K-flat 只回答“普通张量积是否算到了正确的导出张量积”，不回答后面的逐页计算是否在第二页停止。即使 $C,D$ 都有界且逐项自由，高阶 $\operatorname{Tor}$、后续微分以及最终各部分怎样拼成目标同调的问题仍可能存在。

一般的 $\operatorname{Tor}_s^R(M,N)$ 由自由或投射分解在张量后的第 $s$ 个同调计算；其中

$$
\operatorname{Tor}_0^R(M,N)
=
M\otimes_RN,
$$

而 $s>0$ 的项记录更高阶的非正合性。

把候选项排列成双分次的“页”，再用微分从一页取同调得到下一页，这种逐页更新的计算工具称为谱序列（spectral sequence）。[The Stacks Project, Tag 0H7Z](https://stacks.math.columbia.edu/tag/0H7Z) 给出有界 Künneth 谱序列。它采用上同调指标，其 $E^2$ 页与收敛目标写作

$$
E_2^{a,b}
=
\bigoplus_{i+j=b}
\operatorname{Tor}_{-a}^R
\bigl(H^i(C^\bullet),H^j(D^\bullet)\bigr)
\Longrightarrow
H^{a+b}
\bigl(C^\bullet\otimes_R^{\mathbf L}D^\bullet\bigr).
$$

为了回到本文的降次数 convention，把同一复形重新编号为 $C^i=C_{-i}$、$D^j=D_{-j}$，再令

$$
p=-i,
\qquad
q=-j,
\qquad
s=-a,
\qquad
t=-b.
$$

于是 $H_p(C)=H^{-p}(C^\bullet)$，并得到同调版本：

$$
\boxed{
E^2_{s,t}
=
\bigoplus_{p+q=t}
\operatorname{Tor}_s^R
\bigl(H_p(C),H_q(D)\bigr)
\Longrightarrow
H_{s+t}
\bigl(C\otimes_R^{\mathbf L}D\bigr)
}.
$$

这里 $s\geq0$ 是 $\operatorname{Tor}$ 次数，$t=p+q$ 是两个因子同调 degree 之和。Stacks 的上同调微分从 $(a,b)$ 指向 $(a+r,b-r+1)$；按上面的重编号，它变成

$$
d_r:
E^r_{s,t}
\longrightarrow
E^r_{s-r,t+r-1}.
$$

这个微分把总次数 $s+t$ 降低 $1$，与本文的链复形 convention 一致。

谱序列不是一张静态表。每一页 $(E^r,d_r)$ 都是一个带微分的双分次对象，下一页就是这一页的同调：

$$
\boxed{
E^{r+1}_{s,t}
=
\frac{
\ker\bigl(
d_r:E^r_{s,t}\to E^r_{s-r,t+r-1}
\bigr)
}{
\operatorname{im}\bigl(
d_r:E^r_{s+r,t-r+1}\to E^r_{s,t}
\bigr)
}
}.
$$

所以一个 $E^2$ 项可能被后续微分送走，也可能因为它是另一项的像而在下一页消失。特别地，不能把所有高阶 $\operatorname{Tor}$ 项一看到就当成乘积同调中的额外直和类。

当谱序列稳定到 $E^\infty$ 时，还没有自动得到目标同调的直和分解。对固定的总次数 $n$，目标

$$
H_n
=
H_n(C\otimes_R^{\mathbf L}D)
$$

带有一个有限滤过

$$
0=F_{-1}H_n
\subseteq
F_0H_n
\subseteq
F_1H_n
\subseteq
\cdots
\subseteq
F_mH_n
=
H_n,
$$

使得

$$
F_sH_n/F_{s-1}H_n
\cong
E^\infty_{s,n-s}.
$$

把相邻层的商并列起来，得到伴随分次（associated graded object）

$$
\operatorname{gr}H_n
=
\bigoplus_s
F_sH_n/F_{s-1}H_n
\cong
\bigoplus_s
E^\infty_{s,n-s}.
$$

知道这些商以后，仍要决定它们怎样拼成 $H_n$。这个重建问题称为扩张问题（extension problem）。滤过未必分裂；即使分裂，也未必有自然的分裂。因此 $E^\infty$ 通常不能直接改写成目标同调的首选直和。

一般环上的三个检查点现在可以准确表述为：

1. **导出目标：** 若没有 K-flat 条件，谱序列收敛到 $H(C\otimes_R^{\mathbf L}D)$，不能自动改成 $H(C\otimes_RD)$；
2. **逐页同调：** $E^2$ 上的高阶 $\operatorname{Tor}$ 可能被后续 $d_r$ 改变；
3. **扩张重建：** $E^\infty$ 只给出滤过的相邻商，不自动给出自然直和。

在域上，所有高阶 $\operatorname{Tor}$ 都消失，谱序列只剩 $s=0$ 一行，因此回到前面的自然比较同构。PID 上则由更专门的定理得到只有 $\operatorname{Tor}_1$ 的自然短正合列。

### 一个直接计算的失败例子

这是本文中的直接计算：下面不借助谱序列，而是从链群、边界、核与像直接算出比较映射。

令

$$
R_2
=
\mathbb F_2[x]/\langle x^2-1\rangle.
$$

设

$$
\varepsilon=x+1.
$$

由于在 $\mathbb F_2$ 上

$$
x^2-1=(x+1)^2,
$$

有

$$
R_2
\cong
\mathbb F_2[\varepsilon]/\langle\varepsilon^2\rangle.
$$

所以 $\varepsilon\neq0$ 但 $\varepsilon^2=0$。取两个相同的二项自由复形

$$
C=D=
\left(
0\longrightarrow R_2
\xrightarrow{\ \varepsilon\ }
R_2
\longrightarrow0
\right),
$$

非零项位于 degree $1,0$，边界是乘以 $\varepsilon$。

任意元素可唯一写成

$$
u=a+b\varepsilon,
\qquad
a,b\in\mathbb F_2,
$$

而

$$
\varepsilon u=a\varepsilon.
$$

因此

$$
H_1(C)
=
\ker(\varepsilon)
=
(\varepsilon),
$$

$$
H_0(C)
=
R_2/\langle\varepsilon\rangle,
$$

对 $D$ 同理。作为 $R_2$-模，

$$
(\varepsilon)
\cong
R_2/\langle\varepsilon\rangle
\cong
\mathbb F_2.
$$

并且

$$
\bigl(R_2/\langle\varepsilon\rangle\bigr)
\otimes_{R_2}
\bigl(R_2/\langle\varepsilon\rangle\bigr)
\cong
R_2/\langle\varepsilon\rangle.
$$

所以 $\kappa_1$ 的源

$$
H_1(C)\otimes_{R_2}H_0(D)
\oplus
H_0(C)\otimes_{R_2}H_1(D)
$$

作为 $\mathbb F_2$-向量空间是二维的。

按

$$
(C_1\otimes_{R_2}D_0)
\oplus
(C_0\otimes_{R_2}D_1)
$$

排列 degree-$1$ 项，并使用

$$
R_2\otimes_{R_2}R_2\cong R_2,
$$

乘积复形的相关部分是

$$
R_2
\xrightarrow{\partial_2}
R_2^2
\xrightarrow{\partial_1}
R_2,
$$

其中

$$
\partial_2(r)
=
(\varepsilon r,\varepsilon r),
$$

$$
\partial_1(a,b)
=
\varepsilon(a+b).
$$

以 $1,\varepsilon$ 为 $R_2$ 的 $\mathbb F_2$-基，直接得到

$$
\ker\partial_1
=
\operatorname{span}_{\mathbb F_2}
\{
(1,1),
(\varepsilon,0),
(0,\varepsilon)
\},
$$

$$
\operatorname{im}\partial_2
=
\operatorname{span}_{\mathbb F_2}
\{
(\varepsilon,\varepsilon)
\}.
$$

因此

$$
\dim_{\mathbb F_2}
H_1(C\otimes_{R_2}D)
=
3-1
=
2.
$$

源与目标的二进制维数都等于 $2$，但比较映射的秩只有 $1$。确切地说，用 $\overline{1}$ 表示 $1$ 在 $R_2/\langle\varepsilon\rangle$ 中的商类。源的两个生成元

$$
[\varepsilon]\otimes\overline{1},
\qquad
\overline{1}\otimes[\varepsilon]
$$

分别映到

$$
[(\varepsilon,0)],
\qquad
[(0,\varepsilon)].
$$

这两个目标类都非零，因为唯一的非零 boundary 方向由 $(\varepsilon,\varepsilon)$ 张成；但

$$
(\varepsilon,0)+(0,\varepsilon)
=
(\varepsilon,\varepsilon)
=
\partial_2(1),
$$

所以

$$
[(\varepsilon,0)]
=
[(0,\varepsilon)].
$$

于是两个不同的源方向在目标中发生一次线性关系，$\kappa_1$ 不单射。

另一方面，

$$
[(1,1)]
$$

不是 boundary，因为 $\operatorname{im}\partial_2$ 中每个向量的两个常数项都为零。它也与 $[(\varepsilon,0)]$ 线性无关：任何含有 $(1,1)$ 的非零线性组合仍保留常数项，不可能落入 $\operatorname{im}\partial_2$。比较映射的像只由 $[(\varepsilon,0)]$ 张成，所以 $[(1,1)]$ 没有原像，$\kappa_1$ 也不满射。总结为

$$
\boxed{
\dim_{\mathbb F_2}
\bigl(\kappa_1\text{ 的定义域}\bigr)
=
\dim_{\mathbb F_2}
\bigl(\kappa_1\text{ 的目标}\bigr)
=
2,
\qquad
\operatorname{rank}_{\mathbb F_2}\kappa_1
=
1
}.
$$

这里 $R_2$ 有零因子，不是整环，因此不是 PID。这个例子证明域上的直和公式不能无条件搬到 $R_2$；它不证明所有非域系数、所有循环环或所有环系数乘积都会失败。

### 提升积码（lifted-product, LP）的安全接口

LP 常使用循环系数环

$$
R_\ell
=
\mathbb F_2[x]/\langle x^\ell-1\rangle.
$$

这类环不能自动当作域或 PID。LP 的标准输入是有界且逐项自由的链复形，因此这些输入是 K-flat，普通张量积确实代表导出张量积；但这仍然不保证 Künneth 谱序列在 $E^2$ 页退化，也不保证环上同调由两个 HGP 型直和项自然分解。

因此，逐项自由虽然已经解决了 K-flat 条件，但在没有另外证明谱序列退化和扩张分裂之前，仍不能把域上的

$$
K
=
k_Ak_B^{\mathsf T}
+
k_A^{\mathsf T}k_B
$$

当作一般 LP 的无条件维数公式。

具体 LP 实例有一个不依赖这类环上退化假设的接口。先按 [[Lifted product code]] 的规则把环值边界展开成共享同一组 $N$ 个二进制列的 CSS 校验矩阵

$$
H_X,
\qquad
H_Z.
$$

这里 $N$ 是展开后的物理量子比特数。只要已经验证 CSS 对易条件

$$
H_XH_Z^{\mathsf T}=0,
$$

编码逻辑量子比特数就由二进制秩直接给出：

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

这条秩公式是有限实例中可直接执行的安全结论。它不要求先把环上乘积同调写成 Künneth 直和，也不会把 $E^2$ 页的候选项误当成最终逻辑类。

若系数环非交换，还必须区分右 $R$-模与左 $R$-模，并检查两个因子作用的次序与相容性。那些侧别条件属于 LP 构造本身，见 [[Lifted product code]]；本文只负责说明为什么环上的 Künneth 直和不能在未核对假设时自动使用。

## 如何判断当前问题属于哪一层

面对一个具体乘积复形，可以按下面的顺序判断：

1. **系数是域，复形有界且有限维：** 直接使用自然同构

   $$
   H_n(C\otimes_kD)
   \cong
   \bigoplus_{p+q=n}
   H_p(C)\otimes_kH_q(D).
   $$

2. **系数是 PID，至少一个因子逐项平坦：** 使用带 $\operatorname{Tor}_1$ 的自然短正合列；只有在相应 $\operatorname{Tor}_1$ 消失时，比较映射才恢复为同构。

3. **系数是一般交换环：** 先判断普通张量积是否代表导出张量积，再使用 Künneth 谱序列逐页计算；$E^\infty$ 之后还要处理滤过与扩张。

4. **目标是具体 LP 的逻辑量子比特数：** 在没有额外退化定理时，展开到二进制 $H_X,H_Z$，使用秩公式计算 $K$。

这四层回答的是同一个中心问题：比较映射 $\kappa_n$ 在什么条件下能够把“先取同调再作张量积”与“先作张量积再取同调”连接起来。域上它是自然同构；离开域后，$\operatorname{Tor}$、后续微分和扩张问题分别记录这条简单路线可能失效的位置。

## 来源与延伸

- [[Chain complex 与 cochain complex]]：闭链、边界、同调以及 chain/cochain convention。
- [[Cochain complex 的 tensor product]]：总次数、直和与 Koszul 符号；本文使用其降次数链版本。
- [[二进制空间性质]]：向量子空间的非唯一直和补空间。
- [[Hypergraph product code]]：HGP 的三项链角色、物理扇区、逻辑支撑商空间与校验矩阵。
- [[Lifted product code]]：LP 的环值输入、左右模边界、二进制展开与有限实例秩公式。
- J. P. May, [*A Concise Course in Algebraic Topology*, Chapter 17](https://math.uchicago.edu/~may/CONCISE/ConciseRevised.pdf)：PID 上的自然 Künneth 短正合列、非自然分裂与域上推论。
- [The Stacks Project, Tag 06XY](https://stacks.math.columbia.edu/tag/06XY)：K-flat 复形与导出张量积。
- [The Stacks Project, Tag 0H7Z](https://stacks.math.columbia.edu/tag/0H7Z)：一般环上的有界 Künneth 谱序列。
