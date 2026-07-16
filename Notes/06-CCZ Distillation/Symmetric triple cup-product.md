[[Tricycle complex 的 balanced-product 构造]] 已经给出 Menon tricycle code 的四项 cochain complex

$$
C^0=R,
\qquad
C^1=R^3,
\qquad
C^2=R^3,
\qquad
C^3=R,
\qquad
R=\mathbb F_2[G],
$$

其中 $G$ 是有限 Abelian 群。[[Balanced quotient 上的 inherited product 与 integrated Leibniz]] 进一步从三个 classical seed 的 symmetric local products 构造出 balanced complex 上的 degree-additive trilinear operation

$$
\mu_C:C^{\times3}\longrightarrow C
$$

以及 $C^3\cong R$ 上的 integral $\lambda_C$。本笔记讨论复合

$$
f_{\mathrm{CCZ}}
=
\lambda_C\circ
\left.\mu_C\right|_{(C^1)^{\times3}}
:
(C^1)^{\times3}\longrightarrow\mathbb F_2.
$$

它在 physical-qubit basis 上决定 $CCZ$ hyperedges；symmetric integrated Leibniz 则保证它只依赖 $H^1(C)$ 中的 logical classes。

---
### Tricycle 上的三线性相位

由 total-degree decomposition，

$$
C^1
=
R_{100}\oplus R_{010}\oplus R_{001}.
$$

把这三个 summands 依次记为 sectors

$$
\mathrm I,\qquad \mathrm {II},\qquad \mathrm {III},
$$

并记相应的 constituent seed elements 为

$$
\alpha_{\mathrm I}=a,
\qquad
\alpha_{\mathrm {II}}=b,
\qquad
\alpha_{\mathrm {III}}=c.
$$

Sector 是 $C^1$ 的 total-degree summand，不是 classical seed complex 本身。固定 group basis $G$ 后，sector $i$ 中 coordinate $p\in G$ 对应的 physical-qubit basis cochain 记为

$$
p_i,
\qquad
p\in G,
\quad
i\in\{\mathrm I,\mathrm {II},\mathrm {III}\}.
$$

三个输入 $p_i,q_j,r_k$ 分别属于同一 code 的三个 blocks 的 $C^1$；下标 $i,j,k$ 标记 sectors，$p,q,r$ 标记各 sector 内的 group coordinates。

Total degree 为 $3$ 的部分是

$$
C^3=R_{111}\cong R.
$$

在这个同构下，$\lambda_C$ 是 group-algebra augmentation

$$
\lambda_C=\int_R,
\qquad
\int_R\left(\sum_{h\in G}v_hh\right)
=
\sum_{h\in G}v_h
\pmod2.
$$

因此

$$
f_{\mathrm{CCZ}}(p_i,q_j,r_k)
=
\int_R\mu_C(p_i,q_j,r_k)
$$

是一个 $0/1$ 数。值为 $1$ 时，在三块码的 qubits $p_i,q_j,r_k$ 上放置一个 physical $CCZ$；值为 $0$ 时不放置。全部 basis triples 给出线路

$$
U_{\mathrm{CCZ}}
=
\prod_{p_i,q_j,r_k:\,
f_{\mathrm{CCZ}}(p_i,q_j,r_k)=1}
CCZ_{p_iq_jr_k}.
$$

对一般 $x,y,z\in C^1$，同一个 $f_{\mathrm{CCZ}}$ 按 $\mathbb F_2$ 三线性延拓；它统计三个 supports 所选择的 physical hyperedges 的奇偶。

若这个 physical circuit 要定义 logical gate，则对任意 $u\in C^0$ 和 $z_2,z_3\in\ker\delta^1$ 必须有

$$
f_{\mathrm{CCZ}}(\delta^0u,z_2,z_3)=0,
$$

另外两个 argument 也满足相同条件。这个 coboundary-invariance 判据的 CSS 含义见 [[CSS码中的cochain complex#为什么 CCZ 构造需要 $H^1$]]；本笔记后面由 symmetric integrated Leibniz 验证它。

---
### Symmetric local product

三个 constituent seed complexes 分别是

$$
C_{\alpha_s}:
R\xrightarrow{\delta_s}R,
\qquad
\delta_s(v)=\alpha_sv,
\qquad
s\in\{\mathrm I,\mathrm {II},\mathrm {III}\}.
$$

对每个 seed 选择 support 两两不交的分解

$$
\alpha_s
=
\alpha_s^{\mathrm{in}}
+
\alpha_s^{\mathrm{out}}
+
\alpha_s^{\mathrm{free}}.
$$

对 degree-$0$ basis check $u_g$ 与 degree-$1$ basis bit $x_h$，其中 $g,h\in G$，classical preorientation 定义

$$
u_g\cup x_h
=
\begin{cases}
x_h,
&
h\in\operatorname{supp}
(\alpha_s^{\mathrm{out}}g),\\
0,
&
\text{otherwise},
\end{cases}
$$

$$
x_h\cup u_g
=
\begin{cases}
x_h,
&
h\in\operatorname{supp}
(\alpha_s^{\mathrm{in}}g),\\
0,
&
\text{otherwise}.
\end{cases}
$$

Degree-$0$ basis elements 使用对角乘法：

$$
u_g\cup u_{g'}
=
\begin{cases}
u_g,&g=g',\\
0,&g\ne g'.
\end{cases}
$$

没有列出的 basis products 为 $0$，再双线性延拓。Free piece 仍属于完整 coboundary $\alpha_sg$，但不直接出现在上述两条 mixed-degree products 中；它会进入 integrated Leibniz 的合法性条件。完整的一般定义与 group translations 的等变性分别见 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#Preorientation]] 和 [[Balanced quotient 上的 inherited product 与 integrated Leibniz#Preorientation 的平移等变性]]。

这个二元 cup product 一般不结合。因此 Menon 直接把 symmetric triple product 定义为下列 position-dependent operation：

| 三个 local arguments 的 degrees | symmetric triple product |
| --- | --- |
| $(1,0,0)$ | $x\cup u\cup v:=(x\cup u)\cup v$ |
| $(0,1,0)$ | $u\cup x\cup v:=(u\cup x)\cup v$ |
| $(0,0,1)$ | $u\cup v\cup x:=u\cup(v\cup x)$ |
| $(0,0,0)$ | $u\cup v\cup w:=(u\cup v)\cup w$ |
| 其它 degree patterns | $0$ |

这里的 symmetric 只指括号随唯一 degree-$1$ argument 的位置而变；它既不声称二元 cup product 结合，也不声称三线性 operation 在置换 arguments 后不变。

#### Averaging transport

三个 seed complexes 的 ordinary tensor product 是

$$
\widetilde C
=
C_a
\otimes_{\mathbb F_2}
C_b
\otimes_{\mathbb F_2}
C_c.
$$

两个 balanced interfaces 给出群

$$
H=G^2
$$

及其在 $\widetilde C$ 上的作用

$$
\begin{aligned}
(g,h)\cdot
(y_a\otimes y_b\otimes y_c)
={}&
(y_ag^{-1})
\otimes
(gy_bh^{-1})
\otimes
(hy_c).
\end{aligned}
$$

Seed coboundaries 与相应的左右 regular translations 对易；相应计算见 [[Tricycle complex 的 balanced-product 构造#Abelian group algebra 与 seed maps]]。所以 ordinary tensor-product coboundary $\widetilde\delta$ 满足

$$
\widetilde\delta(\eta y)
=
\eta\,\widetilde\delta(y),
\qquad
\eta\in H.
$$

因此这个 $H$-作用是 cochain action，coinvariant quotient 与 invariant subspace 都继承 coboundary。

Balanced complex 正是 coinvariant quotient

$$
C=\widetilde C_H.
$$

相同作用的不变子复形记为

$$
\widetilde C^H
=
\left\{
z\in\widetilde C:
\eta z=z
\text{ for every }\eta\in H
\right\}.
$$

对 coinvariant class $[y]_H\in\widetilde C_H$，非归一化 averaging map 定义为

$$
\operatorname{avg}:
C=\widetilde C_H
\longrightarrow
\widetilde C^H,
\qquad
\operatorname{avg}([y]_H)
=
\sum_{\eta\in H}\eta y.
$$

这个作用在每个 degree sector 的 regular product basis 上自由，具体作用见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz#Menon 的三重 group-algebra product]]。因此，由 [[Balanced quotient 上的 inherited product 与 integrated Leibniz#Averaging 的 orbit 分解与可逆性]]，$\operatorname{avg}$ 是 cochain-complex isomorphism。这里没有因子 $|H|^{-1}$：每个 orbit sum 是一组不同 basis elements 的和，而 $\operatorname{avg}^{-1}$ 只是把这个 orbit sum 送回相应的 orbit class。

三个 local trilinear maps 先组成 ordinary operation

$$
\widetilde\mu
=
\mu_a\otimes\mu_b\otimes\mu_c
:
\widetilde C^{\times3}
\longrightarrow
\widetilde C.
$$

Preorientation pieces 的平移等变性逐 factor 给出共同 $H$-等变性

$$
\widetilde\mu
\left(
\eta y_1,
\eta y_2,
\eta y_3
\right)
=
\eta\,
\widetilde\mu(y_1,y_2,y_3),
\qquad
\eta\in H.
$$

这里是同一个 $\eta$ 同时作用于三个 arguments。于是

$$
\widetilde\mu
\left(
(\widetilde C^H)^{\times3}
\right)
\subseteq
\widetilde C^H.
$$

因此 balanced complex 上的 inherited operation 是把这条 invariant operation 经 $\operatorname{avg}$ transport 回 coinvariants：

$$
\mu_C
=
\operatorname{avg}^{-1}
\circ
\left.
\widetilde\mu
\right|_{(\widetilde C^H)^{\times3}}
\circ
\operatorname{avg}^{\times3}.
$$

把 orbit sums 展开，可得到同一个 operation 的 relative-translate formula：

$$
\begin{aligned}
&\mu_C
\left(
[y_1]_H,
[y_2]_H,
[y_3]_H
\right)\\
&\qquad
=
\sum_{\eta_2,\eta_3\in H}
\left[
\widetilde\mu
\left(
y_1,
\eta_2y_2,
\eta_3y_3
\right)
\right]_H.
\end{aligned}
$$

这说明 $\mu_C$ 不是在 balanced representatives 上只取单项 $[\widetilde\mu(y_1,y_2,y_3)]_H$；整个 relative-translate sum 才不依赖 representatives。后文只写 $\mu_C$，是因为 $\operatorname{avg}$ 已经被吸收到这个 inherited operation 的定义中。

Top-degree functional 使用另一条下降路径。记 $\epsilon=\int_R:R\to\mathbb F_2$，ordinary top degree 上定义

$$
\widetilde\lambda:
\widetilde C^3
\longrightarrow
\mathbb F_2,
\qquad
\widetilde\lambda
(r_a\otimes r_b\otimes r_c)
=
\epsilon(r_a)\epsilon(r_b)\epsilon(r_c).
$$

由于 $\epsilon(gr)=\epsilon(rg)=\epsilon(r)$，对所有 $\eta\in H$ 都有

$$
\widetilde\lambda(\eta v)
=
\widetilde\lambda(v).
$$

因此 $\widetilde\lambda$ 直接下降到 coinvariants：

$$
\lambda_C([v]_H)
=
\widetilde\lambda(v).
$$

在

$$
C^3
=
R\otimes_RR\otimes_RR
\cong
R
$$

下，multiplication isomorphism 把 $r_a\otimes_Rr_b\otimes_Rr_c$ 送到 $r_ar_br_c$。Augmentation 的乘法性

$$
\epsilon(rs)=\epsilon(r)\epsilon(s)
$$

因而给出

$$
\epsilon(r_a)\epsilon(r_b)\epsilon(r_c)
=
\epsilon(r_ar_br_c).
$$

所以这个 descended functional 正是前文写出的 augmentation $\lambda_C=\int_R$；augmentation 乘法性的 coefficient 计算见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz#Augmentation integral]]。

$H$-invariance 只保证 $\lambda_C$ 在 coinvariant quotient 上良定义。要使它成为 cochain-complex integral，还需它在 top-degree coboundaries 上取零。Tricycle coboundary 满足

$$
\delta^2(x,y,z)
=
bx+ay+cz,
$$

所以当

$$
\epsilon(a)=\epsilon(b)=\epsilon(c)=0
$$

时，

$$
\begin{aligned}
\lambda_C\!\left(\delta^2(x,y,z)\right)
={}&
\epsilon(b)\epsilon(x)
+
\epsilon(a)\epsilon(y)
+
\epsilon(c)\epsilon(z)\\
={}&0.
\end{aligned}
$$

在后文采用的 free-$0$ 情形中，

$$
\alpha
=
\alpha^{\mathrm{in}}
+
\alpha^{\mathrm{out}},
$$

而第一组 parity condition

$$
\left|\alpha^{\mathrm{in}}\right|
+
\left|\alpha^{\mathrm{out}}\right|
=0
\pmod2
$$

恰好给出 $\epsilon(\alpha)=0$；对 $\alpha=a,b,c$ 分别应用即可得到上述 integral 条件。

$\lambda_C$ 不通过 $\operatorname{avg}^{-1}$ transport。令

$$
\operatorname{avg}^3
=
\left.
\operatorname{avg}
\right|_{C^3}
:
C^3
\longrightarrow
(\widetilde C^3)^H.
$$

则

$$
\widetilde\lambda
\circ
\operatorname{avg}^3
=
\left(|H|1_{\mathbb F_2}\right)
\lambda_C,
$$

所以一般不能用 $\widetilde\lambda\circ\operatorname{avg}^3$ 定义 $\lambda_C$。Free action 只用于保证 $\operatorname{avg}$ 可逆，不是 top-degree functional 直接下降的条件。

---
### Sector degree patterns

Balanced complex 来自三个二项 seed complexes

$$
C_a\otimes_R C_b\otimes_R C_c,
$$

其中每个 seed 只有 degrees $0,1$。三位 sector label

$$
R_{\varepsilon_a\varepsilon_b\varepsilon_c}
=
C_a^{\varepsilon_a}
\otimes_R
C_b^{\varepsilon_b}
\otimes_R
C_c^{\varepsilon_c}
$$

中，$\varepsilon_a,\varepsilon_b,\varepsilon_c$ 分别记录三个 tensor factors $C_a,C_b,C_c$ 中所取的 cochain degree。也就是说，$(\varepsilon_a,\varepsilon_b,\varepsilon_c)$ 是一个逐 factor 的 degree vector，而不是三个新的 cochains；它们的和

$$
\varepsilon_a+\varepsilon_b+\varepsilon_c
$$

才是 balanced complex 中的 total degree。因此，total degree 为 $1$ 的三个 sectors 是

$$
\begin{aligned}
\mathrm I
&=R_{100}
=C_a^1\otimes_R C_b^0\otimes_R C_c^0,\\
\mathrm {II}
&=R_{010}
=C_a^0\otimes_R C_b^1\otimes_R C_c^0,\\
\mathrm {III}
&=R_{001}
=C_a^0\otimes_R C_b^0\otimes_R C_c^1.
\end{aligned}
$$

换言之，sector $\mathrm I$ 的 degree-$1$ factor 来自 seed $a$，sector $\mathrm {II}$ 的来自 seed $b$，sector $\mathrm {III}$ 的来自 seed $c$。先取 sector choice

$$
(i,j,k)
=
(\mathrm I,\mathrm {II},\mathrm {III}).
$$

为了区分外部 code blocks 与每个 block 内部的 seed factors，这一张表暂时把三个 arguments 写成

$$
p_{\mathrm I}^{(1)},
\qquad
q_{\mathrm {II}}^{(2)},
\qquad
r_{\mathrm {III}}^{(3)}.
$$

上标 $(1),(2),(3)$ 标记三个外部 code blocks，下标 $\mathrm I,\mathrm {II},\mathrm {III}$ 标记各 block 内的 sectors。下面的 degree table 必须从两个方向读取：

- 固定一列，从 $a,b,c$ 三行向下读，得到一个 argument 的 factor-degree vector，也就是它的 sector label；
- 固定一行，从三个 arguments 横向读，得到一个 internal seed factor 上的 local triple degree pattern；symmetric triple product 按这个 pattern 计算。

| 内部 seed factor | block $1$: $p_{\mathrm I}^{(1)}$ | block $2$: $q_{\mathrm {II}}^{(2)}$ | block $3$: $r_{\mathrm {III}}^{(3)}$ | local output degree |
| --- | ---: | ---: | ---: | ---: |
| $a$ | $1$ | $0$ | $0$ | $1$ |
| $b$ | $0$ | $1$ | $0$ | $1$ |
| $c$ | $0$ | $0$ | $1$ | $1$ |

例如，第一列从上到下是 $(1,0,0)^T$，说明 $p_{\mathrm I}^{(1)}$ 属于 sector $\mathrm I$；第一行从左到右也是 $(1,0,0)$，但它表示在 internal factor $a$ 上，三个 local arguments 的 degrees 依次为 $(1,0,0)$。这两个三元组数值相同，指标方向却不同：前者跨 seed factors，后者跨外部 code blocks。

因此完全可以让两个 arguments 都属于 sector $\mathrm I$，也就是出现两列 $(1,0,0)^T$。例如取

$$
p_{\mathrm I}^{(1)},
\qquad
q_{\mathrm I}^{(2)},
\qquad
r_{\mathrm {III}}^{(3)}.
$$

相应的 degree table 是

| 内部 seed factor | $p_{\mathrm I}^{(1)}$ | $q_{\mathrm I}^{(2)}$ | $r_{\mathrm {III}}^{(3)}$ | local product |
| --- | ---: | ---: | ---: | --- |
| $a$ | $1$ | $1$ | $0$ | $0$ |
| $b$ | $0$ | $0$ | $0$ | degree $0$ |
| $c$ | $0$ | $0$ | $1$ | degree $1$ |

在 factor $a$ 上，local degree pattern 是 $(1,1,0)$。Two-term seed 只有 degrees $0,1$，没有 degree-$2$ component；因此 symmetric triple product 的 degree rule 把这个 local product 定义为 $0$。三个 local products 的 tensor 中只要有一个 factor 为 $0$，整个 inherited triple product 就为 $0$。

所以“不能有两个 $(1,0,0)$”并不是 domain restriction：$(C^1)^{\times3}$ 中允许重复 sectors；只是这些 triples 被 $\mu_C$ 送到 $0$。要得到非零值，三列必须分别是 $(1,0,0)^T,(0,1,0)^T,(0,0,1)^T$，次序可以 permutation。此时每一行恰有一个 degree-$1$ argument，三个 local product values 的 balanced tensor 属于

$$
C_a^1\otimes_RC_b^1\otimes_RC_c^1
=
R_{111}
=
C^3.
$$

这正是后文 physical-basis CCZ formula 中 pairwise-distinct sector indicator 的 degree 来源。

---
### Symmetric integrated Leibniz

本节始终取系数域 $\mathbb F_2$。[[#Averaging transport]] 已经从 ordinary tensor-product complex

$$
\widetilde C
:=
C_a\otimes_{\mathbb F_2}C_b\otimes_{\mathbb F_2}C_c
$$

构造出 balanced complex

$$
C=\widetilde C_H,
\qquad
H=G^2,
$$

上的 inherited operation $\mu_C$，并在 $C^3$ 上定义了 integral $\lambda_C$。要使

$$
f_{\mathrm{CCZ}}(z_1,z_2,z_3)
=
\lambda_C\mu_C(z_1,z_2,z_3)
$$

只依赖 $H^1(C)$ 中的 classes，需要先证明 $\mu_C$ 与 $\lambda_C$ 在 balanced complex 上满足 integrated Leibniz。

#### Balanced complex 上的 Leibniz defect

取 homogeneous

$$
q_i\in C^{p_i},
\qquad
p_1+p_2+p_3=2.
$$

这个 total-degree 条件保证 $\delta_C$ 作用于任一 argument 后，degree-additive operation $\mu_C$ 的值都属于 $C^3$，因而可以作用 $\lambda_C:C^3\to\mathbb F_2$。定义 balanced Leibniz defect

$$
\begin{aligned}
\mathcal L_C(q_1,q_2,q_3)
:={}&
\lambda_C\mu_C(\delta_Cq_1,q_2,q_3)\\
&+
\lambda_C\mu_C(q_1,\delta_Cq_2,q_3)\\
&+
\lambda_C\mu_C(q_1,q_2,\delta_Cq_3).
\end{aligned}
$$

为每个 $q_i$ 选择 homogeneous lift

$$
q_i=[y_i]_H,
\qquad
y_i\in\widetilde C^{p_i}.
$$

Ordinary complex 上相应的 defect 记为

$$
\begin{aligned}
\widetilde{\mathcal L}(y_1,y_2,y_3)
:={}&
\widetilde\lambda\widetilde\mu
(\widetilde\delta y_1,y_2,y_3)\\
&+
\widetilde\lambda\widetilde\mu
(y_1,\widetilde\delta y_2,y_3)\\
&+
\widetilde\lambda\widetilde\mu
(y_1,y_2,\widetilde\delta y_3).
\end{aligned}
$$

这里 $\mu_C$ 由 relative translates 计算，而 $\lambda_C$ 由 $H$-invariance 直接下降：

$$
\begin{aligned}
&\mu_C([y_1]_H,[y_2]_H,[y_3]_H)\\
&\qquad=
\sum_{\eta_2,\eta_3\in H}
\left[
\widetilde\mu(y_1,\eta_2y_2,\eta_3y_3)
\right]_H,
\qquad
\lambda_C([v]_H)=\widetilde\lambda(v).
\end{aligned}
$$

又因为 $H$ 的作用是 cochain action，

$$
\delta_C[y]_H=[\widetilde\delta y]_H,
\qquad
\widetilde\delta(\eta y)=\eta\widetilde\delta y.
$$

分别把 relative-translate formula 代入 $\mathcal L_C$ 的三个 summands，得到

$$
\begin{aligned}
&\mathcal L_C(q_1,q_2,q_3)\\
={}&
\sum_{\eta_2,\eta_3\in H}
\Bigl[
\widetilde\lambda\widetilde\mu
(\widetilde\delta y_1,\eta_2y_2,\eta_3y_3)\\
&\qquad+
\widetilde\lambda\widetilde\mu
(y_1,\widetilde\delta(\eta_2y_2),\eta_3y_3)\\
&\qquad+
\widetilde\lambda\widetilde\mu
(y_1,\eta_2y_2,\widetilde\delta(\eta_3y_3))
\Bigr]\\
={}&
\sum_{\eta_2,\eta_3\in H}
\widetilde{\mathcal L}
(y_1,\eta_2y_2,\eta_3y_3).
\end{aligned}
$$

因此 relative-translate formula 把 balanced defect 写成 ordinary defects 的和；它没有单独令这些 summands 为零。但若 $\widetilde{\mathcal L}$ 对所有 homogeneous arguments 都为零，则每个固定 $(\eta_2,\eta_3)$ 对应的 summand 都为零，从而 $\mathcal L_C=0$。

#### Ordinary tensor product 的 seed 来源

对每个 $\alpha\in\{a,b,c\}$，定义零延拓后的 seed integral

$$
\lambda_\alpha:
C_\alpha^0\oplus C_\alpha^1
\longrightarrow
\mathbb F_2,
\qquad
\left.\lambda_\alpha\right|_{C_\alpha^0}=0,
$$

并要求它在 $C_\alpha^1$ 上读取 support parity。对 homogeneous $a_i\in C_\alpha$，相应的 seed Leibniz defect 定义为

$$
\begin{aligned}
\mathcal L_\alpha(a_1,a_2,a_3)
:={}&
\lambda_\alpha\mu_\alpha
(\delta_\alpha a_1,a_2,a_3)\\
&+
\lambda_\alpha\mu_\alpha
(a_1,\delta_\alpha a_2,a_3)\\
&+
\lambda_\alpha\mu_\alpha
(a_1,a_2,\delta_\alpha a_3).
\end{aligned}
$$

Ordinary operation 与 integral 分别逐 seed 分解为

$$
\widetilde\mu
=
\mu_a\otimes\mu_b\otimes\mu_c,
\qquad
\widetilde\lambda
=
\lambda_a\otimes\lambda_b\otimes\lambda_c,
\qquad
\left.\widetilde\lambda\right|_{\widetilde C^q}=0
\quad(q\ne3).
$$

对 homogeneous pure tensor

$$
y
=
y^{(a)}\otimes y^{(b)}\otimes y^{(c)},
$$

$\widetilde\delta$ 展开为

$$
\begin{aligned}
\widetilde\delta y
={}&
(\delta_a y^{(a)})\otimes y^{(b)}\otimes y^{(c)}\\
&+
y^{(a)}\otimes(\delta_b y^{(b)})\otimes y^{(c)}\\
&+
y^{(a)}\otimes y^{(b)}\otimes(\delta_c y^{(c)}).
\end{aligned}
$$

一般系数下，后两项带有由左侧 factors 的 degrees 决定的 Koszul signs；这里因为 $-1=1\in\mathbb F_2$ 而全部消失。把这个展开代入 $\widetilde{\mathcal L}$，再按被微分的 seed factor $\alpha$ 分组。对 pure tensors $y_j=\bigotimes_\beta y_j^{(\beta)}$，固定-$\alpha$ 的整组 summands 经过 product integral 后等于

$$
\mathcal L_\alpha
\left(
y_1^{(\alpha)},y_2^{(\alpha)},y_3^{(\alpha)}
\right)
\prod_{\beta\ne\alpha}
\lambda_\beta\mu_\beta
\left(
y_1^{(\beta)},y_2^{(\beta)},y_3^{(\beta)}
\right).
$$

其余 seed factors 与 Leibniz position 无关，所以 $\mathcal L_\alpha=0$ 会令固定-$\alpha$ 的整组和为零。对 $\alpha=a,b,c$ 分别应用并作多线性延拓，便得到

$$
\mathcal L_a=\mathcal L_b=\mathcal L_c=0
\quad\Longrightarrow\quad
\widetilde{\mathcal L}=0
\quad\Longrightarrow\quad
\mathcal L_C=0.
$$

所以证明 $\mathcal L_C=0$ 归结为验证三个 seed 的 $\mathcal L_\alpha=0$。上式只保留了当前三 seed 构造所用的 fixed-factor 分组；一般证明见 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#Ordinary tensor product 上的 integrated Leibniz]]。一般 relative-translate 继承证明见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz#Integrated Leibniz 的继承]]。

#### Seed local identity

固定

$$
\alpha\in\{a,b,c\}
$$

及其 local seed complex

$$
C_\alpha:
C_\alpha^0=R
\xrightarrow{\delta_\alpha}
C_\alpha^1=R,
\qquad
\delta_\alpha(r)=\alpha r.
$$

记 $\mu_\alpha$ 为 [[#Symmetric local product]] 定义的 local symmetric triple product。对 $x\in C_\alpha^1$，上一小节引入的 seed integral 具体为

$$
\lambda_\alpha(x)
:=
\left|\operatorname{supp}(x)\right|
\pmod2,
$$

而它在 $C_\alpha^0$ 上取零。上一小节定义的 seed Leibniz defect 用 symmetric bracketing 的 cup 记号展开为

$$
\begin{aligned}
\mathcal L_\alpha(a_1,a_2,a_3)
={}&
\left|\delta_\alpha(a_1)\cup a_2\cup a_3\right|
+
\left|a_1\cup\delta_\alpha(a_2)\cup a_3\right|\\
&+
\left|a_1\cup a_2\cup\delta_\alpha(a_3)\right|
\pmod2.
\end{aligned}
$$

要求 $\mathcal L_\alpha=0$ 是每个 seed 的 preorientation 必须验证的条件。在结合的 differential graded algebra 中，若三重 operation 是二元 cup product 的迭代、二元 cup product 满足 cochain-level Leibniz，并且 $\lambda_\alpha$ 在 coboundaries 上取零，这条 identity 会由积分后的普通 Leibniz 公式得到。当前 position-dependent local product 不满足这些完整前提，所以直接检查积分后的等式。一般定义与 support 判据见 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#Integrated Leibniz rule]]。

Integrated-Leibniz identity 对三个 arguments 都是线性的。若某个 argument 属于 $C_\alpha^1$，则 two-term seed 的 $\delta_\alpha$ 在它上面取零，而其余 Leibniz summands 含有至少两个 degree-$1$ arguments，因而也由 symmetric triple product 的 degree rule 取为零。因此只需检查三个 arguments 都属于 $C_\alpha^0=R$ 的情形；再由三线性，只需检查 group basis triples

$$
(u_f,u_g,u_h),
\qquad
f,g,h\in G.
$$

#### Preorientation constraints

一般 in/out/free support 判据见 [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz#Integrated Leibniz rule]]。这里使用 Menon group-algebra seed 的 free-part-free 化简。

##### Free part 为空

先取这个 seed 的 free part 为空：

$$
\alpha^{\mathrm{free}}=0.
$$

对每个 $t\in G$，记

$$
\begin{aligned}
I_t&=\operatorname{supp}\left(\alpha^{\mathrm{in}}t\right),\\
O_t&=\operatorname{supp}\left(\alpha^{\mathrm{out}}t\right),\\
N_t&=\operatorname{supp}(\alpha t).
\end{aligned}
$$

以下 $|S|$ 表示有限集合 $S$ 的 cardinality，并一律在 mod $2$ 下读取；对 $\beta\in R$，$|\beta|$ 是 $|\operatorname{supp}(\beta)|$ 的简写。

由于 in/out pieces 的 supports 不交，而且

$$
\alpha
=
\alpha^{\mathrm{in}}
+
\alpha^{\mathrm{out}},
$$

所以

$$
N_t=I_t\sqcup O_t.
$$

把 $(u_f,u_g,u_h)$ 代入 local integrated-Leibniz identity。由 mixed-degree cup products 的 in/out 读数和 symmetric bracketing，

$$
\begin{aligned}
\operatorname{supp}
\left(\delta_\alpha u_f\cup u_g\cup u_h\right)
&=
N_f\cap I_g\cap I_h,\\
\operatorname{supp}
\left(u_f\cup\delta_\alpha u_g\cup u_h\right)
&=
O_f\cap N_g\cap I_h,\\
\operatorname{supp}
\left(u_f\cup u_g\cup\delta_\alpha u_h\right)
&=
O_f\cap O_g\cap N_h.
\end{aligned}
$$

第一项中的 degree-$1$ cochain 右侧有两个 degree-$0$ checks，因而连续通过两个 in tests；第二项左侧通过 out test、右侧通过 in test；第三项左侧的两个 checks 都给出 out tests。因此 integrated-Leibniz 左端为

$$
\begin{aligned}
L_\alpha(f,g,h)
={}&
\left|N_f\cap I_g\cap I_h\right|
+
\left|O_f\cap N_g\cap I_h\right|\\
&+
\left|O_f\cap O_g\cap N_h\right|
\pmod2.
\end{aligned}
$$

展开每个 $N_t=I_t\sqcup O_t$，得到

$$
\begin{aligned}
L_\alpha(f,g,h)
={}&
\left|I_f\cap I_g\cap I_h\right|
+
\left|O_f\cap I_g\cap I_h\right|\\
&+
\left|O_f\cap I_g\cap I_h\right|
+
\left|O_f\cap O_g\cap I_h\right|\\
&+
\left|O_f\cap O_g\cap I_h\right|
+
\left|O_f\cap O_g\cap O_h\right|
\pmod2.
\end{aligned}
$$

中间两类 mixed intersections 各出现两次，在 $\mathbb F_2$ 中抵消。因此，对所有允许重复的 $f,g,h\in G$，

$$
L_\alpha(f,g,h)
=
\left|I_f\cap I_g\cap I_h\right|
+
\left|O_f\cap O_g\cap O_h\right|
\pmod2.
$$

令这个表达式为零，再按 $f,g,h$ 的相等关系分类。以下用 $\beta\cap\gamma$ 表示 $\operatorname{supp}(\beta)\cap\operatorname{supp}(\gamma)$。分类中使用共同右平移作归一化；右乘 group element 是 $G$ 上的双射，因而把 intersections 映到 intersections 并保持 cardinality。这正是 [[Balanced quotient 上的 inherited product 与 integrated Leibniz#Preorientation 的平移等变性]] 中的共同平移不变性。

1. 若 $f=g=h$，集合交满足幂等性，所以

   $$
   L_\alpha(f,f,f)
   =
   |I_f|+|O_f|.
   $$

   右乘 $f^{-1}$ 只置换 group basis，故 $|I_f|=|\alpha^{\mathrm{in}}|$、$|O_f|=|\alpha^{\mathrm{out}}|$。于是得到

   $$
   \left|\alpha^{\mathrm{in}}\right|
   +
   \left|\alpha^{\mathrm{out}}\right|
   =0
   \pmod2.
   $$

2. 若集合 $\{f,g,h\}$ 恰含两个 group elements，可取 $f=g\ne h$；其它重复位置给出同一个 intersection condition。此时

   $$
   L_\alpha(f,f,h)
   =
   |I_f\cap I_h|
   +
   |O_f\cap O_h|.
   $$

   对交式中的 supports 共同右乘 $f^{-1}$，并令

   $$
   w=hf^{-1}\ne e,
   $$

   得到

   $$
   \left|
   \alpha^{\mathrm{in}}
   \cap
   \alpha^{\mathrm{in}}w
   \right|
   +
   \left|
   \alpha^{\mathrm{out}}
   \cap
   \alpha^{\mathrm{out}}w
   \right|
   =0
   \pmod2.
   $$

3. 若 $f,g,h$ 两两不同，对交式中的 supports 共同右乘 $f^{-1}$，并令

   $$
   v=gf^{-1},
   \qquad
   w=hf^{-1}.
   $$

   此时 $e,v,w$ 两两不同，并得到

   $$
   \begin{aligned}
   &
   \left|
   \alpha^{\mathrm{in}}
   \cap
   \alpha^{\mathrm{in}}v
   \cap
   \alpha^{\mathrm{in}}w
   \right|\\
   &\qquad
   +
   \left|
   \alpha^{\mathrm{out}}
   \cap
   \alpha^{\mathrm{out}}v
   \cap
   \alpha^{\mathrm{out}}w
   \right|
   =0
   \pmod2.
   \end{aligned}
   $$

以上三种 equality patterns 穷尽 $G^3$。因此，local integrated-Leibniz identity 在所有 group-basis triples 上成立，当且仅当这三组 parity conditions 成立；一般 cochains 的情形再由前面的 degree reduction 与三线性得到。若 free part 非空，记

$$
F_t
=
\operatorname{supp}\left(\alpha^{\mathrm{free}}t\right),
$$

则

$$
N_t=I_t\sqcup O_t\sqcup F_t,
$$

展开后还会留下 $F_f\cap I_g\cap I_h$、$O_f\cap F_g\cap I_h$、$O_f\cap O_g\cap F_h$ 等 terms，不能使用上述化简；此时必须检查论文中完整的 in/out/free preorientation constraints（Eqs. (46)–(50)）。

#### Cohomology representatives

对 $\alpha=a,b,c$ 分别验证上述 local conditions 后，前文的两步 implication 给出

$$
\mathcal L_C(q_1,q_2,q_3)=0
$$

对所有 total degree 为 $2$ 的 homogeneous $q_1,q_2,q_3\in C$ 成立。取

$$
a\in C^0,
\qquad
z_2,z_3\in Z^1(C)=\ker\delta_C^1,
$$

代入 $(a,z_2,z_3)$ 得

$$
\begin{aligned}
0={}&
f_{\mathrm{CCZ}}(\delta_C^0a,z_2,z_3)
+
\lambda_C\mu_C(a,\delta_Cz_2,z_3)\\
&+
\lambda_C\mu_C(a,z_2,\delta_Cz_3).
\end{aligned}
$$

因为 $\delta_Cz_2=\delta_Cz_3=0$，后两项为零，所以

$$
f_{\mathrm{CCZ}}(\delta_C^0a,z_2,z_3)=0.
$$

另外两个 argument 同理。因此 $f_{\mathrm{CCZ}}$ 诱导

$$
\bar f_{\mathrm{CCZ}}:
H^1(C)^{\times3}
\longrightarrow
\mathbb F_2,
\qquad
\bar f_{\mathrm{CCZ}}([z_1],[z_2],[z_3])
=
f_{\mathrm{CCZ}}(z_1,z_2,z_3).
$$

Integrated Leibniz 是这项 coboundary invariance 的充分条件，因而保证函数在 cohomology classes 上良定义。

---
### Physical CCZ 的基向量公式

前文的 $\mu_C$ 与 $\lambda_C$ 已经定义了 $f_{\mathrm{CCZ}}$；preorientation conditions 的作用是保证它进一步下降为 $\bar f_{\mathrm{CCZ}}$。这里在 physical-qubit basis 上计算同一个 $f_{\mathrm{CCZ}}$。先定义

$$
\mathbf 1_{\mathrm{pd}}(i,j,k)
=
\begin{cases}
1,&i,j,k\text{ 两两不同},\\
0,&\text{otherwise}.
\end{cases}
$$

以下解释 indicator 为 $1$，即 $i,j,k$ 两两不同的情形。在 ordered basis arguments

$$
(p_i,q_j,r_k)
$$

中，$p,q,r\in G$ 是三个 qubits 的 group coordinates；第一、第二、第三个 argument 分别来自三个外部 code blocks，而 $i,j,k$ 仍是各 argument 的 sector labels。对 local product，

$$
u\cup x
\text{ 读取 out},
\qquad
x\cup u
\text{ 读取 in}.
$$

因此，degree-$0$ argument 位于唯一 degree-$1$ argument 左侧时贡献 out piece，位于右侧时贡献 in piece。分别考察 sectors $i,j,k$ 所对应的 internal seed factors：

| internal seed factor | $(p_i,q_j,r_k)$ 的 local degrees | 唯一的 degree-$1$ argument | 左侧：out | 右侧：in |
| --- | ---: | --- | --- | --- |
| $C_{\alpha_i}$ | $(1,0,0)$ | $p_i$ | — | $q_j,r_k$ |
| $C_{\alpha_j}$ | $(0,1,0)$ | $q_j$ | $p_i$ | $r_k$ |
| $C_{\alpha_k}$ | $(0,0,1)$ | $r_k$ | $p_i,q_j$ | — |

现在按 group coordinate 收集它受到的两个 pieces：

- $r$ 在 factors $C_{\alpha_i},C_{\alpha_j}$ 中都位于 degree-$1$ argument 右侧，所以得到 $\alpha_i^{\mathrm{in}}\alpha_j^{\mathrm{in}}$；
- $q$ 在 $C_{\alpha_i}$ 中位于右侧、在 $C_{\alpha_k}$ 中位于左侧，所以得到 $\alpha_i^{\mathrm{in}}\alpha_k^{\mathrm{out}}$；
- $p$ 在 factors $C_{\alpha_j},C_{\alpha_k}$ 中都位于左侧，所以得到 $\alpha_j^{\mathrm{out}}\alpha_k^{\mathrm{out}}$。

把 $p,q,r\in G$ 视为 group basis $G\subset R$ 中的 basis elements，便在 $R=\mathbb F_2[G]$ 中定义

$$
\beta_r
=
r\alpha_i^{\mathrm{in}}\alpha_j^{\mathrm{in}},
\qquad
\beta_q
=
q\alpha_i^{\mathrm{in}}\alpha_k^{\mathrm{out}},
\qquad
\beta_p
=
p\alpha_j^{\mathrm{out}}\alpha_k^{\mathrm{out}}.
$$

前文的 local translates 写成 $\alpha_s^\bullet t$，这里把 coordinate 写在前面；由于 $G$ Abelian，$R$ 交换，所以 $t\alpha_s^\bullet=\alpha_s^\bullet t$，两种顺序相同。

若 $\operatorname{coeff}_h(\beta)$ 表示 group element $h$ 在 $\beta\in R$ 中的系数，则 physical-basis CCZ formula 可写为

$$
f_{\mathrm{CCZ}}(p_i,q_j,r_k)
=
\mathbf 1_{\mathrm{pd}}(i,j,k)
\sum_{h\in G}
\operatorname{coeff}_h(\beta_r)
\operatorname{coeff}_h(\beta_q)
\operatorname{coeff}_h(\beta_p)
\pmod2.
$$

三个 coefficient factors 同时为 $1$，当且仅当

$$
h\in
\operatorname{supp}(\beta_r)
\cap
\operatorname{supp}(\beta_q)
\cap
\operatorname{supp}(\beta_p).
$$

因此上式也可以写成论文中的 support-intersection form：

$$
\begin{aligned}
f_{\mathrm{CCZ}}(p_i,q_j,r_k)
={}&
\left|
\operatorname{supp}
\left(r\alpha_i^{\mathrm{in}}\alpha_j^{\mathrm{in}}\right)
\cap
\operatorname{supp}
\left(q\alpha_i^{\mathrm{in}}\alpha_k^{\mathrm{out}}\right)\right.\\
&\left.\qquad\cap
\operatorname{supp}
\left(p\alpha_j^{\mathrm{out}}\alpha_k^{\mathrm{out}}\right)
\right|
\mathbf 1_{\mathrm{pd}}(i,j,k)
\pmod2.
\end{aligned}
$$

这里每个 group-algebra product 都先在 $\mathbb F_2[G]$ 中完成；若多个乘积项产生同一个 group element，它们先按 mod $2$ 抵消，再取 $\operatorname{coeff}_h$ 或 support。

例如

$$
(i,j,k)
=
(\mathrm I,\mathrm {II},\mathrm {III})
$$

时，

$$
\beta_r=ra^{\mathrm{in}}b^{\mathrm{in}},
\qquad
\beta_q=qa^{\mathrm{in}}c^{\mathrm{out}},
\qquad
\beta_p=pb^{\mathrm{out}}c^{\mathrm{out}}.
$$

因此 $f_{\mathrm{CCZ}}$ 是三个 group-algebra coefficient functions 的逐点乘积经 augmentation 得到的数；在作用 augmentation 之前，$\mu_C(p_i,q_j,r_k)$ 属于 $C^3=R_{111}$，这一 degree 已由 [[#Sector degree patterns]] 的 calculation 确定。

---
### Logical connectivity tensor

实际计算 logical connectivity 时，先把 logical cocycle representatives 按 physical-qubit basis 展开，再对 [[#Physical CCZ 的基向量公式]] 作三线性延拓。

选取三块 code blocks 的 logical $X$ bases，并为每个 class 选 cocycle representative：

$$
\{l_\mu^{(1)}\},
\qquad
\{l_\nu^{(2)}\},
\qquad
\{l_\rho^{(3)}\}.
$$

Logical connectivity tensor 定义为

$$
T_{\mu\nu\rho}^{\mathrm{log}}
=
\bar f_{\mathrm{CCZ}}
\left(
[l_\mu^{(1)}],
[l_\nu^{(2)}],
[l_\rho^{(3)}]
\right).
$$

Coboundary invariance 保证这个数不依赖 representatives。它不推出

$$
\bar f_{\mathrm{CCZ}}\not\equiv0.
$$

是否存在非平凡 logical action，必须实际计算 $T^{\mathrm{log}}$。若某个 entry 为 $1$，相应的 logical gate 含有 $CCZ_{\mu\nu\rho}$，从而

$$
U_{\mathrm{log}}
=
\prod_{\mu,\nu,\rho:\,
T_{\mu\nu\rho}^{\mathrm{log}}=1}
CCZ_{\mu\nu\rho}.
$$

把它作用于三块 logical $|+\rangle$ blocks 得到 logical hypergraph magic state。由 $T^{\mathrm{log}}$ 抽取互不重叠的 $|CCZ\rangle$ resources 需要进一步研究 tensor subrank；这属于 [[Menon 2025 Magic Tricycles]] 及后续 hypergraph-state 笔记。

---
### 边界

- STCP 给出解析的 physical $CCZ$ hyperedge function；它不决定 hyperedges 的最短 parallel schedule。
- 一般的 in/out/free preorientation conditions 与 symmetric integrated Leibniz 保证 coboundary invariance，但不保证 logical connectivity tensor 非零。
- Free part 非空时必须使用论文中完整的 in/out/free preorientation constraints（Eqs. (46)–(50)），不能套用本笔记列出的 free-$0$ 简化条件。
- 当前公式取系数域 $\mathbb F_2$；一般系数下需要恢复 Koszul signs。
- Balanced quotient、averaging 与 relative-translate inheritance 放在 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；single-shot preparation、decoder soundness、Numerical Leibniz Rule、scheduled depth 与 $K_{\mathrm{CCZ}}$ subrank 放在 [[Menon 2025 Magic Tricycles]]。

---
### 来源

- Varun Menon, J. Pablo Bonilla Ataides, Rohan Mehta, Andi Gu, Daniel Bochen Tan, Mikhail D. Lukin, [*Magic tricycles: Efficient magic state generation with finite block-length quantum LDPC codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), arXiv:2508.10714v2, 2025, Appendix D: the definitions of preorientation and symmetric triple product, the local integrated-Leibniz identity, the sufficient preorientation conditions and their free-part-free group-algebra reduction, and the physical-basis CCZ formula.
- Nikolas P. Breuckmann, Margarita Davydova, Jens N. Eberhardt, Nathanan Tantivasadakarn, [*Cups and Gates I: Cohomology Invariants and Logical Quantum Operations*](<../../Papers/S002_2026_Breuckmann_cups_and_gates_I.pdf>), *Communications in Mathematical Physics* 407:86, 2026, Sections 3.3–3.4 and 5.2.
- [[Tricycle complex 的 balanced-product 构造]]：$C^1$ sectors、$C^3=R_{111}$ 与 group-algebra coordinates。
- [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]：classical in/out/free products、position-dependent multilinear operation 与 ordinary tensor-product inheritance。
- [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]：averaging construction、relative translates、augmentation integral 与 balanced integrated-Leibniz inheritance。
- [[CSS码中的cochain complex]]：physical support、coboundary 与 $H^1(C)$ 的 CSS 含义。
