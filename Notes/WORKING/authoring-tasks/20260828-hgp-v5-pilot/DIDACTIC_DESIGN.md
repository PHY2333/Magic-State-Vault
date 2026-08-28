---
design_revision: 5
based_on_learner_revision: 1
status: designed
---

# 目标表现

1. 区分超图乘积构造、所得 HGP 码、输入 `A,B` 与输出 `H_X,H_Z`。
2. 说明 CSS 输出为什么不能是任意共享列的矩阵 pair，而必须满足异型校验彼此对易。
3. 从逐位置 Pauli 交换规则，以不过量的深度推出偶数重叠与 `H_XH_Z^T=0`。
4. 解释三项箭头中三个坐标空间、两个映射和零复合怎样统一表达同一条件。
5. 保持 HGP 主问题可见，把完整 `2×2` Pauli 逐项计算放入可跳过补充。
6. 结束时把读者送回下一主问题：具体 HGP 构造怎样用 `A,B` 产生两支映射并证明复合恒为零。

# 文件决策

- note_type: `reference`
- entry_mode: `guided`
- action: 只设计 U01、U02 staged fragments
- draft_strategy: `unit-fragments`
- formal target: 只读；Writer 不写正式文件
- split decision: 不新建正式笔记；Pauli 完整计算不升级为独立主线
- integration boundary: 本轮最多生成只读 `INTEGRATION_PREVIEW.md`

# 全局主线与范围

```text
构造方法与所得对象
→ 经典输入与量子输出
→ 输出必须满足的 CSS 对易问题
→ 局部交换规则
→ 偶数重叠
→ H_XH_Z^T=0
→ 三项箭头的零复合
→ 下一步由 A,B 具体构造并证明零复合
```

U01/U02 禁止进入 Kronecker blocks、`A/B` 尺寸、total degree、两路径抵消、homology、Künneth、logical quotient、stabilizer group、syndrome、metacheck、qLDPC 参数或 LP 推广。

# U01 — 构造、所得码与输入／输出

## Entry / exit / why now

- entry_capabilities: LM01 `unverified`；LM03、LM04 `unseen`；LM05 `named`；LM02 `unseen`；LM06、LM19 `unverified`。
- exit_capability: 能用自己的话区分方法、所得对象、两份经典输入和两张量子输出矩阵，并指出输出还需满足异型校验对易。
- why_now: 没有这组角色区分，U02 会把 `A,B`、`H_X,H_Z` 和 CSS 条件混成同一层对象。
- primary_pattern: 类别定位 → 最小数据提醒 → 构造／产物关系 → 输入／输出角色 → 当前合法性问题。

## Phases

### U01-P1 — 稳定第一对象

- cognitive_action: 建立超图乘积构造的类别，紧邻提醒奇偶校验矩阵的一般含义，再命名所得 HGP 码。
- load_profile: `new_entities=2`（构造、所得码）；`new_relations=1`（produces）；`new_notation=HGP`；`holding_set=构造方法`。
- consolidation: 用一句“构造是方法，HGP 码是所得对象”收束。

### U01-P2 — 两层矩阵角色

- cognitive_action: 引入 `A,B` 的经典输入角色和 `H_X,H_Z` 的量子输出角色。
- load_profile: `new_entities=2 notation groups`；`new_relations=2`；`holding_set=输入→构造→输出`。
- consolidation: 明确输出不是输入别名。

### U01-P3 — 当前 CSS 问题

- cognitive_action: 说明共享列；在首次使用“支撑”时把它闭合为一行中非零列对应的位置集合；再说明两类行支撑和“彼此对易”的当前局部要求，只提出一个结尾问题。
- load_profile: `new_entities=2 check types`；`new_relations=2`；`holding_set=H_X,H_Z`。
- consolidation: 唯一末句问“怎样由构造本身保证两类校验彼此对易？”

## Concept action ledger

| capability_id | subject | facet | evidence_state | action | first_allowed_phase | local_treatment |
|---|---|---|---|---|---|---|
| LM01 | 奇偶校验矩阵一般含义 | identity | unverified | remind | U01-P1 | `reminder / mainline`；第二句闭合 |
| LM03 | 超图乘积构造类别 | identity | unseen | introduce | U01-P1 | 方法类别与两份输入 |
| LM04 | 构造与 HGP 码关系 | context_role | unseen | introduce | U01-P1 | 方法／所得对象分开 |
| LM02 | `A,B` 输入角色 | context_role | unseen | introduce | U01-P2 | `introduce / mainline` |
| LM06 | `H_X,H_Z` 共享列与行支撑 | representation | unverified | introduce | U01-P3 | compact local bridge；明确一行中取值为 `1` 的列对应的位置构成支撑 |
| LM05 | CSS 名称 | identity | named | use | U01-P1 | 可先作定位标签，不依赖其含义推理 |
| LM19 | CSS 当前局部含义 | context_role | unverified | introduce | U01-P3 | `compact / mainline` definition treatment |
| LM17 | Künneth 名称 | identity | named | omit | — | 不出现 |

## Definition cards

### DEF01 — 超图乘积构造

- definition_depth: compact
- category: 构造方法
- basic_data: 两张经典二进制奇偶校验矩阵
- current_function: 构造 CSS 量子码
- discriminates_from: 由它得到的 HGP 码
- capability_dependencies: CSS 只需名称识别；奇偶校验矩阵可先作定位标签
- prohibited_shortcuts: 不写“既指构造，也指所得码”；不先讲 blocks、尺寸或 Künneth
- preview_allowed: no
- closure_deadline: `immediate_label`
- first_allowed_phase: U01-P1 第一首句

### DEF02 — HGP 码

- definition_depth: local
- category: 量子码
- basic_data: 由超图乘积构造所得
- current_function: 给所得对象命名
- discriminates_from: 超图乘积构造这一方法
- capability_dependencies: DEF01
- prohibited_shortcuts: 不把 HGP 解释成输入矩阵名称
- preview_allowed: no
- closure_deadline: `before_first_dependency`
- first_allowed_phase: U01-P1

### DEF03 — 经典二进制奇偶校验矩阵（局部提醒）

- definition_depth: reminder
- category: 二进制矩阵
- basic_data: 每一行规定一条模 2 的奇偶校验条件
- current_function: 说明 `A,B` 所属的数据类别
- discriminates_from: HGP 输出的量子校验矩阵角色
- capability_dependencies: 无
- prohibited_shortcuts: 不写“用于记录校验关系的矩阵”；不扩展经典编码理论
- preview_allowed: yes；第一句可先把名称作为输入类别
- closure_deadline: `before_first_dependency`；必须在首次用其性质或引入 `A,B` 角色前，由紧邻第二句闭合
- first_allowed_phase: U01-P1

### DEF04 — CSS 的当前局部含义

- definition_depth: compact
- category: 当前量子校验结构
- basic_data: 同一组物理量子比特上的 X 型校验与 Z 型校验
- current_function: 要求所有异型校验彼此对易
- discriminates_from: 不展开完整 stabilizer/logical 形式化
- capability_dependencies: LM06 的共享列与行支撑需在同段先闭合
- prohibited_shortcuts: 不使用 stabilizer group、logical quotient 或 syndrome
- preview_allowed: CSS 名称可在 P1 出现
- closure_deadline: `before_first_dependency`；在提出“怎样保证对易”前闭合
- first_allowed_phase: U01-P3

## Explanation claim ledger

| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | closure_deadline | source_anchor | first_allowed_phase |
|---|---|---|---|---|---|---|---|---|---|
| U1-C01 | 超图乘积构造从两张经典二进制奇偶校验矩阵构造 CSS 量子码 | category | 建立第一对象 | LM05=`named`，只允许 CSS 作定位标签 | — | define DEF01 | immediate_label | K02 | U01-P1 |
| U1-C02 | 每张奇偶校验矩阵的每一行规定一条模 2 条件 | definition | 恢复输入类别含义 | — | — | remind DEF03 | before_first_dependency | K01/PR01/LD00 | U01-P1 第二句 |
| U1-C03 | 由该构造得到的量子码称为 HGP 码 | role | 区分方法与产物 | — | U1-C01 | define DEF02 | before_first_dependency | K03 | U01-P1 |
| U1-C04 | `A,B` 是两份经典种子输入 | role | 建立输入角色 | — | U1-C01,U1-C02 | introduce | before_first_dependency | K04 | U01-P2 |
| U1-C05 | `H_X,H_Z` 是量子校验输出，不是 `A,B` 的别名 | role/boundary | 建立输出角色 | — | U1-C03,U1-C04 | define/contrast | before_first_dependency | K04 | U01-P2 |
| U1-C06 | 两张输出矩阵共享物理量子比特列，行分别给出两类校验支撑 | representation | 为对易问题提供对象 | — | U1-C05 | 用自然语言逐项定义行、列与支撑；支撑在首次出现时闭合为一行中非零列对应的位置集合 | before_first_dependency | K05/PR02 | U01-P3 |
| U1-C07 | 此处 CSS 要求 X 型与 Z 型校验彼此对易 | definition/motivation | 建立合法性问题 | LM05=`named` | U1-C06 | define DEF04 | before_first_dependency | K05 | U01-P3 |
| U1-C08 | 怎样由构造本身保证两类校验对易 | motivation | 形成 U02 主问题 | — | U1-C07 | demonstrate need | immediate_label | K05→K15 | U01 唯一末句 |

## Depth and placement ledger

| item_id | capability_or_claim | centrality | explanation_depth | placement | closure_deadline | mainline_cost | canonical_detail | duplication_rationale |
|---|---|---|---|---|---|---|---|---|
| U1-DP01 | 奇偶校验矩阵一般含义 | bridge | reminder | mainline | before_first_dependency | 1 short sentence | DOMAIN:D01 | 无独立长 owner；局部提醒不可缺 |
| U1-DP02 | `A,B` 输入角色；concept action=`introduce` | core | compact_derivation | mainline | before_first_dependency | 1 sentence | K04 | 用输入→构造的数据流简洁闭合新角色，不假设读者已知 |
| U1-DP03 | CSS 当前含义；definition depth=`compact` | core | compact_derivation | mainline | before_first_dependency | 1 short paragraph 内 | DOMAIN:D02 | 用共享列→两类支撑→对易要求闭合当前作用，不复制 logical detail |
| U1-DP04 | HGP blocks、尺寸、Künneth | optional | delay | delay | — | 0 | DOMAIN:D09–D11 | 后续 owner 已承担；本 unit 没有 dependent use |

## Mainline contract

- main_question: 什么是超图乘积构造、它产生什么对象、为什么输出还面临对易要求？
- mainline_result: 构造／HGP 码／`A,B`／`H_X,H_Z` 四层角色清楚，并得到唯一结尾问题。
- supporting_details: 仅奇偶校验矩阵一句提醒、共享列与行支撑的 compact bridge。
- return_to_mainline: 每段末分别回到“方法／所得对象”“输入／输出”“怎样保证对易”。
- latency_budget:
  - max_supporting_paragraphs: 3 个短段落（即整个 U01）
  - max_new_notation_groups: 2（`A,B`；`H_X,H_Z`）
- optional_skip_test: U01 不设置 optional block。
- proportionality_rationale: 任一上游定义不得长于当前构造—码和输入—输出两组核心关系。

## Opening contract

- 第一首句只建立“超图乘积构造是一种从两张经典二进制奇偶校验矩阵构造 CSS 量子码的方法”。
- 紧邻第二句提醒“这类矩阵的每一行规定一条模 2 的奇偶校验条件”；不要求塞回第一句。
- 不出现“既指……也指……”、Künneth、ownership、前置清单、维护边界或 wikilink。

## Language contract

- register: 自然、连续的简体中文教材语体。
- required Chinese: 奇偶校验矩阵、X 型校验、Z 型校验、物理量子比特、行、列、支撑、对易。
- allowed exceptions: HGP、CSS、`A,B,H_X,H_Z`。
- forbidden: `X-type checks`、`row pair`、`support space`、packet/audit/canonical owner 等维护语言。
- link budget: 0。

## Math and sources

- K01–K05、PR01–PR02。
- 不使用 Pauli 计算、chain complex 或具体 blocks。

## Reader card design

- reading situation: 第一次进入 HGP 开头。
- assumed: 只识别 CSS 名称；其它当前需要的行、列和支撑含义均由正文局部建立。
- explicitly not assumed: HGP 类别、`A/B` 角色、`H_X/H_Z` 角色、CSS 当前对易要求。
- expected exit: 能区分四层对象，并说出下一问题。
- 不给出标准答案、phase、claim、depth、来源或审查状态。

# U02 — 对易条件与零复合

## Entry / exit / why now

- entry_capabilities: U01 exit；LM06–LM16、LM18、LM20 均不直接假设。
- exit_capability: 从逐位置局部规则推出偶数重叠和 `H_XH_Z^T=0`，再解释三项箭头的三个坐标空间、两个映射和零复合用途；同时知道具体 HGP blocks 尚待下一单元。
- why_now: 先建立“输出必须满足什么”及其机制，下一单元才能说明 HGP 构造“怎样保证”。
- primary_pattern: 问题 → 局部规则 → 总符号 → 矩阵汇总 → 反例边界 → 整体箭头 → 零复合 → 返回 HGP。

## Phases

### U02-P1 — 从局部 Pauli 规则到矩阵条件

- main cognitive action: 把所有异型校验对易化成可检验的 `H_XH_Z^T=0`。
- ordered steps:
  1. 共享列与行支撑；行到 `X/Z/I` 的逐位置作用。
  2. 用计算基作用给出同比特 `XZ=-ZX` 的短推导；登记张量积乘法规则，再推出异比特作用对易。
  3. 可跳过的显式 `2×2` 矩阵逐项计算。
  4. 每个共同位置贡献一个负号，总符号 `(-1)^w`。
  5. 偶数重叠给出对易。
  6. 一个矩阵元记录对应两行的重叠奇偶；零矩阵汇总全部行对。
  7. `[1]` 反例说明共享列并不自动保证条件。
- load_profile: `new_entities=x,z,w`；`new_relations=局部交换→总符号→重叠奇偶→矩阵条件`；`reader-visible notation groups=5`（`x,z,X(x),Z(z)`；列坐标 `q`；计算基 `|0>,|1>`；共同位置数 `w`；行索引 `i,j` 与矩阵元）；`holding_set=如何把全部异型对易写成可检验条件`。
- consolidation: optional block 后立即回到“每个共同位置贡献一个负号”；P1 末用最小反例重申真正条件。
- prohibited: `C_2,C_1,C_0`、“链复形”、具体 HGP blocks、尺寸、两路径抵消。

### U02-P2 — 三项箭头整体

- main cognitive action: 把同一个零矩阵条件读成“选择 Z 校验 → 物理支撑 → X 重叠奇偶”的零复合。
- ordered steps:
  1. 整体写出三项箭头，并立即给三个空间的坐标含义。
  2. 不引入维数符号或额外向量变量，用自然语言解释 `H_Z^T` 的输入、输出与模 2 叠加。
  3. 不引入额外向量变量，用自然语言解释 `H_X` 输出各分量的重叠奇偶。
  4. 连续复合为 `H_XH_Z^T`；其为零统一表达全部对易。
  5. 对象和用途闭合后才命名链复形；回到下一步 HGP 构造问题。
- load_profile: `new_entities=C_2,C_1,C_0`（一个坐标组三元组）；`new_relations=2 maps+1 composite`；`reader-visible notation groups=2`（三空间；`H_Z^T,H_X,H_XH_Z^T`）；明确不出现 `s,v,r_Z,r_X,n`；`holding_set=零复合怎样表达同一条件`。
- consolidation: 每个空间出现时立即解释坐标；最后回到 `A,B` 如何构造两支映射。

## Concept action ledger

| capability_id | subject | facet | evidence_state | action | first_allowed_phase | local_treatment |
|---|---|---|---|---|---|---|
| LM06 | 共享列与行支撑 | representation | unverified | remind | U02-P1 | 第一段自足重申 |
| LM18 | 行支撑到 `X/Z/I` | representation | unverified | introduce | U02-P1 | compact derivation/mainline |
| LM07 | 同比特反对易 | rationale | unverified | introduce | U02-P1 | compact derivation/mainline |
| LM08 | 异比特对易 | rationale | unverified | introduce | U02-P1 | compact derivation/mainline |
| LM20 | 完整 `2×2` 逐项相乘 | procedure | unverified | introduce | U02-P1 | 只在 optional derivation 中提供；非出口能力 |
| LM09 | 总交换符号 | rationale | unverified | introduce | U02-P1 | compact derivation/mainline |
| LM10 | 偶数重叠 | rationale | unverified | introduce | U02-P1 | compact derivation/mainline |
| LM11 | 矩阵元重叠奇偶 | representation | unverified | introduce | U02-P1 | compact derivation/mainline |
| LM12 | 零乘积的 CSS 作用 | context_role | unverified | introduce | U02-P1 | compact derivation/mainline |
| LM14 | 三空间坐标 | representation | unverified | introduce | U02-P2 | compact derivation/mainline |
| LM15 | 两映射作用 | representation | unverified | introduce | U02-P2 | compact derivation/mainline |
| LM16 | 零复合作用 | context_role | unverified | introduce | U02-P2 | compact derivation/mainline |
| LM13 | 链复形名称 | identity | named | remind | U02-P2 末 | 对象与用途闭合后命名 |
| LM17 | Künneth | identity | named | omit | — | 不出现 |

## Definition cards

### DEF05 — 从二进制行到整条校验

- definition_depth: compact operational
- category: 二进制行到多量子比特 Pauli 算符的操作性表示
- basic_data: 行中 `1` 的列对应的位置构成支撑；该行属于 `H_X` 或 `H_Z` 决定支撑上作用 `X` 或 `Z`，`0` 的位置作用 `I`
- current_function: 把矩阵行连接到逐位置交换规则
- discriminates_from: 支撑只记录非零位置，不等于携带 `X/Z` 类型的完整校验算符；类型由该行所属矩阵提供
- capability_dependencies: LM06
- prohibited_shortcuts: 不引入一般 Pauli 群或辛表示
- preview_allowed: no
- closure_deadline: `before_first_dependency`；在任何交换推理之前
- first_allowed_phase: U02-P1 第 1 段

### DEF06 — 链复形的当前局部含义

- definition_depth: compact
- category: 向量空间与线性映射组成的序列
- basic_data: 三个空间、两个映射；连续两步复合为零
- current_function: 用零复合统一表达全部异型校验对易
- discriminates_from: 任意画出的三项箭头；不展开 cycle/homology
- capability_dependencies: U2-C10–U2-C14 全部闭合
- prohibited_shortcuts: 不在 P1 出现名称；不以名称代替三个空间和两个映射的解释
- preview_allowed: yes；P2 可先展示箭头，但在命名和推理前逐项闭合
- closure_deadline: `preview_then_close`
- first_allowed_phase: U02-P2 末

## Explanation claim ledger

| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | closure_deadline | source_anchor | first_allowed_phase |
|---|---|---|---|---|---|---|---|---|---|
| U2-C01 | 两矩阵共享物理列，各行给出一条相应类型校验支撑 | representation | 固定成对对象 | U01 exit | U1-C06 | remind | immediate_label | K05/PR02 | P1.1 |
| U2-C02 | 二进制行逐位置指定 `X/Z/I`，可写成 `X(x),Z(z)` | definition/representation | 从支撑到算符 | — | U2-C01 | define DEF05；明确支撑／类型边界，同时逐项解释 `0,1` 与 `\bigotimes_q` 表示把逐位置作用组合成整条校验 | before_first_dependency | K06/PR03/LD03 | P1.1 |
| U2-C03 | `X` 交换计算基状态，`Z` 区分其符号；逐个基态比较得到 `XZ=-ZX` | mechanism | 真正闭合共同位置的局部负号 | — | U2-C02 | demonstrate on `|0>,|1>` | before_first_dependency | K07/PR04/LD01 | P1.2 |
| U2-C04a | 当前特例中，分处两个张量因子的作用按对应因子相乘 | supporting premise | 给异比特交换提供规则 | — | U2-C02 | 只给 `X,I,Z` 特例等式，不引入通用 `M,N,P,Q` | before_first_dependency | LD02 | P1.3 |
| U2-C04 | 不同量子比特上的作用彼此对易 | mechanism | 排除异位置额外符号 | — | U2-C02,U2-C04a | demonstrate tensor factors | before_first_dependency | K08/PR05/LD02 | P1.3 |
| U2-C05 | 共同位置数为 `w` 时总符号是 `(-1)^w` | mechanism | 从局部到整条校验 | — | U2-C02,U2-C03,U2-C04a,U2-C04 | derive | before_first_dependency | K09/PR06/LD04 | P1.4 |
| U2-C06 | `w` 为偶数当且仅当该异型校验对易 | equivalence | 建立偶数重叠判据 | — | U2-C05 | 就地说明偶数个负号成对抵消 | before_first_dependency | K10 | P1.4 |
| U2-C07 | `(H_XH_Z^T)_{ij}` 记录对应两行重叠奇偶 | representation | 把逐对条件矩阵化 | — | U2-C01,U2-C06 | 展开一个矩阵元，并逐项解释共同非零列与模 2 奇偶 | before_first_dependency | K11/PR07/LD05 | P1.5 |
| U2-C08 | `H_XH_Z^T=0` 等价于所有异型校验彼此对易 | equivalence | 汇总全部行对 | — | U2-C06,U2-C07 | derive/quantify | before_first_dependency | K11/PR08 | P1.5 |
| U2-C09 | 共享列不自动保证零乘积；`[1]` 是最小反例 | boundary/demonstration | 阻止任意 pair 误读 | — | U2-C08 | demonstrate briefly | immediate_label | K12/LD06 | P1.5，与零矩阵结果同段收束 |
| U2-C10 | `C_2,C_1,C_0` 分别以 Z 校验、物理量子比特、X 校验为坐标 | definition/representation | 建立箭头对象 | — | U2-C08 | define immediately | immediate_label | K13/LD07 | P2.1 |
| U2-C11 | `H_Z^T` 把 Z 校验选择映成物理支撑 | mechanism | 解释第一箭头 | — | U2-C10 | explain row combination in words | before_first_dependency | K13/PR09/LD07 | P2.2 |
| U2-C12 | `H_X` 把物理支撑映成与各 X 校验的重叠奇偶向量 | mechanism | 解释第二箭头 | — | U2-C07,U2-C10 | explain components in words | before_first_dependency | K13/PR09/LD07 | P2.3 |
| U2-C13 | 连续复合就是 `H_XH_Z^T` | equivalence | 连接矩阵条件与箭头 | — | U2-C11,U2-C12 | compose | before_first_dependency | K13 | P2.4 |
| U2-C14 | 连续复合为零统一表达全部异型校验对易 | role/equivalence | 建立整体价值 | — | U2-C08,U2-C13 | restate equivalence | before_first_dependency | K14/PR10 | P2.4 |
| U2-C15 | 满足零复合的这类映射序列是当前所需链复形 | category | 最后命名 | LM13=`named` | U2-C10–C14 | define DEF06 | preview_then_close | K14 | P2.5 |
| U2-C16 | 下一步应由 `A,B` 构造两支映射并证明复合恒为零 | motivation/boundary | 返回 HGP 主线 | U01 exit | U2-C14,U2-C15 | delay concrete proof | immediate_label | K15/DOMAIN:D09 | P2 唯一结尾 |

## Depth and placement ledger

| item_id | capability_or_claim | centrality | explanation_depth | placement | closure_deadline | mainline_cost | canonical_detail | duplication_rationale |
|---|---|---|---|---|---|---|---|---|
| U2-DP01 | 行支撑到 `X/Z/I` 逐位置作用 | bridge | compact_derivation | mainline | before_first_dependency | P1 第 1 段；1 tensor notation group | DOMAIN:D02 | 后续交换推理不可缺；不复制辛形式 |
| U2-DP02 | 同比特 `XZ=-ZX` 的计算基短推导 | core | compact_derivation | mainline | before_first_dependency | P1 第 2 段；计算基 1 notation group | DOMAIN:D04 | LM07 是 rationale/unverified，故主线给真实短推导而非裸陈述 |
| U2-DP03 | 当前 `X/I/Z` 特例中的张量因子乘法 | supporting | compact_derivation | mainline | before_first_dependency | P1 第 3 段；1 equality | DOMAIN:D06 | 异比特对易的显式 premise，必须先闭合；不引入通用矩阵字母 |
| U2-DP04 | 异比特作用对易 | core | compact_derivation | mainline | before_first_dependency | P1 第 3 段；1 tensor equality | DOMAIN:D06 | 无直接 owner，由当前 `X/I/Z` 特例的 local derivation 闭合 |
| U2-DP05 | 显式 `2×2` 矩阵逐项相乘 | optional | optional_derivation | optional_block | before_first_dependency | 0 mainline paragraphs；1 collapsible block | DOMAIN:D05 | 不是出口能力；后文不依赖 block 独有步骤 |
| U2-DP06 | 总符号 `(-1)^w` 与偶数重叠 | core | compact_derivation | mainline | before_first_dependency | P1 第 4 段 | DOMAIN:D04–D06 | 当前出口机制，必须展开局部负号如何相乘 |
| U2-DP07 | 矩阵元是重叠奇偶 | core | compact_derivation | mainline | before_first_dependency | P1 第 5 段；1 displayed equation | DOMAIN:D02 | 本地解释矩阵元，避免承重链接 |
| U2-DP08 | `[1]` 反例；local treatment=`demonstrate` | supporting | compact_derivation | mainline | immediate_label | P1 第 5 段；1 short equation | DOMAIN:D02 | 极短新反例堵住“共享列自动对易” |
| U2-DP09 | 三空间、两映射与连续复合 | core | compact_derivation | mainline | before_first_dependency | P2 第 1–4 段 | DOMAIN:D02,D08 | 当前出口能力；只保留坐标和用途 |
| U2-DP10 | 链复形当前局部定义 | bridge | compact_derivation | mainline | preview_then_close | P2 第 5 段；1 sentence | DOMAIN:D08 | 对象和用途先闭合，再给当前名称；无需承重链接 |
| U2-DP11 | generic degree/cycle/homology | optional | delay | delay | — | 0 | DOMAIN:D08 | 完整理论留给 owner，本 unit 没有 dependent use |
| U2-DP12 | HGP blocks 与两路径抵消 | optional | delay | delay | — | 0 | DOMAIN:D09 | 结尾只建立需求，不代替下一单元构造性证明 |

## Mainline contract — U02-P1

- main_question: 如何把全部 X 型与 Z 型校验彼此对易写成一个可检验条件？
- mainline_result: `H_XH_Z^T=0` 精确汇总所有行对的偶数重叠；共享列本身不够。
- supporting_details: 行到逐位置作用、两条局部交换规则、总符号、矩阵元、最小反例。
- return_to_mainline: optional block 后第一句必须回到“每个共同位置贡献一个负号”；P1 末明确真正条件是偶数重叠／零乘积。
- latency_budget:
  - max_supporting_paragraphs: 从提出问题到首次得到 `H_XH_Z^T=0` 最多 5 个 mainline 段落
  - paragraph_allocation: P1.1 行与逐位置作用；P1.2 计算基短推导；P1.3 当前 `X/I/Z` 张量因子特例、异比特对易及 optional block；P1.4 从 callout 后显式回返到总符号与偶数重叠；P1.5 矩阵元、零乘积与极短最小反例
  - max_new_notation_groups: 5（`x,z,X(x),Z(z)`；列坐标 `q`；`|0>,|1>`；`w`；`i,j` 与矩阵元）
- optional_skip_test: 完全跳过 `2×2` callout 后，主线仍以计算基作用真实推出 `XZ=-ZX`，以张量积乘法规则推出异比特对易，再逐位置累计为 `(-1)^w`；后文不得引用 callout 独有计算步骤。
- proportionality_rationale: 主线每项 detail 都直接服务零矩阵条件；完整矩阵乘法不属于出口，必须折叠。

## Mainline contract — U02-P2

- main_question: 怎样把零矩阵条件读成一幅有对象含义的三项箭头，而不是事后碰巧核验？
- mainline_result: `C_2→C_1→C_0` 表示 Z 校验选择到物理支撑再到 X 重叠奇偶，零复合统一表达全部对易。
- supporting_details: 三个坐标空间、两个映射的分量作用、连续复合。
- return_to_mainline: 每个空间出现时立即说明坐标；最后回到 `A,B` 怎样构造两支映射并证明复合恒为零。
- latency_budget:
  - max_supporting_paragraphs: 5 个 mainline 段落
  - paragraph_allocation: P2.1 整体箭头及三个坐标空间；P2.2 第一映射；P2.3 第二映射；P2.4 连续复合及 CSS 回接；P2.5 命名链复形并建立下一步期待
  - max_new_notation_groups: 2（三空间一组；两映射与复合一组）；禁止 `s,v,r_Z,r_X,n`
- optional_skip_test: P2 无 optional block；generic chain detail 全部 delay。
- proportionality_rationale: 不引入 degree/cycle/homology，三项箭头始终服务 CSS 对易和下一步 HGP 构造。

## Optional block contract

- title: `补充推导：直接核对 XZ=-ZX`，使用可折叠 callout。
- content: 标准 `X,Z` 矩阵与 `XZ,ZX` 的逐项结果；不扩展 `Y` 或一般 Pauli algebra。
- independence: 主线用 `X,Z` 对 `|0>,|1>` 的作用给出短推导，并用张量积乘法规则闭合异比特对易；callout 只提供矩阵核验，不提供后文独有 premise。
- return sentence: callout 后立即写“回到整条校验，每个共同位置都会贡献这样一个负号”。

## Opening and transition contract

- U02-P1 首句承接 U01 的问题，并说当前先把输出必须满足的对易要求化成可检验条件；不得声称已证明具体 HGP 输出满足它。
- P1 标题固定为 `### 从局部交换到矩阵条件`；只谈局部交换到矩阵条件，不出现链复形。
- P2 标题固定为 `### 三个空间与两支映射`。
- repository heading rationale: 目标 HGP 当前所有正式 section 均为同级 `###`；两处 U02 标题使用相同级别，避免其第二节错误统摄后续参数、qLDPC、LP 与来源。只改变标题标记，不改变 phase、标题文字、正文、depth 或 reader exit。
- P2 在对象／映射用途闭合后才命名链复形。
- 唯一结尾期待：由 `A,B` 构造两支映射并证明复合恒为零；不得写成“代入后碰巧核验”。

## Language contract

- register: 自然、统一的简体中文教材语体。
- required Chinese: 奇偶校验矩阵、X 型校验、Z 型校验、行、列、支撑、重叠、重叠奇偶、对易、反对易、物理量子比特、向量空间、映射、链复形。
- allowed exceptions: HGP、CSS、`I,X,Z,A,B,H_X,H_Z,C_2,C_1,C_0` 及数学符号。
- forbidden English shortcuts: `X-type checks`、`row pair`、`support space`、`mainline`、`optional` 等不得进入 reader-visible text。
- links: staged U02 默认 0；local bridge 自足。Integration Preview 可在不承重时规划最多 1 个 CSS owner 链接；不得链接 Twirling 作为 Pauli 代数 owner。

## Math and sources

- K05–K15、PR02–PR11；LD01–LD07。
- Contract Auditor 可用上游 CSS、Chain、Pauli 等式和 HGP 后续 blocks 交叉核对。
- Writer packet 只嵌入当前所需来源摘录／local derivation；不提供 canonical、index 或完整 Domain。

## Reader card design

- reading situation: 已读 U01，想知道为什么两类输出校验必须满足一个额外条件，以及三项箭头有何作用。
- assumed: 仅采用 U01 已建立的出口能力：能区分构造、所得码、`A,B` 输入、`H_X,H_Z` 输出，并知道输出还需满足异型校验对易。
- explicitly not assumed: 行到 `X/Z/I`、Pauli 交换理由、重叠奇偶、零矩阵、三空间和零复合。
- expected exit: 能独立解释量子输出的对易要求如何被写成矩阵条件，并说明三项箭头在当前问题中的用途；能指出下一步尚待解决的问题。
- 不泄露中间公式链、反例答案、phase、depth、来源或审查状态。

# Link 与 duplication 决定

- U01 链接预算 0；U02 staged draft 链接预算 0。
- `CSS码中的cochain complex.md` 承担完整 CSS/logical/syndrome detail；U01/U02 只保留自足 local bridge。
- `Chain complex 与 cochain complex.md` 承担 generic degree/cycle/homology；本处只给三项箭头与零复合的当前含义。
- 完整 Pauli `2×2` 计算无独立 canonical owner，但不是出口能力；放 optional block，而不复制成主线。
- 正式 HGP 第 102–165 行承担 `A,B` blocks 与两路径抵消；本次只在结尾产生需求，不重复证明。
- 正式 HGP 第 1 行与 U01 竞争、第 39–51 行与 U02-P2 重复；具体 replacement 与保留范围交给 manuscript pass 后的 Integration Preview，Integrator 不得静默改 staged text。

# Packet / Reader Card 编译合同

- `PACKETS/U01.md`、`PACKETS/U02.md` 必须带入当前 unit 的 capability actions、definitions/claims、closure deadlines、depth/placement、mainline budget、来源摘录和语言合同。
- Writer 不读取 Brief、Domain、Learner、完整 Design、canonical、index 或 audits。
- `READER_CARDS/U01.md`、`U02.md` 只含 reading situation、assumed、not assumed、expected exit 和 language register；不得给标准答案。
- Writer packet 不要求 canonical/index；授权 source excerpt 与 local derivation必须足够自足。

# 拆分与整合决定

- 不拆分新正式 note。
- Staged U01/U02 是拟议替换片段，不在本轮整合。
- Integration Preview 必须核对旧 opening、三项 convention、logical quotient 段、product spaces 和后续构造性对易证明的 assembled flow。

# 需要用户决定

无。若 Design Audit 发现可解决 major，内部返回本文件修订；若仓库适配需要 reader-visible 改稿，则在 Integration Preview 标记 `changes_required` 并返回 design/writer。
