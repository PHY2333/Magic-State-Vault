# 已实际读取

- `Notes/WORKING/authoring-tasks/20260827-hgp-v3-pilot/TASK.md`
- `Notes/WORKING/authoring-tasks/20260827-hgp-v3-pilot/BRIEF.md`
- `Notes/NOTE_TYPES.md`
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`
- `Notes/06-CCZ Distillation/CSS码中的cochain complex.md`
  - 采用“CSS 码先给出两张矩阵”“把 CSS 商空间写成 cochain 语言”“注意 convention”中的矩阵方向和对易条件。
- `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`
  - 采用“chain complex：边界映射连续两次为零”中的三项箭头和复合为零定义。
- `CANONICAL_KNOWLEDGE.md`
  - 采用“Hypergraph product code”“CSS 码的 cochain complex”“Chain complex、cochain complex 与 (co)homology”条目。
- `Notes/00-index.md`
  - 只用于确认目标文件是 lifted-product 主线的 HGP 核心入口；不把路线存在性当作 learner evidence。

# 知识单元

## K01 — HGP 的构造类别

- formal_statement：Hypergraph-product code construction 以两张经典二进制校验矩阵为种子，构造一对满足 CSS 对易条件的量子校验矩阵；“HGP”既可指该构造，也可指由此得到的码。
- conditions：输入矩阵在 \(\mathbb F_2\) 上；本单元不承诺距离、稀疏性或逻辑维数。
- canonical_owner：`Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- source_anchors：目标文件开头、“从两张经典校验矩阵开始”；`CANONICAL_KNOWLEDGE.md` 的“Hypergraph product code”。
- verification：`verified`。

## K02 — HGP 的输入与输出

- formal_statement：输入是两张经典校验矩阵，当前用 \(A,B\) 标记；输出是作用在同一批物理量子比特上的 \(X\)-type 与 \(Z\)-type check matrices，分别记为 \(H_X,H_Z\)。
- conditions：U01 只把 \(A,B\) 当作二进制矩阵，不引入其尺寸、Kronecker blocks 或行列乘积坐标。
- canonical_owner：`Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- source_anchors：目标文件“从两张经典校验矩阵开始”“HGP 校验矩阵与对易”。
- verification：`verified`。

## K03 — CSS 两类 checks 与共享物理列

- formal_statement：\(H_X\) 与 \(H_Z\) 具有相同列数；每一列对应同一批物理量子比特中的一个位置，\(H_X\) 的每行给出一条 \(X\)-type check 的 support，\(H_Z\) 的每行给出一条 \(Z\)-type check 的 support。
- conditions：局部解释只使用“同一批物理量子比特、两类 checks、彼此对易”，不调用 stabilizer code、stabilizer group 或 logical quotient。
- canonical_owner：`Notes/06-CCZ Distillation/CSS码中的cochain complex.md`。
- source_anchors：该文件“CSS 码先给出两张矩阵”。
- verification：`verified`。

## K04 — CSS 对易的矩阵条件

- formal_statement：\(H_XH_Z^T\) 的第 \((i,j)\) 个元素是第 \(i\) 条 \(X\)-type check 与第 \(j\) 条 \(Z\)-type check 的二进制 support overlap；所有异型行对彼此对易等价于
  \[
  H_XH_Z^T=0.
  \]
- conditions：所有矩阵和 overlap parity 在 \(\mathbb F_2\) 上；`CSS码中的cochain complex.md` 使用转置后的等价写法 \(H_ZH_X^T=0\)。
- canonical_owner：`Notes/06-CCZ Distillation/CSS码中的cochain complex.md`；HGP convention 由目标文件承担。
- source_anchors：目标文件“HGP 校验矩阵与对易”；CSS 文件“CSS 码先给出两张矩阵”“注意 convention”。
- verification：`verified`。

## K05 — 任意矩阵对不自动满足 CSS 对易

- formal_statement：两张矩阵即使具有相同列数，其行 overlap matrix 也可能非零；因此任意指定 \(H_X,H_Z\) 不能保证 \(H_XH_Z^T=0\)。
- conditions：这是 K04 的直接线性代数推论，不主张任意非对易矩阵都来自某种量子码。
- canonical_owner：该判断服务于 `Notes/07-Lifted-Product Code/Hypergraph product code.md` 的自动对易动机。
- source_anchors：目标文件“HGP 校验矩阵与对易”末句；K04。
- verification：`inference`，依据 K04 可直接验证。

## K06 — 三项箭头的空间角色

- formal_statement：取
  \[
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0.
  \]
  \(C_1\) 是物理量子比特 support 的二进制向量空间；\(C_2\) 的坐标承载 \(Z\)-type checks 的线性组合；\(C_0\) 的坐标承载对所有 \(X\)-type checks 的 overlap 结果。
- conditions：U02 只要求读者操作 \(C_1\) 的物理含义和两侧 checks 的角色，不引入 \(A,B\) 的尺寸、product blocks 或 total-degree 公式。
- canonical_owner：目标文件的 HGP chain convention；一般 chain 定义由 `Chain complex 与 cochain complex.md` 承担。
- source_anchors：目标文件“从两张经典校验矩阵开始”；CSS 文件“注意 convention”。
- verification：`verified`。

## K07 — 连续两步为零承接自动对易

- formal_statement：三项箭头的复合是
  \[
  C_2\xrightarrow{\,H_XH_Z^T\,}C_0.
  \]
  因而“连续两步为零”与 \(H_XH_Z^T=0\) 是同一条件；若构造先保证这串映射的复合为零，CSS 对易便由构造本身保证。
- conditions：U02 不展开 HGP 的 Kronecker blocks 如何具体实现该零复合。
- canonical_owner：`Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- source_anchors：目标文件“HGP 校验矩阵与对易”；`Chain complex 与 cochain complex.md` 的“chain complex：边界映射连续两次为零”。
- verification：`verified`。

## K08 — 链复形名称的当前深度

- formal_statement：一串线性映射若连续两步复合为零，就满足 chain-complex condition；在读者已经看到 K06、K07 的对象和用途后，可把这张三项图命名为“链复形”。
- conditions：当前只提供名称和零复合条件，不引入 degree、homology、cochain 对偶或 logical quotient。
- canonical_owner：`Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`。
- source_anchors：该文件“chain complex：边界映射连续两次为零”。
- verification：`verified`。

## K09 — 当前明确不进入正文的后续事实

- formal_statement：HGP 的具体 blocks 使用 Kronecker products，并通过 \(\mathbb F_2\) 中两条 \(A\otimes B\) 路径抵消实现 K07；Künneth 只参与后续逻辑空间分析。
- conditions：U01/U02 不使用、解释或命名这些事实。
- canonical_owner：`Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- source_anchors：目标文件“HGP 校验矩阵与对易”“长度、秩与可选逻辑空间分解”。
- verification：`verified`，但 `out of scope`。

# Formal dependencies

| dependent | requires | reason |
|---|---|---|
| K04 CSS 对易条件 | K03 共享物理列与两类 check rows | 矩阵乘积的元素只有在列坐标表示同一物理位置时才是异型 checks 的 overlap。 |
| K05 任意矩阵对不自动对易 | K04 CSS 对易条件 | 只要 overlap matrix 可能非零，就不能由“有两张矩阵”推出对易。 |
| K07 连续两步为零 | K06 三项箭头；K04 CSS 对易条件 | 两张映射的复合恰为 \(H_XH_Z^T\)。 |
| K08 链复形名称 | K07 连续两步为零 | chain-complex condition 的定义就是相邻映射复合为零。 |
| K09 具体 HGP blocks | K01、K02、K07 | blocks 是输入矩阵产生输出映射并实现零复合的后续具体机制。 |

# Explanatory dependencies

| target_explanation | requires_reader_capability | reason |
|---|---|---|
| 区分 HGP 输入与输出 | 能区分“经典种子矩阵”和“量子码的两类 check matrices” | 否则 \(A,B\) 与 \(H_X,H_Z\) 会被误读成同一层对象。 |
| 理解 CSS 对易问题 | 能把两张输出矩阵的行读成作用在同一物理列空间上的两类 checks | 对易条件讨论的是每一对异型 rows 的 overlap。 |
| 理解 \(H_XH_Z^T=0\) | 能把矩阵乘积读成所有异型 check pairs 的 overlap 汇总 | 仅看到公式不足以知道其物理用途。 |
| 理解三项箭头 | 能识别 \(C_1\) 是物理 support 空间，左右映射分别由两类 checks 给出 | 这使零复合重新落回 CSS 对易问题。 |
| 理解“链复形”名称 | 已理解当前三项箭头及连续两步为零的用途 | 名称不应先于对象和需求出现。 |

# Motivational relations

| predecessor_problem_or_result | motivates | reason |
|---|---|---|
| 输入 \(A,B\) 需要产生量子校验 | 输出 \(H_X,H_Z\) 的区分 | 构造任务必须先说明要得到哪两类 checks。 |
| 任意 \(H_X,H_Z\) 不保证对易 | 寻找由构造保证 \(H_XH_Z^T=0\) 的组织方式 | 这是真实的自动对易障碍。 |
| \(H_XH_Z^T=0\) 是两个映射的零复合 | 三项箭头整体图景 | 箭头把对易等式解释为结构性条件。 |
| 三项箭头的用途已经明确 | “链复形”名称 | 名称此时压缩已经理解的对象，不替代解释。 |

# Reference relations

| knowledge_unit | owner | owned_scope |
|---|---|---|
| K01、K02、K05、K07、K09 | `Notes/07-Lifted-Product Code/Hypergraph product code.md` | HGP 构造、自动对易、具体 product blocks 与后续边界。 |
| K03、K04 | `Notes/06-CCZ Distillation/CSS码中的cochain complex.md` | CSS matrices、行列方向与对易条件的一般解释。 |
| K08 | `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md` | chain complex 与连续两步为零的一般定义。 |
| HGP 在学习路线中的入口职责 | `Notes/00-index.md` | 读者路线与入口描述，不承担数学定义。 |
| HGP canonical ownership | `CANONICAL_KNOWLEDGE.md` | 长期归属、固定 convention 和边界索引。 |

# 约定与边界

- 所有矩阵均在 \(\mathbb F_2\) 上。
- 当前采用目标文件的 chain convention：
  \[
  H_Z^T:C_2\to C_1,\qquad H_X:C_1\to C_0.
  \]
- \(H_XH_Z^T=0\) 与相关 CSS 笔记中的 \(H_ZH_X^T=0\) 互为转置，是同一逐行对易条件。
- U01/U02 不把 canonical owner 当作读者前置，不把仓库中已有笔记当作 learner evidence。
- 本 pilot 不改变目标文件的长期 ownership、索引位置或正式正文。

# 缺失与冲突

- 未发现数学或来源冲突。
- 未重新核对目标文件末尾列出的外部论文；本次 onboarding 的承诺由当前仓库三处相互一致的正式表述和直接矩阵复合验证支撑。
- HGP blocks 怎样由 \(A,B\) 具体生成三项对象属于下一单元，不在本 pilot 中承诺。

# 可供设计使用的结论

- 可以从 HGP 类别与 \(A,B\to H_X,H_Z\) 的构造任务进入。
- CSS 只能用普通语言局部解释为共享物理列的两类 checks，并指出它们必须彼此对易。
- 自动对易的真实障碍是任意 \(H_X,H_Z\) 不保证 \(H_XH_Z^T=0\)。
- 三项箭头可以在不展开 blocks 的情况下，把零复合与 CSS 对易识别为同一条件。
- “链复形”名称只能在整体图景和用途已经出现后引入。
- U01/U02 必须排除 K09 的所有后续内容。
