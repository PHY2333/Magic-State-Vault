---
design_revision: 4
based_on_learner_revision: 2
---

# 目标表现

完成 U01、U02 后，读者能够：

1. 用自己的话区分超图乘积构造与由它得到的 HGP 码。
2. 指出 `A,B` 是两张经典奇偶校验矩阵构成的种子输入，`H_X,H_Z` 是量子码的输出校验矩阵。
3. 说明 `H_X,H_Z` 不能只是任意两张共享列的矩阵，而必须满足 CSS 对易条件。
4. 从同一量子比特与不同量子比特上的泡利交换规则，推出偶数重叠对应一对异型校验对易。
5. 把 `(H_XH_Z^T)_{ij}` 读成一对行支撑的重叠奇偶，并把 `H_XH_Z^T=0` 读成所有异型校验对易。
6. 用三项箭头解释三个空间、两个映射和连续复合，并说明“连续两步为零”怎样统一表达上述 CSS 条件。

# 文件决策

| file | note_type | entry_mode | draft_strategy | action | reason |
|---|---|---|---|---|---|
| `Notes/07-Lifted-Product Code/Hypergraph product code.md` | `reference` | `guided` | `unit-fragments` | 只 staged 重写开头 U01、U02；本任务不 integration | 文件长期保存 HGP 构造，但开头需承担第一次进入该对象的责任；两个 unit 足以完成局部 onboarding，不拆文件 |

- 正式文件 frontmatter 本任务不改；上述两个维度只约束 staged fragments。
- U01 与 U02 是连续开头：U02 可以使用 U01 已闭合的对象关系，但不能假设旧正式正文的其余内容。
- Künneth、Kronecker blocks、`A/B` 尺寸、total degree、两路径抵消、homology、stabilizer group、logical quotient 全部不在这两个 unit 中出现。

# Units

## U01 — 从构造到需要解决的对易问题

- entry_capabilities:
  - `LM01`：经典二进制奇偶校验矩阵／`identity`／`unverified`，只允许局部提醒。
  - `LM03`：HGP 构造类别／`identity`／`unseen`。
  - `LM04`：构造与所得码关系／`context_role`／`unseen`。
  - `LM05`：CSS 名称／`identity`／`named`，名称证据不承担含义。
  - `LM06`：`H_X,H_Z` 共享列与行支撑／`representation`／`unverified`。
  - `LM19`：CSS 的当前局部含义／`context_role`／`unverified`。
- exit_capability: 读者能稳定区分方法、所得码、两份经典输入与两张量子输出，并能指出输出两类校验必须在同一组物理量子比特上彼此对易；自然提出“怎样由构造本身保证对易”。
- why_now: 旧开头把这些对象和维护边界压成一句；后续任何矩阵构造都必须先有稳定的数据流和明确的合法性问题。
- primary_pattern: 类别定位 → 基本数据 → 构造关系。
- supporting_pattern: 问题 → 障碍；只提出对易问题，不提前给出解决工具。

### Phases

#### P1 — 建立稳定第一对象和构造／所得码关系

- cognitive_job: 第一完整句始终以“超图乘积构造”为稳定主语，并在同句用一个短分句闭合奇偶校验矩阵的行级含义；紧接的第二句建立“由它得到的 HGP 码”，让方法和产物各有稳定指称。
- new_entities: 超图乘积构造；HGP 码。
- new_relations: 奇偶校验矩阵每行规定模 2 条件；构造的类别；所得码由该构造产生并据此命名。
- new_notation: `HGP`、`CSS` 两个公认缩写；不出现其它符号。
- holding_set: 两个相邻但不同类别的对象。
- consolidation: 第一完整句可采用“超图乘积构造从两张经典二进制奇偶校验矩阵出发；这类矩阵的每一行规定一条模 2 的奇偶校验条件，而这个构造的目标是得到 CSS 量子码”这一句内顺序，使 D03 在 D01 完成前闭合；第二句回指“这种构造”并落到 HGP 码。随后只用短对照确认方法与所得对象，不采用“既指……也指……”句式。

#### P2 — 区分经典种子输入与量子校验输出

- cognitive_job: 使用 P1 已闭合的奇偶校验矩阵行级含义，完整引入 `A,B` 的种子输入角色，并把 `H_X,H_Z` 定位为构造输出。
- new_entities: 作为一对输入的 `A,B`；作为一对输出的 `H_X,H_Z`。
- new_relations: 输入 pair 经构造得到输出 pair；输入与输出不可混同。
- new_notation: `A`、`B`、`H_X`、`H_Z`，按成对对象引入，不在此处引入尺寸或块公式。
- holding_set: “方法—输入—输出—所得码”四个数据流位置，其中输入和输出各作为一个协调 pair 处理。
- consolidation: 用自然中文复述一次：`A,B` 是送入构造的经典矩阵，`H_X,H_Z` 才描述所得量子码；不使用流程图或维护术语。

#### P3 — 给出 CSS 的当前局部要求并产生结尾问题

- cognitive_job: 只用同一组物理量子比特、X 型校验、Z 型校验和彼此对易，说明输出为何有合法性约束。
- new_entities: X 型校验；Z 型校验。
- new_relations: `H_X,H_Z` 的列指向同一组物理量子比特；两类行给出相应校验支撑；两类校验必须彼此对易。
- new_notation: 复用 `H_X,H_Z`，不新增抽象空间或链复形符号。
- holding_set: 输出 pair 及其一项必要条件。
- consolidation: 不在 U01 预先断言任意矩阵 pair 会失败；只由“输出必须对易”自然留下问题“怎样由构造本身保证两类校验彼此对易？”

### Concept action ledger

| capability_id | subject | facet | evidence_state | action | first_allowed_phase | local_treatment |
|---|---|---|---|---|---|---|
| LM03 | 超图乘积构造类别 | `identity` | `unseen` | `introduce` | U01-P1 | 给方法类别与两份经典二进制矩阵这一最小来源数据 |
| LM04 | 构造与所得 HGP 码的关系 | `context_role` | `unseen` | `introduce` | U01-P1 | 用第二句建立 produced-by/name 关系，不能和构造身份合成一句多义定义 |
| LM01 | 经典奇偶校验矩阵的一般含义 | `identity` | `unverified` | `remind` | U01-P1 首句内 | 在构造类别句的中间分句立即提醒“每一行规定一条模 2 的奇偶校验条件”，不留到后文补猜 |
| LM02 | `A,B` 在 HGP 中是两份输入 | `context_role` | `unseen` | `introduce` | U01-P2 | 明说种子输入，并与 `H_X,H_Z` 输出区分 |
| LM06 | `H_X,H_Z` 的共享列与行支撑 | `representation` | `unverified` | `introduce` | U01-P2（输出角色）；U01-P3（行列读取） | 先命名输出，后说明共享列与两类行支撑 |
| LM05 | CSS 名称 | `identity` | `named` | `use` | U01-P1 | 只把 CSS 当读者已见过的类别标签；首句的可理解类别落在“量子码”，不由该标签承担解释 |
| LM19 | CSS 的当前局部含义 | `context_role` | `unverified` | `introduce` | U01-P3 | 只给当前所需的同组物理量子比特、两类校验和彼此对易，不扩展专名体系 |
| LM07–LM12 | Pauli 机制到矩阵条件 | `rationale/representation/context_role` | `unverified` | `delay` | U02-P1 | U01 不宣称机制，只产生问题 |
| LM13–LM16 | 链复形名称、表示与角色 | `identity/representation/context_role` | `named/unverified` | `delay` | U02-P2 | 对象和用途闭合前不出现名称 |
| LM17 | Künneth 名称 | `identity` | `named` | `omit` | 不适用 | U01/U02 完全不出现 |

### Definition cards

#### D01 — 超图乘积构造

- definition_depth: 当前开头所需的局部类别定义。
- category: 一种构造 CSS 量子码的方法。
- basic_data: 两张经典二进制奇偶校验矩阵。
- current_function: 把两份经典种子数据变成一对满足量子码要求的校验矩阵。
- discriminates_from: 由该方法得到的 HGP 码；构造方法与所得对象分别落点。
- capability_dependencies: LM01 必须由同一完整首句中更早出现的 D03 分句立即闭合；LM05 仅按 `named` 识别 CSS 标签，类别的可理解核心是“量子码”；不假设 HGP 角色知识。
- prohibited_shortcuts: 不用“用于构造 HGP 的 HGP 构造”循环定义；不用 Künneth、chain、tensor product 或 wikilink 替代类别说明。
- first_allowed_phase: U01-P1。

#### D02 — HGP 码

- definition_depth: 名称与来源关系。
- category: CSS 量子码。
- basic_data: 它由超图乘积构造从两张经典种子矩阵得到；不在此处展开内部 blocks。
- current_function: 命名构造所得对象，并与构造方法分开。
- discriminates_from: 超图乘积构造本身；种子输入 `A,B`；输出校验矩阵 `H_X,H_Z`。
- capability_dependencies: 已闭合 D01/U1-C01。
- prohibited_shortcuts: 第一或第二句不得写成“Hypergraph product 既指构造，也指码族”；不得用英文词典式括注承担关系。
- first_allowed_phase: U01-P1，在 D01 之后的连续第二句。

#### D03 — 经典二进制奇偶校验矩阵（局部提醒）

- definition_depth: remind；只恢复当前读取所需深度。
- category: 二进制矩阵。
- basic_data: 行、列以及 `0/1` 元素；无需定义经典码空间。
- current_function: 每一行规定一条模 2 的奇偶校验条件；`A,B` 在本构造中充当两份种子输入。
- discriminates_from: 输出的量子校验矩阵 `H_X,H_Z`；一般含义与本构造角色分别陈述。
- capability_dependencies: 基本的行列与模 2 词义；没有掌握证据时由本句直接提醒。
- prohibited_shortcuts: 禁写“用于记录校验关系的矩阵”；禁把一般含义和 `A,B` 的 HGP 角色压成同一状态或同义定义。
- first_allowed_phase: U01-P1 首句内，在完成 D01 的类别断言之前以短分句闭合。

#### D04 — CSS 的当前局部含义

- definition_depth: 只到本次对易问题所需的局部含义。
- category: 当前讨论的一类量子码描述。
- basic_data: 同一组物理量子比特上的 X 型校验和 Z 型校验，由共享列的 `H_X,H_Z` 行支撑表示。
- current_function: 要求两类校验彼此对易，从而给 HGP 输出提出必要约束。
- discriminates_from: 只给出两张共享列矩阵而没有提出对易要求的描述；此区别在 U01 只用于设计边界，读者可见的“任意 pair 不保证”延到 U02-P1.7 示范。
- capability_dependencies: LM06 在同 phase 闭合共享列、行与支撑的读取；LM19 由本卡引入当前用途。
- prohibited_shortcuts: 不出现 stabilizer group、logical quotient、syndrome、metacheck；不把“CSS”只换成另一串未解释专名。
- first_allowed_phase: U01-P3。

### Explanation claim ledger

| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | source_anchor | first_allowed_phase |
|---|---|---|---|---|---|---|---|---|
| U1-C03 | 经典奇偶校验矩阵的每一行规定一条模 2 的奇偶校验条件 | `definition` | 立即闭合首句来源数据的含义 | LM01 | 无 | `remind`（D03） | K01 | U01-P1 首句中间分句，早于 U1-C01 的完整谓语闭合 |
| U1-C01 | 超图乘积构造从两张经典二进制奇偶校验矩阵出发并得到 CSS 量子码 | `category` | 建立第一稳定对象 | LM03；LM01 由同句 U1-C03 提醒；LM05 仅按 `named` 使用标签 | U1-C03（在同一完整句的中间分句先闭合） | `define`（D01）+ `remind`（D03） | S01；K02 | U01-P1 首句 |
| U1-C02 | 由这种构造得到的量子码称为 HGP 码 | `role` | 区分方法与所得对象 | LM04 | U1-C01 | `define`（D02） | S01；K03 | U01-P1，紧随 U1-C01 |
| U1-C04 | `A,B` 在 HGP 中是两份种子输入 | `role` | 完整引入新角色 | LM02 | U1-C01, U1-C03 | `define` | S01；K04 | U01-P2 |
| U1-C05 | `H_X,H_Z` 是构造为所得量子码给出的输出校验矩阵，不是 `A,B` 的别名 | `role` | 闭合输入／输出区分 | LM06 | U1-C01, U1-C02, U1-C04 | `define` | S01；K04 | U01-P2 |
| U1-C06 | `H_X,H_Z` 的列对应同一组物理量子比特，行分别给出 X 型与 Z 型校验的支撑 | `role` | 让输出矩阵有可读取落点 | LM06 | U1-C05 | `define` | S02:5–21；K05 | U01-P3 |
| U1-C07 | CSS 在这里要求这两类校验彼此对易 | `definition` | 给出当前局部合法性要求 | LM19, LM06 | U1-C06 | `define`（D04） | S02:15–21；K05 | U01-P3 |
| U1-C08 | 当前需要回答的是构造怎样保证两类校验彼此对易 | `motivation` | 把下一 unit 的问题自然产生 | 无新增 | U1-C07 | `derive`（必要条件产生保证问题） | BRIEF 目标；K05 | U01-P3 末句 |

### Opening contract

- first_sentence_job: 以超图乘积构造为唯一稳定主语；在同一完整句中先给两张经典二进制奇偶校验矩阵这一来源数据，立即插入“每一行规定一条模 2 条件”的短分句，再完成构造 CSS 量子码的类别断言。
- first_paragraph_job: 用连续第二句建立“由这种构造得到的量子码称为 HGP 码”，然后停止扩展；除首句必要的行级提醒外，第一段不承担前置、边界或下游用途。
- stable_referent: 第一对象固定为“超图乘积构造”；第二句的“这种构造”只回指它。
- allowed_vocabulary: 超图乘积构造、经典二进制奇偶校验矩阵、CSS 量子码、HGP 码。
- notation_budget: 首段只允许 HGP、CSS；`A,B,H_X,H_Z` 延后至 P2。
- link_budget: 0；U01 不出现 wikilink。
- forbidden_terms/topics: “既指……也指……”、Künneth、ownership、前置清单、维护边界、Kronecker、链复形、tensor product、stabilizer group、logical quotient。
- closing/transition_job: 末句只能提出“怎样由构造本身保证两类校验彼此对易？”，不得预答或追加第二问题。

### Language contract

- primary_language: 自然、连续的简体中文教材语体。
- permitted_abbreviations: HGP、CSS。
- preferred_terms: 奇偶校验矩阵、X 型校验、Z 型校验、物理量子比特、行、列、支撑、对易、输入、输出。
- English_exceptions: 仅 HGP、CSS 与数学符号 `A,B,H_X,H_Z,X,Z`；不保留普通英文术语。
- prohibited_mixed_language_forms: `parity-check matrix`、`X-type checks`、`row pair`、`support space`、`input role`、`output checks`。
- heading_style: 对象短语或读者已能理解的问题短语；不写流程阶段名。
- rendering_rule: 设计字段名、claim 类型和 role 等元语言不得进入正文。

### Math and sources

- 必须写出：首句内的奇偶校验矩阵行级提醒；构造／所得码关系；`A,B` 输入角色；`H_X,H_Z` 输出角色；共享列与行支撑；CSS 的当前对易要求。
- 只作定位：`A,B,H_X,H_Z` 的四个符号；不操作具体矩阵。
- source anchors: S01、S02；D03 的行级提醒由 K01 支撑。
- 不可承诺：HGP blocks 的具体公式、为何特定 blocks 零复合、码参数或逻辑空间。

### Reader card

- reading_situation: 第一次连续阅读 HGP reference 的开头，尚未进入具体矩阵公式。
- assumed_entry_capabilities: 见过 CSS 名称；能跟随一句模 2 行条件的局部提醒。
- explicitly_not_assumed: 不假设知道 HGP 构造类别、`A,B` 的当前角色、`H_X,H_Z` 的行列含义或 CSS 对易机制。
- expected_exit_capability: 能区分构造、所得码、经典输入和量子输出，并说出接下来必须解决的合法性问题。
- language_register: 简体中文教材语体；只允许 HGP、CSS 与数学符号作为英文／符号例外。

## U02 — 从局部交换规则到零复合

- entry_capabilities:
  - 已完成 U01 出口：能区分 `A,B` 与 `H_X,H_Z`，并知道 `H_X,H_Z` 的共享列和两类行支撑。
  - `LM07`、`LM08`、`LM09`、`LM10`：Pauli 局部规则到偶数重叠／`rationale`／`unverified`。
  - `LM11`：矩阵乘积的行重叠读取／`representation`／`unverified`。
  - `LM12`：零矩阵条件的当前 CSS 角色／`context_role`／`unverified`。
  - `LM18`：X 型／Z 型校验的行支撑到逐位置泡利作用／`representation`／`unverified`；不能与“会读行支撑”合并。
  - `LM13`：链复形名称／`identity`／`named`；只认名称，不承担定义。
  - `LM14`、`LM15`、`LM16`：三项箭头的表示与零复合角色／`unverified`。
- exit_capability: 读者能完整复述 U02-P1 的七步推理，并用 `C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0` 说明三个坐标空间、两个映射、连续复合和 CSS 对易之间的关系。
- why_now: U01 已产生“为何不能任意取两张矩阵、怎样保证对易”的问题；U02 给出判断条件及其统一表达，但仍不展开 HGP blocks 的具体实现。
- primary_pattern: 局部计算 → 抽象 → 支架渐隐。
- supporting_pattern: 问题 → 障碍 → 整体箭头 → 命名。

### Phases

#### U02-P1 — 从局部泡利规则到矩阵对易条件

- cognitive_job: 用一个连续、可逐步复述的机制链，把逐位置交换符号推到所有行对的零矩阵条件。
- required_micro_sequence:
  1. 重申 `H_X,H_Z` 的列是同一组物理量子比特，每行给出一条校验支撑；随即说明 X 型行在支撑位置作用 `X`、Z 型行在支撑位置作用 `Z`，非支撑位置作用 `I`，从而把行向量连接到整条校验算符。
  2. 显式计算／说明同一量子比特上的 `X,Z` 交换产生负号，并用张量积最小计算说明不同量子比特上的作用对易。
  3. 由逐位置符号相乘得到一对异型校验的总符号只由共同作用位置数决定。
  4. 共同位置数为偶数时，负号成对抵消，两条校验对易；在此做一次口头 consolidation。
  5. 展开 `(H_XH_Z^T)_{ij}`，说明它记录对应两行重叠数的模 2 奇偶。
  6. 汇总为 `H_XH_Z^T=0` 等价于所有异型校验对易；做第二次 consolidation。
  7. 用 `H_X=H_Z=[1]` 的最小计算说明共享列仍可得到非零乘积，再明说任意写两张共享列的矩阵不能保证该条件。
- new_entities: 单量子比特泡利算符 `X,Z`；一对 X 型／Z 型校验（不是新矩阵）。
- new_relations: 行支撑到泡利作用的表示、同比特反对易、异比特对易、总符号乘积、偶数重叠、矩阵元重叠奇偶、零矩阵汇总。
- new_notation: `X(x),Z(z),I`、`XZ=-ZX`、`(-1)^w`、`(H_XH_Z^T)_{ij}`、`H_XH_Z^T=0`；每个符号在对应推理步出现并在 consolidation 后释放不用的局部记号。
- holding_set: 当前只保持“一对行支撑”和共同位置数 `w`；到矩阵元步骤释放局部算符矩阵细节。
- consolidation: 微步骤 4 把局部负号汇成“一对校验是否对易”；微步骤 6 把一对行汇成“全部行对”。
- load_justification: 关系数量超过通常单 phase 建议，但用户明确要求它们构成一个不可断开的 P1 推理链；通过七个微步骤、两次 consolidation 与符号逐步引入避免同时操作全部关系。
- forbidden_here: `C_2,C_1,C_0`、“链复形”以及任何 HGP block 公式。

#### U02-P2 — 三项箭头的整体含义与命名

- cognitive_job: 把已理解的矩阵零乘积放入三个有明确坐标含义的空间和两个有明确用途的映射；所有对象闭合后才命名链复形。
- required_micro_sequence:
  1. 展示整体 `C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0`，说明标签暂时只用于定位。
  2. 逐项解释 `C_2` 以 Z 型校验为坐标、`C_1` 以物理量子比特为坐标、`C_0` 以 X 型校验为坐标，三者均为二进制向量空间。
  3. 解释 `H_Z^T` 把一组 Z 型校验的选择映成物理支撑。
  4. 解释 `H_X` 把物理支撑映成向量，每个分量记录其与相应 X 型校验的重叠奇偶。
  5. 说明连续复合就是 `H_XH_Z^T`，并把其为零接回 U02-P1 的全部对易条件。
  6. 只有此时才命名：这种连续两步复合为零的三项向量空间与映射构成当前所需的链复形。
- new_entities: `C_2,C_1,C_0` 三个协调的坐标空间；不把每个基向量或 degree 作为新实体。
- new_relations: 两个映射的输入／输出；复合等于矩阵乘积；零复合统一表达 CSS 对易。
- new_notation: 三个 `C` 标签与一条整体箭头；`H_Z^T,H_X` 均为 P1/U01 已见符号。
- holding_set: 一条三项箭头及“选择—支撑—重叠奇偶向量”三步口头对应。
- consolidation: 在命名“链复形”之前，用一句话从 Z 型校验选择沿箭头走到 X 型重叠奇偶，确认每个对象和映射用途；命名后回到 CSS 对易，不继续扩展术语。
- load_justification: 三个 `C` 标签作为一张整体图共同引入，两个矩阵符号是复用；标签先定位、用途逐项解释，因此需要操作的新符号不超过三个。

### Concept action ledger

| capability_id | subject | facet | evidence_state | action | first_allowed_phase | local_treatment |
|---|---|---|---|---|---|---|
| U01-exit | `H_X,H_Z` 的共享列与行支撑 | `representation` | 本任务前 unit 已闭合 | `remind` | U02-P1 步骤 1 | 一句重申，作为推理对象 |
| LM18 | X 型／Z 型行支撑到泡利作用 | `representation` | `unverified` | `introduce` | U02-P1 步骤 1 | 以 `X(x),Z(z)` 或等价自然语言说明支撑位置作用 `X/Z`、其余位置作用 `I` |
| LM07 | 同一量子比特上的 `X,Z` 反对易 | `rationale` | `unverified` | `introduce` | U02-P1 步骤 2 | 写出显式矩阵或最小乘法，得到 `XZ=-ZX` |
| LM08 | 不同量子比特上的泡利作用对易 | `rationale` | `unverified` | `introduce` | U02-P1 步骤 2 | 展示 `(X\otimes I)(I\otimes Z)` 两种次序相同 |
| LM09 | 总交换符号由共同位置数决定 | `rationale` | `unverified` | `introduce` | U02-P1 步骤 3 | 将各共同位置负号相乘成 `(-1)^w` |
| LM10 | 偶数重叠与成对对易 | `rationale` | `unverified` | `introduce` | U02-P1 步骤 4 | 说明偶数个负号成对抵消 |
| LM11 | 矩阵乘积读成行重叠奇偶 | `representation` | `unverified` | `introduce` | U02-P1 步骤 5 | 展开单个矩阵元求和并逐项解释 |
| LM12 | 零矩阵表示全部异型校验对易 | `context_role` | `unverified` | `introduce` | U02-P1 步骤 6 | 从任意 `i,j` 的矩阵元汇总 |
| LM14 | 三个 `C` 空间的坐标含义 | `representation` | `unverified` | `introduce` | U02-P2 步骤 1–2 | 整体定位后逐项解释 |
| LM15 | `H_Z^T,H_X` 的映射作用 | `representation` | `unverified` | `introduce` | U02-P2 步骤 3–4 | 用“校验选择—物理支撑—重叠奇偶向量”闭合 |
| LM16 | 零复合的当前 CSS 角色 | `context_role` | `unverified` | `introduce` | U02-P2 步骤 5 | 复合等于 `H_XH_Z^T`，回接 P1 |
| LM13 | 链复形名称 | `identity` | `named` | `introduce` | U02-P2 步骤 6 | 名称在对象与用途全部闭合后出现 |
| LM17 | Künneth 名称 | `identity` | `named` | `omit` | 不适用 | U02 完全不出现 |

### Definition cards

#### D05 — X 型与 Z 型校验（当前局部表示）

- definition_depth: 只到二进制行支撑与逐量子比特泡利作用，不引入群或商空间。
- category: 作用在同一组物理量子比特上的两类校验算符。
- basic_data: X 型校验由二进制行 `x` 给出，在 `x_q=1` 的位置作用 `X`、其余位置作用 `I`；Z 型校验由行 `z` 给出并类似作用 `Z/I`。
- current_function: 把 `H_X,H_Z` 的一对行变成可应用局部交换规则的整条算符，从而计算总交换符号。
- discriminates_from: 只把行看作抽象 `0/1` 记录而未说明其物理作用；以及不同校验类型使用的局部算符。
- capability_dependencies: LM18 由本卡直接引入；LM06/U01-exit 提供共享列与行支撑。
- prohibited_shortcuts: 不用 stabilizer group 或 Pauli group 替代逐位置说明；不默认读者会从“支撑”自动补出 `X/Z/I`。
- first_allowed_phase: U02-P1 步骤 1，在任何局部交换推理之前。

#### D06 — 链复形（当前局部含义）

- definition_depth: 只到三项线性映射与零复合；不展开一般次数、cycle、boundary 或 homology。
- category: 一串向量空间和连接它们的线性映射。
- basic_data: 本处为三个二进制向量空间 `C_2,C_1,C_0` 与映射 `H_Z^T,H_X`。
- current_function: 用“连续两步的复合为零”统一表达 `H_XH_Z^T=0`，进而包装所有异型校验对易。
- discriminates_from: 任意三项箭头；仅有空间和映射但复合不为零时，不满足这里的链复形条件。
- capability_dependencies: LM14、LM15、LM16 必须已在正文中逐项闭合；名称证据 LM13 不承担含义。
- prohibited_shortcuts: 不用“链复形就是满足链复形条件的复形”；不以 degree、boundary、homology、Künneth 或几何边界替代当前对象用途；名称不得早于三个空间和两个映射的解释。
- first_allowed_phase: U02-P2 步骤 6，仅在 U2-C09–U2-C15 之后。

### Explanation claim ledger

| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | source_anchor | first_allowed_phase |
|---|---|---|---|---|---|---|---|---|
| U2-C01 | `H_X,H_Z` 的列是同一组物理量子比特，每行给出相应校验支撑 | `role` | 固定逐行推理对象 | U01-exit/LM06 | U1-C06 | `remind` | S02:9–18；PR05 | U02-P1.1 |
| U2-C01R | X 型行 `x` 在支撑位置作用 `X`、Z 型行 `z` 在支撑位置作用 `Z`，其余位置作用 `I` | `definition` | 把矩阵行连接到整条校验算符 | LM18 | U2-C01 | `define`（D05） | LD03；PR07 | U02-P1.1，紧随 U2-C01 |
| U2-C02 | 同一量子比特上的 `X,Z` 交换次序产生负号 | `mechanism` | 提供共同位置的局部符号 | LM07 | U2-C01R | `demonstrate`（显式矩阵） | S04；LD01；PR01 | U02-P1.2 |
| U2-C03 | 不同量子比特上的泡利作用彼此对易 | `mechanism` | 说明不同位置不会额外产生负号 | LM08 | U2-C01 | `demonstrate`（张量积最小计算） | LD02；PR02 | U02-P1.2，紧随 U2-C02 |
| U2-C04 | 一对 X 型与 Z 型校验的总交换符号只由共同作用位置数决定，并等于 `(-1)^w` | `mechanism` | 从局部规则推进到整条校验 | LM09, LM18 | U2-C01R, U2-C02, U2-C03 | `derive` | LD03；PR03, PR07 | U02-P1.3 |
| U2-C05 | 共同位置为偶数时负号成对抵消，两条校验对易 | `inference` | 得到逐对判断 | LM10 | U2-C04 | `derive` | LD03；K09 | U02-P1.4 |
| U2-C06 | `(H_XH_Z^T)_{ij}` 记录 `H_X` 第 `i` 行与 `H_Z` 第 `j` 行重叠数的模 2 奇偶 | `equivalence` | 把行支撑连接到矩阵元 | LM11 | U2-C01 | `demonstrate`（展开求和） | LD04；PR04 | U02-P1.5 |
| U2-C07 | `H_XH_Z^T=0` 同时表示所有异型校验对易 | `equivalence` | 汇总全部行对 | LM12 | U2-C05, U2-C06 | `derive` | LD04；S02 转置条件 | U02-P1.6 |
| U2-C08 | 任意写两张共享列的矩阵不能保证这个零乘积条件 | `boundary` | 回答为什么输出不能是任意 pair | 无新增 | U2-C07 | `demonstrate`（`H_X=H_Z=[1]` 给出非零乘积） | LD06；K13 | U02-P1.7 |
| U2-C09 | `C_2` 是以 Z 型校验为坐标的二进制向量空间 | `definition` | 给箭头起点具体坐标 | LM14 | U2-C01 | `define` | LD05；K11 | U02-P2.2 |
| U2-C10 | `C_1` 是以物理量子比特为坐标的支撑空间 | `definition` | 给中间项具体坐标 | LM14 | U2-C01 | `define` | LD05；K11 | U02-P2.2 |
| U2-C11 | `C_0` 是以 X 型校验为坐标的二进制向量空间 | `definition` | 给箭头终点具体坐标 | LM14 | U2-C01 | `define` | LD05；K11 | U02-P2.2 |
| U2-C12 | `H_Z^T` 把一组 Z 型校验的选择映成物理支撑 | `role` | 解释第一支箭头 | LM15 | U2-C09, U2-C10 | `demonstrate`（行的模 2 叠加） | S02:48–75 的对偶读取；LD05 | U02-P2.3 |
| U2-C13 | `H_X` 把物理支撑映成向量，每个分量记录与相应 X 型校验的重叠奇偶 | `role` | 解释第二支箭头 | LM15, LM11 | U2-C06, U2-C10, U2-C11 | `demonstrate`（矩阵向量分量） | LD04–LD05 | U02-P2.4 |
| U2-C14 | 连续复合就是 `H_XH_Z^T` | `equivalence` | 把两箭头连成已知矩阵条件 | LM16 | U2-C12, U2-C13 | `derive` | LD05；K11 | U02-P2.5 |
| U2-C15 | 连续复合为零统一表达全部异型校验对易 | `equivalence` | 回接 CSS 问题 | LM16 | U2-C07, U2-C14 | `derive` | LD05；K12 | U02-P2.5 |
| U2-C16 | 对象与用途都已闭合的这串零复合映射可称为链复形 | `category` | 只在需求后命名工具 | LM13, LM14, LM15, LM16 | U2-C09, U2-C10, U2-C11, U2-C12, U2-C13, U2-C14, U2-C15 | `define`（D06） | S03；PR06 | U02-P2.6 |
| U2-C17 | 链复形写法把逐对对易条件压缩为“连续两步为零” | `motivation` | 说明命名与整体写法的当前价值 | 无新增 | U2-C15, U2-C16 | `derive` | K12 | U02-P2.6 末 |

### Opening contract

- first_sentence_job: 回接 U01 的真实问题，指出要判断两类校验是否对易，必须先看一对行在同一物理量子比特上的作用；不得以“链复形是……”开头。
- first_paragraph_job: 重申共享列与行支撑，并把注意力缩到一对 X 型／Z 型校验。
- stable_referent: 一对具体校验及其共同支撑位置。
- allowed_vocabulary: U01 已建立术语，加“泡利算符、反对易、重叠奇偶、映射、二进制向量空间、链复形”；后三项仅 P2 按时出现。
- notation_budget: P1 符号逐步出现；P2 整体箭头一次展示，逐项解释。
- link_budget: 0；U02 不出现 wikilink。
- forbidden_terms/topics: P1 禁止 `C_2,C_1,C_0` 和“链复形”；全文禁止 Kronecker blocks、`A/B` 尺寸、total degree、两路径抵消、homology、Künneth、stabilizer group、logical quotient。
- closing/transition_job: 以“连续两步为零”对 CSS 对易的统一表达收束；不预告被禁止的具体 HGP block 证明。

### Language contract

- primary_language: 自然、连续的简体中文教材语体。
- permitted_abbreviations: HGP、CSS。
- preferred_terms: 泡利算符、同一量子比特、不同量子比特、X 型校验、Z 型校验、行、列、支撑、共同位置、重叠、重叠奇偶、对易、反对易、二进制向量空间、映射、连续复合、链复形。
- English_exceptions: 仅 HGP、CSS 和数学符号／公式；`Pauli` 正文写“泡利”，`vector space` 写“向量空间”。
- prohibited_mixed_language_forms: `local Pauli rule`、`row pair`、`support space`、`overlap parity`、`X-type/Z-type checks`、`zero composition`。
- heading_style: 使用“为什么偶数重叠给出对易”“把条件写成连续两步为零”一类已可理解的问题／对象短语，不写 P1/P2 或 contract 字段。
- rendering_rule: because/therefore 可自然写作“因为／因此”，但每个因果句必须按 claim ledger 显式闭合前提。

### Math and sources

- 必须写出：行支撑到 `X/Z/I` 逐位置作用的表示桥梁；LD01 或等价的显式 `2\times2` 乘法；LD02 的最小张量积计算；`(-1)^w`；矩阵元展开；零矩阵等价；LD06 最小非零反例；完整三项箭头；三个空间和两个映射的逐项意义；复合矩阵。
- 可压缩但不可省略：LD01 的矩阵可由 `XZ=-ZX` 配合已展示的 `X,Z` 矩阵完成；LD02 两个次序必须都出现。
- source anchors: S02、S03、S04、LD01–LD06；S05 仅供 Contract Auditor 交叉核对。
- 不可承诺：任意 HGP 输入的参数、具体 block 构造、两路径抵消、逻辑空间或 Künneth 结论。

### Reader card

- reading_situation: 已读完 HGP 开头的对象与输入／输出区分，正在追问两类输出校验为何必须且如何能够彼此对易。
- assumed_entry_capabilities: 能读出 `H_X,H_Z` 的共享列和两类行支撑；知道 `A,B` 与输出矩阵不是同一角色。
- explicitly_not_assumed: 不假设能从一行的支撑读出整条校验算符的逐位置作用；也不假设泡利局部交换规则、总交换符号、重叠奇偶的矩阵读取、三项箭头或链复形含义。
- expected_exit_capability: 能从局部交换规则独立重建矩阵对易条件，并能说明三项箭头中各对象与连续复合的当前用途。
- language_register: 简体中文教材语体；HGP、CSS 与数学符号之外不使用不必要英文。

# 拆分与整合决定

- 不拆正式文件。U01、U02 是同一 guided reference 开头的两个 staged unit fragments。
- 本 pilot 只生成 `DRAFTS/U01.md`、`DRAFTS/U02.md`；不修改目标文件，不生成 integration 产物。
- Writer packet 不需要、也不得包含 canonical/index；授权数学均由 packet 的来源摘录与 local derivations 自足提供。

# 需要用户决定

- 无。目标、顺序、禁止主题和停止点均已固定；没有两条互斥的长期路线或来源冲突。
