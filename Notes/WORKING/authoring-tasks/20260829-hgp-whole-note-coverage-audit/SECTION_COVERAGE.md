---
task_id: 20260829-hgp-whole-note-coverage-audit
status: complete
target_blob: 3251b0075281fdf4dc86fccb230ae44397732bad
section_count: 14
validated_sections: 3
legacy_audited_sections: 1
legacy_unreviewed_sections: 0
changes_required_sections: 10
---

# Coverage boundary

行号均指审计基线中的正式文件。当前共有 13 个现有标题；标题前的 U01 作为一个无标题 opening section 单独记录，因此 coverage 共 14 项。`validated` 只继承 revision 5 对 U01/U02 的 exact verdict；`legacy-audited` 仅表示本次 coverage 已完成，不等同 manuscript pass。

# S00 — 标题前 opening（U01；第 7–11 行）

- 当前读者入口能力：能接受二进制矩阵、物理量子比特和量子码的基本语言；不要求已知 HGP 构造。
- 该节实际假设的能力：能暂时把 CSS、X 型／Z 型校验和对易作为待解释的局部术语使用。
- 该节出口能力：区分超图乘积构造与所得 HGP 码，区分输入 (A,B) 与输出 (H_X,H_Z)，并指出输出必须解决的对易问题。
- 隐含前置：CSS 和泡利作用的完整结构尚未给出，但没有在本节被用于推导。
- 当前讲解模式：对象优先的 guided opening；类别、输入／输出、行支撑和主问题依次建立。
- 是否保持 HGP 主问题：是；末句明确提出“怎样由构造本身保证两类校验彼此对易”。
- 中文术语问题：未发现需要返修的中英混合；HGP、CSS 属 language profile 允许缩写。
- 数学或来源风险：本节 exact revision 5 已通过双审查；本任务没有发现新增风险。
- 与其它 section 的重复：与 S01 首段对共享列和行支撑有受控唤回，承担进入推导的必要衔接，不是 competing explanation。
- review_state：`validated`。

# S01 — 从局部交换到矩阵条件（第 13–89 行）

- 当前读者入口能力：已知 (H_X,H_Z) 是共享物理列的 X 型／Z 型校验矩阵，并知道当前问题是异型校验对易。
- 该节实际假设的能力：能阅读计算基、张量积符号和模 2 矩阵乘法；这些能力在使用处得到局部展开。
- 该节出口能力：能从同位反对易和异位对易得到 ((-1)^w)，把偶数重叠写成 (H_XH_Z^T=0)，并反驳“只要共享列就自动对易”。
- 隐含前置：完整泡利群与 stabilizer formalism 被有意省略；当前出口不依赖它们。
- 当前讲解模式：问题驱动的 compact derivation，带最小反例和可跳过的 (2\times2) 矩阵核验。
- 是否保持 HGP 主问题：是，但本节只完成“输出必须满足什么”的第一步，没有冒充具体 HGP 构造证明。
- 中文术语问题：术语统一；optional callout 结束后明确回到“每个共同位置贡献一个负号”。
- 数学或来源风险：Pauli、重叠奇偶和矩阵元 premises 已在 revision 5 source packet 与 audit 中闭合。
- 与其它 section 的重复：S05 再次出现零复合，是把一般条件应用到具体构造的 payoff，不应删除为重复。
- review_state：`validated`。

# S02 — 三个空间与两支映射（第 91–105 行）

- 当前读者入口能力：能使用 (H_XH_Z^T=0) 表示全部异型校验对易。
- 该节实际假设的能力：二进制向量空间、矩阵作为线性映射以及按模 2 相加的操作意义。
- 该节出口能力：能解释 (C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0) 的三个坐标空间、两支映射和零复合用途，并知道下一步是由 (A,B) 构造它们。
- 隐含前置：次数编号为什么选择为 2、1、0 尚未承担证明作用，留给具体构造阶段。
- 当前讲解模式：从逐行条件到整体映射的结构重述；对象闭合后才命名链复形。
- 是否保持 HGP 主问题：是；末句形成到 legacy 构造部分的明确承诺。
- 中文术语问题：未发现额外问题。
- 数学或来源风险：方向 (H_X=\partial_1,H_Z=\partial_2^T) 与仓库 chain convention 一致。
- 与其它 section 的重复：S03 末尾再次写三项链复形及 convention；未来需保留“通用语义→具体 convention”的作用差异，避免重复定义。
- review_state：`validated`。

# S03 — 从两张经典校验矩阵开始（第 107–155 行）

- 当前读者入口能力：已理解待构造的三空间、两映射和零复合，并认识 (A,B) 是两张经典输入。
- 该节实际假设的能力：能把 (m\times n) 矩阵直接看成 (\mathbb F_2^n\to\mathbb F_2^m) 的线性映射；已会二项链复形、次数、指标集合和 chain convention。
- 该节出口能力：得到 (A,B) 的尺寸、四组行列指标及 (H_X=\partial_1,H_Z=\partial_2^T) 的局部约定。
- 隐含前置：任意矩阵为什么能成为二项链复形；端点零映射为何自动满足链条件；变量／校验为什么分别放在 1／0 次；这一重写为什么有助于制造 U02 所需的三项复形。
- 当前讲解模式：notation-first formal setup；尺寸、复形、指标和 convention 连续罗列。
- 是否保持 HGP 主问题：部分保持；对象仍是 (A,B)，但从 U02 末句到本节结束尚未说明“为什么改写成二项复形”，主问题暂时退场。
- 中文术语问题：`degree`、`chain convention` 中英混用；“本库固定”带维护者视角；“经典变量／经典校验”与后文 S007 标签尚未统一层级。
- 数学或来源风险：次数方向和矩阵尺寸正确；风险主要是 motivation／premise closure。两篇 HGP 主来源尚未在 Papers 中稳定登记版本。
- 与其它 section 的重复：第 143–155 行与 S02 的三项箭头及映射语义近邻重复，但承担具体符号 convention；未来应只固定一次。
- review_state：`changes-required`。

# S04 — 乘积中间项与物理比特扇区（第 157–185 行）

- 当前读者入口能力：已接受两份二项复形及其行列次数标签。
- 该节实际假设的能力：已会链复形的张量积、总次数、张量积对直和的分配、维数相乘以及不同总次数分量的直和。
- 该节出口能力：列出 (C_2,C_1,C_0) 的具体空间，识别 (C_1) 的两个物理量子比特扇区和四类乘积指标。
- 隐含前置：总次数是次数相加的定义；为什么 (2=1+1)、(1=1+0=0+1)、(0=0+0) 逐项产生三个空间；为什么 (C_1) 被解释为物理坐标；特征 2 对后续乘积微分符号的作用。
- 当前讲解模式：公式先行的 totalization 总览，加一张代数标签／CSS 角色对照表。
- 是否保持 HGP 主问题：部分保持；结尾把两个扇区连接到后续 Tanner 边，但没有在公式前说明总复形如何推进“构造两支映射”。
- 中文术语问题：`Total degree`、`chain group` 式混用；“物理比特／物理量子比特”不统一；表中 `Z-校验标签`、`X-校验标签` 与正文的“Z 型／X 型校验”不一致。
- 数学或来源风险：三个链群和两个物理扇区计算正确；当前只有第 185 行事后解释 (1=1+0=0+1)，不足以承担完整 derivation。仓库 tensor-product owner 已有稳定推导。
- 与其它 section 的重复：对 S02 三个空间作具体化是必要重组；但必须明确“代数 totalization”和“CSS 物理解释”是两个出口，避免在一张表中同时首次引入。
- review_state：`changes-required`。

# S05 — HGP 校验矩阵与对易（第 187–250 行）

- 当前读者入口能力：能识别三个链群、两个 (C_1) 扇区及 (H_X/H_Z) 的方向约定。
- 该节实际假设的能力：张量积微分、Kronecker 块的定义域／陪域、mixed-product identity、特征 2 下两份相同项抵消。
- 该节出口能力：写出 (H_X,H_Z) 四个块，理解两条复合路径都给出 (A\otimes B)，并由此证明具体 HGP 输出满足 CSS 对易。
- 隐含前置：四个块分别从哪个输入扇区映向哪组校验；恒等因子固定哪个坐标；乘积边界公式如何由两份种子微分产生。
- 当前讲解模式：构造公式 + 两路径 proof map + 回到 U01 主问题的结论。
- 是否保持 HGP 主问题：是；这是 legacy 中最清楚的 question/result/return 闭环。
- 中文术语问题：`product paths`、`chain convention`、`HGP blocks` 中英混用；可保留符号但需统一中文叙述层。
- 数学或来源风险：四块尺寸、转置、块顺序和 (A\otimes B+A\otimes B=0) 均通过局部计算；解释风险在于 mixed-product premise 和四块语义没有在本节闭合。
- 与其它 section 的重复：S01/S02 给一般对易条件，本节给具体构造证明，功能不同；S07 才逐块解释边，但被 S007 记号接管，造成解释延迟。
- review_state：`changes-required`。

# S06 — 与 S007 式 (1) 的记号转换（第 252–315 行）

- 当前读者入口能力：已掌握一般 (A,B) convention 与 HGP blocks。
- 该节实际假设的能力：知道 S007 的阅读目的、(H_1,H_2) 尺寸、相反的第二因子方向，以及 (q^A,q^B,x,z) 的来源角色。
- 该节出口能力：能在本库 (A,B) 与 S007 (H_1,H_2) 两套矩阵、尺寸和节点标签之间转换。
- 隐含前置：为什么一般 HGP reference 此时必须切换到 S007；论文式 (1) 与图 1 的应用范围；转置怎样交换第二因子的变量／校验角色。
- 当前讲解模式：source-specific lookup crosswalk。
- 是否保持 HGP 主问题：否；对易已在 S05 回收，本节没有建立新的 HGP phase question，而是进入论文记号任务。
- 中文术语问题：`HGP blocks`、`chain 标签／方向` 等混用；S007 首次出现时没有先建立其作为来源对照的角色。
- 数学或来源风险：(A=H_1,B=H_2^T) 及尺寸转换由 S007 arXiv v1 本地 PDF／译文核实；水平／竖直和 (q^A,q^B,x,z) 必须保持 source-specific。
- 与其它 section 的重复：完整重抄两张块矩阵；与现有 `S007 中 LP 码的分层执行.md` 的来源接口重叠。若成为 optional，S07/S08 必须先脱离其记号，否则 skip test 失败。
- review_state：`changes-required`。

# S07 — 四类 Tanner 边（第 317–375 行）

- 当前读者入口能力：已完成 S007 convention crosswalk，并能识别 (H_1,H_2,q^A,q^B,x,z)。
- 该节实际假设的能力：能把 Kronecker 元素展开成 Tanner 邻接关系；能区分数据节点、校验节点和具体综合征提取中的辅助量子比特。
- 该节出口能力：由 (H_1,H_2) 的非零元枚举四类边，并知道每块中的恒等矩阵固定哪个乘积坐标。
- 隐含前置：(\mathcal H_X,\mathcal H_Z) 与此前 (H_X,H_Z) 的同一性；抽象校验标签何时可以实例化为校验辅助量子比特；Tanner 图边和硬件门边的层级区别。
- 当前讲解模式：逐块 worked expansion。
- 是否保持 HGP 主问题：保持 HGP 结构问题，但依赖论文专用记号，读者无法在一般 (A,B) 语境下直接使用这一出口。
- 中文术语问题：`Kronecker blocks`、`Tanner`、数据量子比特／校验辅助量子比特的对象层级混杂；突然改用 (\mathcal H_X,\mathcal H_Z)。
- 数学或来源风险：四类边逐项计算正确，并与 S007 式 (1) 相符；把一般 Tanner check node 直接称为辅助量子比特属于来源／实现范围升级。
- 与其它 section 的重复：是 S05 四块的必要语义展开，不应删除；但其一般部分应先在 (A,B) 记号下闭合，S007 标签只能作 adapter。
- review_state：`changes-required`。

# S08 — 行与列的乘积方向（第 377–392 行）

- 当前读者入口能力：已掌握四类 Tanner 边及其固定／变化坐标。
- 该节实际假设的能力：Tanner 图副本、节点互斥、并行处理的相容性，以及 S007 图 1(b) 的水平／竖直布局含义。
- 该节出口能力：说明每条边只改变一个因子坐标、同一方向分解为种子 Tanner 图副本，并排除同时改变两个坐标的对角边。
- 隐含前置：“相容副本”的判据；抽象图分解到实际门调度之间仍需的 syndrome-extraction 与硬件假设。
- 当前讲解模式：由四类边综合出几何／图结构，再附加 S007 执行协议解释。
- 是否保持 HGP 主问题：一般固定／变化坐标结论保持 HGP canonical 主线；最后一句转入 S007 调度，改变对象层级。
- 中文术语问题：“相容”未定义；“一维分解”的结构含义与执行含义同段出现，容易被读成同一 claim。
- 数学或来源风险：固定坐标、无对角边的计算正确；“水平／竖直”是 S007 图布局标签，不是 HGP 内禀命名；执行顺序只由 paper-guide source 支撑。
- 与其它 section 的重复：对 S07 四类边作有目的的综合；S007 协议部分与现有 paper-guide 重复。
- review_state：`changes-required`。

# S09 — 长度、秩与可选逻辑空间分解（第 394–447 行）

- 当前读者入口能力：能数两个物理扇区，并已知 (H_X,H_Z) 的行数与块结构。
- 该节实际假设的能力：CSS rank 公式、核／余核、同调、Künneth 同构和有限维对偶。
- 该节出口能力：由扇区得到 (N)，用矩阵秩计算有限实例的 (K)，并在选择高级支线时得到两个 logical-support 同调扇区和闭式维数公式。
- 隐含前置：为什么 (K=N-\operatorname{rank}H_X-\operatorname{rank}H_Z)；(H_1) 在当前 convention 中对应 logical Z support quotient 而不是编码 Hilbert space；余核与 Künneth 的适用条件。
- 当前讲解模式：基础参数 lookup，随后通过 upstream link 引入可选高阶分解。
- 是否保持 HGP 主问题：已从对易主问题转入 HGP 参数 phase；Künneth 的引入动机本身自然，因为先出现“进一步分解逻辑空间”的需求。
- 中文术语问题：`product sectors`、`kernel/cokernel`、`logical` 中英混用；“逻辑空间”可能混淆 logical-support quotient 与量子编码子空间。
- 数学或来源风险：(N)、rank 公式和 Künneth 维数公式正确；第 257 行的 S007 种子矩阵 (H_1) 与第 416 行的一阶同调 (H_1(\mathcal A\otimes\mathcal B)) 形成显著记号碰撞。LP/sqrt 后文又依赖本节定义的 (k_A,k_A^T)，使“可选”支线实际不可跳过。
- 与其它 section 的重复：Künneth owner 已有完整推导；当前 reference 的 result/bridge 可保留，但不应重做 owner proof。S11 使用其符号，必须解除 hidden downstream dependency。
- review_state：`changes-required`。

# S10 — qLDPC 条件（第 449–451 行）

- 当前读者入口能力：已知 HGP 的四个 Kronecker 块及行列扇区。
- 该节实际假设的能力：知道码族、行重／列重统一上界和 qLDPC 定义，并能自行追踪块拼接后的每类行列重量。
- 该节出口能力：识别一个充分条件：两份种子的行重和列重均一致有界时，HGP 输出形成 qLDPC 码族。
- 隐含前置：统一上界相对于家族参数；每个输出行重是两份种子局部重量之和、每个输出列度也同样有界。
- 当前讲解模式：高度压缩的条件—结论 reminder。
- 是否保持 HGP 主问题：保持“构造额外保证什么”的参数主线，但不再属于 CSS 对易 phase。
- 中文术语问题：qLDPC 属允许缩写；“码长”需要区分种子规模和量子码长的渐近族语境。
- 数学或来源风险：充分条件正确，Tillich–Zémor 与 Panteleev–Kalachev 原始文献也给出相应稀疏性传播；当前本地说明未展示最小权重计算，且两篇来源尚未在 Papers 稳定登记。
- 与其它 section 的重复：S11 末尾再次回收 qLDPC 与常数率，是 parameter payoff，不是无效重复。
- review_state：`changes-required`。

# S11 — 标准的 \(\sqrt N\) 参数基准（第 453–495 行）

- 当前读者入口能力：已知 (N,K)、qLDPC 条件和基本经典码参数。
- 该节实际假设的能力：四个经典／转置码距离、零核距离约定、HGP 距离定理、渐近记号、同调扇区和非平凡 logical representative。
- 该节出口能力：知道 (d=\Theta(\sqrt N)) 不是任意 HGP 的结论，并能识别 (B=A^T)、满行秩、线性经典距离和 LDPC 稀疏性给出的标准常数率平方根距离基准。
- 隐含前置：(d_A,d_A^T,d_B,d_B^T) 的对象定义；距离下界的精确来源和零逻辑比特边界；为什么存在重量 1 的非零余核代表元，以及它和最小经典码字怎样给出重量 (d_A) 的非平凡 logical class。
- 当前讲解模式：一般距离限定 + 条件化 worked benchmark + HGP→LP 动机。
- 是否保持 HGP 主问题：保持参数与下游动机，但能力负荷显著高于相邻 qLDPC 段；完整证明开始压过 reference 主线。
- 中文术语问题：`kernel/cokernel`、`logical` 中英混用；四个距离首次出现时缺少中文对象标签。
- 数学或来源风险：(N=n^2+m^2,K=k^2) 和标准下界计算正确；精确等号 (d=d_A) 的上界桥梁过短。官方 arXiv 主来源支持该特例，但仓库没有稳定登记其版本／核对章节。
- 与其它 section 的重复：使用 S09 仅在“可选”Künneth 分支定义的 (k_A,k_A^T) 与余核概念，导致 optional skip test 失败；末句与 S12 的 LP 过渡重复。
- review_state：`changes-required`。

# S12 — 从 HGP 到 LP（第 497–526 行）

- 当前读者入口能力：已掌握 HGP 三项复形、两个物理扇区、四块和平方根参数基准。
- 该节实际假设的能力：有限维代数、环值矩阵、二进制块表示、置换表示、反对合、左右模、balanced tensor product 和 lift 坐标。
- 该节出口能力：当前文本试图让读者列出 LP 保留的 HGP 骨架以及新增的 lift 数据，并把问题交给下一篇 LP note。
- 隐含前置：什么是 lift；哪类环元素对应单一置换；一般元素怎样展开；平衡张量积和自由群作用的适用范围；交换系数或左右模条件为什么仍保证两路径抵消。
- 当前讲解模式：比较表 + downstream bridge。
- 是否保持 HGP 主问题：合理离开 HGP 并建立下游接口，但表格同时引入过多未闭合对象，不能作为读者已获得可操作 LP 能力的证据。
- 中文术语问题：`lift`、`permutation`、`ordinary/balanced tensor product`、`product`、`cyclic-shift` 密集中英混用。
- 数学或来源风险：高。单项式／群基元素可展开为一个置换；多项式或一般群代数元素是置换块的二进制和；一般有限维代数元素甚至不必是置换。两路径抵消还需要系数交叉对易与转置相容表示，非阿贝尔情形需要右／左模侧别。当前表述把这些层次压成了无条件的一般 LP 叙述。
- 与其它 section 的重复：再次抄写三项复形和 (H_X/H_Z) convention；与 `Lifted product code.md` 的一般定义和 S007 paper-guide 的 cyclic-shift 特例均重叠。
- review_state：`changes-required`。

# S13 — 来源（第 528–532 行）

- 当前读者入口能力：无需新增数学能力。
- 该节实际假设的能力：能把正文 claims 对应到 HGP、LP 和 S007 三组来源。
- 该节出口能力：获得三个主要 provenance 入口。
- 隐含前置：列表没有逐 claim 标出核对章节；两个外部 arXiv 来源没有本地稳定 ID、版本和阅读状态。
- 当前讲解模式：bibliography／provenance。
- 是否保持 HGP 主问题：不适用；它是 reference 的来源区。
- 中文术语问题：书目信息本身无重大问题；正文中使用的 `chain convention` 等不应由来源列表承担解释。
- 数学或来源风险：S007 arXiv v1 已在仓库登记并有 PDF／译本；Tillich–Zémor arXiv:0903.0566v2 与 Panteleev–Kalachev arXiv:2012.04068v2 可由官方页面核对，但尚未进入仓库稳定来源登记。
- 与其它 section 的重复：正常书目回收；未来应把关键定理和 source-specific claims 的锚点分配到对应 unit，而不是只依赖尾部总表。
- review_state：`legacy-audited`。

# Coverage summary

| review state | sections | 含义 |
|---|---|---|
| `validated` | S00–S02 | 仅 revision 5 U01/U02 exact scope |
| `legacy-audited` | S13 | coverage 完成；不等于 manuscript pass |
| `legacy-unreviewed` | 无 | 所有 section 均获得本轮 coverage |
| `changes-required` | S03–S12 | 未来 whole-note 重构必须返回 mapping／learner／didactic design；不能直接编译 Writer Packet |
