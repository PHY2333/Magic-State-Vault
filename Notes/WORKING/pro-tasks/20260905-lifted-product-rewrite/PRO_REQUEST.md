---
task_id: 20260905-lifted-product-rewrite
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh
binding_id: dc14ebb688434609834c42283bbd8a97
target_files:
  - Notes/07-Lifted-Product Code/Lifted product code.md
---

# 用户目标与实际反馈

用户：“Notes/07-Lifted-Product Code/Lifted product code我觉得写的不算很好，按照流程交给pro重写一份”。没有更具体的读者反馈；请实际读旧文，自行完成教学诊断与规划，直接交付完整的新正文，不只润色或追加问答。

目标读者应能从已懂的 HGP 出发，实际解释 lift 怎样改写矩阵条目、怎样得到 LP 的二进制 CSS 校验、为什么对易，以及为什么它不同于先展开再做 ordinary HGP；能读懂一个可计算的循环实例，并分清构造、稀疏性、长度压缩、维数、距离与解码各需要什么条件。

# Reader assumptions

可以直接依赖：二进制线性代数、经典校验矩阵与 Tanner 图、CSS 的对易与秩计数、HGP 的两个物理扇区和四个 blocks、链复形的边界复合为零及 homology 的基本含义。调用这些结果时仍需交代本篇采用的对象与方向。

不能直接依赖：已熟悉群代数、循环多项式商环、正则表示、反对合、balanced tensor product 的当前作用、非阿贝尔左右模或一般环 Künneth。可以使用这些工具，但在首次承重使用前给出当前所需的最短充分解释。仓库存在前置笔记不等于读者已经全部掌握；不重证上游整套理论。

# 必须读取

实际读取 Browser 固定 commit 中以下材料；相邻笔记只需读取指定内容，目标全文必须读完。

- `Notes/WORKING/pro-tasks/20260905-lifted-product-rewrite/TASK.md`
- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `Notes/07-Lifted-Product Code/Lifted product code.md`：全文。
- `CANONICAL_KNOWLEDGE.md`：HGP、LP、balanced tensor product、Künneth 与 S007 相关条目。
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`：构造、chain/cochain convention、两扇区与四个 blocks。
- `Notes/06-CCZ Distillation/Balanced tensor product 与 coinvariant quotient.md`：balanced relation、左右作用、coinvariant 与自由作用边界。
- `Notes/07-Lifted-Product Code/Künneth 分解.md`：域上 HGP 与一般系数环边界。
- `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md`：文件职责、循环移位约定与 S007 信息范围。

# 来源与数学边界

旧文来源链接是待实际核查的来源入口，不等于本请求已经核验它们。核心构造请核对原论文的定义和条件：Panteleev–Kalachev, *Quantum LDPC Codes with Almost Linear Minimum Distance*, https://arxiv.org/abs/2012.04068；自由群商对应请核对 Breuckmann–Eberhardt, *Balanced Product Quantum Codes*, https://arxiv.org/abs/2012.09271。可读取对应原文版本，并在最终来源中指明适用的定义、章节或命题。

若保留非阿贝尔／渐近良好子族或解码结论，必须实际核对相应原始来源及其条件： https://arxiv.org/abs/2111.03654 、 https://arxiv.org/abs/1904.02703 、 https://arxiv.org/abs/2206.07571 、 https://arxiv.org/abs/2411.04464 。不是必须把这些结果全部展开成独立长节；可以把非核心内容压缩为有准确来源的边界说明，避免接管构造主线。不得声称这些外部论文已经登记为本地文献。

如保留 S007 具体事实，核对 `Translations/S007.full.zh-CN.md` 第 6 节；其来源登记为 S007 / arXiv:2608.20164 / v1。本篇只作去往独立应用笔记的短接口，不展开硬件教程。S007 展示一个 3×7 单项式 seed matrix，不能补猜未展示的第二因子、完整 sector 映射或由此推出完整参数。

请特别核查以下范围；这些是检查点，不是要求照抄的教学结构或已裁定的冲突：

- 区分一般忠实的 ell×ell 块表示与自由 R-模的底层二进制坐标化。前者的维数未必等于 dim_F2 R；不要把任意忠实表示不加条件地当作正则表示。主线可先固定循环环／群代数正则表示，再准确说明一般化范围。
- 保持已用 convention：循环移位 `Pe_t=e_{t+1 mod ell}`、列是变量、行是校验；共轭转置与二进制转置的关系应能追踪到逆移位。
- 核对环值 Kronecker blocks 的尺寸、映射方向、交叉对易、特征 2 消去，以及展开后的 CSS 对易。不要把环矩阵的 Kronecker 积与模上的 balanced tensor product 混作未解释的同一操作。
- 解释先展开再 ordinary HGP 与在系数环上乘积再展开的差别；自由正则群作用下才有精确的群坐标与长度压缩计数。balanced relation 本身不要求自由作用。
- 一般 K 使用二进制秩；若保留 B=[1+x] 的特殊公式，核对其充分条件、参数限制与理由，不只说“论文给出”。不能无条件套用域上 Künneth。
- LP 对易、LDPC 稀疏、良好距离、可证明解码是不同层次。任意 lift 不自动给出好参数，具体码族的定理不能泛化为 LP 定义。
- 非阿贝尔情形必须准确区分左右作用及其线性／模性质，不能仅在交换环公式中加入星号。

# Ownership 与写作权限

唯一 allowlist 是 `Notes/07-Lifted-Product Code/Lifted product code.md`。在原文件职责内可全篇重构顺序、替换解释、选取贯穿例子、压缩支线并修正经来源核查的数学内容；无需沿用旧小节次序。不要把 Codex 的检查点列表变成正式正文。

该文件继续承担 LP 的循环 lift、环值 blocks、二进制展开、自由反对角商及参数／应用边界。HGP 全部推导、一般 balanced tensor 理论、Künneth 完整证明和 S007 硬件应用各由既有笔记承担；给出必要局部桥梁后链接，并说明采用什么结果、用于哪一步。

已有其他文件引用以下两个标题，请原样保留为有实际对应内容的标题：`循环 lift 的环表示`、`反对合与二进制转置`。其他标题可重组。

禁止写入 allowlist 外路径；不新增前置笔记，不修改索引或 canonical 文件。若确实必须删除、移动、拆分、合并、重命名正式文件或改变 ownership，返回 DECISION_REQUIRED，不擅自实施。无法读取必需上下文或来源时如实按协议返回，禁止补猜。

# 写作与完成标准

自然、连续的中文教材语体；开头建立读者可理解的对象、问题或整体图景，不列仓库依赖。核心构造要有足够推导和可计算实例；每个新工具在需要它时出现，关键公式的条件与用途完整。明确区分主线和可跳过支线，避免百科式堆放所有相关结果。

输出前从头连续复读全文，按 WRITING_GUIDE 自查。直接返回完整可替换 Markdown，不返回设计稿、建议清单或 patch。严格按 PRO_OUTPUT_PROTOCOL 包装，文件使用至少五个反引号的 markdown fence，正文使用 Obsidian `$` / 独立成行 `$$`，不要 JSON 双重转义。Codex 只做纯格式规范化，不替你补教学或数学内容。
