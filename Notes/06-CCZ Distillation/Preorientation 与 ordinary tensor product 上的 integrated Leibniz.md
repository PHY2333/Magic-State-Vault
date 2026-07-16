[[Cup product 与 Leibniz rule]] 说明了 cochain-level Leibniz rule 如何让 cup product 下降到 cohomology。这里从 classical two-term seed

$$
C^0(X;\mathbb F_2)\xrightarrow{\delta}C^1(X;\mathbb F_2)
$$

出发，用 preorientation 定义局部 cup product。这个乘法不必满足完整的 cochain-level Leibniz rule；构造 product code 上的数值相位时，只需相应的 Leibniz 展开在 integral 之后消失。Breuckmann 等人的 fixed-factor 证明把这条 seed 条件带到 ordinary tensor product，并进一步保证积分后的多重乘积不依赖 cohomology representative。

本文到 ordinary tensor-product 分支为止。Balanced quotient 上的 free-basis averaging、relative-translate operation 与 inherited integrated Leibniz 见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；Menon 的 symmetric triple bracketing 和 physical $CCZ$ 判据见 [[Symmetric triple cup-product]]。

---
### Classical seed 与 parity integral

取有限集合 $X^0$ 和 $X^1$。在 Tanner graph 中，$X^0$ 标记 classical parity checks，$X^1$ 标记 classical bits；在 parity-check matrix 中，$X^0$ 标记行标签，$X^1$ 标记列标签。若 parity-check matrix 为

$$
H=(h_{u,x})_{u\in X^0,\,x\in X^1},
$$

则在 column-vector 约定下，check-to-bit coboundary map 是

$$
\delta=H^T:
\mathbb F_2^{X^0}\longrightarrow\mathbb F_2^{X^1}.
$$

同一个符号 $u\in X^0$、$x\in X^1$ 也表示相应的 basis cochain。对 basis check $u$，

$$
\delta u=\sum_{x\in X^1}h_{u,x}x.
$$

记这个 support 为

$$
N(u):=\operatorname{supp}(\delta u)
=\{x\in X^1:h_{u,x}=1\}.
$$

这里的 $x$ 是 seed bit，不是 product code 的 physical qubit。

假设每个 check support 都有偶数个 bits。此时可以定义 seed parity integral

$$
\int_1:C^1(X;\mathbb F_2)\longrightarrow\mathbb F_2,
\qquad
\int_1\left(\sum_{x\in X^1}r_xx\right)
=\sum_{x\in X^1}r_x\pmod 2.
$$

偶重量假设保证

$$
\int_1\delta u=|N(u)|=0\pmod 2.
$$

由线性性，$\int_1$ 在整个 $\operatorname{im}\delta$ 上都为零。若存在奇重量 check，上面的 coefficient-sum map 就不能作为这个 complex 的 integral。

---
### Preorientation

Coboundary $\delta u$ 只记录 check $u$ 接触哪些 seed bits。为了定义 mixed-degree cup product，还要指定这些 bits 在 check 出现在 cup product 左侧或右侧时怎样被保留。

Preorientation 为每个 basis check 选择不交分解

$$
N(u)
=
N_{\mathrm{in}}(u)
\sqcup
N_{\mathrm{out}}(u)
\sqcup
N_{\mathrm{free}}(u).
$$

后面的例子会看到本质是定义有向图。
用这些集合的 indicator cochains 记

$$
\delta_{\mathrm{in}}u
=\sum_{x\in N_{\mathrm{in}}(u)}x,
\qquad
\delta_{\mathrm{out}}u
=\sum_{x\in N_{\mathrm{out}}(u)}x,
\qquad
\delta_{\mathrm{free}}u
=\sum_{x\in N_{\mathrm{free}}(u)}x.
$$

于是

$$
\delta u
=
\delta_{\mathrm{in}}u
+\delta_{\mathrm{out}}u
+\delta_{\mathrm{free}}u.
$$

这个分解没有改变 $H$ 或 $\delta$；它为同一个 coboundary support 增加了 cup-product 数据。

在 basis cochains 上定义

$$
u\cup v=
\begin{cases}
u,&u=v,\\
0,&u\ne v,
\end{cases}
\qquad u,v\in X^0,
$$

以及

$$
u\cup x=
\begin{cases}
x,&x\in N_{\mathrm{out}}(u),\\
0,&\text{otherwise},
\end{cases}
\qquad u\in X^0,\ x\in X^1,
$$

$$
x\cup u=
\begin{cases}
x,&x\in N_{\mathrm{in}}(u),\\
0,&\text{otherwise},
\end{cases}
\qquad x\in X^1,\ u\in X^0.
$$

没有列出的 basis products 取 $0$，再按 $\mathbb F_2$ 双线性延拓。特别地，$C^1\cup C^1=0$，因为 two-term seed 没有 $C^2$。

因此 `out` 表示 check 位于 bit 左侧时允许保留的部分，`in` 表示 check 位于 bit 右侧时允许保留的部分。它们描述 cup product 中 factors 的次序，不表示 physical information flow。Free bits 仍属于完整的 $\delta u$，但两条 mixed-degree 规则都不直接读取它们。

---
### 多重局部乘积

先考虑所有 factors 都在 degree $0$ 的情形。由 $C^0$ 上的对角乘法，对 basis checks 有

$$
u_1\cup\cdots\cup u_\ell
=
\begin{cases}
u_1,&u_1=\cdots=u_\ell,\\
0,&\text{otherwise}.
\end{cases}
$$

这个乘法在 $C^0$ 上结合，再按 $\mathbb F_2$ 多线性延拓。若至少有两个 degree-$1$ factors，则乘积为 $0$，因为 two-term seed 没有 degree $2$。

剩下需要规定的是恰有一个 degree-$1$ factor 的情形。包含 mixed degrees 的完整二元乘法一般不结合，因此采用随这个 factor 的位置变化的运算顺序，使计算过程中不会先把两个 degree-$0$ factors 相乘。例如三重乘积约定为

$$
x\cup u\cup v:=(x\cup u)\cup v,
$$

$$
u\cup x\cup v:=(u\cup x)\cup v,
$$

$$
u\cup v\cup x:=u\cup(v\cup x).
$$

一般地，若 $x\in X^1$ 位于第 $j$ 个位置，而其余 $u_i\in X^0$，这个 position-dependent 约定给出

$$
u_1\cup\cdots\cup u_{j-1}\cup x\cup u_{j+1}\cup\cdots\cup u_\ell
=
\begin{cases}
x,&
x\in
\displaystyle
\bigcap_{i<j}N_{\mathrm{out}}(u_i)
\cap
\bigcap_{k>j}N_{\mathrm{in}}(u_k),\\[1.2ex]
0,&\text{otherwise}.
\end{cases}
$$

当 $j=1$ 或 $j=\ell$ 时，缺少的一侧交集按整个 $X^1$ 处理。左侧 checks 全部用 out pieces 筛选，右侧 checks 全部用 in pieces 筛选。含有两个 degree-$1$ factors 的乘积落在不存在的 degree $2$，因而为零。

若对任意不同的 $u,v\in X^0$ 还有

$$
N_{\mathrm{in}}(u)\cap N_{\mathrm{in}}(v)=\varnothing,
\qquad
N_{\mathrm{out}}(u)\cap N_{\mathrm{out}}(v)=\varnothing,
$$

则二元 cup product 本身结合，括号不再影响结果。一般情形不假设这个 non-overlapping condition，所以上面的多重运算顺序是定义的一部分。

---
### Integrated Leibniz rule

普通 Leibniz rule 要求 Leibniz 展开 $\delta x \cup y+x \cup \delta y$ 在 cochain 层等于一个 coboundary。Preorientation 定义的乘法可能不满足这个等式；较弱的要求是 Leibniz 展开经过 $\int_1$ 后为零。

对 $a_1,\ldots,a_\ell\in C^0$ 或 $C^{1}$，若

$$
\int_1
\sum_{j=1}^{\ell}
a_1\cup\cdots\cup\delta(a_j)\cup\cdots\cup a_\ell
=0,
$$

就称这个 $\ell$ 重乘积满足 integrated Leibniz rule。每一项都使用上一节的 position-dependent 运算顺序。

在 two-term seed 上，$\delta(C^1)=0$，而含两个 degree-$1$ factors 的乘积也为零。因此由多线性性，只需检查 $a_1,\ldots,a_\ell$ 为 basis checks $u_1,\ldots,u_\ell\in X^0$ 的情形。对 preorientation 乘法，一个充分判据是

$$
\sum_{j=1}^{\ell}
\left|
\left(\bigcap_{i<j}N_{\mathrm{out}}(u_i)\right)
\cap N(u_j)\cap
\left(\bigcap_{k>j}N_{\mathrm{in}}(u_k)\right)
\right|
=0
\pmod 2
$$

对所有允许重复的 $u_1,\ldots,u_\ell\in X^0$ 成立。

推导过程就是第 $j$ 项把 $\delta(u_{j})$ 作为 support $N(u_j)$，展开成 support $x$ 的并集，其余 checks 再使用 in/out pieces。因此 $N_{\mathrm{free}}(u_j)$ 虽然不出现在 mixed-degree cup product 的筛选规则中，仍会进入这个判据。

当 $\ell=1$ 时，判据退化为

$$
|N(u)|=0\pmod2,
$$

即 $\delta u$ 这个 coboundary 经过 integral 读数以后变成 0。

当 $\ell=2$ 时，判据是

$$
|N(u)\cap N_{\mathrm{in}}(v)|
+|N_{\mathrm{out}}(u)\cap N(v)|
=0
\pmod2.
$$

把两个完整 supports 按 in/out/free 展开后，重复出现的
$N_{\mathrm{out}}(u)\cap N_{\mathrm{in}}(v)$ 抵消，留下

$$
\begin{aligned}
0={}&
|N_{\mathrm{in}}(u)\cap N_{\mathrm{in}}(v)|
+|N_{\mathrm{free}}(u)\cap N_{\mathrm{in}}(v)|\\
&+
|N_{\mathrm{out}}(u)\cap N_{\mathrm{out}}(v)|
+|N_{\mathrm{out}}(u)\cap N_{\mathrm{free}}(v)|
\pmod2.
\end{aligned}
$$

这四项显示了 free pieces 对 integrated Leibniz 的影响。

---
### 定向图例子

普通 graph orientation 是 preorientation 的标准模型。取三个 checks

$$
X^0=\{u,v,w\}
$$

和三条形成有向环的 seed bits

$$
u\xrightarrow{x_{uv}}v,
\qquad
v\xrightarrow{x_{vw}}w,
\qquad
w\xrightarrow{x_{wu}}u.
$$

这表示同一个 degree-1 基元素 $x_{uv}$​ 同时出现在两个 checks 的 coboundary support 里。

再给每个 check $p\in\{u,v,w\}$ 添加两个只放在 free part 中的 bits $s_p,t_p$。例如

$$
N(u)=\{x_{wu},x_{uv},s_u,t_u\},
$$

并取

$$
N_{\mathrm{in}}(u)=\{x_{wu}\},
\qquad
N_{\mathrm{out}}(u)=\{x_{uv}\},
\qquad
N_{\mathrm{free}}(u)=\{s_u,t_u\}.
$$

$v,w$ 处按循环方式作相同选择。每个 check 有一条 incoming edge 和一条 outgoing edge，二者数量同奇偶；free bits 与三条有向 edges 不相交。

局部乘法读取 edge 的方向：

$$
u\cup x_{uv}=x_{uv},
\qquad
x_{uv}\cup v=x_{uv},
$$

而

$$
x_{uv}\cup u=0,
\qquad
v\cup x_{uv}=0.
$$

所以

$$
(u\cup x_{uv})\cup v=x_{uv}
$$

表示 $x_{uv}$ 同时通过左侧 $u$ 的 out test 和右侧 $v$ 的 in test。

这个例子也区分了普通 Leibniz 与 integrated Leibniz。由 $u\cup u=u$，普通 Leibniz 左边为

$$
\delta(u\cup u)
=\delta u
=x_{wu}+x_{uv}+s_u+t_u,
$$

而右边只有

$$
(\delta u)\cup u+u\cup(\delta u)
=x_{wu}+x_{uv}.
$$

两者在 cochain 层并不相等；free pair 正是差别。不过

$$
\int_1\bigl((\delta u)\cup u+u\cup(\delta u)\bigr)
=1+1=0,
$$

所以 $u,u$ 通过二重 integrated Leibniz 检查。对相邻的 $u,v$，

$$
(\delta u)\cup v=x_{uv},
\qquad
u\cup(\delta v)=x_{uv},
$$

两项直接在 $\mathbb F_2$ 中抵消。更一般地，Breuckmann 等人的 oriented-graph criterion 说明：若每个 vertex 的 incoming 与 outgoing edges 数量同奇偶，并把图外的 incident bits 放入 free part，就得到满足相应 integrated Leibniz 判据的 preorientation。上面的计算展示了这个判据在低阶时怎样工作。

---
### Ordinary tensor product 上的 integrated Leibniz

以下取 $\ell$ 个 two-term seed complexes，并在每个 seed 上使用 $\ell$ 重局部乘积。相应的 product complex 最高 degree 也是 $\ell$，因此 $\ell$ 个 degree-$1$ cochains 的乘积恰好落在 top degree。这是本节中 seed 数量、乘积 arity 和 integral degree 都记为 $\ell$ 的约定。

#### Seed 数据与 $\ell$ 的约定

设有 $\ell$ 个 two-term seed complexes

$$
C_{(s)}^0\xrightarrow{\delta^{(s)}}C_{(s)}^1,
\qquad
s=1,\ldots,\ell.
$$

第 $s$ 个 seed 沿用前文完整的局部 $\ell$ 重乘积，记为

$$
\mu_s\left(a_1^{(s)},\ldots,a_\ell^{(s)}\right)
=
a_1^{(s)}\cup_s\cdots\cup_s a_\ell^{(s)}.
$$

这里全在 $C_{(s)}^0$、恰有一个 factor 在 $C_{(s)}^1$、至少两个 factors 在 $C_{(s)}^1$ 的三种 degree patterns，分别使用对角乘积、position-dependent 规则和零乘积。第 $s$ 个 seed 还带有一维 integral

$$
\int_1^{(s)}:C_{(s)}^1\longrightarrow\mathbb F_2,
$$

并约定它在 $C_{(s)}^0$ 上取 $0$。假设局部乘积满足 seed integrated Leibniz rule：对任意 homogeneous

$$
a_j^{(s)}\in C_{(s)}^{p_j^{(s)}},
\qquad
p_j^{(s)}\in\{0,1\},
$$

都有

$$
\int_1^{(s)}
\sum_{j=1}^{\ell}
a_1^{(s)}\cup_s\cdots\cup_s
\delta^{(s)}a_j^{(s)}
\cup_s\cdots\cup_s a_\ell^{(s)}
=
0.
$$

#### Product complex 上的 cup product 与 top-degree integral

令

$$
\underline C
=
\bigotimes_{s=1}^{\ell}C_{(s)}.
$$

对 homogeneous pure tensors

$$
y_j
=
\bigotimes_{s=1}^{\ell}y_j^{(s)},
\qquad
j=1,\ldots,\ell,
$$

下标 $j$ 标记 seed complex $\ell$ 重乘积中的第 $j$ 个 argument，下标 $s$ 标记 $y_j$ 在第 $s$ 个 seed complex 中的 tensor factor。

在 $\mathbb F_2$ 上，product coboundary 为

$$
\underline\delta y_j
=
\sum_{s=1}^{\ell}\delta_s y_j,
$$

其中

$$
\delta_s y_j
=
y_j^{(1)}\otimes\cdots\otimes
\delta^{(s)}y_j^{(s)}
\otimes\cdots\otimes y_j^{(\ell)}.
$$

一般系数下，$\delta_s$ 前还带有由左侧 factors 的 degrees 决定的 Koszul sign；这里因为 $-1=1$ 而消失。Total degree 与 product coboundary 的约定见 [[Cochain complex 的 tensor product]]。

Product complex 上的 $\ell$ 重乘积直接定义为各局部 $\ell$ 重乘积的外张量积：

$$
y_1\cup\cdots\cup y_\ell
=
\bigotimes_{s=1}^{\ell}
\mu_s\left(y_1^{(s)},\ldots,y_\ell^{(s)}\right).
$$

这条公式按每个 argument $y_{j}$ 多线性延拓，定义整个 $\underline C$ 上的 $\ell$-linear product。

这个定义先把属于同一个 seed complex 的 factors 配在一起，再应用对应的 position-dependent $\ell$ 重乘积。一般系数下，重排 homogeneous factors 会产生 Koszul signs；二元特例为

$$
(a\otimes b)\cup(c\otimes d)
=
(-1)^{|b||c|}
(a\cup c)\otimes(b\cup d).
$$

在 $\mathbb F_2$ 上这些 signs 都等于 $1$。非结合情形以逐 seed 给出的 $\ell$-linear maps $\mu_s$ 为基本定义，不要求它们来自某个统一括号顺序的二元迭代。这是 Breuckmann 等人 Eq. (5) 在当前多重乘积约定下的形式。

每个 seed 最高只有 degree $1$，所以 $\underline C$ 的最高层为

$$
\underline C^\ell
=
\bigotimes_{s=1}^{\ell}C_{(s)}^1.
$$

Product top-degree integral 定义为

$$
\int_\ell:
\underline C^\ell\longrightarrow\mathbb F_2,
\qquad
\int_\ell
\left(
\bigotimes_{s=1}^{\ell}b^{(s)}
\right)
=
\prod_{s=1}^{\ell}
\int_1^{(s)}b^{(s)},
$$

再按线性延拓。下文同时采用零延拓约定：

$$
\int_\ell\big|_{\underline C^q}=0,
\qquad q\ne\ell.
$$

对任意 homogeneous pure tensor

$$
b=b^{(1)}\otimes\cdots\otimes b^{(\ell)},
$$

局部与 product integral 的零延拓给出统一公式

$$
\int_\ell b
=
\prod_{s=1}^{\ell}\int_1^{(s)}b^{(s)}.
$$

若某个 local factor 在 degree $0$，等式两边都为 $0$；若所有 local factors 都在 degree $1$，公式就是 top-degree integral 的定义。

下一节把 $\underline\delta=\sum_s\delta_s$ 代入 Leibniz 和并固定 $s$ 后，这个逐 factor 公式会把 global readout 分解为第 $s$ 个局部 Leibniz 和的 integral 与其余固定局部乘积的 integrals 之积。

#### Integrated Leibniz 的继承命题

Product complex 上的 Leibniz 和记为

$$
\mathcal L(y_1,\ldots,y_\ell)
:=
\sum_{j=1}^{\ell}
\int_\ell
y_1\cup\cdots\cup
\underline\delta y_j
\cup\cdots\cup y_\ell.
$$

要证明的继承命题是：对任意 $y_1,\ldots,y_\ell\in\underline C$，

$$
\mathcal L(y_1,\ldots,y_\ell)=0.
$$

#### Pure tensors 的 fixed-factor 分组

为了简单，先取 $y_{j}$ 为 homogeneous pure tensors

$$
y_j=\bigotimes_{s=1}^{\ell}y_j^{(s)},
\qquad
y_j^{(s)}\in C_{(s)}^{p_j^{(s)}},
\qquad
p_j^{(s)}\in\{0,1\}.
$$

局部 factors 可以排成

$$
\begin{array}{c|cccc}
 & s=1 & s=2 & \cdots & s=\ell\\
\hline
j=1 & y_1^{(1)} & y_1^{(2)} & \cdots & y_1^{(\ell)}\\
j=2 & y_2^{(1)} & y_2^{(2)} & \cdots & y_2^{(\ell)}\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
j=\ell & y_\ell^{(1)} & y_\ell^{(2)} & \cdots & y_\ell^{(\ell)}
\end{array}.
$$

固定一行 $j$，沿 $s$ 方向做 tensor product 得到 $y_j$；固定一列 $s$，沿 $j$ 方向做第 $s$ 个 seed 的局部 $\ell$ 重乘积。

把 $\underline\delta=\sum_s\delta_s$ 代入 $\mathcal L$，得到

$$
\mathcal L(y_1,\ldots,y_\ell)
=
\sum_{s=1}^{\ell}
\sum_{j=1}^{\ell}
\int_\ell
y_1\cup\cdots\cup
\delta_s y_j
\cup\cdots\cup y_\ell.
$$

固定一个 seed factor $s$，再固定一个 Leibniz 位置 $j$。在当前 $\mathbb F_2$ 约定下，把 $\delta_s y_j$ 的第 $t$ 个 local factor 记为

$$
z_{j;s}^{(t)}
:=
\begin{cases}
\delta^{(s)}y_j^{(s)},&t=s,\\
y_j^{(t)},&t\ne s.
\end{cases}
$$

于是

$$
\delta_s y_j
=
\bigotimes_{t=1}^{\ell}z_{j;s}^{(t)}.
$$

对 $t\ne s$，第 $t$ 个 local argument list 仍是

$$
\left(y_1^{(t)},\ldots,y_j^{(t)},\ldots,y_\ell^{(t)}\right),
$$

不随 Leibniz 位置 $j$ 改变。记它的局部乘积为

$$
A_t
:=
\mu_t\left(y_1^{(t)},\ldots,y_\ell^{(t)}\right).
$$

只有第 $s$ 个 local argument list 的第 $j$ 项被 coboundary 替换。保留这个 $j$-依赖，记

$$
B_{s,j}
:=
\mu_s\left(
y_1^{(s)},\ldots,y_{j-1}^{(s)},
\delta^{(s)}y_j^{(s)},
y_{j+1}^{(s)},\ldots,y_\ell^{(s)}
\right).
$$

因此对固定的 $s,j$，逐 factor 的 product 定义给出

$$
\begin{aligned}
&y_1\cup\cdots\cup
\delta_s y_j
\cup\cdots\cup y_\ell\\
&=
\bigotimes_{t=1}^{\ell}
\mu_t\left(
y_1^{(t)},\ldots,y_{j-1}^{(t)},
z_{j;s}^{(t)},
y_{j+1}^{(t)},\ldots,y_\ell^{(t)}
\right)\\
&=
A_1\otimes\cdots\otimes A_{s-1}
\otimes B_{s,j}\otimes
A_{s+1}\otimes\cdots\otimes A_\ell.
\end{aligned}
$$

第 $s$ 个 seed factor 中对所有 Leibniz 位置求和为

$$
B_s:=\sum_{j=1}^{\ell}B_{s,j}.
$$

由于其余 tensor factors 与 $j$ 无关，tensor product 对第 $s$ 个位置的线性性给出

$$
\begin{aligned}
&\sum_{j=1}^{\ell}
y_1\cup\cdots\cup
\delta_s y_j
\cup\cdots\cup y_\ell\\
&=
\sum_{j=1}^{\ell}
A_1\otimes\cdots\otimes A_{s-1}
\otimes B_{s,j}\otimes
A_{s+1}\otimes\cdots\otimes A_\ell\\
&=
A_1\otimes\cdots\otimes A_{s-1}
\otimes\left(\sum_{j=1}^{\ell}B_{s,j}\right)\otimes
A_{s+1}\otimes\cdots\otimes A_\ell\\
&=
A_1\otimes\cdots\otimes A_{s-1}
\otimes B_s\otimes
A_{s+1}\otimes\cdots\otimes A_\ell.
\end{aligned}
$$

由 product integral 的逐 factor 公式，

$$
\begin{aligned}
&\sum_{j=1}^{\ell}
\int_\ell
y_1\cup\cdots\cup
\delta_s y_j
\cup\cdots\cup y_\ell\\
&\qquad=
\left(\int_1^{(s)}B_s\right)
\prod_{t\ne s}
\left(\int_1^{(t)}A_t\right).
\end{aligned}
$$

Seed integrated Leibniz 的假设直接给出

$$
\int_1^{(s)}B_s=0.
$$

因此固定-$s$ 的整个 $j$-sum 经过积分后为零；这里消失的是对所有 Leibniz 位置求和得到的整体，不要求每个单独的 $j$-summand 分别为零。

对所有 $s$ 求和即得

$$
\mathcal L(y_1,\ldots,y_\ell)=0.
$$

这一分组对应 Breuckmann 等人 Lemma 5.1 Eqs. (20)–(23)：这里的 $s$ 对应论文中固定的 constituent-complex 指标 $k$，$j$ 标记 Leibniz position。

#### 多线性延拓

Homogeneous pure tensors 张成 $\underline C$ 的每个 total-degree 分量，而 $\mathcal L$ 对每个 argument 都是线性的。把一般 homogeneous $y_j$ 写成 pure tensors 的有限线性组合并逐项展开，每个 pure-tensor 组合都由上一段给出零，因此

$$
\mathcal L(y_1,\ldots,y_\ell)=0
$$

对任意 homogeneous cochains 成立。非 homogeneous cochain 先按 total degree 分解，结论仍由直和线性性成立。符号 $y_j^{(s)}$ 专用于选定的 pure-tensor summand；一般 cochain 由有限线性展开处理。

因此 tensor-product complex 继承 integrated Leibniz。

#### Product integral 与 top-degree coboundaries

Product integral 还满足 top-degree coboundary invariance。若 $b=\bigotimes_t b^{(t)}\in\underline C^{\ell-1}$ 是 homogeneous pure tensor，则恰有一个 factor（记为第 $s$ 个）在 degree $0$，其余 factors 都在 degree $1$。Two-term seed 上 $C_{(t)}^1$ 的 coboundary 为零，因此

$$
\int_\ell\underline\delta b
=
\left(\int_1^{(s)}\delta^{(s)}b^{(s)}\right)
\prod_{t\ne s}\int_1^{(t)}b^{(t)}
=0.
$$

Homogeneous pure tensors 张成 $\underline C^{\ell-1}$，所以 $\int_\ell$ 在 $\operatorname{im}(\underline\delta:\underline C^{\ell-1}\to\underline C^\ell)$ 上为零。由于 $\underline C^\ell$ 已是最高层，它因而诱导逻辑读数

$$
H^\ell(\underline C)\longrightarrow\mathbb F_2.
$$

这是 Breuckmann 等人 Eq. (9) 对 $\ell$ 个一维 integrals 的特例。

---
### Ordinary tensor product 上的 representative invariance

前文已经证明 ordinary tensor-product complex $\underline C$ 继承 integrated Leibniz 和 top-degree integral。这里说明这两个结论怎样保证积分后的多重乘积只依赖 cohomology classes。后续 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]] 会先用 averaging 与 relative translates 构造 balanced quotient 上的 inherited product，再调用同一个消去论证。

#### 数值相位函数

对 $z_1,\ldots,z_\ell\in\underline C^1$ 定义

$$
F_{\underline C}(z_1,\ldots,z_\ell)
=
\int_\ell z_1\cup\cdots\cup z_\ell.
$$

$F_{\underline C}$ 是作用在 $\ell$ 个相同 $\underline C$-code blocks 之间的多线性相位函数，而不是单个 code block 上的一元函数。若 $\mathcal H_{\underline C}$ 表示一个 code block 的 physical Hilbert space，则相应的 diagonal gate 作用在 $\mathcal H_{\underline C}^{\otimes\ell}$ 上，并采用记号

$$
|z_1,\ldots,z_\ell\rangle
:=
|z_1\rangle_{(1)}\otimes\cdots\otimes|z_\ell\rangle_{(\ell)},
$$

其中 $z_j\in\underline C^1$ 是第 $j$ 个 code block 的 computational-basis label。这些 code blocks 不要与构成 $\underline C=\bigotimes_s C_{(s)}$ 的 seed tensor factors 混淆。于是 $F_{\underline C}$ 给出

$$
U_{F_{\underline C}}|z_1,\ldots,z_\ell\rangle
=
(-1)^{F_{\underline C}(z_1,\ldots,z_\ell)}
|z_1,\ldots,z_\ell\rangle.
$$

在 physical-qubit basis vectors $e_{q_1},\ldots,e_{q_\ell}$ 上，$z_{j}=\sum_{q=1}^nz_{j,q}e_{q}$，若

$$
F_{\underline C}(e_{q_1},\ldots,e_{q_\ell})=1
$$

表示选择相应的 multi-controlled-$Z$ factor；$\ell=3$ 时就是一个 physical $CCZ$ hyperedge。

取 cocycles

$$
z_j\in Z^1(\underline C)=\ker\underline\delta,
$$

并把第 $m$ 个 representative 改为

$$
z_m+\underline\delta a_m,
\qquad
a_m\in\underline C^0.
$$

由多线性，相位指数的变化为

$$
\begin{aligned}
\Delta_mF_{\underline C}
&:=
F_{\underline C}(z_1,\ldots,z_m+\underline\delta a_m,\ldots,z_\ell)
-
F_{\underline C}(z_1,\ldots,z_m,\ldots,z_\ell)\\
&=
\int_\ell
z_1\cup\cdots\cup\underline\delta a_m\cup\cdots\cup z_\ell.
\end{aligned}
$$

记

$$
w_j=
\begin{cases}
a_m,&j=m,\\
z_j,&j\ne m.
\end{cases}
$$

对 $(w_1,\ldots,w_\ell)$ 使用 $\underline C$ 上已经继承的 integrated Leibniz，得到

$$
0=
\sum_{j=1}^{\ell}
\int_\ell
w_1\cup\cdots\cup
\underline\delta w_j
\cup\cdots\cup w_\ell.
$$

$j=m$ 的一项正是

$$
\int_\ell
z_1\cup\cdots\cup
\underline\delta a_m
\cup\cdots\cup z_\ell.
$$

当 $j\ne m$ 时，$w_j=z_j$，而 cocycle 条件给出 $\underline\delta z_j=0$，所以其余项全部消失。因此

$$
F_{\underline C}
(z_1,\ldots,z_m+\underline\delta a_m,\ldots,z_\ell)
=
F_{\underline C}(z_1,\ldots,z_m,\ldots,z_\ell).
$$

于是 $F_{\underline C}$ 诱导

$$
\overline F_{\underline C}:
H^1(\underline C)^{\times\ell}
\longrightarrow
\mathbb F_2.
$$

这个证明只使用多线性、cocycle 条件和 product complex 上的 integrated Leibniz。它保证数值函数不依赖 cohomology representative；若要证明 logical action 非平凡，还需另外检验 $\overline F_{\underline C}\not\equiv0$。

Integrated Leibniz 是上述 representative invariance 的充分条件。若某个 preorientation 不满足 integrated Leibniz，这个论证不能推出 invariance；是否存在其它抵消方式需要另行验证。

---
### 来源

- Nikolas P. Breuckmann, Margarita Davydova, Jens N. Eberhardt, Nathanan Tantivasadakarn, [*Cups and Gates I: Cohomology Invariants and Logical Quantum Operations*](<../../Papers/S002_2026_Breuckmann_cups_and_gates_I.pdf>), *Communications in Mathematical Physics* 407:86, 2026, Sections 3.2、3.4、5.1–5.2；Eqs. (5)、(9)、Lemma 5.1 Eqs. (19)–(26)。本文展开 Lemma 5.1 的 ordinary tensor-product fixed-factor 证明。
- Varun Menon, J. Pablo Bonilla Ataides, Rohan Mehta, Andi Gu, Daniel Bochen Tan, Mikhail D. Lukin, [*Magic Tricycles: Efficient Magic State Generation with Finite Block-Length Quantum LDPC Codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), arXiv:2508.10714v2, 2025, Appendix D；Definitions 5–6、Proposition 4。
- [[Cup product 与 Leibniz rule]]：普通 cochain-level Leibniz、cohomology cup product 与一般 representative invariance。
- [[Cochain complex 的 tensor product]]：total degree、ordinary tensor-product coboundary 与 Koszul sign 约定。
- [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]：free-basis averaging、relative-translate operation、invariant integral 与 balanced integrated-Leibniz 继承。
- [[Symmetric triple cup-product]]：Menon 的 symmetric bracketing、preorientation constraints 与 physical $CCZ$ 判据。
