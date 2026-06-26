给定一个 triorthogonal matrix，可以由它读出一个 magic-state distillation protocol：矩阵的行决定输出与检查自由度，矩阵的列决定需要消耗的非 Clifford resources。本篇关注这两个方向如何在线路、错误检测和资源计数中出现。

本文采用

$$
T=\operatorname{diag}(1,e^{i\pi/4}),
\qquad
|T\rangle=T|+\rangle,
\qquad
\omega=e^{i\pi/4}.
$$

---
### 1. Distillation 要完成什么

给定 $n$ 个有噪声的 $|T\rangle$ states，distillation protocol 希望只使用 Clifford 操作、Pauli 测量和经典前馈，在成功事件上输出 $k$ 个错误率更低的 $|T\rangle$ states：

$$
n\longrightarrow k.
$$

[[State injection]] 说明单个 magic state 如何提供非 Clifford gate；distillation 则把多个 noisy resources 组织成带 postselection 的错误检测过程。需要回答的问题是：哪些检查决定接受、接受后还可能留下什么错误，以及输入数、输出数和线路宽度分别由什么决定。

---
### 2. 基本对象与记号

设

$$
G=
\begin{pmatrix}
G_1\\
G_0
\end{pmatrix}
\in\mathbb F_2^{m\times n},
\qquad
m=k+m_x.
$$

约定：

- $G_1$ 包含 $k$ 条奇重量行，承载 $k$ 个逻辑输出；
- $G_0$ 包含 $m_x$ 条线性独立的偶重量行，对应 $X$ 型检查；
- $G$ 的行记为 $g_a$，列记为 $c_j=G_{*,j}\in\mathbb F_2^m$；
- $n$ 是矩阵列数；
- $m=k+m_x$ 是矩阵行数。

若原始 $G_0$ 含线性相关行，应先删除冗余检查；此时更准确地写

$$
m_x=\operatorname{rank}(G_0),
\qquad
m=\operatorname{rank}(G).
$$

$G$ 为 triorthogonal matrix，指任意两条不同的行和任意三条不同的行都有偶数重叠：

$$
|g_a\wedge g_b|
\equiv0\pmod2
\qquad(a<b),
$$

$$
|g_a\wedge g_b\wedge g_c|
\equiv0\pmod2
\qquad(a<b<c).
$$

---
### 3. 由 $G$ 建立码空间协议

矩阵 $G$ 首先定义一个编码 $k$ 个逻辑 qubits 的 $n$ qubit CSS 错误检测码。

#### CSS stabilizer

矩阵 $G$ 定义一个 CSS 码：

$$
\mathcal S_X
=
\{X(g):g\in\operatorname{rowspan}(G_0)\},
$$

$$
\mathcal S_Z
=
\{Z(h):h\in\operatorname{rowspan}(G)^\perp\}.
$$

这里要求 $G_0$ 的行线性独立，并采用

$$
\operatorname{rank}(G)=k+m_x.
$$

#### 编码逻辑数

在行满秩的约定下，该码把 $n$ 个物理 qubit 编码为 $k$ 个逻辑 qubit。奇重量行给出逻辑 $X$ 的代表元，偶重量行给出 $X$ 型 stabilizer。

编码数可直接由稳定子秩核对：

$$
\begin{aligned}
k_{\mathrm{code}}
&=
n-\operatorname{rank}(\mathcal S_X)
-\operatorname{rank}(\mathcal S_Z)\\
&=
n-m_x-(n-m)\\
&=
m-m_x\\
&=
k.
\end{aligned}
$$

横向相位层是否实现所需逻辑 $T/T^\dagger$，由 triorthogonality 和各行重量模 $8$ 决定。相关相位展开将在紧凑线路中重新出现；一般推导详见 [[三正交码与横向逻辑T门]]。

#### 协议骨架

码空间版本的协议骨架是：

1. 准备编码的 $|+\rangle_L^{\otimes k}$；
2. 用 $n$ 个 noisy $|T\rangle$ resources 实现横向 $T$ 或 $T^\dagger$ 层；
3. 施加由行重量和行重叠决定的已知 Clifford correction；
4. 测量 $G_0$ 对应的 $X$ syndrome；
5. 仅在所有检查结果为 $+1$ 时接受；
6. 解码并输出 $k$ 个 magic states。

具体协议还必须核对横向层实现的是 $T_L$ 还是 $T_L^\dagger$，以及需要哪些 Clifford corrections。15-to-1 的约定和推导见 [[Reed-Muller码]]。

$G_0$ 的偶重量行决定要检查的 $X$ syndrome，$G_1$ 的奇重量行决定保留下来的逻辑自由度。因此矩阵的行划分同时指定了“哪些自由度用于检测”和“哪些自由度作为输出”。

---
### 4. 构造紧凑线路

码空间描述使用 $n$ 个物理位置，但横向相位在码空间中的作用可以只用行系数表示，不必始终显式保存完整码块。

#### 行系数表示

若 $G$ 的 $m$ 行线性独立，则任意行空间码字都可唯一写成

$$
y=xG,
\qquad
x=(x_1,\ldots,x_m)\in\mathbb F_2^m.
$$

按照 [[逻辑基态的表示]] 中的 CSS 陪集态表示，二进制码字 $y$ 对应计算基矢 $|y\rangle$，而逻辑基态是同一 $G_0$ 陪集内计算基矢的相干叠加。

行系数 $x$ 记录生成码字 $y=xG$ 时选择了哪些行。定义

$$
V_G|x\rangle=|xG\rangle.
$$

行满秩保证 $x\mapsto xG$ 一一对应。把行系数写成

$$
x=(u,v),
\qquad
u\in\mathbb F_2^k,
\quad
v\in\mathbb F_2^{m_x},
$$

则所选逻辑计算基可以写为

$$
|u_L\rangle
=
\frac{1}{\sqrt{2^{m_x}}}
\sum_{v\in\mathbb F_2^{m_x}}
|uG_1+vG_0\rangle.
$$

等价地，

$$
\boxed{
V_G\left(
|u\rangle\otimes|+\rangle^{\otimes m_x}
\right)
=
|u_L\rangle
}.
$$

#### 横向相位的逐列分解

对原始码字有

$$
T^{\otimes n}|xG\rangle
=
\omega^{|xG|}|xG\rangle.
$$

通过映射 $V_G$ 拉回到 $m$ qubit 空间，得到有效对角门

$$
U_G
=
V_G^\dagger T^{\otimes n}V_G,
$$

因而

$$
U_G|x\rangle
=
\omega^{|xG|}|x\rangle.
$$

为了分解 $|xG|$，先写出码字

$$
y=xG=(y_1,\ldots,y_n)
$$

并逐个考察分量 $y_j$。

记 $G$ 的第 $j$ 列为

$$
c_j=G_{*,j}\in\mathbb F_2^m.
$$

码字 $xG$ 的第 $j$ 位为

$$
(xG)_j
=
\left[
\sum_{a=1}^m x_aG_{a,j}
\right]_2
=
[c_j\cdot x]_2.
$$

也就是说，第 $j$ 个码坐标上的计算基值 $y_j$，等于寄存器中由列 $c_j$ 选中的变量的 XOR parity。由于单 qubit $T$ 门满足

$$
T|b\rangle=\omega^b|b\rangle,
\qquad
b\in\{0,1\},
$$

原始横向层中的第 $j$ 个 $T$ 门贡献的相位就是

$$
\omega^{(xG)_j}
=
\omega^{[c_j\cdot x]_2}.
$$

因此在寄存器空间中，必须使用一个只在该 parity 为 $1$ 时乘上 $\omega$ 的门。对任意非零列 $c\in\mathbb F_2^m$，定义 parity-phase gate

$$
P(c)|x\rangle
=
\omega^{[c\cdot x]_2}|x\rangle,
\qquad
x\in\mathbb F_2^m,
$$

其中 $[c\cdot x]_2$ 是二进制内积。下文将逐步证明它等价于

$$
P(c)
=
\exp\left[
\frac{i\pi}{8}\bigl(I-Z(c)\bigr)
\right],
$$

$$
Z(c)=Z^{c_1}\otimes\cdots\otimes Z^{c_m}.
$$

所以第 $j$ 个原始横向 $T$ 门在紧凑线路中的等价物就是

$$
T_j
\quad\longleftrightarrow\quad
P(c_j).
$$

把所有列的相位相乘便得到

$$
\prod_{j=1}^n
\omega^{[c_j\cdot x]_2}
=
\omega^{\sum_j(xG)_j}
=
\omega^{|xG|},
$$

这与 $T^{\otimes n}$ 在原始码字上的相位完全相同。因此 $P(c_j)$ 不是额外假设的门，而是把第 $j$ 个码坐标上的 $T$ 门改写到行系数寄存器后必然得到的 parity-phase gate。

若 $c=0$，则

$$
P(0)=I.
$$

这样的零列不消耗非 Clifford resource，通常可以从协议矩阵中删除。

#### Parity-phase gate 的算符形式

设

$$
S(c)=\{a:c_a=1\}
$$

为 $c$ 的支撑。对计算基字符串 $x$，先计算 parity

$$
b_c(x)
=
\bigoplus_{a\in S(c)}x_a
=
[c\cdot x]_2.
$$

于是 $P(c)$ 的计算规则就是

$$
|x\rangle
\longmapsto
\begin{cases}
|x\rangle,&b_c(x)=0,\\
\omega|x\rangle,&b_c(x)=1.
\end{cases}
$$

定义

$$
Z(c)=\bigotimes_{a=1}^m Z^{c_a}.
$$

它在计算基上的本征值正好记录 parity：

$$
Z(c)|x\rangle=(-1)^{b_c(x)}|x\rangle.
$$

因此奇 parity 子空间的投影算符为

$$
\Pi_{\mathrm{odd}}(c)=\frac{I-Z(c)}{2}.
$$

投影算符的一般构造见 [[逻辑基态的表示#投影算符表示]]。只在该子空间施加相位 $\omega=e^{i\pi/4}$，得到

$$
\boxed{
P(c)
=
\exp\left(
\frac{i\pi}{4}\Pi_{\mathrm{odd}}(c)
\right)
=
\exp\left[
\frac{i\pi}{8}\bigl(I-Z(c)\bigr)
\right]
}.
$$

当 $b_c(x)=0$ 时指数为 $0$；当 $b_c(x)=1$ 时指数为 $i\pi/4$。因此该式与

$$
P(c)|x\rangle=\omega^{b_c(x)}|x\rangle
$$

严格相等。

由于 $I$ 与 $Z(c)$ 对易，也可以把恒等项从指数中提出：

$$
\begin{aligned}
P(c)
&=
\exp\left[
\frac{i\pi}{8}I-\frac{i\pi}{8}Z(c)
\right]\\
&=
e^{i\pi/8}
\exp\left[-\frac{i\pi}{8}Z(c)\right].
\end{aligned}
$$

其中 $e^{i\pi/8}$ 是作用在整个 Hilbert 空间上的全局相位。若只关心普通线路中的物理作用，可以把 $P(c)$ 视为多体 Pauli rotation $\exp[-i\pi Z(c)/8]$，二者只差全局相位；若要保持与上面的 parity-phase 定义严格相等，或者讨论受控的 $P(c)$，则应保留这个全局相位。

#### 用 Clifford+$T$ 实现 $P(c)$

$P(c)$ 除了一个全局相位外，是绕多 qubit Pauli string $Z(c)$ 的旋转，而标准 Clifford+$T$ 门集直接提供的是绕单 qubit $Z_t$ 的 $T_t$。因此需要先用 Clifford network 把多 qubit parity $b_c(x)$ 写到一个 accumulator qubit 上，再施加 $T_t$，最后反计算。CNOT 只改变 $T$ 门所依赖的 parity，不提供 magic；非 Clifford resource 仍只有中间的一个 $T$ gate。

##### 为什么不能把 $P(c)$ 直接拆成多个单 qubit $T$ 门

若直接在每个 $a\in S(c)$ 上施加 $T_a$，得到

$$
\left(\prod_{a\in S(c)}T_a\right)|x\rangle
=
\omega^{\sum_{a\in S(c)}x_a}|x\rangle.
$$

这里指数是普通整数和

$$
\sum_{a\in S(c)}x_a.
$$

但 $P(c)$ 要求的指数是 XOR parity

$$
b_c(x)
=
\bigoplus_{a\in S(c)}x_a
=
\left[\sum_{a\in S(c)}x_a\right]_2.
$$

普通和与 XOR 只有在至多一个被选 bit 为 $1$ 时相同；当多个 bits 同时为 $1$ 时，两者不同。

最简单的反例是

$$
c=(1,1).
$$

此时

$$
P(1,1)|x_1x_2\rangle
=
\omega^{x_1\oplus x_2}|x_1x_2\rangle,
$$

所以

$$
P(1,1)
=
\operatorname{diag}(1,\omega,\omega,1).
$$

而两个单 qubit $T$ 门给出

$$
(T\otimes T)|x_1x_2\rangle
=
\omega^{x_1+x_2}|x_1x_2\rangle,
$$

即

$$
T\otimes T
=
\operatorname{diag}(1,\omega,\omega,\omega^2).
$$

在 $|11\rangle$ 分支上：

$$
P(1,1)|11\rangle
=
|11\rangle,
$$

因为

$$
1\oplus1=0,
$$

但

$$
(T\otimes T)|11\rangle
=
\omega^2|11\rangle
=
i|11\rangle.
$$

因此

$$
\boxed{
P(1,1)\neq T\otimes T
}.
$$

差异来自 XOR 与普通整数和不同。把 XOR 写成整数多项式时会出现二次及更高次相位项；多个独立 $T_a$ 只产生一次项，无法补上这些多体相位。相关重量展开详见 [[三正交码与横向逻辑T门]]。

CNOT–$T$–CNOT 方法没有把 $P(c)$ 近似成多个局域旋转，而是先把整个 XOR parity 编码到一个 qubit 上，再只施加一次 $T$。因此它精确实现

$$
\omega^{\oplus_a x_a}
$$

而不是

$$
\omega^{\sum_a x_a}.
$$

任选一个 $t\in S(c)$ 作为 parity accumulator，定义

$$
C_c
=
\prod_{a\in S(c)\setminus\{t\}}
\operatorname{CNOT}_{a\rightarrow t}.
$$

$C_c$ 把目标位变为

$$
x_t
\longmapsto
\bigoplus_{a\in S(c)}x_a
=
b_c(x),
$$

其余计算基变量不变。于是

$$
\boxed{
P(c)=C_c^\dagger T_tC_c
}.
$$

对控制位 $a$、目标位 $t$，

$$
\operatorname{CNOT}_{a\rightarrow t}^\dagger
Z_t
\operatorname{CNOT}_{a\rightarrow t}
=
Z_aZ_t.
$$

依次共轭全部 CNOT 后，

$$
C_c^\dagger Z_tC_c
=
\prod_{a\in S(c)}Z_a
=
Z(c).
$$

所以 Clifford conjugation 把旋转轴 $Z_t$ 变为 $Z(c)$，并给出

$$
C_c^\dagger T_tC_c
=
\exp\left[
\frac{i\pi}{8}\bigl(I-Z(c)\bigr)
\right]
=
P(c).
$$

如果硬件或 fault-tolerant architecture 能原生执行多体 Pauli rotation

$$
\exp\left(-\frac{i\pi}{8}Z(c)\right)
$$

或直接测量相应 Pauli product，则不一定要实际使用这串 CNOT。此时实现的是与 $P(c)$ 相差全局相位 $e^{-i\pi/8}$ 的门；在普通非受控线路中这不改变输出态。CNOT–$T$–CNOT 是把 $P(c)$ 编译到标准 Clifford+$T$ 门集的一种通用实现，不是 $P(c)$ 定义本身的一部分。

特别地，若 $c$ 的重量为 $1$，例如 $c=e_t$，则

$$
Z(c)=Z_t,
\qquad
C_c=I,
\qquad
P(c)=T_t.
$$

此时 parity 已经存放在单个 qubit 上，不需要任何 CNOT。只有当 $|c|>1$、所需相位依赖多个 qubits 的 XOR 时，才需要 parity network 或其它等价的多体 Pauli-rotation primitive。

若逻辑 $T_t$ 通过 [[State injection]] 实现，则每个非零 $P(c)$ 消耗一个 noisy $|T\rangle$ state。若该注入发生等效 $Z_t$ 错误，反计算后有

$$
C_c^\dagger Z_tC_c=Z(c),
$$

这也解释了下一节中为什么第 $j$ 个输入错误在寄存器上变成 $Z(c_j)$。

#### 合并所有列

对 $G$ 的全部列定义

$$
U_G
=
\prod_{j=1}^{n}P(c_j).
$$

所有 $P(c_j)$ 都是对角门，因而彼此对易。对任意计算基态 $|x\rangle$，

$$
U_G|x\rangle
=
\omega^{|xG|}|x\rangle,
$$

其中 $xG\in\mathbb F_2^n$，$|xG|$ 是其 Hamming weight。

将 $|xG|$ 按行重叠展开并模 $8$ 化简后，triorthogonality 保证额外的非 Clifford 二次、三次相位消失，只留下奇重量行上的 $T$ 型相位以及可校正的 Clifford phase。完整重量展开和各项来源见 [[三正交码与横向逻辑T门]]。

因此存在一个可由 $S$、$Z$ 和 $CZ$ 组成的已知对角 Clifford $C_G$，使得

$$
C_GU_G|+\rangle^{\otimes m}
=
|T\rangle^{\otimes k}
\otimes
|+\rangle^{\otimes m_x},
$$

其中 qubit 顺序按 $G_1$、$G_0$ 的行顺序排列。

#### 寄存器 qubit 与线路宽度

在上述推导中，$m=k+m_x$ 个 qubits 保存的是行系数

$$
x=(x_{\mathrm{out}},x_{\mathrm{check}}),
$$

而不是完整的 $n$ 位码字 $y=xG$。本文把这些持续保存量子信息的工作 qubits 称为“寄存器 qubits”。其中前 $k$ 个对应 $G_1$ 的奇重量行，最终保留为输出；后 $m_x$ 个对应 $G_0$ 的偶重量行，最终在 $X$ 基测量。

“第 $j$ 个码坐标”只是码字分量 $y_j$，也就是原始 $n$ qubit 码块中的第 $j$ 个物理位置。矩阵第 $j$ 列 $c_j$ 告诉我们，该位置的值是哪些行系数的 XOR：

$$
y_j=[c_j\cdot x]_2.
$$

因此原始第 $j$ 个物理 $T_j$ 门在寄存器空间中变成 $P(c_j)$。CNOT network 不产生 magic；它只是把多 qubit parity 临时集中到一个 qubit，使单 qubit $T$ 能按该 parity 添加相位，然后再恢复原来的计算基标签。

这个改写把需要持续保存的协议宽度从 $n$ 个码坐标变为

$$
m=k+m_x
$$

个行自由度，但没有减少 magic-state input count：一次尝试仍要执行 $n$ 个 $P(c_j)$，因此仍消耗 $n$ 个 noisy $|T\rangle$ states。

紧凑 distillation circuit 可写为：

1. 准备 $m=k+m_x$ 个 $|+\rangle$；
2. 按 $G$ 的 $n$ 列执行 $P(c_j)$，共消耗 $n$ 个 noisy $|T\rangle$ states；
3. 施加 $C_G$；
4. 对后 $m_x$ 个检查 qubit 各施加 $H$，再做计算基测量，即完成 $X$ 基测量；
5. 仅在 $X$ 本征值全为 $+1$，等价地计算基读数全为 $0$ 时接受；
6. 保留前 $k$ 个输出 qubit。

#### 检查 qubit 的 $X$ 基测量

对第 $a$ 个检查 qubit，$X$ 基测量可用

$$
\text{先施加 }H
\quad\longrightarrow\quad
\text{再做计算基测量}
$$

实现，因为

$$
H|+\rangle=|0\rangle,
\qquad
H|-\rangle=|1\rangle.
$$

若计算基测量结果记为 $r_a\in\{0,1\}$，对应的 $X$ 本征值就是

$$
\lambda_a=(-1)^{r_a}.
$$

因此：

- $r_a=0$ 等价于测得 $X=+1$；
- $r_a=1$ 等价于测得 $X=-1$。

把 $m_x$ 个结果排成

$$
r=(r_1,\ldots,r_{m_x})\in\mathbb F_2^{m_x},
$$

协议只在

$$
r=0
$$

时接受。

无错误时，施加 $C_G$ 后检查寄存器为

$$
|+\rangle^{\otimes m_x},
$$

所以所有测量结果都是 $r_a=0$。若检查寄存器上存在

$$
Z(s)
=
Z^{s_1}\otimes\cdots\otimes Z^{s_{m_x}},
$$

则第 $a$ 个 qubit 变为

$$
Z^{s_a}|+\rangle
=
\begin{cases}
|+\rangle,&s_a=0,\\
|-\rangle,&s_a=1.
\end{cases}
$$

经过 $H$ 后分别成为 $|0\rangle$ 和 $|1\rangle$，所以在理想测量模型中

$$
\boxed{r=s}.
$$

下一节将得到

$$
s=G_0e^T,
$$

因此这组 $X$ 基测量直接读出 distillation syndrome。

上述描述假设 $C_G$ 已经实际施加。若只在 Clifford frame 中跟踪 $C_G$，则不必物理执行它，但测量算符必须相应改为

$$
C_G^\dagger X_a C_G.
$$

在 fault-tolerant architecture 中，也可以直接执行逻辑 $X$ 测量，例如读取逻辑 patch 的 $X$ 基结果并结合 decoder 判定；$H$ 后测 $Z$ 是抽象线路层的等价实现。

这里的压缩来自编码、横向相位层和解码的代数化简，不是简单删除 CSS 码中的 $Z$-check。Triorthogonality 保证该相位网络经过已知 Clifford correction 后，前 $k$ 个 qubits 具有所需的 $T$ 型相位，后 $m_x$ 个 qubits 可作为检查自由度。

---
### 5. 错误如何进入 syndrome 和输出

给定一组有错误的输入 magic states，需要分别判断错误是否触发检查，以及通过检查后是否仍会破坏输出。

#### 有效错误模型

经过适合 $|T\rangle$ 的 dephasing/twirling 后，单个输入可写为

$$
\rho_T(p)
=
(1-p)|T\rangle\langle T|
+pZ|T\rangle\langle T|Z.
$$

这一步及其适用条件详见 [[Clifford Twirling 与魔态错误模型]]。现在额外假设：

- 各输入错误独立；
- Clifford gate、$X$ 测量和 classical feedforward 理想；
- 已知的 Pauli/Clifford byproduct 已吸收到 frame；
- 不考虑 coherent error、leakage 和 correlated fault。

用

$$
e=(e_1,\ldots,e_n)\in\mathbb F_2^n
$$

表示 $n$ 个注入资源上的等效 $Z$ 错误，其中 $e_j=1$ 表示第 $j$ 个 parity-phase gadget 有错。

#### 错误在紧凑线路中的传播

在标准 parity-compute–$T$–uncompute 实现中，第 $j$ 个错误映射到紧凑寄存器上为 $Z(c_j)$。因此总错误为

$$
\prod_{j:e_j=1}Z(c_j)
=
Z\left(\bigoplus_{j=1}^n e_jc_j\right)
=
Z(Ge^T).
$$

按奇、偶行分块，

$$
Ge^T
=
\begin{pmatrix}
G_1e^T\\
G_0e^T
\end{pmatrix}
=
\begin{pmatrix}
\ell\\
s
\end{pmatrix}.
$$

这里：

$$
\boxed{s=G_0e^T}
$$

是 $m_x$ 位 syndrome。因为检查 qubit 最终在 $X$ 基测量，而 $Z$ 会翻转 $X$ 测量结果，所以协议接受当且仅当

$$
\boxed{G_0e^T=0}.
$$

接受后，前 $k$ 个输出 qubit 上的逻辑 $Z$ 错误为

$$
\boxed{\ell=G_1e^T}.
$$

因此一个错误模式会被“无害地接受”当且仅当

$$
G_0e^T=0,
\qquad
G_1e^T=0,
$$

而“未被检测且破坏输出”当且仅当

$$
G_0e^T=0,
\qquad
G_1e^T\neq0.
$$

#### 接受条件与输出错误

$G_0e^T$ 记录错误在检查自由度上的投影。只要它非零，至少一个 $X$ 基检查结果会翻转，协议便拒绝。$G_1e^T$ 记录同一错误在输出自由度上的投影；在 syndrome 为零时，它决定接受的输出是否损坏。

这个分块关系把“错误是否被检测”和“错误是否破坏输出”分成了两个不同问题。一个错误可以被检测并拒绝，也可以通过所有检查后成为逻辑输出错误。

这里只使用 $X$ syndrome，是因为有效输入错误已经化为 $Z$ error；$Z$ 型 stabilizer 与这些错误对易，不能用于筛选。但 $Z$ stabilizer 仍参与 CSS 码的定义，底层 fault-tolerant implementation 也仍需完整纠错。相关噪声模型与这一简化的边界见 [[Clifford Twirling 与魔态错误模型]]。

---
### 6. 计算接受概率与输出错误率

有了 $G_0e^T$ 和 $G_1e^T$，接受概率与输出错误率都可以写成对错误模式的求和。

#### 错误模式的概率

若第 $j$ 个输入错误率为 $p_j$，定义错误模式的概率

$$
w(e)
=
\prod_{j=1}^{n}
p_j^{e_j}(1-p_j)^{1-e_j}.
$$

这里允许各输入错误率不同，但仍假设错误彼此独立。若输入存在相关性，应把 $w(e)$ 替换为完整联合分布。

#### 接受后的输出分布

接受概率为

$$
\boxed{
P_{\mathrm{acc}}
=
\sum_{\substack{e\in\mathbb F_2^n\\G_0e^T=0}}
w(e)
}.
$$

给定接受事件，输出逻辑错误向量 $\ell$ 的条件分布为

$$
\boxed{
\Pr(\ell\mid\mathrm{acc})
=
\frac{
\displaystyle
\sum_{\substack{
e\in\mathbb F_2^n\\
G_0e^T=0,\;G_1e^T=\ell
}}
w(e)
}{
P_{\mathrm{acc}}
}
}.
$$

对 $k>1$ 的协议，必须区分：

$$
p_{\mathrm{out}}^{\mathrm{block}}
=
1-\Pr(\ell=0\mid\mathrm{acc}),
$$

和第 $i$ 个输出的边缘错误率

$$
p_{\mathrm{out},i}
=
\sum_{\ell:\ell_i=1}
\Pr(\ell\mid\mathrm{acc}).
$$

多个输出错误一般可能相关，不能仅用一个单 qubit 错误率描述整个输出块。

#### 低错误率行为

对独立同分布错误 $p_j=p$，协议检测距离定义为

$$
\boxed{
d
=
\min_{\substack{
e\in\mathbb F_2^n\\
G_0e^T=0,\;G_1e^T\neq0
}}
|e|
}.
$$

若重量为 $d$ 的坏错误模式共有 $A_d$ 个，则低错误率下

$$
\boxed{
p_{\mathrm{out}}^{\mathrm{block}}
=
A_dp^d+O(p^{d+1})
}.
$$

$d$ 决定 leading order，$A_d$ 决定 leading coefficient。只知道“码距为 $d$”不足以推出具体常数。

对于 $k=1$，block error 与单输出错误率相同；对于 $k>1$，输出之间可能相关，因此需要同时报告 block error、各输出边缘错误率，必要时还要报告联合错误分布。

---
### 7. 输入消耗、yield 与线路宽度

资源估算中至少要区分每次尝试消耗的 magic states、平均成功产出和需要同时保存的工作 qubits。

一次尝试使用 $n$ 个 noisy magic states；若 syndrome 检查通过，则输出 $k$ 个 states。紧凑相位线路长期保存 $k+m_x$ 个工作 qubits。

#### 输入消耗与 yield

每次尝试的 magic-state 输入数为

$$
N_{\mathrm{in}}=n.
$$

接受时输出 $k$ 个状态，因此平均 yield 为

$$
\boxed{
Y=\frac{kP_{\mathrm{acc}}}{n}
}.
$$

平均每个成功输出消耗的 noisy 输入数为

$$
\boxed{
\frac{n}{kP_{\mathrm{acc}}}
}.
$$

#### 寄存器宽度与线路深度

紧凑相位线路的寄存器宽度为

$$
\boxed{
N_{\mathrm{reg}}=k+m_x
}.
$$

但这不等于完整硬件的峰值 qubit 数。若每个 $P(c_j)$ 通过 magic-state injection 实现，还需要注入 ancilla、测量 ancilla，以及底层纠错码的 syndrome qubits。更准确地说，

$$
N_{\mathrm{peak}}
\geq
N_{\mathrm{reg}},
$$

具体差值由 injection gadget、并行度和 fault-tolerant architecture 决定。

若把 $n$ 个 parity-phase gadgets 完全串行执行，可构造一个

$$
D_T=n
$$

的调度；但这只是串行上界，不是协议固有深度。由于这些 gates 对易，实际 T-depth 和总 Clifford depth 取决于：

- 哪些 gadgets 可以并行；
- parity 的计算与反计算网络；
- qubit connectivity 和 routing；
- 可用 ancilla 数；
- 是否采用 lattice surgery 或多体 Pauli measurement。

因此不应笼统写成“线路深度 $=n$”。

#### 各资源量的区别

这些资源量不能混用：

| 数量 | 公式 | 含义 |
|---|---:|---|
| 每次尝试的 noisy 输入数 | $N_{\mathrm{in}}=n$ | $G$ 的列数，即 parity-phase gadgets 数 |
| 接受时的输出数 | $k$ | $G_1$ 的行数 |
| 平均 yield | $Y=kP_{\mathrm{acc}}/n$ | 每个输入平均产生的成功输出数 |
| 紧凑线路寄存器宽度 | $N_{\mathrm{reg}}=k+m_x$ | 需要持续保存的输出和检查 qubits |
| 完整硬件峰值 qubit 数 | $N_{\mathrm{peak}}\geq N_{\mathrm{reg}}$ | 还包含 injection、测量和底层纠错 ancillas |
| 串行 T-depth 上界 | $D_T\leq n$ | 完全串行时取 $n$，并行调度可能更小 |

矩阵的列数控制每次尝试需要多少个 non-Clifford resources，矩阵的行数控制紧凑线路要同时保存多少个输出和检查自由度。这两个数量来自矩阵的不同方向，不能相互替代。

---
### 8. 15-to-1 Reed–Muller 特例

15-to-1 协议对应一个 $5\times15$ 的 triorthogonal matrix，因此

$$
k=1,
\qquad
m_x=4,
\qquad
n=15.
$$

由一般公式立即得到 $15\to1$、紧凑寄存器宽度 $k+m_x=5$ 和三阶错误抑制。具体矩阵、$35p^3$ 的计数、精确接受概率、阈值和横向 $T/T^\dagger$ 方向均见 [[Reed-Muller码]]，不在此重复。

---
### 9. 适用范围与失效模式

上面的

$$
G_0e^T=0,
\qquad
G_1e^T=\ell
$$

以及 $p_{\mathrm{out}}=O(p^d)$ 依赖以下条件：

- 输入 magic-state error 已被随机化为 stochastic $Z$ error；
- 输入错误独立，或至少已知完整联合分布 $w(e)$；
- Clifford correction、parity network 和 $X$ measurement 理想；
- 不存在 leakage、coherent accumulation 和跨 gadget correlated fault；
- $G$ 的行划分、$T/T^\dagger$ 方向和 Clifford frame 一致。

失效方式包括：

- correlated error 使重量为 $d$ 的事件不再按 $p^d$ 缩放；
- coherent error 在 postselection 后可能保留相干项；
- parity network fault 可同时制造数据错误和错误 syndrome；
- 测量错误可把应拒绝事件误判为接受；
- 多输出协议中，边缘错误率很低但 block error 或输出间相关性仍可能显著。

因此这里的 $p_{\mathrm{out}}$ 是 distillation code 对输入 magic-state error 的抑制，不是完整 surface-code factory 的总逻辑失败率。

---
### 与其它笔记的连接

- [[Clifford Twirling 与魔态错误模型]]：说明何时可以把 noisy $|T\rangle$ 化为随机 $Z$ 错误模型。
- [[三正交码与横向逻辑T门]]：推导 triorthogonality 如何消除额外的非 Clifford 二次、三次相位。
- [[Reed-Muller码]]：给出 15-to-1 的矩阵、码距、weight enumerator、接受概率和精确输出错误率。
- [[State injection]]：说明每个 parity-phase gadget 如何消耗一个 noisy magic state 实现非 Clifford rotation。

---
### 参考来源

- S. Bravyi and J. Haah, [Magic state distillation with low overhead](https://arxiv.org/abs/1209.2426), *Physical Review A* **86**, 052329 (2012).
- E. T. Campbell and M. Howard, [A unified framework for magic state distillation and multi-qubit gate-synthesis with reduced resource cost](https://arxiv.org/abs/1606.01904), *Physical Review A* **95**, 022316 (2017).
