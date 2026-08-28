# Source packet scope

- task_id: 20260828-hgp-v5-pilot
- repository version checked: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6
- purpose: 为 Repository Mapper、Didactic Architect、Packet Builder 与两道审查提供已核对事实、精确锚点和可复算局部推导。
- isolation note: Writer 不得直接读取本文件。Packet Builder 只能把当前 unit 需要的局部事实／计算编译进 packet，并单独列出授权来源和目标旧片段。Blind Reader 不得读取本文件或下列来源。

# Source records

## S01 — 正式 HGP owner 与目标旧文

- source: Notes/07-Lifted-Product Code/Hypergraph product code.md
- version: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6 工作树版本。
- locations:
  - 第 1–23 行：旧 opening、A/B 输入与二项复形入口；
  - 第 39–70 行：三项链方向、H_X/H_Z convention 与 logical quotient；
  - 第 72–100 行：product spaces 与两类物理比特扇区；
  - 第 102–165 行：HGP blocks、两路径抵消与 CSS 零乘积；
  - 第 167 行以后：S007 convention、Tanner 边、参数与 LP 过渡。
- classification: repository canonical owner / target fragment。
- supported claims:
  - A、B 是两张经典种子校验矩阵；
  - HGP 产生 H_X、H_Z，目标采用 \(H_X=\partial_1,\ H_Z=\partial_2^T\)；
  - chain 方向的条件是 \(H_XH_Z^T=0\)；
  - 后续具体 HGP blocks 由两条相同 product paths 在 \(\mathbb F_2\) 中抵消而自动满足条件。
- unsupported or unsuitable:
  - 第 1 行把对象、自动对易、多个前置链接与 Künneth 边界压在同一段，不是新 opening 的语言样板；
  - 第 53–70 行的 logical quotient、第 72 行以后 product degree、blocks 与 Künneth 均不属于 U01/U02 的局部解释范围；
  - 原文没有从局部 Pauli 交换逐步推出偶数重叠。
- intended use:
  - Mapper／Architect：核对 owner、chain convention、后续 canonical detail 和重复范围；
  - Writer：只能读取 packet 明确授权的旧目标片段，不得读取整个正式文件；
  - Integration Preview：核对第 1、3–23、39–70、72–100、102–165 行的竞争、重复与不可丢失内容。

## S02 — CSS 矩阵、支撑与 cochain owner

- source: Notes/06-CCZ Distillation/CSS码中的cochain complex.md
- version: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6 工作树版本。
- locations:
  - 第 7–21 行：同为 n 列的 H_X、H_Z，两类行支撑与 \(H_ZH_X^T=0\)；
  - 第 23–32 行：二进制 X support 到 \(X(x)\)；
  - 第 48–75 行：校验选择经 \(H_X^T\) 映成支撑；
  - 第 110–140 行：三项 cochain 的三个空间、两个映射和零复合；
  - 第 142 行以后：logical quotient、例子、metacheck 与更深细节。
- classification: repository canonical owner / stable upstream detail。
- supported claims:
  - H_X、H_Z 共享物理量子比特列，行分别给出 X 型与 Z 型支撑；
  - CSS 对易可写为零矩阵乘积；
  - 校验选择经矩阵转置映为物理支撑；
  - 三项映射的零复合等于 CSS 零乘积。
- unsupported or unsuitable:
  - 来源采用 cochain 方向 \(H_ZH_X^T=0\)，需转置为本任务的 chain 方向；
  - 原文不提供异比特张量因子对易与 \((-1)^w\) 的完整局部推导；
  - stabilizer、logical、syndrome、metacheck 和英文混合表述均不授权进入 U01/U02。
- intended use:
  - 支撑 CSS 的局部含义、共享列、行支撑与三项映射；
  - 若 Packet Builder 授权 Writer，只给出任务相关摘录或内嵌自然中文重述，不把整个文件及其链接链传入。

## S03 — Chain complex owner

- source: Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md
- version: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6 工作树版本。
- locations:
  - 第 4–24 行：chain complex 与连续边界复合为零；
  - 第 28–170 行：几何例子、cycle、boundary、homology；
  - 第 173–210 行：cochain 方向与零复合。
- classification: repository canonical owner / stable upstream detail。
- supported claim: 一串向量空间与线性映射若连续两步复合为零，就具有本任务所需的 chain-complex 结构。
- unsupported or unsuitable:
  - degree、几何边界例子、cycle、boundary、homology 与 cohomology 都不属于 U02-P2 的出口；
  - 来源不替代对当前 C_2、C_1、C_0 坐标意义的局部解释。
- intended use: 在对象、映射与用途已由 packet 给出后，授权“链复形”当前局部名称；不复制 owner 的长证明。

## S04 — 单比特 Pauli 交换的稳定锚点

- source: Notes/03-Magic State基础/Clifford Twirling 与魔态错误模型.md
- version: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6 工作树版本。
- locations:
  - 第 777–791 行：Pauli 对易／反对易对应交换符号 \(+1/-1\)；
  - 第 1402–1410 行：\(ZX=iY,\ XZ=-iY\)，从而 \(XZ=-ZX\)。
- classification: repository stable Pauli source。
- supported claim: 同一量子比特上的 X、Z 交换次序贡献一个负号。
- unsupported or missing:
  - 没有在相邻局部范围直接证明不同量子比特上的作用对易；
  - 没有显式展示标准 \(2\times2\) 矩阵逐项相乘；
  - twirling 的其它推导与 HGP 无关。
- intended use:
  - 作为 PR04 的稳定来源与 Contract Auditor 的交叉核对；
  - 完整 \(2\times2\) 计算若需要，使用 LD01，而不得声称 S04 已逐项展示；
  - 用户已明确完整矩阵计算不是当前出口能力。

## S05 — 一般辛对易判据（只作交叉核对）

- source: Notes/01-量子纠错基础/逻辑基态的表示.md
- version: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6 工作树版本。
- location: 第 168–200 行。
- classification: repository cross-check source。
- supported claim: 二进制 Pauli 支撑有统一的矩阵化对易判据 \(H\Lambda H^T=0\)，逻辑 X/Z 的交换符号由配对决定。
- unsupported or unsuitable:
  - 一般辛矩阵、任意 X/Y/Z 稳定子和逻辑算符显著超出 U01/U02；
  - 不提供当前行重叠机制所需的渐进解释。
- intended use: Contract Auditor 数学一致性交叉核对；不授权 Writer 引入 \(\Lambda\)、一般 stabilizer 或 logical operator。

## S06 — Canonical ownership 与路线（只读定位）

- source:
  - CANONICAL_KNOWLEDGE.md:75–140；
  - CANONICAL_KNOWLEDGE.md:267–300；
  - Notes/00-index.md:43–47、63–77。
- version: Git 40ed879dab4601858db6a1a56742ad4fdb4fdaf6 工作树版本。
- classification: repository routing / ownership metadata。
- supported claims:
  - chain、CSS 与 HGP 的 canonical owner；
  - HGP 固定 blocks、zero composition 与后续职责；
  - HGP 在正式阅读路线中的现有位置。
- unsupported or unsuitable:
  - ownership、前置清单、路线、维护入口不是读者正文；
  - 不作为数学局部推导的替代。
- intended use: Mapper 与 Integration Preview 只读核对；严禁传入 Writer 或 Blind Reader。

## S07 — v4 pilot 历史证据

- source:
  - Notes/WORKING/authoring-tasks/20260828-hgp-v4-pilot/DOMAIN_MODEL.md；
  - Notes/WORKING/authoring-tasks/20260828-hgp-v4-pilot/SOURCE_PACKET.md。
- version: 历史任务保留版本；其仓库锚点已在当前 Git 40ed879 重新打开核对。
- classification: historical task artifact / navigation aid。
- supported use:
  - 提供上一轮 premise inventory 与 local-derivation 的候选；
  - 帮助定位 S01–S05。
- unsupported or stale:
  - 它不是当前数学权威；
  - v4 Writer packet 曾把显式 \(2\times2\) 计算作为主线必写，不能沿用为 v5 depth/placement 决定；
  - v4 没有 v5 的 canonical detail、latency、proportionality 或 Integration Preview 门。
- intended use: Mapper／Learner／Architect 的历史证据；不传入 Writer、Contract Auditor 或 Blind Reader，除非当前 packet 重新编译并独立授权其中已复核的局部事实。

# Conventions

- 所有支撑向量、奇偶和矩阵乘积均在 \(\mathbb F_2\) 上。
- 当前任务采用 chain 方向

  $$
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0,
  \qquad H_XH_Z^T=0.
  $$

- S02 采用对偶 cochain 方向 \(H_X^T\) 后接 \(H_Z\)，写作 \(H_ZH_X^T=0\)。二者互为转置，表达相同的 X 行／Z 行正交条件。
- A、B 始终是经典种子输入；H_X、H_Z 始终是量子校验输出。
- 当前中文术语：奇偶校验矩阵、X 型校验、Z 型校验、物理量子比特、行、列、支撑、共同位置、重叠、重叠奇偶、对易、反对易、二进制向量空间、映射、连续复合、链复形。
- 可保留：HGP、CSS 以及 A、B、H_X、H_Z、C_2、C_1、C_0、X、Z、I 等数学符号。
- 不授权以 X-type checks、row pair、support space、overlap parity、zero composition 等英文速记替代中文正文。

# Local derivations

以下计算提供可复算锚点。它们的存在不决定本次必须采用 full depth，也不决定 mainline／optional placement。

## LD00 — 一行怎样规定模 2 奇偶校验

设

$$
H\in\mathbb F_2^{m\times n},
\qquad c\in\mathbb F_2^n.
$$

第 i 个校验输出是

$$
(Hc)_i=\sum_{q=1}^n H_{iq}c_q\pmod2.
$$

第 i 行中 H_{iq}=1 的位置被计入该和。因此 \((Hc)_i=0\) 表示这些位置上 c_q 的 1 的个数为偶数；也就是这一行规定一条模 2 的奇偶校验条件。

- classification: local-derivation。
- limitation: 只解释“一行的条件”，不引入经典码 kernel、距离或编码。

## LD01 — 同一量子比特上的 X、Z 反对易

采用标准矩阵

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

直接相乘：

$$
XZ=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
ZX=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-XZ.
$$

所以 \(XZ=-ZX\)。结果与 S04 的 \(ZX=iY,\ XZ=-iY\) 一致。

同一事实还可在主线中作更短的计算基核验：`X` 交换 \(|0\rangle,|1\rangle\)，`Z` 保持 \(|0\rangle\) 并给 \(|1\rangle\) 一个负号，因此

$$
XZ|0\rangle=|1\rangle=-ZX|0\rangle,
\qquad
XZ|1\rangle=-|0\rangle=-ZX|1\rangle.
$$

两个算符在一组基上只差整体负号，故 \(XZ=-ZX\)。这一短核验与完整矩阵逐项相乘是不同 depth：前者可作 `compact_derivation / mainline`，后者仍只作 `optional_derivation`。

- classification: local-derivation / calculation-verified。
- depth boundary: 这是可用的 full \(2\times2\) 计算；用户明确它不是当前出口能力。不能因 learner evidence 为 unverified 就自动要求主线完整展示。

## LD02 — 不同量子比特上的局部作用对易

由张量积乘法规则

$$
(M\otimes N)(P\otimes Q)=MP\otimes NQ
$$

得到

$$
(X\otimes I)(I\otimes Z)=XI\otimes IZ=X\otimes Z,
$$

$$
(I\otimes Z)(X\otimes I)=IX\otimes ZI=X\otimes Z.
$$

两种次序相同。对更多量子比特，在其余张量因子插入 I，结论不变。

- classification: local-derivation / calculation-verified。
- source gap closed: 仓库稳定来源没有在相邻局部范围直接给出这一证明。

## LD03 — 二进制行支撑到整条校验算符

对 x、z 属于 \(\mathbb F_2^n\)，定义

$$
X(x)=\bigotimes_{q=1}^n X^{x_q},
\qquad
Z(z)=\bigotimes_{q=1}^n Z^{z_q}.
$$

当 x_q=0 时 \(X^{x_q}=I\)，当 x_q=1 时 \(X^{x_q}=X\)；Z 型同理。这正把二进制行的 1/0 读成支撑位置／非支撑位置上的 X 或 I、Z 或 I。

- classification: local-derivation / calculation-verified。
- stable cross-check: S02:15–29 给出 X support 的同一表示。

## LD04 — 共同位置数决定总交换符号

在单个位置 q，

$$
X^{x_q}Z^{z_q}
=(-1)^{x_qz_q}Z^{z_q}X^{x_q}.
$$

只有 x_q=z_q=1 时指数为 1，并由 LD01 贡献负号。不同位置间的重排按 LD02 对易。因此

$$
X(x)Z(z)
=(-1)^{\sum_qx_qz_q}Z(z)X(x)
=(-1)^wZ(z)X(x),
$$

其中 w 是两条支撑共同位置的整数个数。w 为偶数时负号成对抵消，两条校验对易；w 为奇数时反对易。

- classification: local-derivation / calculation-verified。

## LD05 — 矩阵元就是对应两行的重叠奇偶

设 h_i 是 H_X 第 i 行，g_j 是 H_Z 第 j 行。矩阵乘法给出

$$
(H_XH_Z^T)_{ij}
=\sum_{q=1}^n(H_X)_{iq}(H_Z)_{jq}
=\sum_{q=1}^n(h_i)_q(g_j)_q
\pmod2.
$$

乘积项仅在两行第 q 列都为 1 时贡献 1，因此该值是共同非零列数的模 2 奇偶。结合 LD04，

$$
H_XH_Z^T=0
\Longleftrightarrow
\text{每一对异型行的重叠数为偶数}
\Longleftrightarrow
\text{所有 X 型与 Z 型校验彼此对易}.
$$

- classification: local-derivation / calculation-verified。
- completeness: 第一个等价逐个覆盖所有 i,j；第二个等价使用 LD04，没有省略 explanation premise。

## LD06 — 共享列不自动推出零乘积

取

$$
H_X=\begin{bmatrix}1\end{bmatrix},
\qquad
H_Z=\begin{bmatrix}1\end{bmatrix}.
$$

它们共享同一个物理量子比特列，但

$$
H_XH_Z^T=\begin{bmatrix}1\end{bmatrix}\ne0.
$$

相应 X 与 Z 在唯一共同位置上反对易。因此“共享列”只说明两张矩阵使用同一组坐标，不保证 CSS 对易。

- classification: local-derivation / calculation-verified。
- limitation: 该反例不用于推断其它码性质。

## LD07 — 三项箭头的坐标与连续复合

令

$$
C_2=\mathbb F_2^{r_Z},
\qquad
C_1=\mathbb F_2^n,
\qquad
C_0=\mathbb F_2^{r_X}.
$$

若 s 属于 C_2 是 Z 型校验选择向量，则

$$
H_Z^Ts\in C_1
$$

是被选 Z 型行支撑的模 2 叠加。若 v 属于 C_1 是物理支撑，则

$$
(H_Xv)_i
=\sum_q(H_X)_{iq}v_q
$$

是 v 与第 i 条 X 型校验支撑的重叠奇偶。因此连续两步为

$$
s\longmapsto H_Z^Ts
\longmapsto H_XH_Z^Ts.
$$

零复合 \(H_XH_Z^T=0\) 正是 LD05 的全部异型校验对易条件。对象、坐标、映射和用途在此均已明确；“链复形”名称由 S03 授权。

- classification: local-derivation / calculation-verified。

# Canonical detail and duplication handoff

- CSS／Pauli 上游已有 detail：
  - S02 已承担共享列、行支撑、零乘积、校验选择到支撑和三项 cochain 映射；
  - S04 已承担 Pauli 交换符号及单比特 X/Z 乘法恒等式；
  - S03 已承担一般 chain/cochain、零复合及更深的 (co)homology；
  - S05 提供一般辛判据，但不适合当前读者主线。
- 局部缺口由 LD00–LD07 闭合；这些 local derivations 不自动成为正文 full derivation。
- 完整 \(2\times2\) Pauli 计算不是当前出口能力。若 packet 保留它，必须显式说明用途与 placement；不得让它替代 HGP 主问题。
- 正式目标重复范围：
  - 第 1 行与新 U01 opening 直接竞争；
  - 第 3–23 行与 A/B 输入角色部分重复，但含后续所需尺寸与二项复形数据；
  - 第 39–51 行与 U02-P2 三项箭头直接重复；
  - 第 53–70 行含本次不写、但整合时不得丢失的 logical quotient；
  - 第 72–100 行是一般箭头的 HGP-specific product-space 实例化；
  - 第 102–165 行应继续承担 blocks 与两路径抵消，第 156–165 行会重复零复合结论。
- 上述只是 fit inventory；替换／插入及链接策略必须由 manuscript pass 后的只读 Integration Preview 决定。

# Source authorization boundary

| material | Mapper / Architect | Packet Builder | Writer | Contract Auditor | Blind Reader |
|---|---|---|---|---|---|
| S01 指定旧目标片段 | read | may authorize excerpt | excerpt only | packet-authorized excerpt | no |
| S02–S04 | read | may embed/authorize relevant facts | only explicitly authorized source/excerpt | yes if packet-authorized | no |
| S05 | cross-check | do not pass by default | no | cross-check only | no |
| S06 canonical/index | read | no | no | no | no |
| S07 v4 task artifacts | historical evidence | no direct pass | no | no | no |
| LD00–LD07 | read | compile selected derivation into packet | packet content only | yes through packet/source authorization | no |
| Reader Card + Draft + language profile | not applicable here | produce later | draft role only | separate context | sole allowed review context |

# Unsupported claims and forbidden extrapolations

- 不得把 A、B 称作最终 H_X、H_Z。
- 不得宣称任意共享列矩阵 pair 自动满足 CSS 对易。
- 不得从 \(H_XH_Z^T=0\) 单独推出距离、逻辑比特数、qLDPC 或其它码参数。
- 不得声称 S04 已直接证明异比特对易；该缺口由 LD02 计算闭合。
- 不得把一般辛表示、stabilizer group、logical quotient、syndrome 或 metacheck 引入 U01/U02。
- 不得把 Kronecker blocks、A/B 尺寸、total degree、两路径抵消、homology 或 Künneth 提前写入 U01/U02。
- 不得把 S06 的 ownership、路线、维护边界或 wikilink 串传入 Writer／正文。
- 不得因某项 learner capability 为 unverified 自动选择 full derivation。

# Verification status and blocker

- S01–S06 的全部列出锚点已在当前 v5 分支实际打开核对。
- LD00–LD07 已逐式复算；未使用未说明的模型常识补齐 Pauli premises。
- chain/cochain transpose convention 已核对，无数学冲突。
- blocker: 无。
