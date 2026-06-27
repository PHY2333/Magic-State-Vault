Jacinto 等人的 compact factory 构造把一个 $nT\to1T$ 蒸馏协议，先改写成 $N$ 个工作 qubits 上的容错逻辑 $T$ 门问题，再通过解码线路把它转回紧凑的 distillation circuit。附录 C 的作用是给出一个系统生成这类线路的反演方法：先规定每个 singleton、pair、triplet 应被多少个 Pauli product rotations 覆盖，再用 Boolean lattice 上的 Möbius inversion 解出实际要放哪些 rotations。

本文采用

$$
T=\operatorname{diag}(1,e^{i\pi/4}),
\qquad
P_{A,\pi/8}
=
\exp\left(-\frac{i\pi}{8}\prod_{i\in A}Z_i\right),
\qquad
[N]=\{1,\ldots,N\}.
$$

这里的 $N$ 是 compact circuit 长期保存的工作 qubits 数；$n$ 是一次尝试消耗的 noisy $|T\rangle$ resources 数。二者不能混同。

---
### 从逻辑门条件到覆盖次数

先在 $N$ qubits 的 phase-flip repetition code 上工作：

$$
|+_L\rangle=|+\rangle^{\otimes N},
\qquad
|-_L\rangle=|-\rangle^{\otimes N},
\qquad
\bar Z=Z_1Z_2\cdots Z_N.
$$

单个 noisy $|T\rangle$ injection 只需在有效模型中留下 $Z$ 型错误；这个约化见 [[State injection]] 和 [[Clifford Twirling 与魔态错误模型]]。外层 repetition code 因而只负责检测 $Z$ 图样。

直接把 $T_1$ 交换过 encoding/decoding ladder，会得到一个对角门层：

$$
E T_1 E^\dagger
=
\prod_i T_i
\prod_{i<j}CS^\dagger_{ij}
\prod_{i<j<k}CCZ_{ijk}.
$$

这个分解的相位来源见 [[重复码上的逻辑T门#相位展开给出的局部门分解]]。为了不用昂贵的 $CS^\dagger$ 和 $CCZ$ 分解，论文改用一组 $\pi/8$ Pauli product rotations。每个 support $A\subseteq[N]$ 的 rotation $P_{A,\pi/8}$ 可以看成在 $A$ 上的小 repetition code 逻辑 $T$，因此它贡献：

- 对每个 $i\in A$，一次 $T_i$；
- 对每个 $\{i,j\}\subseteq A$，一次 $CS^\dagger_{ij}$；
- 对每个 $\{i,j,k\}\subseteq A$，一次 $CCZ_{ijk}$。

如果只要求等价到 Clifford correction，则 $T^2=S$、$(CS^\dagger)^2=CZ$ 都可吸收到 Clifford frame；于是只需要 parity 条件。设 $f:\mathcal P([N])\to\mathbb F_2$ 表示 support $A$ 是否被选入线路，定义覆盖次数

$$
g(B)
=
\sum_{A\supseteq B} f(A)
\pmod 2.
$$

要实现逻辑 $T_L$，每个 singleton、pair、triplet 都必须被奇数个 selected supports 覆盖：

$$
g(B)=1
\qquad
(1\le |B|\le3).
$$

这就是正文 Eq. (15) 的集合版。线路是否容错还要看 faulty rotations 的 supports 能否异或成全重逻辑错误。

---
### Zeta 与 Möbius 反演

这里的对象不是量子态空间，而是所有可能的 gate supports。

给定 $N$ 条工作线，一个 Pauli product rotation 的 support 是某个子集

$$
A\subseteq[N].
$$

所有子集组成

$$
\mathcal P([N])=\{A:A\subseteq[N]\}.
$$

把这些子集按包含关系排序，就得到 Boolean lattice：

$$
(\mathcal P([N]),\subseteq).
$$

这里的 lattice 不是几何里的格点图，而是一种偏序集合。它要求任意两个元素都有：

- 最大下界，称为 meet；
- 最小上界，称为 join。

在 support 的包含关系里，$C$ 是 $A$ 和 $B$ 的下界，意思是

$$
C\subseteq A,
\qquad
C\subseteq B.
$$

最大的这种 $C$ 正是公共部分：

$$
A\wedge B=A\cap B.
$$

类似地，$C$ 是 $A$ 和 $B$ 的上界，意思是

$$
A\subseteq C,
\qquad
B\subseteq C.
$$

最小的这种 $C$ 正是合并后的 support：

$$
A\vee B=A\cup B.
$$

所以 Boolean lattice 在这里的具体含义是：所有 supports 按包含关系作为偏序关系，并且任意两个 supports 都能取“公共子 support” $A\cap B$ 和“合并 support” $A\cup B$。“Boolean” 则指每条线只有“不在 support 中”和“在 support 中”两个状态。

本文真正用到的只是偏序关系 $B\subseteq A$：如果 $B$ 是 singleton、pair 或 triplet，而 $A$ 是某个 selected gate 的 support，那么 $B\subseteq A$ 表示这个 gate 覆盖了 $B$。

设

$$
f(A)=
\begin{cases}
1, & \text{线路中选择 support }A,\\
0, & \text{否则}.
\end{cases}
$$

对一个待检查的小集合 $B$，覆盖次数是

$$
g(B)=\sum_{A\supseteq B}f(A).
$$

这就是 zeta transform。在一般偏序集合上，zeta function 只是“是否可比较且在上方”的指示函数：

$$
\zeta(B,A)=
\begin{cases}
1, & B\subseteq A,\\
0, & \text{otherwise}.
\end{cases}
$$

把它作用在 $f$ 上，就是把所有包含 $B$ 的 supports 的 $f(A)$ 加起来：

$$
(\zeta\star f)(B)
=
\sum_{A\supseteq B}\zeta(B,A)f(A)
=
\sum_{A\supseteq B}f(A)
=g(B).
$$

这里的 kernel 可以理解成一个二元权重函数：

$$
K(B,A).
$$

它描述“support $A$ 对检查对象 $B$ 应该贡献多少权重”。在线性代数语言中，$K(B,A)$ 就像矩阵元，$B$ 是行指标，$A$ 是列指标：

$$
g(B)=\sum_A K(B,A)f(A).
$$

因此 zeta transform 的 kernel 就是覆盖关系指示函数：

$$
K(B,A)=\zeta(B,A).
$$

若 $A$ 覆盖 $B$，权重为 $1$；否则权重为 $0$。所以

$$
g(B)=\sum_A\zeta(B,A)f(A)
$$

只是“矩阵乘向量”的 support 版本，区别是行列指标不是 $1,2,3,\ldots$，而是子集 $A,B\subseteq[N]$。

附录 C 把所有这类定义在有序 pair $(B,A)$ 上、且只在 $B\subseteq A$ 时可能非零的 kernel 组成 incidence algebra。也就是说，incidence algebra 里的二元函数只记录偏序区间

$$
[B,A]=\{C:B\subseteq C\subseteq A\}
$$

上的关系。

两个 kernel 的乘法是 convolution：

$$
(\nu\ast\eta)(B,A)
=
\sum_{B\subseteq C\subseteq A}
\nu(B,C)\eta(C,A).
$$

这个卷积就是矩阵乘法的偏序版本。普通矩阵乘法对所有中间指标求和；这里由于 kernel 只沿包含关系非零，所以中间 support 必须满足

$$
B\subseteq C\subseteq A.
$$

操作上，它是在计算“从小 support $B$ 走到大 support $A$，可以经由哪些中间 support $C$”。引入 incidence algebra 不是为了增加抽象，而是为了能精确地说“zeta transform 可以被反演”。

Möbius function 就是 zeta function 在这个卷积意义下的逆。对 Boolean lattice，

$$
\mu(B,A)=
\begin{cases}
(-1)^{|A|-|B|}, & B\subseteq A,\\
0, & \text{otherwise}.
\end{cases}
$$

这个公式可以直接由“$\mu$ 是 $\zeta$ 的卷积逆”推出。因为

$$
(\mu\ast\zeta)(B,A)
=
\sum_{B\subseteq C\subseteq A}
\mu(B,C)\zeta(C,A).
$$

在求和范围内总有 $C\subseteq A$，所以 $\zeta(C,A)=1$，于是只需让

$$
\sum_{B\subseteq C\subseteq A}\mu(B,C)
=
\delta(B,A).
$$

若 $B=A$，区间里只有 $C=B=A$，因此必须有

$$
\mu(B,B)=1.
$$

若 $B\subsetneq A$，设差集

$$
D=A\setminus B,
\qquad
|D|=m>0.
$$

每个中间 support $C$ 都唯一写成

$$
C=B\cup S,
\qquad
S\subseteq D.
$$

如果令

$$
\mu(B,C)=(-1)^{|C|-|B|}=(-1)^{|S|},
$$

则

$$
\sum_{B\subseteq C\subseteq A}\mu(B,C)
=
\sum_{S\subseteq D}(-1)^{|S|}
=
\sum_{r=0}^{m}\binom mr(-1)^r
=
(1-1)^m
=0.
$$

这正好给出 $B\ne A$ 时的 $\delta(B,A)=0$。因此上面的 $\mu$ 确实满足

$$
\mu\ast\zeta=\delta,
$$

其中 $\delta(B,A)=1$ 当且仅当 $B=A$。Boolean lattice 上同样也可验证 $\zeta\ast\mu=\delta$，所以它就是 Möbius function。因此如果

$$
g=\zeta\star f,
$$

就有

$$
f=\mu\star g.
$$

在普通整数上，这就是 inclusion-exclusion。已知

$$
g(B)=\sum_{A'\supseteq B}f(A')
$$

记录“覆盖 $B$ 的所有 supports 的总贡献”。要反推出某个固定 support $A$ 是否被选中，需要把所有更大检查集合 $B\supseteq A$ 的覆盖次数交替相加：

$$
f(A)=
\sum_{B\supseteq A}
(-1)^{|B|-|A|}g(B).
$$

交替符号会把严格包含 $A$ 的更大 supports 的贡献抵消掉，只留下 $f(A)$。在 $|T\rangle$ distillation 的 $\mathbb F_2$ 情形，$\sum$是$\oplus$，减法和加法没有区别，所有系数都只看模 $2$，而

$$
-1\equiv 1\pmod2.
$$

所以 $(-1)^{|B|-|A|}$ 无论指数奇偶，作为 $\mathbb F_2$ 中的系数都等于 $1$。因此反演进一步简化为

$$
\boxed{
f(A)=\sum_{B\supseteq A}g(B)\pmod2
}.
$$

一个小例子可以看出这个式子的作用。若 $N=3$，并规定

$$
g(\{1\})=g(\{2\})=g(\{3\})
=g(\{1,2\})=g(\{1,3\})=g(\{2,3\})
=g(\{1,2,3\})=1,
$$

则

$$
f(\{1,2,3\})=g(\{1,2,3\})=1,
$$

而

$$
f(\{1,2\})
=g(\{1,2\})+g(\{1,2,3\})
=0\pmod2.
$$

也就是说，虽然 pair $\{1,2\}$ 需要被奇数次覆盖，但它已经被三体 support $\{1,2,3\}$ 覆盖了一次，所以不需要再单独放一个 pair rotation。附录 C 的反演就是把这种“哪些大 support 已经满足了小 support 的覆盖条件”系统化。

因此，一旦指定所有 $g(B)$，每个 possible support $A$ 是否出现在线路中就被反演出来。自由度来自 $|B|>3$ 的 $g(B)$，因为 Eq. (15) 只约束到 triplet,我们只知道$g(B)$的一部分值，其余部分值任取。

---
### Canonical family $F_N^0$

附录 C 的 canonical choice 是把自由变量取成最小形式：

$$
g_0(B)=
\begin{cases}
1, & 1\le |B|\le 3,\\
0, & |B|>3.
\end{cases}
$$

对非空 $A$，令 $r=|A|$。反演给出

$$
f_0(A)
=
\sum_{s=r}^{3}
\binom{N-r}{s-r}
\pmod2.
$$

于是

$$
f_0(A)=0
\qquad(r>3),
$$

$$
f_0(A)=1
\qquad(r=3),
$$

$$
f_0(A)=N-1\pmod2
\qquad(r=2),
$$

$$
f_0(A)=N+\binom{N-1}{2}\pmod2
\qquad(r=1).
$$

因此 $f_0(A)$ 只依赖 support 的大小 $r=|A|$，不依赖具体是哪几条线。所有 triplets 总是被选中，因为 $f_0(A)=1$。Pairs 是否被选中由

$$
N-1\pmod2
$$

决定：$N$ 为偶数时 $N-1$ 为奇数，所以所有 pairs 被选中；$N$ 为奇数时所有 pairs 不被选中。

Singletons 是否被选中由

$$
N+\binom{N-1}{2}
\pmod2
$$

决定。只需看 $N\bmod4$。令 $N=4q+s$，$s\in\{0,1,2,3\}$，则

| $N\bmod4$ | $N-1\bmod2$ | $N+\binom{N-1}{2}\bmod2$ | selected supports        |
| --------: | ----------: | -----------------------: | ------------------------ |
|       $0$ |         $1$ |                      $1$ | singleton, pair, triplet |
|       $1$ |         $0$ |                      $1$ | singleton, triplet       |
|       $2$ |         $1$ |                      $0$ | pair, triplet            |
|       $3$ |         $0$ |                      $0$ | triplet                  |

例如 singleton 的判定中，$\binom{N-1}{2}=(N-1)(N-2)/2$ 的奇偶随 $N\bmod4$ 周期变化，所以不需要知道更细的 $N$。也就是说，canonical family 只使用 weight-$1$、weight-$2$、weight-$3$ 的 Pauli product rotations；是否保留所有 singleton 或所有 pair 只由 $N\bmod4$ 决定。设 $n$ 为 selected supports 数，则

$$
\boxed{
n=
\begin{cases}
\binom N1+\binom N2+\binom N3, & N\equiv0\pmod4,\\[2mm]
\binom N1+\binom N3, & N\equiv1\pmod4,\\[2mm]
\binom N2+\binom N3, & N\equiv2\pmod4,\\[2mm]
\binom N3, & N\equiv3\pmod4.
\end{cases}
}
$$

例如这个 family 给出：

| $N$ | $n$ | distance |
|---:|---:|---:|
| $4$ | $14$ | $2$ |
| $5$ | $15$ | $3$ |
| $10$ | $165$ | $4$ |
| $11$ | $165$ | $5$ |

$N=5$ 的 $15\to1$ 与 [[Reed-Muller码]] 的三阶协议对应；$N=10,11$ 则说明单层 compact circuit 可以用较小工作宽度达到 $p^4$、$p^5$ 阶错误抑制，但 $n$ 和完整 surface-code 开销仍需另算。

---
### 距离为什么由覆盖 $[N]$ 决定

若 support 为 $A$ 的 Pauli product rotation 出错，它在 repetition block 上留下

$$
Z(A)=\prod_{i\in A}Z_i.
$$

一组 faulty gates $K$ 的总错误 support 是 symmetric difference：

$$
\bigoplus_{A\in K} A.
$$

phase-flip repetition code 的无 syndrome $Z$ 图样只有 $0$ 和 $[N]$；后者是逻辑错误 $\bar Z$。因此 canonical logical-gate circuit 的距离是

$$
d(F_N^0)
=
\min |K|
\quad\text{s.t.}\quad
\bigoplus_{A\in K}A=[N].
$$

由于 $F_N^0$ 中每个 support 至多包含 $3$ 个 qubits，必有

$$
d(F_N^0)\ge \left\lceil\frac N3\right\rceil.
$$

这个下界只使用了 support 大小，不足以得到$d(F_{N}^{0})$,要得到具体值需要处理奇偶性。对 symmetric difference 有

$$
|A\oplus B|
=
|A|+|B|-2|A\cap B|,
$$

所以模 $2$ 意义下

$$
|A\oplus B|
\equiv
|A|+|B|
\pmod2.
$$

推广到一组 supports：

$$
\left|\bigoplus_{A\in K}A\right|
\equiv
\sum_{A\in K}|A|
\pmod2.
$$

当 $N$ 为奇数时，canonical family 只允许奇数大小的 supports：

- $N\equiv1\pmod4$：只选 singleton 和 triplet；
- $N\equiv3\pmod4$：只选 triplet。

因此每个 faulty support 都有 $|A|\equiv1\pmod2$，于是

$$
\left|\bigoplus_{A\in K}A\right|
\equiv
|K|
\pmod2.
$$

又未检测逻辑错误要求

$$
\bigoplus_{A\in K}A=[N],
$$

而 $|[N]|=N$ 是奇数，所以必须有

$$
|K|\equiv1\pmod2.
$$

这就是奇数 $N$ 的 parity 限制：不仅要用至少 $\lceil N/3\rceil$ 个 faulty gates 覆盖全部 $N$ 条线，faulty gates 的个数还必须是奇数。附录 C 的结论是

$$
\boxed{
d(F_N^0)=
\begin{cases}
\left\lceil N/3\right\rceil,
& N\text{ even},\\[2mm]
\min\{t\in2\mathbb Z+1:t\ge N/3\},
& N\text{ odd}.
\end{cases}
}
$$

构造方式可以这样理解：

- 偶数 $N$ 时，使用 disjoint triplets，余下 $1$ 个 qubit 时用两个 pairs 替代，余下 $2$ 个 qubits 时用一个 pair，因此达到 $\lceil N/3\rceil$。
- $N\equiv1\pmod4$ 时，allowed supports 是 singletons 和 triplets；用 triplets 覆盖主体，剩余 qubits 用 singletons 补齐，并保持 faulty gate 数为奇数。
- $N\equiv3\pmod4$ 时，allowed supports 只有 triplets。若剩余 $7$ 个 qubits，可用三个 triplets 只共享一个 qubit，例如 $\{a,b,c\},\{a,d,e\},\{a,f,g\}$，异或后得到全部 $7$ 个 qubits。

原文笔误：附录 C 在 $N=3q+2$ 且 $N\equiv3\pmod4$ 的构造句子中写成“two triplets sharing one qubit for the 5 remaining qubits”。但两个三元组共享一个 qubit 时，symmetric difference 的重量为 $4$，不可能得到 5 个剩余 qubits；若不共享则重量为 $6$，同样不对。距离公式和表格要求这里使用奇数个 triplets；一个可行的 5-qubit block 是三个 triplets 共享两个 qubits：

$$
\{a,b,c\}\oplus\{a,b,d\}\oplus\{a,b,e\}
=
\{a,b,c,d,e\}.
$$

这与 $N=11$ 给出的 distance $5$ 一致。

---
### 从 repetition 线路到 triorthogonal matrix

本篇的解析构造发生在 repetition-code logical gate 的 support 空间中。把这个逻辑门线路交换过解码 ladder $E^\dagger$ 后，才得到真正的 compact distillation circuit。具体的有限差分推导见 [[重复码上的逻辑T门#$\alpha$ 条件如何变成 triorthogonal 条件]]；这里仅保留本篇需要的桥梁。

若逻辑门线路中的第 $k$ 个 Pauli product rotation 的 support 是

$$
\alpha^k\in\mathbb F_2^N,
$$

则解码后对应的 support 是

$$
\beta_1^k=\alpha_1^k,
\qquad
\beta_i^k=\alpha_i^k\oplus\alpha_{i-1}^k
\quad(2\le i\le N).
$$

把 $\beta^k$ 作为列排成矩阵 $G$，第一行对应输出 qubit，其余 $N-1$ 行对应检查 qubits。有限差分把 $\alpha$ 空间中的“每个 singleton、pair、triplet 被奇数次覆盖”转成 punctured triorthogonal 条件：

$$
\sum_k\beta_1^k\equiv1\pmod2,
\qquad
\sum_k\beta_i^k\equiv0\pmod2
\quad(i\ge2),
$$

$$
\sum_k\beta_i^k\beta_j^k\equiv0\pmod2,
\qquad
\sum_k\beta_i^k\beta_j^k\beta_l^k\equiv0\pmod2.
$$

错误条件也随同一个差分变换移动。repetition-code 逻辑门中的未检测逻辑错误是全重图样

$$
\bigoplus_{k\in K}\alpha^k
=
\mathbf 1.
$$

解码后它变成只打到第一条线的输出错误：

$$
\bigoplus_{k\in K}\beta^k
=
\begin{pmatrix}
1\\0\\ \vdots\\0
\end{pmatrix}
\pmod2.
$$

因此同一组 supports 给出一个 $nT\to1T$ distillation protocol；若输入 magic-state error 是独立随机 $Z$ 错误，则

$$
p_{\mathrm{out}}
=
C p_{\mathrm{in}}^d+O(p_{\mathrm{in}}^{d+1}),
$$

其中 $d$ 是能产生上式输出错误的最小 faulty set 大小，$C$ 是 weight-$d$ malignant sets 的个数。$C$ 取决于具体矩阵的 weight enumerator，不由距离单独决定。

#### 为什么不直接在解码后做 canonical 反演

容易误以为：既然最终对象是 triorthogonal distillation matrix，就可以直接在解码后的 $\beta$ 空间中照搬附录 C 的做法，把未约束的高阶覆盖变量全设为零。这样做会退化成平凡协议。

在 $\beta$ 空间中，设 $h(A)$ 表示是否选择 support $A$ 的 distillation rotation，并定义覆盖次数

$$
\widetilde g(B)
=
\sum_{A\supseteq B}h(A).
$$

triorthogonal 条件要求第一行是输出行，其余行是检查行。因此低阶覆盖条件不是“所有 singleton、pair、triplet 都为 $1$”，而是

$$
\widetilde g(\{1\})=1,
$$

并且对所有其它非空 $B$、只要 $|B|\le3$，都有

$$
\widetilde g(B)=0.
$$

如果再把自由变量也取为零，

$$
\widetilde g(B)=0
\qquad(|B|>3),
$$

那么所有 $\widetilde g(B)$ 中唯一非零的就是 $\widetilde g(\{1\})$。用 $\mathbb F_2$ 上的 Möbius 反演

$$
h(A)=\sum_{B\supseteq A}\widetilde g(B)
$$

可得

$$
h(\{1\})=1,
\qquad
h(A)=0
\quad(A\ne\{1\},\;A\ne\varnothing).
$$

也就是说，线路只剩下一个 support 为 $\{1\}$ 的 $\pi/8$ rotation：在第一条输出线上做一个物理 $T$。它没有使用检查 qubits，也不会把输入错误变成可检测 syndrome；作为 distillation protocol，它没有错误阶数提升。

repetition code 的作用正是在反演之前改变“目标错误”的几何形状。逻辑门空间中的未检测错误不是局域的 $e_1$，而是全重的

$$
\mathbf 1=(1,\ldots,1).
$$

canonical family 只允许大小不超过 $3$ 的 supports，因此若要由 faulty rotations 异或出 $\mathbf1$，至少需要约 $N/3$ 个错误。构造完成后再通过解码差分把

$$
\mathbf1\longmapsto e_1
$$

转成 distillation 输出错误。也就是说，repetition code 先把将来的输出错误“摊开”为全重逻辑 $\bar Z$，附录 C 的 support 反演再利用小 supports 很难拼出全重图样来获得距离；最后解码才把它压回第一条输出线。

---
### $\sqrt T$ 与更高层旋转

附录 C 还说明同一反演框架可用于

$$
|\sqrt T\rangle
=
R_Z(\pi/16)|+\rangle
$$

以及更一般的

$$
|L\sqrt{\;T\;}\rangle
=
R_Z\left(\frac{\pi}{2^{L+2}}\right)|+\rangle.
$$

对 $\sqrt T$，逻辑 $\sqrt T_L$ 交换过 CNOT ladder 后会出现 $\sqrt T$、$CT^\dagger$、$CCS$ 和 $CCCZ$。前三类门平方后仍非 Clifford，因此覆盖条件要提升到模 $4$：

$$
\sum_k\alpha_i^k\equiv1\pmod4,
$$

$$
\sum_k\alpha_i^k\alpha_j^k\equiv1\pmod4,
\qquad
\sum_k\alpha_i^k\alpha_j^k\alpha_l^k\equiv1\pmod4,
$$

而四体项只需

$$
\sum_k
\alpha_i^k\alpha_j^k\alpha_l^k\alpha_m^k
\equiv1\pmod2.
$$

因此 $f$ 不再只取 $0/1$，而是取值于 $\mathbb Z/4\mathbb Z$，用来区分注入 $|\sqrt T\rangle$、$|T\rangle$ 或 $|T^{3/2}\rangle$ 型 rotation。canonical choice 取

$$
g(B)=1\pmod4
\quad(1\le |B|\le3),
\qquad
g(B)=1\pmod4
\quad(|B|=4),
\qquad
g(B)=0\pmod4
\quad(|B|>4),
$$

其中 $|B|=4$ 的物理条件只要求 $1\pmod2$；这里选择 $1\pmod4$ 作为 canonical representative。

并由 Möbius inversion 得到

$$
f_1(A)\equiv
(-1)^{|A|}
\binom{N-|A|-1}{4-|A|}
\pmod4
\qquad(1\le |A|\le4).
$$

每个非零 support 的 $P_{\pi/16}$ injection 由于有非 Clifford correction，按论文约定计作 $2$ 个 $\sqrt T$ resources。因此

$$
n_{\sqrt T}
=
2\sum_{s=1}^4
\binom Ns\,
\mathbf 1\!\left[
f_1(A_s)\not\equiv0\pmod4
\right],
$$

其中 $A_s$ 是任意 $s$ 元 support；canonical family 对同一大小的 support 全选或全不选。它的距离是

$$
d(F_N^1)=\left\lceil\frac N4\right\rceil.
$$

这个推广展示了方法的结构：若要蒸馏更高层 $Z$ 轴 magic state，就把系数环换成 $\mathbb Z/2^{L+1}\mathbb Z$，覆盖条件一直约束到 $|B|=L+3$，canonical family 的距离至少随 $\lceil N/(L+3)\rceil$ 增长。代价是 canonical circuits 很深，更多是给出可证明 family 和搜索基准，不一定是实用最优 factory。

---
### 适用范围与失效模式

上面的推导依赖以下条件：

- inner QECC 已把 Clifford 操作、Pauli measurements、classical feedforward 和 lattice-surgery 型 Pauli product rotations 的 Clifford 部分保护好；
- noisy magic states 的主要错误可化成独立随机 $Z$ 错误；
- Clifford corrections 可可靠执行或并入 Clifford frame；
- repetition code 只检测 $Z$ 型错误，不处理 leakage、measurement fault、routing fault 或 correlated faults；
- $n$ 只计 non-Clifford resource injections，不等于完整硬件峰值 qubit 数、周期数或 spacetime volume。

因此 $p_{\mathrm{out}}\sim p_{\mathrm{in}}^d$ 只描述 distillation code 对输入 magic-state error 的阶数抑制。若 injection gadgets、检查测量或底层纠错引入相关错误，距离和前因子都要重新估算。

---
### 连接

- [[State injection]]：说明 $|T\rangle$ 或 $|\sqrt T\rangle$ 如何通过 injection 实现对应 $Z$ 轴 rotation。
- [[重复码上的逻辑T门]]：给出 repetition-code logical $T$、$\alpha\mapsto\beta$ 变换和 triorthogonal 条件的线路推导。
- [[Distillation protocol]]：把解码后的 $G$ 矩阵解释为一般 $n\to k$ triorthogonal distillation protocol。
- [[Reed-Muller码]]：展开 $N=5,n=15,d=3$ 的标准 15-to-1 特例和 $35p^3$ 常数。

---
### 来源

- H. Jacinto, X. Valcarce, V. Barizien, É. Gouzien, and N. Sangouard, [*Exploring the landscape of compact magic-state distillation factories*](<../../Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf>), arXiv:2606.07734 (2026), Sec. II.B, Sec. III, Sec. IV, Appendix C.
