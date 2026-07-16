Jacinto 等人的 SAT 搜索把 compact distillation factory 的存在性问题变成有限的 Boolean satisfiability problem(SAT)：给定工作 qubits 数 $N$、输入 $T$ resources 数 $n$ 和目标距离 $d$，问是否存在一组 Pauli product rotations，使它在 repetition code 上实现容错逻辑门，并在解码后成为 $nT\to1T$ 或 $nT\to1CCZ$ 的蒸馏线路。

本文只整理论文 Sec. V 的搜索框架和结果。canonical family 的解析反演见 [[Canonical distillation family]]；$\alpha\mapsto\beta$ 的线路变换见 [[重复码上的逻辑T门#$\alpha$ 条件如何变成 triorthogonal 条件]]。

---
### 无对称 SAT formulation

先考虑 $T$-state distillation。在线路空间中，一个候选 logical-$T$ circuit 是若干个 $\pi/8$ Pauli product rotations：

$$
P^k_{\pi/8}
=
\exp\left(-\frac{i\pi}{8}P^k\right),
\qquad
P^k\in\{I,Z\}^{\otimes N}.
$$

每个 rotation 用 support 向量表示：

$$
\alpha^k_i=
\begin{cases}
1, & (P^k)_i=Z,\\
0, & (P^k)_i=I.
\end{cases}
$$

共有 $2^N$ 个 possible supports。SAT 变量

$$
v_k\in\{0,1\}
$$

表示 support $\alpha^k$ 是否被选入线路。每个 support 至多出现一次：在论文使用的 normal form 中，所有 non-Clifford gates 都已经写成同一组 wires 上的 $Z$-type Pauli product rotations，它们彼此对易；同一个 support 出现两次只留下 Clifford correction。因此 SAT 只记录每个 support 是否出现奇数次。

如果原始线路中间夹着会改变 Pauli string 的 Clifford 层，应先把线路共轭回这种 Pauli-product normal form；SAT formulation 搜索的是 normal form 中的 support set，而不是任意交错 Clifford+$T$ 线路。于是列顺序不重要。

#### 逻辑门约束

要在 repetition code 上实现逻辑 $T_L$，每条线、每对线、每组三条线都必须被 selected supports 覆盖奇数次：

$$
\forall i\in[N],
\qquad
\bigoplus_{k:\alpha_i^k=1}v_k=1,
$$

$$
\forall i_1<i_2,
\qquad
\bigoplus_{k:\alpha_{i_1}^k=\alpha_{i_2}^k=1}v_k=1,
$$

$$
\forall i_1<i_2<i_3,
\qquad
\bigoplus_{k:\alpha_{i_1}^k=\alpha_{i_2}^k=\alpha_{i_3}^k=1}v_k=1.
$$

这些 XOR constraints 就是 Eq. (15) 的 Boolean-variable 版本。它们只保证线路实现逻辑 $T$ up to Clifford correction，还没有保证距离。

#### 距离约束

一个 faulty rotation 会留下它的 support 上的 $Z$ 错误。若一组 faulty supports 的异或为全 $1$，

$$
\bigoplus_{k\in K}\alpha^k=\mathbf1,
$$

则 repetition code 看不到 syndrome，产生逻辑 $\bar Z$。因此距离约束可以分两步理解。

先在全部 possible supports 中枚举坏集合：

$$
K\subseteq\{1,\ldots,2^N\},
\qquad
|K|<d_{\min},
\qquad
\bigoplus_{k\in K}\alpha^k=\mathbf1.
$$

这样的 $K$ 表示：如果这些 supports 都出现在候选线路里，并且它们同时发生 input magic-state error，就会用少于 $d_{\min}$ 个错误造成 undetected logical error。为了让 protocol 的距离至少为 $d_{\min}$，候选线路必须避免完整包含任何这样的坏集合。

SAT 变量 $v_k$ 表示 support $k$ 是否被选。于是对每个坏集合 $K$，加入 clause：

$$
\prod_{k\in K}v_k=0.
$$

这只是一个紧凑写法，意思是

$$
\text{not all of } \{v_k:k\in K\}\text{ are }1.
$$

等价地，至少有一个 support 没被选：

$$
\bigvee_{k\in K}\neg v_k.
$$

把“坏集合的判定”和“禁止同时选中”合在一起，就得到论文中的蕴含式：

$$
\forall K,\ |K|<d_{\min},
\quad
\left[
\bigoplus_{k\in K}\alpha^k=\mathbf1
\right]
\Longrightarrow
\prod_{k\in K}v_k=0.
$$

例如若三个 supports 满足

$$
\alpha^2\oplus\alpha^5\oplus\alpha^9=\mathbf1,
$$

而目标是 $d_{\min}>3$，就必须加入

$$
v_2v_5v_9=0,
$$

也就是禁止同时选择第 $2,5,9$ 三列。这个约束数量随 $d_{\min}$ 组合爆炸，是无对称搜索的主要瓶颈。

如果还想限制 T-count，可以加入

$$
\sum_k v_k\le n_{\max}.
$$

求解策略是固定 $N$ 和 $d_{\min}$，若 SAT 就得到一个候选 protocol；若 UNSAT，则证明在该变量空间中不存在距离至少 $d_{\min}$ 的线路。注意：timeout 或未找到解不是不存在性证明。

论文使用 z3 和 Google OR-Tools CP-SAT 实现。原则上也可以改用 [[Canonical distillation family]] 中的覆盖变量 $g(B)$，变量数会更少，但约束设计更复杂，且问题规模仍随 $N$ 组合增长。

---
### 小 $N$ 搜索结果

无对称 SAT 的第一个用途是确定小工作宽度下能达到的最大距离。

论文报告：

- $N=4$ 的最大距离为 $d=2$；
- $5\le N\le7$ 的最大距离为 $d=3$；
- $N=8,d_{\min}=4$ 的 UNSAT/SAT 判定在两个月运行后仍未收敛，因此没有给出严格不存在性证明；
- 在测试中，若存在满足解通常很快找到；$N=8,9$ 未找到 $d_{\min}=4$ 解，而 $N=10$ 找到距离 $4$ 的解，所以论文把 $N=10$ 视为首个已知 $d\ge4$ compact 宽度。

搜索到的代表 protocol 包括：

| 工作 qubits $N$ | protocol | distance | leading output error |
|---:|---:|---:|---:|
| $10$ | $165T\to1T$ | $4$ | $18900p_{\mathrm{in}}^4$ |
| $11$ | $165T\to1T$ | $5$ | $784245p_{\mathrm{in}}^5$ |

加入 T-count 上界后，SAT 还可用于寻找更小 $n$：

- 对 $N\le7$，可证明不存在 $n<15$ 的距离 $3$ T-state distillation protocol；
- 对 $N=10$，找到 $80T\to1T$、距离 $4$、$p_{\mathrm{out}}=1259p_{\mathrm{in}}^4$ 的 protocol；
- 对 $N=10$，论文报告在 $n<80$ 的搜索中一小时内未找到距离 $4$ 解，但这不是严格 UNSAT 证书；
- 对 $N=11$，无对称搜索没有在合理时间内进一步降低 T-count。

这些结果说明：无对称 SAT 在小 $N$ 上能给出存在性或不存在性信息，但很快受限于距离 clauses 的数量。

---
### 全排列对称子族 $F_{S_N}$

为了进入更大的 $N$，论文先考虑对所有 qubits 的排列都不变的子族。此时不再为每个 support 单独设变量，而是为每个 Hamming weight 设一个变量：

$$
w_k=
\begin{cases}
1, & \text{所有 weight-}k\text{ supports 都选入},\\
0, & \text{所有 weight-}k\text{ supports 都不选}.
\end{cases}
$$

若 $w_k=1$，则任意固定 qubit 被 weight-$k$ supports 覆盖的次数是

$$
\binom{N-1}{k-1}.
$$

任意固定 pair 被覆盖的次数是

$$
\binom{N-2}{k-2},
$$

任意固定 triplet 被覆盖的次数是

$$
\binom{N-3}{k-3}.
$$

只需保留奇偶，定义

$$
\ell_k=\binom{N-1}{k-1}\pmod2,
\qquad
p_k=\binom{N-2}{k-2}\pmod2,
\qquad
t_k=\binom{N-3}{k-3}\pmod2.
$$

逻辑 $T$ 条件变成三个 XOR constraints：

$$
\bigoplus_k w_k\ell_k=1,
\qquad
\bigoplus_k w_kp_k=1,
\qquad
\bigoplus_k w_kt_k=1.
$$

距离条件也大幅简化。由于每个 active weight class 中所有 supports 都存在，若能选出 $r$ 个 active weights

$$
k_1\le\cdots\le k_r,
\qquad
\sum_{j=1}^r k_j=N,
$$

就可以把它们安排成 disjoint supports，异或出全重 $\mathbf1$，从而形成逻辑错误。因此要求距离至少 $d_{\min}$ 时，要禁止所有 $r<d_{\min}$ 的这类组合：

$$
\prod_{j=1}^r w_{k_j}=0.
$$

T-count 约束为

$$
\sum_k w_k\binom Nk\le n_{\max}.
$$

这个子族变量少，论文搜索到 $N=23$。它达到的最大距离与 canonical family $F_N^0$ 相同，但它是严格受限的对称子族。例如 $N=6$ 时，$F_{S_N}$ 中没有距离 $3$ 的对称方案，而非对称地扩展 $15\to1$ protocol 可以做到。

---
### Young subgroup 子族 $F_Y$

全排列对称太强。下一步是只保留 block 内部的置换对称性。

先固定一个 block decomposition：

$$
[N]=I_1\sqcup I_2\sqcup\cdots\sqcup I_b,
\qquad
|I_i|=\lambda_i,
$$

其中

$$
\lambda=(\lambda_1,\ldots,\lambda_b),
\qquad
\sum_i\lambda_i=N.
$$

这里用 $b$ 表示 block 数，避免和前面表示 faulty support set 的 $K$ 混淆。

对应的 Young subgroup 是

$$
S_\lambda=S_{\lambda_1}\times\cdots\times S_{\lambda_b}
$$

也就是 $S_N$ 中保持每个 block 不变的子群：

$$
S_\lambda
=
\{\sigma\in S_N:\sigma(I_i)=I_i,\ \forall i\}.
$$

它允许在第 $i$ 个 block 内任意重排 qubits，但不允许把 qubit 从一个 block 移到另一个 block。若两个 block 大小相同，这里也默认不允许交换两个 block 本身；否则得到的是更大的 wreath-product 型对称性，而不是本文使用的 Young subgroup。

在全排列群 $S_N$ 下，一个 support $A\subseteq[N]$ 只由总重量 $|A|$ 分类；所有同重量 supports 都等价。在 Young subgroup 下，总重量不够了，因为 block 之间不能互换。真正的不变量是 block-wise weight vector：

$$
w(A)=
\bigl(|A\cap I_1|,\ldots,|A\cap I_b|\bigr).
$$

两个 supports $A,A'$ 在同一个 $S_\lambda$-orbit 中，当且仅当

$$
|A\cap I_i|=|A'\cap I_i|
\qquad(\forall i).
$$

因为在每个 block 内，可以分别找一个置换把 $A\cap I_i$ 映到 $A'\cap I_i$。因此 orbit 可以用

$$
w=(w_1,\ldots,w_b)
$$

标记，其中 $w_i$ 表示从第 $i$ 个 block 中选了多少条线。

对固定 $w$，第 $i$ 个 block 有 $\lambda_i$ 条线，从中选 $w_i$ 条有 $\binom{\lambda_i}{w_i}$ 种选择；不同 block 独立，所以 orbit 大小为

$$
|\operatorname{Orb}(w)|
=
\prod_i\binom{\lambda_i}{w_i}.
$$

从 $S_N$ 到 $S_\lambda$ 的效果，是把一个总重量为 $r$ 的 full-symmetry orbit 细分为多个 block-weight orbits：

$$
\binom Nr
=
\sum_{w_1+\cdots+w_b=r}
\prod_i\binom{\lambda_i}{w_i}.
$$

SAT 变量 $v_w$ 表示是否选入整个 orbit。全零 support 和全一 support 通常排除：前者没有 non-Clifford 作用，后者会直接制造距离 $1$ 逻辑错误。

#### 逻辑门约束

大小为 $t\in\{1,2,3\}$ 的检查集合也按 block 分成类型

$$
\tau=(\tau_1,\ldots,\tau_b),
\qquad
\sum_i\tau_i=t.
$$

对于固定类型 $\tau$，orbit $w$ 中有多少 supports 覆盖这个检查集合，只取决于 $\tau$ 和 $w$，其奇偶为

$$
c_{\tau,w}
=
\prod_{i=1}^b
\binom{\lambda_i-\tau_i}{w_i-\tau_i}
\pmod2.
$$

于是每个类型 $\tau$ 给出一个 XOR constraint：

$$
\bigoplus_{w:c_{\tau,w}=1}v_w=1.
$$

这比无对称 SAT 少了许多变量和约束，同时比 $F_{S_N}$ 允许更多非对称结构。

#### 距离和 T-count

距离约束仍然是禁止少于 $d_{\min}$ 个 selected orbits 组合出全重逻辑错误。这里的

$$
w^{(j)}=(w^{(j)}_1,\ldots,w^{(j)}_b)
$$

表示第 $j$ 个 faulty gate 的 support 在各个 block 中分别占了多少条线。更具体地说，第 $j$ 个 faulty gate 对应某个实际 support $A^{(j)}\subseteq[N]$，但在 Young subgroup 对称下，不区分 block 内的具体 qubit 标签，只记录

$$
w^{(j)}_i=|A^{(j)}\cap I_i|.
$$

因此 $w^{(j)}$ 不是某一列的完整 support，而是这列 support 所在的 orbit label：所有满足同一个 block-wise weight vector 的 supports 被视为同一类。$v_{w^{(j)}}$ 是这个 orbit 是否被整体选入线路的 SAT 变量。写成 multiset 是因为同一个 orbit label 可以被多次使用：实际线路里包含该 orbit 的所有 supports，两个不同 faulty gates 可以来自同一个 orbit 中的两列。

形式上，若某个 orbit-label multiset

$$
\{w^{(1)},\ldots,w^{(r)}\}
$$

可以在每个 block 内选出实际 supports，使它们的异或覆盖该 block 的全部 $\lambda_i$ 个 qubits，则对应 clause 为

$$
\prod_{j=1}^r v_{w^{(j)}}=0
\qquad(r<d_{\min}).
$$

T-count 是所有 selected orbits 的大小之和：

$$
n=
\sum_w v_w
\prod_i\binom{\lambda_i}{w_i}.
$$

论文枚举 $N$ 的 partitions：先找各 partition 的最大距离，再在达到全局最大距离的 partitions 中迭代降低 $n_{\max}$。这个子族包含全排列对称情形，并能恢复 $N\ge5$ 时的 $15\to1$ protocol。它还把 $N=10,d=4$ 的一个方案从 $n=165$ 降到 $n=164$。

---
### Cyclic subgroup 子族 $F_C$

Young subgroup 仍然要求 block 内全排列不变。Cyclic subgroup 子族进一步放松为每个 block 内只要求循环平移不变：

$$
C_\lambda=C_{\lambda_1}\times\cdots\times C_{\lambda_b}.
$$

由于

$$
C_{\lambda_i}\subseteq S_{\lambda_i},
$$

这个子族更大，论文构造使

$$
F_Y\subseteq F_C.
$$

此时 orbit 不再由 block 内 Hamming weights 唯一决定；同样重量的 binary pattern 可能不在同一个 cyclic orbit。对一个 support $\alpha$，

$$
\operatorname{Orb}(\alpha)
=
\{\sigma\cdot\alpha:\sigma\in C_{\lambda_1}\times\cdots\times C_{\lambda_b}\}.
$$

SAT 变量 $v_s$ 表示是否选入 orbit $s$。对一个检查集合 $B$，orbit $s$ 的贡献奇偶是

$$
c_{B,s}
=
\left|
\{\alpha\in\operatorname{Orb}(s):B\subseteq\operatorname{supp}(\alpha)\}
\right|
\pmod2.
$$

因此每个 qubit-subset orbit 的代表 $B$ 给出

$$
\bigoplus_{s:c_{B,s}=1}v_s=1
\qquad(|B|=1,2,3).
$$

距离约束也按 orbit-label multiset 写：若可以从 $r<d_{\min}$ 个 selected orbits 中各取一列，使这些列异或为 $\mathbf1$，则禁止这些 orbits 同时被选：

$$
\prod_{j=1}^r v_{s_j}=0.
$$

T-count 是

$$
n=\sum_s v_s|\operatorname{Orb}(s)|.
$$

$F_C$ 的 SAT instance 比 $F_Y$ 大，但能找到更低 T-count 的方案。论文报告：

| 工作 qubits $N$ | protocol | distance | leading output error |
|---:|---:|---:|---:|
| $10$ | $64T\to1T$ | $4$ | $495p_{\mathrm{in}}^4$ |
| $11$ | $65T\to1T$ | $5$ | $7947p_{\mathrm{in}}^5$ |

这些矩阵列在论文 Appendix D。这里的重点不是具体矩阵，而是：弱化对称性会增大搜索空间，但可能显著降低 T-count。

---
### 扩展到 $CCZ$ factories

许多整数算术子程序由 Toffoli/CCZ 主导。一个 Toffoli 可由一个 $|CCZ\rangle$ 消耗实现，因此直接蒸馏 $CCZ$ states 可能比先蒸馏 $T$ states 再综合 Toffoli 更合适。

论文把 repetition-code 搜索框架改成 $nT\to1CCZ$。坐标约定是：

- qubits $1,2$ 是 $CCZ$ 的前两个输入，不用 repetition code 保护；
- qubits $3,\ldots,N$ 是第三个输入的 phase-flip repetition block；
- 第三个逻辑 qubit 的 $X$-basis repetition codewords 为

$$
|+_L\rangle=|+\rangle_3\cdots|+\rangle_N,
\qquad
|-_L\rangle=|-\rangle_3\cdots|-\rangle_N.
$$

也就是说，$CCZ_L$ 的目标是对 qubits $1,2$ 和第三个逻辑 qubit 施加

$$
CCZ_{1,2,L}.
$$

若采用 decode--gate--encode 的朴素写法，就是先用 $E^\dagger$ 把 repetition block 解码到第 $3$ 条线，在 qubits $1,2,3$ 上施加 $CCZ_{1,2,3}$，再用 $E$ 编码回去。

为了得到容错的对角门层，论文把 $CCZ_{1,2,3}$ 交换过解码 CNOT ladder。解码 ladder 的作用是把逻辑 $Z_L$ 转成第一条 block 线上的 $Z_3$；反过来，把 $Z_3$ 共轭回编码空间会变成全重逻辑

$$
Z_L=Z_3Z_4\cdots Z_N.
$$

因此一个只在第 $3$ 条 block 线参与的三体相位，在编码空间中等价于让 qubits $1,2$ 与 block 中每一条线都参与一次三体相位：

$$
CCZ_{1,2,L}
\quad\leadsto\quad
\prod_{l=3}^{N}CCZ_{1,2,l}.
$$

也可以直接从计算基相位看：$CCZ_{1,2,l}$ 在 $x_1=x_2=x_l=1$ 时给 $-1$。乘积

$$
\prod_{l=3}^{N}CCZ_{1,2,l}
$$

给出的相位是

$$
(-1)^{x_1x_2(x_3+\cdots+x_N)}
=
(-1)^{x_1x_2(x_3\oplus\cdots\oplus x_N)}.
$$

这里指数只看模 $2$，而 $x_3\oplus\cdots\oplus x_N$ 正是 repetition block 解码到逻辑线后的 bit。于是这个门层实现了 qubits $1,2$ 与第三个逻辑 qubit 之间的 $CCZ$。

还要禁止只作用在未保护 qubits $1,2$ 上的 Pauli product rotations：这类错误不会进入 repetition syndrome，无法通过第三个 block 的检查检测出来。

仍用 support 向量 $\alpha^k\in\mathbb F_2^N$ 表示每个 Pauli product rotation。若 Clifford corrections 视为免费，正确实现 $CCZ_L$ 的约束化为

$$
\forall i\in[N],
\qquad
\sum_k\alpha_i^k\equiv0\pmod2,
$$

$$
\forall i<j\in[N],
\qquad
\sum_k\alpha_i^k\alpha_j^k\equiv0\pmod2,
$$

$$
\forall l\in\{3,\ldots,N\},
\qquad
\sum_k\alpha_1^k\alpha_2^k\alpha_l^k
\equiv1\pmod2,
$$

$$
\forall 3\le i<j<l\le N,
\qquad
\sum_k\alpha_i^k\alpha_j^k\alpha_l^k
\equiv0\pmod2.
$$

前两行去掉不想要的单体和二体相位；第三行保留目标 $CCZ_{1,2,l}$；第四行避免在 repetition block 内产生额外三体相位。

距离条件比 $T$-state case 更复杂。$T$ distillation 中，坏错误只对应全重 $\mathbf1$。这里未检测逻辑错误可以是前两个 unprotected qubits 上的任意非零 $Z$ 图样，也可以伴随 repetition block 的全重逻辑 $Z$。论文把七种非零图样写成

$$
\mathcal E
=
\{(a,b,c,c,\ldots,c):
(a,b,c)\in\mathbb F_2^3\setminus\{(0,0,0)\}\}.
$$

于是距离定义为

$$
d=
\min_K |K|
\quad\text{s.t.}\quad
\bigoplus_{k\in K}\alpha^k=e,
\qquad
e\in\mathcal E.
$$

SAT 搜索只需把 $T$ case 中的逻辑门约束和坏错误集合替换为上面两组条件。论文报告：

- $N<8$ 时不存在距离 $>2$ 的 $nT\to1CCZ$ protocol；
- $N=9$ 时找到 $47T\to1CCZ$，$p_{\mathrm{out}}=236p_{\mathrm{in}}^3$；
- $N=10$ 时找到 $48T\to1CCZ$，$p_{\mathrm{out}}=2816p_{\mathrm{in}}^4$。

这与 $T$-state 搜索形成对比：论文观察到 $T$ protocols 的较好 plateau 常出现在奇数距离，而 $CCZ$ protocols 的 plateau 更偏向偶数距离。

---
### 适用范围与失效模式

这些 SAT 结果描述的是 abstract compact distillation circuit，而不是完整硬件 factory：

- $N$ 是长期保存的 logical work qubits 数；
- $n$ 是 selected Pauli product rotations 数，也就是消耗的 noisy $T$ resources 数；
- $d$ 是输入 magic-state stochastic $Z$ error 的 leading-order 抑制阶数；
- $C$ 是 malignant weight-$d$ sets 的数量，决定 $p_{\mathrm{out}}=Cp_{\mathrm{in}}^d+O(p_{\mathrm{in}}^{d+1})$ 的前因子。

它们没有自动计入 lattice surgery rounds、routing、idle errors、measurement faults、decoder failure、factory warm-up 或 correlated faults。若底层 Clifford 层和测量不再理想，SAT 中的距离不是完整 surface-code factory 的 logical failure rate。

SAT 的结论也要区分：

- SAT：给出一个存在性构造；
- UNSAT：在给定变量空间、约束和距离下证明不存在；
- timeout 或未找到解：只说明当前搜索没有成功，不是不存在性证明。

---
### 连接

- [[Canonical distillation family]]：给出不用 SAT 的解析 family，并解释 support coverage 与 Möbius 反演。
- [[重复码上的逻辑T门]]：说明逻辑 $T$ 线路如何变成 compact distillation matrix。
- [[Distillation protocol]]：把 SAT 得到的矩阵解释成 triorthogonal distillation protocol，并区分 $n$、$N_{\mathrm{reg}}$、yield 和 output error。
- [[State injection]]：说明每个 Pauli product rotation 如何消耗 noisy magic state，并把主要错误化为 $Z$ 型输出错误。

---
### 来源

- H. Jacinto, X. Valcarce, V. Barizien, É. Gouzien, and N. Sangouard, [*Exploring the landscape of compact magic-state distillation factories*](<../../Papers/S001_2026_Jacinto_compact_magic_state_factories.pdf>), arXiv:2606.07734 (2026), Sec. V.
