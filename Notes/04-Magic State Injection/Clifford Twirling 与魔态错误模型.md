Twirling 的作用不是消除噪声，而是利用随机对称操作，把难以分析的相干项平均掉，得到适合 stabilizer code 和 magic-state distillation 分析的有效随机错误模型。

在 magic-state 文献中，“Clifford twirling”可能指两件不同的事：

- 对量子通道使用完整 Clifford 群平均，得到 depolarizing channel；
- 对 noisy $|T\rangle$ state 只使用稳定 $|T\rangle$ 的 Clifford 子群平均，把态对角化为 $|T\rangle$ 与 $Z|T\rangle$ 的概率混合。

后者才是 15-to-1 distillation 中

$$
\rho_T(p)
=
(1-p)|T\rangle\langle T|
+
pZ|T\rangle\langle T|Z
$$

这一输入错误模型的直接来源。它不等同于 full Clifford twirling。

---
### 1. 通道 twirling 的一般定义

设 $\mathcal E$ 是量子通道，$\mathcal G$ 是有限酉算符集合。对应的 twirled channel 定义为

$$
\mathcal E_{\mathcal G}(\rho)
=
\frac{1}{|\mathcal G|}
\sum_{G\in\mathcal G}
G^\dagger
\mathcal E(G\rho G^\dagger)
G.
$$

每一项表示：

1. 在噪声前施加随机 $G$；
2. 经历原始通道 $\mathcal E$；
3. 在噪声后施加 $G^\dagger$；
4. 对随机选择取平均。

Twirled channel 具有 $\mathcal G$ 对称性。对任意 $H\in\mathcal G$，

$$
\begin{aligned}
H^\dagger
\mathcal E_{\mathcal G}
(H\rho H^\dagger)
H
&=
\frac1{|\mathcal G|}
\sum_{G\in\mathcal G}
H^\dagger G^\dagger
\mathcal E
(GH\rho H^\dagger G^\dagger)
GH.
\end{aligned}
$$

令

$$
K=GH.
$$

因为右乘固定群元素 $H$ 只是对群元素重新编号，$G$ 遍历 $\mathcal G$ 时 $K$ 也恰好遍历一次 $\mathcal G$。因此

$$
\begin{aligned}
H^\dagger
\mathcal E_{\mathcal G}
(H\rho H^\dagger)
H
&=
\frac1{|\mathcal G|}
\sum_{K\in\mathcal G}
K^\dagger\mathcal E(K\rho K^\dagger)K\\
&=
\mathcal E_{\mathcal G}(\rho).
\end{aligned}
$$

等价地，

$$
\boxed{
\mathcal E_{\mathcal G}
(H\rho H^\dagger)
=
H\mathcal E_{\mathcal G}(\rho)H^\dagger
}.
$$

后面 Pauli channel 和 depolarizing channel 的简化形式，本质上都来自这个群协变性对通道矩阵的限制。

这个定义描述的是一个平均有效通道。若随机门本身有误差、噪声依赖于所选 $G$、或不同轮次存在记忆效应，就不能直接把实际实现等同于上述理想平均。

---
### 2. Pauli twirling：一般通道到 Pauli channel

对单 qubit，忽略整体相位后的 Pauli 集为

$$
\mathcal P_1=\{I,X,Y,Z\}.
$$

Pauli-twirled channel 是

$$
\mathcal E_{\mathrm P}(\rho)
=
\frac14
\sum_{P\in\mathcal P_1}
P\mathcal E(P\rho P)P.
$$

对任意单 qubit CPTP channel，结果可写成

$$
\boxed{
\mathcal E_{\mathrm P}(\rho)
=
p_I\rho
+p_XX\rho X
+p_YY\rho Y
+p_ZZ\rho Z
},
$$

这在后面会证明，其中

$$
p_I+p_X+p_Y+p_Z=1,
\qquad
p_\mu\geq0.
$$

因此 Pauli twirling 消去不同 Pauli 分量之间的相干耦合，但保留 $X,Y,Z$ 三个方向的不同错误概率。

#### 2.1 Pauli transfer matrix 表示（PTM表示)

##### 为什么是 $4\times4$ 矩阵

单 qubit Hilbert 空间是二维的，但量子通道 $\mathcal E$ 的输入不是态矢量，而是 $2\times2$ 算符：

$$
\mathcal E:\mathcal L(\mathbb C^2)\longrightarrow\mathcal L(\mathbb C^2).
$$

$2\times2$ 复矩阵组成的算符空间是四维的。一组方便的正交基是

$$
P_0=I,\quad P_1=X,\quad P_2=Y,\quad P_3=Z
$$

因为它们满足 Hilbert–Schmidt 正交关系

$$
\operatorname{Tr}(P_iP_j)=2\delta_{ij}.
$$

因此任意单 qubit 算符 $O$ 都能唯一展开为

$$
\boxed{
O
=
\sum_{j=0}^3
c_jP_j
},
$$

其中系数由内积投影得到：

$$
\boxed{
c_j=\frac12\operatorname{Tr}(P_jO)
}.
$$

推导如下。假设

$$
O=\sum_jc_jP_j.
$$

左乘 $P_i$ 并取迹：

$$
\begin{aligned}
\operatorname{Tr}(P_iO)
&=
\sum_jc_j\operatorname{Tr}(P_iP_j)\\
&=
\sum_jc_j\,2\delta_{ij}\\
&=2c_i.
\end{aligned}
$$

所以

$$
c_i=\frac12\operatorname{Tr}(P_iO),
$$

也就是上面的系数公式。把四个系数排列成列向量：

$$
\boxed{
\boldsymbol c(O)
=
\frac12
\begin{pmatrix}
\operatorname{Tr}(IO)\\
\operatorname{Tr}(XO)\\
\operatorname{Tr}(YO)\\
\operatorname{Tr}(ZO)
\end{pmatrix}
}.
$$

对 density matrix

$$
\rho=\frac12(I+r_xX+r_yY+r_zZ),
$$

对应的 Pauli 坐标向量是

$$
\boldsymbol c(\rho)
=
\frac12
\begin{pmatrix}
1\\
r_x\\
r_y\\
r_z
\end{pmatrix}.
$$

其中第一个展开系数恒为 $1/2$，因为

$$
c_0
=
\frac12\operatorname{Tr}(I\rho)
=
\frac12.
$$

为了直接使用通常的 Bloch 向量，常把公共因子 $1/2$ 提到外面，并定义增广 Bloch 坐标

$$
\boxed{
\boldsymbol s(\rho)
=
2\boldsymbol c(\rho)
=
\begin{pmatrix}
1\\
r_x\\
r_y\\
r_z
\end{pmatrix}
}.
$$

后面会看到，无论使用 $\boldsymbol c(\rho)$ 还是 $\boldsymbol s(\rho)$，通道都由同一个 PTM 相乘；二者只差全局因子 $2$。

##### 通道矩阵的每一列从哪里来

量子通道是线性映射。只要知道它对四个基算符

$$
I,\quad X,\quad Y,\quad Z
$$

分别做什么，就能知道它对任意算符做什么。

把每个输出 $\mathcal E(P_j)$ 再展开到 Pauli 基：

$$
\mathcal E(P_j)
=
\sum_{i=0}^3R_{ij}P_i.
$$

根据前面的系数投影公式，

$$
\boxed{
R_{ij}
=
\frac12\operatorname{Tr}
\left[
P_i\mathcal E(P_j)
\right]
}.
$$

物理量子通道保持 Hermitian 性。因为 $P_j$ 是 Hermitian，$\mathcal E(P_j)$ 也是 Hermitian；两个 Hermitian 算符乘积的迹为实数，所以 PTM 的元素 $R_{ij}$ 都是实数。

PTM 的第 $j$ 列是 $\mathcal E(P_j)$ 的直接展开系数 $\boldsymbol c(\mathcal E(P_j))$。

因此：

- 下标 $j$ 表示输入基算符 $P_j$；
- 下标 $i$ 表示输出中 $P_i$ 的系数；
- 矩阵第 $j$ 列就是 $\mathcal E(P_j)$ 的直接 Pauli 展开系数。

具体写成

$$
R_{\mathcal E}
=
\left[
\boldsymbol c(\mathcal E(I))
\ \middle|\
\boldsymbol c(\mathcal E(X))
\ \middle|\
\boldsymbol c(\mathcal E(Y))
\ \middle|\
\boldsymbol c(\mathcal E(Z))
\right].
$$

例如，第二列对应输入 $X$。若

$$
\mathcal E(X)
=
r_{xx}X+r_{yx}Y+r_{zx}Z,
$$

那么第二列就是

$$
\begin{pmatrix}
0\\
r_{xx}\\
r_{yx}\\
r_{zx}
\end{pmatrix}.
$$

第一个分量为零的原因是 trace-preserving channel 保持

$$
\operatorname{Tr}\mathcal E(X)
=
\operatorname{Tr}X
=0.
$$

##### 为什么第一行固定为 $(1,0,0,0)$

若 $\mathcal E$ 保持迹，则对任意算符 $O$ 都有

$$
\operatorname{Tr}\mathcal E(O)=\operatorname{Tr}O.
$$

令 $O=P_j$，得到

$$
\begin{aligned}
R_{0j}
&=
\frac12
\operatorname{Tr}
\left[
I\mathcal E(P_j)
\right]\\
&=
\frac12
\operatorname{Tr}\mathcal E(P_j)\\
&=
\frac12\operatorname{Tr}P_j.
\end{aligned}
$$

由于

$$
\operatorname{Tr}I=2,
\qquad
\operatorname{Tr}X
=\operatorname{Tr}Y
=\operatorname{Tr}Z
=0,
$$

所以

$$
R_{00}=1,
\qquad
R_{01}=R_{02}=R_{03}=0.
$$

这就解释了 trace-preserving 单 qubit channel 的第一行：

$$
R_{\mathcal E}
=
\begin{pmatrix}
1&0&0&0\\
t_x&r_{xx}&r_{xy}&r_{xz}\\
t_y&r_{yx}&r_{yy}&r_{yz}\\
t_z&r_{zx}&r_{zy}&r_{zz}
\end{pmatrix}.
$$

##### 第一列和平移向量的来源

矩阵第一列来自 $\mathcal E(I)$。保持迹只要求

$$
\operatorname{Tr}\mathcal E(I)=\operatorname{Tr}I=2,
$$

所以一般可以写成

$$
\boxed{
\mathcal E(I)
=
I+t_xX+t_yY+t_zZ
}.
$$

这里

$$
t_i
=
\frac12
\operatorname{Tr}
\left[
P_i\mathcal E(I)
\right].
$$

如果通道还满足幺正条件

$$
\mathcal E(I)=I,
$$

那么

$$
t_x=t_y=t_z=0.
$$

但幺正不等于 trace-preserving 。例如 amplitude damping 会把所有状态拉向 $|0\rangle$，因此 Bloch 球中心不再保持在原点，对应非零平移向量 $\vec t$。

##### PTM 如何作用在 Bloch 向量上

先对任意算符 $O=\sum_jc_jP_j$ 使用线性性：

$$
\begin{aligned}
\mathcal E(O)
&=
\sum_jc_j\mathcal E(P_j)\\
&=
\sum_{i,j}
R_{ij}c_jP_i.
\end{aligned}
$$

因此输出的直接展开系数满足

$$
\boldsymbol c(\mathcal E(O))
=
R_{\mathcal E}\boldsymbol c(O).
$$

对 density matrix，$\boldsymbol s=2\boldsymbol c$，所以公共因子 $2$ 抵消：

$$
\begin{aligned}
\boldsymbol s(\mathcal E(\rho))
&=
2\boldsymbol c(\mathcal E(\rho))\\
&=
2R_{\mathcal E}\boldsymbol c(\rho)\\
&=
R_{\mathcal E}\boldsymbol s(\rho).
\end{aligned}
$$

因此输出增广 Bloch 坐标满足普通矩阵乘法

$$
\boxed{
\boldsymbol s(\mathcal E(\rho))
=
R_{\mathcal E}\boldsymbol s(\rho)
}.
$$

也就是

$$
\begin{pmatrix}
1\\
r_x'\\
r_y'\\
r_z'
\end{pmatrix}
=
\begin{pmatrix}
1&0&0&0\\
t_x&r_{xx}&r_{xy}&r_{xz}\\
t_y&r_{yx}&r_{yy}&r_{yz}\\
t_z&r_{zx}&r_{zy}&r_{zz}
\end{pmatrix}
\begin{pmatrix}
1\\
r_x\\
r_y\\
r_z
\end{pmatrix}.
$$

所以 Bloch 向量的变换是仿射变换

$$
\boxed{
\vec r'
=
\vec t+M\vec r
},
$$

其中

$$
M=
\begin{pmatrix}
r_{xx}&r_{xy}&r_{xz}\\
r_{yx}&r_{yy}&r_{yz}\\
r_{zx}&r_{zy}&r_{zz}
\end{pmatrix}.
$$

- $\vec t$ 描述 Bloch 球中心的平移；
- $M$ 描述旋转、压缩和不同方向之间的混合。

##### 例子：逐列计算 amplitude-damping channel

取衰减概率 $\gamma\in[0,1]$，Kraus 算符为

$$
K_0=
\begin{pmatrix}
1&0\\
0&\sqrt{1-\gamma}
\end{pmatrix},
\qquad
K_1=
\begin{pmatrix}
0&\sqrt\gamma\\
0&0
\end{pmatrix}.
$$

它保持迹，因为

$$
K_0^\dagger K_0+K_1^\dagger K_1
=
\begin{pmatrix}
1&0\\
0&1-\gamma
\end{pmatrix}
+
\begin{pmatrix}
0&0\\
0&\gamma
\end{pmatrix}
=I.
$$

通道为

$$
\mathcal E_\gamma(O)
=
K_0OK_0^\dagger
+K_1OK_1^\dagger.
$$

先计算四个 Pauli 基算符的像。

对 $I$：

$$
\begin{aligned}
\mathcal E_\gamma(I)
&=
K_0K_0^\dagger+K_1K_1^\dagger\\
&=
\begin{pmatrix}
1+\gamma&0\\
0&1-\gamma
\end{pmatrix}\\
&=
I+\gamma Z.
\end{aligned}
$$

对 $X$：

$$
\begin{aligned}
\mathcal E_\gamma(X)
&=
\begin{pmatrix}
0&\sqrt{1-\gamma}\\
\sqrt{1-\gamma}&0
\end{pmatrix}\\
&=
\sqrt{1-\gamma}\,X.
\end{aligned}
$$

对 $Y$：

$$
\begin{aligned}
\mathcal E_\gamma(Y)
&=
\begin{pmatrix}
0&-i\sqrt{1-\gamma}\\
i\sqrt{1-\gamma}&0
\end{pmatrix}\\
&=
\sqrt{1-\gamma}\,Y.
\end{aligned}
$$

对 $Z$：

$$
\begin{aligned}
\mathcal E_\gamma(Z)
&=
\begin{pmatrix}
1&0\\
0&-(1-\gamma)
\end{pmatrix}
+
\begin{pmatrix}
-\gamma&0\\
0&0
\end{pmatrix}\\
&=
\begin{pmatrix}
1-\gamma&0\\
0&-(1-\gamma)
\end{pmatrix}\\
&=
(1-\gamma)Z.
\end{aligned}
$$

把四个输出的坐标依次作为四列：

$$
\boxed{
R_{\mathcal E_\gamma}
=
\begin{pmatrix}
1&0&0&0\\
0&\sqrt{1-\gamma}&0&0\\
0&0&\sqrt{1-\gamma}&0\\
\gamma&0&0&1-\gamma
\end{pmatrix}
}.
$$

例如左下角元素可直接由迹公式验证：

$$
\begin{aligned}
R_{30}
&=
\frac12
\operatorname{Tr}
\left[
Z\mathcal E_\gamma(I)
\right]\\
&=
\frac12
\operatorname{Tr}
\left[
Z(I+\gamma Z)
\right]\\
&=\gamma.
\end{aligned}
$$

作用在 Bloch 坐标上：

$$
\begin{pmatrix}
1\\
r_x'\\
r_y'\\
r_z'
\end{pmatrix}
=
R_{\mathcal E_\gamma}
\begin{pmatrix}
1\\
r_x\\
r_y\\
r_z
\end{pmatrix},
$$

所以

$$
\boxed{
\begin{aligned}
r_x'&=\sqrt{1-\gamma}\,r_x,\\
r_y'&=\sqrt{1-\gamma}\,r_y,\\
r_z'&=\gamma+(1-\gamma)r_z.
\end{aligned}
}
$$

$x,y$ 分量被压缩，而 $z$ 分量除压缩外还整体向 $+z$ 方向平移。这正对应 amplitude damping 把状态拉向

$$
|0\rangle\langle0|
=
\frac{I+Z}{2}.
$$

> 阅读 PTM 时最直接的方法：按列读。第一列是 $\mathcal E(I)$，第二列是 $\mathcal E(X)$，第三列是 $\mathcal E(Y)$，第四列是 $\mathcal E(Z)$。

作为最简单的检查，恒等通道满足

$$
\mathcal I(P_j)=P_j,
$$

所以四列依次是四个标准基向量：

$$
R_{\mathcal I}=I_4.
$$

构造一个单 qubit channel 的 PTM 可以归纳为四步：

1. 选定有序 Pauli 基 $(I,X,Y,Z)$；
2. 分别计算 $\mathcal E(I),\mathcal E(X),\mathcal E(Y),\mathcal E(Z)$；
3. 用
   $$
   R_{ij}
   =
   \frac12\operatorname{Tr}
   \left[P_i\mathcal E(P_j)\right]
   $$
   求每个输出的 Pauli 展开系数；
4. 按输入顺序把四组系数排成四列。

> 本文采用“列表示输入、行表示输出”和有序基 $(I,X,Y,Z)$。有些文献使用归一化基 $P_i/\sqrt2$、行向量或转置约定；比较 PTM 时必须先核对这些约定。

#### 2.2 为什么非对角项消失

下面推导为什么 Pauli twirling 只保留对角项。

对任意 $P\in\mathcal P_1$ 和 Pauli 基元素 $P_j$，共轭作用只会产生一个符号：

$$
PP_jP
=
\chi_j(P)P_j,
\qquad
\chi_j(P)\in\{+1,-1\}.
$$

其中 $\chi_j(P)=+1$ 表示 $P$ 与 $P_j$ 对易，$\chi_j(P)=-1$ 表示反对易。把通道对基元素的作用展开为

$$
\mathcal E(P_j)
=
\sum_{i=0}^3R_{ij}P_i.
$$

于是 twirled channel 对 $P_j$ 的作用为

$$
\begin{aligned}
\mathcal E_{\mathrm P}(P_j)
&=
\frac14\sum_{P\in\mathcal P_1}
P\mathcal E(PP_jP)P\\
&=
\frac14\sum_P
\chi_j(P)
P\mathcal E(P_j)P\\
&=
\frac14\sum_P
\sum_i
\chi_j(P)\chi_i(P)
R_{ij}P_i\\
&=
\sum_i
\left[
\frac14\sum_P
\chi_i(P)\chi_j(P)
\right]
R_{ij}P_i.
\end{aligned}
$$

单 qubit Pauli 共轭符号满足正交关系

$$
\frac14
\sum_{P\in\mathcal P_1}
\chi_i(P)\chi_j(P)
=
\delta_{ij}.
$$

例如 $i=X,j=Y$ 时，四个 $P=I,X,Y,Z$ 给出的乘积符号依次为

$$
+1,-1,-1,+1,
$$

总和为零；而 $i=j$ 时每项都是 $+1$。因此

$$
\mathcal E_{\mathrm P}(P_j)
=
R_{jj}P_j.
$$

特别地，对 $P_0=I$，

$$
\mathcal E(I)
=
I+t_xX+t_yY+t_zZ,
$$

而 $X,Y,Z$ 三个平移分量也因符号平均为零。这就得到

$$
R_{\mathcal E_{\mathrm P}}
=
\begin{pmatrix}
1&0&0&0\\
0&r_{xx}&0&0\\
0&0&r_{yy}&0\\
0&0&0&r_{zz}
\end{pmatrix}.
$$

所以平移项和 Pauli 分量间的混合项都在群平均后消失。

#### 2.3 从对角 PTM 恢复 Pauli channel 与 Kraus 表示

设 Pauli twirling 后的 PTM 为

$$
R_{\mathcal E_{\mathrm P}}
=
\begin{pmatrix}
1&0&0&0\\
0&\lambda_x&0&0\\
0&0&\lambda_y&0\\
0&0&0&\lambda_z
\end{pmatrix},
$$

其中

$$
\lambda_x=r_{xx},
\qquad
\lambda_y=r_{yy},
\qquad
\lambda_z=r_{zz}.
$$

按照 PTM 按列读取的规则，这个矩阵表示

$$
\boxed{
\begin{aligned}
\mathcal E_{\mathrm P}(I)&=I,\\
\mathcal E_{\mathrm P}(X)&=\lambda_xX,\\
\mathcal E_{\mathrm P}(Y)&=\lambda_yY,\\
\mathcal E_{\mathrm P}(Z)&=\lambda_zZ.
\end{aligned}
}
$$

因此对任意

$$
\rho
=
\frac12
\left(
I+r_xX+r_yY+r_zZ
\right),
$$

利用通道线性性可以直接得到

$$
\boxed{
\mathcal E_{\mathrm P}(\rho)
=
\frac12
\left(
I+\lambda_xr_xX+\lambda_yr_yY+\lambda_zr_zZ
\right)
}.
$$

这已经由 PTM 唯一确定了 $\mathcal E_{\mathrm P}(\rho)$。下面的工作不是重新定义通道，而是把同一个线性映射改写为具有明确物理概率含义的 Pauli/Kraus 形式。

目标是把这个线性映射写成

$$
\boxed{
\mathcal E_{\mathrm P}(\rho)
=
p_I\rho
+p_X\,X\rho X
+p_Y\,Y\rho Y
+p_Z\,Z\rho Z
}.
$$

##### 2.3.1 为什么应当尝试 Pauli 随机混合

定义四个 Pauli 共轭通道

$$
\mathcal P_\mu(O)
=
P_\mu OP_\mu,
\qquad
P_\mu\in\{I,X,Y,Z\}.
$$

每个 $\mathcal P_\mu$ 在 Pauli 基下都是对角的，因为两个 Pauli 算符要么对易、要么反对易：

$$
P_\mu P_jP_\mu
=
\pm P_j.
$$

具体符号为

$$
\begin{array}{c|rrrr}
&
I&X&Y&Z\\
\hline
I(\cdot)I&I&X&Y&Z\\
X(\cdot)X&I&X&-Y&-Z\\
Y(\cdot)Y&I&-X&Y&-Z\\
Z(\cdot)Z&I&-X&-Y&Z
\end{array}
$$

因此这四个共轭通道的 PTM 分别是

$$
\begin{aligned}
R_I&=\operatorname{diag}(1,1,1,1),\\
R_X&=\operatorname{diag}(1,1,-1,-1),\\
R_Y&=\operatorname{diag}(1,-1,1,-1),\\
R_Z&=\operatorname{diag}(1,-1,-1,1).
\end{aligned}
$$

任意 Pauli 随机混合

$$
\mathcal F
=
p_I\mathcal I
+p_X\mathcal X
+p_Y\mathcal Y
+p_Z\mathcal Z
$$

的 PTM 由线性性给出：

$$
R_{\mathcal F}
=
p_IR_I+p_XR_X+p_YR_Y+p_ZR_Z.
$$

为了使 $\mathcal F=\mathcal E_{\mathrm P}$，只需让两个通道在基

$$
\{I,X,Y,Z\}
$$

上的作用完全相同。

##### 2.3.2 建立并求解概率方程

先作用在 $I$ 上。所有 Pauli 共轭都保持 $I$：

$$
\mathcal F(I)
=
(p_I+p_X+p_Y+p_Z)I.
$$

为了匹配

$$
\mathcal E_{\mathrm P}(I)=I,
$$

必须有

$$
\boxed{
p_I+p_X+p_Y+p_Z=1
}.
$$

再作用在 $X$ 上：

$$
\begin{aligned}
\mathcal F(X)
={}&
p_I(IXI)
+p_X(XXX)
+p_Y(YXY)
+p_Z(ZXZ)\\
={}&
(p_I+p_X-p_Y-p_Z)X.
\end{aligned}
$$

这里使用了

$$
XXX=X,
\qquad
YXY=-X,
\qquad
ZXZ=-X.
$$

与

$$
\mathcal E_{\mathrm P}(X)=\lambda_xX
$$

比较，得到

$$
\lambda_x=p_I+p_X-p_Y-p_Z.
$$

同理，逐项使用

$$
XYX=-Y,\quad YYY=Y,\quad ZYZ=-Y,
$$

以及

$$
XZX=-Z,\quad YZY=-Z,\quad ZZZ=Z,
$$

得到

$$
\begin{aligned}
\lambda_y&=p_I-p_X+p_Y-p_Z,\\
\lambda_z&=p_I-p_X-p_Y+p_Z.
\end{aligned}
$$

四个线性方程可以统一写成

$$
\begin{pmatrix}
1\\
\lambda_x\\
\lambda_y\\
\lambda_z
\end{pmatrix}
=
\underbrace{
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}
}_{H_4}
\begin{pmatrix}
p_I\\
p_X\\
p_Y\\
p_Z
\end{pmatrix}.
$$

这个符号矩阵满足

$$
H_4^2=4I_4,
$$

所以

$$
H_4^{-1}=\frac14H_4.
$$

因此概率为

$$
\boxed{
\begin{aligned}
p_I&=\frac{1+\lambda_x+\lambda_y+\lambda_z}{4},\\
p_X&=\frac{1+\lambda_x-\lambda_y-\lambda_z}{4},\\
p_Y&=\frac{1-\lambda_x+\lambda_y-\lambda_z}{4},\\
p_Z&=\frac{1-\lambda_x-\lambda_y+\lambda_z}{4}.
\end{aligned}
}
$$

把

$$
\lambda_x=r_{xx},
\qquad
\lambda_y=r_{yy},
\qquad
\lambda_z=r_{zz}
$$

代入，就能直接从对角 PTM 得到四个 Pauli 错误概率。

##### 2.3.3 从概率写成 Kraus operator

当

$$
p_I,p_X,p_Y,p_Z\geq0
$$

时，可以定义 Kraus operators

$$
\boxed{
\begin{aligned}
K_I&=\sqrt{p_I}\,I,\\
K_X&=\sqrt{p_X}\,X,\\
K_Y&=\sqrt{p_Y}\,Y,\\
K_Z&=\sqrt{p_Z}\,Z.
\end{aligned}
}
$$

直接把 PTM 本征值代入，可以写成

$$
\boxed{
\begin{aligned}
K_I
&=
\frac12
\sqrt{1+\lambda_x+\lambda_y+\lambda_z}\,I,\\
K_X
&=
\frac12
\sqrt{1+\lambda_x-\lambda_y-\lambda_z}\,X,\\
K_Y
&=
\frac12
\sqrt{1-\lambda_x+\lambda_y-\lambda_z}\,Y,\\
K_Z
&=
\frac12
\sqrt{1-\lambda_x-\lambda_y+\lambda_z}\,Z.
\end{aligned}
}
$$

根号内非负正是后面列出的完全正条件。若某个概率为零，对应的 Kraus operator 可以省略。

Kraus 形式为

$$
\begin{aligned}
\mathcal E_{\mathrm P}(\rho)
&=
\sum_{\mu\in\{I,X,Y,Z\}}
K_\mu\rho K_\mu^\dagger\\
&=
p_I\rho
+p_X\,X\rho X
+p_Y\,Y\rho Y
+p_Z\,Z\rho Z.
\end{aligned}
$$

因为 Pauli 算符都是 Hermitian unitary，

$$
P_\mu^\dagger P_\mu=I,
$$

所以 Kraus 完备关系为

$$
\begin{aligned}
\sum_\mu K_\mu^\dagger K_\mu
&=
\sum_\mu p_\mu P_\mu^\dagger P_\mu\\
&=
\left(
p_I+p_X+p_Y+p_Z
\right)I\\
&=I.
\end{aligned}
$$

这验证了该 Kraus 表示保持迹。

同时，任何写成

$$
\sum_\mu K_\mu\rho K_\mu^\dagger
$$

的映射都是完全正的。因此“$p_\mu\geq0$”给出完全正性，“$\sum_\mu p_\mu=1$”给出保持迹。

Kraus 表示本身并不唯一，但

$$
\{\sqrt{p_I}I,\sqrt{p_X}X,\sqrt{p_Y}Y,\sqrt{p_Z}Z\}
$$

是 Pauli channel 最直接的一组 Kraus operators。

##### 2.3.4 完全正条件在对角 PTM 中是什么

并非任意三个实数

$$
(\lambda_x,\lambda_y,\lambda_z)
$$

都对应物理量子通道。完全正要求反演得到的四个概率均非负：

$$
\boxed{
\begin{aligned}
1+\lambda_x+\lambda_y+\lambda_z&\geq0,\\
1+\lambda_x-\lambda_y-\lambda_z&\geq0,\\
1-\lambda_x+\lambda_y-\lambda_z&\geq0,\\
1-\lambda_x-\lambda_y+\lambda_z&\geq0.
\end{aligned}
}
$$

这些不等式定义了 $(\lambda_x,\lambda_y,\lambda_z)$ 空间中的一个四面体，其四个顶点对应四个确定性 Pauli 共轭：

$$
\begin{aligned}
I&:(1,1,1),\\
X&:(1,-1,-1),\\
Y&:(-1,1,-1),\\
Z&:(-1,-1,1).
\end{aligned}
$$

由于 $\mathcal E_{\mathrm P}$ 是由原始 CPTP channel 经过 Pauli twirling 得到的，它自动满足这些完全正条件。

##### 2.3.5 例子：随机 Z 错误

若对角 PTM 是

$$
R
=
\operatorname{diag}
\left(
1,1-2q,1-2q,1
\right),
$$

则

$$
\lambda_x=\lambda_y=1-2q,
\qquad
\lambda_z=1.
$$

代入反演公式：

$$
\begin{aligned}
p_I
&=
\frac{
1+(1-2q)+(1-2q)+1
}{4}
=1-q,\\
p_X
&=
\frac{
1+(1-2q)-(1-2q)-1
}{4}
=0,\\
p_Y
&=0,\\
p_Z
&=
\frac{
1-(1-2q)-(1-2q)+1
}{4}
=q.
\end{aligned}
$$

所以

$$
\boxed{
\mathcal E(\rho)
=(1-q)\rho+qZ\rho Z
}
$$

且可取 Kraus operators

$$
\boxed{
K_0=\sqrt{1-q}\,I,
\qquad
K_1=\sqrt q\,Z
}.
$$

> 从对角 PTM 到 Kraus 形式的核心步骤：先把三个对角本征值反演为四个 Pauli 概率，再对每个概率开平方并乘以对应 Pauli 算符。

---
### 3. 例子：相干 Z 旋转变成随机 Z 错误

考虑 coherent over-rotation

$$
U_\theta=e^{-i\theta Z/2},
\qquad
\mathcal U_\theta(\rho)
=U_\theta\rho U_\theta^\dagger.
$$

它对 Pauli 算符的作用为

$$
U_\theta
=
\cos\frac{\theta}{2}I
-i\sin\frac{\theta}{2}Z.
$$

令

$$
c=\cos\frac{\theta}{2},
\qquad
s=\sin\frac{\theta}{2}.
$$

利用

$$
ZX=iY,
\qquad
XZ=-iY,
\qquad
ZXZ=-X,
$$

可逐步得到

$$
\begin{aligned}
U_\theta XU_\theta^\dagger
&=(cI-isZ)X(cI+isZ)\\
&=c^2X+ics(XZ-ZX)+s^2ZXZ\\
&=(c^2-s^2)X+2csY\\
&=\cos\theta\,X+\sin\theta\,Y.
\end{aligned}
$$

对 $Y$ 使用

$$
ZY=-iX,
\qquad
YZ=iX,
\qquad
ZYZ=-Y,
$$

得到

$$
\begin{aligned}
U_\theta YU_\theta^\dagger
&=(cI-isZ)Y(cI+isZ)\\
&=c^2Y+ics(YZ-ZY)+s^2ZYZ\\
&=-2csX+(c^2-s^2)Y\\
&=-\sin\theta\,X+\cos\theta\,Y.
\end{aligned}
$$

由于 $U_\theta$ 是 $Z$ 的函数，它与 $Z$ 对易，因此

$$
U_\theta ZU_\theta^\dagger=Z.
$$

因此

$$
R_{\mathcal U_\theta}
=
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&-\sin\theta&0\\
0&\sin\theta&\cos\theta&0\\
0&0&0&1
\end{pmatrix}.
$$

这里不能把“删除非对角项”当作定义直接操作矩阵。必须从 Pauli twirling 的群平均计算：

$$
\mathcal U_{\theta,\mathrm P}(\rho)
=
\frac14
\sum_{P\in\{I,X,Y,Z\}}
P\,U_\theta(P\rho P)U_\theta^\dagger P.
$$

利用 $P^2=I$，每一项可改写为

$$
P\,U_\theta(P\rho P)U_\theta^\dagger P
=
(PU_\theta P)\rho(PU_\theta^\dagger P).
$$

若 $P=I,Z$，则 $P$ 与 $Z$ 对易，因此

$$
PZP=Z
$$

并且

$$
PU_\theta P
=
\exp\left(-\frac{i\theta}{2}PZP\right)
=U_\theta.
$$

若 $P=X,Y$，则 $P$ 与 $Z$ 反对易，因此

$$
PZP=-Z
$$

并且

$$
PU_\theta P
=
\exp\left(-\frac{i\theta}{2}PZP\right)
=
\exp\left(+\frac{i\theta Z}{2}\right)
=U_\theta^\dagger
=U_{-\theta}.
$$

所以四项平均实际是

$$
\boxed{
\mathcal U_{\theta,\mathrm P}(\rho)
=
\frac12
\left[
U_\theta\rho U_\theta^\dagger
+
U_\theta^\dagger\rho U_\theta
\right]
}.
$$

对应的 PTM 也必须通过平均得到：

$$
\begin{aligned}
R_{\mathcal U_{\theta,\mathrm P}}
&=
\frac12
\left(
R_{\mathcal U_\theta}
+
R_{\mathcal U_{-\theta}}
\right)\\
&=
\frac12
\left[
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&-\sin\theta&0\\
0&\sin\theta&\cos\theta&0\\
0&0&0&1
\end{pmatrix}
+
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&\sin\theta&0\\
0&-\sin\theta&\cos\theta&0\\
0&0&0&1
\end{pmatrix}
\right]\\
&=
\operatorname{diag}
(1,\cos\theta,\cos\theta,1).
\end{aligned}
$$

因此 $\pm\sin\theta$ 项并不是被任意删去，而是因为 $\theta$ 与 $-\theta$ 两个旋转在群平均中权重相同，反对称的相干项彼此抵消。

还可以直接在通道层面验证。令

$$
c=\cos\frac{\theta}{2},
\qquad
s=\sin\frac{\theta}{2},
$$

则

$$
\begin{aligned}
U_\theta\rho U_\theta^\dagger
={}&
c^2\rho+s^2Z\rho Z
+ics(\rho Z-Z\rho),\\
U_\theta^\dagger\rho U_\theta
={}&
c^2\rho+s^2Z\rho Z
-ics(\rho Z-Z\rho).
\end{aligned}
$$

平均后，commutator 对应的相干项抵消：

$$
\boxed{
\mathcal U_{\theta,\mathrm P}(\rho)
=
c^2\rho+s^2Z\rho Z
}.
$$

因此最终得到

$$
R_{\mathcal U_{\theta,\mathrm P}}
=
\operatorname{diag}
(1,\cos\theta,\cos\theta,1).
$$

随机 $Z$ 错误通道

$$
\mathcal Z_q(\rho)
=(1-q)\rho+qZ\rho Z
$$

的 Pauli transfer matrix 为

$$
R_{\mathcal Z_q}
=
\operatorname{diag}
(1,1-2q,1-2q,1).
$$

比较两式可得

$$
1-2q=\cos\theta,
$$

即

$$
\boxed{
q=\sin^2\frac{\theta}{2}
}.
$$

所以

$$
\boxed{
\mathcal U_{\theta,\mathrm P}(\rho)
=
\cos^2\frac{\theta}{2}\rho
+
\sin^2\frac{\theta}{2}Z\rho Z
}.
$$

原始通道会在多轮作用下相干积累旋转角；twirled model 则是随机错误。两者具有相同的相关对角参数，但不是逐次演化完全相同的物理噪声。

---
### 4. Full Clifford twirling：Pauli 方向进一步平均

单 qubit Clifford 群通过共轭置换

$$
\{\pm X,\pm Y,\pm Z\}.
$$

对通道使用完整 Clifford 群平均，会把三个非平凡 Pauli 方向的收缩率变成相同数值。结果是 depolarizing channel。

#### 4.1 从 Pauli 方向到 Clifford 轨道平均

可以先对通道做 Pauli twirling，因为 Pauli 群是 Clifford 群的正规子群。忽略不影响共轭通道的整体相位，取商群 $\mathcal C_1/\mathcal P_1$ 的六个陪集代表 $R$，每个 Clifford 可唯一写成

$$
C=PR,
\qquad
P\in\mathcal P_1.
$$

于是完整 Clifford 平均可重排为

$$
\begin{aligned}
\mathcal E_{\mathrm C}(\rho)
&=
\frac1{24}
\sum_R\sum_P
R^\dagger P^\dagger
\mathcal E
(PR\rho R^\dagger P^\dagger)
PR\\
&=
\frac16
\sum_R
R^\dagger
\mathcal E_{\mathrm P}
(R\rho R^\dagger)
R.
\end{aligned}
$$

所以 inner average 正是 Pauli twirling，outer average 再把三个 Pauli 方向混合。设 Pauli-twirled channel 满足

$$
\mathcal E_{\mathrm P}(X)=\lambda_xX,
\qquad
\mathcal E_{\mathrm P}(Y)=\lambda_yY,
\qquad
\mathcal E_{\mathrm P}(Z)=\lambda_zZ.
$$

对固定的非平凡 Pauli $P_j$，任意 Clifford $C$ 都满足

$$
CP_jC^\dagger=s(C,j)P_{k(C,j)},
\qquad
s(C,j)\in\{\pm1\}.
$$

代入 twirling 定义：

$$
\begin{aligned}
\mathcal E_{\mathrm C}(P_j)
&=
\frac{1}{|\mathcal C_1|}
\sum_{C\in\mathcal C_1}
C^\dagger
\mathcal E_{\mathrm P}
(CP_jC^\dagger)
C\\
&=
\frac{1}{|\mathcal C_1|}
\sum_C
s(C,j)\lambda_{k(C,j)}
C^\dagger P_{k(C,j)}C\\
&=
\frac{1}{|\mathcal C_1|}
\sum_C
\lambda_{k(C,j)}P_j.
\end{aligned}
$$

最后一步中两个共轭符号相互抵消。单 qubit Clifford 群共有 $24$ 个元素；对固定的 $P_j$，其中各有 $8$ 个元素把它映到 $\pm X$、$\pm Y$、$\pm Z$ 中的某一轴。因此三个方向在群平均中出现次数相同，从而

$$
\mathcal E_{\mathrm C}(P_j)
=
\bar\lambda P_j,
\qquad
\bar\lambda
=
\frac{\lambda_x+\lambda_y+\lambda_z}{3}.
$$

同时 $\mathcal E_{\mathrm C}(I)=I$。若

$$
\rho=\frac12(I+r_xX+r_yY+r_zZ),
$$

则

$$
\begin{aligned}
\mathcal E_{\mathrm C}(\rho)
&=
\frac12
\left[
I+\bar\lambda
(r_xX+r_yY+r_zZ)
\right]\\
&=
\bar\lambda\rho
+(1-\bar\lambda)\frac I2.
\end{aligned}
$$

这就是 depolarizing channel。令 $\lambda=\bar\lambda$。

#### 4.2 Depolarizing channel 的两种参数化

一种参数化是

$$
\boxed{
\mathcal D_\lambda(\rho)
=
\lambda\rho
+(1-\lambda)\frac{I}{2}
}.
$$

也可以写成随机 Pauli 错误形式

$$
\boxed{
\mathcal D_p(\rho)
=
(1-p)\rho
+
\frac p3
\left(
X\rho X+Y\rho Y+Z\rho Z
\right)
},
$$

两种参数满足

$$
\lambda=1-\frac{4p}{3}.
$$

这里 $p$ 表示三个非恒等 Pauli 错误的总概率，不等于 Bloch 收缩参数中的 $1-\lambda$；两种文献参数化比较时必须先核对定义。

这个关系也可以直接推导。对任意单 qubit density matrix

$$
\rho=\frac12(I+\vec r\cdot\vec\sigma),
$$

三个 Pauli 共轭之和为

$$
X\rho X+Y\rho Y+Z\rho Z
=
2I-\rho.
$$

原因是每个 Bloch 分量在一个同轴共轭中保号、在另外两个共轭中变号。例如 $r_xX$ 的总系数为

$$
+1-1-1=-1.
$$

所以

$$
\begin{aligned}
\mathcal D_p(\rho)
&=
(1-p)\rho+\frac p3(2I-\rho)\\
&=
\left(1-\frac{4p}{3}\right)\rho
+\frac{2p}{3}I\\
&=
\lambda\rho+(1-\lambda)\frac I2,
\end{aligned}
$$

从而

$$
\lambda=1-\frac{4p}{3}.
$$

因此：

$$
\begin{array}{c|c|c}
\text{twirling 集合}
&
\text{输出通道}
&
\text{保留的信息}
\\
\hline
\mathcal P_1
&
\text{Pauli channel}
&
p_X,p_Y,p_Z\text{ 可不同}
\\
\mathcal C_1
&
\text{depolarizing channel}
&
X,Y,Z\text{ 方向完全等价}
\end{array}
$$

这里的 full Clifford channel twirl 依赖 Clifford 群的 unitary 2-design 性质。它与下一节只使用两个 Clifford 元素的 magic-state twirl 不同。

---
### 5. T magic state 的本征基

定义

$$
T=\operatorname{diag}(1,e^{i\pi/4}),
\qquad
|T\rangle
=
T|+\rangle
=
\frac{|0\rangle+e^{i\pi/4}|1\rangle}{\sqrt2}.
$$

与其正交的状态可选为

$$
|T_\perp\rangle
=Z|T\rangle
=
\frac{|0\rangle-e^{i\pi/4}|1\rangle}{\sqrt2},
$$

因为

$$
\langle T|Z|T\rangle=0.
$$

引入 Hermitian Clifford 算符

$$
A=\frac{X+Y}{\sqrt2}.
$$

#### 5.1 验证 $A$ 是 Clifford 算符

先验证它是 Hermitian unitary。由于

$$
X^\dagger=X,
\qquad
Y^\dagger=Y,
$$

所以 $A^\dagger=A$。又因为

$$
X^2=Y^2=I,
\qquad
XY=-YX,
$$

故

$$
\begin{aligned}
A^2
&=
\frac12(X+Y)^2\\
&=
\frac12(X^2+XY+YX+Y^2)\\
&=I.
\end{aligned}
$$

再验证它把 Pauli 算符映到 Pauli 算符。例如

$$
\begin{aligned}
AXA
&=
\frac12(X+Y)X(X+Y)\\
&=
\frac12
\left(
XXX+XXY+YXX+YXY
\right)\\
&=
\frac12(X+Y+Y-X)\\
&=Y.
\end{aligned}
$$

另一个方向为

$$
\begin{aligned}
AYA
&=
\frac12(X+Y)Y(X+Y)\\
&=
\frac12
\left(
XYX+XYY+YYX+YYY
\right)\\
&=
\frac12(-Y+X+X+Y)\\
&=X.
\end{aligned}
$$

因为 $X$、$Y$ 都与 $Z$ 反对易，所以 $A$ 也与 $Z$ 反对易：

$$
AZ=-ZA.
$$

结合 $A^2=I$，

$$
AZA=-ZA^2=-Z.
$$

因此

$$
AXA=Y,
\qquad
AYA=X,
\qquad
AZA=-Z,
$$

说明 $A$ 的共轭作用保持 Pauli 群，所以 $A$ 属于单 qubit Clifford 群。

#### 5.2 验证 $|T\rangle$ 与 $|T_\perp\rangle$ 是本征态

接着验证它的本征态。矩阵形式为

$$
\begin{aligned}
A
&=
\frac1{\sqrt2}
\begin{pmatrix}
0&1-i\\
1+i&0
\end{pmatrix}\\
&=
\begin{pmatrix}
0&e^{-i\pi/4}\\
e^{i\pi/4}&0
\end{pmatrix}.
\end{aligned}
$$

因此

$$
\begin{aligned}
A|T\rangle
&=
\frac1{\sqrt2}
\begin{pmatrix}
0&e^{-i\pi/4}\\
e^{i\pi/4}&0
\end{pmatrix}
\begin{pmatrix}
1\\
e^{i\pi/4}
\end{pmatrix}\\
&=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
e^{i\pi/4}
\end{pmatrix}\\
&=|T\rangle.
\end{aligned}
$$

而 $|T_\perp\rangle=Z|T\rangle$，所以

$$
\begin{aligned}
A|T_\perp\rangle
&=AZ|T\rangle\\
&=-ZA|T\rangle\\
&=-Z|T\rangle\\
&=-|T_\perp\rangle.
\end{aligned}
$$

于是

$$
A|T\rangle=|T\rangle,
\qquad
A|T_\perp\rangle=-|T_\perp\rangle.
$$

对应的本征投影为

$$
\Pi_\pm=\frac{I\pm A}{2}.
$$

验证很直接：

$$
\Pi_\pm^2
=
\frac{I\pm2A+A^2}{4}
=
\frac{I\pm A}{2}
=\Pi_\pm,
$$

并且

$$
\Pi_+\Pi_-
=
\frac{I-A^2}{4}
=0.
$$

由于两个本征空间都是一维，得到

$$
\Pi_+
=|T\rangle\langle T|
=\frac{I+A}{2},
$$

$$
\Pi_-
=|T_\perp\rangle\langle T_\perp|
=Z|T\rangle\langle T|Z
=\frac{I-A}{2}.
$$

---
### 6. Magic-state twirling 的精确映射

#### 6.1 随机化映射与矩阵块消去

对任意单 qubit state $\rho$，随机施加 $I$ 或 $A$，各以概率 $1/2$：

$$
\boxed{
\mathcal T_A(\rho)
=
\frac12(\rho+A\rho A)
}.
$$

因为 $A=\Pi_+-\Pi_-$，展开可得

$$
I=\Pi_++\Pi_-,
\qquad
A=\Pi_+-\Pi_-.
$$

先用单位分解把 $\rho$ 写成四个块：

$$
\begin{aligned}
\rho
&=
(\Pi_++\Pi_-)
\rho
(\Pi_++\Pi_-)\\
&=
\Pi_+\rho\Pi_+
+\Pi_+\rho\Pi_-
+\Pi_-\rho\Pi_+
+\Pi_-\rho\Pi_-.
\end{aligned}
$$

而

$$
\begin{aligned}
A\rho A
&=
(\Pi_+-\Pi_-)
\rho
(\Pi_+-\Pi_-)\\
&=
\Pi_+\rho\Pi_+
-\Pi_+\rho\Pi_-
-\Pi_-\rho\Pi_+
+\Pi_-\rho\Pi_-.
\end{aligned}
$$

两式相加后，非对角块恰好抵消：

$$
\mathcal T_A(\rho)
=
\Pi_+\rho\Pi_+
+
\Pi_-\rho\Pi_-.
$$

这说明 $\mathcal T_A$ 是在

$$
\{|T\rangle,|T_\perp\rangle\}
$$

基中的完全 dephasing：对角概率保持不变，两个本征态之间的相干项被消去。

任意输入态都可写成

$$
\begin{aligned}
\rho
={}&
(1-p)|T\rangle\langle T|
+p|T_\perp\rangle\langle T_\perp|\\
&+\alpha|T\rangle\langle T_\perp|
+\alpha^*|T_\perp\rangle\langle T|.
\end{aligned}
$$

twirling 后得到

$$
\boxed{
\mathcal T_A(\rho)
=
(1-p)|T\rangle\langle T|
+
pZ|T\rangle\langle T|Z
}.
$$

这里可以直接看到四个矩阵块的变化：

$$
\begin{array}{c|c}
\text{矩阵块}
&
\mathcal T_A\text{ 的作用}
\\
\hline
|T\rangle\langle T|
&
|T\rangle\langle T|
\\
|T_\perp\rangle\langle T_\perp|
&
|T_\perp\rangle\langle T_\perp|
\\
|T\rangle\langle T_\perp|
&
0
\\
|T_\perp\rangle\langle T|
&
0
\end{array}
$$

#### 6.2 错误概率与 fidelity

其中

$$
\boxed{
p
=
\langle T_\perp|\rho|T_\perp\rangle
=\operatorname{Tr}(\rho \Pi_{-})=\operatorname{Tr}\left( \rho \frac{I-A}{2} \right)=
\frac{1-\operatorname{Tr}(A\rho)}{2}
}
$$

且

$$
1-p
=
\langle T|\rho|T\rangle.
$$

因此 twirling 保持 target-state fidelity：

$$
\begin{aligned}
\langle T|\mathcal T_A(\rho)|T\rangle
&=
\langle T|
\Pi_+\rho\Pi_+
|T\rangle\\
&=
\langle T|\rho|T\rangle,
\end{aligned}
$$

其中含 $\Pi_-$ 的项被 $\Pi_-|T\rangle=0$ 消掉。

它没有提高单个输入态对 $|T\rangle$ 的保真度，只是把同一保真度下的相干偏差转成经典二点混合模型。

---
### 7. Bloch 球上的几何意义

$|T\rangle$ 的 Bloch 方向为

$$
\hat t
=
\frac{1}{\sqrt2}(1,1,0),
$$

并且

$$
A=\hat t\cdot(X,Y,Z).
$$

若

$$
\rho=\frac12(I+\vec r\cdot\vec\sigma),
$$

为了推导 twirling 后的 Bloch 向量，使用 Pauli 乘法恒等式

$$
(\vec a\cdot\vec\sigma)
(\vec b\cdot\vec\sigma)
=
(\vec a\cdot\vec b)I
+i(\vec a\times\vec b)\cdot\vec\sigma.
$$

取 $\vec a=\hat t$，并利用 $|\hat t|=1$，可得

$$
\begin{aligned}
A(\vec r\cdot\vec\sigma)A
&=
(\hat t\cdot\vec\sigma)
(\vec r\cdot\vec\sigma)
(\hat t\cdot\vec\sigma)\\
&=
\left[
(\hat t\cdot\vec r)I
+i(\hat t\times\vec r)\cdot\vec\sigma
\right]
(\hat t\cdot\vec\sigma)\\
&=
(\hat t\cdot\vec r)
\hat t\cdot\vec\sigma
-
\left[
(\hat t\times\vec r)\times\hat t
\right]\cdot\vec\sigma\\
&=
\left[
2(\vec r\cdot\hat t)\hat t-\vec r
\right]\cdot\vec\sigma.
\end{aligned}
$$

其中使用了

$$
(\hat t\times\vec r)\cdot\hat t=0
$$

和向量三重积

$$
(\hat t\times\vec r)\times\hat t
=
\vec r-(\vec r\cdot\hat t)\hat t.
$$

这个共轭作用是在 Bloch 球上绕 $\hat t$ 轴旋转 $\pi$：平行分量保持，垂直分量反号。代入

$$
\mathcal T_A(\rho)
=
\frac12(\rho+A\rho A),
$$

得到

$$
\begin{aligned}
\mathcal T_A(\rho)
&=
\frac14
\left[
2I+
\vec r\cdot\vec\sigma
+
\left(
2(\vec r\cdot\hat t)\hat t-\vec r
\right)\cdot\vec\sigma
\right]\\
&=
\frac12
\left[
I+
(\vec r\cdot\hat t)
\hat t\cdot\vec\sigma
\right].
\end{aligned}
$$

因此 magic-state twirling 把 Bloch 向量正交投影到 $\hat t$ 轴：

$$
\boxed{
\vec r
\longmapsto
(\vec r\cdot\hat t)\hat t
}.
$$

输出态可写成

$$
\mathcal T_A(\rho)
=
\frac12
\left[
I+(1-2p)A
\right].
$$

因此

$$
1-2p=\operatorname{Tr}(A\rho)=\vec r\cdot\hat t.
$$

> Magic-state twirling 不是把 Bloch 球所有方向都平均掉，而是保留目标 magic axis 上的极化，删除垂直于该轴的分量。

---
### 8. 例子：T state 的相干相位偏差

考虑带相位偏差的纯态

$$
|T_\delta\rangle
=
\frac{
|0\rangle
+e^{i(\pi/4+\delta)}|1\rangle
}{\sqrt2}.
$$

它与目标态的 fidelity 为

$$
\begin{aligned}
|\langle T|T_\delta\rangle|^2
&=
\left|
\frac{1+e^{i\delta}}{2}
\right|^2\\
&=
\cos^2\frac{\delta}{2}.
\end{aligned}
$$

所以经过 magic-state twirling 后，

$$
\mathcal T_A
\left(
|T_\delta\rangle\langle T_\delta|
\right)
=
\cos^2\frac{\delta}{2}
|T\rangle\langle T|
+
\sin^2\frac{\delta}{2}
Z|T\rangle\langle T|Z.
$$

等效随机错误率为

$$
\boxed{
p=\sin^2\frac{\delta}{2}
}.
$$

这与前面的 coherent $Z$-rotation channel 示例形式相同，但对象不同：前者 twirl 的是量子通道，当前 twirl 的是制备完成后的 noisy magic state。

---
### 9. 多输入状态：去相干不等于独立同分布

对 $n$ 个 magic states 独立施加局域 twirl

$$
\mathcal T_A^{\otimes n},
$$

定义 error-pattern operator

$$
Z(x)
=
\bigotimes_{j=1}^n Z_j^{x_j},
\qquad
x=(x_1,\ldots,x_n)\in\mathbb F_2^n.
$$

#### 9.1 多比特 twirl 的投影算符推导

对每个 qubit 定义

$$
\Pi_0=|T\rangle\langle T|,
\qquad
\Pi_1=|T_\perp\rangle\langle T_\perp|.
$$

多比特 error-pattern projector 为

$$
\Pi_x
=
\bigotimes_{j=1}^n\Pi_{x_j}.
$$

由于

$$
|T_\perp\rangle=Z|T\rangle,
$$

它也可写成

$$
\Pi_x
=
Z(x)|T\rangle\langle T|^{\otimes n}Z(x).
$$

现在推导局域 twirl。令

$$
A(s)
=
\bigotimes_{j=1}^nA_j^{s_j},
\qquad
s\in\mathbb F_2^n.
$$

则

$$
\mathcal T_A^{\otimes n}(\rho)
=
\frac1{2^n}
\sum_{s\in\mathbb F_2^n}
A(s)\rho A(s).
$$

$A(s)$ 在 $\Pi_x$ 子空间上的本征值为

$$
(-1)^{s\cdot x},
$$

因为每个满足 $s_j=x_j=1$ 的位置贡献一个 $-1$。插入单位分解

$$
I=\sum_x\Pi_x
$$

可得

$$
\begin{aligned}
\mathcal T_A^{\otimes n}(\rho)
&=
\frac1{2^n}
\sum_s
\sum_{x,y}
A(s)\Pi_x\rho\Pi_yA(s)\\
&=
\sum_{x,y}
\left[
\frac1{2^n}
\sum_s
(-1)^{s\cdot(x+y)}
\right]
\Pi_x\rho\Pi_y.
\end{aligned}
$$

这里 $x+y$ 是 $\mathbb F_2^n$ 中的按位异或。二进制角色正交关系给出

$$
\frac1{2^n}
\sum_{s\in\mathbb F_2^n}
(-1)^{s\cdot(x+y)}
=
\delta_{xy}.
$$

当 $x=y$ 时，指数恒为零，平均值显然为 $1$。当 $x\neq y$ 时，可选一个满足 $x_k\neq y_k$ 的坐标 $k$；把每个 $s$ 与 $s+e_k$ 配对后，两项符号相反，因而总和为零。

因此所有 $x\neq y$ 的相干块消失，只剩

$$
\boxed{
\mathcal T_A^{\otimes n}(\rho)
=
\sum_x\Pi_x\rho\Pi_x
}.
$$

每个 $\Pi_x$ 都是一维投影，所以

$$
\Pi_x\rho\Pi_x
=
\operatorname{Tr}(\Pi_x\rho)\Pi_x.
$$

定义

$$
p_x=\operatorname{Tr}(\Pi_x\rho),
$$

便得到任意联合输入态都会在 error-pattern basis

$$
\left\{
Z(x)|T\rangle^{\otimes n}
:
x\in\mathbb F_2^n
\right\}
$$

中对角化：

$$
\boxed{
\mathcal T_A^{\otimes n}(\rho)
=
\sum_{x\in\mathbb F_2^n}
p_x
Z(x)|T\rangle\langle T|^{\otimes n}Z(x)
}.
$$

其中

$$
p_x\geq0,
\qquad
\sum_xp_x=1.
$$

#### 9.2 独立模型是额外假设

局域 twirling 消除了不同错误模式 $x$ 之间的量子相干，但一般不会使

$$
p_x
$$

分解成独立概率。

只有额外假设输入为独立同分布

$$
\rho_{\mathrm{in}}
=
\rho_T(p)^{\otimes n},
$$

才有

$$
\begin{aligned}
p_x
&=
\operatorname{Tr}
\left[
\Pi_x\rho_T(p)^{\otimes n}
\right]\\
&=
\prod_{j=1}^n
\operatorname{Tr}
\left[
\Pi_{x_j}\rho_T(p)
\right]\\
&=
\prod_{j:x_j=0}(1-p)
\prod_{j:x_j=1}p\\
&=
p^{|x|}(1-p)^{n-|x|}.
\end{aligned}
$$

因此：

$$
\boxed{
\text{twirling}
\not\Rightarrow
\text{i.i.d. error}
}
$$

一个直接反例是

$$
\rho_{\mathrm{corr}}
=
(1-\epsilon)
|T\rangle\langle T|^{\otimes n}
+
\epsilon
Z(x_*)
|T\rangle\langle T|^{\otimes n}
Z(x_*),
$$

其中 $|x_*|=3$。这个态已经在 error-pattern basis 中对角，因此局域 twirling 后完全不变；但 weight-3 pattern $x_*$ 的概率是

$$
p_{x_*}=\epsilon,
$$

而不是独立模型预言的 $O(\epsilon^3)$。所以“没有相干项”和“高重量错误按单体错误率的高次幂衰减”是两个不同条件。

跨 magic states 的 correlated error、共同漂移和泄漏不会仅靠单比特 twirling 自动消失。

---
### 10. 与 15-to-1 distillation 的关系

[[Reed-Muller码]] 中使用的标准输入模型是

$$
\rho_{\mathrm{in}}
=
\rho_T(p)^{\otimes15},
$$

其中

$$
\rho_T(p)
=
(1-p)|T\rangle\langle T|
+
pZ|T\rangle\langle T|Z.
$$

这个模型包含两层假设：

1. magic-state twirling 把每个输入对角化为随机 $Z$ error；
2. 不同输入错误彼此独立且具有相同错误率 $p$。

第二条不是 twirling 的结论，而是额外噪声模型。

在 i.i.d. 模型中，错误模式 $x\in\mathbb F_2^{15}$ 的概率为

$$
\Pr(x)
=
p^{|x|}(1-p)^{15-|x|}.
$$

对 Reed–Muller 15-to-1 protocol，接受条件是

$$
G_0x^T=0.
$$

这里的 $G_0$ 是一个 $4\times15$ 矩阵，它的 $15$ 个列向量恰好遍历

$$
\mathbb F_2^4\setminus\{0\}.
$$

把第 $j$ 列记为 $h_j$。若错误模式 $x$ 的支撑集为

$$
S=\{j:x_j=1\},
$$

则测得的四比特 syndrome 是

$$
s(x)
=
G_0x^T
=
\sum_{j\in S}h_j,
$$

其中求和是在 $\mathbb F_2^4$ 中进行，即逐位异或。所谓“错误模式不被接受”，不是说该模式不会发生，也不是说协议把它纠正了，而是说

$$
s(x)\neq0,
$$

至少有一个稳定子 check 给出 $-1$，因此这一次 distillation run 在 postselection 中被丢弃。

#### 10.1 为什么 weight $1$ 和 weight $2$ 都不被接受

对 weight-$1$ 错误，设唯一出错位置为 $a$，则

$$
s(x)=h_a\neq0,
$$

因为 $G_0$ 没有零列。因此任意单输入错误都会触发 syndrome。

对 weight-$2$ 错误，设出错位置为不同的 $a,b$，则

$$
s(x)=h_a+h_b.
$$

若它等于零，则在 $\mathbb F_2$ 上必须有 $h_a=h_b$；但 $G_0$ 的 $15$ 列互不相同，所以这是不可能的。因此任意两个不同位置上的错误也都会被拒绝。等价地，

$$
C_X^\perp
=
\ker G_0
$$

是最小非零重量为 $3$ 的 Hamming $[15,11,3]$ 码：零 syndrome 的非平凡错误不可能具有 weight $1$ 或 weight $2$。

#### 10.2 weight-$3$ 的 $35$ 个模式怎么数

设三个出错位置对应互不相同的非零列向量 $h_a,h_b,h_c$。该模式被接受当且仅当

$$
h_a+h_b+h_c=0,
$$

也就是

$$
h_c=h_a+h_b.
$$

任取两个不同的非零向量 $h_a,h_b$：

- 它们的和 $h_a+h_b$ 非零，否则会有 $h_a=h_b$；
- 它们的和也不同于 $h_a$ 和 $h_b$，否则另一个向量会等于零；
- $G_0$ 的列遍历所有非零四比特向量，所以存在唯一位置 $c$ 满足 $h_c=h_a+h_b$。

因此每个无序对 $\{a,b\}$ 都唯一生成一个被接受的三元组

$$
\{h_a,h_b,h_c\}
=
\{h_a,h_b,h_a+h_b\}.
$$

无序对共有

$$
\binom{15}{2}=105
$$

个，但同一个三元组会由其中的三个无序对

$$
\{a,b\},\qquad
\{a,c\},\qquad
\{b,c\}
$$

各生成一次，所以必须除以 $3$：

$$
\boxed{
N_3
=
\frac{\binom{15}{2}}{3}
=
\frac{105}{3}
=35
}.
$$

注意总共有

$$
\binom{15}{3}=455
$$

种 weight-$3$ 错误模式，其中只有这 $35$ 种满足零 syndrome；其余 $420$ 种会被拒绝。

#### 10.3 为什么这 $35$ 个被接受模式都会造成逻辑错误

零 syndrome 只说明错误算符与所有 $X$ checks 对易，即它没有被检测出来；它仍可能是稳定子，也可能是非平凡逻辑算符。对该 Reed–Muller 码，奇重量行是全 $1$ 向量

$$
g_0=(1,\ldots,1),
$$

因此

$$
g_0\cdot x
=
|x|\pmod2.
$$

若 $G_0x^T=0$ 且 $g_0\cdot x=0$，则该 $Z$ 错误属于 $Z$ 型稳定子空间；若

$$
G_0x^T=0,
\qquad
g_0\cdot x=1,
$$

则它位于非平凡逻辑 $Z_L$ 陪集中。weight $3$ 是奇数，所以前面数出的 $35$ 个零-syndrome 模式全部造成输出逻辑错误。

因此，未归一化的错误输出概率从

$$
\begin{aligned}
P_{\mathrm{bad}}
&=
35p^3(1-p)^{12}
+O(p^5)\\
&=
35p^3+O(p^4)
\end{aligned}
$$

开始。这里 $O(p^5)$ 表示下一个被接受且导致逻辑错误的模式重量至少为 $5$；展开 $(1-p)^{12}$ 后仍会产生 $p^4$ 项，所以第二行写成 $O(p^4)$。

与此同时，接受概率包含无错误事件以及被接受的 weight-$3$、weight-$4$ 等事件：

$$
\begin{aligned}
P_{\mathrm{acc}}
&=
(1-p)^{15}
+35p^3(1-p)^{12}
+O(p^4)\\
&=
1-15p+105p^2+O(p^3).
\end{aligned}
$$

这里出现 $105p^2$ 并不表示某些 weight-$2$ 错误被接受；它来自无错误概率 $(1-p)^{15}$ 的二阶展开。所有实际发生的 weight-$1$ 和 weight-$2$ 错误事件仍然都给出非零 syndrome 并被丢弃。

所以条件输出错误率为

$$
\begin{aligned}
p_{\mathrm{out}}
&=
\frac{P_{\mathrm{bad}}}{P_{\mathrm{acc}}}\\
&=
35p^3+O(p^4).
\end{aligned}
$$

这说明 $35p^3$ 同时依赖 twirled 单体错误模型、输入独立性、码的接受条件和 weight-3 错误模式数目，而不是仅由 twirling 本身推出。

如果存在权重小但概率为 $O(p)$ 的 correlated error pattern，三阶抑制可能被破坏。例如某个不可检测的 weight-3 pattern 若以概率 $O(p)$ 出现，就会给输出引入 $O(p)$ 而不是 $O(p^3)$ 的错误。

---
### 11. Twirling 保留什么、丢掉什么

Magic-state twirling 保留：

- $|T\rangle$ fidelity，即 $1-p$；
- 目标 magic axis 上的 Bloch 极化；
- 对角 error-pattern probability。

它丢掉：

- $|T\rangle$ 与 $Z|T\rangle$ 之间的相干相位；
- 单 qubit Bloch 向量中垂直于 magic axis 的分量；
- 多输入情况下不同 error patterns 之间的量子相干。

它不会自动处理：

- 输入之间的经典相关性；
- Clifford gate、measurement 和 decoder error；
- leakage 与超出 qubit Hilbert space 的误差；
- 随机化 Clifford 本身的不完美；
- 时间相关或 gate-dependent noise。

因此，twirled model 是一个明确假设下的有效分析模型，不应被解释为原始物理噪声“本来就是随机 $Z$ error”。

---
### 12. 与其它笔记的连接

- [[State injection]]：说明 twirled magic-state error 如何在 gate injection 后变成数据上的逻辑 $Z$ error。
- [[Reed-Muller码]]：在 i.i.d. 随机 $Z$ 模型下推导 15-to-1 的接受概率和 $35p^3$。
- [[三正交码与横向逻辑T门]]：说明 distillation code 如何利用横向非 Clifford 门与 syndrome postselection。

---
### 参考来源

- S. Bravyi and A. Kitaev, [Universal Quantum Computation with ideal Clifford gates and noisy ancillas](https://arxiv.org/abs/quant-ph/0403025), *Physical Review A* **71**, 022316 (2005).
- C. Dankert, R. Cleve, J. Emerson, and E. Livine, [Exact and Approximate Unitary 2-Designs: Constructions and Applications](https://arxiv.org/abs/quant-ph/0606161), *Physical Review A* **80**, 012304 (2009).
- J. J. Wallman and J. Emerson, [Noise tailoring for scalable quantum computation via randomized compiling](https://arxiv.org/abs/1512.01098), *Physical Review A* **94**, 052325 (2016).
