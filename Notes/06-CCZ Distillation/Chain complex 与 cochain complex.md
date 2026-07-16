Chain complex 的作用是用线性代数记录“哪些对象闭合、哪些闭合对象其实是某个更高维对象的边界”。它把点、边、面片这类不同维度的对象放进一串向量空间，再用边界映射连接起来。cochain complex 是同一套结构的对偶写法；读 [[Menon 2025 Magic Tricycles]] 时，先把 cycle/cocycle、boundary/coboundary 和 homology/cohomology 读成 kernel、image 和 quotient 即可。

---
### chain complex：边界映射连续两次为零

一个 chain complex 写成

$$
\cdots
\xrightarrow{\partial_{i+2}}
C_{i+1}
\xrightarrow{\partial_{i+1}}
C_i
\xrightarrow{\partial_i}
C_{i-1}
\xrightarrow{\partial_{i-1}}
\cdots
$$

并满足

$$
\partial_i\partial_{i+1}=0.
$$

这里的下标 $i$ 叫 degree。$C_i$ 里的元素叫 $i$-chains；例如 $C_1$ 里的元素叫 $1$-chains。后面出现的 `1-cycle`、`1-cocycle` 里的 `1` 都是 degree，不是系数，也不是说只有一个对象。

在几何直觉中，$\partial$ 是“取边界”：二维面片的边界是边，一维边的边界是端点。为了把“取边界”写成线性映射，先把三角形里的顶点、边和面片分别当作不同维度的 basis labels。若顶点为 $a,b,c$，则顶点层的空间是

$$
C_0=\mathrm{span}\{[a],[b],[c]\}.
$$

边层的空间是

$$
C_1=\mathrm{span}\{[ab],[bc],[ca]\},
$$

面片层的空间是

$$
C_2=\mathrm{span}\{[abc]\}.
$$

这些空间里的元素是形式线性组合，例如 $\alpha[a]+\beta[b]+\gamma[c]$。这里相加的是 basis labels，不是几何点的位置向量。

记号 $[ab]$ 表示从 $a$ 指向 $b$ 的有向边，反向边差一个负号：

$$
[ba]=-[ab].
$$

记号 $[abc]$ 表示按 $a\to b\to c\to a$ 这个方向取的三角形面片。边界映射先在这些基本对象上定义，再线性延拓到整个空间。边的边界是终点减起点：

$$
\partial_1[ab]=[b]-[a].
$$

三角形面片的边界是沿边缘绕一圈：

$$
\partial_2[abc]=[ab]+[bc]+[ca].
$$

因为 $[ca]=-[ac]$，也可以写成

$$
\partial_2[abc]=[bc]-[ac]+[ab].
$$

这个写法和常见的交替删点公式一致：

$$
\partial_2[abc]
=
[bc]-[ac]+[ab],
$$

其中三项分别来自删掉 $a,b,c$。再取一次边界，

$$
\partial_1\partial_2[abc]
=([c]-[b])-([c]-[a])+([b]-[a])=0.
$$

每个顶点在最终结果里出现两次、符号相反，所以抵消。

若在 $\mathbb F_2$ 上工作，符号不用区分正负；同一个顶点出现两次就是 $0$。抽象的 chain complex 把这个“边界的边界为零”保留下来，写成 $\partial_i\partial_{i+1}=0$。

---
### cycle、boundary 和 homology

在 degree $i$ 上，先定义 cycles：

$$
Z_i=\ker\partial_i.
$$

$i$-cycle 是一个 $i$-chain，取边界后为零。几何上它像闭合回路；在线性代数里只需要读成“被后一张检查映射打成零”。

再定义 boundaries：

$$
B_i=\operatorname{im}\partial_{i+1}.
$$

$i$-boundary 是从更高一层 $C_{i+1}$ 取边界得到的 $i$-chain。由于 $\partial_i\partial_{i+1}=0$，

$$
B_i\subseteq Z_i.
$$

所以每个 boundary 自动是 cycle。

homology 把“已经是某个更高维对象边界”的平凡 cycles 商掉：

$$
H_i(C)=Z_i/B_i
=
\ker\partial_i/\operatorname{im}\partial_{i+1}.
$$

如果 $H_i(C)=0$，意思是 degree $i$ 上没有非平凡闭合对象：每个 cycle 都已经是 boundary。

继续用上面的三角形。令

$$
z=[ab]+[bc]+[ca]\in C_1.
$$

它是一个 $1$-cycle，因为

$$
\partial_1z
=
([b]-[a])+([c]-[b])+([a]-[c])
=0.
$$

若三角形的面片 $[abc]$ 也在 complex 里，那么

$$
z=\partial_2[abc],
$$

所以 $z$ 不只是闭合的 cycle，还是一个 boundary。它在 $H_1(C)$ 里代表平凡类。

更自然的非平凡例子是甜甜圈表面。把甜甜圈沿两条基本方向剪开，可以画成一个正方形；左右边重新粘在一起，上下边也重新粘在一起。记横向绕一圈的闭合边为 $a$，纵向绕一圈的闭合边为 $b$，正方形面片为 $s$。

这两条边都是 $1$-cycles：

$$
\partial_1a=0,
\qquad
\partial_1b=0.
$$

正方形面片的边界是四条边绕一圈，但粘合后相反方向的边相互抵消：

$$
\partial_2s=a+b-a-b=0.
$$

所以这个二维面片不会把 $a$ 或 $b$ 单独变成 boundary。直观地说，绕甜甜圈洞的一圈没有被表面上的某个二维区域填住；若真的有一个面片以 $a$ 为边界，就等于把洞封住了。

因此 $a$ 和 $b$ 是 cycles，但不是 boundaries，它们在 $H_1$ 里给出非平凡 classes。与之相对，甜甜圈表面上一条围住小圆盘的闭合曲线可以写成某个小面片的边界，所以它在 $H_1$ 里是平凡的。homology 记录的正是这种差别：闭合对象是否真的由更高一层对象填出来。

---
### cochain complex：箭头反过来的同一套结构

cochain complex 常写成上标递增：

$$
\cdots
\xrightarrow{\delta^{i-2}}
C^{i-1}
\xrightarrow{\delta^{i-1}}
C^i
\xrightarrow{\delta^i}
C^{i+1}
\xrightarrow{\delta^{i+1}}
\cdots
$$

并满足

$$
\delta^{i+1}\delta^i=0.
$$

$C^i$ 里的元素叫 $i$-cochains。若它在下一张映射下变成零，

$$
x\in\ker\delta^i,
$$

它叫 $i$-cocycle。若它来自前一张映射，

$$
x\in\operatorname{im}\delta^{i-1},
$$

它叫 $i$-coboundary。cohomology 定义为

$$
H^i(C)
=
\ker\delta^i/\operatorname{im}\delta^{i-1}.
$$

因此 `1-cocycle` 的意思是：住在 $C^1$ 里的 cochain，并且被 $\delta^1:C^1\to C^2$ 打成零。这里的 `1` 只标记它位于 $C^1$，不是说 cocycle 由一个元素组成。`1-coboundary` 的意思是：住在 $C^1$ 里，但其实由前一层 $\delta^0:C^0\to C^1$ 生成。

---
### co- 的来源

在代数拓扑里，cochains 可以看作 chains 的对偶对象。这里先固定符号：

- $\mathbb F$ 是系数域，例如 $\mathbb R$、$\mathbb C$ 或 $\mathbb F_2$；
- $\operatorname{Hom}(C_i,\mathbb F)$ 表示从 $C_i$ 到 $\mathbb F$ 的线性映射空间；
- $f\in C^i$ 是一个 $i$-cochain，也就是一个线性函数 $f:C_i\to\mathbb F$；
- $c\in C_{i+1}$ 是一个 $(i+1)$-chain。

若取

$$
C^i=\operatorname{Hom}(C_i,\mathbb F),
$$

那么 coboundary map $\delta^i:C^i\to C^{i+1}$ 可以由 boundary map $\partial_{i+1}:C_{i+1}\to C_i$ 对偶得到。意思是：要让 $\delta^if$ 作用在一个 $(i+1)$-chain $c$ 上，先对 $c$ 取边界，再让 $f$ 作用在这个边界上：

$$
(\delta^if)(c)=f(\partial_{i+1}c).
$$

再取 $c'\in C_{i+2}$，于是

$$
(\delta^{i+1}\delta^if)(c')
=
f(\partial_{i+1}\partial_{i+2}c')
=0.
$$

这解释了为什么 cochain complex 也满足“连续两步为零”。不过在量子码笔记里，通常不需要真的构造对偶空间；只要看到一串上标递增的线性空间和映射满足 $\delta^{i+1}\delta^i=0$，就可以按 cochain complex 读。

---
### 读 CSS 码时保留什么

后续在 [[CSS码中的cochain complex]] 里使用的是 cochain 写法：

$$
C^0\xrightarrow{\delta^0}C^1\xrightarrow{\delta^1}C^2.
$$

最重要的翻译是：

| cochain 术语     | 线性代数含义                                       |
| -------------- | -------------------------------------------- |
| $i$-cochain    | $C^i$ 中的元素                                   |
| $i$-cocycle    | $\ker\delta^i$ 中的元素                          |
| $i$-coboundary | $\operatorname{im}\delta^{i-1}$ 中的元素         |
| $H^i(C)$       | $\ker\delta^i/\operatorname{im}\delta^{i-1}$ |

因此不要先把 `cocycle` 想成新的物理对象。它在 CSS 码里通常只是“通过后一张检查”的 support；`coboundary` 是“由前一张映射生成的平凡方向”；cohomology 是“通过检查后再商掉平凡方向”。
