这个索引用来记录本库的学习顺序和主笔记入口。它不替代具体笔记中的推导；新增主线笔记或移动目录时，应同步更新这里。

---
### 学习顺序

1. 线性代数与稳定子表示
   - [[二进制空间性质]]：$\mathbb F_2^n$、直和补空间、正交补和 CSS 码需要的线性代数记号。
   - [[逻辑基态的表示]]：从 $X$ 型稳定子、CSS 码到一般稳定子码的逻辑计算基态表示。
   - [[逻辑基态的二次相位]]：一般稳定子态在计算基展开中允许的一次相位和 $CZ$ 型二次相位。

2. 噪声通道与 magic-state 错误模型
   - [[CPTP映射与Kraus表示]]：量子信道、Kraus 表示、保迹条件和 postselection 分支的数学语言。
   - [[Clifford Twirling 与魔态错误模型]]：把 noisy $|T\rangle$ 归约为随机 $Z$ 错误模型，并区分 twirling 与独立性假设。

3. Magic-state injection
   - [[State injection]]：从 gate teleportation 推导 $U$-injection、in-place gadget、$T$ injection 和 byproduct correction。
   - [[MGT 的反向传播与稳定子码构造]]：区分物理、反向传播与稳定子码表示，并推导一般 commuting-Pauli 资源态的分支门和确定性前馈。

4. 横向 $T$ 与 triorthogonal distillation
   - [[汉明重量展开]]：把 XOR 和码字汉明重量写成整数多项式，是横向 $T$ 模 $8$ 相位分析的工具。
   - [[三正交码与横向逻辑T门]]：说明 triorthogonal 条件如何保证横向 $T$ 的非 Clifford 相位只落在逻辑一次项上。
   - [[Reed-Muller码]]：$[\![15,1,3]\!]$ Reed-Muller 码、横向 $T/T^\dagger$ 方向和 15-to-1 的 $35p^3$。
   - [[Distillation protocol]]：统一的 $G_1/G_0$ distillation 矩阵表示、syndrome、输出逻辑错误、接受概率和 yield。

5. Compact distillation factory
   - [[重复码上的逻辑T门]]：从 repetition-code logical $T$ 到 compact distillation matrix 的 $\alpha\mapsto\beta$ 变换。
   - [[Canonical distillation family]]：用 zeta/Möbius 反演构造 Jacinto 等人的 canonical compact family。
   - [[SAT搜索紧凑蒸馏工厂]]：把 support 选择、距离约束和 T-count 优化写成 SAT 搜索。

6. CCZ / qLDPC factory 延伸
   - [[Chain complex 与 cochain complex]]：chain/cochain complex 的 degree、cycle/cocycle、boundary/coboundary 和 homology/cohomology。
   - [[CSS码中的cochain complex]]：kernel、image、quotient、logical operator class 和 metacheck 的 CSS 码翻译。
   - [[Tensor product 对 direct sum 的分配律]]：解释普通 tensor product 如何把两个 direct sum 分解成双指标网格。
   - [[Cochain complex 的 tensor product]]：解释 graded vector space、total degree、coboundary map 和二项 complex 乘成三项/四项的来源。
   - [[Balanced tensor product 与 coinvariant quotient]]：固定右模、左模与中间 bimodule，说明 module tensor 与 anti-diagonal linear coinvariants 一般自然同构；作用保持选定 bases 时，它又是集合层 orbit quotient 的线性化。
   - [[Tricycle complex 的 balanced-product 构造]]：在 Menon 的有限 Abelian group-algebra 特例中构造 $R\to R^3\to R^3\to R$，并固定 regular representation 与二进制矩阵的方向约定。
   - [[Cup product 与 Leibniz rule]]：说明额外乘法 $\cup$ 和 Leibniz rule 如何让 cup product 在 cohomology 上良定义。
   - [[Preorientation 与 ordinary tensor product 上的 integrated Leibniz]]：说明 cup product 后为什么要用泛函读成 physical phase，解释 classical seed code 上的 in/out/free 局部读数，并证明 ordinary tensor product 继承 integrated Leibniz。
   - [[Balanced quotient 上的 inherited product 与 integrated Leibniz]]：解释 free-basis averaging、relative-translate operation 与 invariant integral 如何共同继承 integrated Leibniz。
   - [[Symmetric triple cup-product]]：解释 Menon 如何用 $\int_R$、symmetric integrated Leibniz、sector 和 preorientation 选择得到 physical $CCZ$ 三元组判据。
   - [[Menon 2025 Magic Tricycles]]：finite-block qLDPC tricycle codes、logical hypergraph magic state 和 single-shot $CCZ$ factory。

7. Lifted-product qLDPC 构造
   - [[Künneth 分解]]：构造 product homology 的自然比较映射，用域上的分裂与 contracting homotopy 证明直接和公式，并区分 PID 与一般环的 $\operatorname{Tor}$ 边界。
   - [[Hypergraph product code]]：从两个经典二项链复形推导 HGP 的 CSS 校验矩阵、长度与标准 $\Theta(\sqrt N)$ 距离基准，并调用 Künneth 分解计算维数。
   - [[Lifted product code]]：用群代数记录图 lift，在 $R$ 上取 HGP 型 balanced tensor product，并区分 QC、阿贝尔自由作用与非阿贝尔构造的适用条件。

---
### 当前目录归属

- `Notes/01-量子纠错基础/`：二进制空间、CSS 码和逻辑基态表示等前置结构。
- `Notes/02-Clifford与稳定子形式/`：稳定子态相位、Clifford/stabilizer 形式相关内容。
- `Notes/03-Magic State基础/`：量子通道、twirling 和 magic-state 错误模型。
- `Notes/04-Magic State Injection/`：state injection、gate teleportation 和 byproduct correction。
- `Notes/05-Magic State Distillation/`：triorthogonal code、Reed-Muller、distillation protocol、compact factory 和相关资源计数。
- `Notes/06-CCZ Distillation/`：CCZ/qLDPC factory、tricycle code、cochain complex、balanced product、metacheck 和 single-shot state preparation。
- `Notes/07-Lifted-Product Code/`：HGP 前置、lifted-product code、群 lift 与相关 qLDPC 构造。

容错架构与资源估算主题仍未建立；若后续建立 surface-code factory、lattice surgery、code distance selection、T-count/T-depth 和 spacetime volume，可另开编号目录并同步更新这里。

---
### 知识库维护

以下入口只用于维护正式知识笔记，不属于上述正式阅读顺序：

- [正文写作规范](WRITING_GUIDE.md)
- [复杂笔记任务流程](WORKFLOWS/note-writing.md)
- [上下文与规划契约](WORKFLOWS/planning-contract.md)
- [执行契约](WORKFLOWS/execution-contract.md)
- [只读 subagent 检查规则](WORKFLOWS/subagents.md)

`Notes/WORKING/` 是单次任务的临时交接区，不属于正式阅读索引；这里不列出任何单次任务目录。

---
### 后续应补主题

- [[Clifford group]]
- [[Gottesman-Knill theorem]]
- [[T state]]
- [[Magic State Distillation]]
- [[T gate injection]]
- [[Surface-code factory]]
