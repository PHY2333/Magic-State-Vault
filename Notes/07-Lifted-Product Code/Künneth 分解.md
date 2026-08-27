Künneth 分解描述 tensor-product chain complex 的同调如何由两个因子的同调组成。[[Cochain complex 的 tensor product]] 已经给出升 degree 的 cochain 版本；以下采用 [[Hypergraph product code]] 的 chain convention，先构造从两个因子的同调到乘积复形同调的映射，再证明它在域上是同构，并把 degree-$1$ 分解用于 HGP 的逻辑空间。一般系数环下这个映射不再自动成为同构，这一边界决定同一公式能否用于 [[Lifted product code]]。

### 链复形的乘积与比较映射

设 $k$ 是域，$C_\bullet,D_\bullet$ 是 $k$ 上的有界有限维链复形；有界表示只有有限多个 degree 的链群非零。它们的 tensor-product chain complex 按 total degree 分层：

$$
(C\otimes_kD)_n
=
\bigoplus_{p+q=n}C_p\otimes_kD_q.
$$

对 $c\in C_p$ 与 $d\in D_q$，乘积边界为

$$
\partial(c\otimes d)
=
\partial_Cc\otimes d
+(-1)^p c\otimes\partial_Dd.
$$

符号由第一个因子的 degree $p$ 决定；只有在 $k=\mathbb F_2$ 时，$-1=1$ 才能把它省略。

记

$$
Z_p(C)=\ker\bigl(\partial_p^C:C_p\to C_{p-1}\bigr),
\qquad
B_p(C)=\operatorname{im}\bigl(\partial_{p+1}^C:C_{p+1}\to C_p\bigr),
\qquad
H_p(C)=Z_p(C)/B_p(C),
$$

若 $c\in Z_p(C)$、$d\in Z_q(D)$，则

$$
\partial(c\otimes d)=0,
$$

所以 $c\otimes d$ 是 total degree $p+q$ 的 cycle。由此得到候选映射

$$
\kappa_{p,q}:
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_{p+q}(C\otimes_kD),
\qquad
[c]\otimes[d]\longmapsto[c\otimes d].
$$

它必须与两个商空间中的代表元选择无关。若 $x\in C_{p+1}$，用 $c+\partial_Cx$ 替换 $c$，新增项满足

$$
(\partial_Cx)\otimes d
=
\partial(x\otimes d),
$$

因为 $\partial_Dd=0$。若 $y\in D_{q+1}$，用 $d+\partial_Dy$ 替换 $d$，则

$$
c\otimes(\partial_Dy)
=
(-1)^p\partial(c\otimes y),
$$

因为 $\partial_Cc=0$。两种替换都只给 $C\otimes_kD$ 增加一个 boundary，因此 $[c\otimes d]$ 只依赖 $[c]$ 和 $[d]$。双线性使这些映射可以在 total degree $n$ 上合成

$$
\kappa_n:
\bigoplus_{p+q=n}H_p(C)\otimes_kH_q(D)
\longrightarrow
H_n(C\otimes_kD).
$$

$\kappa_n$ 的两端对应两种运算顺序：定义域先分别取 $C,D$ 的同调，再将同调群作 tensor product，并收集 $p+q=n$ 的分量；陪域则先构造乘积链复形 $C\otimes_kD$，再取它的 $n$ 阶同调。映射 $\kappa_n$ 把第一种顺序得到的 $[c]\otimes[d]$ 送到第二种顺序中的 $[c\otimes d]$，所以称为 Künneth 比较映射。前面的代表元计算已经证明它是一个不随代表元选择改变的线性映射；下面还要证明它在域上是同构。

### 域上的同调代表元分裂

固定 $C_\bullet$。因为 $k$ 是域，$B_p(C)\subseteq Z_p(C)$ 是向量子空间的包含关系，可以逐 degree 为 $B_p(C)$ 选择一个 [[二进制空间性质#直和补空间|直和补空间]] $\widetilde H_p(C)$：

$$
Z_p(C)=B_p(C)\oplus\widetilde H_p(C).
$$

因此每个 $z\in Z_p(C)$ 都能唯一写成

$$
z=b+h,
\qquad
b\in B_p(C),\ h\in\widetilde H_p(C).
$$

定义商映射

$$
\pi_p:
Z_p(C)
\longrightarrow
H_p(C)=Z_p(C)/B_p(C),
\qquad
z\longmapsto[z].
$$

把 $\pi_p$ 的定义域从 $Z_p(C)$ 缩小到 $\widetilde H_p(C)$，得到

$$
\left.\pi_p\right|_{\widetilde H_p(C)}:
\widetilde H_p(C)
\longrightarrow
H_p(C),
\qquad
h\longmapsto[h].
$$

这个映射是满射。任取 $[z]\in H_p(C)$，利用上面的唯一分解写成 $z=b+h$。因为 $b\in B_p(C)$ 在商空间中代表零，

$$
[z]=[b+h]=[h],
$$

所以每个同调类都有一个来自 $\widetilde H_p(C)$ 的原像。它也是单射。若 $h\in\widetilde H_p(C)$ 且 $[h]=0$，则 $h\in B_p(C)$，从而

$$
h\in B_p(C)\cap\widetilde H_p(C)=\{0\}.
$$

因此

$$
\rho_p
:=
\left.\pi_p\right|_{\widetilde H_p(C)}:
\widetilde H_p(C)
\xrightarrow{\sim}
H_p(C).
$$

这个同构表示：选定 $\widetilde H_p(C)$ 后，每个同调类都在该子空间中有唯一的 cycle 代表元。商空间 $H_p(C)$ 和商映射 $\pi_p$ 只由 $B_p(C)\subseteq Z_p(C)$ 决定，没有使用补空间。但链复形本身一般不会指定唯一的 $\widetilde H_p(C)$。若另选

$$
Z_p(C)=B_p(C)\oplus\widetilde H'_p(C),
$$

那么同一个同调类可能分别由 $h\in\widetilde H_p(C)$ 与 $h'\in\widetilde H'_p(C)$ 代表。因为 $[h]=[h']$，两个代表元满足

$$
h-h'\in B_p(C).
$$

所以随补空间改变的是代表元子空间 $\widetilde H_p(C)$，以及从 $H_p(C)$ 中每个类选出 cycle 代表元的逆映射

$$
\rho_p^{-1}:
H_p(C)
\longrightarrow
\widetilde H_p(C)
\subseteq Z_p(C),
$$

而不是 $H_p(C)$ 或 $\pi_p$ 本身。这些代表元只用于下面构造链级分裂。

接着为另一个包含关系 $Z_p(C)\subseteq C_p$ 选择补空间 $L_p(C)$：

$$
C_p=Z_p(C)\oplus L_p(C).
$$

边界映射在 $L_p(C)$ 上限制为

$$
\left.\partial_p\right|_{L_p(C)}:
L_p(C)\longrightarrow B_{p-1}(C).
$$

这个限制是单射。若 $\ell\in L_p(C)$ 且 $\partial_p\ell=0$，则 $\ell\in Z_p(C)\cap L_p(C)=0$。它也是满射：对任意 $b\in B_{p-1}(C)$，取 $x\in C_p$ 使 $\partial_px=b$，再写成 $x=z+\ell$，其中 $z\in Z_p(C)$、$\ell\in L_p(C)$，便有

$$
b=\partial_px=\partial_p\ell.
$$

因此

$$
\delta_p
:=
\left.\partial_p\right|_{L_p(C)}:
L_p(C)\xrightarrow{\sim}B_{p-1}(C).
$$

令 $\widetilde{\mathcal H}(C)$ 是以 $\widetilde H_p(C)$ 为 degree-$p$ 分量、边界恒为零的链复形。若把 $H_\bullet(C)$ 也看成 degree-$p$ 分量为 $H_p(C)$、边界恒为零的链复形，那么各 degree 上的 $\rho_p$ 组合成链复形同构

$$
\rho_\bullet:
\widetilde{\mathcal H}(C)_\bullet
\xrightarrow{\sim}
\bigl(H_\bullet(C),0\bigr).
$$

再令

$$
Q(C)_p=B_p(C)\oplus L_p(C).
$$

边界映射在 $Q(C)$ 上的限制记为

$$
d_p^Q:
Q(C)_p
\longrightarrow
Q(C)_{p-1}.
$$

按定义域 $B_p(C)\oplus L_p(C)$ 和陪域 $B_{p-1}(C)\oplus L_{p-1}(C)$ 排列，它的分块矩阵为

$$
d_p^Q
=
\begin{bmatrix}
0&\delta_p
\\
0&0
\end{bmatrix},
\qquad
d_p^Q(b,\ell)=(\delta_p\ell,0).
$$

矩阵的列对应定义域，行对应陪域。第一列为零，因为 $B_p(C)\subseteq Z_p(C)$；唯一的非零块就是先前构造的同构 $\delta_p:L_p(C)\to B_{p-1}(C)$。因此 $\partial_pQ(C)_p\subseteq Q(C)_{p-1}$，$Q(C)$ 是链子复形。

两次补空间分解在每个 degree 上给出

$$
C_p
=
B_p(C)\oplus\widetilde H_p(C)\oplus L_p(C)
=
\widetilde H_p(C)\oplus Q(C)_p.
$$

边界在这两个分量上的作用可画成

$$
\begin{array}{ccccc}
C_p
&=&
\widetilde H_p(C)
&\oplus&
Q(C)_p
\\
\downarrow{\scriptstyle\partial_p}
&&
\downarrow{\scriptstyle 0}
&&
\downarrow{\scriptstyle d_p^Q}
\\
C_{p-1}
&=&
\widetilde H_{p-1}(C)
&\oplus&
Q(C)_{p-1}.
\end{array}
$$

中间的零箭头来自 $\widetilde H_p(C)\subseteq Z_p(C)$；右边的箭头内部只有 $L_p(C)\xrightarrow{\delta_p}B_{p-1}(C)$ 这一个非零分块。因此边界分别保持 $\widetilde{\mathcal H}(C)$ 与 $Q(C)$，上述逐 degree 直和升级为链复形的直和分解：

$$
C_\bullet
=
\widetilde{\mathcal H}(C)_\bullet
\oplus
Q(C)_\bullet
$$

是链复形的直和分解。

### 可缩部分的 tensor product

定义 degree $+1$ 的线性映射

$$
s_p:Q(C)_p\longrightarrow Q(C)_{p+1},
$$

$$
s_p(b+\ell)
=
\delta_{p+1}^{-1}(b),
\qquad
b\in B_p(C),\ \ell\in L_p(C).
$$

它把 $B_p(C)$ 送回唯一的 $L_{p+1}(C)$ 原像，并在 $L_p(C)$ 上取零。于是

$$
\partial_{p+1}s_p(b+\ell)=b,
\qquad
s_{p-1}\partial_p(b+\ell)=\ell,
$$

从而

$$
\partial s+s\partial=\operatorname{id}_{Q(C)}.
$$

满足这个等式的 $s$ 称为 contracting homotopy；该等式直接说明 $Q(C)$ 中的每个 cycle 都是 boundary。只有 $Q(C)$ 可缩，整个 $C$ 一般不可缩。

若 $u\in Q(C)_p$、$d\in D_r$，在 $Q(C)\otimes_kD$ 上定义

$$
S_C(u\otimes d)=s_C(u)\otimes d.
$$

乘积边界中的交叉项系数为 $(-1)^{p+1}$ 与 $(-1)^p$，两者相加为零，因此

$$
\begin{aligned}
(\partial S_C+S_C\partial)(u\otimes d)
&=
(\partial s_C+s_C\partial)u\otimes d
\\
&\quad+
\bigl((-1)^{p+1}+(-1)^p\bigr)s_C(u)\otimes\partial_Dd
\\
&=u\otimes d.
\end{aligned}
$$

所以 $Q(C)\otimes_kD$ 仍然可缩。若可缩部分位于第二个因子，符号必须随第一个因子的 degree 改变。对固定 degree 的 $h\in\widetilde H_p(C)$ 与 $q\in Q(D)$，定义

$$
S_D(h\otimes q)=(-1)^p h\otimes s_D(q).
$$

由于 $\partial h=0$，

$$
\partial S_D(h\otimes q)=h\otimes\partial s_D(q),
$$

$$
S_D\partial(h\otimes q)=h\otimes s_D\partial(q),
$$

故

$$
\partial S_D+S_D\partial
=
\operatorname{id}_{\widetilde{\mathcal H}(C)\otimes_kQ(D)}.
$$

现在把两个因子的链级分裂代入 tensor product：

$$
\begin{aligned}
C\otimes_kD
={}&
\widetilde{\mathcal H}(C)\otimes_k\widetilde{\mathcal H}(D)
\\
&\oplus
\widetilde{\mathcal H}(C)\otimes_kQ(D)
\\
&\oplus
Q(C)\otimes_k\widetilde{\mathcal H}(D)
\\
&\oplus
Q(C)\otimes_kQ(D).
\end{aligned}
$$

后三项都含有一个可缩因子。第二项由 $S_D$ 收缩，第三、四项由 $S_C$ 收缩，因此它们的同调为零。第一项的两个因子都具有零边界，乘积边界也为零。

### Künneth 分解

乘积复形的同调只剩 $\widetilde{\mathcal H}(C)\otimes_k\widetilde{\mathcal H}(D)$。它的 total degree-$n$ 分量是

$$
\bigoplus_{p+q=n}
\widetilde H_p(C)\otimes_k\widetilde H_q(D).
$$

利用 $\widetilde H_p(C)\cong H_p(C)$ 与 $\widetilde H_q(D)\cong H_q(D)$，得到

$$
\boxed{
H_n(C\otimes_kD)
\cong
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D)
}.
$$

上述链级直和与 contracting homotopy 依赖补空间选择，但存活分量进入乘积复形的映射正是先前定义的 $\kappa_n$。因此补空间只用于证明这个已经定义好的 $\kappa_n$ 可逆；$\kappa_n$ 的定义本身没有使用任何补空间。

### 链映射下的自然性

固定 $C,D$ 时，域上分裂已经证明比较映射是同构。若 $C,D$ 分别由链映射送到 $C',D'$，还需检查先传递同调类与先使用比较映射是否得到同一结果。

设 $C',D'$ 也是 $k$ 上的链复形，degree-$0$ 链映射 $f:C\to C'$ 与 $g:D\to D'$ 的分量为

$$
f_p:C_p\to C'_p,
\qquad
g_q:D_q\to D'_q,
$$

它们满足

$$
\partial_p^{C'}f_p=f_{p-1}\partial_p^C,
\qquad
\partial_q^{D'}g_q=g_{q-1}\partial_q^D.
$$

若 $c\in Z_p(C)$，则

$$
\partial_p^{C'}f_p(c)
=
f_{p-1}\partial_p^C(c)
=0,
$$

所以 $f_p(c)\in Z_p(C')$。若 $c\in B_p(C)$，写成 $c=\partial_{p+1}^Cx$，则

$$
f_p(c)
=
f_p\partial_{p+1}^C(x)
=
\partial_{p+1}^{C'}f_{p+1}(x)
\in B_p(C').
$$

因此 $f_p$ 把 cycle 送到 cycle，也把 boundary 送到 boundary；对 $g_q$ 的计算同理。于是它们诱导出同调上的映射

$$
H_p(f):H_p(C)\to H_p(C'),
\qquad
[c]\longmapsto[f_p(c)],
$$

$$
H_q(g):H_q(D)\to H_q(D'),
\qquad
[d]\longmapsto[g_q(d)].
$$

两个链映射还给出乘积复形之间的分次映射

$$
(f\otimes g)_n
=
\bigoplus_{p+q=n}f_p\otimes g_q,
$$

即

$$
(f\otimes g)(c\otimes d)=f_p(c)\otimes g_q(d),
\qquad c\in C_p,\ d\in D_q.
$$

它确实是链映射。对上述齐次元，

$$
\begin{aligned}
\partial^{C'\otimes D'}\bigl(f_p(c)\otimes g_q(d)\bigr)
&=
f_{p-1}(\partial_Cc)\otimes g_q(d)
+(-1)^pf_p(c)\otimes g_{q-1}(\partial_Dd)
\\
&=(f\otimes g)\partial^{C\otimes D}(c\otimes d).
\end{aligned}
$$

所以 $f\otimes g$ 诱导出

$$
H_n(f\otimes g):
H_n(C\otimes_kD)
\longrightarrow
H_n(C'\otimes_kD').
$$

用 $\kappa_n^{C,D}$ 与 $\kappa_n^{C',D'}$ 分别标记由两对复形构造的比较映射。

要求“先使用 $\kappa_n$ 合成乘积同调类，再沿 $f\otimes g$ 移动”与“先沿 $f,g$ 移动两个因子的同调类，再使用 $\kappa_n$ 合成”得到相同结果，就是要求以下等式成立：

$$
H_n(f\otimes g)\circ\kappa_n^{C,D}
=
\kappa_n^{C',D'}\circ
\bigoplus_{p+q=n}\bigl(H_p(f)\otimes H_q(g)\bigr).
$$

对 $p+q=n$ 与任意 $[c]\otimes[d]$，等式左边的路径是

$$
[c]\otimes[d]
\xrightarrow{\ \kappa_n^{C,D}\ }
[c\otimes d]
\xrightarrow{\ H_n(f\otimes g)\ }
[f_p(c)\otimes g_q(d)],
$$

右边的路径是

$$
[c]\otimes[d]
\xrightarrow{\ H_p(f)\otimes H_q(g)\ }
[f_p(c)]\otimes[g_q(d)]
\xrightarrow{\ \kappa_n^{C',D'}\ }
[f_p(c)\otimes g_q(d)].
$$

两条路径得到同一个同调类；纯张量张成每个直和分量，所以上述映射等式成立。这个交换关系就是 $\kappa_n$ 的自然性：它保证不同复形上的 Künneth 映射能沿链映射一致地传递，而不是一族彼此无关的同构。自然性不负责证明 $\kappa_n$ 可逆；前面的域上分裂才负责这一点。这里的交换计算本身没有使用 $k$ 是域；域条件只用于把自然的比较映射升级为自然同构。

### 二项复形与 HGP 逻辑空间

取两个二项链复形

$$
\mathcal A:\quad
0\longrightarrow A_1\xrightarrow{A}A_0\longrightarrow0,
$$

$$
\mathcal B:\quad
0\longrightarrow B_1\xrightarrow{B}B_0\longrightarrow0.
$$

在 degree $1$ 处没有来自更高 degree 的 boundary，所以

$$
H_1(\mathcal A)=\ker A.
$$

在 degree $0$ 处，所有元素都被后面的零映射送到零，而来自 degree $1$ 的 boundaries 是 $\operatorname{im}A$，所以

$$
H_0(\mathcal A)
=
A_0/\operatorname{im}A
=
\operatorname{coker}A.
$$

对 $\mathcal B$ 同理。Total degree $1$ 只有 $1=1+0$ 和 $1=0+1$ 两种分解，Künneth 同构给出

$$
\boxed{
H_1(\mathcal A\otimes_k\mathcal B)
\cong
\ker A\otimes_k\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes_k\ker B
}.
$$

第一项由 $A$ 方向的 cycle 与 $B$ 方向未被 boundary 覆盖的商类组成，第二项交换两个因子的作用。这是两个不同的同调扇区，而不是同一组代表元的两种写法。

在 [[Hypergraph product code#从两张经典校验矩阵开始]] 采用的 chain convention 中，

$$
H_1(\mathcal A\otimes\mathcal B)
=
\frac{\ker H_X}{\operatorname{im}H_Z^T}
$$

表示 logical $Z$ support classes；对偶 cochain complex 的 $H^1$ 表示 logical $X$ support classes。两者维数都等于 CSS 码的逻辑比特数 $K$。

现在令 $k=\mathbb F_2$，并取

$$
A:\mathbb F_2^{n_A}\longrightarrow\mathbb F_2^{m_A}.
$$

记

$$
k_A=\dim_{\mathbb F_2}\ker A,
\qquad
k_A^T=\dim_{\mathbb F_2}\ker A^T,
$$

并类似定义 $k_B,k_B^T$。有限维对偶给出

$$
(\operatorname{coker}A)^*\cong\ker A^T,
$$

因而

$$
\dim\operatorname{coker}A
=m_A-\operatorname{rank}A
=\dim\ker A^T.
$$

对两个 Künneth 扇区取维数，得到 HGP 的逻辑比特数公式

$$
\boxed{
K=k_Ak_B^T+k_A^Tk_B
}.
$$

### PID 与一般系数环

域上证明使用了两个事实：向量子空间包含关系可以选择直和补空间，tensor product 保持短正合列。对一般环上的模，这两点都可能失败。

先取主理想整环（principal ideal domain, PID）$R$，即 $R$ 的每个理想都由一个元素生成。若 $C,D$ 是有界且逐项自由的 $R$-链复形，Künneth 定理给出自然短正合列

$$
0
\longrightarrow
\bigoplus_{p+q=n}
H_p(C)\otimes_RH_q(D)
\xrightarrow{\ \kappa_n\ }
H_n(C\otimes_RD)
\longrightarrow
\bigoplus_{p+q=n-1}
\operatorname{Tor}_1^R(H_p(C),H_q(D))
\longrightarrow0.
$$

$\operatorname{Tor}_1^R(M,N)$ 衡量 tensor product 作用于模的短正合列时可能产生的额外核。平坦模是与它作 tensor product 后仍保持短正合列的模；若 $M$ 或 $N$ 是平坦模，$\operatorname{Tor}_1^R(M,N)$ 为零。上面的短正合列可以分裂，但分裂一般不自然。$R$ 为域时所有模都平坦，$\operatorname{Tor}_1$ 消失，便恢复前面的自然同构。

PID 公式不能直接推广到任意环。对交换环 $R$ 上的有界链复形，一般结论使用 derived tensor product。准同构是一个在每个 degree 上都诱导同调同构的链映射。K-flat 复形与任意无同调复形作 tensor product 后仍然无同调；这个条件保证 tensor product 保持所用的准同构。把一个因子替换为与它准同构的 K-flat 复形，再取 ordinary tensor product，所得准同构类记为

$$
C\otimes_R^{\mathbf L}D.
$$

若 $C,D$ 本身是有界自由复形，它们已经可以用于这一步，所以 ordinary tensor product 计算 derived tensor product。相关同调由 Künneth spectral sequence 组织：

$$
E^2_{s,t}
=
\bigoplus_{p+q=t}
\operatorname{Tor}_s^R(H_p(C),H_q(D))
\Longrightarrow
H_{s+t}(C\otimes_R^{\mathbf L}D).
$$

谱序列的下一页由当前页及其微分的同调得到，即 $E^{r+1}=H(E^r,d_r)$。稳定后的 $E^\infty$ 给出目标同调的一个滤过（filtration）

$$
0=F_{-1}H_n\subseteq F_0H_n\subseteq\cdots\subseteq H_n.
$$

伴随分次（associated graded）把相邻层之差并列保存：

$$
\operatorname{gr}H_n
:=
\bigoplus_sF_sH_n/F_{s-1}H_n
\cong
\bigoplus_sE^\infty_{s,n-s}.
$$

因此 $E^2$ 页上的高阶 $\operatorname{Tor}$ 还可能经过后续微分。各商空间 $F_sH_n/F_{s-1}H_n$ 重新组成 $H_n$ 时，相应短正合列也未必有典范分裂；这就是这里的 extension 问题。高阶 $\operatorname{Tor}$ 不能无条件读成目标同调的额外直和项。

循环 LP 常用

$$
R_\ell=\mathbb F_2[x]/(x^\ell-1).
$$

LP 的两个输入二项复形是有界自由 $R_\ell$-复形，所以 ordinary complex $C\otimes_{R_\ell}D$ 可以计算相应 derived tensor product；这不保证谱序列退化。另一方面，即使 $R_\ell$ 不是域，也不表示每个实例必有非零 $\operatorname{Tor}$：若每一对相关同调模中至少有一个是平坦模，高阶 $\operatorname{Tor}$ 仍会消失。即使它们消失，$R_\ell$-module tensor product 的二进制维数也不等于两个因子二进制维数的简单乘积。

所以一般 LP 实例不能无条件套用 $K=k_Ak_B^T+k_A^Tk_B$；应按 [[Lifted product code#二进制长度、行数、秩与 LDPC 条件]] 中展开后的二进制秩计算 $K$。非交换 group-algebra LP 还需要区分右模与左模，具体 convention 由 [[Lifted product code]] 承担。

### $\ell=2$ 的环系数反例

在 $\mathbb F_2$ 上，令 $\varepsilon=x+1$。因为

$$
x^2-1=(x+1)^2,
$$

所以

$$
R_2=\mathbb F_2[x]/(x^2-1)
\cong
\mathbb F_2[\varepsilon]/(\varepsilon^2).
$$

取两个相同的二项自由 $R_2$-复形

$$
C=D=\left(0\longrightarrow R_2\xrightarrow{\,\varepsilon\,}R_2\longrightarrow0\right),
$$

其中箭头表示乘以 $\varepsilon$。写 $u=a+b\varepsilon$，则 $\varepsilon u=a\varepsilon$，因此

$$
H_1(C)=\ker(\varepsilon)=(\varepsilon),
\qquad
H_0(C)=R_2/(\varepsilon),
$$

对 $D$ 也相同。两个模都同构于 $\mathbb F_2$，所以 $\kappa_1$ 的定义域

$$
H_1(C)\otimes_{R_2}H_0(D)
\oplus
H_0(C)\otimes_{R_2}H_1(D)
$$

具有两个 $\mathbb F_2$ 生成元。

按 $(C_1\otimes D_0)\oplus(C_0\otimes D_1)$ 排列中间项，特征 $2$ 使两个符号相同，乘积复形为

$$
R_2\xrightarrow{\partial_2}R_2^2\xrightarrow{\partial_1}R_2,
$$

$$
\partial_2(r)=(\varepsilon r,\varepsilon r),
\qquad
\partial_1(a,b)=\varepsilon(a+b).
$$

直接计算得到

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

所以

$$
\dim_{\mathbb F_2}H_1(C\otimes_{R_2}D)=3-1=2.
$$

$\kappa_1$ 的两个源生成元分别映到

$$
[(\varepsilon,0)],
\qquad
[(0,\varepsilon)].
$$

但

$$
(\varepsilon,0)+(0,\varepsilon)
=(\varepsilon,\varepsilon)
=\partial_2(1),
$$

所以这两个像代表同一个同调类；而 $[(1,1)]$ 不在 $\kappa_1$ 的像中。于是 $\kappa_1$ 的秩为 $1$，既非单射也非满射。

本例中比较映射的定义域与目标恰好都有二进制维数 $2$，失败发生在映射本身，而不是维数已经不同。它证明域上的 Künneth 直和不能无条件搬到 $R_2$，但不表示每个非域系数环或每个 LP 实例都会失败。

### 来源

- J. P. May, [*A Concise Course in Algebraic Topology*](https://math.uchicago.edu/~chicagotopology2/ConciseRevised.pdf), “The Künneth theorem”：PID 上的短正合列、非自然分裂与域上的自然同构。
- The Stacks Project, [*Derived tensor product*](https://stacks.math.columbia.edu/tag/06XY)：K-flat 复形与 derived tensor product。
- The Stacks Project, [*Künneth Spectral Sequence*](https://stacks.math.columbia.edu/tag/0H7Z)：有界复形的一般环 Künneth 谱序列。
