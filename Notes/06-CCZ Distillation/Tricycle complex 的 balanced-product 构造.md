[[Balanced tensor product 与 coinvariant quotient]] 已经固定了 balanced tensor product 所需的右模、左模与中间 bimodule，并说明三重 regular-module product 的每个 basis orbit 由一个群乘积坐标标记。这里把该构造应用到 Menon 的三个 group-algebra seed complexes，得到 tricycle code 的四项 cochain complex。

普通 tensor-product complex 的 total degree 与 coboundary 公式见 [[Cochain complex 的 tensor product]]。以下计算始终采用 Menon 的有限 Abelian 群假设。

---
### Abelian group algebra 与 seed maps

令 $G$ 是有限 Abelian 群，并取

$$
R=\mathbb F_2[G].
$$

$R$ 的元素写成

$$
r=\sum_{g\in G}r_g\,g,
\qquad
r_g\in\mathbb F_2.
$$

因为 $G$ Abelian，$R$ 是交换的含幺结合环。每份 $R$ 都使用 regular bimodule 结构：左、右作用分别是环内左乘和右乘。

给定 $x\in R$，定义

$$
\delta_x:R\longrightarrow R,
\qquad
\delta_x(r)=xr.
$$

这个 map 总是右 $R$-linear：

$$
\delta_x(rs)=xrs=\delta_x(r)s.
$$

它是左 $R$-linear 当且仅当 $x\in Z(R)$。Menon 的 $R$ 交换，因此

$$
\delta_x(sr)=xsr=sxr=s\delta_x(r).
$$

所以 $\delta_x$ 是 regular bimodule map。这个检查说明了 Abelian 假设在 balanced-product complex 中的具体用途；一般非交换 group algebra 上，不能只写“乘以 $x$ 是 $R$-linear”而不说明作用侧别。

Menon 的三个 two-term seed complexes 为

$$
C_a:R\xrightarrow{\delta_a}R,
\qquad
C_b:R\xrightarrow{\delta_b}R,
\qquad
C_c:R\xrightarrow{\delta_c}R,
$$

其中

$$
\delta_a(r)=ar,
\qquad
\delta_b(r)=br,
\qquad
\delta_c(r)=cr.
$$

每个 cochain space 都是 regular bimodule，每个 coboundary 都兼容左右作用。因此三重 balanced product

$$
C
=
C_a\otimes_RC_b\otimes_RC_c
$$

在两个 interfaces 上都有良定义的 coboundary。

---
### Total degree 与 balanced sectors

每个 seed 只含 degrees $0,1$。三个 seed 的 ordinary tensor-product complex 按 total degree 分成

$$
1,\quad3,\quad3,\quad1
$$

个 sectors。Balanced product 不改变 sector 数量，只把每个 ordinary sector

$$
R\otimes_{\mathbb F_2}R\otimes_{\mathbb F_2}R
$$

换成

$$
R\otimes_RR\otimes_RR
\cong
R.
$$

因此

$$
C^0=R,
\qquad
C^1=R^3,
\qquad
C^2=R^3,
\qquad
C^3=R.
$$

这里 $R^3=R\oplus R\oplus R$，三个 summands 分别记录不同的 degree sectors，而不是把三个 group-algebra 元素预先相加成一份 $R$。

用三位标签表示 sectors：

$$
R_{ijk}
:=
(C_a)^i\otimes_R(C_b)^j\otimes_R(C_c)^k
\cong R,
\qquad
i,j,k\in\{0,1\}.
$$

采用顺序

$$
C^0=R_{000},
\qquad
C^1=(R_{100},R_{010},R_{001}),
$$

$$
C^2=(R_{101},R_{011},R_{110}),
\qquad
C^3=R_{111}.
$$

$C^2$ 的排列只用于固定后续矩阵的 row order。

---
### Tricycle coboundaries

在 $\mathbb F_2$ 上，Koszul signs 消失，三重 product 的 coboundary 为

$$
\delta
=
\delta_a\otimes I\otimes I
+
I\otimes\delta_b\otimes I
+
I\otimes I\otimes\delta_c.
$$

在乘法同构

$$
r_1\otimes_Rr_2\otimes_Rr_3
\longmapsto
r_1r_2r_3
$$

下，推进第一、第二、第三个 factor 分别给出乘以 $a,b,c$。这里能把三个 contributions 都写成同一侧的乘法，是因为 $a,b,c$ 位于交换环 $R$ 中。

从 $R_{000}$ 出发，三个 factors 都可以推进一次：

$$
\delta^0(r)=(ar,br,cr),
$$

所以

$$
\delta^0
=
\begin{bmatrix}
a\\ b\\ c
\end{bmatrix}.
$$

从 $C^1$ 到 $C^2$：

- $R_{100}$ 可推进第二或第三个 factor，分别到 $R_{110}$、$R_{101}$，对应列 $(c,0,b)^T$；
- $R_{010}$ 可推进第一或第三个 factor，分别到 $R_{110}$、$R_{011}$，对应列 $(0,c,a)^T$；
- $R_{001}$ 可推进第一或第二个 factor，分别到 $R_{101}$、$R_{011}$，对应列 $(a,b,0)^T$。

因此

$$
\delta^1
=
\begin{bmatrix}
c&0&a\\
0&c&b\\
b&a&0
\end{bmatrix}.
$$

从 $C^2$ 到 $C^3$ 时，$R_{101},R_{011},R_{110}$ 分别缺少第二、第一、第三个 factor，所以

$$
\delta^2
=
\begin{bmatrix}
b&a&c
\end{bmatrix}.
$$

于是得到四项 complex

$$
R
\xrightarrow{\delta^0}
R^3
\xrightarrow{\delta^1}
R^3
\xrightarrow{\delta^2}
R.
$$

两个复合为

$$
\delta^1\delta^0
=
\begin{bmatrix}
ca+ac\\
cb+bc\\
ba+ab
\end{bmatrix}
=0,
$$

$$
\delta^2\delta^1
=
\begin{bmatrix}
bc+cb&ac+ca&ba+ab
\end{bmatrix}
=0.
$$

这里同时使用了 $R$ 的交换性和 $\mathbb F_2$ 中 $x+x=0$。

---
### Regular representation 与二进制矩阵

固定 $R$ 的自然基 $G$，并把

$$
r=\sum_{\beta\in G}r_\beta\beta
$$

表示为 coefficient column

$$
b_G(r)=(r_\beta)_{\beta\in G}.
$$

Menon 的 regular representation 定义为

$$
B_G(x)_{\alpha,\beta}
=
\sum_{g\in G}x_g\,\delta_{\alpha,g\beta}.
$$

它表示左乘 $L_x:r\mapsto xr$：

$$
b_G(xr)=B_G(x)b_G(r).
$$

令

$$
A=B_G(a),
\qquad
B=B_G(b),
\qquad
C=B_G(c).
$$

则 $\delta^0$ 在 coefficient-column convention 下的二进制矩阵是

$$
D_0=
\begin{bmatrix}
A\\B\\C
\end{bmatrix}.
$$

CSS convention 取

$$
\delta^0=H_X^T,
\qquad
\delta^1=H_Z,
\qquad
\delta^2=H_{\mathrm{meta}}.
$$

因此

$$
H_X
=
\begin{bmatrix}
A^T&B^T&C^T
\end{bmatrix},
$$

$$
H_Z
=
\begin{bmatrix}
C&0&A\\
0&C&B\\
B&A&0
\end{bmatrix},
$$

$$
H_{\mathrm{meta}}
=
\begin{bmatrix}
B&A&C
\end{bmatrix}.
$$

$H_X$ 中的转置来自 $\delta^0=H_X^T$ 的 row/column convention，不是把左 regular action 换成右 regular action。四项 complex 的两个复合为零对应

$$
H_ZH_X^T=0,
\qquad
H_{\mathrm{meta}}H_Z=0.
$$

---
### CSS code 对应

| complex 项 | Menon code 对象 | 含义 |
|---|---|---|
| $C^0=R$ | $X$ checks | 一组 group-algebra check generators |
| $C^1=R^3$ | physical qubits | 三个 data sectors |
| $C^2=R^3$ | $Z$ check outcomes | 三组 syndrome bits |
| $C^3=R$ | metachecks | $Z$ syndrome relations |

Logical $X$ supports 是 $1$-cocycles modulo $1$-coboundaries：

$$
H^1(C)
=
\ker\delta^1/\operatorname{im}\delta^0.
$$

Balanced product 到这里完成的是 code complex 的构造。Local products 如何继承到这个 coinvariant complex，见 [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]；继承后的 symmetric triple product 如何给出 physical 与 logical $CCZ$，见 [[Symmetric triple cup-product]]。

---
### 来源

- Varun Menon, J. Pablo Bonilla Ataides, Rohan Mehta, Andi Gu, Daniel Bochen Tan, Mikhail D. Lukin, [*Magic Tricycles: Efficient Magic State Generation with Finite Block-Length Quantum LDPC Codes*](<../../Papers/S003_2025_Menon_magic_tricycles.pdf>), Appendix A, Eqs. (4)、(23)–(25), and Supplementary Material, Eqs. (83)–(89).
- [[Balanced tensor product 与 coinvariant quotient]]：module tensor、anti-diagonal coinvariants、三重 $G^2$-作用与 regular bimodule 的乘法同构。
- [[Cochain complex 的 tensor product]]：total degree、Koszul sign 与 product coboundary。
