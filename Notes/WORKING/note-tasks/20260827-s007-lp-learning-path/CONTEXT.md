---
task_id: 20260827-s007-lp-learning-path
context_version: 1
base_commit: 29f63769803fe72bbf974268071801f7592c02e3
working_tree: "clean at task start; this task adds only TASK.md and CONTEXT.md"
generated_by: codex-sol
---

# 证据口径与任务边界

- 本文件只压缩已经实际读取的仓库内容和指定来源，不设计最终学习顺序，不决定三篇候选笔记的去留。
- 三篇目标笔记均按 legacy candidate material 审查；<code>CANONICAL_KNOWLEDGE.md</code> 的“主笔记／已整理”登记只表示当前 ownership，不等于通过本任务验收。
- <code>Translations/S007.full.zh-CN.md</code> 是下游验收来源，不是本次正文修改目标。
- 以下“足够／不足”只判断现有内容能否支持 S007 第 6 节的特定解释目标，不是对笔记整体质量的裁决。
- PDF 核验以所登记的 arXiv v1 本地文件为准；图 1、图 12 同时核对了译文中的原文截图。

# 已实际读取的文件

- <code>AGENTS.md</code>
  - 采用内容：复杂笔记任务的分流、Context → Plan → approval → execution 边界、正式笔记与系统区的区分、禁止本轮直接改正文。
- <code>Notes/WRITING_GUIDE.md</code>
  - 采用内容：正式知识笔记的正文判断、前置与重复边界、数学对象和来源的写作要求；本文件没有向其写入流程规则。
- <code>Notes/WORKFLOWS/note-writing.md</code>
  - 采用内容：复杂任务各阶段职责、Context Builder 的只读调查边界、用户批准前不得执行正文修改。
- <code>Notes/WORKFLOWS/planning-contract.md</code>
  - 采用内容：<code>TASK.md</code>、<code>CONTEXT.md</code> 的最小字段，<code>context_ready</code> 状态和 Planner 输入契约。
- <code>CANONICAL_KNOWLEDGE.md</code>
  - 采用内容：Künneth、HGP、LP 及其直接上游的现有 ownership、前置、边界和“不要重复”关系。
- <code>Notes/00-index.md</code>
  - 采用内容：第 7 条“Lifted-product qLDPC 构造”的现有三项顺序、目录归属，以及维护入口不属于正式阅读顺序的声明。
- <code>Notes/07-Lifted-Product Code/Künneth 分解.md</code>
  - 采用内容：全文；比较映射、域上分裂证明、自然性、二项复形的 HGP 逻辑空间、PID／一般环边界和环系数反例。
- <code>Notes/07-Lifted-Product Code/Hypergraph product code.md</code>
  - 采用内容：全文；二项链复形、两个物理比特扇区、CSS blocks、对易、长度／维数、qLDPC 与 HGP → LP。
- <code>Notes/07-Lifted-Product Code/Lifted product code.md</code>
  - 采用内容：全文；循环 lift、环表示、反对合、环值 LP blocks、二进制展开、balanced quotient、QC 特例、距离／一般群／解码边界。
- <code>Notes/01-量子纠错基础/二进制空间性质.md</code>
  - 采用内容：全文；Künneth 笔记实际引用的直和补空间事实，以及它与正交补的区别。
- <code>Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md</code>
  - 采用内容：全文；chain/cochain、cycle/boundary/homology、对偶和 CSS 翻译。
- <code>Notes/06-CCZ Distillation/CSS码中的cochain complex.md</code>
  - 采用内容：CSS 条件、stabilizer quotient、chain/cochain convention 和首次阅读对照表；中间与本任务无关的 4,2,2 例及 metacheck 展开未采用。
- <code>Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md</code>
  - 采用内容：全文；total degree、两个二项 complex 的三项乘积、block maps、两条路径抵消。
- <code>Notes/06-CCZ Distillation/Balanced tensor product 与 coinvariant quotient.md</code>
  - 采用内容：right/left module、balanced relation、反对角作用与 coinvariant quotient、basis orbit、balanced-product complex 和来源；与本任务无关的三因子细节未采用。
- <code>Translations/S007.full.zh-CN.md</code>
  - 采用内容：译文信息与术语表；图 1；第 2.2 节；第 3 节中架构协议、行／列分解和 ONEX 一维执行；第 4.2.1 节；第 6 节、图 12、表 3；参考文献 [6]、[19]、[26]、[42]、[50]。
- <code>Papers/SOURCES.md</code>
  - 采用内容：S007 登记；arXiv:2608.20164、arXiv v1、本地 PDF、已通读、当前全文译本、无主文献笔记。
- <code>Papers/RELATIONS.md</code>
  - 采用内容：当前唯一登记关系是 S003 ← S002；没有 S007 的主辅关系。
- <code>Papers/S007_2026_Liu_architecture_compilation_codesign.pdf</code>
  - 采用内容：PDF 页序／印刷页码 12–13；英文原文的式 (2)、图 12、四阶段说明、表 3、后续讨论。
- <code>Translations/Snapshots/S007/p002-01-fig-1-motivation.png</code>
  - 采用内容：图 1(a) 的 HGP／LP 码族关系和图 1(b) 的乘积坐标、两类数据扇区、X/Z 校验、水平／竖直相容组及行／列子问题。
- <code>Translations/Snapshots/S007/p012-01-fig-12-lp-execution.png</code>
  - 采用内容：图 12(a)–(d) 的 lift-level graph、示意性的 <code>x^2</code>/<code>l=6</code> 循环移位、相互作用位点对齐和对角停放转向。

# 当前目标文件

- 当前主线：
  - <code>Künneth 分解.md</code>：从 product homology 比较映射到域上同构，再延伸到 HGP 逻辑空间和一般环边界。
  - <code>Hypergraph product code.md</code>：从两个二项链复形推导 HGP 的两个物理扇区、CSS 校验矩阵、参数和 HGP → LP 接口。
  - <code>Lifted product code.md</code>：以环／群代数上的 balanced tensor product 表述 LP，并展开循环 lift、CSS 对易、长度、商、距离和一般群情形。
- 已有可复用事实（不构成保留决定）：
  - HGP 的两个中间项扇区、两个 product paths 和 CSS 对易。
  - <code>R_\ell=\mathbb F_2[x]/(x^\ell-1)</code>、<code>x^s\mapsto P^s</code> 与循环副本移位。
  - LP 保留 HGP 型 block skeleton、增加环系数／lift 标签并在二进制展开后得到实际校验矩阵。
  - Künneth 对域上 HGP 的逻辑空间与维数公式的作用，以及一般环时不能无条件套用该公式的边界。
- 已发现的问题：
  - 三篇都没有把主线锚定到 S007 第 6 节，也没有解释具体矩阵 (2)、图 12 或四阶段执行。
  - HGP 笔记与 S007 式 (1) 对第二个种子矩阵使用不同方向的 convention；两式可通过令笔记中的 <code>B=H_2^{\mathsf T}</code> 对齐，但现有正文没有给出这张转换表。
  - S007 第 6 节只展示一个 <code>3\times7</code> 环值矩阵 <code>A</code>；现有 LP 笔记以一般 <code>A,B</code> 成对构造，仓库来源没有明说具体实例的第二因子。
  - 现有 Künneth 深度远超过 S007 构造与执行本身显式使用的内容。

# Canonical ownership

| 概念或结论 | canonical 文件 | 当前任务的处理方式 |
|---|---|---|
| chain/cochain、homology quotient、对偶 convention | <code>Chain complex 与 cochain complex.md</code> | 只记录为上游；不在候选笔记重复定义 |
| CSS stabilizer quotient 与 chain/cochain 对照 | <code>CSS码中的cochain complex.md</code> | 用于核对 HGP 矩阵方向；不重写 CSS 基础 |
| total degree、product differential、两条路径抵消 | <code>Cochain complex 的 tensor product.md</code> | HGP/LP 可直接引用；不重复一般证明 |
| 域上 product homology、HGP 逻辑空间和一般环边界 | <code>Künneth 分解.md</code> | 作为 legacy ownership 记录；是否及多深进入学习路径由 Planner 决定 |
| balanced relation 与 anti-diagonal coinvariants | <code>Balanced tensor product 与 coinvariant quotient.md</code> | LP 可直接引用；不重复一般 module quotient 证明 |
| HGP blocks、两个物理扇区、N/K 与平方根距离边界 | <code>Hypergraph product code.md</code> | 记录现有覆盖和 S007 convention 差异；不预先决定改写方案 |
| 循环／群 lift、环值 LP blocks、二进制展开与长度压缩 | <code>Lifted product code.md</code> | 记录与 S007 的交集和缺口；不预先决定改写方案 |
| S007 的具体执行案例 | 当前无 canonical 知识笔记；来源是 S007 译文／PDF | 只作为下游验收事实登记，不在本轮创建 ownership |

# 上游与下游

## 上游可直接继承

- <code>Chain complex 与 cochain complex.md</code>：提供 chain/cochain 与 homology quotient 的语言。
- <code>CSS码中的cochain complex.md</code>：提供 CSS 矩阵与逻辑 quotient 的 convention 边界。
- <code>Cochain complex 的 tensor product.md</code>：提供两个二项 complex 形成三项 product complex，以及两条路径抵消。
- <code>Balanced tensor product 与 coinvariant quotient.md</code>：提供 LP 所用的 <code>\otimes_R</code>、right/left module 和 anti-diagonal quotient。
- <code>二进制空间性质.md</code>：只支撑 Künneth 域上证明中的补空间选择；不是 S007 的直接前置。

## 下游确实需要

- S007 §2.2 的式 (1)、四类 Tanner 边和“固定一个乘积坐标、只改变另一个坐标”的严格划分。
- S007 图 1(b) 和 §3.1 中“所有行子问题并行，再切换到所有列子问题”的物理含义。
- S007 §6 的 <code>l=45</code>、<code>[[2610,744,d\le16]]</code>、式 (2)、图 12(a)–(d) 和四阶段。
- 明确区分：
  - 外层 product direction；
  - lift 与 lift 之间的元层级图；
  - 单个 lift 内由多项式标签决定的循环移位；
  - 门对齐与行／列方向切换。
- Künneth 只在要推导逻辑空间／维数或讨论一般环同调时进入；S007 的构造、坐标分解和四阶段没有显式调用它。

# 不得重复

- chain/cochain、cycle、boundary、homology quotient 的一般定义已在 <code>Chain complex 与 cochain complex.md</code>。
- CSS stabilizer quotient 和 logical X/Z 的 convention 已在 <code>CSS码中的cochain complex.md</code>。
- ordinary product complex 的 total degree、Koszul sign 和两条路径抵消已在 <code>Cochain complex 的 tensor product.md</code>。
- right/left module、balanced relation、anti-diagonal quotient 的一般证明已在 <code>Balanced tensor product 与 coinvariant quotient.md</code>。
- 域上 Künneth 的完整 complement／contracting-homotopy 证明和一般环反例已在 <code>Künneth 分解.md</code>；若只解释 S007 构造，不应另行复述。
- S007 的执行事实应锚定译文／PDF，不把它们改写成无来源的通用 LP 定理。

# 来源锚点

| 事实 | 准确来源位置 |
|---|---|
| HGP CSS 矩阵与两类数据扇区 | <code>Translations/S007.full.zh-CN.md</code> §2.2，式 (1)，约第 190–213 行；S007 PDF p.3 |
| 四类边、固定一个坐标、无对角支撑 | 同上，式 (1) 后两组边关系，约第 201–215 行 |
| 图 1 的水平／竖直相容组及行／列子问题 | 译文图 1 与图注，约第 124–128 行；截图 <code>p002-01-fig-1-motivation.png</code> |
| 一维执行计划如何扩展为逐行／逐列阶段 | 译文 §3.1，约第 221–239 行；图 3(c) |
| 行／列分解的应用级作用 | 译文 §4.2.1，约第 300–308 行 |
| LP 具体码、<code>l=45</code> 与矩阵 <code>A</code> | 译文 §6，约第 437–449 行，式 (2)；PDF p.12 |
| 图 12 四个 panel | 译文约第 451–465 行；截图 <code>p012-01-fig-12-lp-execution.png</code>；PDF p.12 |
| 四阶段逐项文字说明 | 译文 §6，约第 457–467 行；PDF pp.12–13 |
| 具体执行时间分解 | 译文 §6 表 3，约第 469–478 行；PDF p.13 |
| S007 来源身份 | <code>Papers/SOURCES.md</code> 的 S007 登记 |
| S007 所称具体码的来源 | S007 参考文献 [6]：Madelyn Cain et al., arXiv:2603.28627；当前仓库未登记或保存该来源 |
| S007 所引一般 LP 来源 | S007 参考文献 [26]：Panteleev–Kalachev (2022)；候选笔记列有外部链接，当前 <code>Papers/SOURCES.md</code> 未登记本地副本 |

# S007 第 6 节依赖表

## 该节唯一显式给出的基矩阵

S007 式 (2) 为

$$
A=
\begin{pmatrix}
x^{29}&x^{21}&x^{31}&x^{15}&x^{37}&x^{25}&x^{27}\\
x^{13}&x^{25}&x^{19}&x^{26}&x^{11}&x^{18}&x^{29}\\
x^{31}&x^{2}&x^{27}&x^{32}&x^{41}&x^{41}&x^{18}
\end{pmatrix}.
$$

来源只把它称为 seed base matrix／式 (2)，没有在 §6 另写第二个环值矩阵。下表因此不把未写出的第二因子当作已知事实。

| 类别 | 第 6 节对象 | 来源中实际陈述的内容 | 所需前置概念 | 当前覆盖 | 足够性 | 准确来源 |
|---|---|---|---|---|---|---|
| 术语 | LP code | 该节用一个具体 LP 码展示 ONEX 从 HGP 向更一般乘积码推广 | HGP 与 LP 的共有 product skeleton；lift 数据 | <code>Lifted product code.md</code> 给出一般代数定义；<code>Hypergraph product code.md</code> 给出 skeleton | 数学一般性有覆盖；与 S007 案例未连接 | 译文 §6 首段；PDF p.12 |
| 参数 | lift size <code>l=45</code> | 具体码有 45 个提升副本；这里的 <code>l</code> 是实例参数 | lift fiber／副本指标；循环群坐标 | LP 笔记 §“循环 lift 的环表示”把环维数与副本数对应 | 基本足够；没有把 <code>l=45</code> 接到式 (2) 和图 12 | 译文 §6 首段；PDF p.12 |
| 参数 | <code>[[2610,744,d\le16]]</code> | 论文直接给出该量子码参数并称其为高码率存储码实例 | 量子码 <code>[[n,k,d]]</code> 记号 | CSS 上游和 HGP/LP 笔记解释一般 <code>N,K</code> | 能读参数；仓库来源不足以从式 (2) 独立重建 <code>2610,744</code> | 译文 §6 首段；PDF p.12；来源指向文献 [6] |
| 矩阵 | <code>A\in R_\ell^{3\times7}</code> 的 21 个单项式项 | 式 (2) 给出所有指数；每个非零条目是一个单项式 <code>x^k</code> | 环值基矩阵；行／列是外层 seed 节点，系数是内层 lift 标签 | LP 笔记覆盖一般 <code>A,B</code> 环值矩阵与单项式块 | 一般对象足够；未解释这 3 行、7 列如何对应 S007 的 data/X/Z lifts | 译文式 (2)；PDF p.12 |
| 缺失矩阵数据 | 第二个 LP 因子 | §6 只展示 <code>A</code>；没有显式写 <code>B</code>、<code>A^*</code> 或“自乘积”定义 | LP(A,B) 的具体 convention | LP 笔记要求一般 <code>A,B</code>；HGP 笔记也从两个因子开始 | 不足；不能把数值吻合自行升级成来源事实 | 译文 §6 与 PDF pp.12–13 均未给出；待查文献 [6] |
| 公式前置 | <code>R_\ell=\mathbb F_2[x]/(x^\ell-1)</code> | S007 §6 使用多项式和 <code>x^k</code>，但该节没有显式定义这个商环 | 循环 lift 的代数表示 | LP 笔记 §“循环 lift 的环表示”明确给出 | 对理解单项式足够；必须标明这是上游补充而非 S007 §6 原句 | LP 笔记约第 25–86 行；S007 图 12(b) |
| 公式前置 | <code>x^k</code> 是循环移位 | S007 明说每个多项式项在 <code>\ell</code> 个提升副本间诱导一次循环移位 | <code>x^\ell=1</code>；副本指标模 <code>\ell</code> | LP 笔记固定 <code>Pe_t=e_{t+1}</code>、<code>x^s\mapsto P^s</code> | 足够解释一种明确方向 convention；S007 图本身没有固定正负号 convention | 图 12(b) 图注；译文第 2 阶段；PDF p.12 |
| 图示 | 图 12(b) 的 <code>x^2</code>、<code>l=6</code> | panel 使用 6 个点演示界内移位和溢出回绕 | 模 <code>l</code> 指标、循环回绕 | LP 笔记有 <code>R_3</code> 的显式例子，机制相同 | 机制足够；现有笔记未提醒该 panel 是缩小示意，不是实际 <code>l=45</code> 全图 | 图 12(b) 原图；PDF p.12 |
| HGP 前置 | 两个乘积坐标与两个物理比特扇区 | S007 式 (1) 的物理列块是 <code>(j,l)\in[n_1]\times[n_2]</code> 与 <code>(i,m)\in[r_1]\times[r_2]</code> | Kronecker product、经典 bit/check 指标、CSS blocks | HGP 笔记覆盖两个扇区，但第二因子方向不同 | 数学结构有覆盖；缺少 <code>B=H_2^{\mathsf T}</code> 的显式记号转换 | 译文 §2.2 式 (1) 及其后指标定义 |
| HGP 前置 | 行／列方向为何独立 | 四类边各自固定一个乘积坐标，不存在同时改变两个坐标的对角边 | Tanner 图副本、Kronecker identity block | HGP 笔记能从 blocks 推出，但未写四类边或执行含义 | 对构造部分接近足够；对 ONEX 的一维子问题解释不足 | 译文 §2.2 四类边；图 1(b) |
| 图示／术语 | data lift、X check lift、Z check lift | 图 12(a) 把整组 lift 当作节点，形成 lift-level interaction graph | 单个 base-matrix node 展开成 <code>\ell</code> 个副本；CSS data/check 类型 | LP 笔记解释系数块；HGP 笔记解释 data/check sectors | 缺少“一个 lift 是调度单元”的执行层解释 | 图 12(a) 与第 1 阶段；PDF p.12 |
| 执行步骤 | 提升间重排 | 从 seed base matrix 出发，把每个 data/check lift 当作调度单元，经边着色得到 schedule，再用 ONEX 求元层级移动 | lift-level interaction graph、边着色、ONEX 一维执行输入 | 三篇候选均未覆盖；S007 §3 解释 ONEX 接收门 schedule | 不足 | 译文 §6 第 1 阶段；PDF p.12 |
| 执行步骤 | 提升内重排 | 在每个活跃 data lift 内，按相应多项式元素执行启发式二维循环移动；本例全为单项式，故可直接变成一维移位 | <code>x^k</code> 循环移位、活跃 lift、内／外层级区分 | LP 笔记覆盖单项式到 permutation block；不覆盖物理重排 | 代数含义够，执行含义不足 | 译文 §6 第 2 阶段；图 12(b)；PDF p.12 |
| 执行步骤 | 门执行 | 两级重排后，data/check qubits 在指定 interaction sites 对齐；相容组内门并行 | 中性原子 interaction site、相容组、门 schedule | 候选笔记不覆盖硬件；S007 §3.1 是直接来源 | 候选不足，来源本身足够 | 译文 §6 第 3 阶段；图 12(c)；§3.1 |
| 执行步骤 | 定向转移 | 一个乘积方向完成后转到另一方向，并重复前三阶段 | 外层 row/column product directions、二维布局方向 | HGP 笔记未连接布局；候选 LP 笔记无执行内容 | 不足 | 译文 §6 第 4 阶段；图 12(d)；PDF p.12 |
| 图示 | 对角停放、双层转移 | 本例用 diagonal parking 在水平、竖直 orientation 之间切换完整布局 | row/column orientation；to-/from-diagonal movements | 三篇候选均未覆盖 | 不足；只能按 S007 案例解释，不应推广为 LP 定义 | 图 12(d) 及第 4 阶段 |
| 结构关系 | 层级化处理 inter-lift 与 intra-lift，再结合 product-dimension decomposition | 论文把这三层关系作为一般 LP 可执行计划的依据 | HGP 外层 product；LP 内层 lift；ONEX 调度 | HGP、LP 两篇分别覆盖两种数学层；没有合并成执行语义 | 核心缺口 | 译文 §6 四阶段后的总结；PDF pp.12–13 |
| 性能结果 | 表 3 | ONEX/ONEX-Z 分解为 inter-lift、intra-lift、gate、transfer、shuttle；本例 ONEX-Z 总周期约缩短 10% | 四阶段分类和分区式布局 | 候选笔记不覆盖；S007 §5 是硬件前置 | 对学习目标不是数学前置，但可用于核对四类时间含义 | 译文 §6 表 3；PDF p.13 |

# 三篇现有笔记审查

## <code>Künneth 分解.md</code>

- 当前主线：
  - 构造 product homology 比较映射；
  - 用域上的补空间与 contracting homotopy 证明自然同构；
  - 特化到二项复形的 HGP degree-1 homology；
  - 讨论 PID、一般环、derived tensor、谱序列与 <code>R_2</code> 反例。
- 实际覆盖的数学对象：
  - cycle/boundary/homology、tensor-product chain complex、比较映射；
  - <code>ker A</code>、<code>coker A</code> 与 HGP 两个逻辑扇区；
  - <code>K=k_Ak_B^{T}+k_A^{T}k_B</code>；
  - <code>Tor</code>、K-flat、一般环 Künneth spectral sequence 和 extension。
- 与 S007 第 6 节直接相关的部分：
  - S007 第 6 节没有显式使用 Künneth；
  - 只有当任务要求推导 HGP 逻辑空间／维数，或判断一般环 LP 能否沿用域上维数公式时，二项复形特化和一般环边界才相关。
- 对当前目标过深或过宽的部分：
  - 域上完整自然性证明、contracting homotopy 的逐项构造；
  - PID 短正合列、一般环 derived tensor／谱序列；
  - <code>R_2</code> 比较映射既非单射也非满射的完整反例。
  - 这些内容在 S007 §2.2、§3、§4.2.1、§6、图 1、图 12 和 PDF pp.12–13 均未被调用。
- 缺失的必要连接：
  - 没有显式标出“HGP 构造、CSS 对易、行／列执行分解不依赖 Künneth”；
  - 没有把 S007 的 <code>k=744</code> 作为来源给定参数与“自行推导 K”区分。
- 与其他主笔记重复的内容：
  - product differential 和两条路径的基础在 <code>Cochain complex 的 tensor product.md</code>；
  - HGP degree-1 公式和 <code>K</code> 又在 <code>Hypergraph product code.md</code> 摘要性出现；
  - 一般 right/left module 与 balanced relation 属于 <code>Balanced tensor product 与 coinvariant quotient.md</code>。
- 尚未找到来源支持的内容：
  - 笔记列出 May 和 Stacks Project 作为一般定理来源，但这些外部来源未纳入本地 <code>Papers/SOURCES.md</code>，本任务未独立核验；
  - <code>R_2</code> 反例是笔记内推导，来源段没有为该具体例单列外部出处。
- 当前引用：
  - <code>Notes/00-index.md</code> 第 7 条；
  - <code>CANONICAL_KNOWLEDGE.md</code> 的 Künneth ownership，以及 cochain tensor/HGP/LP 的边界说明；
  - <code>Hypergraph product code.md</code> 开头与维数段；
  - <code>Lifted product code.md</code> 的一般环维数边界；
  - 没有发现其他正式主题笔记的实际 wikilink 入链。

## <code>Hypergraph product code.md</code>

- 当前主线：
  - 从 <code>A\in\mathbb F_2^{m_A\times n_A}</code>、<code>B\in\mathbb F_2^{m_B\times n_B}</code> 两个二项 chain complexes 构造三项 product complex；
  - 解释两个物理比特扇区；
  - 写出 <code>H_X,H_Z</code>、CSS 对易、<code>N,K</code>、qLDPC 与标准平方根距离；
  - 以“系数从 <code>\mathbb F_2</code> 换成 <code>R</code>”连接 LP。
- 实际覆盖的数学对象：
  - <code>C_1=\mathbb F_2^{n_A m_B}\oplus\mathbb F_2^{m_A n_B}</code>；
  - <code>H_X=[A\otimes I_{m_B}\mid I_{m_A}\otimes B]</code>；
  - <code>H_Z=[I_{n_A}\otimes B^{T}\mid A^{T}\otimes I_{n_B}]</code>；
  - 两条 product paths、长度、逻辑维数和 qLDPC 条件。
- 与 S007 第 6 节直接相关的部分：
  - 两种 physical sectors、HGP block skeleton 和 HGP → LP 的共同结构；
  - 这是理解 S007 §2.2 和 §6 外层 product directions 的直接候选材料。
- 对当前目标过深或过宽的部分：
  - Künneth 维数推导、一般 qLDPC family 条件和 <code>\Theta(\sqrt N)</code> 参数讨论不是理解图 12 四阶段的必要条件；
  - 距离基准和 family asymptotics 不参与 S007 的具体执行。
- 缺失的必要连接：
  - 没有把 Kronecker blocks 展开成 S007 §2.2 的四类边；
  - 没有说明“固定一个坐标、只改变另一个坐标、无对角支撑”为何产生独立一维 row/column subproblems；
  - 没有图 1 的数据／X check／Z check 布局或 ONEX 执行接口；
  - 没有明确给出与 S007 式 (1) 的 convention 转换：
    - 笔记取 <code>B\in\mathbb F_2^{m_B\times n_B}</code>；
    - S007 取 <code>H_2\in\mathbb F_2^{r_2\times n_2}</code>；
    - 令笔记中的 <code>B=H_2^{\mathsf T}</code>，即 <code>m_B=n_2,n_B=r_2</code>，两套 blocks 和 physical sectors 才逐项对应。
- 与其他主笔记重复的内容：
  - product complex 的一般定义和两路径抵消属于 <code>Cochain complex 的 tensor product.md</code>；
  - logical quotient convention 属于 <code>CSS码中的cochain complex.md</code>；
  - Künneth 逻辑空间公式在 <code>Künneth 分解.md</code> 有完整推导。
- 尚未找到来源支持的内容：
  - 笔记列有 Tillich–Zémor 和 Panteleev–Kalachev 外部链接；两者未作为本地来源登记，本任务未独立核验；
  - S007 可直接支持其自身 convention 下的式 (1)、四类边与执行分解，但不支持候选笔记全部距离／family claims。
- 当前引用：
  - <code>Notes/00-index.md</code> 第 7 条；
  - <code>CANONICAL_KNOWLEDGE.md</code> 的 HGP ownership，以及 Künneth/LP 的边界说明；
  - <code>Künneth 分解.md</code> 的 chain convention 与 degree-1 特化；
  - <code>Lifted product code.md</code> 的直接前置、ring blocks、chain convention 和相邻构造表；
  - 没有发现其他正式主题笔记的实际 wikilink 入链。

## <code>Lifted product code.md</code>

- 当前主线：
  - 以群代数／有限维代数记录 graph lift；
  - 以 <code>R</code> 上 balanced tensor product 保留 HGP 型三项 complex；
  - 经反对合和 regular representation 展开为二进制 CSS 码；
  - 延伸到 anti-diagonal quotient、QC 特例、距离、非阿贝尔构造、解码和相邻码族。
- 实际覆盖的数学对象：
  - <code>R_\ell=\mathbb F_2[x]/(x^\ell-1)</code>、循环移位矩阵 <code>P</code>、<code>x^s\mapsto P^s</code>；
  - 环值 <code>A,B</code>、反对合 <code>*</code>、ring-valued <code>\widehat H_X,\widehat H_Z</code>；
  - 二进制展开、<code>N=\ell(n_A m_B+m_A n_B)</code>；
  - balanced quotient、<code>B=[1+x]</code> 特例、一般群和 asymptotic/decoding 边界。
- 与 S007 第 6 节直接相关的部分：
  - lift size 是环的二进制维数／循环副本数；
  - 单项式 <code>x^k</code> 变成副本间循环 permutation；
  - LP 保留 HGP 的 product skeleton，但矩阵条目携带 lift shift 数据。
- 对当前目标过深或过宽的部分：
  - 反对合的完整块证明、一般环 blocks、anti-diagonal quotient 的长度压缩；
  - QC <code>B=[1+x]</code> 维数公式、距离标度、非阿贝尔 right/left module；
  - asymptotically good families、有限长度解码和相邻构造分类。
  - S007 §6 的执行解释没有调用这些完整一般性结果。
- 缺失的必要连接：
  - 没有 S007 的 <code>l=45</code>、具体 <code>3\times7</code> 矩阵或 <code>[[2610,744,d\le16]]</code>；
  - 没有说明图 12 的 data/X/Z check lift、inter-lift graph 或 edge coloring；
  - 没有“提升间重排—提升内重排—门执行—定向转移”四阶段；
  - 没有说明图 12(b) 的 <code>l=6,x^2</code> 只是循环移位示意；
  - 没有把一般 <code>A,B</code> convention 接到 S007 只写一个 <code>A</code> 的实例。
- 与其他主笔记重复的内容：
  - HGP blocks 和两个扇区属于 <code>Hypergraph product code.md</code>；
  - balanced relation、coinvariant quotient 和 right/left module 一般定义属于 <code>Balanced tensor product 与 coinvariant quotient.md</code>；
  - 一般环 Künneth 边界属于 <code>Künneth 分解.md</code>。
- 尚未找到来源支持的内容：
  - 来源段列出六项外部文献，但当前仓库只有候选笔记中的外部链接，没有对应本地登记；本任务未逐篇核验；
  - S007 只支持具体单项式实例及其执行，不支持该笔记全部一般群、距离和解码主张；
  - 该笔记没有为 S007 的具体码标注来源 [6]。
- 当前引用：
  - <code>Notes/00-index.md</code> 第 7 条；
  - <code>CANONICAL_KNOWLEDGE.md</code> 的 LP ownership，以及 Künneth/HGP 的边界说明；
  - <code>Hypergraph product code.md</code> 的开头和 HGP → LP 段；
  - <code>Künneth 分解.md</code> 的一般环边界与反例；
  - 没有发现其他正式主题笔记的实际 wikilink 入链。

# Künneth 的实际依赖

## S007 第 6 节是否显式调用 Künneth

- 否。对译文全文检索 <code>Künneth</code>、同调／homology、kernel、cokernel、逻辑空间和维数公式，没有在正文找到调用；“homological”只出现在参考文献 [51] 的题名。
- 第 6 节把 <code>[[2610,744,d\le16]]</code> 作为已给参数使用，没有推导 <code>744</code>。

## HGP 构造本身不需要 Künneth 的步骤

- 从两个经典 seed check matrices 写出两个二项 complexes。
- 形成三项 product complex 和两个 middle-degree physical sectors。
- 写出 <code>H_X,H_Z</code> 的 Kronecker blocks。
- 用两条 product paths 在 <code>\mathbb F_2</code> 中抵消证明 CSS commutation。
- 把 blocks 展开为四类 Tanner edges。
- 观察每条边固定一个 product coordinate，从而得到独立 row/column execution subproblems。

这些步骤只需要线性代数、CSS、tensor-product complex 和索引展开。

## HGP 逻辑空间或维数公式使用 Künneth 的步骤

- 把 product complex 的 degree-1 homology 分成

$$
\ker A\otimes\operatorname{coker}B
\oplus
\operatorname{coker}A\otimes\ker B.
$$

- 对两个扇区取维数，得到候选笔记 convention 下的 <code>K=k_Ak_B^T+k_A^Tk_B</code>。
- 若只用二进制校验矩阵秩公式 <code>K=N-\operatorname{rank}H_X-\operatorname{rank}H_Z</code>，可以计算具体 <code>K</code> 而不先证明 Künneth 分解；Künneth 提供的是结构分解与简洁通式。

## LP 构造与一般环边界

- 定义 <code>R_\ell</code>、把 <code>x^k</code> 展开成 permutation block、写环值 LP blocks、二进制展开并检查 CSS 对易，不需要先证明完整 Künneth。
- 对 S007 图 12 的 inter-/intra-lift execution、门对齐与 directional transfer，也不需要 Künneth。
- 若要从因子同调推导一般环 LP 的逻辑空间或统一维数公式，域上的直接和不再自动成立；候选 Künneth 笔记登记了 <code>Tor</code>、derived tensor、spectral sequence 和 extension 边界。
- 对非交换 group-algebra LP，还要先固定 right/left module 和 bimodule convention；Künneth 本身不能替代这些类型条件。

## Planner 必须决定但 Context Builder 不裁决的深度问题

- 是否把 Künneth 仅作为“逻辑维数的可选支线”，还是要求读者掌握二项复形的 degree-1 分解。
- 是否需要给出域上 Künneth 的证明，还是只引用 canonical 结果。
- 是否需要触及一般环的 <code>Tor</code>／谱序列；如果正文只承诺解释 S007 构造与执行，这些内容不构成前置事实。
- 是否要求从式 (2) 验证 <code>k=744</code>；若要求，当前缺失具体第二因子和来源 [6]，不能靠现有 S007 段落或模型记忆补出。

# 仓库影响

## 当前索引与 ownership

- <code>Notes/00-index.md</code> 第 7 条按以下顺序列出：
  1. <code>[[Künneth 分解]]</code>；
  2. <code>[[Hypergraph product code]]</code>；
  3. <code>[[Lifted product code]]</code>。
- 同一文件把 <code>Notes/07-Lifted-Product Code/</code> 登记为“HGP 前置、lifted-product code、群 lift 与相关 qLDPC 构造”。
- <code>CANONICAL_KNOWLEDGE.md</code> 分别为三者建立独立 ownership，状态均为“已整理”；文件开头还把该分支概括为“Künneth → HGP → cyclic/group lift → LP → balanced quotient 与 asymptotic qLDPC 参数”。

## 若删除三篇现有笔记会失效的 wikilink

| 被删候选 | 删除后仍存在的入链位置 |
|---|---|
| <code>Künneth 分解.md</code> | <code>Notes/00-index.md</code>；<code>CANONICAL_KNOWLEDGE.md</code> 的 cochain tensor、Künneth、HGP、LP 段；<code>Hypergraph product code.md</code>；<code>Lifted product code.md</code> |
| <code>Hypergraph product code.md</code> | <code>Notes/00-index.md</code>；<code>CANONICAL_KNOWLEDGE.md</code> 的 Künneth、HGP、LP 段；<code>Künneth 分解.md</code>；<code>Lifted product code.md</code> |
| <code>Lifted product code.md</code> | <code>Notes/00-index.md</code>；<code>CANONICAL_KNOWLEDGE.md</code> 的 Künneth、HGP、LP 段；<code>Künneth 分解.md</code>；<code>Hypergraph product code.md</code> |

- 若三篇同时删除，候选之间的互链随文件一起消失，但 <code>Notes/00-index.md</code> 和 <code>CANONICAL_KNOWLEDGE.md</code> 中的入链仍会失效。
- 当前任务目录的 <code>TASK.md</code>、<code>CONTEXT.md</code> 会继续以路径引用这些 legacy candidates；它们是任务记录，不是正式阅读入链。

## 其他正式笔记的实际引用

- 对全仓库 Markdown wikilink 的精确检索未发现 <code>Notes/01-</code> 至 <code>Notes/06-</code> 或其他正式主题笔记链接到这三个标题。
- 实际正式入链仅来自三篇候选彼此；此外是 <code>Notes/00-index.md</code> 与 agent-facing <code>CANONICAL_KNOWLEDGE.md</code>。
- <code>Lifted product code.md</code> 还向下链接 <code>Tricycle complex 的 balanced-product 构造</code> 作为相邻构造；这是候选的出链，不是该候选的入链。

## 后续结构变化必须同步的文件

- <code>Notes/00-index.md</code>：链接、描述、正式阅读顺序和目录归属。
- <code>CANONICAL_KNOWLEDGE.md</code>：三项 ownership、前置依赖、“不要重复”、状态以及开头的分支概述。
- 三篇候选中的相互 wikilink 与 section anchors。
- 若标题或 ownership 迁移影响上游引用，再核对：
  - <code>Cochain complex 的 tensor product.md</code>；
  - <code>CSS码中的cochain complex.md</code>；
  - <code>Balanced tensor product 与 coinvariant quotient.md</code>。
  当前这些正式上游没有反向 wikilink 到三篇候选，但 canonical 边界可能需要同步。
- 当前任务记录应保留为历史证据；不得把单次任务目录列入 <code>Notes/00-index.md</code>。

# 缺失与不确定

## 未找到

- S007 §6 没有显式给出具体 LP 码的第二个 seed factor，也没有说明式 (2) 是与自身、与 adjoint，还是与另一矩阵组成 product。
- 当前仓库没有 S007 参考文献 [6]（Cain et al., arXiv:2603.28627）的登记或本地文件；S007 把具体码来源归给它。
- 当前仓库没有把 S007 式 (2) 的 21 个指数逐项映射到完整 data/X/Z check lift graph 或完整 gate schedule 的材料。
- S007 图 12 和正文只说 <code>x^k</code> 诱导 cyclic shift，没有固定与 LP 笔记 <code>Pe_t=e_{t+1}</code> 完全相同的正负方向标号。
- <code>Papers/RELATIONS.md</code> 没有 S007 的主辅来源关系。

## 已核对的差异而非待猜事实

- HGP convention：
  - S007 使用 <code>H_2\in\mathbb F_2^{r_2\times n_2}</code>，physical sectors 为 <code>n_1n_2</code> 和 <code>r_1r_2</code>；
  - 候选 HGP 笔记使用反向第二 complex，physical sectors 为 <code>n_A m_B</code> 和 <code>m_A n_B</code>；
  - 令候选的 <code>B=H_2^{\mathsf T}</code> 可对齐。Planner 需要显式处理此转换，不能把符号同名后直接混用。
- 图 12(b) 明写 <code>x^2 shift, l=6</code>；具体实例正文明写 <code>l=45</code>。前者是可视化示意，不是把实例 lift size 改成 6。
- PDF p.12 的英文是 “For the example LP code (2)”；译文第 2 阶段显示“示例 LP 码 [2]”，容易被误读为参考文献 [2]。这里应按 PDF 判为对式 (2) 的引用；本任务不修改译文。
- <code>2610/45=58</code> 且 <code>58=7^2+3^2</code> 与一个 <code>3\times7</code> self-product 的 sector count 数值相容，但 S007 §6 未显式陈述该构造；本文件不把该算术观察写成 ownership 或构造事实。

## 需要 Planner 判断

- 三篇 legacy candidates 的保留、重写、拆分、合并、降为可选前置或删除。
- S007 convention 是成为面向该译文的主 convention，还是保留现有 chain convention 并增加清楚的转换。
- Künneth 在目标学习路径中的深度和是否为可选支线。
- 是否必须补入 Cain et al. [6] 后才能承诺“从式 (2) 完整重建具体码”；若不补来源，计划必须限制在 S007 已明确给出的构造层级和执行含义。
- 是否要单独处理译文中 “(2)” 被写成 “[2]” 的最小 workflow 链接／文字修复；翻译不属于本轮修改范围。

## 需要补充来源

- 首要：S007 参考文献 [6]，用于确认具体 <code>[[2610,744,d\le16]]</code> LP 码由式 (2) 形成时的第二因子、adjoint/convention 和参数来源。
- 若 Planner 要验证一般 LP 定义而非只引用现有 canonical：S007 参考文献 [26]／候选笔记所列 Panteleev–Kalachev (2022)。
- 若 Planner 要保留完整 Künneth 证明或一般环边界：候选笔记所列 May 与 Stacks Project 原文；本轮未外部核验。

# 给 Planner 的最小材料包

ChatGPT Pro 生成计划时必须实际读取以下有界集合；不需要读取整个仓库：

1. 任务与契约
   - <code>Notes/WORKING/note-tasks/20260827-s007-lp-learning-path/TASK.md</code>
   - <code>Notes/WORKING/note-tasks/20260827-s007-lp-learning-path/CONTEXT.md</code>
   - <code>Notes/WORKFLOWS/planning-contract.md</code>
   - <code>Notes/WORKFLOWS/note-writing.md</code>
   - <code>Notes/WRITING_GUIDE.md</code>
2. ownership 与正式阅读位置
   - <code>CANONICAL_KNOWLEDGE.md</code> 中 cochain tensor、Künneth、balanced tensor、HGP、LP 五个 ownership 段
   - <code>Notes/00-index.md</code> 中第 7 条和“当前目录归属”
3. 三篇 legacy candidates
   - <code>Notes/07-Lifted-Product Code/Künneth 分解.md</code>
   - <code>Notes/07-Lifted-Product Code/Hypergraph product code.md</code>
   - <code>Notes/07-Lifted-Product Code/Lifted product code.md</code>
4. 为判断重复边界所需的直接上游
   - <code>Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md</code>
   - <code>Notes/06-CCZ Distillation/Balanced tensor product 与 coinvariant quotient.md</code>
   - <code>Notes/06-CCZ Distillation/CSS码中的cochain complex.md</code> 的 convention／首次阅读对照部分
5. 下游验收源
   - <code>Translations/S007.full.zh-CN.md</code>：图 1、§2.2、§3.1、§4.2.1、§6、图 12、表 3
   - <code>Papers/S007_2026_Liu_architecture_compilation_codesign.pdf</code>：pp.12–13
   - <code>Papers/SOURCES.md</code>：S007 登记

如果 Planner 要承诺完整还原具体码而不只是解释 S007 已写出的层级和执行含义，还必须先请求 Context Builder 补入并核验 S007 参考文献 [6]；不得用模型记忆替代。

# 上下文结论

- 现有材料足够让 Planner 规划“如何使笔记服务于读懂 S007 §6”的结构审查，并能明确区分 HGP 外层 product、LP lift 数据和四阶段执行。
- 现有材料不足以无来源地完整重建式 (2) 对应的第二因子或独立推导 <code>k=744</code>；该缺口已定位到 S007 参考文献 [6]，不应在计划或正文中猜测。
- 结论：足够规划，但 Planner 必须把上述来源缺口作为明确边界；若计划承诺补齐具体码的完整代数构造，应先返回上下文补充请求。
