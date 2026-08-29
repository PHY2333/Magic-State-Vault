---
task_id: 20260828-hgp-v5-pilot
status: pass
integrated_draft_revision: 5
target: Notes/07-Lifted-Product Code/Hypergraph product code.md
target_before_blob: d18e00e59d71aa1615417dbfadf4f60d4b27bd69
target_after_blob: 3251b0075281fdf4dc86fccb230ae44397732bad
formal_integration_completed: true
committed: false
---

# Integration Report

## 授权与写入前锁定

用户于 2026-08-29 明确批准按 revision 5 `MANUSCRIPT_VERDICT.md` 与 `INTEGRATION_PREVIEW.md` 执行 formal integration；该授权取代 preview 中“尚未授权正式写入”的阶段性边界，但不扩大 preview 的内容范围。

| lock | expected | actual | result |
|---|---|---|---|
| 目标 HGP blob | `d18e00e59d71aa1615417dbfadf4f60d4b27bd69` | `d18e00e59d71aa1615417dbfadf4f60d4b27bd69` | match |
| U01 SHA-256 | `3713ad6565c3f992f402b4372db00efa37b798e56f6ac2d0fde9a04b5a46c585` | `3713ad6565c3f992f402b4372db00efa37b798e56f6ac2d0fde9a04b5a46c585` | match |
| U02 SHA-256 | `b5fe54e31c51308230fb356373ae3c13c86325991805eff92cc43ebb36de531a` | `b5fe54e31c51308230fb356373ae3c13c86325991805eff92cc43ebb36de531a` | match |
| `Notes/00-index.md` blob | `847c0b231fd7471f49a445cb7f0d0426a53285cb` | `847c0b231fd7471f49a445cb7f0d0426a53285cb` | match |
| `CANONICAL_KNOWLEDGE.md` blob | `12b3fdb92c5214f4c6e48b54d3a6777cd76ead67` | `12b3fdb92c5214f4c6e48b54d3a6777cd76ead67` | match |

Preview 记录的全局 HEAD 为 `d320a790...`，写入前当前 HEAD 为 `1eecc216...`；两者之间只包含已批准的本任务 revision 5 产物提交。目标 HGP、index、canonical 与相关 owner 的对象级基线均未变化，因此没有内容冲突。

## 已执行修改

1. 在目标文件顶部添加：

```yaml
---
note_type: reference
entry_mode: guided
status: reviewed
---
```

2. 删除整合前旧第 1 行。
3. 原样放入 revision 5 U01，紧接原样放入 revision 5 U02。
4. 原第 3–51 行逐字保留。
5. 原第 53–70 行完整删除；相邻空行收束为一个正常空行。
6. 原第 72–447 行逐字保留。
7. 未新增链接，未修改 index/canonical，未进行其它格式化。

## 精确装配证明

机器逐行比较使用以下期望序列：

```text
frontmatter
+ DRAFTS/U01.md
+ DRAFTS/U02.md
+ HEAD 目标原第 3–51 行
+ 单个空行
+ HEAD 目标原第 72–447 行
```

结果：`expected_lines=532`、`current_lines=532`、`delta_count=0`。

- U01 正式切片与 staged draft SHA-256 均为 `3713ad6565c3f992f402b4372db00efa37b798e56f6ac2d0fde9a04b5a46c585`。
- U02 正式切片与 staged draft SHA-256 均为 `b5fe54e31c51308230fb356373ae3c13c86325991805eff92cc43ebb36de531a`。
- 原第 39–51 行完整映射到新第 143–155 行。
- 原第 72–447 行完整映射到新第 157–532 行。
- 旧 opening 与原第 53–70 行均已不存在。

独立只读 Integration Verifier 复核上述装配、切片指纹和删除范围，结论为 `PASS`。

## Assembled reading flow

- 新第 11 行提出构造怎样保证对易；新第 13 行立即进入“从局部交换到矩阵条件”。
- 新第 105 行把具体构造保留为下一步；新第 107 行立即进入“从两张经典校验矩阵开始”。
- 新第 143–155 行保留三项复形与 `H_X=\partial_1`、`H_Z=\partial_2^T` convention。
- 新第 157 行进入乘积中间项，新第 187 行开始具体 HGP blocks 与两路径抵消，兑现 U02 的问题。
- 新第 394–447 行保留可选逻辑空间分解；`H_1` 前的句子与 Künneth owner anchor 继续提供 logical-space 落点。

## Heading anchors 与 links

- 正式文件共有 13 个标题，全部为 `###`；原 11 个标题均保留且层级不变，只新增 U02 的两个标题；无重复标题。
- `#从两张经典校验矩阵开始` 与 `#行与列的乘积方向` 两个既有入站 anchor 继续存在。
- `[[Künneth 分解#二项复形与 HGP 逻辑空间|Künneth 分解]]` 的目标文件与第 521 行 anchor 均存在。
- 两处 `[[Lifted product code]]` 均解析到唯一正式文件。
- 正式 HGP 中不存在 `Notes/WORKING`、task id、authoring task 或 draft 路径。

## Index / canonical

- `Notes/00-index.md`：未修改；HEAD/worktree blob 仍为 `847c0b231fd7471f49a445cb7f0d0426a53285cb`。
- `CANONICAL_KNOWLEDGE.md`：未修改；HEAD/worktree blob 仍为 `12b3fdb92c5214f4c6e48b54d3a6777cd76ead67`。
- 未新增、拆分、合并、改名或移动正式笔记。

## Preview 一致性与 Git 检查

- reader-visible 正文、删除范围、frontmatter、链接策略、index/canonical 决定均与 ready preview 一致。
- 目标文件整合后的规范化 Git blob 为 `3251b0075281fdf4dc86fccb230ae44397732bad`；工作树文件 SHA-256 为 `9e274216a8fa5e976b344b191cf0bcea5bdff83936be7141f7483db1e508fd2f`。
- `git diff --check`：通过。
- 写入正文后、生成本报告前，Git diff 仅包含正式 HGP 文件。
- Windows 工作树当前含由原 CRLF 正文与 apply_patch 新增 LF 切片形成的混合 EOL；`core.autocrlf=true` 会在未来 Git 写入时归一化。该现象不产生 reader-visible 或 Git 语义 diff，也未触发 `git diff --check`。
- 未暂存、未提交、未推送、未合并分支。

## 正式 HGP 精确 unified diff（zero-context）

以下为 `git diff --unified=0` 的完整语义 diff；只去除了 `---`／`+++` 文件标头末尾由 Git 输出的分隔制表符，使报告自身不含 trailing whitespace。全部 hunk 范围与增删行逐字一致。

```diff
diff --git a/Notes/07-Lifted-Product Code/Hypergraph product code.md b/Notes/07-Lifted-Product Code/Hypergraph product code.md
index d18e00e..3251b00 100644
--- a/Notes/07-Lifted-Product Code/Hypergraph product code.md
+++ b/Notes/07-Lifted-Product Code/Hypergraph product code.md
@@ -1 +1,105 @@
-Hypergraph-product code（HGP 码）把两张经典校验矩阵组织成一对自动对易的 CSS 校验矩阵。构造校验矩阵只需要 [[Chain complex 与 cochain complex]]、[[CSS码中的cochain complex]] 和 [[Cochain complex 的 tensor product]] 中的二项复形、CSS 方向与乘积边界。[[Künneth 分解]] 只在分析逻辑空间和简洁维数公式时使用，不是建立 HGP 构造或理解行／列乘积方向的前置。
+---
+note_type: reference
+entry_mode: guided
+status: reviewed
+---
+
+超图乘积构造是一种从两张经典二进制奇偶校验矩阵构造 CSS 量子码的方法。这类矩阵的每一行规定一条模 2 的奇偶校验条件。由这种构造得到的量子码称为 HGP 码：超图乘积构造是产生量子码的方法，HGP 码则是所得对象。
+
+在构造一个 HGP 码时，把作为输入的两张经典二进制奇偶校验矩阵记为 \(A\) 和 \(B\)，它们就是构造所用的两份经典种子输入。构造以它们为数据产生两张量子校验矩阵，并把这两张量子校验输出记为 \(H_X\) 和 \(H_Z\)。因此，\(H_X\)、\(H_Z\) 是由输入生成的输出，而不是 \(A\)、\(B\) 的别名。
+
+\(H_X\) 与 \(H_Z\) 的列对应同一组物理量子比特。对于这两张输出矩阵，一行中取值为 1 的列指出该行所表示的校验作用的物理量子比特位置，这些位置构成该行的支撑；具体而言，\(H_X\) 的每一行给出一条 X 型校验的支撑，\(H_Z\) 的每一行给出一条 Z 型校验的支撑。在这里，CSS 的当前要求是所有 X 型校验都与所有 Z 型校验彼此对易。怎样由构造本身保证两类校验彼此对易？
+
+### 从局部交换到矩阵条件
+
+要回答上一节的问题，第一步是把输出必须满足的对易要求化成一个可检验的矩阵条件。\(H_X\) 与 \(H_Z\) 的列对应同一组物理量子比特，每一行给出一条相应类型校验的支撑。把 \(H_X\) 的一行记为 \(x\)，把 \(H_Z\) 的一行记为 \(z\)。对列坐标 \(q\)，\(x_q=1\) 表示 X 型校验在该量子比特上作用 \(X\)，\(x_q=0\) 表示作用 \(I\)；相应地，\(z_q=1\) 表示作用 \(Z\)，\(z_q=0\) 表示作用 \(I\)。因此两条完整校验所对应的泡利算符为
+$$
+X(x)=\bigotimes_q X^{x_q},
+\qquad
+Z(z)=\bigotimes_q Z^{z_q}.
+$$
+符号 \(\bigotimes_q\) 表示把每个量子比特上的 \(I\)、\(X\) 或 \(Z\) 作用组合成整条校验。支撑本身只记录一行中的非零列；该行来自 \(H_X\) 还是 \(H_Z\)，才决定这些位置上分别作用 \(X\) 还是 \(Z\)。
+
+先看两条校验在同一个量子比特上分别作用 \(X\) 和 \(Z\) 时会发生什么。在计算基上，
+$$
+X|0\rangle=|1\rangle,
+\quad X|1\rangle=|0\rangle,
+\qquad
+Z|0\rangle=|0\rangle,
+\quad Z|1\rangle=-|1\rangle.
+$$
+于是
+$$
+XZ|0\rangle=|1\rangle=-ZX|0\rangle,
+\qquad
+XZ|1\rangle=-|0\rangle=-ZX|1\rangle.
+$$
+\(XZ\) 与 \(ZX\) 在这组基上的作用始终相差一个整体负号，所以同一量子比特上的这两种作用满足 \(XZ=-ZX\)。
+
+如果 \(X\) 和 \(Z\) 分处不同的量子比特，交换次序则不会产生负号。当前所需的张量因子等式是
+$$
+(X\otimes I)(I\otimes Z)
+=X\otimes Z
+=(I\otimes Z)(X\otimes I).
+$$
+更多量子比特的情形只是在其余位置插入 \(I\)，因此不同量子比特上的作用彼此对易。
+
+> [!note]- 补充推导：直接核对 \(XZ=-ZX\)
+> $$
+> X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
+> \qquad
+> Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
+> $$
+> $$
+> XZ=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
+> \qquad
+> ZX=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-XZ.
+> $$
+
+回到整条校验：每个共同位置都会贡献一个负号。非共同位置至少有一条校验作用 \(I\)，而分处不同位置的作用又彼此对易，因此交换两条完整校验时，
+$$
+X(x)Z(z)
+=(-1)^{\sum_q x_qz_q}Z(z)X(x)
+=(-1)^wZ(z)X(x),
+$$
+其中 \(w\) 是两条支撑共同位置的整数个数。\(w\) 为偶数时，局部负号成对抵消，两条校验对易；\(w\) 为奇数时，它们反对易。
+
+现在逐对汇总所有 X 型行与 Z 型行。第 \(i\) 条 X 型校验和第 \(j\) 条 Z 型校验对应的矩阵元为
+$$
+(H_XH_Z^T)_{ij}
+=\sum_q(H_X)_{iq}(H_Z)_{jq}
+\pmod 2.
+$$
+其中每一项只在两行的第 \(q\) 列都为 \(1\) 时贡献 \(1\)，所以这个矩阵元正是两行共同非零列数的奇偶。覆盖所有 \(i,j\) 后便得到
+$$
+H_XH_Z^T=0
+\quad\Longleftrightarrow\quad
+\text{每一对 X 型与 Z 型校验的重叠数均为偶数}
+\quad\Longleftrightarrow\quad
+\text{每条 X 型校验都与每条 Z 型校验对易}.
+$$
+共享物理列本身并不保证这个条件。例如，
+$$
+H_X=\begin{bmatrix}1\end{bmatrix},
+\qquad
+H_Z=\begin{bmatrix}1\end{bmatrix},
+\qquad
+H_XH_Z^T=\begin{bmatrix}1\end{bmatrix}\ne0,
+$$
+此时唯一的 X 型校验与 Z 型校验在同一位置重叠，因而不对易。
+
+### 三个空间与两支映射
+
+现在把同一个零矩阵条件换成整体映射的视角：
+$$
+C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0.
+$$
+这里，\(C_2\) 是以 Z 型校验为坐标的二进制向量空间，\(C_1\) 是以物理量子比特为坐标的二进制向量空间，\(C_0\) 是以 X 型校验为坐标的二进制向量空间。
+
+第一支映射 \(H_Z^T\) 把一组 Z 型校验的选择映到物理量子比特坐标上。它将所选 Z 型校验的行按模 \(2\) 相加；所得二进制向量中取值为 \(1\) 的物理坐标构成其支撑。
+
+第二支映射 \(H_X\) 接收一个物理支撑，并把它映成以 X 型校验为坐标的向量。输出的每个分量都记录该物理支撑与相应 X 型校验支撑的重叠奇偶。
+
+沿两支箭头连续作用得到的正是 \(H_XH_Z^T\)。当这个连续复合为零时，任意一组 Z 型校验的选择经过两步都会得到零；结合前面的逐行解释，这统一表达了每条 X 型校验都与每条 Z 型校验对易。
+
+这样一段由向量空间和线性映射组成、并满足连续两步复合为零的序列，就是这里所说的链复形。下一步就是由 \(A,B\) 构造这两支映射，并证明它们的复合恒为零。
@@ -53,19 +156,0 @@ $$
-因此
-
-$$
-H_1(C)=
-\frac{\ker H_X}{\operatorname{im}H_Z^T}
-$$
-
-表示 logical $Z$ support classes。对偶 cochain complex
-
-$$
-C_0^*
-\xrightarrow{H_X^T}
-C_1^*
-\xrightarrow{H_Z}
-C_2^*
-$$
-
-的 $H^1$ 表示 logical $X$ support classes。这里采用 chain 方向推导 HGP blocks；logical quotient 的一般解释仍由 [[CSS码中的cochain complex]] 承担。
-
```

## 未解决事项

无 blocker、`待核对`、`TODO：补引用` 或 `待补推导`。Formal integration 已按 preview 完成；等待用户审查工作树 diff，未自动提交。
