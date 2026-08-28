---
learner_revision: 1
evidence_date: 2026-08-28
---

# 当前目标

- U01 后，读者能够区分超图乘积构造、由该构造得到的 HGP 码、两份输入 `A、B` 与输出 `H_X,H_Z`。
- U02-P1 后，读者能够从逐位置 Pauli 交换规则解释偶数重叠为何使一对异型校验对易，并把全部异型校验对易读成 `H_XH_Z^T=0`。
- U02-P2 后，读者能够说明三项箭头中三个空间与两个映射的当前用途，并把零复合与 CSS 对易条件联系起来。
- 完整的 Pauli `2×2` 矩阵逐项计算不是本次出口能力；辅助计算只服务于必要的局部依据，不能取代 HGP 主线。
- 上述目标只服务于本次 U01/U02 staged manuscript；没有实际出口表现前，不回写长期 learner 状态。

# 证据边界

- `Notes/LEARNER/PROFILE.md`、`KNOWLEDGE_STATE.md` 与 `QUESTIONS.md` 没有提供可升级本表状态的长期表现证据。
- v4 pilot 的 snapshot 是本次可复核的历史任务证据，但 staged draft 的存在不等于读者已经掌握其中内容。
- 本轮用户明确规定完整 Pauli 矩阵计算不是出口能力，并明确要求 evidence state 与 explanation depth 分离。
- 仓库中是否已有稳定 CSS／Pauli detail、以及正式 HGP 后文是否重复，属于 Domain 与 Canonical detail inventory；文件存在不构成 learner capability 证据。

# Faceted capabilities

| capability_id | subject | facet | evidence_state | scope | evidence | evidence_date | confidence | risk_flags |
|---|---|---|---|---|---|---|---|---|
| LM01 | 经典二进制奇偶校验矩阵的一般含义 | `identity` | `unverified` | 是否知道每一行规定一条模 2 的奇偶校验条件；不含 HGP 中的输入角色 | 长期知识状态无记录，用户未展示定义复述或使用表现 | 2026-08-28 | high | `claim-gap` |
| LM02 | `A、B` 在 HGP 中是两份种子输入 | `context_role` | `unseen` | 只限本构造中的输入角色；不含一般奇偶校验矩阵定义、矩阵尺寸或块构造 | v4 明确的第一次接触证据；本轮没有相反表现证据 | 2026-08-28 | high | `role-confusion` |
| LM03 | 超图乘积构造的对象类别 | `identity` | `unseen` | 是否知道它是从两张经典二进制奇偶校验矩阵构造 CSS 量子码的方法 | v4 明确的第一次接触证据；本轮没有升级证据 | 2026-08-28 | high | `role-confusion` |
| LM04 | 超图乘积构造与所得 HGP 码的关系 | `context_role` | `unseen` | 构造产生一个码，所得码因该构造而称为 HGP 码；不把构造与码合并成同一对象 | v4 明确的第一次接触证据；本轮仍将区分二者列为目标表现 | 2026-08-28 | high | `role-confusion` |
| LM05 | CSS 这一名称 | `identity` | `named` | 只支持识别 CSS 名称；不支持其当前局部含义、表示或对易机制 | v4 只提供名称层面证据；没有含义或操作表现 | 2026-08-28 | high | `claim-gap` |
| LM06 | `H_X,H_Z` 的共享列与行支撑 | `representation` | `unverified` | 是否能把共享列读成同一组物理量子比特，并把每一行读成一条相应类型校验的支撑 | 用户未展示矩阵行列或支撑的读取表现 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM07 | 同一量子比特上的 Pauli `X、Z` 反对易 | `rationale` | `unverified` | 是否能解释交换顺序为何产生一个负号，而非只识别公式 | 用户未展示局部交换推导或口头解释 | 2026-08-28 | high | `claim-gap` |
| LM08 | 不同量子比特上的 Pauli 作用彼此对易 | `rationale` | `unverified` | 是否能根据不同张量因子解释两处局部作用可交换 | 用户未展示张量积推理或相应解释 | 2026-08-28 | high | `claim-gap` |
| LM09 | 一对 X 型与 Z 型校验的总交换符号由共同作用位置数决定 | `rationale` | `unverified` | 是否能说明每个共同位置贡献一个负号，非共同位置不贡献负号，总符号为 `(-1)^w` | 没有从局部 Pauli 规则推进到整条校验交换符号的表现证据 | 2026-08-28 | high | `claim-gap` |
| LM10 | 偶数重叠与一对异型校验对易的关系 | `rationale` | `unverified` | 是否能说明偶数个负号成对抵消，重叠奇偶决定交换结果 | 用户只给出目标表现，没有展示该推导 | 2026-08-28 | high | `claim-gap` |
| LM11 | 矩阵乘积读成行对重叠奇偶 | `representation` | `unverified` | 是否能把 `(H_XH_Z^T)_{ij}` 读成 `H_X` 第 `i` 行与 `H_Z` 第 `j` 行共同非零列数的模 2 奇偶 | 用户未展示元素展开或行重叠解释 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM12 | `H_XH_Z^T=0` 在当前 CSS 问题中的作用 | `context_role` | `unverified` | 是否能把所有行对的偶数重叠汇总为全部异型校验对易；不含完整稳定子形式化 | 没有把逐对条件汇总成矩阵等式的表现证据 | 2026-08-28 | high | `claim-gap`, `role-confusion` |
| LM13 | 链复形这一名称 | `identity` | `named` | 只支持识别名称；不支持三项箭头的对象、映射或运算 | v4 只提供名称层面证据；没有表示或操作表现 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM14 | 三项箭头中 `C_2,C_1,C_0` 的坐标含义 | `representation` | `unverified` | 是否能分别读成以 Z 型校验、物理量子比特、X 型校验为坐标的二进制向量空间 | 用户没有展示对三类坐标空间的读取表现 | 2026-08-28 | high | `notation-overload` |
| LM15 | `H_Z^T` 与 `H_X` 在三项箭头中的映射作用 | `representation` | `unverified` | 是否能把前者读成“校验选择到物理支撑”，后者读成“物理支撑到各 X 型校验的重叠奇偶向量” | 用户没有展示对两个箭头输入、输出或分量意义的读取表现 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM16 | 零复合在当前 CSS 问题中的作用 | `context_role` | `unverified` | 是否能说明连续复合为 `H_XH_Z^T`，其为零统一表达全部 CSS 对易条件 | 用户只给出目标表现，没有展示零复合的当前作用 | 2026-08-28 | high | `claim-gap`, `role-confusion` |
| LM17 | Künneth 这一名称 | `identity` | `named` | 只支持识别名称；U01/U02 必须 `omit`，不推断其用途或内容 | v4 的名称层面证据和本轮明确的范围排除 | 2026-08-28 | high | `notation-overload` |
| LM18 | X 型／Z 型校验的行支撑怎样对应 Pauli 作用 | `representation` | `unverified` | 是否能把二进制行中的 `1` 读成相应位置上的 `X` 或 `Z`，把 `0` 读成恒等作用 | 用户要求建立这一主线桥接，但未展示表示能力 | 2026-08-28 | high | `claim-gap`, `notation-overload` |
| LM19 | CSS 在当前段落中的局部含义 | `context_role` | `unverified` | 是否知道此处只取同一组物理量子比特上的 X 型、Z 型校验及二者彼此对易，不含更完整形式化 | CSS 的 `named` 证据不能承担当前用途；用户未展示局部含义 | 2026-08-28 | high | `role-confusion`, `claim-gap` |
| LM20 | 显式 Pauli `2×2` 矩阵逐项相乘 | `procedure` | `unverified` | 是否能完成矩阵乘法并直接验证 `XZ=-ZX`；明确不是本次出口能力 | 用户没有展示计算表现，并明确排除该计算作为本次出口能力 | 2026-08-28 | high | `over-explanation-risk` |

# 出口能力边界

| 项目 | 是否为当前出口能力 | 证据与约束 |
|---|---|---|
| 区分构造、所得码、输入与输出 | 是 | 用户明确列为目标表现 |
| 从局部交换规则解释偶数重叠和矩阵对易条件 | 是 | 用户明确列为目标表现；需要能复述理由，不要求完整矩阵计算 |
| 用三项箭头解释零复合 | 是 | 用户明确列为目标表现 |
| 完整 Pauli `2×2` 矩阵逐项计算 | 否 | 用户明确排除；若设计保留，只能作为可跳过的局部依据或上游 bridge，不能成为理解主线的前提 |

# Evidence state 与 explanation depth 分离

- 本表的 `unverified` 只表示缺少读者表现证据，不表示第一次接触，也不自动要求 full derivation。
- `unseen` 与 `named` 来自已有明确证据，但仍不直接决定正文深度。
- reminder、introduce、compact derivation、optional derivation、upstream bridge 或 omit 由 Didactic Architect 根据出口能力、中心性、风险、主线成本和 canonical duplication 决定。
- 用户在本轮指定的 depth／placement 是设计合同，不是从本表的 evidence state 推导出的结论。

# 可以直接使用

- 可以把 CSS、链复形和 Künneth 当作读者见过的名称；名称证据不支持省略当前局部含义、对象用途或推理步骤。
- U01/U02 对 Künneth 的合法处理是 `omit`。
- 可以按任务合同把完整 `2×2` 矩阵计算排除在出口能力之外；这不等于假设读者已经会算。
- 除名称识别外，目前没有可直接承担本次解释链的 `operational` 或 `fluent` 能力证据。

# 不得直接假设

- 不得直接假设读者知道经典奇偶校验矩阵的一般含义；若正文需要，可在首次 dependent use 前局部提醒“每一行规定一条模 2 的奇偶校验条件”。
- 不得把“经典奇偶校验矩阵是什么”与“`A、B` 是 HGP 的两份输入”合成同一状态。
- 不得把超图乘积构造、由构造所得的 HGP 码、输入 `A、B` 和输出 `H_X,H_Z` 合并成同一对象身份。
- 不得从见过 CSS 名称推断读者已经知道共享列、行支撑、局部 Pauli 表示或对易条件。
- 不得从“行给出支撑”直接跳到整条校验的 Pauli 作用；必须闭合 `1/0` 与 `X/Z/I` 的表示桥接。
- 不得跳过同一量子比特与不同量子比特两条局部交换规则，也不得跳过从局部负号到 `(-1)^w`、偶数重叠和矩阵元素的中间理由。
- 不得直接假设读者会读取三项箭头中的坐标空间、两个映射或零复合的当前用途；见过链复形名称不足以承担这些能力。
- 不得因为 LM20 是 `unverified` 就把完整 `2×2` 矩阵计算放进主线。

# 近期真实问题

- 长期 learner 文件没有记录近期回答、计算或迁移表现，当前没有可用于升级上述能力状态的新证据。
- 当前问题是怎样以足够但不过量的 Pauli 细节支撑 HGP 对易主线；这是设计与比例性风险，不是读者已经掌握或完全未见某项内容的证据。
- 主要风险是 `role-confusion`、`claim-gap`、`notation-overload` 和 `over-explanation-risk`：对象角色可能混合，局部规则到矩阵条件的理由可能断裂，三项箭头可能过载，辅助计算可能压过 HGP 主问题。

# 可能改变路线的不确定项

- Learner 阶段没有需要向用户追问的分歧。用户已固定出口能力与 U01/U02 范围；其余缺证据项保持 `unverified`。
- CSS／Pauli 的稳定 canonical detail 和正式 HGP 后续段落的重复范围必须由 Mapper 在 Domain/Source Packet 中核对；若关键 premise 无来源或局部推导锚点，应返回 mapping，而不是改变 learner state。
- 若后续真实 cold-read 表现显示局部 bridge 不足或辅助 detail 过重，应分别返回 design 调整 depth／placement；不得据此静默升级长期 learner 状态。
