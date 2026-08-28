---
status: designed
design_revision: 3
based_on_learner_revision: 1
---

# 目标表现

1. 读者能用一句话说明 HGP 是由两张经典二进制校验矩阵构造 CSS 量子码的方法或由此得到的一类码。
2. 读者能把 \(A,B\) 指认为输入，把 \(H_X,H_Z\) 指认为输出，并说明后两者分别承载 X-type 与 Z-type checks。
3. 读者能解释为什么任意两张输出矩阵不够：所有异型 check rows 必须彼此对易。
4. 读者能说明 \(H_XH_Z^T=0\) 汇总了所有异型 row pairs 的对易条件。
5. 读者能用
   \[
   C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0
   \]
   解释连续两步为零如何把自动对易写成构造自身的条件，并在用途出现后识别“链复形”名称。

# 文件决策

| file | note_type | entry_mode | draft_strategy | action | reason |
|---|---|---|---|---|---|
| `Notes/07-Lifted-Product Code/Hypergraph product code.md` | `reference` | `guided` | `unit-fragments` | 只生成 U01/U02 staged onboarding，不整合 | 文件长期承担 HGP canonical reference；短小 guided onboarding 负责第一次入口，不改变长期职责，也不足以拆成独立 lesson。 |

# Units

## U01 — HGP 的类别、输入与构造任务

- entry_capabilities：
  - 只把 CSS、X-type check、Z-type check 当作见过的名称；不假设能解释或操作。
  - 不要求任何 HGP、check-matrix 行列、Kronecker、chain/cochain 或 \(\mathbb F_2\) 运算能力。
- exit_capability：
  - 能说明 HGP 的构造类别；
  - 能区分输入 \(A,B\) 与输出 \(H_X,H_Z\)；
  - 能提出构造必须解决的唯一当前问题：怎样由构造本身保证两类 checks 对易。
- why_now：现有开头需要先给第一次接触者一个对象落点和具体构造任务，再进入任何公式或工具名称。
- primary_pattern：类别定位 → 基本数据 → 当前构造任务。
- supporting_pattern：在结尾使用“问题 → 障碍”的前两步，只提出自动对易障碍，不提前给工具。

### Phases

#### U01-P1 — 建立类别与第一句术语闭包

- cognitive_job：第一句把 HGP 放到“由两张经典二进制校验矩阵构造 CSS 量子码”的类别中；紧接着分别用普通语言闭合“经典二进制校验矩阵”和 CSS 的当前含义。
- new_entities：HGP；经典二进制校验矩阵这一输入类别；CSS 量子码；同一批物理量子比特上的两类 checks。
- new_relations：HGP 以两张 0/1 经典校验关系表为输入并构造量子码；两类 checks 必须彼此对易。
- new_notation：无。
- holding_set：HGP 是一种构造；输入类别是两张记录经典校验关系的 0/1 矩阵；目标量子码有 X-type 与 Z-type 两组 checks。
- consolidation：先用一句话确认“两张经典矩阵是输入素材”，再把 CSS 当前所需含义压缩为“两组作用在同一批物理量子比特上的 checks，并且彼此对易”。

#### U01-P2 — 区分输入与输出

- cognitive_job：为 P1 已闭合的两张经典输入绑定 \(A,B\)，再引入 \(H_X,H_Z\) 作为两类量子输出。
- new_entities：输入矩阵 \(A,B\)；输出矩阵 \(H_X,H_Z\)。
- new_relations：\(A,B\) 是构造素材；\(H_X,H_Z\) 分别收集 X-type/Z-type checks。
- new_notation：\(A,B,H_X,H_Z\)。
- holding_set：两张输入不等于两张输出；输出两矩阵作用在同一批物理量子比特上。
- consolidation：用“输入 \(A,B\)；输出 \(H_X,H_Z\)”的对照句释放四个符号的负荷。

#### U01-P3 — 提出自动对易问题

- cognitive_job：指出构造不只要给出两张输出矩阵，还必须保证两类 checks 对易；以问题句结束。
- new_entities：无。
- new_relations：任意矩阵对不自动满足对易要求；HGP 必须结构性保证该要求。
- new_notation：无；不出现 \(H_XH_Z^T\)。
- holding_set：输出 pair 与对易要求。
- consolidation：结尾只保留问题：“怎样由构造本身保证两组 checks 对易？”

### Concept action ledger

| concept_or_capability | evidence_state | action | first_allowed_phase | local_explanation | explanation_dependencies |
|---|---|---|---|---|---|
| HGP 构造类别 | `unseen` | `introduce` | U01-P1 第一句 | 从两张经典二进制校验矩阵构造 CSS 量子码的方法或由此得到的一类码 | 依赖同 phase 随后立即闭合的“经典二进制校验矩阵”输入标签与 CSS 当前含义 |
| CSS 名称 | `named` | `introduce` | U01-P1 第一句后 | 两组作用在同一批物理量子比特上的 X-type 与 Z-type checks，并且它们需要彼此对易 | X/Z-type 只作两类标签；“同一批物理量子比特”在同句说明 |
| stabilizer code / stabilizer group / logical quotient | `unverified` | `omit` | 不出现 | 无 | 无 |
| 经典二进制校验矩阵这一输入类别 | `unseen` | `introduce` | U01-P1 第一句后 | 由 0/1 组成并记录经典校验关系的矩阵；当前不解释行列细节 | 普通语言“0/1 矩阵、校验关系” |
| \(A,B\) | `unseen` | `introduce` | U01-P2 | 两张经典输入矩阵的短标签 | 经典二进制校验矩阵已在上一 phase 闭合 |
| \(H_X,H_Z\) | `unseen` | `introduce` | U01-P2 | 分别收集 X-type 与 Z-type checks 的输出矩阵 | CSS 局部解释已在 U01-P1 闭合 |
| check rows 与共享物理 columns | `unverified` | `delay` | U02-P1 | U01 只说两矩阵作用在同一批物理量子比特上，不操作行列 | U02-P1 局部解释 |
| \(H_XH_Z^T=0\) | `unverified` | `delay` | U02-P1 | U01 不出现公式 | U02-P1 闭合 |
| “链复形”名称 | `named` | `delay` | U02-P2 末尾 | U01 不出现 | U02-P2 在对象与用途后命名 |
| 解释三项箭头与零复合 | `unverified` | `delay` | U02-P2 | U01 不出现 | U02-P2 闭合 |
| Künneth 名称 | `named` | `omit` | 不出现 | 无 | 无 |
| 说明 Künneth 用途 | `unverified` | `omit` | 不出现 | 无 | 无 |
| Kronecker 名称 | `named` | `omit` | 不出现 | 无 | 无 |
| 执行 Kronecker 操作 | `unverified` | `omit` | 不出现 | 无 | 无 |
| 解释 \(\mathbb F_2\) 两路径抵消 | `unverified` | `omit` | 不出现 | 无 | 无 |
| qLDPC、LP、距离相关能力 | `unverified` | `omit` | 不出现 | 无 | 无 |

### Local definition closure

- “CSS”局部解释的全部词汇依赖：
  - “两组”与“同一批”是普通语言；
  - “物理量子比特”在当前句中指输出 checks 共同作用的位置；
  - X-type/Z-type 只标记两种 check 类别，不调用 stabilizer；
  - “对易”当前只说明两类 checks 必须相容地共同成立，具体矩阵判据延后到 U02-P1。
- “经典二进制校验矩阵”在 U01-P1 第一句之后立即闭合：它是由 0/1 组成并记录经典校验关系的矩阵；不使用 code kernel、syndrome 或行列角色解释。
- HGP 第一句中的两个新标签都在同一 phase 紧接着闭合：先闭合经典输入类别，再闭合 CSS 当前含义。
- \(A,B,H_X,H_Z\) 均在出现的同一句明确绑定输入或输出。

### Opening contract

- first_sentence_job：只说明 HGP 是从两张经典二进制校验矩阵构造 CSS 量子码的方法或由此得到的一类码。
- first_paragraph_job：紧接第一句闭合经典二进制校验矩阵与 CSS 的当前普通语言含义；下一段再绑定 \(A,B,H_X,H_Z\) 并建立输入层与输出层的区别。
- allowed_vocabulary：HGP、经典、二进制、校验矩阵、CSS 量子码、物理量子比特、X-type check、Z-type check、对易、构造。
- notation_budget：\(A,B,H_X,H_Z\)，总计四个符号；不出现尺寸。
- link_budget：0。
- forbidden_terms_topics：Künneth、qLDPC、LP、距离、canonical、ownership、前置、不是前置、wikilink、stabilizer code、stabilizer group、logical quotient、chain/cochain、Kronecker、total degree、任务或审查语言。
- closing_job：只提出“怎样由构造本身保证两组 checks 对易”，不回答、不写矩阵条件。

### Math and sources

- required_math：
  - \(A,B\) 是输入；\(H_X,H_Z\) 是输出；
  - 输出是作用在同一批物理量子比特上的两类 checks；
  - 任意给出两张输出矩阵不能自动保证对易。
- example：不安排数值例子；本 unit 的动作是识别类别和构造任务，例子会引入额外行列负荷。
- source_anchors：`SOURCE_PACKET.md` 的 S01、S02、S05、S06。
- unsupported_claims：不声称具体 blocks、尺寸、距离、稀疏性、逻辑空间或下游用途。

## U02 — 从 CSS 对易条件到三项箭头整体图景

- entry_capabilities：
  - 来自 U01：能区分 \(A,B\) 输入与 \(H_X,H_Z\) 输出；
  - 来自 U01：知道 \(H_X,H_Z\) 是作用在同一批物理量子比特上的两类 checks；
  - 来自 U01：能提出构造必须保证两类 checks 对易的问题。
- exit_capability：
  - 能解释 \(H_XH_Z^T=0\) 为什么汇总所有异型 row pairs 的对易；
  - 能说明任意矩阵 pair 不保证该条件；
  - 能用三项箭头把连续两步为零与 CSS 自动对易识别为同一件事；
  - 在对象与用途已经明确后，能识别这是一段链复形。
- why_now：U01 已经产生自动对易问题；U02 先把问题写成可核对公式，再给出能够结构性保证该公式的简化整体。
- primary_pattern：问题 → 障碍 → 工具 → 解决 → 作用。
- supporting_pattern：整体 → 部件 → 重新组装；整体图只承担当前自动对易用途。

### Phases

#### U02-P1 — 先建立对易问题

- cognitive_job：沿固定微顺序把两类 checks 的共享物理列、0/1 row support、overlap parity 与逐对对易压缩为 \(H_XH_Z^T=0\)，并明确任意矩阵 pair 不保证它。
- new_entities：check row；共享物理列空间；row-pair overlap matrix。
- new_relations：
  - \(H_X,H_Z\) 的列指向同一批物理量子比特；
  - 每行用 0/1 标出一条相应类型 check 作用的位置；
  - 乘积的一个元素把一对异型 rows 共同为 1 的列数按模 2 记录；
  - 元素为 0 表示共同作用位置为偶数个，而偶数次 X/Z 交叠的符号反转成对抵消，所以该 row pair 对易；
  - 整个 \(H_XH_Z^T\) 为零表示所有异型 row pairs 都对易。
- new_notation：\(H_Z^T\)、\(H_XH_Z^T=0\)；\(H_X,H_Z\) 已由 U01 引入。
- holding_set：共享列 → 共同为 1 的位置数 → 模 2 为零 → 偶 overlap → 单个 row pair 对易 → 全矩阵为零。
- consolidation：
  - 中途先总结“矩阵的一个元素只检查一对 rows”；
  - phase 末尾再总结“全零矩阵同时覆盖所有 row pairs，因此 CSS 对易是输出必须通过的整体条件，不是任意 pair 自动拥有的性质”。
- hard_boundary：本 phase 不出现 \(A,B\) 尺寸、\(C_2,C_1,C_0\)、chain complex 名称或任何 product block。

#### U02-P2 — 再给三项箭头整体

- cognitive_job：先展示三项箭头，再解释中间物理空间和两侧 check roles，最后把连续两步为零重新组装为 \(H_XH_Z^T=0\)；完成后才命名链复形。
- new_entities：\(C_2,C_1,C_0\) 三个位置；链复形名称只在 phase 末尾出现。
- new_relations：
  - \(H_Z^T\) 把 Z-type checks 的组合送入物理 support 空间 \(C_1\)；
  - \(H_X\) 从 \(C_1\) 读出与所有 X-type checks 的 overlap；
  - 连续两步为零等价于 CSS 对易。
- new_notation：\(C_2,C_1,C_0\) 与
  \[
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0.
  \]
- holding_set：左侧 Z-check combinations → 中间 physical-qubit space → 右侧 X-check overlap results。
- consolidation：回到 U01 的问题，说明 HGP 下一步只需让输入 \(A,B\) 具体生成一串满足零复合的映射；不设计或预告 U03 细节。
- hard_boundary：不引入 Kronecker blocks、\(A,B\) 的线性映射尺寸、total-degree 公式、\(A\otimes B+A\otimes B=0\)、homology 或 cochain 迁移。

### Concept action ledger

| concept_or_capability | evidence_state | action | first_allowed_phase | local_explanation | explanation_dependencies |
|---|---|---|---|---|---|
| \(H_X,H_Z\) 输出角色 | `introduced` by U01 | `use` | U02-P1 | 直接承接 U01 两类输出 | U01 exit |
| 共享物理列空间 | `unverified` | `introduce` | U02-P1 | 两矩阵的同一列位置指向同一个物理量子比特 | U01 已说明两矩阵作用于同一批物理量子比特 |
| 每行是一条 check | `unverified` | `introduce` | U02-P1 | 一行用 0/1 标出该 check 作用的物理位置 | 共享列已在同 phase 更早解释 |
| 把 row-pair overlap 读成二进制乘积元素 | `unverified` | `introduce` | U02-P1 | 找出两行共同为 1 的列，计数后按模 2 保留奇偶；该值就是乘积中对应元素 | row 角色与共享列已闭合 |
| 偶 overlap 对应异型 checks 对易 | `unverified` | `introduce` | U02-P1 | 每个共同位置带来一次 X/Z 符号反转；偶数次反转成对抵消 | 共同为 1 的列数与奇偶已在同 phase 更早解释 |
| \(H_XH_Z^T=0\) | `unverified` | `introduce` | U02-P1 | 每个元素为零表示对应 row pair 有偶 overlap 并对易；全矩阵为零覆盖所有异型 row pairs | 二进制 overlap 与偶 overlap 对易均已闭合 |
| 任意 pair 不自动对易 | `unverified` | `introduce` | U02-P1 | 相同列空间不强制 overlap matrix 为零 | \(H_XH_Z^T\) 已解释 |
| \(C_1\) | `unverified` | `introduce` | U02-P2 | 物理量子比特 support 空间 | U02-P1 已建立共享物理列 |
| \(C_2,C_0\) | `unverified` | `introduce` | U02-P2 | 左侧承载 Z-type check combinations；右侧承载 X-type overlap results | check row 与 \(C_1\) 已解释 |
| 连续两步为零 | `unverified` | `introduce` | U02-P2 | 两个箭头的复合就是 \(H_XH_Z^T\)，零复合即 CSS 对易 | U02-P1 公式与本 phase 箭头角色 |
| “链复形”名称 | `named` | `introduce` | U02-P2 最后一段 | 对已经建立的“相邻线性映射复合为零”结构命名 | 三项箭头和零复合用途均已在前文解释 |
| 理解 \(A,B\) 的尺寸与映射角色 | `unverified` | `delay` | 下一单元 | 本 pilot 不出现 | 无 |
| 理解具体 HGP blocks 如何生成 | `unverified` | `delay` | 下一单元 | 本 pilot 不出现 | 无 |
| Künneth 名称 | `named` | `omit` | 不出现 | 无 | 无 |
| 说明 Künneth 用途 | `unverified` | `omit` | 不出现 | 无 | 无 |
| Kronecker 名称 | `named` | `omit` | 不出现 | 无 | 无 |
| 执行 Kronecker 操作 | `unverified` | `omit` | 不出现 | 无 | 无 |
| total degree 与 \(\mathbb F_2\) 两路径抵消 | `unverified` | `omit` | 不出现 | 无 | 无 |
| qLDPC、LP、距离、logical quotient | `unverified` | `omit` | 不出现 | 无 | 无 |

### Local definition closure

- “共享物理列空间”先用“一列对应一个物理量子比特位置”解释，不使用 tensor-product sector。
- “每行是一条 check”用 0/1 support 解释，不使用 stabilizer group。
- \(H_XH_Z^T\) 的元素按以下闭包解释：共享列坐标 → 两行共同为 1 的位置 → 计数模 2 → 0 表示偶 overlap。
- 偶 overlap 的对易意义在当前用法处即时解释：每个共同位置贡献一次 X/Z 符号反转，偶数次成对抵消；不假设读者预先会该判据。
- “全零矩阵”只在单个元素和单个 row pair 已闭合后，才翻译为所有异型 checks 对易。
- \(C_1\) 在第一次出现时只叫物理量子比特 support 空间。
- \(C_2,C_0\) 不给抽象 degree 定义，只按左右两侧 check roles 解释。
- “链复形”依赖的全部概念——线性映射、三项箭头、相邻复合为零——均在同 phase 更早位置可见。

### Opening and transition contract

- first_sentence_job：承接 U01 结尾，指出必须先把“每一对 checks 都对易”压缩成一个矩阵条件。
- first_paragraph_job：建立共享列和每行 check 的具体含义，不出现 chain 名称。
- allowed_vocabulary：物理量子比特、列、行、0/1 support、共同为 1、模 2、奇偶、偶数 overlap、符号反转、X-type/Z-type check、对易、矩阵乘积、箭头、线性映射、物理 support 空间、链复形（仅 P2 末尾）。
- notation_budget：
  - P1：复用 \(H_X,H_Z\)，新增 \(H_Z^T,H_XH_Z^T=0\)；
  - P2：新增 \(C_2,C_1,C_0\)，不增加其它符号。
- link_budget：0。
- forbidden_terms_topics：wikilink、Künneth、qLDPC、LP、距离、canonical、ownership、前置、不是前置、stabilizer code/group、logical quotient、Kronecker、total degree、\(A,B\) 尺寸、\(A\otimes B+A\otimes B=0\)、homology、cochain、任务或审查语言。
- closing_job：说明三项零复合把自动对易变成构造条件；只指出后续才会说明 \(A,B\) 如何具体生成它，不设计 U03。

### Math and sources

- required_math：
  - \(H_X,H_Z\) 共享物理 columns；
  - rows 是两类 checks；
  - 乘积的一个元素是对应两行共同为 1 的列数模 2；
  - 元素为零表示偶 overlap，偶数次 X/Z 符号反转成对抵消，所以该 row pair 对易；
  - \(H_XH_Z^T=0\) 因而等价于所有异型 row pairs 对易；
  - 任意 matrices 不保证零乘积；
  - \(C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0\) 的复合为 \(H_XH_Z^T\)；
  - 对象和用途出现后才命名 chain complex。
- example：不使用具体数值矩阵；row-pair overlap 的逐元素解释本身承担最小 worked interpretation，避免引入额外数字和尺寸。
- source_anchors：`SOURCE_PACKET.md` 的 S01、S02、S03、S05、S06。
- unsupported_claims：不说明 HGP blocks 怎样实现零复合，不说明任何逻辑、距离、稀疏性或下游性质。

# 拆分与整合决定

- 不拆文件。U01/U02 共同构成目标 reference 的短小 guided onboarding。
- U01 与 U02 分成独立 packets/drafts，以保证 Writer 每次只持有一个 unit。
- U02 内部必须保留 P1、P2 两个 phase，不合并。
- 本 pilot 只生成 staged fragments；不删除旧开头，不写正式文件，不执行 integration。

# Writer packet 编译约束

- 每个 packet 必须自足地携带授权数学摘录和目标旧开头片段；Writer 无需且不得读取 canonical/index、Brief、Domain、Learner 或完整 Design。
- Packet 必须删除 ownership、路线、前置判断、审查状态和所有可复制为维护者开头的句子。
- U01 packet 只能授权四个符号 \(A,B,H_X,H_Z\)。
- U02 packet 必须显式保留 P1/P2 边界；P1 不得看到 \(C_2,C_1,C_0\)，P2 才授权三项箭头。

# 需要用户决定

- 无。设计不改变正式文件结构、学习路线或长期 ownership。
