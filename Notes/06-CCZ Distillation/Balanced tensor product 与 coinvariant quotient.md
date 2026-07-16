Ordinary tensor-product complex 只使用基域上的线性结构。若两个 complexes 还带有同一个群或群代数的作用，可以进一步识别“把同一个群元素作用在相邻两个 factors 的哪一侧”所得到的 tensors。Module tensor product 与 anti-diagonal linear coinvariant quotient 一般自然同构；若群作用还保持选定 bases，同一个对象又可写成集合层 anti-diagonal orbit quotient 的线性化。

这种识别需要先固定左、右作用，再逐 degree 构造 balanced-product complex。Menon tricycle 的四项 complex 是 regular group-algebra modules 上的特例，见 [[Tricycle complex 的 balanced-product 构造]]。

---
### 左右 module 与 balanced relation

令 $k$ 是域，$R$ 是含幺结合 $k$-algebra。 $R$-module 是一个 $k$-vector space，另外给定了与 $R$ 的乘法相容的作用。若 $R=k$，这就是普通的向量空间标量乘法；一般的 $R$ 则为每个 $r\in R$ 指定一个线性作用。

由于 $R$ 的乘法未必交换，必须说明 $r$ 从哪一侧作用。左 $R$-module ${}_R N$ 带有 $k$-bilinear map

$$
R\times N\longrightarrow N,
\qquad
(r,n)\longmapsto r\cdot n,
$$

满足

$$
(rs)\cdot n=r\cdot(s\cdot n),
\qquad
1\cdot n=n.
$$

右 $R$-module $M_R$ 带有 $k$-bilinear map

$$
M\times R\longrightarrow M,
\qquad
(m,r)\longmapsto m\cdot r,
$$

满足

$$
(m\cdot r)\cdot s=m\cdot(rs),
\qquad
m\cdot1=m.
$$

$R$ 自身给出最基本的例子：环内左乘使它成为 ${}_R R$，环内右乘使它成为 $R_R$，两种作用同时存在时记为 regular bimodule ${}_R R_R$：

$$
r\cdot x=rx,
\qquad
x\cdot r=xr.
$$

若 $R=k[G]$ 是群代数，那么左、右 $R$-module 分别等价于带左、右线性 $G$-作用的 $k$-vector space。

Balanced tensor product 把一个右 $R$-module $M_R$ 放在张量缝隙左边，把一个左 $R$-module ${}_R N$ 放在右边。共享的 $r\in R$ 因而可以写成第一个 factor 上的 $m\cdot r$，也可以写成第二个 factor 上的 $r\cdot n$。 

#### 乘法映射与作用侧别

右模与左模的配对来自环乘法的结合律。先在两份 regular module 上考虑乘法映射

$$
\mu:R_R\times{}_R R\longrightarrow R,
\qquad
\mu(x,y)=xy.
$$

由 ordinary tensor product 的泛性质，$\mu$ 诱导线性映射

$$
\widetilde\mu:R\otimes_kR\longrightarrow R,
\qquad
\widetilde\mu(x\otimes y)=xy.
$$

Ordinary tensor product 的泛性质只处理基域 $k$ 上的双线性，因此没有施加关系令

$$
(xr)\otimes y
\qquad\text{与}\qquad
x\otimes(ry),
$$

相等。但是环乘法结合律给出

$$
\widetilde\mu((xr)\otimes y)
=(xr)y
=x(ry)
=\widetilde\mu(x\otimes(ry)).
$$

若把 tensor product 改为 over $R$，下标 $R$ 表示 $r$ 是两个 factors 共享的中间系数：让 $r$ 右乘第一个 factor，或让同一个 $r$ 左乘第二个 factor，不应产生两个不同的 tensor classes。为了满足这项要求，把所有这类位置差张成的子空间记为

$$
W
=
\operatorname{span}_k
\left\{
(xr)\otimes y-x\otimes(ry)
:x,y,r\in R
\right\}.
$$

上式说明 $W\subseteq\ker\widetilde\mu$。令

$$
Q=(R\otimes_kR)/W.
$$

于是存在唯一的线性映射 $\overline\mu:Q\to R$，使下面的复合仍是原来的乘法：

$$
R\otimes_kR
\xrightarrow{q}
Q
\xrightarrow{\overline\mu}
R,
\qquad
\widetilde\mu=\overline\mu\circ q,
\qquad
\overline\mu([x\otimes y])=xy.
$$

因此在 $Q$ 中，

$$
[(xr)\otimes y]
=
[x\otimes(ry)].
$$

这个 $Q$ 就是两份 regular modules 的 balanced tensor product，记作 $R_R\otimes_R{}_RR$。

这条关系把 $r$ 从第一个 factor 的右侧移到第二个 factor 的左侧，所以第一个 factor 需要右作用，第二个 factor 需要左作用。

若误把第一个作用改成左作用，并写成

$$
(rx)\otimes y
\stackrel{?}{\sim}
x\otimes(ry),
$$

那么乘法映射要尊重该关系就必须满足

$$
rxy=xry.
$$

取 $y=1$ 后得到 $rx=xr$。这不是结合律，而是额外的交换性要求；例如在 $R=k[S_3]$ 中取两个不交换的群元素便会失败，交换环会掩盖这个差别。

对一般的 $M_R$ 与 ${}_RN$，保留同样的右—左识别便得到 balanced tensor product。

Balanced tensor product 定义为

$$
M_R\otimes_R{}_RN
:=
\frac{M\otimes_kN}
{
\left\langle
(m\cdot r)\otimes n-m\otimes(r\cdot n)
:m\in M,n\in N,r\in R
\right\rangle
}.
$$

因此其中的基本关系是

$$
(m\cdot r)\otimes_R n
=
m\otimes_R(r\cdot n).
$$

在 $k=\mathbb F_2$ 上，商空间分母中的减号可以写成加号；这只改变关系的线性写法，不改变左、右作用的位置。

若 $U$ 是一个 $k$-vector space，$k$-bilinear map

$$
B:M\times N\longrightarrow U
$$

称为 $R$-balanced，如果

$$
B(m\cdot r,n)=B(m,r\cdot n).
$$

每个这样的 $B$ 唯一诱导一个 $k$-linear map

$$
\overline B:M\otimes_RN\longrightarrow U,
\qquad
\overline B(m\otimes_Rn)=B(m,n).
$$

这就是 $M\otimes_RN$ 的泛性质。

#### Tensor 结果上的外侧作用

$M_R$ 的右 $R$-作用与 ${}_R N$ 的左 $R$-作用已经用于中间的 balanced relation；它们不会自动变成 $M\otimes_RN$ 上的 $R$-作用。若只给出 $M_R$ 与 ${}_R N$，则 $M\otimes_RN$ 一般首先只是 $k$-vector space。

令 $S,T$ 也是含幺结合 $k$-algebras。若希望 tensor 结果继续带左 $S$-作用，需要把 $M$ 加强为 $(S,R)$-bimodule ${}_S M_R$，使外侧的左 $S$-作用与内侧的右 $R$-作用相容：

$$
s\cdot(m\cdot r)
=
(s\cdot m)\cdot r.
$$

此时可定义

$$
s\cdot(m\otimes_Rn)
:=
(s\cdot m)\otimes_Rn.
$$

相容条件保证这个定义尊重 balanced relation：

$$
\begin{aligned}
s\cdot\bigl((m\cdot r)\otimes_Rn\bigr)
&=\bigl(s\cdot(m\cdot r)\bigr)\otimes_Rn\\
&=\bigl((s\cdot m)\cdot r\bigr)\otimes_Rn\\
&=(s\cdot m)\otimes_R(r\cdot n)\\
&=s\cdot\bigl(m\otimes_R(r\cdot n)\bigr).
\end{aligned}
$$

类似地，若要保留右 $T$-作用，需要把 $N$ 加强为 $(R,T)$-bimodule ${}_R N_T$，满足

$$
(r\cdot n)\cdot t
=
r\cdot(n\cdot t),
$$

并定义

$$
(m\otimes_Rn)\cdot t
:=
m\otimes_R(n\cdot t).
$$

右 $T$-作用同样尊重 balanced relation：

$$
\begin{aligned}
\bigl((m\cdot r)\otimes_Rn\bigr)\cdot t
&=(m\cdot r)\otimes_R(n\cdot t)\\
&=m\otimes_R\bigl(r\cdot(n\cdot t)\bigr)\\
&=m\otimes_R\bigl((r\cdot n)\cdot t\bigr)\\
&=\bigl(m\otimes_R(r\cdot n)\bigr)\cdot t.
\end{aligned}
$$

两个外侧作用分别落在不同 factors 上，因而彼此相容：

$$
\begin{aligned}
\bigl(s\cdot(m\otimes_Rn)\bigr)\cdot t
&=(s\cdot m)\otimes_R(n\cdot t)\\
&=s\cdot\bigl((m\otimes_Rn)\cdot t\bigr).
\end{aligned}
$$

它们的结合律和单位元公理分别从 $M$ 的左 $S$-作用与 $N$ 的右 $T$-作用继承。因此一般的类型关系是

$$
{}_S M_R\otimes_R{}_R N_T
\quad\text{是一个}\quad
(S,T)\text{-bimodule}.
$$

中间的 $R$-作用用于 balanced quotient；结果上的左 $S$-作用来自第一个 factor 的外侧，右 $T$-作用来自第二个 factor 的外侧。

后面的三重 balanced product 取 $T=R$：第一次形成 $M_R\otimes_R{}_R N_R$ 后，tensor 结果从 $N$ 继承右 $R$-作用，因而还能继续与 ${}_R P$ 作第二次 balanced tensor product。

当 $R$ 交换时，一个左 $R$-module 可以通过

$$
m\cdot r:=r\cdot m
$$

成为右 $R$-module。此时才可以把 balanced relation 简写成

$$
(rm)\otimes n=m\otimes(rn).
$$

这条简写依赖交换性，不能代替一般定义中的右模、左模类型。

---
### Anti-diagonal action 与 coinvariants

#### Coinvariant quotient

令 $G$ 是有限群，$U$ 是带左 $G$-作用的 $k$-vector space。Coinvariant quotient 定义为

$$
U_G
:=
\frac{U}
{W_G(U)},
\qquad
W_G(U)
:=
\operatorname{span}_k
\{g\cdot u-u:g\in G,u\in U\}.
$$

若 $[u]_G$ 表示 $u$ 在 quotient 中的 class，则

$$
[g\cdot u]_G=[u]_G.
$$

集合

$$
G\cdot u
=
\{g\cdot u:g\in G\}
$$

称为 $u$ 的 $G$-orbit。因此同一个 orbit 中的 vectors 在 $U_G$ 中代表同一个 class。等价地，$U_G$ 是强制所有 $g\in G$ 都作用为恒等映射后得到的最大线性 quotient：若线性映射 $q:U\to Q$ 满足

$$
q(g\cdot u)=q(u),
$$

则 $W_G(U)\subseteq\ker q$，所以 $q$ 唯一经过 $U_G$ 分解。

Coinvariants 不要与 invariants 混淆。Invariants 是 fixed-vector subspace

$$
U^G
=
\{u\in U:g\cdot u=u\text{ for all }g\in G\},
$$

而 $U_G$ 是把 $g\cdot u-u$ 商掉所得的 quotient。二者一般不是同一个对象。

#### Balanced relation 与 anti-diagonal action

现在取 $R=k[G]$。右 $G$-module $M$ 和左 $G$-module $N$ 也分别是右、左 $R$-modules，并记

$$
V=M\otimes_kN.
$$

前一节已经直接定义了 balanced tensor product。对群代数而言，只用群元素生成 relations 即可：令

$$
W_{\mathrm{bal}}
=
\operatorname{span}_k
\left\{
(m\cdot g)\otimes n-m\otimes(g\cdot n)
:m\in M,n\in N,g\in G
\right\},
$$

则

$$
M_R\otimes_{k[G]}{}_R N
=
V/W_{\mathrm{bal}}.
$$

Balanced quotient $V/W_{\mathrm{bal}}$ 已由上文固定。接下来主动在 $V$ 上构造一个左 $G$-作用，把同一组 balanced relations 表成 $g\cdot v-v$ 型 coinvariant relations。这样会显式保留产生这些 relations 的群作用：若该作用 permutes $V$ 的选定 tensor-product basis，quotient 的 basis 可以按 basis-orbits 描述。后文的 averaging transport 还会另行假设这个 basis action 自由，并要求 ordinary operation 关于共同群作用等变；

所构造作用的 coinvariant relation subspace 是

$$
W_G
=
\operatorname{span}_k
\{g\cdot v-v:g\in G,v\in V\}.
$$

需要选择这个作用，使 $W_G$ 恰好等于 $W_{\mathrm{bal}}$。一旦做到这一点，就有

$$
V/W_{\mathrm{bal}}
=
V/W_G
=
V_G.
$$

为使 $W_G$ 产生同一组 balanced relations，先寻找 $v$，使 $g\cdot v-v$ 给出

$$
m\otimes(g\cdot n)-(m\cdot g)\otimes n.
$$

取 $v=(m\cdot g)\otimes n$，第一个 factor 必须消掉已有的右乘 $g$，所以使用右乘 $g^{-1}$。这给出

$$
g\cdot(m\otimes n)
=
(m\cdot g^{-1})\otimes(g\cdot n).
$$

它确实是左群作用，因为

$$
\begin{aligned}
g_1\cdot\bigl(g_2\cdot(m\otimes n)\bigr)
&=(m\cdot g_2^{-1}g_1^{-1})
  \otimes((g_1g_2)\cdot n)\\
&=(m\cdot(g_1g_2)^{-1})
  \otimes((g_1g_2)\cdot n)\\
&=(g_1g_2)\cdot(m\otimes n).
\end{aligned}
$$

若第一项错误地使用 $m\cdot g$，连续作用 $g_2$、$g_1$ 后会出现 $m\cdot g_2g_1$，在非 Abelian 群中不满足结合律。同一个 $g$ 在两个 factors 上分别以 $g^{-1}$ 与 $g$ 出现，因此这里称它为 anti-diagonal action。

现在比较两个关系子空间。对每个 balanced generator，取 $v=(m\cdot g)\otimes n$，则

$$
g\cdot v-v
=
m\otimes(g\cdot n)-(m\cdot g)\otimes n,
$$

所以 $W_{\mathrm{bal}}\subseteq W_G$。反过来，对 pure tensor $v=m\otimes n$，令 $m'=m\cdot g^{-1}$，于是 $m=m'\cdot g$，并且

$$
\begin{aligned}
g\cdot v-v
&=(m\cdot g^{-1})\otimes(g\cdot n)-m\otimes n\\
&=m'\otimes(g\cdot n)-(m'\cdot g)\otimes n
\in W_{\mathrm{bal}}.
\end{aligned}
$$

Pure tensors 张成 $V$，因此 $W_G\subseteq W_{\mathrm{bal}}$。综上，

$$
W_G=W_{\mathrm{bal}},
\qquad
M_R\otimes_{k[G]}{}_R N
\cong
(M\otimes_kN)_G.
$$

至此，前面定义的 balanced quotient 已被识别为所构造的 anti-diagonal action 的 coinvariant quotient。记号 $M_R\otimes_{k[G]}{}_R N$ 直接记录同一个群元素怎样从第一个 factor 的右作用移到第二个 factor 的左作用，记号 $(M\otimes_kN)_G$ 则记录同一 anti-diagonal orbit 中的 tensors 具有同一个 class。

若 $M=k[X]$、$N=k[Y]$，并且右、左 $G$-作用分别 permute **bases** $X,Y$，则

$$
M\otimes_kN
\cong
k[X\times Y].
$$

对应的 anti-diagonal action 在 basis $X\times Y$ 上为

$$
g\cdot(x,y)=(xg^{-1},gy).
$$

因此

$$
M_R\otimes_{k[G]}{}_R N
\cong
\bigl(k[X\times Y]\bigr)_G
\cong
k[(X\times Y)/G].
$$

也就是说，balanced quotient 的 basis 由 $X\times Y$ 的 anti-diagonal orbits 标记。

这个 orbit-class 描述不要求群作用自由。到了后文的 cochain-complex 情形，还会假设群作用在每个 degree 的选定 basis 上自由；这不是 balanced quotient 的定义条件，而只是保证非归一化 averaging 从 coinvariants 到 invariants 成为同构的一个充分条件。在相应等变性条件下，这个同构才用于把 ordinary operation 继承到 balanced quotient，见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]。

#### 逆元的作用

取 $G=C_3=\langle t\mid t^3=e\rangle$，并在 $G\times G$ 上使用 regular actions。正确的 anti-diagonal action 保持乘积坐标：

$$
(xt^{-1})(ty)=xy.
$$

若把第一项错误地写成 $xt$，乘积会变成

$$
(xt)(ty)=xt^2y,
$$

它一般不等于 $xy$。因此即使 $G$ Abelian，anti-diagonal action 中的逆元也不能省略；$C_2$ 上 $t=t^{-1}$，反而会掩盖这一点。

---
### Balanced-product complex

设 $C$ 是右 $R$-module cochain complex，$D$ 是左 $R$-module cochain complex，并且各自的 coboundary maps 关于相应侧的 $R$-作用线性。Balanced-product complex 的 degree-$n$ 项为

$$
(C\otimes_RD)^n
=
\bigoplus_{p+q=n}C^p\otimes_RD^q.
$$

对 homogeneous $c\in C^p$、$d\in D^q$，coboundary 为

$$
\delta(c\otimes_Rd)
=
\delta_Cc\otimes_Rd
+
(-1)^p c\otimes_R\delta_Dd.
$$

两边 coboundary 的 module-linearity 保证这个公式尊重 balanced relation。先看 $\delta_C$ 项：

$$
\delta_C(c\cdot r)\otimes_Rd
=
(\delta_Cc\cdot r)\otimes_Rd
=
\delta_Cc\otimes_R(r\cdot d).
$$

这里两个等号的来源不同。第一个等号使用 $\delta_C$ 的右 $R$-线性

$$
\delta_C(c\cdot r)=(\delta_Cc)\cdot r.
$$

若记右乘 $r$ 的映射为 $R_r(c)=c\cdot r$，这项条件也可以写成

$$
\delta_C\circ R_r=R_r\circ\delta_C.
$$

第二个等号则直接使用 balanced relation，并在

$$
(m\cdot r)\otimes_Rn
=
m\otimes_R(r\cdot n)
$$

中取 $m=\delta_Cc$、$n=d$。同理，$\delta_D$ 的左 $R$-线性给出

$$
\delta_D(r\cdot d)=r\cdot\delta_Dd.
$$

因此 balanced relation 两边的完整 coboundary 满足

$$
\begin{aligned}
\delta\bigl((c\cdot r)\otimes_Rd\bigr)
&=\delta_C(c\cdot r)\otimes_Rd
  +(-1)^p(c\cdot r)\otimes_R\delta_Dd\\
&=\delta_Cc\otimes_R(r\cdot d)
  +(-1)^p c\otimes_R\delta_D(r\cdot d)\\
&=\delta\bigl(c\otimes_R(r\cdot d)\bigr).
\end{aligned}
$$

也就是说，两个 representatives 由 balanced relation 相差时，它们的 coboundaries 仍由同一关系识别，所以 $\delta$ 在 balanced quotient 上良定义。

若 $R=k[G]$，这也可以写成 ordinary product complex 的 coinvariants：

$$
C\otimes_GD
=
(C\otimes_kD)_G.
$$

#### Coinvariant quotient 上的 coboundary

上式若要理解为 cochain complexes 的等式，而不只是各 degree 向量空间的等式，还需要说明 ordinary coboundary 怎样作用在 coinvariant classes 上。

设 $M=(M^\bullet,\delta)$ 是 cochain complex。记号 $M^\bullet$ 代表全部 degree spaces，而 $\delta$ 代表其中所有 coboundary maps；固定一个 degree $p$ 时，原 complex 中的箭头是

$$
\delta^p:M^p\longrightarrow M^{p+1}.
$$

令有限群 $H$ 逐 degree 作用在 $M$ 上。也就是说，对每个 $h\in H$ 和每个 $p$，都有可逆线性映射

$$
h_p:M^p\longrightarrow M^p.
$$

先只用这个 degree-preserving action 构造 quotient spaces。Degree $p$ 的 relation subspace 定义为

$$
W_H^p
:=
\operatorname{span}_k
\{h_p(v)-v:h\in H,\ v\in M^p\}.
$$

下标 $H$ 表示这些 relations 来自 $H$-作用，上标 $p$ 表示它们位于 $M^p$。Degree $p$ 的 coinvariant quotient 是

$$
(M_H)^p
:=
M^p/W_H^p.
$$

这里 $M_H$ 的下标 $H$ 表示逐 degree 取 $H$-coinvariants。

记相应的 quotient map 为

$$
q_p:M^p\longrightarrow(M_H)^p,
\qquad
q_p(v)=[v]_H=v+W_H^p.
$$

因此 $[v]_H$ 表示 $v$ 在 degree-$p$ quotient 中的 class。把 $p$ 换成 $p+1$，同样的构造给出 $W_H^{p+1}$、$(M_H)^{p+1}$ 和 quotient map $q_{p+1}$。此外，

$$
\ker q_p=W_H^p,
\qquad
[h_p(v)]_H=[v]_H.
$$

到这里，$\{(M_H)^p\}_p$ 还只是一族按 degree 排列的 quotient spaces。要让它成为 cochain complex，需要为每个 $p$ 构造一条新箭头

$$
\delta_H^p:(M_H)^p\longrightarrow(M_H)^{p+1}.
$$

这里下标 $H$ 表示这是 coinvariant quotient $M_H$ 上的 coboundary，上标 $p$ 表示它从 degree $p$ 指向 degree $p+1$。希望这条新箭头与原 coboundary 和两个 quotient maps 组成交换图：

$$
\begin{array}{ccc}
M^p & \xrightarrow{\delta^p} & M^{p+1}\\
\downarrow q_p && \downarrow q_{p+1}\\
(M_H)^p & \xrightarrow{\delta_H^p} & (M_H)^{p+1}.
\end{array}
$$

交换图的意思是，从 $M^p$ 出发，先向右再向下与先向下再向右得到同一个结果：

$$
q_{p+1}\circ\delta^p
=
\delta_H^p\circ q_p.
$$

由于 $q_p$ 是满射，若这样的 $\delta_H^p$ 存在，交换式就已经唯一决定了它。存在性则取决于原 coboundary 是否尊重被商掉的 relations。若 $w\in W_H^p=\ker q_p$，交换式要求

$$
q_{p+1}(\delta^pw)
=
\delta_H^p(q_p(w))
=0,
$$

所以必须有

$$
\delta^p(W_H^p)
\subseteq
W_H^{p+1}.
$$

反过来，若这个 inclusion 成立，并且 $q_p(v')=q_p(v)$，那么 $v'-v\in W_H^p$，从而

$$
\delta^pv'-\delta^pv
\in
W_H^{p+1}.
$$

于是 $q_{p+1}(\delta^pv')=q_{p+1}(\delta^pv)$，所以先取原 coboundary 再取 quotient class 的结果只依赖 $[v]_H$。因此 $\delta^p(W_H^p)\subseteq W_H^{p+1}$ 正是 quotient coboundary 存在的充要条件。

现在加入一个容易检查的充分条件：群作用与 coboundary 对易，即

$$
\delta^p\circ h_p
=
h_{p+1}\circ\delta^p.
$$

对 $W_H^p$ 的每个 generator，这给出

$$
\begin{aligned}
\delta^p\bigl(h_p(v)-v\bigr)
&=h_{p+1}(\delta^pv)-\delta^pv\\
&\in W_H^{p+1}.
\end{aligned}
$$

这些 generators 张成 $W_H^p$，所以由线性性得到 $\delta^p(W_H^p)\subseteq W_H^{p+1}$。此时才可以定义

$$
\delta_H^p([v]_H)
:=
[\delta^pv]_H.
$$

这条公式的操作顺序是：先为 degree-$p$ class 选择 representative $v$，再用原 coboundary 得到 $\delta^pv\in M^{p+1}$，最后取它在 $(M_H)^{p+1}$ 中的 class。上面的 inclusion 保证结果不依赖 representative；$q_p$ 的满射性保证这是唯一满足交换图的定义。

原 coboundary 满足 $\delta^{p+1}\delta^p=0$，因此 quotient coboundary 也平方为零：

$$
\delta_H^{p+1}\delta_H^p([v]_H)
=
[\delta^{p+1}\delta^pv]_H
=0.
$$

严格的对易条件是保证上述包含关系成立的充分条件，但不是逻辑上的必要条件；即使两者不严格对易，$\delta^p(W_H^p)\subseteq W_H^{p+1}$ 仍可能成立。真正的失败情形是存在 $h\in H$、$v\in M^p$ 使

$$
\delta^p\bigl(h_p(v)-v\bigr)
\notin
W_H^{p+1}.
$$

此时 $[h_p(v)]_H=[v]_H$，但 $[\delta^p(h_p(v))]_H\ne[\delta^pv]_H$，所以两个相同 class 的 representatives 会得到不同的 coboundary classes，$\delta_H^p$ 不能按上式定义。

这一构造不要求群作用保持某个选定 basis，也不要求作用自由；这些条件只在 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]] 中用于 averaging 与 inherited operation。

---
### 三重 balanced product 与两个 interfaces

三重 balanced product 需要三个不同的侧别：

$$
M_R,
\qquad
{}_RN_R,
\qquad
{}_RP.
$$

中间项 $N$ 是 $R$-$R$ bimodule，其左、右作用满足

$$
(r\cdot n)\cdot r'
=
r\cdot(n\cdot r'),
\qquad
r,r'\in R.
$$

于是可以形成

$$
M_R\otimes_R{}_RN_R\otimes_R{}_RP.
$$

第一个接口识别

$$
(m\cdot r)\otimes n\otimes p
\sim
m\otimes(r\cdot n)\otimes p,
$$

第二个接口识别

$$
m\otimes(n\cdot r)\otimes p
\sim
m\otimes n\otimes(r\cdot p).
$$

当 $R=k[G]$ 时，这两个接口合成 $H=G^2$ 在 ordinary triple product 上的作用：

$$
(g,h)\cdot(m_1,m_2,m_3)
=
(m_1\cdot g^{-1},\,g\cdot m_2\cdot h^{-1},\,h\cdot m_3).
$$

对 regular basis $G^3$，

$$
(g,h)\cdot(g_1,g_2,g_3)
=
(g_1g^{-1},\,gg_2h^{-1},\,hg_3).
$$

这个作用是自由的：若它固定 $(g_1,g_2,g_3)$，第一坐标给出 $g=e$，第三坐标给出 $h=e$。它还保持有序乘积

$$
(g_1g^{-1})(gg_2h^{-1})(hg_3)
=
g_1g_2g_3.
$$

反过来取 $g=g_1$、$h=g_1g_2$，任意三元组都可移到

$$
(e,e,g_1g_2g_3).
$$

因此每条 orbit 由乘积坐标唯一标记：

$$
G^3/G^2\cong G.
$$

这一结论只使用群的结合律和消去律，不要求 $G$ Abelian。

---
### Quotient 层次

Balanced product 路径中会出现两种不同的 quotient：

| 阶段 | 对象 | 商掉的关系 |
|---|---|---|
| complex 构造 | $B=\widetilde B_H\cong C_1\otimes_R\cdots\otimes_RC_m$ | group action / balanced relations |
| logical classes | $H^i(B)=\ker\delta_B^i/\operatorname{im}\delta_B^{i-1}$ | coboundaries |

第一行先构造新的 cochain complex；第二行是在这个 complex 内再取 cohomology。一般不能把二者交换成

$$
H^*(\widetilde B_H)
\stackrel{?}{=}
H^*(\widetilde B)_H.
$$

---
### 来源

- The Stacks Project, [*Tensor products*](https://stacks.math.columbia.edu/tag/00CV)：tensor product 的泛性质与迭代 tensor 的 associativity。正文中的非交换 $k$-algebra、右模与左模侧别不归因于该条目，而是由 quotient relation 与泛性质直接定义。
- Nikolas P. Breuckmann, Jens N. Eberhardt, [*Balanced Product Quantum Codes*](https://arxiv.org/abs/2012.09271), *IEEE Transactions on Information Theory* 67, 6653–6674 (2021)：balanced-product code construction。
- Nikolas P. Breuckmann, Margarita Davydova, Jens N. Eberhardt, Nathanan Tantivasadakarn, [*Cups and Gates I: Cohomology Invariants and Logical Quantum Operations*](<../../Papers/S002_2026_Breuckmann_cups_and_gates_I.pdf>), Sections 3.3–3.4：Section 3.3.2 直接给出 $g\cdot(x,y)=(x\cdot g^{-1},g\cdot y)$，并由此定义 balanced-product complexes；Sections 3.3–3.4 进一步讨论 coinvariants、inherited operations 与 integrals。
- Varun Menon et al., [*Magic Tricycles: Efficient Magic State Generation with Finite Block-Length Quantum LDPC Codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), Supplementary Material, Eqs. (83)–(89)：group-algebra balanced product 的 Abelian 特例。
