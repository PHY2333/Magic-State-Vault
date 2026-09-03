---
task_id: 20260903-tensor-direct-sum-up-interface
request_id: R02
request_type: fresh-whole-file-review
binding_id: 27cebcf49a4247dcb59a4a89f4231318
target_files:
  - Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md
---

# 审查目标

从头连续审查 Browser 提示所绑定的最新 GitHub commit 中的完整目标文件。不要依赖 R01 作者对自己的说明，也不要只逐条打勾；先判断整篇是否让目标读者真正掌握“tensor 线性化、direct sum 拼接”这一映射构造模式，再审查数学、教学、ownership 边界和 Obsidian 格式。

# 原始目标

完整读取同任务的 `PRO_REQUEST.md`。其中 reader outcomes、用户素材、reader assumptions、ownership、数学边界、唯一文件 allowlist 与完成标准全部继续生效。

# 必须读取

- `Notes/WORKING/pro-tasks/20260903-tensor-direct-sum-up-interface/PRO_REQUEST.md`
- `Notes/WORKING/pro-tasks/20260903-tensor-direct-sum-up-interface/TASK.md`：核对两条预定机械集成文字及其精确插入位置
- Browser 提示所绑定最新 commit 中的 `Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md`
- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `CANONICAL_KNOWLEDGE.md` 的相关 ownership 边界
- `Notes/06-CCZ Distillation/Tensor product 对 direct sum 的分配律.md`
- `Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md`
- `Notes/06-CCZ Distillation/Balanced tensor product 与 coinvariant quotient.md`
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`
- `Notes/07-Lifted-Product Code/Künneth 分解.md`
- `Notes/07-Lifted-Product Code/Lifted product code.md`

# Fresh review 重点

- 开头是否从读者能理解的映射延伸问题进入，而不是从仓库依赖、术语清单或抽象口号进入；
- 全文是否围绕“先验证规则，再线性化，再按分量拼接”推进，没有退化为 tensor/direct sum 百科；
- tensor universal property 是否和典范双线性映射一起陈述，存在性、因子化唯一性与对象唯一到唯一同构是否准确区分；
- quotient realization 是否列全关系并真正说明为何任意双线性映射下降到 quotient；
- pure tensor、一般 tensor、$f\otimes g$ 与 basis expansion 是否保持不同层次，是否避免暗示一般 tensor 有唯一 pure-tensor decomposition；
- direct sum 的 mapping-out 泛性质是否完整，有限 biproduct 与无限 direct sum/product 的分叉是否准确；
- 两种泛性质是否比较了输入数据、映射方向和输出，而不只给直觉标签；
- 是否准确说明二元 $V\times W$ 与 $V\oplus W$ 的向量空间关系，以及“双线性但通常非联合线性”才是相关映射类别的分叉；不得把这一点错误归因于有限维或把 $V\times W$ 说成仅是集合；
- quotient representatives 一节是否准确区分 $(v,w)$、$v\otimes w$、$[v]\otimes[w]$、$[v\otimes w]$，并把 quotient-tensor 公式严格限制在安全范围；
- Künneth 接口是否先用 Koszul differential 证明 $c\otimes d$ 是 cycle，再检查两个因子的代表元改变给出 boundaries、得到同调类上的 bilinear map，最后使用 tensor universal property；是否避免从尚未定义的 $[c\otimes d]$ 起步，并明确泛性质不自动给出同构；
- HGP 中两个物理 summands 是否与 Künneth 的两个逻辑同调 summands 严格区分；
- HGP 的 qubit／物理坐标解释是否明确专门化到 $k=\mathbb F_2$ 并采用现有 HGP owner 的降次数 chain convention，没有无说明推广到任意域；
- 是否避免混淆 ordinary tensor、Kronecker matrix blocks、product-complex totalization 与 balanced tensor；
- 是否只用最短充分接口连接相邻主笔记，没有重写分配律的 $\Phi/\Psi$、$\partial^2=0$、完整 Künneth、HGP blocks 或 balanced tensor proof；
- 是否与 `TASK.md` 中已固定的两条机械集成文字一致：`Notes/00-index.md` 把它列为 HGP 后的可选应用桥梁，`CANONICAL_KNOWLEDGE.md` 明确它不接管一般泛性质与分配律 ownership；这两条文字和位置不由 Codex另行发挥；
- 例子是否真正检验读者能否构造映射，且没有成为竞争性主线；
- 术语是否都在承担推理前得到解释，关键“因此／唯一／良定义”能沿前文追踪；
- 中文是否自然统一，链接是否有效，是否残留任务、review、allowlist、ownership 或维护者语言；
- 所有 reader-visible 数学是否严格符合 Obsidian 的行内与独立块公式定界规范。

# 写入边界

- 唯一允许返回的文件是 `Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md`，必须是完整 replace block；
- 不得修改其它正式笔记、canonical、索引、Papers、Translations 或任务 artifact；
- 不得删除、移动、拆分、合并或重命名正式文件；
- 不得只返回意见、patch、审查表或部分章节。

# 输出

全文通过且所有审查重点均满足时，返回 `REVIEW_PASS`。

需要修改时，返回 `COMPLETE` 和完整修正文件，不只给建议。严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。

孤立的 Markdown / Obsidian 外层格式或可唯一判断的 LaTeX 语法问题由 Codex按 `Notes/OBSIDIAN_MATH.md` 修复，不能单独触发整篇 `COMPLETE`；只有实质教学、数学、语义或范围问题才要求返回完整修正版。
