---
task_id: 20260831-kunneth-pro-rewrite
request_id: R02
request_type: fresh-whole-file-review
binding_id: 1c08a6f6c7f64936bd39ac56c06d7c61
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md
---

# 审查目标

从头连续审查 Browser 提示所绑定的最新 GitHub commit 中的完整目标文件。不要依赖上一轮作者对自己的说明，也不要只核对零散要求；先判断整篇是否让目标读者形成可继续使用的 Künneth 理解，再检查证明、应用、一般系数边界与来源。

# 原始目标

见同任务的 `PRO_REQUEST.md`。其中 reader outcomes、真实反馈、assumptions、来源与数学边界、唯一文件 allowlist 和完成标准全部继续生效。

# 必须读取

- `Notes/WORKING/pro-tasks/20260831-kunneth-pro-rewrite/PRO_REQUEST.md`
- Browser 提示所绑定最新 commit 中的 `Notes/07-Lifted-Product Code/Künneth 分解.md`
- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `CANONICAL_KNOWLEDGE.md`：重点核对 Künneth、HGP 与 LP 的 ownership 边界
- `Notes/06-CCZ Distillation/Chain complex 与 cochain complex.md`
- `Notes/06-CCZ Distillation/Cochain complex 的 tensor product.md`
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`
- `Notes/07-Lifted-Product Code/Lifted product code.md`
- `PRO_REQUEST.md` 列出的 May 与 Stacks 来源，重点复核精确假设、指标与收敛目标
- S003 补充材料式 (91) 的来源边界：用户已决定它不作为一般定理，不得用来支持无条件的一般环直和

# 审查重点

- 开头是否真正提出 $H(C\otimes D)$ 与 $H(C),H(D)$ 的关系问题，并在读者承担技术证明前给出域上结论、条件和用途；
- 全文是否只有“比较映射 → 域上同构 → 二项复形/HGP 回报 → 一般系数边界”这一条清楚主线；
- $\kappa_n$ 的良定义、域上可逆性与自然性是否被准确区分；
- complement/contracting-homotopy 证明是否逻辑完整且不过度展开，所有含可缩因子的 tensor summands 是否真的被处理；
- 一般域证明中的 Koszul sign 是否完整，两个因子上的 contraction 是否使用了正确符号；
- 是否明确区分自然的 $\kappa_n$ 与不自然的补空间选择；
- 域上 worked example 是否正确、紧凑并真正帮助理解；
- 二项复形的 kernel/cokernel 公式、HGP chain convention、logical-$Z$ support quotient 与 $K$ 公式是否一致；
- 是否始终使用“两类逻辑来源”或“Künneth 直和项”，没有把它们误称为 HGP 两个物理扇区；
- PID 短正合列的 flat/free 假设、$p+q=n-1$ 的 $\operatorname{Tor}_1$ 指标与一般不自然 splitting 是否与 May 一致，是否避免把更强充分条件误说成必要条件；
- 一般环谱序列是否以 derived tensor product 为目标，ordinary tensor product 是否有 K-flat 边界，是否说明从 Stacks 上同调指标到本文同调指标的重编号，并准确处理微分方向、高阶 $\operatorname{Tor}$、$E^\infty$、associated graded 与 extension；
- 是否避免把循环 LP 环默认成 PID，避免把“非域”误写成“必有非零 $\operatorname{Tor}$”或“每例都失败”；
- $R_2$ 反例是否注明本文直接计算，说明 $R_2$ 不是 PID，并正确展示定义域/目标维数均为 $2$、两个像代表同一非零类、像秩为 $1$、非单射且非满射；
- 是否严格遵守用户决定，不把 S003 式 (91) 当作一般定理或用它覆盖 May/Stacks 的条件；
- 对 LP 的结论是否只是安全边界和秩计算接口，没有越界重写 LP blocks、balanced relation 或非交换左右模理论；
- 一般理论、HGP 应用、一般环进阶层是否层次清楚，后半没有突然退回专家压缩语体；
- 中文是否自然统一，术语是否在承担推理前说明，是否存在重复、竞争性解释、失效链接、任务语言或维护者语言；
- 是否保留文字精确为 `PID 与一般系数环` 的 heading，使 `[[Künneth 分解#PID 与一般系数环]]` 继续解析；
- 所有 reader-visible 数学是否严格符合 Obsidian 的行内与独立块公式定界规范。

# 写入边界

- 唯一允许返回的文件是 `Notes/07-Lifted-Product Code/Künneth 分解.md`，必须是完整 replace block；
- 不得修改其他正式笔记、canonical、索引、Papers、Translations 或任务 artifact；
- 不得删除、移动、拆分、合并或重命名正式文件；
- 不得只返回意见、patch、审查表或部分章节。

# 输出

全文通过且所有审查重点均满足时，返回 `REVIEW_PASS`。

需要修改时，返回 `COMPLETE` 和完整修正文件，不只给建议。严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。
