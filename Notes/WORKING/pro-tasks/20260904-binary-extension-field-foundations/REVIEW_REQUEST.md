---
task_id: 20260904-binary-extension-field-foundations
request_id: R02
request_type: fresh-whole-file-review
binding_id: d5926455b5fe42b4ba63bfd80a5dd173
target_files:
  - Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md
---

# 审查目标

从头连续审查 Browser 提示所绑定最新 GitHub commit 中的完整目标文件。不要依赖 R01 作者的解释、自评或摘要；先判断目标读者能否从具体构造出发形成可计算、可迁移的 $\mathbb F_{2^s}$ 理解，再审查数学、教学、文件边界和 Obsidian 格式。

# 原始目标

完整读取同任务的 `PRO_REQUEST.md`。其中 reader outcomes、reader assumptions、ownership、数学边界、唯一文件 allowlist 与完成标准全部继续生效。

# 必须读取

- `Notes/WORKING/pro-tasks/20260904-binary-extension-field-foundations/PRO_REQUEST.md`
- `Notes/WORKING/pro-tasks/20260904-binary-extension-field-foundations/TASK.md`：核对唯一 owner 边界与预定索引/canonical 集成文字
- Browser 提示所绑定最新 commit 中的 `Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md`
- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `CANONICAL_KNOWLEDGE.md` 的相关 ownership 边界
- `Notes/01-量子纠错基础/二进制空间性质.md`
- `Notes/07-Lifted-Product Code/Lifted product code.md`

# Fresh review 重点

- 开头是否从“怎样给 $s$ 个二进制坐标补上域乘法”这一真实问题进入，并准确解释 $\mathbb F_2^s$ 与 $\mathbb Z/2^s\mathbb Z$ 为什么不是所需域；
- 不可约多项式商是否从同余类、低次唯一代表元、加乘法到 Bézout 逆元论证全部闭合，且没有把可约多项式、本原多项式混同；
- 是否区分抽象唯一的有限域与依赖不可约多项式、基、本原元的具体表示，没有声称存在自然坐标同构；
- $\mathbb F_4$ 是否真正作为贯穿算例，完成 XOR 加法、乘法约化、求逆，并至少支撑一个后续结构或矩阵判断；
- Frobenius 是否确为 $\mathbb F_2$-线性自同构，$a^{2^s}=a$、其阶、固定域、Galois 群与子域 $d\mid s$ 条件是否准确且没有循环论证；
- 乘法群循环性是否只在合适深度使用，没有把“非零元素阶整除 $2^s-1$”误写成每个非零元素都是本原元；
- 绝对迹、绝对范数、迹配对、对偶基和坐标提取是否定义完整，符号指标一致；是否明确绝对范数对非零元素恒为 $1$；
- 若提正规基、自对偶基或自对偶正规基，其存在性条件是否精确，且内容确实服务坐标/矩阵主线；
- 固定元素乘法矩阵 $M_\gamma$ 的列/坐标约定是否明确，$M_{\gamma+\eta}$、$M_{\gamma\eta}$、可逆性和基依赖是否正确；一般基是否使用 $\operatorname{tr}(\beta_i\gamma\alpha_j)$，并且只在自对偶基前提下化为 $\operatorname{tr}(\alpha_i\gamma\alpha_j)$；
- 未知元素乘法的结构常数公式是否与对偶基、坐标约定一致，并真正解释“双线性但不联合线性／坐标上为二次”这一分叉；
- 是否准确区分单输入上的线性映射、两个变量上的双线性乘法与拼接输入上的联合线性，不把双线性误作线性；
- 量子信息接口是否只说明 $s$ 比特标签、可逆二进制线性算术与未知乘法的非线性分叉，没有无证明宣称完整 Clifford 层级、门最优性或蒸馏结论；
- 全文是否持续推进“构造—计算—结构—二进制表示—后续接口”的主线，而不是有限域性质百科、定义列表或论文背景综述；
- 新对象是否在首次承重使用前解释，关键“因此／唯一／良定义／可逆／线性”是否可沿前文追踪；
- 是否没有重复 `[[二进制空间性质]]` 的补空间/正交补内容，也没有展开 `[[Lifted product code]]` 的 LP 构造；
- 中文是否自然统一，wikilink 是否有效，是否残留任务、review、allowlist、ownership、路径或维护者语言；
- 所有 reader-visible 数学是否严格符合 Obsidian 的 `$` 与独立 `$$` 定界规范。

# 写入边界

- 唯一允许返回的文件是 `Notes/08-Binary Extension Field Non Clifford Module/二元扩域.md`，必须是完整 replace block；
- 不得修改 `Notes/00-index.md`、`CANONICAL_KNOWLEDGE.md`、现有正式笔记、Papers、Translations 或任务 artifact；
- 不得删除、移动、拆分、合并或重命名正式文件；
- 不得只返回意见、patch、审查表或部分章节。

# 输出

全文通过且所有审查重点均满足时，返回 `REVIEW_PASS`。

若存在实质问题，返回 `COMPLETE` 和完整修正文件，不只给建议。严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。

孤立的 Markdown / Obsidian 外层格式或可唯一判断的 LaTeX 语法问题由 Codex按 `Notes/OBSIDIAN_MATH.md` 修复，不能单独触发整篇 `COMPLETE`；只有实质教学、数学、语义或范围问题才要求返回完整修正版。
