# 张量积与直和泛性质的 HGP–Künneth 接口

许多线性代数构造都从一条“只在局部输入上写出的规则”开始。真正需要解决的不是怎样把公式写得更长，而是：

$$
\text{这条局部规则是否决定了整个空间上的唯一线性映射？}
$$

在 HGP 与 Künneth 中会反复遇到两种不同的局部数据。

第一种数据同时依赖两个变量。例如，我们先规定 $(v,w)$ 应被送到某个值，并要求这条规则分别对 $v$ 和 $w$ 线性。此时需要张量积把双线性规则线性化。

第二种数据分别定义在若干个直和分量上。例如，我们已经有 $f:V\to X$ 和 $g:W\to X$，想把它们拼成一张从 $V\oplus W$ 出发的线性映射。此时需要直和的泛性质。

两种构造都把“局部规则”变成“唯一整体映射”，但它们处理的数据、典范映射和映射方向并不相同。先把这两步分别建立起来，后面才不会把乘积复形的总次数直和、Künneth 比较映射和 HGP 的物理分量混在一起。

## 张量积解决什么问题

固定一个域 $k$，以下向量空间和普通张量积默认都在 $k$ 上。

### 同一个 $V\times W$ 上的两种线性要求

集合 $V\times W$ 由有序对 $(v,w)$ 组成。给它规定逐坐标运算

$$
(v_1,w_1)+(v_2,w_2)
=
(v_1+v_2,w_1+w_2),
$$

$$
a(v,w)=(av,aw),
$$

就得到一个向量空间。对两个因子而言，这正是外直和 $V\oplus W$ 通常使用的有序对模型。

先把 $(v,w)$ 看成这个向量空间中的一个输入，并要求

$$
F:V\oplus W\longrightarrow X
$$

整体线性。由于

$$
(v,w)=(v,0)+(0,w),
$$

线性性迫使

$$
F(v,w)=F(v,0)+F(0,w).
$$

令 $f(v)=F(v,0)$、$g(w)=F(0,w)$，那么 $f$ 与 $g$ 都是线性映射，并且

$$
F(v,w)=f(v)+g(w).
$$

因此，从 $V\oplus W$ 出发的线性映射完全由它在两个坐标分量上的限制决定，并把两部分的结果相加。后面的直和泛性质将精确表述这一点。

现在考虑同一个有序对集合上的映射

$$
b:V\times W\longrightarrow X,
$$

但不要求它对有序对整体线性，而是要求它对两个输入分别线性：

$$
\begin{aligned}
b(v_1+v_2,w)&=b(v_1,w)+b(v_2,w),\\
b(v,w_1+w_2)&=b(v,w_1)+b(v,w_2),\\
b(av,w)&=a\,b(v,w),\\
b(v,aw)&=a\,b(v,w).
\end{aligned}
$$

这就是双线性。这里每次只改变一个变量，另一个变量保持不动。特别地，双线性给出

$$
b(v,0)=0,
\qquad
b(0,w)=0.
$$

这使两种线性要求产生了直接冲突。若 $b$ 同时还是乘积向量空间上的线性映射，那么

$$
\begin{aligned}
b(v,w)
&=b\bigl((v,0)+(0,w)\bigr)\\
&=b(v,0)+b(0,w)\\
&=0.
\end{aligned}
$$

所以同时满足这两种线性要求的只有零映射。作为最简单的非零例子，域上的乘法

$$
m:k\times k\longrightarrow k,
\qquad
m(x,y)=xy
$$

是双线性的，却不是 $k\oplus k\to k$ 的线性映射，因为

$$
m\bigl((1,0)+(0,1)\bigr)=m(1,1)=1,
$$

而

$$
m(1,0)+m(0,1)=0.
$$

因此，两种映射区别不在底层集合，也不只是记号选择。对 $F$ 而言，$(v,w)$ 是 $V\oplus W$ 中的一个整体向量；对 $b$ 而言，$v$ 与 $w$ 是两个分别接受线性条件的输入。非零双线性规则无法直接成为 $V\oplus W$ 上的线性映射，所以我们需要另找一个向量空间作为它的线性定义域。这个空间就是 $V\otimes_kW$，下一节的泛性质将把这件事说准确。

### 泛性质同时刻画空间与典范双线性映射

$V$ 与 $W$ 的张量积不是孤立的一个向量空间，而是一对数据

$$
\left(V\otimes_k W,\tau\right),
$$

其中

$$
\tau:V\times W\longrightarrow V\otimes_k W
$$

是典范双线性映射。记

$$
\tau(v,w)=v\otimes w.
$$

这对数据满足如下泛性质（universal property）：对任意 $k$-向量空间 $X$ 和任意双线性映射

$$
b:V\times W\longrightarrow X,
$$

都存在唯一的线性映射

$$
\widetilde b:V\otimes_k W\longrightarrow X
$$

使得

$$
\widetilde b\circ\tau=b.
$$

逐元素写，就是

$$
\widetilde b(v\otimes w)=b(v,w)
\qquad
\text{对所有 }v\in V,\ w\in W.
$$

因此，复合典范映射 $\tau$ 给出一一对应

$$
\operatorname{Hom}_k(V\otimes_k W,X)
\longrightarrow
\operatorname{Bilin}_k(V\times W,X),
\qquad
L\longmapsto L\circ\tau,
$$

而它的逆方向把双线性映射 $b$ 送到唯一的线性因子化映射 $\widetilde b$。于是可以写成

$$
\operatorname{Hom}_k(V\otimes_k W,X)
\cong
\operatorname{Bilin}_k(V\times W,X).
$$

这里“唯一”说的是：一旦规定了所有纯张量 $v\otimes w$ 的像，且这些像来自一条双线性规则，就只有一张线性映射 $V\otimes_kW\to X$ 与之相容。泛性质不是张量积构造完以后附加的一条好性质；它正是在说明什么对象有资格称为 $V$ 与 $W$ 的张量积。

### 一个具体实现：自由向量空间再取商

泛性质说明 $\tau$ 把双线性映射转化成唯一的线性映射，但还需要证明这样的 $\tau$ 确实存在。一个标准的实现从自由向量空间开始。

令 $F(V\times W)$ 是以集合 $V\times W$ 为基的自由 $k$-向量空间。它的元素是这些基符号的有限形式线性组合，所以在每个基符号上指定像，就会唯一决定一张线性映射。为避免提前使用张量符号，把与有序对 $(v,w)$ 对应的基向量记作

$$
\langle v,w\rangle.
$$

令 $\mathcal R\subseteq F(V\times W)$ 为下列四类元素张成的子空间，其中 $v,v'\in V$、$w,w'\in W$、$a\in k$：

$$
\langle v+v',w\rangle
-\langle v,w\rangle
-\langle v',w\rangle,
$$

$$
\langle v,w+w'\rangle
-\langle v,w\rangle
-\langle v,w'\rangle,
$$

$$
\langle av,w\rangle
-a\langle v,w\rangle,
$$

$$
\langle v,aw\rangle
-a\langle v,w\rangle.
$$

定义

$$
T=\frac{F(V\times W)}{\mathcal R},
$$

并记商映射为

$$
q:F(V\times W)\longrightarrow T,
\qquad
q(\xi)=\xi+\mathcal R.
$$

令

$$
\tau(v,w)
=q(\langle v,w\rangle)
=\langle v,w\rangle+\mathcal R.
$$

商掉上述关系以后，$\tau$ 分别对两个变量可加且与标量乘法相容，所以它是双线性映射。把它的值记作 $v\otimes w$，便得到一个候选张量积。

现在取任意双线性映射 $b:V\times W\to X$。由于 $F(V\times W)$ 是自由向量空间，基向量上的规则

$$
\langle v,w\rangle\longmapsto b(v,w)
$$

唯一线性张成为

$$
B:F(V\times W)\longrightarrow X.
$$

$b$ 的双线性保证上述四类关系全被 $B$ 送到零。例如，

$$
B\bigl(
\langle v+v',w\rangle
-\langle v,w\rangle
-\langle v',w\rangle
\bigr)
=0,
$$

其余三类同理。因此

$$
\mathcal R\subseteq\ker B.
$$

因此 $B$ 可以下降到商空间，即找一张新映射 $\widetilde b:T\to X$，使得

$$
B=\widetilde b\circ q.
$$

这样的映射之所以能够定义，是因为 $B$ 无法区分同一个商类的不同代表元。若

$$
\xi+\mathcal R=\eta+\mathcal R,
$$

则 $\xi-\eta\in\mathcal R\subseteq\ker B$，因而

$$
B(\xi)-B(\eta)=B(\xi-\eta)=0.
$$

所以 $B(\xi)=B(\eta)$，公式

$$
\widetilde b:T\longrightarrow X,
\qquad
\widetilde b(\xi+\mathcal R)=B(\xi),
$$

不依赖代表元的选择，因此是良定义的。又因为 $B$ 线性，对任意 $c\in k$ 都有

$$
\begin{aligned}
\widetilde b\bigl((\xi+\mathcal R)+c(\eta+\mathcal R)\bigr)
&=B(\xi+c\eta)\\
&=B(\xi)+cB(\eta)\\
&=\widetilde b(\xi+\mathcal R)
+c\,\widetilde b(\eta+\mathcal R),
\end{aligned}
$$

所以 $\widetilde b$ 也是线性映射。它还必然是唯一的：若 $L:T\to X$ 也满足 $B=L\circ q$，那么对每个商类都有

$$
L(\xi+\mathcal R)
=L(q(\xi))
=B(\xi)
=\widetilde b(\xi+\mathcal R),
$$

所以 $L=\widetilde b$。这里使用了每个商类都是某个 $q(\xi)$，也就是 $q$ 的满射性。反过来，若 $\mathcal R$ 中存在某个 $r$ 满足 $B(r)\ne0$，即 $R \not\subseteq \ker B$，那么商空间会把 $r$ 与 $0$ 视为同一个元素，而 $B$ 却给它们不同的值；此时下降就不可能成立。

由于 $v\otimes w=q(\langle v,w\rangle)$，这张下降映射满足

$$
\begin{aligned}
\widetilde b(v\otimes w)
&=\widetilde b\bigl(q(\langle v,w\rangle)\bigr)\\
&=B(\langle v,w\rangle)\\
&=b(v,w).
\end{aligned}
$$

也就是说，$\widetilde b\circ\tau=b$。若线性映射 $L:T\to X$ 也满足 $L\circ\tau=b$，那么 $L\circ q$ 与 $B$ 在自由向量空间的每个基向量 $\langle v,w\rangle$ 上取值相同，因而 $L\circ q=B$；上述下降的唯一性随即给出 $L=\widetilde b$。

因此，每条双线性映射 $b:V\times W\to X$ 都给出唯一的线性因子化映射 $\widetilde b:T\to X$。这个商空间实现确实满足张量积的泛性质，因此可以取

$$
V\otimes_kW:=T.
$$

这只是张量积的一个具体实现，不是说张量积必须拥有这一套字面上的底层集合。若 $(T,\tau)$ 与 $(T',\tau')$ 都满足同一泛性质，那么由 $\tau'$ 的双线性，存在唯一线性映射

$$
\phi:T\longrightarrow T'
$$

满足 $\phi\circ\tau=\tau'$；同理存在唯一

$$
\psi:T'\longrightarrow T
$$

满足 $\psi\circ\tau'=\tau$。于是

$$
(\psi\circ\phi)\circ\tau=\tau
=
\operatorname{id}_T\circ\tau.
$$

$$
\psi\circ\phi=\operatorname{id}_T.
$$

同理 $\phi\circ\psi=\operatorname{id}_{T'}$。所以两个实现之间存在唯一一张与典范双线性映射相容的同构。具体构造负责证明存在，泛性质则说明所有实现都通过唯一的相容同构彼此识别。

### 空间、纯张量与诱导映射是三个层次

记号相似时，最容易把下面三类对象混在一起。

第一，$V\otimes_kW$ 是一个向量空间。张量积在这一层以两个向量空间为输入，产生新的向量空间。

第二，$v\otimes w$ 是这个空间中的一个向量，称为纯张量（pure tensor）。它是典范双线性映射 $\tau$ 在有序对 $(v,w)$ 上的值。

第三，若有线性映射

$$
f:V\longrightarrow V',
\qquad
g:W\longrightarrow W',
$$

则规则

$$
(v,w)\longmapsto f(v)\otimes g(w)
$$

是从 $V\times W$ 到 $V'\otimes_kW'$ 的双线性映射。例如，

$$
\begin{aligned}
f(v+v')\otimes g(w)
&=(f(v)+f(v'))\otimes g(w)\\
&=f(v)\otimes g(w)+f(v')\otimes g(w),
\end{aligned}
$$

第二个变量和标量相容性同理。由泛性质，它唯一诱导线性映射

$$
f\otimes g:
V\otimes_kW
\longrightarrow
V'\otimes_kW',
$$

满足

$$
(f\otimes g)(v\otimes w)
=
f(v)\otimes g(w).
$$

因此 $f\otimes g$ 是一张映射，不是一个纯张量。

任意张量都能写成有限个纯张量之和：

$$
t=\sum_{r=1}^m v_r\otimes w_r.
$$

这种分解通常不唯一，也不保证 $t$ 本身能写成单个 $v\otimes w$。若选定 $V$ 的基 $(e_i)_i$ 和 $W$ 的基 $(f_j)_j$，则 $(e_i\otimes f_j)_{i,j}$ 构成张量积基；相对于这组已经选定的基，系数展开才是唯一的。这里的唯一性来自基，不来自任意纯张量分解。

### 例子：双线性型怎样变成一张线性泛函

取

$$
V=W=k^2
$$

并使用标准基 $e_1,e_2$。定义

$$
b:V\times W\longrightarrow k,
\qquad
b(x,y)=x_1y_1+x_2y_2.
$$

这条规则分别对 $x$ 和 $y$ 线性，所以张量积泛性质给出唯一线性泛函

$$
\widetilde b:V\otimes_kW\longrightarrow k
$$

满足

$$
\widetilde b(x\otimes y)=b(x,y).
$$

在张量积基 $(e_i\otimes e_j)_{i,j=1}^2$ 上，

$$
\widetilde b(e_i\otimes e_j)
=
\begin{cases}
1,&i=j,\\
0,&i\ne j.
\end{cases}
$$

因而对

$$
t=\sum_{i,j=1}^2a_{ij}e_i\otimes e_j
$$

有

$$
\widetilde b(t)=a_{11}+a_{22}.
$$

这里我们只在纯张量上给出规则，泛性质保证它已经唯一决定整个张量积上的线性映射。与此同时，$b$ 并不是乘积向量空间 $V\times W\to k$ 上的普通线性映射，因为

$$
(e_1,0)+(0,e_1)=(e_1,e_1),
$$

但

$$
b(e_1,e_1)=1
\ne
b(e_1,0)+b(0,e_1)=0.
$$

这个例子具体显示了“分别线性”为什么需要经过张量积，不能直接当作有序对空间上的普通线性。

## 直和解决什么问题

张量积从一条双线性规则出发。直和的局部数据则是：每个分量上已经各有一张普通线性映射，现在要把它们拼成一张从整体映出的线性映射。

### 从直和映出的泛性质

对两个向量空间 $V,W$，使用外直和的有序对模型：

$$
V\oplus W
=
\{(v,w):v\in V,\ w\in W\}.
$$

典范包含映射为

$$
\iota_V:V\longrightarrow V\oplus W,
\qquad
\iota_V(v)=(v,0),
$$

$$
\iota_W:W\longrightarrow V\oplus W,
\qquad
\iota_W(w)=(0,w).
$$

给定两张线性映射

$$
f:V\longrightarrow X,
\qquad
g:W\longrightarrow X,
$$

定义

$$
[f,g]:V\oplus W\longrightarrow X,
\qquad
[f,g](v,w)=f(v)+g(w).
$$

这张映射是线性的，并满足

$$
[f,g]\circ\iota_V=f,
\qquad
[f,g]\circ\iota_W=g.
$$

它也是唯一满足这两个条件的线性映射。事实上，每个 $(v,w)$ 都有唯一分解

$$
(v,w)=\iota_V(v)+\iota_W(w).
$$

若 $F:V\oplus W\to X$ 具有同样的线性性和 $F\circ \iota_{V}=f,F\circ\iota_{W}=g$，则

$$
\begin{aligned}
F(v,w)
&=F\bigl(\iota_V(v)+\iota_W(w)\bigr)\\
&=f(v)+g(w)\\
&=[f,g](v,w).
\end{aligned}
$$

因此，限制到两个典范分量给出一一对应

$$
\operatorname{Hom}_k(V\oplus W,X)
\longrightarrow
\operatorname{Hom}_k(V,X)\times\operatorname{Hom}_k(W,X),
$$

$$
F\longmapsto
(F\circ\iota_V,F\circ\iota_W),
$$

其逆方向把 $(f,g)$ 送到 $[f,g]$。这就是二元直和的映出（mapping-out）泛性质。

对任意指标族 $(V_i)_{i\in I}$，直和只允许有限多个分量同时非零：

$$
\bigoplus_{i\in I}V_i
=
\left\{
(v_i)_{i\in I}:
v_i\in V_i,\quad
v_i\ne0\text{ 的指标只有有限多个}
\right\}.
$$

因此任意一族线性映射 $f_i:V_i\to X$ 都唯一拼成

$$
[f_i]_{i\in I}:
\bigoplus_{i\in I}V_i
\longrightarrow X,
$$

$$
[f_i]_{i\in I}\bigl((v_i)_i\bigr)
=
\sum_i f_i(v_i),
$$

右边总是有限和。同理，相应的泛性质是

$$
\operatorname{Hom}_k
\left(
\bigoplus_{i\in I}V_i,X
\right)
\cong
\prod_{i\in I}
\operatorname{Hom}_k(V_i,X).
$$

这时直和称为这一族对象的余积（coproduct）。

### 有限直和还可以从外部映入

二元直和还有典范投影

$$
\pi_V:V\oplus W\longrightarrow V,
\qquad
\pi_V(v,w)=v,
$$

$$
\pi_W:V\oplus W\longrightarrow W,
\qquad
\pi_W(v,w)=w.
$$

给定

$$
a:X\longrightarrow V,
\qquad
b:X\longrightarrow W,
$$

存在唯一线性映射

$$
\langle a,b\rangle:
X\longrightarrow V\oplus W,
\qquad
\langle a,b\rangle(x)=(a(x),b(x)),
$$

满足

$$
\pi_V\circ\langle a,b\rangle=a,
\qquad
\pi_W\circ\langle a,b\rangle=b.
$$

若 $h:X\to V\oplus W$ 也有这两个投影，那么 $h(x)$ 的两个坐标只能分别是 $a(x)$ 与 $b(x)$，所以 $h=\langle a,b\rangle$。因此还有

$$
\operatorname{Hom}_k(X,V\oplus W)
\cong
\operatorname{Hom}_k(X,V)\times
\operatorname{Hom}_k(X,W).
$$

有限多个向量空间的直和与直积典范同构，因而有限直和同时满足余积的映出泛性质和积的映入泛性质，称为双积（biproduct）。

无限族时必须分开。无限直和仍然是余积，只满足映出泛性质不满足映入泛性质，而无限直积

$$
\prod_{i\in I}V_i
$$

才满足完整的积泛性质

$$
\operatorname{Hom}_k
\left(
X,\prod_{i\in I}V_i
\right)
\cong
\prod_{i\in I}\operatorname{Hom}_k(X,V_i).
$$

无限直和虽然也有每个坐标投影，却不能仅凭这些投影成为积。举例来说，取 $X=k$ 且对每个 $i\in\mathbb N$ 令 $V_i=k$，再令所有

$$
a_i:X\longrightarrow V_i
$$

都是恒等映射。若这些映射能够拼成 $a:k\to\bigoplus_i k$，那么必须有

$$
a(1)=(1,1,1,\ldots),
$$

但这个向量不是有限支撑的，因而不属于直和。相同的坐标族却确实定义了一张到直积的映射。

## 两种泛性质的分工

前两节可以压缩成下面的对照，但表格中的结论都依赖已经完成的定义与唯一性论证。

| 问题 | 张量积 | 直和 |
|---|---|---|
| 局部输入 | 双线性 $b:V\times W\to X$ | 线性族 $f_i:V_i\to X$ |
| 典范映射 | $\tau:V\times W\to V\otimes_kW$ | $\iota_i:V_i\to\bigoplus_iV_i$ |
| 得到的整体映射 | $\widetilde b:V\otimes_kW\to X$ | $[f_i]:\bigoplus_iV_i\to X$ |
| 需要验证 | 对两个变量分别线性 | 每个 $f_i$ 线性 |
| 唯一性的来源 | 纯张量生成张量积 | 每个元素有有限分量分解 |

张量积先把“两个输入共同决定一个输出”的双线性规则变成线性映射。直和则把“不同来源各自已有的线性映射”拼到同一个目标。它们不是两种可互换的记号：若局部规则尚未证明双线性，就不能调用张量积泛性质；若每个分量上的线性映射尚未构造出来，也没有可供直和泛性质拼接的数据。

普通张量积怎样与直和分配，并由这两种泛性质构造完整的正反同构，见 [[Tensor product 对 direct sum 的分配律]]。这里后续只使用“先线性化每个双线性规则，再拼接各个直和分量”这一接口。

## 四种相似符号属于不同空间

方括号和张量符号同时出现时，应先确定每个对象所在的空间。

设 $U\subseteq V$、$S\subseteq W$ 是子空间。因为 $k$ 是域，通过包含映射诱导的映射可以把 $U\otimes_kW$ 和 $V\otimes_kS$ 视为 $V\otimes_kW$ 的子空间。记

$$
N=U\otimes_kW+V\otimes_kS.
$$

现在四个相似表达式的 ambient space 分别是：

- $(v,w)\in V\times W$；在二元外直和的有序对模型中，它也对应 $V\oplus W$ 的元素。
- $v\otimes w\in V\otimes_kW$。
- $[v]\otimes[w]\in(V/U)\otimes_k(W/S)$，其中 $[v]=v+U$、$[w]=w+S$。
- $[v\otimes w]\in(V\otimes_kW)/N$。

第三个表达式先分别取商再张量，第四个表达式先张量再取商；它们不是字面上的同一个对象。关键是规则

$$
([v],[w])
\longmapsto
[v\otimes w]
$$

确实只依赖商类：若把 $v$ 改成 $v+u$，其中 $u\in U$，目标变化为 $[u\otimes w]=0$，因为 $u\otimes w\in N$；若把 $w$ 改成 $w+s$，其中 $s\in S$，变化同样落入 $N$。

因此这是一条良定义的双线性规则，由张量积泛性质得到典范线性映射

$$
(V/U)\otimes_k(W/S)
\longrightarrow
(V\otimes_kW)/N,
\qquad
[v]\otimes[w]\longmapsto[v\otimes w].
$$

在域 $k$ 上，这张典范映射是同构，所以

$$
(V/U)\otimes_k(W/S)
\cong
\frac{V\otimes_kW}
{U\otimes_kW+V\otimes_kS}.
$$

这个结论也说明目标为什么必须再商掉 $N$：代表元改变在 $V\otimes_kW$ 中一般不是零，只是在模去 $N$ 后才消失。

对一般的、可以非交换的环 $R$，必须先固定左右模侧别：约定 $U\subseteq V$ 是右 $R$-子模，$S\subseteq W$ 是左 $R$-子模。此时两张诱导映射

$$
U\otimes_R W\longrightarrow V\otimes_R W,
\qquad
V\otimes_R S\longrightarrow V\otimes_R W
$$

未必单射，因此安全写法是使用它们在 ambient tensor product $V\otimes_R W$ 中的像，而不能无条件把 $U\otimes_R W$ 或 $V\otimes_R S$ 本身称为其中的子模。若 $W$ 是平坦左 $R$-模，则第一张诱导映射单射；若 $V$ 是平坦右 $R$-模，则第二张诱导映射单射，此时才可以分别把相应张量积与它们在 $V\otimes_R W$ 中的像识别。

方括号本身从不说明商掉了什么；必须连同所在商空间一起读取。下一节的 $[c\otimes d]$ 将表示模去边界后的同调类，而不是本节模去 $N$ 的商类。

## Künneth 接口：先验证，再线性化，最后拼接

Künneth 比较映射正好连续使用前面的两种泛性质。关键是顺序不能颠倒：必须先证明同调类上的规则有定义，才能用张量积泛性质；必须先得到每个 $(p,q)$ 分量上的线性映射，才能用直和泛性质把它们拼起来。

设 $C_\bullet,D_\bullet$ 是域 $k$ 上的链复形，采用降低次数的链约定。乘积复形按总次数（total degree）取

$$
(C\otimes_kD)_n
=
\bigoplus_{p+q=n}C_p\otimes_kD_q,
$$

并在齐次元素上使用 Koszul 边界

$$
\partial(c\otimes d)
=
\partial_Cc\otimes d
+
(-1)^p c\otimes\partial_Dd,
\qquad
c\in C_p.
$$

总次数分层与边界平方为零的完整构造见 [[Cochain complex 的 tensor product]]；这里仅使用这条公式构造比较映射。

### 第一步：先证明 $c\otimes d$ 是闭链

取

$$
c\in Z_p(C),
\qquad
d\in Z_q(D).
$$

也就是说，

$$
\partial_Cc=0,
\qquad
\partial_Dd=0.
$$

代入乘积边界，

$$
\partial(c\otimes d)
=
0\otimes d
+
(-1)^pc\otimes0
=
0.
$$

所以 $c\otimes d$ 是总次数 $p+q$ 的闭链（cycle）。只有完成这一步以后，记号

$$
[c\otimes d]
\in
H_{p+q}(C\otimes_kD)
$$

才有定义。

### 第二步：检查两个因子的代表元变化

同调类 $[c]$ 不是某个固定闭链，而是所有相差边界（boundary）的闭链所组成的等价类。若

$$
c'=c+\partial_Cx,
\qquad
x\in C_{p+1},
$$

则因为 $\partial_Dd=0$，

$$
\partial(x\otimes d)
=
\partial_Cx\otimes d.
$$

因此

$$
c'\otimes d-c\otimes d
=
\partial(x\otimes d)
$$

是乘积复形中的边界。

若

$$
d'=d+\partial_Dy,
\qquad
y\in D_{q+1},
$$

则因为 $\partial_Cc=0$，

$$
\partial(c\otimes y)
=
(-1)^p c\otimes\partial_Dy,
$$

所以

$$
c\otimes d'-c\otimes d
=
c\otimes\partial_Dy
=
(-1)^p\partial(c\otimes y)
$$

同样是边界。逐个因子改变代表元都不改变目标同调类，连续改变两个因子也就不改变结果。

于是规则

$$
\beta_{p,q}:
H_p(C)\times H_q(D)
\longrightarrow
H_{p+q}(C\otimes_kD),
$$

$$
\beta_{p,q}([c],[d])
=
[c\otimes d]
$$

良定义。它还对两个变量分别线性。例如，若 $c_1,c_2\in Z_p(C)$，则

$$
\begin{aligned}
\beta_{p,q}([c_1]+[c_2],[d])
&=[(c_1+c_2)\otimes d]\\
&=[c_1\otimes d]+[c_2\otimes d],
\end{aligned}
$$

标量相容性以及第二个变量的验证相同。因此 $\beta_{p,q}$ 是一张双线性映射。

### 第三步：用张量积泛性质线性化

现在才可以调用张量积泛性质。它给出唯一线性映射

$$
\kappa_{p,q}:
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_{p+q}(C\otimes_kD)
$$

满足

$$
\kappa_{p,q}([c]\otimes[d])
=
[c\otimes d].
$$

泛性质完成的是从双线性 $\beta_{p,q}$ 到线性 $\kappa_{p,q}$ 的因子化。它没有替代前两步的闭链检查和代表元无关性检查。

### 第四步：用直和泛性质拼成总次数映射

固定总次数 $n$。对每一对 $p+q=n$，已经有一张同目标的线性映射

$$
\kappa_{p,q}:
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_n(C\otimes_kD).
$$

令

$$
\iota_{p,q}:
H_p(C)\otimes_kH_q(D)
\longrightarrow
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D)
$$

为典范包含映射。由直和的映出泛性质，所有 $\kappa_{p,q}$ 唯一拼成

$$
\kappa_n:
\bigoplus_{p+q=n}
H_p(C)\otimes_kH_q(D)
\longrightarrow
H_n(C\otimes_kD),
$$

并满足

$$
\kappa_n\circ\iota_{p,q}
=
\kappa_{p,q}.
$$

对一个只有有限多个非零分量的元素，$\kappa_n$ 就是把各分量的像相加。

到这里证明的是比较映射存在且有明确公式，并没有证明它是同构。在线性化阶段，张量积泛性质只保证唯一的因子化映射；在拼接阶段，直和泛性质只保证唯一的整体映射。单射、满射以及与链映射的自然相容性需要另行证明。在 [[Künneth 分解]] 采用的有界有限维、系数为域的条件下，$\kappa_n$ 进一步是自然同构；一般环上的 $\operatorname{Tor}$、谱序列和扩张边界也由该笔记处理。

## HGP 接口：内层张量积与外层直和

现在专门取

$$
k=\mathbb F_2
$$

并采用 [[Hypergraph product code]] 中的降次数链约定。把两张二进制矩阵放进二项链复形

$$
\mathcal A:
0\longrightarrow A_1\xrightarrow{A}A_0\longrightarrow0,
$$

$$
\mathcal B:
0\longrightarrow B_1\xrightarrow{B}B_0\longrightarrow0.
$$

记乘积链复形为

$$
\mathcal C
=
\mathcal A\otimes_{\mathbb F_2}\mathcal B.
$$

它按

$$
C_r
=
\bigoplus_{p+q=r}A_p\otimes_{\mathbb F_2}B_q
$$

分层。总次数 $1$ 有两种来源，因此

$$
C_1
=
(A_1\otimes_{\mathbb F_2}B_0)
\oplus
(A_0\otimes_{\mathbb F_2}B_1).
$$

这条公式中，两种运算承担不同工作。

内层张量积配对两个因子的坐标。若 $e_j$ 是 $A_1$ 的基向量、$f_\alpha$ 是 $B_0$ 的基向量，那么

$$
e_j\otimes f_\alpha
$$

由坐标对 $(j,\alpha)$ 标记。另一个分量中的基向量则由 $A_0$ 与 $B_1$ 的坐标配对。选定基以后，因子映射的张量所对应的矩阵表现为 Kronecker 分块。

外层直和不再把两个坐标相乘，而是保留总次数 $1=1+0$ 与 $1=0+1$ 的两种来源。一个物理支撑向量唯一写成

$$
(u,v),
\qquad
u\in A_1\otimes_{\mathbb F_2}B_0,
\quad
v\in A_0\otimes_{\mathbb F_2}B_1.
$$

在 HGP 的 CSS 翻译中，这两个直和分量是取核和取商以前的两类物理量子比特坐标。

直和泛性质还解释了 HGP 分块矩阵的拼接方式。边界

$$
\partial_1:C_1\longrightarrow C_0
$$

只要分别给出在两个直和分量上的限制，就被唯一确定；选定基以后，这表现为两个矩阵块的横向拼接。反过来，边界

$$
\partial_2:C_2\longrightarrow C_1
$$

由落入两个直和分量的分量映射确定；由于这里是有限直和，也可使用它的积泛性质，矩阵上表现为两个块的竖直堆叠。完整的四个分块、转置约定与 CSS 对易证明见 [[Hypergraph product code]]，这里不重复展开。

物理直和分量不能与 Künneth 给出的逻辑直和项混称。HGP 的逻辑 $Z$ 支撑类位于

$$
H_1(\mathcal C)
=
\frac{\ker\partial_1}{\operatorname{im}\partial_2}.
$$

在域 $\mathbb F_2$ 上，Künneth 同构进一步给出

$$
H_1(\mathcal A\otimes_{\mathbb F_2}\mathcal B)
\cong
\ker A\otimes_{\mathbb F_2}\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes_{\mathbb F_2}\ker B.
$$

其中

$$
\operatorname{coker}A=A_0/\operatorname{im}A,
\qquad
\operatorname{coker}B=B_0/\operatorname{im}B.
$$

左边先在整个物理空间 $C_1$ 中满足闭链条件，再商掉边界；右边的两个直和项描述所得同调类的两种逻辑来源。虽然每一类可以在相应的物理分量中选择初始代表元，但给代表元加上一个边界后，同一个逻辑类可能同时占据两个物理分量。因此：

$$
\text{链群中的两个物理分量}
\ne
\text{同调中的两个 Künneth 逻辑来源}.
$$

## 几个相邻构造的边界

普通张量积、矩阵 Kronecker 积、乘积复形、同调商空间和平衡张量积经常出现在相邻公式中，但它们发生在不同层次。

**普通张量积。** $V\otimes_kW$ 只使用共同基域上的线性结构，并把任意 $k$-双线性规则唯一线性化。它本身还没有次数、边界映射或同调。

**矩阵 Kronecker 积。** 对线性映射 $f,g$，先由泛性质得到 $f\otimes g$。选定相容的基和坐标排序以后，$f\otimes g$ 的矩阵才写成两张矩阵的 Kronecker 积。矩阵块是诱导映射的坐标表示，不是张量积泛性质本身。

**乘积复形的总次数化。** 从普通张量块 $C_p\otimes_kD_q$ 出发，还要按照 $p+q=n$ 用直和收集同一总次数的分量，并加入带 Koszul 符号的边界，才得到 $C_\bullet\otimes_kD_\bullet$。这一步见 [[Cochain complex 的 tensor product]]。

**同调商空间。** 记号 $[c\otimes d]$ 只有在 $c\otimes d$ 已经是闭链后才表示同调类；随后还要把相差边界的闭链识别。这个商发生在乘积复形已经构造好之后。

**平衡张量积。** 若 $R$ 是一个 $k$-代数，$M_R$ 是右 $R$-模、${}_RN$ 是左 $R$-模，则

$$
M_R\otimes_R{}_RN
=
\frac{M\otimes_kN}
{\left\langle
(m\cdot r)\otimes n-m\otimes(r\cdot n):
m\in M,\ n\in N,\ r\in R
\right\rangle}.
$$

它只对满足

$$
B(m\cdot r,n)=B(m,r\cdot n)
$$

的 $R$-平衡双线性映射具有相应泛性质。这里新增了共享环作用及其左右侧别，不能把普通 $k$-双线性泛性质无条件搬过来。若还要形成平衡张量积链复形，则两个微分必须分别对第一因子的右 $R$-作用和第二因子的左 $R$-作用线性；这保证平衡关系被微分保持，商微分才能下降到平衡张量积上，完整验证见 [[Balanced tensor product 与 coinvariant quotient]]。平衡关系先在链群层构造新的商复形，之后才在该复形中取同调；它与“商掉边界”不是同一个商。

提升乘积码使用的正是带模结构的平衡张量积，并进一步涉及环值 Kronecker 分块、反对合和二进制展开；它不是把 HGP 中的普通 $\mathbb F_2$-张量积只换一个下标。具体构造条件见 [[Lifted product code]]。

## 回收主线

遇到“局部公式怎样成为整体映射”时，可以按固定顺序检查。

1. 先确认局部规则在当前对象上确有定义。若输入是商类，要检查代表元无关；若目标是同调类，要先检查闭链性；若在 $R$ 上取张量，还要检查平衡关系；若还要形成平衡张量积链复形，则还要确认两个微分分别对相应的右／左 $R$-作用线性，使平衡关系能被微分保持。
2. 再确认规则对两个变量分别线性。完成这一步后，张量积泛性质才给出唯一的线性化映射。
3. 若同一总次数含有多个来源，分别构造每个直和分量上的线性映射，再用直和泛性质把它们唯一拼成整体映射。

在 Künneth 中，这条顺序具体成为

$$
\text{闭链与代表元检查}
\longrightarrow
\kappa_{p,q}
\longrightarrow
\kappa_n.
$$

在 HGP 中，内层张量积负责配对两个因子的坐标，外层直和负责保留不同的总次数来源。前者回答“双线性规则怎样线性化”，后者回答“各分量映射怎样拼接”；只有把这两项工作分开，乘积链群、比较映射和逻辑同调的层次才会保持清楚。
