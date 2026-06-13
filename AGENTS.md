# AGENTS.md

本文件给后续协作者和 AI agent 使用，用来保持这个 Obsidian 知识库的写作风格、目录结构和推导标准一致。它也可以作为 magic state、容错量子计算和量子资源理论类 Obsidian 库的编写规范模板。

## 库定位

这是一个围绕 magic state、非 Clifford 资源、容错量子计算、magic state injection、magic state distillation、surface-code 工厂和资源估算展开的学习型知识库。

写作目标不是百科全书式堆材料，而是把一个概念讲到能用于后续推导、协议比较或资源估算：

- 先回答“这个概念为什么需要”：它解决了 Clifford 可高效经典模拟、容错非 Clifford 门、或资源开销中的什么问题。
- 再给出最小必要模型、态、线路、码参数或误差模型。
- 然后说明假设条件、适用范围、失败模式和数量级。
- 最后把它连接到已有笔记或下一层应用，例如 distillation protocol、gate synthesis、surface-code factory 或 fault-tolerant architecture。

## 目录规范

- `Notes/00-index.md` 是主路线图。新增主线主题时，同步更新这里。
- `Notes/01-量子纠错基础/` 放 stabilizer code、logical qubit、syndrome、threshold、distance、logical error rate 等基础容错概念。
- `Notes/02-Clifford与稳定子形式/` 放 Pauli group、Clifford group、Gottesman-Knill theorem、stabilizer tableau、Pauli measurement、Clifford frame 等。
- `Notes/03-Magic State基础/` 放 magic state 的定义、`|T\rangle`、`|H\rangle`、`|CCZ\rangle`、non-stabilizer resource、mana、robustness of magic、Wigner negativity、stabilizer rank 等。
- `Notes/04-Magic State Injection/` 放 state injection、gate teleportation、T gate injection、S correction、Pauli byproduct、measurement-based injection 等。
- `Notes/05-Magic State Distillation/` 放 Bravyi-Kitaev 15-to-1、Bravyi-Haah、triorthogonal code、MEK、CCZ factory、block code protocol、yield、threshold 和 output error scaling。
- `Notes/06-容错架构与资源估算/` 放 surface code、lattice surgery、factory layout、code distance selection、space-time volume、T-count、T-depth、factory scheduling、算法级资源估算等。
- `Notes/07-论文与协议笔记/` 放论文导读、协议对比和历史脉络。优先把可复用概念拆到对应主题目录，不要只堆论文摘要。
- 根目录只放跨主题的前置工具笔记，例如量子信息基础、张量积记号、Pauli 矩阵、Hadamard test、Solovay-Kitaev、统计误差传播等。
- `Code/` 放可独立打开的交互式演示或可视化页面，例如 distillation error scaling、T factory throughput、surface-code distance tradeoff。笔记中用相对 Markdown 链接引用，例如 `[点击打开 T 工厂资源估算器](<../../Code/T工厂资源估算器.html>)`。
- `Papers/` 放 PDF 原文。若要写论文笔记，优先在 `Notes/07-论文与协议笔记/` 或对应概念目录中建立笔记，不要把论文摘要直接堆在 PDF 旁边。

新增一级主题目录时使用编号前缀：`08-主题名`。编号表示学习路线顺序，不表示重要性。

## 命名规范

- 一篇笔记只讲一个核心概念、协议、公式、误差模型或资源估算方法。
- 文件名使用最常用术语，中文概念用中文名，标准英文术语保留英文，例如 `Magic State.md`、`T state.md`、`T gate injection.md`、`Bravyi-Kitaev 15-to-1.md`、`Triorthogonal Code.md`。
- 同一概念只保留一个主笔记，避免 `T态.md` 和 `T state.md` 产生重复内容；如果确实需要两个入口，明确一个是主解释，一个是别名/补充。
- 新建文件前先检查是否已有同义笔记。若只是补充推导、改正符号或加入例子，优先编辑已有笔记。
- Obsidian 双链大小写要尽量与目标文件名一致，避免跨平台或发布时出现断链。

## 笔记结构

多数概念笔记不需要重复写一级标题，文件名已经承担标题作用。正文推荐以下结构：

```md
一句话定义或动机：说明这个概念解决什么问题。

最小模型 / 核心公式 / 协议骨架：
$$
    ...
$$

---
### 关键推导或协议步骤

推导要能看出每一步用了什么假设；协议要写清输入态、测量、接受条件、输出态和错误阶数。

---
### 直觉图像

用自然语言解释为什么这个态是资源、为什么这个协议能压低错误、或者资源开销由什么量主导。

---
### 适用范围与失效模式

写清噪声模型、独立同分布假设、Clifford 操作是否视为理想、码距是否足够、相关错误会如何破坏结论。

---
### 例子 / 应用 / 与其它笔记的连接

链接到 [[相关概念]]，说明它在 gate injection、distillation factory、surface-code architecture 或算法资源估算中如何使用。
```

长笔记可以按“定义”“线路”“错误分析”“资源开销”“协议比较”“论文来源”等分节，但每节都应服务于同一个核心问题。不要把多个协议或多个资源度量强行塞进一篇笔记。

## 写作风格

- 使用中文解释为主，保留必要英文术语和英文缩写。
- 语气保持学习笔记风格：直接、具体、重公式来源和操作含义。
- 优先写“为什么需要 magic”“什么时候成立”和“开销由什么主导”，不要只罗列定义。
- 对重要结论给出推导、线路等价变换或数量级理由；如果暂时无法推导，明确标注“待补推导”。
- 可以使用引用块 `>` 写直觉、提醒、易错点或协议图像。
- 避免留下未整理的 AI 痕迹，例如“AI生成”“不想写了”。如果内容来自 AI 草稿，必须人工核对公式、条件、引用和术语后再合入。
- 不写营销式、科普式空话。每段最好回答一个具体问题，例如“为什么 T 门需要 magic state？”或“为什么 15-to-1 的输出错误是一阶项消失后三阶主导？”。

## 公式与符号规范

- 行内公式用 `$...$`，独立公式用 `$$ ... $$`。
- 线路、态矢量、投影算符、稳定子、逻辑算符和矩阵要写清楚基底或编码空间。
- 使用统一的常见记号：
  - Pauli 算符：`X`、`Y`、`Z`，必要时写作 `\hat{X}`、`\hat{Y}`、`\hat{Z}`。
  - Clifford 群：`\mathcal{C}_n`；Pauli 群：`\mathcal{P}_n`。
  - T 门：`T=\mathrm{diag}(1,e^{i\pi/4})`。
  - T magic state：`|T\rangle = T|+\rangle = (|0\rangle + e^{i\pi/4}|1\rangle)/\sqrt{2}`。
  - H-type magic state 可写为 `|H\rangle`，但必须在笔记中给出采用的 Bloch 方向或等价定义，避免与 Hadamard 门混淆。
  - 逻辑态和逻辑算符使用下标 `L`，例如 `|0_L\rangle`、`X_L`、`Z_L`。
  - 物理错误率写作 `p`，输出 magic-state 错误率写作 `p_{\mathrm{out}}`，逻辑错误率写作 `p_L`。
  - 协议输入数、输出数和接受概率写作 `n`、`k`、`P_{\mathrm{acc}}`；yield 可写作 `Y=k P_{\mathrm{acc}}/n`。
  - T-count、T-depth、factory throughput、space-time volume 分别写清单位或定义。
- 近似和假设必须写条件，例如“Clifford 操作和测量先视为理想”“输入错误独立且主要是一类 Pauli 错误”“忽略 correlated error”“surface-code 周期时间固定”。
- 推导中如果使用 twirling、postselection、code projection、Clifford frame update、Pauli frame update 或 decoding approximation，要说明丢掉或吸收了哪些项。
- 矩阵或线路等价前后要写明全局相位是否忽略、byproduct correction 如何处理、以及测量结果条件分支是什么。

## 双链与知识图谱

- 第一次出现可复用概念时使用 Obsidian 双链，例如 `[[Clifford group]]`、`[[Gottesman-Knill theorem]]`、`[[T state]]`、`[[T gate injection]]`、`[[Magic State Distillation]]`。
- 双链用于概念依赖，不要把每个普通名词都链接。
- 如果一篇笔记依赖另一个推导，直接写“详见 `[[相关笔记]]`”。
- 新笔记至少应连接到一个上游概念或一个下游应用，避免孤立笔记。
- 引入尚不存在但值得独立成文的概念时，可以先建短笔记；不要大量制造空链接。

## 内容标准

每篇笔记至少检查以下问题：

- 研究对象是什么：单 qubit magic state、多 qubit magic state、stabilizer code、distillation protocol、surface-code factory，还是算法级资源估算？
- Hilbert 空间、编码空间、逻辑 qubit 数、输入输出态和测量基是否说明清楚？
- Clifford 操作、非 Clifford 资源、Pauli byproduct 和 classical feedforward 是否区分清楚？
- 噪声模型是什么：state preparation error、Pauli error、depolarizing noise、measurement error、logical error、leakage、correlated error？
- 结论依赖哪些假设：理想 Clifford、独立噪声、低错误率展开、postselection、解码器近似或特定硬件周期？
- 主要数量级是什么：错误阶数、threshold、yield、T-count、T-depth、factory footprint、space-time volume？
- 结论如何映射到后续主题，例如 gate injection、distillation factory、fault-tolerant compilation、surface-code scheduling 或算法资源估算？

对于 magic state distillation 和工厂相关内容，额外检查：

- 明确输入 magic state 类型、输入错误模型、输出态类型和接受条件。
- 写清楚 protocol 的 `n-to-k` 结构、leading-order output error、接受概率和资源开销。
- 区分 distillation error、logical error、factory failure、decoder failure、SPAM error 和 correlated fault。
- 如果给出具体资源数，说明是否包含 Clifford synthesis、ancilla、measurement rounds、routing、idle errors 和 factory warm-up。
- 从 stabilizer check 或 triorthogonal matrix 推导协议性质时，写清 row/column 条件、transversal T 的作用和 syndrome postselection。

## 来源与可信度

- 可以参考 `Papers/` 中的 PDF、教材、论文或公开讲义，但笔记正文应重写为自己的推导和理解。
- 若写入具体 protocol 常数、阈值、资源估算、最新工厂设计、实验保真度或硬件参数，必须注明来源或保留可追溯引用。
- 对不确定的内容使用明确标记：`待核对：...`、`TODO：补引用`、`待补推导：...`。
- 不要把未经核查的 AI 解释当作最终内容，尤其是相位、归一化、byproduct correction、错误阶数、阈值、T-count 和常数因子。

## 交互演示与代码

- 只有当图像或交互能显著帮助理解时才新增 `Code/` 文件。
- HTML 演示应自包含，避免依赖外网资源。
- 文件名与对应笔记概念一致，例如 `T工厂资源估算器.html` 对应 `T工厂资源估算.md`。
- 在笔记中说明演示服务的问题，例如“比较不同 distillation level 的输出错误和 qubit-time 开销”，不要把代码细节写进概念笔记。

## 编辑流程

新增或修改笔记时按这个顺序工作：

1. 先查重：确认是否已有同义、上游或协议主笔记。
2. 放位置：选择合适目录，必要时新建编号主题目录。
3. 写核心：先写动机、模型、公式、协议步骤和直觉图像。
4. 连图谱：补充必要双链和索引入口。
5. 查公式：核对基底、相位、归一化、测量分支、错误阶数、资源单位和适用假设。
6. 清草稿：删除未核对的 AI 痕迹、重复段落和空泛解释。
7. 若是主线内容，更新 `Notes/00-index.md`。

## 最小完成标准

一篇合格新笔记应满足：

- 文件位置合理，文件名清楚。
- 开头能说明概念用途。
- 至少有一个核心公式、线路、协议骨架、误差模型或资源估算关系。
- 至少有一个与已有笔记的双链连接。
- 假设条件、噪声模型和适用范围没有缺失。
- 对 magic state 或 distillation 内容，必须写清输入、输出、接受/校正规则和错误阶数。
- 没有明显断链、未解释符号、未核对 AI 文本或与现有记号冲突。
