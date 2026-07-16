Menon 等人的 magic tricycles 不是把小型 triorthogonal distillation code 多轮级联，而是用有限块长 qLDPC CSS 码同时提供高 rate / distance、常深度 physical CCZ circuit 和 single-shot state preparation，从而直接制备包含 $|CCZ\rangle$ 资源的 logical hypergraph magic states。

本文献的阅读重点是三条桥：

1. 从 Abelian group algebra 元素 $a,b,c$ 构造一个三维 balanced-product CSS 码；
2. 用 cup-product / Leibniz rule 构造保持码空间的常深度 transversal $CCZ$ circuit；
3. 用 redundant $Z$ checks 的 metachecks 和 soundness，把 logical $|+\rangle^{\otimes K}$ 与后续 $CCZ$ 操作放进 single-shot factory 图像。

---
### 先补哪些前置知识

这篇文章的难点不在 $CCZ$ 本身，而在把 qLDPC code、同调乘积和横向三体相位放到同一个语言里。阅读前建议先掌握下面几层。

#### Magic-state 与 CCZ resource

已有笔记可以先读：

- [[State injection]]：理解非 Clifford 逻辑门如何通过 magic state teleportation 消耗资源态实现。
- [[Distillation protocol]]：理解 code-space distillation 中“横向非 Clifford 门 + syndrome/postselection”如何给出错误抑制。
- [[Clifford Twirling 与魔态错误模型]]：传统 distillation 常把输入 magic-state error 约化成随机 Pauli 错误；Menon 这篇则更偏 circuit-level noise 和 encoded state preparation。
- [[SAT搜索紧凑蒸馏工厂#扩展到 $CCZ$ factories]]：对比 Jacinto 的 $nT\to1CCZ$ compact factory。Jacinto 仍把输入资源写成 noisy $T$ rotations；Menon 的路线是假设物理层能执行 noisy $CCZ$，再用 qLDPC 码把它提升成 logical $CCZ$ magic state。

这里的输出不是单个 $T$ state，而是三组 logical qubits 上的

$$
CCZ|+\!+\!+\rangle
$$

或更一般的 hypergraph magic state。若 logical $CCZ$ connectivity 中能找出 $K_{\mathrm{CCZ}}$ 个互不重叠的三元组，就能抽取 $K_{\mathrm{CCZ}}$ 个可单独使用的 $|CCZ\rangle$ resources。

#### CSS code 与同调语言

已有笔记：

- [[二进制空间性质]]：$\mathbb F_2$ 线性空间、正交补、商空间。
- [[逻辑基态的表示]]：CSS/stabilizer code 的逻辑态和投影图像。
- [[三正交码与横向逻辑T门]]：横向对角非 Clifford 门如何由计算基相位、行重叠和逻辑矩阵决定。

本文献把 CSS 码写成 cochain complex。第一次接触这种写法时先读 [[Chain complex 与 cochain complex]]，再读 [[CSS码中的cochain complex]]；完整对象对应见 [[Tricycle complex 的 balanced-product 构造]]。这里采用论文 Sec. D 中用于 cup-product 的 convention：$0$-cochains 对应 $X$ checks，$1$-cochains 对应 qubits，$2$-cochains 对应 $Z$ checks。最小翻译如下：

$$
C^0 \xrightarrow{\delta^0} C^1 \xrightarrow{\delta^1} C^2,
\qquad
\delta^1\delta^0=0.
$$

在 CSS 码里：

- $C^0$ 对应 $X$ checks；
- $C^1$ 对应 physical qubits；
- $C^2$ 对应 $Z$ checks；
- $\operatorname{im}\delta^0$ 是 $X$-stabilizer 生成的 coboundaries；
- $\ker\delta^1/\operatorname{im}\delta^0$ 给出逻辑 $X$ operator 的等价类。

Menon 的 tricycle code 还会多出一项 $C^3$，即

$$
C^0\to C^1\to C^2\to C^3.
$$

最后一张映射不是新的 stabilizer，而是 $Z$ syndrome 之间的关系，也就是 metachecks。

#### qLDPC、single-shot 与 metachecks

这篇文章的 factory 不是只在理想 Clifford 假设下分析 distillation order，而是关心 syndrome extraction circuit 的深度和 circuit-level noise。因此需要区分：

- code distance $D=\min(D_X,D_Z)$；
- check weight 与 qubit degree，决定 syndrome extraction 是否 LDPC；
- metacheck distance $D_Z^{\mathrm{SS}}$，决定 noisy syndrome 中的 measurement error 能否被单次测量记录识别；
- soundness，说明小 syndrome 能由小 data correction 解释，从而避免 single-shot decoder 输出大残余错误。

直观上，surface code 要通过 $O(d)$ 轮 syndrome history 过滤 measurement faults；single-shot code 依赖同一轮 syndrome 内部的冗余关系来过滤这些 faults。

#### Group algebra 与 balanced product

本文的具体码来自有限 Abelian 群

$$
G=\mathbb Z_{m_1}\times\cdots\times\mathbb Z_{m_k},
\qquad
R=\mathbb F_2[G].
$$

一个 group-algebra 元素

$$
a=\sum_{g\in G}a_g g
$$

通过 regular representation 变成一个二进制矩阵 $A=B_G(a)$。若 $a$ 的 support 有 $w$ 个群元素，则 $A$ 的每行每列重量都是 $w$。在 trivariate case 中，也可以把 $R$ 看成

$$
\mathbb F_2[x,y,z]/(x^{m_1}-1,y^{m_2}-1,z^{m_3}-1),
$$

其中单项式对应循环移位 permutation matrices。

普通 cochain-complex tensor product 会让三维乘积码规模按种子大小三次方增长；相关 total degree 分层见 [[Cochain complex 的 tensor product]]。Right/left module、anti-diagonal quotient 与两个 balanced interfaces 见 [[Balanced tensor product 与 coinvariant quotient]]；Menon 特例的具体矩阵来源见 [[Tricycle complex 的 balanced-product 构造]]。三个 classical group-algebra seed codes 经过三重 balanced product 后得到 $R\to R^3\to R^3\to R$。

#### Cup-product 与 Leibniz rule

一般 cup product 与 Leibniz rule 见 [[Cup product 与 Leibniz rule]]；classical seed 上的 in/out/free preorientation 与 local integrated Leibniz 见 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]；这些局部数据通过 free $G^2$-作用和 relative translates 继承到 balanced complex 的过程见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；最高层求和泛函的 physical 读数和 Proposition 5 判据见 [[Symmetric triple cup-product]]。在 Menon 的四项 cochain complex 上，使用的是下面这条结论：如果能定义乘法

$$
\cup:C^i\times C^j\to C^{i+j},
$$

并选择 $C^3=R$ 上的求和泛函，使 integrated coboundary vanish，那么可以由它构造一个对角三体相位线路。对 physical qubits $q_i,q_j,q_k\in C^1$，

$$
f_{\cup}(q_i,q_j,q_k)
=
|(q_i\cup q_j)\cup q_k|
\pmod 2
$$

决定是否施加一个 physical $CCZ$。Leibniz rule 与 Menon 的 $\int_R\delta=0$ 条件保证这个三线性函数对 coboundary 不敏感，因此它能下降到逻辑商空间，而不是依赖某个逻辑算符代表元的任意选择。

---
### 文章理论主线

#### 码构造先给出 sparse checks 和 metachecks

tricycle code 由三个两两可交换的 $n_G\times n_G$ 二进制矩阵 $A,B,C$ 定义。它们来自 group-algebra 元素 $a,b,c\in\mathbb F_2[G]$，且

$$
A=\sum_{i=1}^{w_a}A_i,
\qquad
B=\sum_{i=1}^{w_b}B_i,
\qquad
C=\sum_{i=1}^{w_c}C_i,
$$

其中每个 $A_i,B_i,C_i$ 是 permutation matrix。总 qubit 数是

$$
N=3n_G.
$$

CSS parity-check matrices 是

$$
H_X=
\begin{bmatrix}
A^T&B^T&C^T
\end{bmatrix},
$$

$$
H_Z=
\begin{bmatrix}
C&0&A\\
0&C&B\\
B&A&0
\end{bmatrix}.
$$

因为 $A,B,C$ 两两可交换，且在 $\mathbb F_2$ 上有 $XY+YX=0$，所以

$$
H_ZH_X^T=0.
$$

这一步给出它确实是 CSS 码的对易来源。check weights 由 $w_a,w_b,w_c$ 控制：

- $X$ checks 的重量是 $w_a+w_b+w_c$；
- 三类 $Z$ checks 的重量分别是 $w_c+w_a$、$w_c+w_b$、$w_b+w_a$。

因此只要 $w_a,w_b,w_c=O(1)$，这就是 qLDPC code。

同一个构造还给出 $Z$ syndrome 的冗余关系：

$$
H_{\mathrm{meta}}
=
\begin{bmatrix}
B&A&C
\end{bmatrix},
$$

并满足

$$
H_{\mathrm{meta}}H_Z=0.
$$

这个式子是 single-shot 部分的入口。它说明并非所有 $Z$ syndrome strings 都是独立的；measurement error 会破坏这些 metachecks，从而可以在单轮 syndrome 内被检测。

从 balanced-product 角度看，同一件事来自四项 complex

$$
R
\xrightarrow{(a,b,c)^T}
R^3
\xrightarrow{
\begin{bmatrix}
c&0&a\\
0&c&b\\
b&a&0
\end{bmatrix}}
R^3
\xrightarrow{(b\ a\ c)}
R.
$$

中间三项给出 CSS code，最后一项给出 metachecks。这个同调写法不是装饰；后面的 cup-product、coboundary invariance 和 logical action 都依赖它。

#### 横向 CCZ 先是一个三线性函数

取三个相同的 tricycle code blocks，每个 block 又分成三个 sector，记为 I、II、III。physical $CCZ$ circuit 由

$$
f_{\mathrm{CCZ}}:Q\times Q\times Q\to\mathbb F_2
$$

指定：

$$
f_{\mathrm{CCZ}}(q_1,q_2,q_3)=1
$$

表示在三块码的这三个 physical qubits 上放一个 $CCZ$。

这里的 $Q$ 是 physical qubit labels，所以这一步的 $f_{\mathrm{CCZ}}$ 是 physical hyperedge 的指示函数。后面把它作用到 logical $X$ supports 时，默认按 $\mathbb F_2$ 三线性扩张到 $C^1=\mathbb F_2^Q$；多比特 support 输入只统计被三个 supports 同时选中的 physical $CCZ$ gates 的奇偶。

它要成为合法的 logical gate，需要两个条件。

第一，$f_{\mathrm{CCZ}}$ 必须对 $X$ stabilizer 方向消失。若某个输入是 $X$-coboundary，而另外两个是 logical $X$ 代表元，则

$$
f_{\mathrm{CCZ}}(\delta^0u,y,z)=0
$$

以及另外两条输入腿的同类条件也成立。这样当 logical operator 加上 stabilizer 代表元时，logical action 不会变。换句话说，$f_{\mathrm{CCZ}}$ 在 logical supports 上真正使用的是 quotient 上诱导出的函数

$$
\bar f_{\mathrm{CCZ}}:
H^1(C)^{\times3}\to\mathbb F_2,
\qquad
\bar f_{\mathrm{CCZ}}([x],[y],[z])
=
f_{\mathrm{CCZ}}(x,y,z).
$$

第二，每个 physical qubit 参与的 $CCZ$ 数量必须是常数。这个 maximum degree 控制错误扩散，实际 circuit depth 只比它多一个小的 scheduling 因子。

一旦 $f_{\mathrm{CCZ}}$ 合法，逻辑作用由它限制到 logical $X$ operator basis 得到。设三块码的 logical $X$ basis 为

$$
\{l_i^{(1)}\}_{i=1}^K,
\qquad
\{l_j^{(2)}\}_{j=1}^K,
\qquad
\{l_k^{(3)}\}_{k=1}^K.
$$

定义 logical connectivity tensor

$$
T^{\mathrm{log}}_{ijk}
=
\bar f_{\mathrm{CCZ}}([l_i^{(1)}],[l_j^{(2)}],[l_k^{(3)}]).
$$

于是 logical circuit 是

$$
\prod_{i,j,k:\ T^{\mathrm{log}}_{ijk}=1}
CCZ_{i,j,k}.
$$

把它作用到

$$
|+\rangle_L^{\otimes K}
\otimes
|+\rangle_L^{\otimes K}
\otimes
|+\rangle_L^{\otimes K}
$$

上，就得到一个 logical hypergraph magic state。

如果只想要可单独消费的 $|CCZ\rangle$ resources，需要改变三块码的 logical basis，使 $T^{\mathrm{log}}$ 中出现尽可能大的 identity-like diagonal subtensor。最大可抽取数 $K_{\mathrm{CCZ}}$ 是这个三阶二进制 tensor 的 subrank。文章用 MIP 找下界；这不是 guaranteed optimal，所以表中的 $K_{\mathrm{CCZ}}$ 应理解为已找到的可用产率，而非严格最优产率。

#### Symmetric triple cup-product 给出解析构造

普通 cup-product 构造从 classical two-term complex 的 preorientation 开始。对一个 coboundary $\delta(x)$，选择分割

$$
\delta(x)
=
\delta_{\mathrm{in}}(x)
\sqcup
\delta_{\mathrm{out}}(x)
\sqcup
\delta_{\mathrm{free}}(x).
$$

对 group-algebra code，这等价于把

$$
a=a_{\mathrm{in}}+a_{\mathrm{out}}+a_{\mathrm{free}}
$$

分成三个 disjoint support parts，并令

$$
\delta_{\mathrm{in}}(\alpha)=a_{\mathrm{in}}\alpha,
\quad
\delta_{\mathrm{out}}(\alpha)=a_{\mathrm{out}}\alpha,
\quad
\delta_{\mathrm{free}}(\alpha)=a_{\mathrm{free}}\alpha.
$$

Breuckmann 等人的原始条件在 higher-weight group-algebra elements 上太限制，常导致 $K=3$ 或 $D=2$ 的退化参数。Menon 这篇的核心理论改动是定义 symmetric triple cup-product：根据三个输入中哪个处于 $C^1$，改变 cup-product 的括号顺序。这样得到新的 integrated Leibniz 条件。

在本文实际使用的 free partition 为空时，条件可压缩成三类 parity constraints。对 $a$ 而言：

$$
|a_{\mathrm{in}}|+|a_{\mathrm{out}}|=0\pmod2,
$$

$$
|a_{\mathrm{in}}\cap a_{\mathrm{in}}w|
+
|a_{\mathrm{out}}\cap a_{\mathrm{out}}w|
=0\pmod2
\qquad(w\ne e),
$$

$$
|a_{\mathrm{in}}\cap a_{\mathrm{in}}v\cap a_{\mathrm{in}}w|
+
|a_{\mathrm{out}}\cap a_{\mathrm{out}}v\cap a_{\mathrm{out}}w|
=0\pmod2
\qquad(v\ne w\ne e).
$$

$b,c$ 满足同型条件。重量为 2 的 group-algebra element 自动满足这些条件；重量为 4 时，文章给出一个有用构造：

$$
a=a_1+a_1s+a_3+a_3s,
$$

并取

$$
a_{\mathrm{in}}=a_1+a_1s,
\qquad
a_{\mathrm{out}}=a_3+a_3s,
\qquad
a_{\mathrm{free}}=0.
$$

经验上要避免 $s^2=e$ 的 involution offset；文章观察到 involution offset 往往把距离压到 $D=2$，而允许 $s^2\ne e$ 是得到较好 finite-block parameters 的关键。

给定三组 preorientations，文章 Proposition 5 给出 physical $CCZ$ 的显式判据。令

$$
\alpha^{\mathrm I}=a,
\qquad
\alpha^{\mathrm {II}}=b,
\qquad
\alpha^{\mathrm {III}}=c.
$$

若 $p_i,q_j,r_k$ 分别来自三个 code blocks 且 sector labels 为 $i,j,k\in\{\mathrm I,\mathrm {II},\mathrm {III}\}$，则

$$
f_{\mathrm{CCZ}}(p_i,q_j,r_k)
=
\left|
r\alpha_i^{\mathrm{in}}\alpha_j^{\mathrm{in}}
\cap
q\alpha_i^{\mathrm{in}}\alpha_k^{\mathrm{out}}
\cap
p\alpha_j^{\mathrm{out}}\alpha_k^{\mathrm{out}}
\right|
\mathbf 1_{\mathrm{pd}}(i,j,k)
\pmod2.
$$

这里 $\mathbf 1_{\mathrm{pd}}(i,j,k)=1$ 表示 $i,j,k$ 两两不同。这个公式的用途很具体：交集奇偶为 1，就放一个 physical $CCZ$；两个输入落在同一 sector，则 indicator 为 $0$，不放门。

由这个构造得到的 circuit maximum degree 有简单分类：

- $4-2-2$ tricycle codes：degree $8$；
- $4-4-2$：degree $16$ 或 $32$；
- $4-4-4$：degree $12$、$64$ 或 $128$。

文章主线主要关注 $4-2-2$，因为它的 check weights 小，STCP 给出的 $CCZ$ circuit degree 也小。

#### Numerical Leibniz Rule 是找短线路的第二条路

STCP 是解析构造，但对某些 $4-4-4$ 码会给出很深的 circuit。附录 E 的 Numerical Leibniz Rule (NLR) 换一种做法：不从具体 cup-product partition 出发，而是直接搜索 group-equivariant trilinear functions

$$
f_i^j:C_i\times C_i\times C_i\to\mathbb F_2
$$

使它们满足 generalized Leibniz rule：

$$
f_i^1(\alpha_i g_1,g_2,g_3)
+
f_i^2(g_1,\alpha_i g_2,g_3)
+
f_i^3(g_1,g_2,\alpha_i g_3)
=0\pmod2.
$$

这些函数先形成 classical parity-check problem，再由 product ansatz 拼成 quantum code 上的 $f_{\mathrm{CCZ}}$。NLR 的优势是可能找到更短 degree 的 physical $CCZ$ circuit；代价是它不是一个按参数自动保证短深度的解析族，需要和 code search 一起做。

#### Single-shot factory 依赖 Z-basis metachecks

magic-state generation protocol 的最短骨架是：

1. 准备三块 tricycle code 的 logical $|+\rangle_L^{\otimes K}$；
2. 对三块码施加上面构造的常深度 physical $CCZ$ circuit；
3. 得到 logical hypergraph magic state，并从中抽取 $K_{\mathrm{CCZ}}$ 个 disjoint $|CCZ\rangle$ resources，或把整个 hypergraph state 当作高 magic resource 使用。

第 1 步不是普通“把所有 data qubits 放到 $|+\rangle$”这么简单。物理 $|+\rangle^{\otimes N}$ 自动满足 $X$ checks，但 $Z$ stabilizers 的本征值起初是随机的，必须可靠地修到 $+1$。如果 $Z$-check measurement 本身有错，就需要从 syndrome 冗余里判断哪些 syndrome bits 是假的。

tricycle code 的 metacheck

$$
H_{\mathrm{meta}}
=
\begin{bmatrix}
B&A&C
\end{bmatrix}
$$

正好在 $Z$ syndrome 上形成 classical code。single-shot distance $D_Z^{\mathrm{SS}}$ 衡量的是：最小的 faulty syndrome pattern，既通过所有 metachecks，又不是真实 data error syndrome。文章对表中码发现 $D_Z^{\mathrm{SS}}=D_Z$ 或至少与上界一致，并引用/证明相应 soundness 结果。

这解释了 protocol 可以只用常数轮 syndrome extraction 准备 logical $|+\rangle_L$ 的原因；它不需要像 surface-code style 那样依赖 $O(d)$ 轮时间冗余。

在 $CCZ$ circuit 期间，错误传播方向也很重要。$CCZ$ 会把一个输入腿上的 $X$ 错误共轭成带 $CZ$ byproduct 的错误，例如形式上

$$
X_1\mapsto X_1CZ_{23}.
$$

这些 byproducts 在后续 syndrome 测量中会表现为非确定的 $Z$ 型错误模式，所以必须及时把 $Z$ stabilizers 维持在正确值。相反，$Z$ 错误与 $CCZ$ 对易，不需要在 $CCZ$ circuit 中实时纠正；因此文章强调 $Z$ basis single-shot 比 $X$ basis single-shot 更关键。

---
### 理论部分阅读顺序

不要按页码一口气读到模拟结果。更有效的顺序是：

1. 先读 [[Chain complex 与 cochain complex]] 和 [[CSS码中的cochain complex]]，确认 $\ker/\operatorname{im}$、quotient 和 $H^1$ 的 CSS 码含义；再读 [[Balanced tensor product 与 coinvariant quotient]] 和 [[Tricycle complex 的 balanced-product 构造]]，区分 balanced quotient 与 cohomology quotient，并保留 $C^0\to C^1\to C^2\to C^3$ 的对象对应关系。
2. 读 Appendix A 到 Eq. (25)：确认 $a,b,c$ 如何给出 $H_X,H_Z,H_{\mathrm{meta}}$，以及三重 balanced product 的来源。
3. 回到 Sec. 2.1：把 Table 1 的参数放回 check weight、distance imbalance 和 LDPC 条件中理解。
4. 先读 [[Cup product 与 Leibniz rule]] 和 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]，再读 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]，最后读 [[Symmetric triple cup-product]] 到 Proposition 5。重点是分清两步：relative-translate construction 先让 trilinear operation 定义在 balanced quotient 上，integrated Leibniz 再保证数值读数对 cohomology representative 不变。
5. 回到 Sec. 2.2：用 $T^{\mathrm{log}}_{ijk}=f_{\mathrm{CCZ}}(l_i,l_j,l_k)$ 理解 logical hypergraph magic state。
6. 读 Appendix F：理解 $K_{\mathrm{CCZ}}$ 作为 tensor subrank 问题的定义，以及文中报告可找到下界的原因。
7. 读 Sec. 2.3 和 Appendix B：把 metachecks、single-shot distance 和 soundness 连成 state-preparation 保证。
8. 最后读 Sec. 2.4、Appendix G/H：把数值性能、postselection 和 syndrome extraction depth 当作 protocol feasibility，而不是理论构造本身。

---
### 与传统 distillation 的差别

传统 [[Reed-Muller码]] 或 triorthogonal protocol 的逻辑是：

$$
\text{noisy input magic states}
\xrightarrow{\text{Clifford checks + postselection}}
\text{fewer cleaner magic states}.
$$

Menon 的逻辑更像：

$$
\text{noisy physical }CCZ\text{ gates + qLDPC encoded }|+\rangle
\xrightarrow{\text{transversal logical action + QEC}}
\text{logical hypergraph magic states}.
$$

因此不能直接把 Table 1 里的 $N,K,D$ 读成传统 $n\to k$ distillation matrix 的 $n,k,d$。这里的核心资源量包括：

- 三个 code blocks，总 data qubits 约 $3N$；
- syndrome extraction ancillas 和 schedule depth；
- physical $CCZ$ circuit maximum degree / scheduled depth；
- 是否 postselect，以及接受率；
- 可抽取的 $K_{\mathrm{CCZ}}$，由 logical tensor subrank 决定；
- 最后如何把 logical magic state teleport 到目标计算码。

---
### 适用范围与失效模式

这篇文章给出了很强的 finite-block evidence，但使用时要保留几个边界条件。

第一，表中的 $CCZ$ circuit depth 常指 maximum degree。实际 schedule depth 由对应三部三均匀超图的 edge coloring 决定，文中主例 $[\![48,6,(8,4)]\!]$ 的 maximum degree 是 $8$，但找到的 minimal scheduled depth 是 $10$。错误扩散主要由 degree 控制，idle error 则受实际 schedule depth 影响。

第二，Sec. 2.4 的 circuit-level simulations 主要模拟 syndrome extraction / memory-style QEC 性能，并说明短 $CCZ$ circuit 下它是合理 proxy；文章明确把完整 logical $CCZ$ circuit fidelity simulation 留给未来工作。

第三，抽取 disjoint $CCZ$ resources 需要能把未使用 logical qubits 选择性初始化到 $|0\rangle$。对 qLDPC codes，这不是自动常深度操作；文章也把 selective initialization / teleportation 到目标 computation code 作为后续架构问题。

第四，NLR 是有用的数值构造技术，但对任意给定 code 不保证找到低 degree $f_{\mathrm{CCZ}}$。STCP 给出解析保证，但可能牺牲参数或 circuit degree。

第五，single-shot soundness 的严格证明覆盖特定子类和条件；文章的数值证据更广。读模拟图时要区分“已证明的 adversarial guarantee”和“特定 noise model 下的 Monte Carlo evidence”。

---
### 可作为后续笔记拆分的主题

- `Tricycle code`：专门整理 Eq. (1)、group-algebra construction、balanced-product complex 和距离不平衡 $D_Z\le D_X$。
- [[Cup product 与 Leibniz rule]]：整理 cup product 和 Leibniz rule 如何让乘法在 cohomology 上良定义。
- [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]：整理 classical seed complex 上的 in/out/free 分割、局部 cup product、seed integrated Leibniz 和 ordinary tensor-product 继承。
- [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]：整理 free $G^2$-作用、relative-translate inherited product、augmentation 与 balanced integrated-Leibniz 继承。
- [[Symmetric triple cup-product]]：单独整理 $\int_R$、symmetric integrated Leibniz、sector-dependent bracketing 和 Proposition 5 的 $f_{\mathrm{CCZ}}$。
- `Single-shot CCZ factory`：整理 metachecks、soundness、state preparation 和 $CCZ$ error propagation。
- `Hypergraph magic state`：说明 $T^{\mathrm{log}}$ tensor、subrank、$K_{\mathrm{CCZ}}$ 和 gauge logical initialization。

---
### 来源

- Varun Menon, J. Pablo Bonilla Ataides, Rohan Mehta, Andi Gu, Daniel Bochen Tan, Mikhail D. Lukin, [*Magic tricycles: Efficient magic state generation with finite block-length quantum LDPC codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), arXiv:2508.10714v2, 2025.
