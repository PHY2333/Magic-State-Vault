---
task_id: 20260830-hgp-v7-pro-first-rewrite
request_id: R01
request_type: rewrite
route: pro-write-review
output_mode: full-file
review_policy: fresh-pro-review
binding_nonce: c99284ea8cf94703b00265f5c1c226bb
response_token: ffa96fd2e0f2450b948d97abc248ef24
target_files:
  - Notes/07-Lifted-Product Code/Hypergraph product code.md
---

# 用户目标

请内部自行完成教学规划，整篇重写 HGP 笔记，使读者最终能够：

1. 解释为什么两个经典校验矩阵可以视为二项链复形，以及这种视角怎样服务 HGP 构造；
2. 从链复形张量积的 total degree 逐项推出 $C_2,C_1,C_0$；
3. 解释为什么中间链群的两个直和分量是两类物理量子比特扇区，而不是两个逻辑扇区；
4. 从乘积 differential 逐块构造 $H_X,H_Z$，说明每块的 source、target、尺寸、转置方向，以及恒等矩阵固定哪个坐标；
5. 用清楚的 proof map 解释两条 product path 为什么都给出同一个 $A\otimes B$，并在 $\mathbb F_2$ 中相消；
6. 从 Kronecker blocks 读出四类 Tanner 邻接、种子图副本和行／列方向；
7. 区分一般 $A,B$ 记号下的 HGP 与 S007 的来源特定记号、布局和执行语义；
8. 只在逻辑 support／维数问题真正出现时引入 Künneth，并让该支线可以跳过；
9. 准确说明 HGP 何时是 qLDPC、平方根距离何时只是标准条件化基准，以及 HGP 到 LP 的安全接口与局限。

# 当前真实读者反馈

- “依赖”“不是前置”“ownership”一类维护语言不是教学解释；正文应直接补足读者需要的桥梁。
- 当前笔记前几节细致，后半突然退回专家压缩，读者能力出现断崖。
- 不能只展示 block formulas，让读者自行重建每块作用在哪个扇区、固定或改变哪个坐标。
- 长推导需要先给总体目标或 proof map，再给局部步骤。
- S007 适配、Künneth、距离支线和 HGP 到 LP 应分别放置，不要相互挤压或冒充一般主线。

# Reader assumptions

## 可以直接依赖

- 矩阵、线性映射和基本模 $2$ 运算；
- Pauli 算符与稳定子校验的基础概念。

## 不能直接依赖

- 已经会操作链复形张量积或 total-degree differential；
- 已经掌握 Künneth 分解；
- 已经能从 Kronecker block 公式读出指标语义；
- 已经知道 HGP 的逻辑空间或维数公式。

仓库存在相关笔记不代表读者已经掌握；本笔记需要在首次使用处提供足够桥梁，但不重复上游笔记的完整证明。

# 必须读取

- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`
- `Notes/WORKING/authoring-tasks/20260829-hgp-whole-note-coverage-audit/BRIEF.md`
- `Notes/WORKING/authoring-tasks/20260829-hgp-whole-note-coverage-audit/SECTION_COVERAGE.md`
- `Notes/WORKING/authoring-tasks/20260829-hgp-whole-note-coverage-audit/WHOLE_NOTE_AUDIT.md`
- `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`
- `Notes/06-CCZ Distillation/CSS码中的cochain complex.md`
- `Notes/06-CCZ Distillation/Tensor product 对 direct sum 的分配律.md`
- `Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md`
- `Notes/07-Lifted-Product Code/Künneth 分解.md`
- `Notes/07-Lifted-Product Code/Lifted product code.md`
- `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md`
- `Translations/S007.full.zh-CN.md`：只需聚焦“译文信息”、图 1(b)、§2.2 的式 (1) 与四类边、§3.1 的物理执行语境、§6 的 LP 特例
- `Papers/SOURCES.md`：只需核对 `### S007` 的来源登记

把 coverage audit 当作问题清单和回归证据，不把其中旧 v5 阶段指令当作当前流程，也不要机械冻结旧句或把旧 artifact 链接进正式正文。

# 来源与数学边界

- 当前 HGP 文件是待重写对象；现有 `status: reviewed` 不表示全文无误。旧审计只验证了早期单元，其余章节仍标为 `changes-required`。
- 固定 chain convention 为 $C_2\xrightarrow{H_Z^{\mathsf T}}C_1\xrightarrow{H_X}C_0$。这里的 $H_1=\ker H_X/\operatorname{im}H_Z^{\mathsf T}$ 是 logical-$Z$ support classes；对偶 cochain 的 $H^1$ 才对应 logical-$X$ support classes。不要把种子矩阵名、一阶同调与编码 Hilbert space 混为一谈。
- 可以采用 tensor-product owner 中的 total degree、直和展开和 product differential，但必须从升 degree 的 cochain 叙述正确转换到本笔记的降 degree chain convention。一般系数中的 Koszul 符号不得误述为永远可省略。
- 对两个二项链复形，使用本库固定记号 $A\in\mathbb F_2^{m_A\times n_A}$、$B\in\mathbb F_2^{m_B\times n_B}$。中间链群应给出两个物理扇区，最终 blocks 与 canonical convention 一致：

  $$
  H_X=\left[\,A\otimes I_{m_B}\;\middle|\;I_{m_A}\otimes B\,\right],
  \qquad
  H_Z=\left[\,I_{n_A}\otimes B^{\mathsf T}\;\middle|\;A^{\mathsf T}\otimes I_{n_B}\,\right].
  $$

  必须由 differential 推出这些式子，而不是只把它们列为定义。
- 域上的 Künneth 直和与 $K=k_Ak_B^{\mathsf T}+k_A^{\mathsf T}k_B$ 只用于这里的 $\mathbb F_2$ HGP。完整证明留给 owner note；若设为选读，后续主线不得暗中依赖。不得无条件推广到环系数 LP。
- S007 只支撑其 arXiv:2608.20164 v1 的式 (1)、$q^A/q^B/x/z$ 标签、图 1 的水平／竖直布局和综合征提取语境。水平／竖直不是 HGP 的内禀命名，一般 Tanner check node 也不自动等于硬件 check ancilla。S007 的 ONEX 调度、图 12 四阶段、LP 参数和性能数据不得冒充一般 HGP 定理。
- 一般 HGP 的四 blocks、四类 Tanner 边、固定／变化坐标和种子图副本必须先在 $A,B$ 记号下闭合；S007 只能作为可跳过的记号适配器。
- HGP 构造自动保证 CSS 对易，但不自动保证 qLDPC、高率或平方根距离。qLDPC 需要种子行重和列重在码族中统一有界；$d=\Theta(\sqrt N)$ 只可作为条件明确的标准基准，不是任意输入结论。Tillich–Zémor 与 Panteleev–Kalachev 尚未在本地来源登记中稳定登记，不得新增或强化无支撑的精确定理声称；必要时限缩陈述或返回 `NEEDS_CONTEXT`。
- HGP 到 LP 只作安全接口：群基元素或循环单项式可以给出一个 permutation block；一般多项式／群代数元素给出 permutation blocks 的 $\mathbb F_2$ 和；任意有限维代数元素只保证一般线性 block。非交换情形需要区分右／左模以及 commuting left/right actions，不能靠一个形式化的 $*$ 无条件保证对易。LP 的好距离、好率或 qLDPC 性质都需要额外子族假设。
- 不新增来源未支持的参数或定理，不猜测 S007 未展示的第二因子、完整 sectors 或参数推导。关键材料冲突或不足时返回 `NEEDS_CONTEXT`；若只有拆分、移动、合并、删除或重命名正式文件才能完成，则返回 `DECISION_REQUIRED`。

# 写作权限

## 允许

- 完整替换唯一目标文件；
- 重组标题和论证顺序；
- 删除竞争性或重复解释；
- 在当前文件内把 S007、Künneth、距离推导或 LP 接口明确设为可跳过支线；
- 保留 `note_type: reference`、`entry_mode: guided`，并把本轮作者候选的 frontmatter `status` 设为 `draft`。

## 禁止

- 输出或修改其他任何正式文件、索引、canonical、来源登记、译文或旧 artifact；
- 删除、移动、拆分、合并或重命名正式文件；
- 把任务、审计、依赖清单、canonical ownership 或工作流语言写进读者正文；
- 用链接替代本笔记完成九项目标能力所需的关键解释。

涉及删除、移动、拆分、合并或重命名正式文件时，返回 `DECISION_REQUIRED`，不要自行执行。

# 写作要求

- 内部自行完成整篇教学规划，不输出独立学习路线、设计稿、unit map、审查表或修改说明；
- 直接输出完整、可替换的目标 Markdown，正文采用自然、统一的中文教材语体；
- 开头给出读者将构造什么、各阶段怎样衔接的短路线图；每个长推导先给目标或 proof map，再展开局部步骤；
- 保持从开头到结尾的解释深度；后半不能退化成只有公式、结论和链接的专家摘要；
- 每个 Kronecker block 都要在正文说明作用扇区、固定坐标、变化坐标、索引与尺寸，不能要求读者反向猜；
- 一般 HGP 主线必须独立闭合；S007、Künneth、距离和 LP 支线都应明确入口、出口和可跳过性；
- 可以使用适量 worked example 或索引表，但不要让表格替代连续解释；
- 遵守 Obsidian 数学格式，只用 `$...$` 和独立成行的 `$$...$$`，不得使用 `\\(...\\)`、`\\[...\\]`、`/(...)`、JSON 双转义或未闭合 `$`；
- 正文链接必须有效，不链接 `Notes/WORKING/`，不把来源特例写成一般结论。

# 完成标准

1. 读者能解释两个经典校验矩阵如何成为二项复形，以及端点零映射和 degree 在需要处如何闭合。
2. 从 total degree 逐项得到 $C_2,C_1,C_0$，并明确 $C_1$ 两个分量是两类物理比特扇区。
3. 从 product differential 逐块导出 $H_X,H_Z$；每块都交代 source、target、尺寸、转置、作用扇区和恒等矩阵固定的坐标。
4. 用 proof map 闭合两条 product paths、$A\otimes B+A\otimes B=0$ 与 $H_XH_Z^{\mathsf T}=0$／CSS 对易之间的关系。
5. 在一般 $A,B$ 记号下闭合四类 Tanner 邻接、种子图副本、固定／变化坐标和无对角边，再单独给出 S007 adapter。
6. 清楚区分一般 HGP 与 S007 的 convention、布局和执行语义；跳过 S007 不影响一般主线。
7. 逻辑问题出现后才引入 Künneth；支线可跳过，logical-support quotient、编码空间与物理扇区不混淆。
8. qLDPC、平方根距离基准与 HGP 到 LP 都明确写出必要假设和不得推出的范围。
9. 中文和解释深度整篇一致；长推导有总体目标，局部步骤持续说明其作用。
10. 正文没有任务／审计／ownership 语言、`Notes/WORKING/` 链接或依赖清单，也没有用链接替代核心教学。
11. frontmatter 恰保留 `note_type: reference`、`entry_mode: guided` 并使用 `status: draft`；作者轮不得自称已通过 fresh review。
12. 全部 reader-visible 数学通过 `Notes/TOOLS/check_obsidian_math.py`，只返回 allowlist 中唯一目标的完整 replace block，不返回 patch、设计稿或审查表。

# 输出协议

严格按照 `Notes/PRO_OUTPUT_PROTOCOL.md`。只输出 allowlist 中目标文件的完整文件。
