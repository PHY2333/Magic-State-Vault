---
learner_revision: 2
---

# 当前目标

- 读者在 U01 后能够区分超图乘积构造、构造的两份输入 `A、B`、构造输出 `H_X,H_Z` 与由该构造得到的 HGP 码。
- 读者在 U02-P1 后能够从 Pauli 的局部交换规则解释偶数重叠为何对应一对异型校验对易，并把全部异型校验对易读成 `H_XH_Z^T=0`。
- 读者在 U02-P2 后能够说明三项箭头中三个空间和两个映射的当前用途，并把“连续两步为零”与 CSS 对易条件联系起来。
- 上述状态转移只服务于本次 U01/U02 staged draft；没有实际出口表现前，不回写长期 learner 状态。

# Faceted capabilities

| capability_id | subject | facet | evidence_state | scope | evidence | evidence_date | confidence | risk_flags |
|---|---|---|---|---|---|---|---|---|
| LM01 | 经典二进制奇偶校验矩阵的一般含义 | `identity` | `unverified` | 是否知道这类矩阵的每一行规定一条模 2 奇偶校验条件；不含 HGP 中的角色 | 长期知识状态无记录，用户也未展示定义复述；Brief 明确标为无直接掌握证据 | 2026-08-28 | high | `claim-gap` |
| LM02 | `A、B` 在 HGP 中是两份种子输入 | `context_role` | `unseen` | 只限本构造中的输入角色；不含矩阵尺寸或具体块构造 | 用户明确指定该角色为第一次接触；Brief 复核为 `unseen` | 2026-08-28 | high | `role-confusion` |
| LM03 | 超图乘积构造的对象类别 | `identity` | `unseen` | 是否知道它是从两张经典二进制奇偶校验矩阵构造 CSS 量子码的方法 | 用户明确指定 HGP 构造类别为 `unseen`；没有更高能力证据 | 2026-08-28 | high | `role-confusion` |
| LM04 | 超图乘积构造与所得 HGP 码的关系 | `context_role` | `unseen` | 构造产生一个码、所得码因该构造而称为 HGP 码；这里采用 `context_role`，因为考察的是构造与其输出在当前叙述中的关系，不是把二者合成一个对象身份 | 用户明确指定构造与所得码关系为 `unseen`；Brief 无复述或应用证据 | 2026-08-28 | high | `role-confusion` |
| LM05 | CSS 这一名称 | `identity` | `named` | 只支持“见过 CSS 这个名称”；不支持其定义、校验结构或对易条件 | 用户展示了名称但没有含义或操作证据；Brief 明确只授权名称层面 | 2026-08-28 | high | `claim-gap` |
| LM06 | `H_X,H_Z` 的共享列与行支撑 | `representation` | `unverified` | 是否能把共享列读成同一组物理量子比特，并把每一行读成一条相应类型校验的支撑 | 用户未展示矩阵行列或支撑的读取；Brief 明确标为无直接掌握证据 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM07 | 同一量子比特上的 Pauli `X、Z` 反对易 | `rationale` | `unverified` | 是否能解释交换顺序为何产生负号，而非仅识别公式 | 用户未给出显式矩阵计算、局部交换推导或口头解释 | 2026-08-28 | high | `claim-gap` |
| LM08 | 不同量子比特上的 Pauli 作用彼此对易 | `rationale` | `unverified` | 是否能根据不同张量因子解释两处局部作用可交换 | 用户未展示张量积计算或相应理由 | 2026-08-28 | high | `claim-gap` |
| LM09 | 一对 X 型与 Z 型校验的总交换符号由共同作用位置数决定 | `rationale` | `unverified` | 是否能把每个共同位置的负号相乘，并说明非共同位置不贡献负号 | 没有从局部 Pauli 规则推进到整条校验交换符号的表现证据 | 2026-08-28 | high | `claim-gap` |
| LM10 | 偶数重叠与一对异型校验对易的关系 | `rationale` | `unverified` | 是否能说明偶数个负号成对抵消，奇偶性决定交换结果 | 用户只给出目标表现，没有展示该推导 | 2026-08-28 | high | `claim-gap` |
| LM11 | 矩阵乘积读成行对重叠奇偶 | `representation` | `unverified` | 是否能把 `(H_XH_Z^T)_{ij}` 读成 `H_X` 第 `i` 行与 `H_Z` 第 `j` 行共同非零列数的模 2 奇偶 | 用户未展示元素展开或行重叠解释；Brief 明确标为无直接掌握证据 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM12 | `H_XH_Z^T=0` 表示全部异型校验对易 | `context_role` | `unverified` | 只限该矩阵等式在当前 CSS 问题中的作用；不含一般稳定子形式化 | 没有把逐行重叠条件汇总为矩阵等式的表现证据 | 2026-08-28 | high | `claim-gap`, `role-confusion` |
| LM13 | 链复形这一名称 | `identity` | `named` | 只支持“见过链复形这个名称”；不支持定义、对象识别或运算 | 用户展示了名称但没有含义或操作证据；Brief 明确只授权名称层面 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM14 | 三项箭头中 `C_2,C_1,C_0` 的坐标含义 | `representation` | `unverified` | 是否能分别读成以 Z 型校验、物理量子比特、X 型校验为坐标的二进制向量空间 | 用户没有展示对三类坐标空间的读取能力 | 2026-08-28 | high | `notation-overload` |
| LM15 | `H_Z^T` 与 `H_X` 在三项箭头中的映射作用 | `representation` | `unverified` | 是否能把前者读成“校验选择到物理支撑”，后者读成“物理支撑到各 X 型校验的重叠奇偶向量” | 用户没有展示对两个箭头输入、输出或分量意义的读取能力 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM16 | 零复合在当前 CSS 问题中的作用 | `context_role` | `unverified` | 是否能说明连续复合为 `H_XH_Z^T`，其为零统一表达全部 CSS 对易条件 | 用户只给出目标表现，没有展示零复合的当前作用；Brief 明确标为无直接掌握证据 | 2026-08-28 | high | `claim-gap`, `role-confusion` |
| LM17 | Künneth 这一名称 | `identity` | `named` | 只支持“见过 Künneth 这个名称”；U01/U02 必须 `omit`，不推断任何用途或内容 | 用户展示了名称并明确限制为 `named`，同时要求本次两单元不出现 | 2026-08-28 | high | `notation-overload` |
| LM18 | X 型／Z 型校验的行支撑怎样对应泡利作用 | `representation` | `unverified` | 是否能把二进制行的 `1` 读成 X 型校验在该物理量子比特上作用 `X`、Z 型校验作用 `Z`，并把 `0` 读成恒等作用 | 用户只指定行支撑与局部泡利规则，没有展示从行向量到整条校验算符的表示能力；Design Audit revision 1 暴露该桥接缺口 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM19 | CSS 在当前段落中的局部含义 | `context_role` | `unverified` | 是否知道此处只取同一组物理量子比特上的 X 型、Z 型校验及二者彼此对易，不含更完整形式化 | 用户只展示 CSS 名称，名称证据不能承担当前用途；Design Audit revision 1 要求把标签识别与局部含义分面 | 2026-08-28 | high | `role-confusion`, `claim-gap` |

# 可以直接使用

- 可把 CSS、链复形和 Künneth 视为读者见过的名称，但这种证据只支持名称识别，不支持省略局部定义、对象用途或推理步骤。
- U01/U02 对 Künneth 的唯一合法处理是 `omit`；名称层面的已有证据不构成引入理由。
- 除上述名称识别外，目前没有可直接承担本次解释链的 `operational` 或 `fluent` 能力证据。

# 不得直接假设

- 不得直接假设读者知道经典奇偶校验矩阵的一般含义；若正文需要，只能局部提醒“每一行规定一条模 2 的奇偶校验条件”。
- 不得把“经典奇偶校验矩阵是什么”与“`A、B` 是 HGP 的两份输入”合成一个状态或一次未经区分的引入。
- 不得直接假设读者知道超图乘积构造的类别，或知道该构造与 HGP 码之间的产生和命名关系。
- 不得从见过 CSS 名称推断读者已经知道 `H_X,H_Z` 的表示、共享列的意义或对易条件。
- 不得从“行给出支撑”直接跳到整条校验的泡利算符乘积；必须说明支撑位置上的 `X/Z` 作用与非支撑位置上的恒等作用。
- 不得跳过同一量子比特与不同量子比特两条 Pauli 局部交换规则，也不得跳过从局部负号到总符号、偶数重叠和矩阵元素的中间推理。
- 不得直接假设读者会读取三项箭头中的坐标空间、两个映射或零复合的当前用途；“见过链复形名称”不足以承担这些能力。

# 近期真实问题

- 长期 learner 文件没有记录近期回答、计算或迁移表现；当前没有可用于升级上述能力状态的真实学习者证据。
- Brief 中记录的是现有 HGP 开头的教学组织问题：构造、所得码、自动对易、前置链接和 Künneth 边界拥挤在同一段，且历史 draft 存在词典式首句与中英混合速记。这些是设计风险，不是读者已掌握或未掌握某项能力的额外证据。
- 本次关键风险是 `role-confusion` 与 `claim-gap`：构造身份、输入角色和所得码关系容易被合并；Pauli 局部规则到矩阵零乘积的解释前提容易被省略。

# 可能改变路线的不确定项

- 无需在本阶段向用户追问。用户已固定 U01/U02 的目标、顺序、局部提醒与完整引入范围；上述 `unverified` 状态会影响 Architect 选择 `remind` 或 `introduce`，但不会导致两条互斥路线。
- 若后续 mapping 无法为 Pauli 交换规则或矩阵重叠解释提供已核对来源／局部计算锚点，应返回 mapping 处理；这不是 learner 状态问题，也不授权把 `unverified` 提升为已掌握。
