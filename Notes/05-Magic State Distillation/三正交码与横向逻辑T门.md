# 一般稳定子码中横向 (T) 的完整逻辑矩阵判据

设$\mathcal{C}$是一个$[[n,k]]$稳定子码，编码空间投影为
$$
P_{\mathcal C}.
$$
横向物理T门为
$$
U_{\mathrm{phys}}=T^{\otimes n}.
$$
我们希望判断$T^{\otimes n}$是否在编码空间上实现某个目标逻辑门，例如单逻辑比特上的$T_{L}$，或者多个逻辑比特上的$T_{L,j}$。

---

## 1. 真正需要判断的两件事:保持编码空间和实现目标门

第一，横向门必须保持编码空间：
$$
U_{\mathrm{phys}}P_{\mathcal C}U_{\mathrm{phys}}^\dagger=P_{\mathcal C}.
$$
等价地说，
$$
U_{\mathrm{phys}}\mathcal C=\mathcal C.
$$
如果这一步不成立，那么$T^{\otimes n}$会把编码态带出编码空间，不能称为逻辑门。

第二，如果它保持编码空间，则它在编码空间上诱导一个逻辑门。选定逻辑计算基
$$
{|\overline{x}\rangle:x\in\mathbb F_2^k}.
$$
定义逻辑矩阵元
#### $$
K_{yx}=\langle \overline y|
T^{\otimes n}
|\overline x\rangle.
$$
如果$T^{\otimes n}$保持编码空间，那么矩阵
$$
K=(K_{yx})
$$
就是它诱导的逻辑门。

$K$是直接横向逻辑T门的条件是
$$
K=e^{i\theta}T_{\mathrm{target}}.
$$
如果允许之后加一个逻辑 Clifford 修正$C_{L}$，则要求存在某个逻辑 Clifford$C_{L}$，使得
$$
C_LK=e^{i\theta}T_{\mathrm{target}}.
$$
等价地，
##### $$
KT_{\mathrm{target}}^\dagger

=e^{i\theta}C_L^\dagger.
$$
因此实现目标门的判据是
$$
KT_{\mathrm{target}}^\dagger
\in \mathrm{Clifford}_L
\quad
\text{up to global phase}.
$$
---

## 2. 一般稳定子逻辑基态的仿射支撑表示

由[[逻辑基态的表示]],对每个逻辑基态，可以写成
 $$
|\overline{x}\rangle=
\frac{1}{\sqrt{|A|}}
\sum_{a\in A}
q_x(a)
|t_x\oplus a\rangle.
$$
这里：
- $A\subset \mathbb{F}_{2}^{n}$是线性子空间；
- $\ket{t_{x}+A}$ 是$\ket{x}$的计算基支撑；
- $q_{x}(a)\in\{1,-1,i,-i\}$是稳定子态相位；
- $t_{x}$是逻辑基态$x$对应的陪集代表。
记
$$
W_x=t_x+A.
$$
因为所有$W_{x}$都是同一个线性空间$A$的陪集，所以对任意$(x,y)$，有且只有两种可能：
$$
W_x\cap W_y=\varnothing,
$$
或者
$$
W_x=W_y.
$$
具体地，
$$
W_x=W_y
\iff
t_x\oplus t_y\in A,
$$
而
$$
W_x\cap W_y=\varnothing
\iff
t_x\oplus t_y\notin A.
$$
这就是陪集的基本性质：同一个线性子空间的两个陪集要么完全相同，要么完全不相交。

---

## 3. 逻辑矩阵元
横向物理$T$门在普通计算基上对角：
$$
T^{\otimes n}|z\rangle
=
\omega^{|z|}|z\rangle,
\qquad
\omega=e^{i\pi/4}.
$$
因此
$$
K_{yx}
=
\langle \overline y|
T^{\otimes n}
|\overline x\rangle.
$$
代入仿射支撑展开：
#### $$
K_{yx}
=
\frac{1}{|A|}
\sum_{z\in W_x\cap W_y}
q_y(z)^*q_x(z)\omega^{|z|}.
$$
由于$W_{x}\cap W_{y}$只有空集或同一个陪集两种可能，所以可以写成更简洁的分情况形式：
$$
K_{yx}
=
\begin{cases}
0,
&
W_x\cap W_y=\varnothing \\
\dfrac{1}{|A|}
\displaystyle\sum_{z\in W_x}
q_y(z)^*q_x(z)\omega^{|z|},
&
W_x=W_y.
\end{cases}
$$
如果用$z=t_{x}\oplus a$参数化同一个陪集，则当$W_{x}=W_{y}$时，
$$
K_{yx}
=
\frac{1}{|A|}
\sum_{a\in A}
q_y(t_x\oplus a)^*
q_x(t_x\oplus a)
\omega^{|t_x\oplus a|}.
$$
这就是一般稳定子码中横向T门的完整逻辑矩阵元。

---
## 4. 陪集性质带来的块结构

因为不同逻辑基态的支撑陪集要么相同、要么不交，所以$K$有一种自然的块结构。
若
$$
W_x\cap W_y=\varnothing,
$$
则
$$
K_{yx}=0.
$$
这表示物理对角门$T^{\otimes n}$不会把一个陪集中的计算基态移动到另一个不相交的陪集。
但如果
$$
W_x=W_y,
$$
则非对角矩阵元
$$
K_{yx}
$$
不一定为零。因为两个不同逻辑基态可以支撑在同一个陪集上，只是相位函数$q_{x}$和$q_{y}$不同。

因此，一般稳定子码中横向$T$可以在同一个支撑陪集对应的逻辑子空间内部产生混合。

---

## 5. 用逻辑矩阵元重写编码空间保持条件
令

$$
K=(K_{yx})
$$
为上面计算出的$2^{k}\times 2^{k}$逻辑矩阵。
由于$T^{\otimes n}$是物理空间中的单位门，编码空间是否保持可以由
$$
K^\dagger K
$$
判断。
精确条件是
$$
T^{\otimes n}\text{ 保持编码空间}
\iff
K^\dagger K=I_{2^k}.
$$
直观上，$K$是把$T^{\otimes n}\ket{\overline{x}}$投影回编码空间之后得到的矩阵。如果横向$T$门把态的一部分带出编码空间，那么投影回来的范数会变小，从而
$$
K^\dagger K\neq I.
$$
如果
$$
K^\dagger K=I,
$$
则没有泄漏，$K$就是实际诱导的逻辑门。

---
## 6. 直接横向逻辑$T$门的判据
以单逻辑比特为例，目标逻辑门为
$$
T_L=
\begin{pmatrix}
1&0 \\
0&\omega
\end{pmatrix}.
$$
直接横向逻辑$T$门的条件是存在整体相位$e^{ i\theta }$，使得 $$
K
=
e^{i\theta}
\begin{pmatrix}
1&0 \\
0&\omega
\end{pmatrix}.
$$
也就是
$$
K_{00}=e^{i\theta},
$$
$$
K_{11}=e^{i\theta}\omega,
$$
并且
$$
K_{01}=K_{10}=0.
$$
用支撑求和写，就是
$$
K_{00}=\frac1{|A|}
\sum_{z\in W_0}
\omega^{|z|},
K_{11}=\frac1{|A|}
\sum_{z\in W_1}
\omega^{|z|}.
$$
这里对角项中使用了
$$
q_x(z)^*q_x(z)=1.
$$
非对角项则为:
$$
	K_{10}=\begin{cases}
		0 & W_{0}\cap W_{1}=\varnothing  \\
		\frac{1}{|A|}\sum \limits_{z\in W_{0}} q_{1}(z)^{*}q_{0}(z)\omega^{|z|} & W_{0}=W_{1}
	\end{cases}
$$
如果$W_{0}\cap W_{1}$，则非对角项自动为零。
如果$W_{0}=W_{1}$，则需要相位求和相消，使得非对角项为零。

---
## 7. 多逻辑比特情形
如果目标是在第$j$个逻辑比特上作用逻辑$T$门，则
$$
T_{L,j}|\overline{x}\rangle
=
\omega^{x_j}|\overline{x}\rangle.
$$
因此直接横向逻辑$T_{L,j}$的条件是
#### $$
K_{yx}
=
e^{i\theta}
\omega^{x_j}
\delta_{yx}.
$$
如果目标是在所有逻辑比特上同时作用$T$门，则
$$
T_{L,1}\cdots T_{L,k}|\overline{x}\rangle
=
\omega^{\sum_j x_j}|\overline{x}\rangle.
$$
对应条件为
#### $$
K_{yx}
=
e^{i\theta}
\omega^{\sum_j x_j}
\delta_{yx}.
$$
如果允许 Clifford 修正，则要求
$$
KT_{\mathrm{target}}^\dagger
\in
\mathrm{Clifford}_L
\quad
\text{up to global phase}.
$$

---
## 8. CSS/triorthogonal 情形条件简化
在 CSS 码中，逻辑基态可以写成无相位陪集态：
$$
|\overline{x}\rangle
=
\frac1{\sqrt{|C_X|}}
\sum_{c\in C_X}
|c\oplus t(x)\rangle.
$$
也就是
$$
A=C_X,
\qquad
q_x(c)=1.
$$
在$t(x)$等于逻辑基线性展开下，不同$x$对应不同陪集：
$$
C_X+t(x).
$$
因此若$x\neq y$，通常有
$$
W_x\cap W_y=\varnothing.
$$
于是
$$
K_{yx}=0,
\qquad
x\neq y.
$$
非对角项自动消失。
所以只需要看对角项：
$$
K_{xx}
=
\frac1{|C_X|}
\sum_{c\in C_X}
\omega^{|c\oplus t(x)|}.
$$
这一项是很多单位复数的平均，模长必须为1才能保证态不会泄漏到非编码态。
每一项
$$
	\omega^{|c\oplus t(x)|}
$$
都在单位圆上。单位复数的平均值模长等于1当且仅当所有单位复数相同,即：
#### $$
|c\oplus t(x)|
\equiv
F(x)
\pmod8
$$
**对所有$c\in C_{X}$成立**，那么
$$
K\ket{\overline{x} } \to \ket{\overline{x} } ,K_{xx}
=
\omega^{F(x)}.
$$
这时横向$T$门在逻辑基上实现对角逻辑门。
进一步，如果
$$
F(x)=x_j
\pmod8,
$$
则得到第$j$个逻辑比特上的$T$门。
如果
$$
F(x)=\sum_j x_j
\pmod8,
$$
则得到所有逻辑比特上的横向逻辑$T$门。
三正交条件正是在这种 CSS 陪集情形下，用行重量、二重重叠、三重重叠来控制
$$
|c\oplus t(x)|\pmod8
$$
---
## 9.从横向$T$推导三正交条件
### 9.1 先从 CSS 陪集态的一般行表示开始
取$C_{X}$的一组基
$$
g_1,\ldots,g_r,
$$
所以
$$
c(y)=\bigoplus_{\alpha=1}^r y_\alpha g_\alpha.
$$
再取补空间的一组基：
$$
f_1,\ldots,f_k,
$$
使得
$$
t(x)=\bigoplus_{i=1}^k x_i f_i.
$$
于是普通计算基标签为
$$
v(y,x)

\bigoplus_{\alpha=1}^r y_\alpha g_\alpha
\oplus
\bigoplus_{i=1}^k x_i f_i.
$$
---

### 9.2 横向$T$门只看汉明重量模8

横向$T$作用为
$$
T^{\otimes n}|z\rangle
=
\omega^{|z|}|z\rangle,
\qquad
\omega=e^{i\pi/4}.
$$
所以关键对象是
$$
|v(y,x)|\pmod8.
$$
把所有行统一记成
$$
h_a\in{g_1,\ldots,g_r,f_1,\ldots,f_k},
$$
对应变量统一记成
$$
u_a\in{y_1,\ldots,y_r,x_1,\ldots,x_k}.
$$
于是
$$
v(u)=\bigoplus_a u_a h_a.
$$
[[汉明重量展开]]给出
$$
\begin{aligned}
|v(u)|
\equiv{}&
\sum_a u_a |h_a|
\\
&-2\sum_{a<b}u_a u_b |h_a\wedge h_b|
\\
&+4\sum_{a<b<c}
u_a u_b u_c
|h_a\wedge h_b\wedge h_c|
\pmod8.
\end{aligned}
$$
这个公式是三正交的来源。

---
### 9.3 先看一次项：偶/奇重量划分
一次项是
$$
\sum_a u_a |h_a|.
$$
对某一行$h_{a}$，横向$T$产生的线性相位是
$$
\omega^{u_a|h_a|}.
$$
现在分两类变量讨论。
#### 9.3.1 如果$u_{a}=y_{\alpha}$，即它是稳定子求和变量
$y_{\alpha}$是陪集内部的求和变量，不是逻辑变量。
如果对应行$g_{\alpha}$是奇重量，即
$$
|g_\alpha|=1\pmod2,
$$
那么相位里会出现
$$
\omega^{y_\alpha}
$$
这种 $T$-型非 Clifford 相位，并且它依赖的是稳定子变量$y_{\alpha}$。
这不是我们想要的。横向$T$门的非 Clifford 部分应该来自逻辑自由度$t(x)$上，而不是来自陪集内部的求和变量$c$上。
所以为了避免非 Clifford 相位落在稳定子方向上，必须要求
$$
|g_\alpha|=0\pmod2.
$$
也就是说：
$$
X\text{稳定子的行必须是偶重量。}
$$
---

#### 9.3.2 如果$u_{a}=x_{i}$，即它是逻辑变量
如果对应行$f_{i}$是奇重量，即
$$
|f_i|=1\pmod2,
$$
那么线性相位中有
$$
\omega^{x_i|f_i|}.
$$
由于$|f_{i}|$是奇数，
$$
\omega^{|f_i|x_i}
$$
就是逻辑$T$-型相位，至多差一个逻辑 Clifford 相位。
例如：
$$
|f_i|\equiv1\pmod8  \text{给出}T_i.
$$
$$
|f_i|\equiv3\pmod8给出S_iT_i.
$$
$$
|f_i|\equiv5\pmod8给出Z_iT_i.
$$
$$
|f_i|\equiv7\pmod8给出T_i^\dagger.
$$
而$T_{i}^{^{\dagger}}$也可以通过 Clifford $S_{i}$转成$T_{i}$，因为
$$
S_iT_i^\dagger=T_i.
$$
所以，若允许 Clifford 修正，奇重量逻辑行正好承载逻辑$T$门的非 Clifford 部分。
于是得到：
$$
\text{承载逻辑 }T\text{ 的逻辑算符应该是奇重量行。}
$$
---
### 9.4 再看二次项：要求两行重叠为偶数
二次项是
$$
-2\sum_{a<b}u_a u_b |h_a\wedge h_b|.
$$
考虑两行$(h_{a},h_{b})$。
如果它们的重叠是奇数：
$$
|h_a\wedge h_b|=1\pmod2,
$$
那么对应相位含有
$$
\omega^{-2u_a u_b}.
$$
当$u_a=u_b=1$时，
$$
\omega^{-2}=e^{-i\pi/2}=-i.
$$
这相当于一个 controlled-$S^{^{\dagger}}$型二体相位。
controlled-$S$是非 Clifford 门。所以如果两行重叠为奇数，横向$T$会产生额外的二体非 Clifford 相位。这不是单纯的逻辑$T$加 Clifford 修正。
因此必须要求任意两行满足
$$
|h_a\wedge h_b|=0\pmod2.
$$
如果两行重叠为偶数，写作
$$
|h_a\wedge h_b|=2m,
$$
那么二次项系数为
$$
-2\cdot 2m=-4m.
$$
模8下只有两种可能：
$$
0
\quad\text{或}\quad
4.
$$
对应相位是
$$
1
\quad\text{或}\quad
-1.
$$
这只是 $CZ$-型 Clifford 相位。
所以两行重叠偶数的意义是：
$$
\text{避免 controlled-}S\text{ 型非 Clifford 二体相位，只允许 }CZ\text{ 型 Clifford 二体相位。}
$$
---
### 9.5 再看三次项：为什么要求三行重叠为偶数
三次项是
$$
4\sum_{a<b<c}
u_a u_b u_c
|h_a\wedge h_b\wedge h_c|.
$$
如果三行重叠是奇数：
$$
|h_a\wedge h_b\wedge h_c|=1\pmod2,
$$
那么会出现相位
$$
\omega^{4u_a u_b u_c}
=
(-1)^{u_a u_b u_c}.
$$
这就是$CCZ$-型三体相位。
$CCZ$是非 Clifford 门。如果我们的目标是“横向T门的非 Clifford 部分只是逻辑$T$门”，那么不应额外产生$CCZ$型三体非 Clifford 相位。
所以要求任意三行满足
$$
|h_a\wedge h_b\wedge h_c|=0\pmod2.
$$
如果三重重叠为偶数，那么
$$
4|h_a\wedge h_b\wedge h_c|
\equiv0\pmod8,
$$
三次项消失。

---
### 9.6 三正交条件

我们从任意行$h_{a}$出发。
推导结果是：
第一，稳定子方向不能承载非 Clifford 线性相位，所以稳定子方向行$g_{\alpha}$必须满足
$$
|g_\alpha|=0\pmod2.
$$
第二，承载逻辑$T$的逻辑算符需要奇重量，所以逻辑算符行$f_{i}$应满足
$$
|f_i|=1\pmod2.
$$
第三，为了不产生 controlled-$S$型额外非 Clifford 二体相位，要求任意两行$h_{a},h_{b}$满足
$$
|h_a\wedge h_b|=0\pmod2.
$$
第四，为了不产生$CCZ$型额外非 Clifford 三体相位，要求任意三行$h_{a},h_{b},h_{c}$满足
$$
|h_a\wedge h_b\wedge h_c|=0\pmod2.
$$
这就是三正交条件。
自然表述是：
$$
\text{三正交条件来自要求横向 }T
\text{ 的非 Clifford 相位只出现在逻辑一次项中。}
$$
---
## 9.7 生成矩阵
$g_{\alpha}$和$f_{i}$组成了所有的逻辑基态的基，实际上张成了$C_{Z}^{\perp}$，也就是$C_{Z}^{\perp}$的生成矩阵。
