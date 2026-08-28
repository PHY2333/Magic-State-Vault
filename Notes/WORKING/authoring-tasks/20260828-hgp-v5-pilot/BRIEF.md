# 学习目标

- 可观察表现：区分超图乘积构造、HGP 码、输入 `A,B` 和输出 `H_X,H_Z`；说明 CSS 对易条件的必要性；以适当深度连接局部 Pauli 交换、偶数重叠、`H_XH_Z^T=0` 与三项箭头的零复合。
- 主线质量：辅助 Pauli 计算不能压过 HGP 主问题；正文使用自然中文，开头不出现 Künneth、ownership、前置清单或链接串。
- 仓库适配：staged manuscript 自足，同时保留与上游 CSS／Pauli canonical detail 的职责分工。

# 目标材料

- 正式目标：`Notes/07-Lifted-Product Code/Hypergraph product code.md`
- 单元范围：U01、U02；其中 U02 分为 P1（Pauli 到矩阵条件）与 P2（三项箭头）。
- 产物范围：完整 mapping、learner、design、design audit、packets、reader cards、drafts、双审查、manuscript verdict 与 read-only integration preview。

# 当前真实问题

怎样让第一次进入 HGP 的读者先抓住“从两张经典矩阵构造 CSS 码”这一对象关系，再以不过量的 Pauli 细节理解为什么输出必须对易，并最终把同一条件看成三项复形的零复合？

# 已有证据

- v4 pilot 已建立 faceted capabilities、Pauli/CSS premise inventory 和 U01/U02 staged drafts；这些任务产物只作为 Mapper、Learner Modeler 与 Architect 的历史证据，不授权 Writer 或 Blind Reader 读取。
- 用户明确规定：完整 Pauli `2×2` 矩阵计算不是本次出口能力；`unverified` 不自动触发 full derivation。
- 正式 HGP 笔记已有构造、CSS 对易、链复形、HGP blocks 及后续段落，可用于 mapping 和 integration preview 的重复检查。

# 非目标

- Kronecker blocks、`A/B` 尺寸、total degree、两路径抵消、homology、Künneth、qLDPC 参数和 LP 推广；
- 完整重证上游 Pauli/CSS 理论；
- 修改正式仓库。

# 可能需要用户决定

无。若只读 Integration Preview 发现必须改变已审查正文，则状态改为 `changes_required`，不得静默修改。
