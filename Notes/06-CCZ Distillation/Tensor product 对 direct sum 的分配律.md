本文只记录一个线性代数事实：普通 tensor product 与 direct sum 相容。它只说明对象空间如何分块；graded vector space、total degree 和 coboundary map 见 [[Cochain complex 的 tensor product]]。

---
### 命题

固定一个域 $k$；下文所有 vector spaces 和 tensor products 都在 $k$ 上。本库的二进制 cochain complex 例子通常取 $k=\mathbb F_2$。

设 $C,D$ 是 $k$-vector spaces，并给定 direct sum 分解

$$
C=\bigoplus_{i\in I}C^i,
\qquad
D=\bigoplus_{j\in J}D^j.
$$

则有自然同构

$$
C\otimes_k D
\cong
\bigoplus_{(i,j)\in I\times J} C^i\otimes_k D^j.
$$

若 $I$ 或 $J$ 是无限集合，direct sum 的定义保证每个 $c\in C$ 和 $d\in D$ 只有有限多个非零分量：

$$
c=\sum_i c_i,\qquad d=\sum_j d_j.
$$

因此后面出现的 $\sum_{i,j}$ 都是有限和。

---
### Direct sum、direct product 与 tensor product

有限多个分量时，外部 direct sum 和 direct product 没有本质区别。对两个 vector spaces 或 modules $A,B$，

$$
A\oplus B=\{(a,b):a\in A,\ b\in B\}
\cong
A\times B.
$$

差别只在无限多个分量时出现：

$$
\bigoplus_{i\in I}V_i
=
\left\{(v_i)_{i\in I}\in\prod_{i\in I}V_i:
\text{只有有限多个 }v_i\ne0
\right\},
$$

而

$$
\prod_{i\in I}V_i
=
\left\{(v_i)_{i\in I}:v_i\in V_i\right\}.
$$

普通代数中的线性组合默认是有限和。Direct sum 因此是有限线性组合空间；例如

$$
\bigoplus_{n\in\mathbb N}k
$$

包含 $(1,0,3,0,\ldots)$，但不包含 $(1,1,1,\ldots)$。若要允许

$$
\sum_{n=0}^{\infty}a_ne_n,
$$

需要额外给出拓扑、收敛或完备化结构。

Direct product 的功能不同：它保存所有坐标族，不要求把这些坐标解释成无限和。这个区别也体现在泛性质上。Direct sum 适合把一族从分量出发的映射拼成一个映射

$$
f:\bigoplus_iV_i\to U,
\qquad
f((v_i)_i)=\sum_i f_i(v_i),
$$

其中右边因为有限支撑而总是有限和。Direct product 适合把到各个分量的映射收集成一个映射

$$
g:U\to\prod_iV_i,
\qquad
g(u)=(g_i(u))_{i\in I}.
$$

这里没有无限求和，只是收集坐标。

Tensor product 是另一种构造。$A\otimes B$ 不是保存 pair $(a,b)$ 的空间，而是由符号 $a\otimes b$ 生成，并强制满足双线性关系

$$
(a+a')\otimes b=a\otimes b+a'\otimes b,
\qquad
a\otimes(b+b')=a\otimes b+a\otimes b'.
$$

它的泛性质是

$$
\operatorname{Hom}(A\otimes B,U)
\cong
\operatorname{Bilin}(A\times B,U).
$$

因此 direct sum / direct product 保存的是并列分量；tensor product 保存的是两个方向之间的双线性配对。若 $\dim A=2$、$\dim B=3$，则

$$
\dim(A\oplus B)=5,
\qquad
\dim(A\otimes B)=6,
$$

因为 $A\otimes B$ 的基方向来自所有 $e_i\otimes f_j$。

---
### Direct sum 的包含和泛性质

对 direct sum

$$
C=\bigoplus_{i\in I}C^i,
$$

每个 summand 有一个 canonical inclusion

$$
\iota_i:C^i\to C,
$$

定义为把 $x\in C^i$ 放到第 $i$ 个分量，其它分量取 $0$。也有 canonical projection

$$
p_i:C\to C^i,
$$

定义为取第 $i$ 个分量。它们满足

$$
p_i\iota_{i'}=
\begin{cases}
\mathrm{id}_{C^i}, & i=i',\\
0, & i\ne i'.
\end{cases}
$$

Direct sum 的泛性质是：若 $T$ 是任意 vector space，并且对每个 $i$ 给定线性映射

$$
f_i:C^i\to T,
$$

则存在唯一线性映射

$$
f:\bigoplus_i C^i\to T
$$

满足 $f\iota_i=f_i$。具体地，

$$
f\left(\sum_i\iota_i(c_i)\right)
=
\sum_i f_i(c_i).
$$

右边是有限和。这就是后面把所有 summand 上的映射合成一个 $\Phi$ 的理由。

---
### 正向映射

沿用上节的包含映射。对 $D=\bigoplus_jD^j$ 的 summands，记对应包含映射为

$$
\kappa_j:D^j\hookrightarrow D.
$$

对每对 $(i,j)$，先定义双线性映射

$$
C^i\times D^j
\longrightarrow
C\otimes_k D,
\qquad
(c_i,d_j)
\longmapsto
\iota_i(c_i)\otimes \kappa_j(d_j).
$$

由 tensor product 的泛性质，它唯一诱导出线性映射

$$
\iota_i\otimes\kappa_j:
C^i\otimes_k D^j
\longrightarrow
C\otimes_k D.
$$

接着，由 direct sum 的泛性质，这些线性映射唯一合成一个线性映射

$$
\Phi:
\bigoplus_{i,j} C^i\otimes_k D^j
\longrightarrow
C\otimes_k D,
$$

满足

$$
\Phi(c_i\otimes d_j)=c_i\otimes d_j.
$$

这里右边把 $c_i,d_j$ 通过包含映射视为 $C,D$ 中的向量。

---
### 反向映射

记投影映射为

$$
p_i:C\to C^i,
\qquad
q_j:D\to D^j.
$$

定义双线性映射

$$
B:C\times D\to
\bigoplus_{i,j} C^i\otimes_k D^j
$$

为

$$
B(c,d)=\sum_{i,j}p_i(c)\otimes q_j(d).
$$

由 tensor product 的泛性质，$B$ 唯一诱导出线性映射

$$
\Psi:
C\otimes_k D
\longrightarrow
\bigoplus_{i,j} C^i\otimes_k D^j
$$

满足

$$
\Psi(c\otimes d)
=
\sum_{i,j}p_i(c)\otimes q_j(d).
$$

---
### 互为逆映射

对 $c_i\in C^i$、$d_j\in D^j$，

$$
\Psi\Phi(c_i\otimes d_j)
=
\sum_{i',j'}p_{i'}(c_i)\otimes q_{j'}(d_j)
=
c_i\otimes d_j.
$$

所以 $\Psi\Phi=\mathrm{id}$。

反过来，若

$$
c=\sum_i c_i,\qquad d=\sum_j d_j,
$$

则

$$
\Phi\Psi(c\otimes d)
=
\sum_{i,j}c_i\otimes d_j
=
\left(\sum_i c_i\right)\otimes
\left(\sum_j d_j\right)
=
c\otimes d.
$$

简单张量生成 $C\otimes_k D$，所以 $\Phi\Psi=\mathrm{id}$。因此

$$
C\otimes_k D
\cong
\bigoplus_{i,j}C^i\otimes_k D^j.
$$

这个同构只使用 direct sum 的包含映射和投影映射，因此不依赖基的选择。

---
### 到 cochain tensor product 的接口

若 $C,D$ 进一步是 cochain complexes，上面的同构只给出双指标分块：

$$
C\otimes_k D
\cong
\bigoplus_{i,j}C^i\otimes_k D^j.
$$

要把它变成一个新的 cochain complex，还需要额外定义：

$$
(C\otimes D)^n
=
\bigoplus_{i+j=n}C^i\otimes D^j,
$$

以及 tensor-product coboundary map。这些属于 [[Cochain complex 的 tensor product]]，不属于本文的普通 direct-sum 分解。

---
### 适用范围

- 本文只使用 $k$-vector spaces；本库主要取 $k=\mathbb F_2$。
- 对模块也有类似结论，但需要先固定张量积所在的环以及左右模结构。
- 若把 direct sum 换成 direct product，无限情形下不能直接使用上面的有限分量展开。
