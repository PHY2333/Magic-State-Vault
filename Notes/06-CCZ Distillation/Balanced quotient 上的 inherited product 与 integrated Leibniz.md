令 $\widetilde B$ 是 ordinary tensor-product complex，设有限群 $H$ 通过 degree-preserving cochain automorphisms 作用在 $\widetilde B$ 上，并令

$$
B=\widetilde B_H
$$

是 coinvariant complex。这里先把 $H$ 当作任意有限群；balanced interfaces 只是产生这类群作用的一种方式。[[Balanced tensor product 与 coinvariant quotient]] 已经说明，在 Menon 三重 group-algebra product 中才具体取 $H=G^2$，而 $B$ 就是 module tensor product $C_a\otimes_RC_b\otimes_RC_c$。

[[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]] 则在 $\widetilde B$ 上给出 ordinary multilinear operation、product integral 与 integrated Leibniz。剩下的问题是：ordinary operation 怎样变成 $B$ 上的 operation，以及 descended integral 怎样与它共同保留 integrated Leibniz。

---
### Coinvariants 上的 operation

令 $M=(M^\bullet,\delta)$ 是域 $k$ 上的 cochain complex，并在每个 $M^p$ 中固定一组 basis $X^p$。这就是这里的 based cochain complex：based 只表示逐 degree 选定了线性 basis，不表示带有 basepoint，也不自动要求群作用保持这些 bases。

设有限群 $H$ 通过 degree-preserving cochain automorphisms 作用在 $M$ 上。具体地，对每个 $h\in H$ 和 degree $p$，都有可逆线性映射

$$
h_p:M^p\xrightarrow{\cong}M^p,
$$

并且

$$
e_p=\operatorname{id}_{M^p},
\qquad
(h_1h_2)_p=(h_1)_p\circ(h_2)_p,
$$

$$
\delta^p\circ h_p
=
h_{p+1}\circ\delta^p.
$$

满足这些条件的一族映射 $h_\bullet=(h_p)_p$ 称为 cochain automorphism：它是从整个 cochain complex $M$ 到自身的 cochain map，automorphism 强调每个 $h_p$ 都可逆，其逆映射由 $(h^{-1})_p$ 给出。映射 $h_p:M^p\to M^p$ 不改变 degree；单位元与复合公式给出 $H$ 的群作用；最后一式说明群作用与 coboundary 对易。若 $v\in M^p$，以下把 $h_p(v)$ 简写为 $hv$。

同一个 $H$-作用同时给出 coinvariant spaces 与 fixed subspaces。按照 [[Balanced tensor product 与 coinvariant quotient#Coinvariant quotient 上的 coboundary]]，degree $p$ 的 coinvariant relation subspace 与 quotient space 分别定义为

$$
W_H^p
:=
\operatorname{span}_k\{h_p(v)-v:h\in H,\ v\in M^p\},
$$

$$
(M_H)^p
:=
M^p/W_H^p,
\qquad
[v]_H:=v+W_H^p.
$$

若群作用与 coboundary 对易，则这些 quotient spaces 连同

$$
\delta_H^p([v]_H):=[\delta^pv]_H
$$

组成 coinvariant complex $M_H$。链接小节已经证明该公式不依赖 representative 的选择。

另一方面，在每个 degree 定义 fixed subspace

$$
(M^H)^p
:=
\{v\in M^p:h_p(v)=v,\ \forall h\in H\}.
$$

若 $v\in(M^H)^p$，则对每个 $h\in H$，

$$
h_{p+1}(\delta^pv)
=
\delta^p(h_pv)
=
\delta^pv.
$$

因此

$$
\delta^p\bigl((M^H)^p\bigr)
\subseteq
(M^H)^{p+1},
$$

所以这些 fixed subspaces 组成 $M$ 的 $H$-不变子复形（invariant subcomplex）$M^H$。

现在取一个 $m$-linear operation

$$
\mu:M^{\times m}\longrightarrow M
$$

并假设它关于共同 $H$-作用等变：

$$
\mu(hy_1,\ldots,hy_m)
=
h\mu(y_1,\ldots,y_m).
$$

若 $y_1,\ldots,y_m\in M^H$，则对每个 $h\in H$，

$$
h\mu(y_1,\ldots,y_m)
=
\mu(hy_1,\ldots,hy_m)
=
\mu(y_1,\ldots,y_m).
$$

因此 $\mu(y_1,\ldots,y_m)\in M^H$，也就是 $\mu$ 给出限制映射

$$
\left.\mu\right|_{(M^H)^{\times m}}
:
(M^H)^{\times m}
\longrightarrow
M^H.
$$

这里只说明 $\mu$ 把 $m$ 个 invariant elements 送到 $M^H$；它不表示 $\mu$ 与 coboundary 对易。

接着考虑直接把 representatives 代入 $\mu$ 的候选公式

$$
\mu_H^{\mathrm{dir}}([y_1]_H,\ldots,[y_m]_H)
\stackrel{?}{=}
[\mu(y_1,\ldots,y_m)]_H
$$

是否良定义，取决于改变每个 argument 的 representative 后所得 class 是否不变。具体地，对每个 argument 位置 $j$、每个 $h\in H$ 以及任意 $y_1,\ldots,y_m\in M$，必须有

$$
\left[
\mu(y_1,\ldots,hy_j,\ldots,y_m)
\right]_H
=
\left[
\mu(y_1,\ldots,y_j,\ldots,y_m)
\right]_H.
\tag{*}
$$

这是必要条件，因为 $[hy_j]_H=[y_j]_H$；它也是充分条件，因为每个 degree 的 relation subspace $W_H^p$ 都由 $hy-y$ 这类元素张成，而 $\mu$ 对每个 argument 都线性。因此，检查这些 generators 后，可以逐个 argument 替换任意 representatives。

但共同等变性只给出

$$
\begin{aligned}
\left[\mu(hy_1,\ldots,hy_m)\right]_H
&=
\left[h\mu(y_1,\ldots,y_m)\right]_H\\
&=
\left[\mu(y_1,\ldots,y_m)\right]_H,
\end{aligned}
$$

也就是同一个 $h$ 同时作用于所有 arguments 时，所得 class 不变。对 $m>1$，这一般不能推出只改变第 $j$ 个 argument 所需的条件 $(*)$；对 $m=1$，共同等变性本身已经给出 $(*)$，所以一元 operation 可以直接下降。

若条件 $(*)$ 对每个 argument 都成立，$\mu_H^{\mathrm{dir}}$ 便是良定义的 direct descent。Averaging 不会改变这个候选公式是否良定义；它做的是另一件事：在 averaging 可逆时，利用 $M_H\cong M^H$ 把 invariants 上的限制映射 transport 为 $M_H$ 上的另一个 operation。后文使用的 free basis action 是保证这种可逆性的一个充分条件。

---
### Averaging 的 orbit 分解与可逆性

先在 $M$ 上定义 degree-preserving orbit-sum map

$$
A:M\longrightarrow M,
\qquad
A(v)
=
\sum_{h\in H}hv.
$$

对任意 $a\in H$，左乘 $h\mapsto ah$ 只是重排 $H$，所以

$$
aA(v)
=
\sum_{h\in H}(ah)v
=
A(v).
$$

因此 $A(v)\in M^H$。右乘 $h\mapsto ha$ 也只是重排 $H$，从而

$$
\begin{aligned}
A(av-v)
&=
\sum_{h\in H}h(av)-\sum_{h\in H}hv\\
&=
\sum_{h\in H}(ha)v-\sum_{h\in H}hv
=0.
\end{aligned}
$$

每个 $W_H^p$ 都由 $av-v$ 这类元素张成，而 $A$ 是线性映射，所以 $A(W_H^p)=0$。因此 $A$ 经过 quotient 唯一分解为非归一化 averaging map

$$
\operatorname{avg}:M_H\longrightarrow M^H,
\qquad
\operatorname{avg}([v]_H)
=
A(v)
=
\sum_{h\in H}hv.
$$

这也证明了 averaging 不依赖 representative 的选择。群作用与 coboundary 对易，因此

$$
\delta\operatorname{avg}([v]_H)
=
\sum_{h\in H}\delta(hv)
=
\sum_{h\in H}h(\delta v)
=
\operatorname{avg}([\delta v]_H),
$$

即 averaging 是 cochain map。

以下再假设群作用保持每个 degree 的选定 basis $X^p$：对所有 $h\in H$ 和 $p$，

$$
h_p(X^p)=X^p.
$$

因此 $H$ 通过 permutations 作用在每个 $X^p$ 上。固定 $x\in X^p$，记

$$
O_x
:=
Hx
=
\{hx:h\in H\}
$$

为 $x$ 的轨道（orbit），并记

$$
S_x
:=
\operatorname{Stab}_H(x)
=
\{h\in H:hx=x\}
$$

为固定 $x$ 的稳定子群（stabilizer）。考虑轨道映射（orbit map）

$$
\pi_x:H\longrightarrow O_x,
\qquad
\pi_x(h)=hx.
$$

若 $y=h_0x\in O_x$，则

$$
\pi_x^{-1}(y)=h_0S_x.
$$

所以求和 $\sum_{h\in H}hx$ 中的每个 $y\in O_x$ 都恰好出现 $|S_x|$ 次。令

$$
\sigma_x
:=
\sum_{y\in O_x}y,
\qquad
s_x
:=
|S_x|\,1_k\in k,
$$

其中 $1_k$ 是域 $k$ 的乘法单位元，则

$$
\operatorname{avg}([x]_H)
=
\sum_{h\in H}hx
=
s_x\sigma_x.
$$

记 $k[O_x]\subseteq M^p$ 为 $O_x$ 中 basis elements 张成的子空间。不同 orbits 是 basis $X^p$ 的互不相交子集，因此

$$
M^p
=
\bigoplus_{O\in X^p/H}k[O],
$$

其中 $X^p/H$ 表示 $X^p$ 中所有 $H$-orbits 的集合。每个 $k[O]$ 都在 $H$-作用下保持不变，而且每个 relation $hy-y$ 都位于某个 $k[O]$ 中，因此

$$
(M_H)^p
=
\bigoplus_{O\in X^p/H}(k[O])_H,
\qquad
(M^H)^p
=
\bigoplus_{O\in X^p/H}(k[O])^H.
$$

在 coinvariant quotient 中，同一 orbit 内的 basis elements 都代表同一个 class。为了确认这个 class 不为零，定义 coefficient-sum map

$$
\varepsilon_{O_x}:k[O_x]\longrightarrow k,
\qquad
\varepsilon_{O_x}\left(\sum_{y\in O_x}a_yy\right)
=
\sum_{y\in O_x}a_y.
$$

对任意 $h\in H$ 和 $y\in O_x$，

$$
\varepsilon_{O_x}(hy-y)=1-1=0,
$$

而 $\varepsilon_{O_x}(x)=1$。因此 $[x]_H\ne0$，并且这一 orbit 对应的 coinvariant space 是

$$
(k[O_x])_H
=
\operatorname{span}_k\{[x]_H\}.
$$

在 invariant subspace 中，$H$-不变向量在同一 orbit 的各个 basis elements 上具有相同系数，因此

$$
(k[O_x])^H
=
\operatorname{span}_k\{\sigma_x\}.
$$

由于 $\sigma_x$ 是互不相同的 basis elements 之和，所以 $\sigma_x\ne0$。相对于这两个一维空间的 bases $[x]_H$ 与 $\sigma_x$，averaging 就是乘以标量 $s_x$。因此固定 degree $p$ 后，$\operatorname{avg}^p$ 是各个 orbit 所对应的一维标量映射的直和，并且

$$
\operatorname{avg}^p\text{ 可逆}
\quad\Longleftrightarrow\quad
s_x\ne0
\text{ 对每个 }O_x\in X^p/H\text{ 成立}.
$$

若这一条件对所有 degrees $p$ 都成立，则 averaging 在每个 degree 都是线性同构。结合前面已经证明的 cochain-map 性质，得到 cochain-complex isomorphism

$$
\operatorname{avg}:M_H\xrightarrow{\cong}M^H.
$$

当 $\operatorname{char}k=\ell>0$ 时，$s_x=|S_x|1_k\ne0$ 等价于

$$
\ell\nmid |S_x|
$$

对相应的 basis orbit 成立。因此作用不自由本身既不保证 averaging 失败，也不保证它可逆；关键是 stabilizer 的大小在 $k$ 中是否为零。令 $H=C_2=\{1,t\}$ 在一维空间 $ku$ 上平凡作用，即 $tu=u$。此时 $S_u=H$，coinvariant 与 invariant spaces 都是一维，并且

$$
\operatorname{avg}([u]_H)
=
u+tu
=
2u.
$$

若 $k=\mathbb F_3$，则 $2u=-u\ne0$，所以 averaging 可逆；若 $k=\mathbb F_2$，则 $2u=0$，所以 averaging 是零映射，不能用来把 invariants 上的 operation transport 到 coinvariants。

现在进一步假设这些 permutation actions 是自由作用（free action），即

$$
hx=x
\quad\Longrightarrow\quad
h=e.
$$

此时每个 $S_x=\{e\}$，从而 $s_x=1$，上述可逆性判据自动满足，而且

$$
\operatorname{avg}([x]_H)=\sigma_x,
\qquad
\operatorname{avg}^{-1}(\sigma_x)=[x]_H.
$$

也就是说，averaging 把每个 orbit-class basis element 逐一送到对应的 orbit-sum basis element。虽然 $\sum_{h\in H}hx$ 有 $|H|$ 项，但在 free action 下，这些项是 $|H|$ 个不同的 basis elements，而不是同一个 basis element 的 $|H|$ 个副本。因此构造 $\operatorname{avg}^{-1}$ 时不需要除以 $|H|$；即使 $\operatorname{char}k=\ell>0$ 且 $\ell\mid |H|$，这个 free-action 推论仍然成立。

---
### Averaging transport 与 relative translates

以下假设 averaging 可逆。上游已经证明 Menon 的 regular $G^2$-作用在相应 product bases 上自由，因此满足这个条件。此时有 cochain-complex isomorphism

$$
\operatorname{avg}:M_H\xrightarrow{\cong}M^H
$$

而共同 $H$-等变性给出限制映射

$$
\left.\mu\right|_{(M^H)^{\times m}}
:
(M^H)^{\times m}
\longrightarrow
M^H.
$$

对每个 coinvariant class，$\operatorname{avg}$ 给出不依赖 representative 的 invariant vector $\operatorname{avg}([y]_H)$；把 $m$ 个这样的 vectors 代入 $\mu$，所得向量仍在 $M^H$ 中。Averaging transport 要求构造一条顶边 $\mu_H$，使下图交换：

$$
\begin{array}{ccc}
M_H^{\times m} & \xrightarrow{\mu_H} & M_H\\
\downarrow{\scriptstyle \operatorname{avg}^{\times m}} &&
\downarrow{\scriptstyle \operatorname{avg}}\\
(M^H)^{\times m}
& \xrightarrow{\left.\mu\right|_{(M^H)^{\times m}}} &
M^H.
\end{array}
$$

交换条件具体写成

$$
\operatorname{avg}\circ\mu_H
=
\left.\mu\right|_{(M^H)^{\times m}}
\circ
\operatorname{avg}^{\times m}.
$$

由于 $\operatorname{avg}$ 是同构，在交换式两边左复合 $\operatorname{avg}^{-1}$，得到唯一可能的顶边

$$
\mu_H
=
\operatorname{avg}^{-1}
\circ
\left.\mu\right|_{(M^H)^{\times m}}
\circ
\operatorname{avg}^{\times m}.
$$

这个构造没有使用 direct-descent 条件 $(*)$：每个 class 在应用 $\mu$ 之前已经由 $\operatorname{avg}$ 变成不依赖 representative 的 invariant vector。因此，即使 $\mu_H^{\mathrm{dir}}$ 不良定义，上式仍给出良定义的 $\mu_H$。反过来，$\mu_H$ 的存在也不会使单项公式 $[\mu(y_1,\ldots,y_m)]_H$ 变得 representative-independent；若要使用该单项定义 operation，仍须验证条件 $(*)$。

为了得到 $\mu_H$ 在 representatives 上的具体计算公式，展开各个 averaging vectors。对 basis representatives $y_1,\ldots,y_m$，

$$
\mu
\bigl(
\operatorname{avg}[y_1],\ldots,
\operatorname{avg}[y_m]
\bigr)
=
\sum_{h_1,\ldots,h_m\in H}
\mu(h_1y_1,\ldots,h_my_m).
$$

令 $k_j=h_1^{-1}h_j$。共同等变性给出

$$
\mu(h_1y_1,\ldots,h_my_m)
=
h_1\mu(y_1,k_2y_2,\ldots,k_my_m).
$$

对固定的 $(k_2,\ldots,k_m)$，$h_1$-sum 正是一个 orbit sum。应用 $\operatorname{avg}^{-1}$ 后得到 relative-translate formula：

$$
\mu_H([y_1]_H,\ldots,[y_m]_H)
=
\sum_{k_2,\ldots,k_m\in H}
\left[
\mu(y_1,k_2y_2,\ldots,k_my_m)
\right]_H.
$$

上式两边都对每个 $y_j$ 线性，而各 degree 的 basis elements 张成 $M$，所以从 basis representatives 得到的推导延伸到任意 $y_1,\ldots,y_m\in M$。左侧已经由 averaging transport 定义在 coinvariant classes 上，因此右侧的 relative-translate sum 在任意 $y_j$ 换成同一 class 的其他 representative 后保持不变。公式的关键不是限制 representatives，而是保留整个 relative-translate sum。

当

$$
k_2=\cdots=k_m=e
$$

时，relative-translate sum 中对应的一项是

$$
[\mu(y_1,\ldots,y_m)]_H.
$$

这只是整个和式的 identity-translate 项。一般情况下，averaging transport 定义的 $\mu_H$ 不能只用这一项计算，也不能与前面候选的 $\mu_H^{\mathrm{dir}}$ 混同。

若进一步满足条件 $(*)$，使 $\mu_H^{\mathrm{dir}}$ 良定义，则对每个 $(k_2,\ldots,k_m)\in H^{m-1}$，可以依次改变第 $2,\ldots,m$ 个 representatives，从而

$$
\begin{aligned}
\left[\mu(y_1,k_2y_2,\ldots,k_my_m)\right]_H
&=
\left[\mu(y_1,y_2,\ldots,y_m)\right]_H\\
&=
\mu_H^{\mathrm{dir}}([y_1]_H,\ldots,[y_m]_H).
\end{aligned}
$$

因此 relative-translate sum 的 $|H|^{m-1}$ 项相同，这两种 operations 满足

$$
\mu_H
=
\bigl(|H|^{m-1}1_k\bigr)\mu_H^{\mathrm{dir}}.
$$

这里 $|H|^{m-1}1_k$ 表示整数 $|H|^{m-1}$ 在域 $k$ 中对应的标量。因此，即使 direct descent 存在，它也不自动等于 averaging transport。$m=1$ 时没有 relative variables，指标集合由唯一的 empty tuple 构成，所以此时

$$
\mu_H=\mu_H^{\mathrm{dir}}.
$$

$m=3$、$H=G^2$ 时则有两个独立的 $H$-variables，也就是四个独立的 $G$-variables；这正是三重 balanced-product 公式中四重 relative-translate sum 的来源。

---
### Invariant integral

设

$$
\lambda:M\longrightarrow k
$$

关于 $H$-作用不变：

$$
\lambda(hv)=\lambda(v).
$$

它在同一 orbit 上取相同数值，因此直接下降到 coinvariants：

$$
\lambda_H:M_H\longrightarrow k,
\qquad
\lambda_H([v]_H)=\lambda(v).
$$

这一步不需要 free action。若 $\lambda$ 还在 top-degree coboundaries 上为零，则 $\lambda_H$ 是 balanced complex 上的 integral。

由 $H$-invariance 定义的 $\lambda_H$ 一般不等于复合映射 $\lambda\circ\operatorname{avg}:M_H\to k$。取 $H=C_2=\{e,t\}$ regular 作用在 $M=\mathbb F_2[H]$ 上，并令

$$
\lambda(e)=\lambda(t)=1.
$$

则

$$
\lambda_H([e]_H)=1,
$$

但

$$
\lambda\bigl(\operatorname{avg}([e]_H)\bigr)
=
\lambda(e+t)
=0.
$$

这个例子给出

$$
\lambda_H
\ne
\lambda\circ\operatorname{avg}.
$$

因此 inherited operation 使用 $\operatorname{avg}^{-1}\mu\operatorname{avg}^{\times m}$，而 integral 仍按 $\lambda_H([v]_H)=\lambda(v)$ 定义；后面的 integrated-Leibniz 证明必须区分这两种构造。

---
### Menon 的三重 group-algebra product

令 $G$ 是有限 Abelian 群，$R=\mathbb F_2[G]$，并取三个 seed complexes

$$
C_x:R\xrightarrow{\delta_x}R,
\qquad
\delta_x(r)=xr,
\qquad
x\in\{a,b,c\}.
$$

Ordinary product 与 balanced product 分别记为

$$
\widetilde B
=
C_a\otimes_{\mathbb F_2}C_b\otimes_{\mathbb F_2}C_c,
$$

$$
B
=
C_a\otimes_RC_b\otimes_RC_c.
$$

两个 balanced interfaces 给出 $H=G^2$，并且

$$
B=\widetilde B_H.
$$

在每个 degree sector 的 product basis $G^3$ 上，作用为

$$
(g,h)\cdot(g_1,g_2,g_3)
=
(g_1g^{-1},gg_2h^{-1},hg_3).
$$

[[Balanced tensor product 与 coinvariant quotient]] 已证明这个作用自由，所以

$$
B\xrightarrow[\operatorname{avg}]{\cong}\widetilde B^H.
$$

#### Preorientation 的平移等变性

对 $x\in\{a,b,c\}$，选择 support 两两不交的分解

$$
x=x_{\mathrm{in}}+x_{\mathrm{out}}+x_{\mathrm{free}},
$$

并定义

$$
\delta_{x,\bullet}(r)=x_\bullet r,
\qquad
\bullet\in\{\mathrm{in},\mathrm{out},\mathrm{free}\}.
$$

对 $h\in G$，记

$$
L_h(r)=hr,
\qquad
R_h(r)=rh.
$$

右平移等变性只使用结合律：

$$
\delta_{x,\bullet}(R_hr)
=
x_\bullet(rh)
=
R_h\delta_{x,\bullet}(r).
$$

左平移等变性使用 $G$ Abelian：

$$
\delta_{x,\bullet}(L_hr)
=
x_\bullet(hr)
=
h(x_\bullet r)
=
L_h\delta_{x,\bullet}(r).
$$

这与 [[Tricycle complex 的 balanced-product 构造#Abelian group algebra 与 seed maps]] 中对完整 seed map $\delta_x$ 的 regular-bimodule 计算相同；这里只是分别把 $x$ 换成 $x_{\mathrm{in}},x_{\mathrm{out}},x_{\mathrm{free}}$。因此 preorientation pieces 与两个 balanced interfaces 所需的左右 regular actions 都对易。

由这些 pieces 构造的 position-dependent trilinear map 记为 $\mu_x$。按照 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#多重局部乘积]] 的 basis-level 定义，$\mu_x$ 只取决于各 arguments 与 in/out pieces 的 membership 和 intersection relations。对 $T_h=L_h$ 或 $T_h=R_h$，$T_h$ 都 permute group basis，所以对任意相关 supports $A_1,\ldots,A_r$，

$$
z\in A_i
\quad\Longleftrightarrow\quad
T_hz\in T_hA_i,
\qquad
T_h(A_1\cap\cdots\cap A_r)
=
T_hA_1\cap\cdots\cap T_hA_r.
$$

因此共同平移前后，定义 $\mu_x$ 的 membership 和 intersection conditions 等价，从而

$$
\mu_x(L_hu_1,L_hu_2,L_hu_3)
=
L_h\mu_x(u_1,u_2,u_3),
$$

$$
\mu_x(R_hu_1,R_hu_2,R_hu_3)
=
R_h\mu_x(u_1,u_2,u_3).
$$

第一式和第二式分别给出左、右 regular action 的共同等变性。

三个 seed maps 的等变性逐 factor 推出 ordinary trilinear map

$$
\widetilde\mu
=
\mu_a\otimes\mu_b\otimes\mu_c
$$

关于共同 $H=G^2$-作用等变。Menon balanced complex 上的 inherited operation 因而是

$$
\mu_B
=
\operatorname{avg}^{-1}
\circ
\widetilde\mu
\circ
\operatorname{avg}^{\times3}.
$$

这里 $\mu_a,\mu_b,\mu_c$ 可以直接取 Menon Definition 6 的 symmetric trilinear maps；继承过程只使用三线性与共同等变性，不要求先把它们改写成结合的二元乘法。

---
### Augmentation integral

定义 augmentation

$$
\epsilon:R\longrightarrow\mathbb F_2,
\qquad
\epsilon\left(\sum_{g\in G}r_g\,g\right)
=
\sum_{g\in G}r_g.
$$

这个定义是 $\mathbb F_2$-linear 的，因此 $\epsilon$ 保持加法；群代数的单位元是 group identity $e$，并且 $\epsilon(e)=1$。再取

$$
r=\sum_{g\in G}r_g g,
\qquad
s=\sum_{h\in G}s_h h.
$$

群代数乘法给出

$$
\begin{aligned}
\epsilon(rs)
&=
\epsilon\left(\sum_{g,h\in G}r_gs_h\,gh\right)\\
&=
\sum_{g,h\in G}r_gs_h\\
&=
\left(\sum_{g\in G}r_g\right)
\left(\sum_{h\in G}s_h\right)\\
&=
\epsilon(r)\epsilon(s).
\end{aligned}
$$

因此 $\epsilon$ 保持加法、乘法和单位元，是保单位元的 ring homomorphism。这个计算不使用 $G$ Abelian。在 $\mathbb F_2$ 上，$\epsilon(r)$ 就是 $|\operatorname{supp}(r)|$ 的奇偶。若 $x\in\{a,b,c\}$ 的 support 为偶重量，则

$$
\epsilon(x)=0
$$

并且

$$
\epsilon(\delta_xr)
=
\epsilon(xr)
=
\epsilon(x)\epsilon(r)
=0.
$$

所以 $\epsilon$ 是该 seed 的 degree-$1$ integral。它还满足

$$
\epsilon(hr)=\epsilon(rh)=\epsilon(r),
\qquad
h\in G,
$$

因而关于左右 regular translations 不变。

Ordinary triple product 上的 product integral 是

$$
\widetilde\lambda(r_1\otimes r_2\otimes r_3)
=
\epsilon(r_1)\epsilon(r_2)\epsilon(r_3).
$$

它关于 $H=G^2$ 不变，故直接下降为 $\lambda_B$。在

$$
B^3
\cong
R\otimes_RR\otimes_RR
\cong R
$$

下，

$$
\lambda_B(r_1\otimes_Rr_2\otimes_Rr_3)
=
\epsilon(r_1r_2r_3).
$$

这就是 [[Symmetric triple cup-product]] 中的 coefficient-sum integral $\int_R$。偶重量保证 $\epsilon(\delta_xr)=0$；translation invariance 保证 $\widetilde\lambda$ 下降到 balanced quotient。这是两个不同条件。

---
### Integrated Leibniz 的继承

以下固定 $k=\mathbb F_2$，只让 multilinear arity $m$ 保持一般。假设 ordinary complex $M$ 上的 $(\mu,\lambda)$ 已满足无符号的 integrated Leibniz：

$$
\sum_{j=1}^m
\lambda\mu
(y_1,\ldots,\delta y_j,\ldots,y_m)
=0
$$

对所有 homogeneous $y_1,\ldots,y_m\in M$ 成立。再假设：

- $H$ 是 cochain automorphisms 作用；
- $H$ 在选定 degreewise bases 上自由作用；
- $\mu$ 关于共同 $H$-作用等变；
- $\lambda$ 关于 $H$-作用不变。

令 $q_i=[y_i]_H\in M_H$，并记 $h_1=e$。Relative-translate formula 与 descended integral 给出

$$
\begin{aligned}
&\sum_{j=1}^m
\lambda_H\mu_H
(q_1,\ldots,\delta_Hq_j,\ldots,q_m)\\
&=
\sum_{h_2,\ldots,h_m\in H}
\sum_{j=1}^m
\lambda\mu
(h_1y_1,\ldots,\delta(h_jy_j),\ldots,h_my_m).
\end{aligned}
$$

这里使用了群作用与 coboundary 对易：

$$
\delta(h_jy_j)=h_j\delta y_j.
$$

对每个固定的 $(h_2,\ldots,h_m)$，内层 $j$-sum 正是 ordinary integrated Leibniz 作用在

$$
(y_1,h_2y_2,\ldots,h_my_m)
$$

上的结果，因此等于零。对所有 relative translates 求和后仍为零：

$$
\sum_{j=1}^m
\lambda_H\mu_H
(q_1,\ldots,\delta_Hq_j,\ldots,q_m)
=0.
$$

Menon 特例取

$$
M=\widetilde B,
\qquad
H=G^2,
\qquad
m=3,
\qquad
\mu=\widetilde\mu,
\qquad
\lambda=\widetilde\lambda.
$$

若三个 seed symmetric trilinear maps 满足 local integrated Leibniz，[[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#Ordinary tensor product 上的 integrated Leibniz]] 的 fixed-factor 证明先得到 ordinary tensor-product complex $\widetilde B$ 上的 integrated Leibniz 等式。记 $\delta_{\widetilde B}$ 为 $\widetilde B$ 的 coboundary，则对所有 homogeneous $y_1,y_2,y_3\in\widetilde B$，

$$
\sum_{j=1}^3
\widetilde\lambda\widetilde\mu
(y_1,\ldots,\delta_{\widetilde B}y_j,\ldots,y_3)
=0.
$$

上面的 relative-translate 证明再从这个等式推出 balanced quotient $B$ 上的

$$
\sum_{j=1}^3
\lambda_B\mu_B
(q_1,\ldots,\delta_Bq_j,\ldots,q_3)
=0,
\qquad
q_i=[y_i]_H\in B.
$$

---
### Cohomology classes

对 $1$-cocycles $z_1,z_2,z_3\in Z^1(B)$ 定义

$$
F_B(z_1,z_2,z_3)
=
\lambda_B\mu_B(z_1,z_2,z_3).
$$

若第 $m$ 个 representative 改为 $z_m+\delta_Ba_m$，三线性性使数值变化为含 $\delta_Ba_m$ 的一项。对

$$
(z_1,\ldots,a_m,\ldots,z_3)
$$

使用 balanced integrated Leibniz，其余项都含某个 $\delta_Bz_j=0$，所以变化为零。完整的消去形式见 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#Ordinary tensor product 上的 representative invariance]]。

因此 $F_B$ 诱导

$$
\overline F_B:
H^1(B)^{\times3}
\longrightarrow
\mathbb F_2.
$$

这里处理的是 cohomology representatives。Balanced-orbit representatives 的良定义性已经在构造 $\mu_B$ 时由 averaging transport 保证。

---
### 适用条件与构造边界

记

$$
W_H=\bigoplus_pW_H^p,
\qquad
A=\sum_{h\in H}h.
$$

下表汇总前文构造所用的条件，并区分精确条件、常用充分条件与 Menon 特例中的具体验证。Menon 一列统一取

$$
k=\mathbb F_2,
\qquad
R=\mathbb F_2[G],
\qquad
G\text{ 为有限 Abelian 群},
\qquad
H=G^2.
$$

| 环节 | 数学条件 | 条件地位 | Menon 特例中的验证 |
| --- | --- | --- | --- |
| Coinvariant complex 与 averaging 的 cochain-map 性质 | 对每个 $p$ 有 $\delta^p(W_H^p)\subseteq W_H^{p+1}$，并且 $\delta(M^H)\subseteq M^H$、$\delta A=A\delta$ | 这是相应 quotient differential、invariant subcomplex 与 averaging cochain map 的精确条件。逐元素的等式 $\delta^ph_p=h_{p+1}\delta^p$ 是统一保证三者成立的充分条件 | [[Tricycle complex 的 balanced-product 构造#Abelian group algebra 与 seed maps]] 中的 seed coboundaries 与左右 regular translations 对易 |
| Averaging 可逆 | 一般条件是 $\operatorname{avg}^p:(M_H)^p\to(M^p)^H$ 在相关 degrees 上双射；若 $H$ permute 选定 basis，则等价于每个 basis orbit 都满足 $s_x=\lvert\operatorname{Stab}_H(x)\rvert1_k\ne0$ | Orbit 条件在 basis-preserving 情形中是充要条件；degreewise free permutation action 给出 $s_x=1$，因而是充分条件 | [[Balanced tensor product 与 coinvariant quotient#三重 balanced product 与两个 interfaces]] 中，regular anti-diagonal $G^2$-作用在各 degree sector 的 $G^3$ product basis 上自由 |
| Averaging transport 得到 $\mu_H$ | Averaging 在输入、输出 degrees 上可逆，且 $\mu((M^H)^{\times m})\subseteq M^H$ | 这些条件使 transport 公式有定义；共同 $H$-等变性 $\mu(hy_1,\ldots,hy_m)=h\mu(y_1,\ldots,y_m)$ 保证后一包含关系，并用于 relative-translate 展开 | [[#Preorientation 的平移等变性]] 给出各 $\mu_x$ 的共同平移等变性，从而 $\widetilde\mu=\mu_a\otimes\mu_b\otimes\mu_c$ 共同 $G^2$-等变 |
| Representativewise direct descent | 对每个 argument 都有 $\mu(M,\ldots,W_H,\ldots,M)\subseteq W_H$，即 [[#Coinvariants 上的 operation]] 的条件 $(*)$ | 这是 $[\mu(y_1,\ldots,y_m)]_H$ 不依赖 representatives 的充要条件；$m=1$ 时共同等变性已经足够，$m>1$ 时一般不足 | 本文的 inherited operation 使用 averaging transport，不假设 direct descent |
| $\lambda_H$ 下降 | $W_H\subseteq\ker\lambda$，等价于 $\lambda(hv)=\lambda(v)$ | 这是 $\lambda_H([v]_H)=\lambda(v)$ 良定义的充要条件，不要求 averaging 可逆 | [[#Augmentation integral]] 中的 $\epsilon(gr)=\epsilon(rg)=\epsilon(r)$ 保证 ordinary product integral 关于 $G^2$-作用不变 |
| $\lambda_H$ 成为 integral | $\lambda(\delta w)=0$ 对相应 top-degree coboundaries 成立 | 这是 descended functional 杀掉 quotient coboundaries 的附加条件，与 $H$-invariance 分属不同要求 | Seed supports 的偶重量给出 $\epsilon(x)=0$ 以及 $\epsilon(\delta_xr)=\epsilon(xr)=0$，其中 $x\in\{a,b,c\}$、$r\in R$；逐 factor 推出 $\widetilde\lambda(\delta_{\widetilde B}w)=0$ |
| Integrated Leibniz 继承 | Ordinary $(\mu,\lambda)$ 满足 integrated Leibniz，并且群作用是 cochain action、averaging 可逆、$\mu$ 共同等变、$\lambda$ 是关于 $H$-作用不变的 integral | 这些是 relative-translate 继承证明的充分条件；free action 只用于保证 averaging 可逆 | [[Symmetric triple cup-product#Preorientation constraints]] 给出 seed local identities；[[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#Ordinary tensor product 上的 integrated Leibniz]] 的 fixed-factor 证明先得到 $\widetilde B$ 上的 ordinary integrated Leibniz，relative-translate 证明再得到 $B$ 上的 inherited integrated Leibniz |

表中的 averaging transport 与 integral 的直接下降分别是

$$
\mu_H
=
\operatorname{avg}^{-1}
\circ
\left.\mu\right|_{(M^H)^{\times m}}
\circ
\operatorname{avg}^{\times m},
\qquad
\lambda_H([v]_H)=\lambda(v).
$$

非归一化 averaging 与 descended integral 满足

$$
\lambda\circ\operatorname{avg}
=
(\lvert H\rvert1_k)\lambda_H,
$$

因此 $\lambda_H$ 是由 $\lambda$ 直接下降得到的泛函，一般不等于 $\lambda\circ\operatorname{avg}$；这与 $\mu_H$ 的定义方式不同。在表中其余条件同时成立时，integrated Leibniz 的继承概括为

$$
\sum_{j=1}^m
\lambda\mu(y_1,\ldots,\delta y_j,\ldots,y_m)=0
\quad\Longrightarrow\quad
\sum_{j=1}^m
\lambda_H\mu_H(q_1,\ldots,\delta_Hq_j,\ldots,q_m)=0,
$$

其中 $y_i$ homogeneous，$q_i=[y_i]_H$。Menon 特例中，seed support 的偶重量只保证 augmentation 杀掉 coboundaries；local integrated Leibniz 仍需由 preorientation constraints 另行验证。满足表中条件后，最终得到

$$
\overline F_B:
H^1(B)^{\times3}\longrightarrow\mathbb F_2.
$$

上述构造不使用 $H^*(M_H)=(H^*M)_H$。当前证明取 $k=\mathbb F_2$；一般系数下需要恢复 Koszul signs。$\overline F_B$ 的非零性、physical $CCZ$ hyperedges 与 circuit scheduling 属于 [[Symmetric triple cup-product]] 及其下游问题。

---
### 来源

- Nikolas P. Breuckmann, Margarita Davydova, Jens N. Eberhardt, Nathanan Tantivasadakarn, [*Cups and Gates I: Cohomology Invariants and Logical Quantum Operations*](<../../Papers/S002_2026_Breuckmann_cups_and_gates_I.pdf>), Sections 3.3–3.4 and 5.2；Eqs. (6)–(9), Lemma 5.2, Remark 5.3。文献给出相应的二元、三重公式与推广方向；上文的一般 $m$-linear relative-translate formula 及其 integrated-Leibniz 继承证明是本笔记据此作出的推导。
- Varun Menon, J. Pablo Bonilla Ataides, Rohan Mehta, Andi Gu, Daniel Bochen Tan, Mikhail D. Lukin, [*Magic Tricycles: Efficient Magic State Generation with Finite Block-Length Quantum LDPC Codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), Appendix D；Definitions 5–6、Proposition 3。
- [[Balanced tensor product 与 coinvariant quotient]]：right/left actions、anti-diagonal coinvariants、三重 $G^2$-作用与 free regular basis action。
- [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]：seed local products、ordinary product integral、fixed-factor integrated-Leibniz 继承与 cohomology-representative 消去。
- [[Symmetric triple cup-product]]：Menon symmetric bracketing、$\int_R$ 的 physical 读数与 logical $CCZ$ 判据。
