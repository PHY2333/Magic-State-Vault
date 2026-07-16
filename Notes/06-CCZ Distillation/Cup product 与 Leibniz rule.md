Cup product 的本质是把几个 cochain 的坐标按局部规则相乘，产生新的 cochain。这个新的cochain作用在chain上可以得到二进制数，这个数等价于局部对角门作用在physical qubit上产生的相位的指数。若把这个cochain的坐标视作布尔函数，则这个函数对应于我们想要得到的门。

Cup product在流程上先给出一组局部坐标；再选一个线性泛函 $\lambda:C^r\to\mathbb F_2$，把这些坐标读成总 phase exponent。这里的 $r$ 是当前构造实际读取的 cochain layer；换门型时，$r$ 可以变。普通 degree-additive 规则下，三个 $C^1$ cochain 的 cup product 落在 $C^3$，对应CCZ；两个$C^{1}$cochain的cup product落在$C^{2}$,对应CZ。

---
### $C^1$ 作为 bit vector

在 [[CSS码中的cochain complex]] 的约定下，$C^1$ 是 physical support 空间。取一组 basis

$$
\{e_q:q\in Q\},
$$

其中 $Q$ 是 physical qubit labels。于是

$$
C^1=\mathbb F_2^Q.
$$

任意

$$
x\in C^1
$$

都可以唯一写成

$$
x=\sum_{q\in Q}x_q e_q,
\qquad
x_q\in\mathbb F_2.
$$

也就是一个 bit vector：

$$
x=(x_q)_{q\in Q}.
$$

在 CSS 读法中，$x_q=1$ 表示 support 包含 qubit $q$，$x_q=0$ 表示不包含。也就是说，$x$ 同时可以看成 subset

$$
\operatorname{supp}(x)=\{q\in Q:x_q=1\}
$$

的 indicator function。

在 $\mathbb F_2$ 中，加法是 XOR，乘法是 AND：

$$
a+b=a\oplus b,
\qquad
ab=
\begin{cases}
1,&a=1,\ b=1,\\
0,&\text{otherwise}.
\end{cases}
$$

因此，后面看到 $x_i y_j$ 或 $x_i y_j z_k$ 时，先把它读成几个 bit 坐标同时为 $1$ 的局部条件；看到若干项相加时，读成这些局部条件的奇偶。

---
### Cup product 的坐标与相位读数

Cup product 不是先给一个数，而是先给新的 cochain。选定 bases 后，可以写

$$
C^p=\mathbb F_2^I,
\qquad
C^q=\mathbb F_2^J,
\qquad
C^{p+q}=\mathbb F_2^K.
$$

若

$$
x=(x_i)_{i\in I}\in C^p,
\qquad
y=(y_j)_{j\in J}\in C^q,
$$

cup product作为双线性映射：

$$
C^p\times C^q\to C^{p+q}
$$

在第 $k\in K$ 个坐标上一定具有形式

$$
(x\cup y)_k
=
\sum_{i\in I,\ j\in J}c_{kij}x_i y_j,
\qquad
c_{kij}\in\mathbb F_2.
$$

这是选定 bases 后的坐标表达。乘积 $x_i y_j$ 是 AND，外面的求和是 XOR。若 cup product 是局部定义的，那么固定 $k$ 后，只有少数相关的 $(i,j)$ 会有

$$
c_{kij}=1.
$$

最简单的情形是单项式

$$
(x\cup y)_k=x_i y_j.
$$

复杂一些时会是几个局部项的异或：

$$
(x\cup y)_k=x_i y_j+x_{i'}y_{j'}.
$$

所以 $x\cup y$ 的每个坐标都是一个局部 bit。若把

$$
\alpha=x\cup y\in C^{p+q}
$$

的第 $k$ 个坐标 $\alpha_k$ **用作**局部 $(-1)$ 相位门的 exponent，则这个局部门给出

$$
(-1)^{\alpha_k}.
$$

所有局部相位相乘时，exponent 相加：

$$
\prod_{k\in K}(-1)^{\alpha_k}
=
(-1)^{\sum_{k\in K}\alpha_k}.
$$

指数的加法在 $\mathbb F_2$ 中计算，所以只保留触发了多少个局部 $(-1)$ 的奇偶。于是 parity-sum 读数

$$
\lambda:C^{p+q}\to\mathbb F_2,
\qquad
\lambda(\alpha)=\sum_{k\in K}\alpha_k\pmod2
$$

把这组局部坐标读成总 phase exponent：

$$
(-1)^{\lambda(\alpha)}.
$$

三重 cup product 同理，但括号要写在公式里。若先乘 $x$ 与 $y$，再把结果乘上 $z$，则第 $s$ 个坐标可以写成

$$
((x\cup y)\cup z)_s
=
\sum_{u,\ell}e_{su\ell}(x\cup y)_u z_\ell
=
\sum_{u,\ell,i,j}e_{su\ell}c_{uij}x_i y_j z_\ell.
$$

最后一项仍是三次坐标多项式；括号选择被中间指标 $u$ 记录下来。若改用 $x\cup(y\cup z)$，中间坐标和系数会换成另一组。

普通 degree-additive 规则下，三个 $C^1$ cochain 的 cup product 落在 $C^3$。

---
### Logical classes 与 representative

在 CSS 语境中，logical $X$ classes 是

$$
H^1(C)=\ker\delta^1/\operatorname{im}\delta^0.
$$

若 representatives 为

$$
x,y,z\in\ker\delta^1,
$$

同一个 logical class 还可以由

$$
x+\delta^0u
$$

表示。物理上这是把 logical $X$ support 乘上一个 $X$ stabilizer support；logical construction 不能依赖这种 representative 的选择。

Cup product 为了保证取泛函后的 coboundary invariance，必须是 cohomology 上的乘法。二元情形的目标是定义

$$
H^p(C)\times H^q(C)\to H^{p+q}(C),
\qquad
([x],[y])\mapsto [x\cup y].
$$

为了让这个定义成立，需要两件事：

$$
x,y\text{ 是 cocycles}
\quad\Longrightarrow\quad
x\cup y\text{ 是 cocycle},
$$

以及 representative 改变时，$x\cup y$ 的 cohomology class 不变。Leibniz rule 正是检查这两件事的条件。

---
### Leibniz rule

前面把 cup product 写成双线性映射

$$
\cup_{p,q}:C^p\times C^q\to C^{p+q}.
$$

双线性映射可以等价地先经过 tensor product。也就是说，存在唯一的线性映射

$$
m_{p,q}:C^p\otimes C^q\to C^{p+q}
$$

满足

$$
m_{p,q}(x\otimes y)=x\cup y.
$$

把所有 $(p,q)$ 合在一起，得到保持 total degree 的线性映射

$$
m:C\otimes C\to C,
\qquad
m|_{C^p\otimes C^q}=m_{p,q}.
$$

Leibniz rule 说的就是这个乘法映射 $m$ 与 coboundary map 相容。[[Cochain complex 的 tensor product]] 中有 Koszul sign rule，对 homogeneous elements $x\in C^p$、$y\in C^q$，

$$
\delta_{C\otimes C}(x\otimes y)
=
\delta x\otimes y
+
(-1)^p x\otimes\delta y.
$$

若这个 $m$ 与 coboundary map 相容，即

$$
\delta_C\,m(x\otimes y)
=
m\bigl(\delta_{C\otimes C}(x\otimes y)\bigr),
$$

代入 tensor-product coboundary，得到

$$
\delta(x\cup y)
=
(\delta x)\cup y
+
(-1)^p x\cup(\delta y),
\qquad x\in C^p.
$$

左右两边都属于 $C^{p+q+1}$。在 $\mathbb F_2$ 系数下，$-1=1$，公式简化为

$$
\delta(x\cup y)
=
(\delta x)\cup y
+
x\cup(\delta y).
$$

这个简化依赖特征 $2$；一般系数下必须保留 Koszul sign。

---
### Cocycles 与 representatives

Leibniz rule 首先说明 cocycles 的乘积仍是 cocycle。若

$$
x\in\ker\delta^p,
\qquad
y\in\ker\delta^q,
$$

则 $\delta x=0$ 且 $\delta y=0$。代入 Leibniz rule：

$$
\delta(x\cup y)
=
(\delta x)\cup y
+
(-1)^p x\cup(\delta y)
=0.
$$

因此

$$
x\cup y\in\ker\delta^{p+q}.
$$

还要检查 class 不依赖 representatives。先改变第一个 representative：

$$
x'=x+\delta^{p-1}u,
\qquad
u\in C^{p-1}.
$$

由于 $\delta^2=0$，

$$
\delta x'=\delta x+\delta^2u=0,
$$

所以 $x'$ 仍是 cocycle。乘积改变为

$$
x'\cup y-x\cup y
=
(\delta u)\cup y.
$$

因为 $y$ 是 cocycle，对 $u\cup y$ 使用 Leibniz rule：

$$
\delta(u\cup y)
=
(\delta u)\cup y
+
u\cup(\delta y)
=
(\delta u)\cup y.
$$

所以

$$
x'\cup y-x\cup y
=
\delta(u\cup y)
\in\operatorname{im}\delta^{p+q-1}.
$$

改变第一个 representative 只会让乘积增加一个 coboundary。

同理改变第二个 representative也只会让乘积增加一个 coboundary。

于是 cup product 诱导出 cohomology 上的乘法

$$
H^p(C)\times H^q(C)\to H^{p+q}(C),
\qquad
([x],[y])\mapsto [x\cup y].
$$

之后写

$$
[x]\cup[y]=[x\cup y]
$$

时，使用的正是 cocycle 封闭性和 representative invariance。

---
### 多重乘积与泛函的良定义

固定括号后，二元结论可以迭代使用。例如对

$$
x,y,z\in C^1
$$

的 cocycle representatives，若采用括号

$$
(x\cup y)\cup z,
$$

则先由 $x,y$ 得到

$$
[x]\cup[y]=[x\cup y]\in H^2(C),
$$

再与 $[z]$ 相乘，得到

$$
([x]\cup[y])\cup[z]
=
[(x\cup y)\cup z]\in H^3(C).
$$

这里没有假设 cup product 结合，只是在固定括号后反复使用二元结论。上式中的 $C^3$ 来自普通 degree-additive 规则：三个 $1$-cochains 相乘的代数 degree 为 $3$。

这仍然不是一个 $\mathbb F_2$ 数。若某个 diagonal phase 构造需要把某层 cochain 读成数值相位，还要另外选择泛函

$$
\lambda:C^r\to\mathbb F_2.
$$

这里的 $r$ 表示该构造实际读取的 cochain layer；它不改变前面的 degree-additive cup product。普通三重 $C^1$ cup product 仍然落在 $C^3$。Menon tricycle 的 $\int_R$ 则属于自己的符号约定。

若这个数值读数要只依赖 $H^r(C)$ 中的 cohomology class，还需要

$$
\lambda(\operatorname{im}\delta^{r-1})=0.
$$

这个条件不由 cup product 的 Leibniz rule 自动给出；它是把 cochain 或 cohomology class 进一步读成数值相位时需要检查的条件。Seed integral、preorientation 局部读数和 ordinary tensor-product integrated Leibniz 见 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]；balanced quotient 上的 relative-translate 继承见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；Menon 的具体 $\int_R$ 和 physical $CCZ$ 判据见 [[Symmetric triple cup-product]]。

---
### 来源

- Allen Hatcher, [*Algebraic Topology*](<https://pi.math.cornell.edu/~hatcher/AT/AT.pdf>), Section 3.2, Lemma 3.6：标准 cup product 和 coboundary formula。
- Varun Menon, J. Pablo Bonilla Ataides, Rohan Mehta, Andi Gu, Daniel Bochen Tan, Mikhail D. Lukin, [*Magic tricycles: Efficient magic state generation with finite block-length quantum LDPC codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), arXiv:2508.10714v2, Appendix D：STCP、integrated Leibniz 和 Proposition 5 的下游构造。
- [[Chain complex 与 cochain complex]]：cocycle、coboundary 和 cohomology quotient。
- [[Cochain complex 的 tensor product]]：total degree 和 Koszul sign 约定。
- [[CSS码中的cochain complex]]：$C^1$ 作为 physical support 空间、$H^1(C)$ 作为 logical $X$ support quotient。
