---
task_id: 20260829-hgp-whole-note-coverage-audit
status: changes-required
audit_scope: whole-note-coverage
target: Notes/07-Lifted-Product Code/Hypergraph product code.md
target_head: e837e97b8c35f0cad9f2a6b5ded7d9ea4c87f2ee
target_blob: 3251b0075281fdf4dc86fccb230ae44397732bad
validated_scope:
  - U01
  - U02
whole_note_reviewed: false
formal_file_modified: false
writer_packet_generated: false
---

# Whole-note verdict

当前正式文件不能据 U01/U02 的 v5 通过结论标为整篇通过。覆盖审查把开头 U01、U02-P1、U02-P2 三个单元保持为 `validated`；来源节为 `legacy-audited`；其余十个 legacy section 均为 `changes-required`。本轮没有 `legacy-unreviewed` section，因为所有现有标题都已进入覆盖审查，但“已审查”不等于“已验证”。

正式文件 frontmatter 中现有的 `status: reviewed` 是被观察到的仓库状态，不在本轮扩展为 whole-note verdict，也未被修改。整篇后续重构必须保留已验证 U01/U02 的范围边界，不能把 legacy 风险倒灌成对其 reader-visible 文本的静默修改。

| review state | section 数 | 范围 |
|---|---:|---|
| `validated` | 3 | U01、U02-P1、U02-P2 |
| `legacy-audited` | 1 | 来源 |
| `legacy-unreviewed` | 0 | 无 |
| `changes-required` | 10 | 从经典输入到 LP 过渡的全部 legacy 主体 |

# Audit evidence and protection baseline

- 审查基线为提交 `e837e97b8c35f0cad9f2a6b5ded7d9ea4c87f2ee` 下的目标 blob `3251b0075281fdf4dc86fccb230ae44397732bad`。
- U01/U02 的有效范围依据现有 revision 5 `MANUSCRIPT_VERDICT.md` 与 `INTEGRATION_REPORT.md`，不外推到第 107 行之后的 legacy 内容。
- canonical 路由表明：HGP 主笔记承担构造、校验矩阵、参数与到 LP 的入口；Künneth 的完整分解由独立笔记承担；S007 的记号转换属于已登记的论文特定接口。
- 仓库内可核对 total degree 与 tensor-product differential，也可核对 Künneth 的独立 owner；但正文当前没有把这些稳定前置转化成平滑的读者桥梁。
- S007 来源已在仓库登记。HGP 参数定理与 LP 构造的两项主要外部原始来源可以核对，但当前来源登记尚不足以给 legacy 关键 claim 提供稳定、claim-local 的仓库锚点。

# Mandatory regression checks

| 检查项 | 结论 | 覆盖判断 |
|---|---|---|
| U02 到“从两张经典校验矩阵开始”的难度跳变 | `changes-required` | U02 只建立三项箭头的当前用途；下一节立即假设读者能把两张矩阵看成带次数的二项复形，并操作转置与张量积。缺失的是从“要构造两支映射”到“为什么选择这两个二项复形”的动机和入口能力，不是再重复 CSS 对易。 |
| 二项链复形引入是否有动机 | `changes-required` | 当前先陈列两个二项复形，再说明它们可取张量积；未先交代它们分别编码哪张经典校验矩阵、为何这种方向能产出所需的中间空间与两支边界映射。 |
| total degree 与两个物理扇区 | `changes-required` | 公式与维数匹配，但 total degree 的形成、两个直和项为何成为物理比特坐标，以及代数分次与 CSS 解释之间的转换集中出现，推导次序不足。两个物理扇区不能与后面的两个逻辑同调分量混同。 |
| 四个 Kronecker blocks | `changes-required` | block 公式、维数与转置安排在数学上相容；但四块各自的 source/target、作用于哪个物理扇区及其校验含义没有在一般 HGP 语境逐块闭合。真正的逐块边解释延迟到 S007 记号，造成一般构造依赖论文适配层。 |
| S007 记号的 placement | `changes-required` | 一般 Tanner 边与行列方向属于 HGP 主线；S007 符号转换应是 optional adapter，执行语义应归 paper-guide。当前这些职责混在一起，且“校验节点”到“校验辅助比特”的对象层级变化未显式限定。迁移前还需处理现有 canonical ownership，不能直接删移。 |
| Künneth 是否自然引入 | `changes-required` | 它在“逻辑空间由什么决定”之后出现，问题动机基本自然；但被标为可选后，后续 `sqrt(N)` 参数段又使用其 `H_1` 分解与逻辑类，因此 optional skip test 失败。同时 `H_1` 既出现在 S007 矩阵记号又出现在同调记号中，存在类型冲突。 |
| qLDPC 与 `sqrt(N)` | `changes-required` | qLDPC 的结论可保留在参数主线，但当前压成一句，缺少行/列权重如何传到四个 Kronecker blocks 的紧凑推导。`sqrt(N)` 家族适合独立 derivation 或可跳过证明；当前距离上界依赖未展开的非平凡逻辑类，且来源映射不够稳定。 |
| HGP 到 LP 的“环元素/置换” | `changes-required` | 当前把一般环元素过快等同于置换矩阵。群基元素或单项式可对应一个置换；群代数/多项式环的一般元素通常对应置换之和；任意有限维代数元素则只给一般线性 block。非交换情形还需要左右模作用。这里是范围错误，不只是措辞密度问题。 |

# Cross-section risk register

| ID | 严重度 | 风险 | 影响范围 | 后续路由 |
|---|---|---|---|---|
| COV-01 | high | 正式 frontmatter 的 `reviewed` 容易被误读为整篇 v5 通过 | 全篇 | 在未来任务元数据中显式区分 validated opening 与 legacy coverage；本轮不改 frontmatter |
| TRN-01 | high | U02→经典输入的入口能力断层，HGP 主问题在抽象复形操作中暂时消失 | S02→S03 | mapping + didactic design |
| DEP-01 | high | total degree、直和中间项与物理扇区同批引入，premise 与解释层级未分离 | S03–S04 | definition/claim/depth design |
| MAP-01 | high | 四块只有整体公式，通用的逐块语义被推迟到 S007 | S05–S08 | generic HGP unit redesign |
| TYPE-01 | high | S007 的矩阵、校验节点和辅助比特层级混用，且 owner 边界不清 | S06–S08 | ownership decision + paper-guide split |
| LOG-01 | high | 物理扇区与逻辑同调分量可能混同；`H_1` 记号冲突；Künneth optional skip 失败 | S04、S06、S09、S11 | logical-space interface redesign |
| PAR-01 | medium | qLDPC 条件缺少从经典稀疏性到量子校验权重的可见推导 | S10 | compact parameter derivation |
| PAR-02 | high | `d=d_A` 上界依赖未落地的逻辑类；关键来源未形成稳定仓库锚点 | S11、来源 | source mapping + separate derivation |
| LP-01 | critical | “环元素就是置换”把特殊代数表示泛化为一般事实 | S12 | domain/source remapping before design |
| LANG-01 | medium | `check ancilla`、`sector`、`logical space` 等中英混合与既有中文术语不统一 | S04–S12 | language contract |
| SRC-01 | high | 关键 HGP 参数与 LP 范围 claim 没有稳定的 claim-local 来源登记 | S11–S13 | Papers source registration decision + source packet |
| DUP-01 | medium | block 解释、对易验证和 Tanner 方向在一般构造与 S007 适配层重复 | S05–S08 | ownership/placement design |

# Whole-note reconstruction unit boundaries

以下边界只规定未来重构的知识职责、入口与出口，不规定逐句写法。

| future unit | 当前材料范围 | 单元职责与出口 | 主要边界风险 |
|---|---|---|---|
| V-U01：构造、码与输入/输出角色 | 当前行 7–11 | 保留 revision 5 的已验证 opening；出口是区分构造、HGP 码、输入 `A,B` 与输出 `H_X,H_Z`，并提出对易保证问题 | 不得因 legacy 重构改写已验证字句 |
| V-U02a：局部交换到矩阵条件 | 当前行 13–89 | 保留 revision 5；出口是偶数重叠与 `H_XH_Z^T=0`，optional Pauli block 可跳过 | 不把 optional 细节变成后续隐藏前置 |
| V-U02b：三项箭头与零复合 | 当前行 91–105 | 保留 revision 5；出口是三个坐标空间、两支映射与零复合的当前 CSS 用途 | 下一单元必须重新建立构造动机，不能假设完整链复形语言 |
| R-U03：经典种子作为二项复形 | 当前行 107–155 | 解释为什么将 `A,B` 放入两个二项复形，以及它们怎样服务于构造 `C_2→C_1→C_0` | 解决难度跳变与方向选择的动机；不提前塞入全部 tensor-product machinery |
| R-U04：total degree 与两个物理扇区 | 当前行 157–185 | 先闭合 total degree 的代数来源，再把中间直和解释为两类物理比特坐标 | 严格区分物理扇区与逻辑同调分量 |
| R-U05：乘积边界、四块与对易 | 当前行 187–250，加上当前行 317–353 的一般逐块语义 | 从两个 differential 导出 `H_X,H_Z`，逐块说明 source/target 与扇区，并完成零复合 | 四块解释必须在一般 HGP 层闭合，不依赖 S007；保持 HGP 主问题 |
| R-U06：一般 HGP 的 Tanner 边与行列方向 | 当前行 317–392 中可脱离 S007 的内容 | 给出四类一般 Tanner 邻接与乘积方向的读法 | 先去除 S007 专名依赖，再判定与 R-U05 的重复边界 |
| O-S007：论文记号适配与执行接口 | 当前行 252–315 及行 317–375 的 S007 特定片段 | optional adapter 只承担 HGP 通用记号到 S007 式 (1) 的转换；执行语义由 paper-guide 承担 | canonical 当前保留转换 ownership，移动或拆分需显式决定；避免节点/辅助比特类型偷换 |
| R-U07：有限长度与逻辑维数接口 | 当前行 394–411 | 导出 `N`、秩关系和 `K` 的有限维表达，并提供后续所需的最小核/余核接口 | 不在此把完整 Künneth 当作必经主线 |
| O-K：Künneth 逻辑空间分解 | 当前行 413–447 | 真正可跳过的 canonical bridge；回答逻辑分量来源，但完整定理留给独立 owner | 下游主线不得再依赖跳过内容；解决 `H_1` 记号冲突和对象类型 |
| R-U08：qLDPC 继承 | 当前行 449–451 | 用紧凑 derivation 说明经典行列稀疏性如何限制量子校验权重与比特度 | 当前一句式结论过薄，但不应膨胀成全篇中心 |
| D-SQRT：标准 `sqrt(N)` 参数基准 | 当前行 453–495 | 将特例计算作为独立 derivation 或可跳过证明；主线只保留有范围、有来源的参数基准 | 距离上界需显式逻辑类；需稳定来源锚点；不能暗中依赖 optional Künneth |
| R-U09：从 HGP 到 LP 的安全接口 | 当前行 497–526 | 只在清楚区分基元素、代数元素及其线性表示后说明 LP 如何推广 block | 修复一般环元素/置换的范围错误；非交换情形需左右作用约束 |
| R-SRC：claim-local 来源映射 | 当前行 528–532 | 将来源分别绑定到 HGP 构造/参数、S007 适配与 LP 范围 claim | 来源清单不能代替稳定登记与局部 claim 追踪 |

# Proposed mainline order

未来主线建议按知识依赖排列：已验证 U01/U02 → 经典种子的二项复形角色 → total degree 与物理扇区 → 两支乘积边界及四块 → 零复合/对易 → 有限参数 → qLDPC 继承 → 有范围限制的 HGP→LP 接口。

Künneth、完整 `sqrt(N)` 证明和 S007 适配分别作为可独立跳过的 logical-space bridge、parameter derivation 与 paper adapter；一般 Tanner 解释留在 HGP 主线。是否拆成文件不是本次 coverage audit 的结论，需要后续 ownership 与 didactic design 决定。

# Review-state conclusion

- `validated` 仅覆盖当前 U01/U02 的三个 section，不覆盖后续 legacy 文本。
- 来源节只达到 `legacy-audited`：已识别来源职责与缺口，但未完成逐 claim 验证。
- 十个 legacy 主体 section 都有至少一个结构、解释、类型、数学范围或来源风险，因此为 `changes-required`。
- 当前正式文件不得据本审查标为 whole-note `reviewed` 或 manuscript `pass`。

# Protection and result

- 本轮只创建 `BRIEF.md`、`SECTION_COVERAGE.md`、`WHOLE_NOTE_AUDIT.md`。
- 未创建 Writer Packet、Reader Card、staged draft、正文审查或 Integration Preview。
- 未修改正式 HGP 文件、`Notes/00-index.md`、`CANONICAL_KNOWLEDGE.md`、Papers、Translations 或任何 reader-visible 正文。
- 审查本身无 blocker。未来进入重构前，必须先解决 LP 数学范围、S007 ownership/placement、逻辑空间接口及关键来源登记四类高风险决定。

# Required next route

下一步唯一动作是由用户审查并批准上述 unit 边界与风险；批准后另开重构任务，从 legacy 范围的 mapping 与 Didactic Design 开始，同时冻结 revision 5 U01/U02，不直接进入 Writer。
