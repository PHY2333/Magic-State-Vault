Cochain complex 的 tensor product 接在 [[Tensor product 对 direct sum 的分配律]] 之后：那篇只说明普通 tensor product 如何把 direct sum 分成双指标网格；本文解释当这些分层空间来自 cochain complexes 时，怎样给张量分配 total degree、怎样定义新的 coboundary map，以及为什么二项 complex 相乘会变成三项或四项 complex。

Balanced product 不在本文定义。右模、左模、anti-diagonal coinvariants 以及 over $R=\mathbb F_2[G]$ 的 tensor product 见 [[Balanced tensor product 与 coinvariant quotient]]。读那篇时，公式

$$
(C\otimes D)^n
=
\bigoplus_{i+j=n}C^i\otimes D^j
$$

应该先理解为 tensor-product complex 的定义，而不是某个需要从物理图像推出的等式。

本文只补 tensor product of cochain complexes 的最小线性代数。chain/cochain、cocycle/coboundary 和 quotient 的基本术语见 [[Chain complex 与 cochain complex]]；CSS 码中的 logical class 翻译见 [[CSS码中的cochain complex]]。

---
### 从 graded vector space 到 total degree

设 $C,D$ 是两个 cochain complexes：

$$
\cdots\to C^i\xrightarrow{\delta_C^i}C^{i+1}\to\cdots,
\qquad
\cdots\to D^j\xrightarrow{\delta_D^j}D^{j+1}\to\cdots.
$$

构造 tensor-product complex 有两个步骤：先决定新 complex 的每一层空间是什么，再决定新的 coboundary map 如何作用。第一步只需要 $C,D$ 的分层空间结构，不需要先用到 $\delta_C,\delta_D$。

可以先用一个三角形作图像。三角形同时包含顶点、边和面，但这三类对象不能混在同一个“层”里：

$$
\begin{array}{c|c|c}
\text{degree} & \text{几何对象} & \text{向量空间}\\
\hline
0 & \text{顶点} & V^0=\operatorname{span}\{[a],[b],[c]\}\\
1 & \text{边} & V^1=\operatorname{span}\{[ab],[bc],[ca]\}\\
2 & \text{面} & V^2=\operatorname{span}\{[abc]\}
\end{array}
$$

如果只把这三层空间放在一起，还没有说“面的边界是哪几条边”或“边的边界是哪几个点”，那得到的只是一个按 degree 分层的向量空间：

$$
V=V^0\oplus V^1\oplus V^2.
$$

这就是 graded vector space。它的作用是先保存“哪些对象属于第几层”。后面再加上 degree $+1$ 或 degree $-1$ 的映射，才得到 cochain/chain complex。

一般的 graded vector space 写成

$$
V=\bigoplus_{i\in I}V^i,
$$

其中 $I$ 是允许出现的 degree 集合，常见选择是一个有限集合 $\{0,\ldots,m\}$，或在无限 complex 中取 $I=\mathbb Z$。这里 $V^i$ 是 degree 为 $i$ 的整层子空间；$i$ 只是在标记“第几层”，不表示 $\dim V^i=i$，也不表示 $V^i$ 里只有第 $i$ 个基向量。比如 $V^1$ 可以是一维、十维，也可以是零空间。

一个 cochain complex 可以看成“graded vector space 加上 degree $+1$ 的线性映射 $\delta^i:V^i\to V^{i+1}$，并满足 $\delta^{i+1}\delta^i=0$”。因此下面先用直和结构说明新空间的分层，下一节再把 $\delta_C,\delta_D$ 合成新的 coboundary map。

$$
C=\bigoplus_{i\in I_C} C^i,
\qquad
D=\bigoplus_{j\in I_D} D^j.
$$

按照 [[Tensor product 对 direct sum 的分配律]]，普通 tensor product 会把两个 direct sum 分解为双指标网格：

$$
C\otimes D
\cong
\bigoplus_{i\in I_C,\ j\in I_D}C^i\otimes D^j.
$$

右边每一块 $C^i\otimes D^j$ 的元素可以理解为“一个 degree-$i$ 的 $C$ 对象”和“一个 degree-$j$ 的 $D$ 对象”组成的形式张量。图像上，可以把这些块排成二维网格：

$$
\begin{array}{c|cc}
 & D^0 & D^1\\
\hline
C^0 & C^0\otimes D^0 & C^0\otimes D^1\\
C^1 & C^1\otimes D^0 & C^1\otimes D^1
\end{array}
$$

为了让 $C\otimes D$ 本身也成为一个一维链条状的 cochain complex，需要把这个二维网格重新压回按 degree 排列的层。标准约定是取 total degree：

$$
\deg(c_i\otimes d_j)=i+j
\qquad(c_i\in C^i,\ d_j\in D^j).
$$

这个加法是 graded tensor product 的定义，不是从普通 direct sum 分解中自动推出的。它给出 tensor-product complex 的分层：

$$
(C\otimes D)^n
=
\bigoplus_{i+j=n}C^i\otimes D^j.
$$

这里左边 $(C\otimes D)^n$ 是新 tensor-product complex 的 degree-$n$ cochain space；右边是它的具体构造。这个等号本质上是定义，也可以看成 [[Tensor product 对 direct sum 的分配律]] 中自然分解的 total degree-$n$ 部分。

这个公式里同时出现两种操作。内层的

$$
C^i\otimes D^j
$$

是 tensor product：它把 $C^i$ 的方向和 $D^j$ 的方向两两配对，形成新的张量方向。外层的

$$
\bigoplus_{i+j=n}
$$

是 direct sum：它把 total degree 同为 $n$ 的不同来源并列保存。

比如在两个三角形 cochain complexes 的 tensor product 中，第一份的 degree-$0$ 顶点与第二份的 degree-$1$ 边给出 $C^0\otimes D^1$，第一份的 degree-$1$ 边与第二份的 degree-$0$ 顶点给出 $C^1\otimes D^0$。这两个空间不是同一个 tensor 因子顺序；它们只是因为 total degree 都等于 $1$，被放进同一个 direct sum

$$
(C\otimes D)^1=(C^1\otimes D^0)\oplus(C^0\otimes D^1).
$$

因此 $u\in C^1\otimes D^0$ 和 $v\in C^0\otimes D^1$ 能相加，是因为它们通过标准嵌入进入同一个直和空间。若把上式看作外直和，则

$$
u+v=(u,0)+(0,v)=(u,v).
$$

对上面这个只有两个分量的外部对象，direct sum 和 direct product 没有区别：

$$
(C^1\otimes D^0)\oplus(C^0\otimes D^1)
\cong
(C^1\otimes D^0)\times(C^0\otimes D^1).
$$

标准定义仍写 direct sum，是为了和普通代数 tensor product 的有限支撑性质一致。上游笔记 [[Tensor product 对 direct sum 的分配律#Direct sum、direct product 与 tensor product]] 已经说明：direct sum 是有限线性组合空间，direct product 是所有坐标族空间；tensor product 则处理双线性配对，不是并列保存两个分量。

$$
\left(\bigoplus_i C^i\right)\otimes
\left(\bigoplus_j D^j\right)
\cong
\bigoplus_{i,j}C^i\otimes D^j.
$$

差别只在同一个 degree 里有无限多个分量时出现。若把 degree-$n$ 层改成 direct product，就会允许

$$
(x_i)_{i\in\mathbb Z},
\qquad
x_i\in C^i\otimes D^{n-i},
$$

这种无限多个分量同时非零的元素。它不属于普通代数 tensor product，而是某种完成化后的对象，需要额外的拓扑或收敛约定。本文后面使用的二项或有限项 complex 中，每个 degree 只含有限多个分量，所以 direct sum 和 direct product 自然同构；这里继续写 direct sum，是为了和一般 graded tensor product 的代数定义一致。

这个分层本身还不是 coboundary map。新的 coboundary map 由原来的 $\delta_C,\delta_D$ 定义；采用 total degree 分层后，它会是 degree $+1$ 的线性映射。若 $c_i\in C^i,d_j\in D^j$ 且 $i+j=n$，则

$$
\delta_C c_i\otimes d_j\in C^{i+1}\otimes D^j,
\qquad
c_i\otimes\delta_D d_j\in C^i\otimes D^{j+1},
$$

其中

$$
C^{i+1}\otimes D^j,\quad C^i\otimes D^{j+1}
$$

都是 $(C\otimes D)^{n+1}$ 的 direct-sum 分量。因此后面定义的 $\delta$ 有类型

$$
\delta:(C\otimes D)^n\longrightarrow (C\otimes D)^{n+1}.
$$

---
### 一个二维例子

取两个最小的二项 complex，只看它们的分层空间：

$$
C^0=\operatorname{span}\{c_0\},
\qquad
C^1=\operatorname{span}\{c_1\},
$$

$$
D^0=\operatorname{span}\{d_0\},
\qquad
D^1=\operatorname{span}\{d_1\}.
$$

普通 tensor product 的基向量有四类：

$$
c_0\otimes d_0,\quad
c_1\otimes d_0,\quad
c_0\otimes d_1,\quad
c_1\otimes d_1.
$$

现在按 total degree 分层。因为 $c_0,d_0$ 都来自 degree $0$，

$$
c_0\otimes d_0
\in
(C\otimes D)^0.
$$

因为 $c_1\in C^1,d_0\in D^0$，而 $c_0\in C^0,d_1\in D^1$，所以

$$
c_1\otimes d_0,\quad c_0\otimes d_1
\in
(C\otimes D)^1.
$$

最后

$$
c_1\otimes d_1
\in
(C\otimes D)^2.
$$

因此这个例子里的 tensor-product complex 在对象层面就是

$$
\operatorname{span}\{c_0\otimes d_0\}
\to
\operatorname{span}\{c_1\otimes d_0,\ c_0\otimes d_1\}
\to
\operatorname{span}\{c_1\otimes d_1\}.
$$

这就是公式

$$
(C\otimes D)^n
=
\bigoplus_{i+j=n}C^i\otimes D^j
$$

在最小例子里的具体含义。中间那一层有两个 basis directions，不是因为出现了两个不同的物理系统，而是因为 total degree $1$ 可以由 $(1,0)$ 和 $(0,1)$ 两种来源组成。

---
### Coboundary map 如何作用

写原 complex 的 coboundary maps 为

$$
\delta_C^i:C^i\to C^{i+1},
\qquad
\delta_D^j:D^j\to D^{j+1}.
$$

条件 $\delta_C^2=0$ 的意思是相邻两层的复合为零：

$$
\delta_C^{i+1}\circ\delta_C^i=0
\qquad\text{for all }i,
$$

同理

$$
\delta_D^{j+1}\circ\delta_D^j=0
\qquad\text{for all }j.
$$

Tensor-product complex 的 coboundary map 在简单张量上定义为

$$
\delta(c_i\otimes d_j)
=
\delta_C^i c_i\otimes d_j
+
(-1)^i c_i\otimes\delta_D^j d_j,
\qquad c_i\in C^i,\ d_j\in D^j.
$$

第一项属于 $C^{i+1}\otimes D^j$，第二项属于 $C^i\otimes D^{j+1}$，所以两项都会把 total degree 从 $i+j$ 提到 $i+j+1$。

符号 $(-1)^i$ 的作用是保证新的 coboundary map 仍满足 $\delta^2=0$。对 $c_i\otimes d_j$ 展开：

$$
\begin{aligned}
\delta^2(c_i\otimes d_j)
&=
\delta(\delta_C^i c_i\otimes d_j)
+
(-1)^i\delta(c_i\otimes \delta_D^j d_j)
\\
&=
\delta_C^{i+1}\delta_C^i c_i\otimes d_j
+
(-1)^{i+1}\delta_C^i c_i\otimes\delta_D^j d_j
\\
&\quad
+
(-1)^i\delta_C^i c_i\otimes\delta_D^j d_j
+
(-1)^{2i}c_i\otimes\delta_D^{j+1}\delta_D^j d_j.
\end{aligned}
$$

第一项和最后一项分别由

$$
\delta_C^{i+1}\circ\delta_C^i=0,
\qquad
\delta_D^{j+1}\circ\delta_D^j=0
$$

消失。中间两项的系数为

$$
(-1)^{i+1}+(-1)^i=0,
$$

所以交叉项抵消，得到

$$
\delta^2(c_i\otimes d_j)=0.
$$

如果省略 $(-1)^i$，中间两项会变成

$$
\delta_C^i c_i\otimes\delta_D^j d_j
+
\delta_C^i c_i\otimes\delta_D^j d_j
=
2\,\delta_C^i c_i\otimes\delta_D^j d_j,
$$

在特征不是 $2$ 的系数环或系数域上，这通常不是零。

这个公式是 graded Leibniz rule，也称 Koszul sign rule：

$$
\delta(x\otimes y)
=
\delta x\otimes y
+
(-1)^{|x|}x\otimes\delta y.
$$

这里 $|x|$ 表示 $x$ 的 degree。到了本文主要使用的 $\mathbb F_2$ 系数下，$-1=1$，所以常写成

$$
\delta(c_i\otimes d_j)
=
\delta_C^i c_i\otimes d_j
+
c_i\otimes\delta_D^j d_j.
$$

这个简化依赖特征 $2$；在一般系数下，$(-1)^i$ 是 tensor-product complex 成为 complex 的必要符号。

---
### 两个二项 complex 乘成三项 complex

若

$$
C^0\xrightarrow{\delta_C}C^1,
\qquad
D^0\xrightarrow{\delta_D}D^1,
$$

则 tensor-product complex 的 degree 分层为：

$$
(C\otimes D)^0
=
C^0\otimes D^0,
$$

$$
(C\otimes D)^1
=
(C^1\otimes D^0)\oplus(C^0\otimes D^1),
$$

$$
(C\otimes D)^2
=
C^1\otimes D^1.
$$

所以两个二项 complex 会变成三项 complex：

$$
C^0\otimes D^0
\xrightarrow{\Delta^0}
(C^1\otimes D^0)\oplus(C^0\otimes D^1)
\xrightarrow{\Delta^1}
C^1\otimes D^1.
$$

在 $\mathbb F_2$ 上，中间层按

$$
(C^1\otimes D^0)\oplus(C^0\otimes D^1)
$$

这个顺序写成 direct sum。第一张映射为

$$
\Delta^0(x)
=
(\delta_C\otimes I)x+(I\otimes\delta_D)x,
\qquad x\in C^0\otimes D^0,
$$

其中两项分别落在 $C^1\otimes D^0$ 和 $C^0\otimes D^1$ 两个 direct-sum 分量中。第二张映射为

$$
\Delta^1(u+v)
=
(I\otimes\delta_D)u+(\delta_C\otimes I)v.
$$

这里 $u\in C^1\otimes D^0$，$v\in C^0\otimes D^1$。

相对于这个 direct-sum 分解，两张映射可记为 block matrix：

$$
\Delta^0
=
\begin{bmatrix}
\delta_C\otimes I\\
I\otimes\delta_D
\end{bmatrix},
$$

$$
\Delta^1
=
\begin{bmatrix}
I\otimes\delta_D&
\delta_C\otimes I
\end{bmatrix}.
$$

于是

$$
\Delta^1\Delta^0
=
(I\otimes\delta_D)(\delta_C\otimes I)
+
(\delta_C\otimes I)(I\otimes\delta_D)
=0
$$

在 $\mathbb F_2$ 上成立，因为两项是同一条复合路径的两份拷贝。若在一般系数环上，第二张映射的某一项需要带负号，抵消才成立。

---
### 三个二项 complex 乘成四项 complex

三个二项 complex

$$
A^0\to A^1,\qquad
B^0\to B^1,\qquad
E^0\to E^1
$$

的 tensor product 有四层。按 total degree 收集：

$$
0:\quad
A^0\otimes B^0\otimes E^0,
$$

$$
1:\quad
(A^1\otimes B^0\otimes E^0)
\oplus
(A^0\otimes B^1\otimes E^0)
\oplus
(A^0\otimes B^0\otimes E^1),
$$

$$
2:\quad
(A^1\otimes B^1\otimes E^0)
\oplus
(A^1\otimes B^0\otimes E^1)
\oplus
(A^0\otimes B^1\otimes E^1),
$$

$$
3:\quad
A^1\otimes B^1\otimes E^1.
$$

这只解释乘积 complex 的 sector 数量为 $1,3,3,1$：degree $1$ 有三种来源，degree $2$ 也有三种来源。若 seed complexes 带有 group algebra $R$ 的作用，如何进一步通过 balanced product 得到 Menon 的 $R\to R^3\to R^3\to R$，见 [[Tricycle complex 的 balanced-product 构造]]。

---
### 适用范围

- 以上 tensor-product complex 是线性代数/同调代数中的构造，不是量子态 Hilbert space 的 tensor product 物理解释。
- 本库 Menon 笔记主要在 $\mathbb F_2$ 上工作，所以符号项经常省略；若换到一般整数或实复系数，必须保留 Koszul sign。
- 普通 tensor product 只说明乘积 complex 的分层和映射；balanced product 还需要 $R$-module 结构，不能只从 total degree 公式推出。
