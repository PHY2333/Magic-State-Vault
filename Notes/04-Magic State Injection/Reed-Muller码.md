量子 Reed–Muller $[\![15,1,3]\!]$ 码的重要性不只是“它能纠正一个错误”，而是它把三件事连接起来：经典一次 Boolean 函数、具有横向非 Clifford 门的 CSS 码，以及 Bravyi–Kitaev 15-to-1 magic-state distillation。

本文采用

$$
T=\operatorname{diag}(1,e^{i\pi/4}),
\qquad
\omega=e^{i\pi/4},
$$

并明确区分经典码、量子 CSS 码和 distillation 的有效错误模型。

---
### 1. 从一次 Boolean 函数得到 $RM(1,4)$

定义四变量仿射一次 Boolean 函数

$$
f(x)
=
a_0+a_1x_1+a_2x_2+a_3x_3+a_4x_4,
\qquad
a_i,x_i\in\mathbb F_2.
$$

把 $f$ 在全部 $2^4=16$ 个输入点上的取值排成二进制向量。所有这类向量构成一阶 Reed–Muller 码

$$
RM(1,4)=[16,5,8].
$$

参数的来源是：

- 码长为 $16$，因为定义域有 $16$ 个点；
- 维数为 $5$，对应常数项和四个一次项；
- 非常数仿射函数恰好在一半输入上取 $1$，重量为 $8$；常数函数 $1$ 的重量为 $16$，所以最小距离为 $8$。

为了得到长度 $15$ 的矩阵，删去输入点 $x=0000$ 对应的坐标，即对 $RM(1,4)$ 做 puncture。剩余坐标可按

$$
1111,1110,1101,1100,\ldots,0001
$$

排列。函数 $1,x_1,x_2,x_3,x_4$ 的取值给出

$$
G=
\begin{pmatrix}
1&1&1&1&1&1&1&1&1&1&1&1&1&1&1\\
1&1&1&1&1&1&1&1&0&0&0&0&0&0&0\\
1&1&1&1&0&0&0&0&1&1&1&1&0&0&0\\
1&1&0&0&1&1&0&0&1&1&0&0&1&1&0\\
1&0&1&0&1&0&1&0&1&0&1&0&1&0&1
\end{pmatrix}
=
\begin{pmatrix}
g_0\\
g_1\\
g_2\\
g_3\\
g_4
\end{pmatrix}.
$$

其中

$$
|g_0|=15,
\qquad
|g_i|=8
\quad (1\leq i\leq4).
$$

矩阵 $G$ 的行空间是 punctured $RM(1,4)$，参数为 $[15,5,7]$。量子码并不是简单地“把这个经典码量子化”，而是要从奇、偶重量行构造一对满足对易条件的 CSS 稳定子空间。

---
### 2. CSS 码构造

记偶重量行组成的矩阵为

$$
G_0=
\begin{pmatrix}
g_1\\
g_2\\
g_3\\
g_4
\end{pmatrix},
$$

并定义

$$
C_X=\operatorname{rowspan}(G_0),
\qquad
C_Z=\operatorname{rowspan}(G)^\perp.
$$

本文的约定是：

- $X(c)$，$c\in C_X$，生成 $X$ 型稳定子；
- $Z(z)$，$z\in C_Z$，生成 $Z$ 型稳定子。

记这组稳定子的共同 $+1$ 特征空间为编码空间 $\mathcal Q$。

因为

$$
C_Z^\perp=\operatorname{rowspan}(G)
$$

且

$$
C_X\subseteq\operatorname{rowspan}(G)=C_Z^\perp,
$$

所以任意 $X(c)$ 与 $Z(z)$ 对易。

各空间维数为

$$
\dim C_X=4,
\qquad
\dim C_Z=15-\operatorname{rank}(G)=10.
$$

因此编码逻辑比特数为

$$
k
=
n-\dim C_X-\dim C_Z
=15-4-10
=1.
$$

奇重量行 $g_0$ 满足

$$
g_0\in C_Z^\perp,
\qquad
g_0\notin C_X,
$$

所以可以选取逻辑 $X$ 为

$$
X_L=X(g_0)=X^{\otimes15}.
$$

对应的逻辑计算基可写成

$$
|0_L\rangle
=
\frac{1}{\sqrt{|C_X|}}
\sum_{c\in C_X}|c\rangle
=
\frac{1}{4}\sum_{c\in C_X}|c\rangle,
$$

$$
|1_L\rangle
=X_L|0_L\rangle
=
\frac{1}{4}\sum_{c\in C_X}|g_0+c\rangle.
$$

这里的加法均在 $\mathbb F_2^{15}$ 中进行。

---
### 3. 为什么码距是 $d=3$

对 CSS 码分别定义

$$
d_X
=
\min_{u\in C_Z^\perp\setminus C_X}|u|,
\qquad
d_Z
=
\min_{v\in C_X^\perp\setminus C_Z}|v|.
$$

总码距为

$$
d=\min(d_X,d_Z).
$$

#### 3.1 逻辑 $X$ 距离

因为只编码一个逻辑比特，

$$
C_Z^\perp\setminus C_X=g_0+C_X.
$$

$C_X$ 中的非零向量是非零线性函数在 $15$ 个非零点上的取值，因此重量均为 $8$。于是

$$
|g_0+c|
=
\begin{cases}
15,&c=0,\\
7,&c\neq0.
\end{cases}
$$

所以

$$
d_X=7.
$$

#### 3.2 逻辑 $Z$ 距离

$G_0$ 的 $15$ 个列向量恰好是 $\mathbb F_2^4$ 中所有非零向量。若 $v$ 对应一个 $Z(v)$，则

$$
v\in C_X^\perp
\iff
G_0v^T=0.
$$

- 重量 $1$ 的 $v$ 会选中一个非零列，不可能使列和为零；
- 重量 $2$ 的 $v$ 要求两个不同列相同，也不可能；
- 重量 $3$ 时可以选取满足 $a+b+c=0$ 的三个非零列。

例如按上述列顺序，

$$
\operatorname{col}_4(G_0)
+
\operatorname{col}_8(G_0)
+
\operatorname{col}_{12}(G_0)
=1100+1000+0100
=0000.
$$

因此

$$
v=e_4+e_8+e_{12}
\in C_X^\perp.
$$

同时 $g_0$ 是全 $1$ 向量，所以

$$
g_0\cdot v
=|v|
=3
\equiv1\pmod2.
$$

这说明 $v\notin C_Z=G^\perp$，故

$$
Z_L\sim Z_4Z_8Z_{12}
$$

是一个重量为 $3$ 的非平凡逻辑 $Z$。所以

$$
d_Z=3.
$$

最终

$$
\boxed{
d_X=7,\qquad d_Z=3,\qquad d=3
}
$$

即得到量子 Reed–Muller 码

$$
\boxed{[\![15,1,3]\!]}.
$$

这个码对 $X$ 型和 $Z$ 型逻辑算符是非对称的。写成 $[\![15,1,3]\!]$ 只记录了两者中的较小值。

---
### 4. Triorthogonal 性质

矩阵 $G$ 是 triorthogonal matrix：任意两行和任意三条不同的行，其共同支撑的大小都是偶数。即

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

对当前矩阵：

$$
|g_0\wedge g_i|=8,
\qquad
|g_i\wedge g_j|=4
\quad(i\neq j,\ i,j\geq1),
$$

而三重交叠为 $4$ 或 $2$，因此均为偶数。

这里必须强调“不同的行”。奇重量行 $g_0$ 与自身的重叠当然是奇数，不属于 triorthogonal 定义中的成对条件。

Triorthogonality 控制横向 $T$ 层产生的相位，使非 Clifford 相位只保留在奇重量逻辑行对应的自由度上。一般推导详见 [[三正交码与横向逻辑T门]]。

---
### 5. 横向 T 门的方向

仅说“该码支持横向 $T$”会隐藏一个容易出错的约定问题。按本文的

$$
T=\operatorname{diag}(1,\omega)
$$

以及上面选取的 $|0_L\rangle,|1_L\rangle$，实际有

$$
T^{\otimes15}=T_L^\dagger
\quad\text{on the code space}.
$$

证明直接来自计算基重量。

对任意 $c\in C_X$，

$$
|c|=
\begin{cases}
0,&c=0,\\
8,&c\neq0,
\end{cases}
$$

所以

$$
\omega^{|c|}=1
$$

并且

$$
T^{\otimes15}|0_L\rangle=|0_L\rangle.
$$

另一方面，

$$
|g_0+c|=
\begin{cases}
15,&c=0,\\
7,&c\neq0,
\end{cases}
$$

而

$$
15\equiv7\equiv-1\pmod8.
$$

因此

$$
T^{\otimes15}|1_L\rangle
=
\omega^{-1}|1_L\rangle,
$$

即

$$
T^{\otimes15}
\big|_{\mathcal Q}
=
\operatorname{diag}(1,\omega^{-1})
=T_L^\dagger.
$$

等价地，

$$
\boxed{
(T^\dagger)^{\otimes15}=T_L
}
$$

对这组逻辑基成立。不同文献可能交换 $T$ 与 $T^\dagger$、改变逻辑基标号，或把相差的 Clifford 修正吸收到协议中；比较线路时必须同时核对这些约定。

---
### 6. 15-to-1 distillation 的有效错误模型

考虑经过 twirling 后的独立输入态

$$
\rho(p)
=
(1-p)|T\rangle\langle T|
+
pZ|T\rangle\langle T|Z.
$$

假设：

- $15$ 个输入错误独立同分布；
- Clifford 编码、解码和测量均理想；
- 只考虑等效 $Z$ 错误，不考虑 coherent error、leakage 和 correlated error。

用

$$
x=(x_1,\ldots,x_{15})\in\mathbb F_2^{15}
$$

记录输入 magic state 上的等效 $Z$ 错误，其中 $x_j=1$ 表示第 $j$ 个输入有错。相应误差算符为 $Z(x)$。

15-to-1 电路可以编译成 Clifford 操作、15 个 noisy magic-state resource 和码 syndrome postselection。其错误检测条件是四个偶重量行对应的 $X$ checks 均为 $+1$：

$$
G_0x^T=0.
$$

因此接受当且仅当

$$
x\in C_X^\perp.
$$

若进一步有

$$
g_0\cdot x=0,
$$

则 $x\in G^\perp=C_Z$，接受后的错误是稳定子；若

$$
g_0\cdot x=1,
$$

则接受后的错误属于非平凡逻辑 $Z$ 陪集。由于 $g_0$ 是全 $1$ 行，

$$
g_0\cdot x=|x|\pmod2.
$$

所以在这个约定中，接受的奇重量错误导致输出逻辑错误。

---
### 7. 接受概率和输出错误率

$C_X^\perp$ 是长度 $15$ 的 Hamming $[15,11,3]$ 码，其 weight enumerator 为

$$
\begin{aligned}
W_{C_X^\perp}(z)
={}&1+35z^3+105z^4+168z^5+280z^6+435z^7\\
&+435z^8+280z^9+168z^{10}+105z^{11}
+35z^{12}+z^{15}.
\end{aligned}
$$

令

$$
q=1-p,
\qquad
r=1-2p.
$$

把重量为 $w$ 的码字数乘以 $p^wq^{15-w}$，得到接受概率

$$
\boxed{
P_{\mathrm{acc}}
=
\frac{1+15r^8}{16}
}.
$$

未归一化的输出逻辑错误概率由奇重量项组成：

$$
\begin{aligned}
P_{\mathrm{bad}}
={}&
35p^3q^{12}
+168p^5q^{10}
+435p^7q^8\\
&+280p^9q^6
+105p^{11}q^4
+p^{15}.
\end{aligned}
$$

等价的紧凑形式为

$$
\boxed{
P_{\mathrm{bad}}
=
\frac{1-15r^7+15r^8-r^{15}}{32}
}.
$$

因此，在协议被接受的条件下，

$$
\boxed{
p_{\mathrm{out}}
=
\frac{P_{\mathrm{bad}}}{P_{\mathrm{acc}}}
=
\frac{
1-15(1-2p)^7
+15(1-2p)^8
-(1-2p)^{15}
}{
2\left[1+15(1-2p)^8\right]
}
}.
$$

低错误率展开为

$$
\boxed{
p_{\mathrm{out}}
=35p^3+O(p^4)
}.
$$

系数 $35$ 不是仅由“码距为 $3$”推出的；它来自 $C_X^\perp$ 中恰好有 $35$ 个重量为 $3$ 的码字。码距解释了为什么没有一阶和二阶接受错误，而 weight enumerator 决定具体常数。

在同一理想独立噪声模型下，非零 distillation fixed point 满足

$$
p_{\mathrm{out}}(p_*)=p_*,
$$

数值为

$$
p_*\approx0.14148.
$$

只有当 $p<p_*$ 时，递归使用该协议才会降低错误率。

一次尝试消耗 $15$ 个输入并在接受时输出 $1$ 个状态，因此平均 yield 为

$$
Y=\frac{P_{\mathrm{acc}}}{15},
$$

平均每个成功输出消耗的输入数为

$$
\frac{15}{P_{\mathrm{acc}}}.
$$

这些数量没有计入 Clifford synthesis、ancilla、重复 syndrome measurement、routing、idle error、decoder failure 和 factory warm-up。

---
### 8. 协议骨架与适用范围

在有效逻辑层，15-to-1 协议可概括为：

1. 输入 $15$ 个错误率为 $p$ 的 noisy $|T\rangle$ states；
2. 通过 gate teleportation 将这些资源用于 Reed–Muller 码对应的横向非 Clifford 层；
3. 测量 $G_0$ 的四个 $X$ checks；
4. 仅在 syndrome 全为零时接受；
5. 解码一个逻辑输出，并按所用 $T/T^\dagger$ 约定施加已知 Clifford 修正。

输出错误公式成立需要理想 Clifford 和独立随机 $Z$ 错误。实际 fault-tolerant factory 中还要区分：

- 输入 magic-state error；
- 逻辑 Clifford 或 lattice-surgery failure；
- syndrome measurement 和 decoder failure；
- correlated fault 与 hook error；
- leakage、SPAM error 和工厂级 abort。

因此

$$
p_{\mathrm{out}}\approx35p^3
$$

描述的是 distillation code 对输入 magic-state error 的抑制，不是完整 surface-code factory 的总逻辑错误率。

---
### 9. 与其它笔记的连接

- [[State injection]]：说明 noisy magic state 如何进入编码空间，以及蒸馏后的状态如何被消耗为逻辑 $T$ 门。
- [[三正交码与横向逻辑T门]]：从一般重量模 $8$ 条件解释 triorthogonality 与横向非 Clifford 门。

---
### 参考来源

- S. Bravyi and A. Kitaev, [Universal Quantum Computation with ideal Clifford gates and noisy ancillas](https://arxiv.org/abs/quant-ph/0403025), *Physical Review A* **71**, 022316 (2005).
- S. Bravyi and J. Haah, [Magic state distillation with low overhead](https://arxiv.org/abs/1209.2426), *Physical Review A* **86**, 052329 (2012).
