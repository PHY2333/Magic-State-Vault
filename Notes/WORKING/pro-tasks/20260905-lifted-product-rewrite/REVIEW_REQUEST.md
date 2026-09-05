---
task_id: 20260905-lifted-product-rewrite
request_id: R02
request_type: whole-file-review
review_mode: independent
binding_id: 373162ed9f7f44828c9db9f70a9e835c
target_files:
  - Notes/07-Lifted-Product Code/Lifted product code.md
---

# 审查对象与原始目标

在全新 Pro 对话中实际读取 Browser 所绑定的最新 GitHub commit。读取本任务 `PRO_REQUEST.md`、`TASK.md`、`Notes/WRITING_GUIDE.md`、`Notes/OBSIDIAN_MATH.md`、`Notes/PRO_OUTPUT_PROTOCOL.md`，以及完整目标 `Notes/07-Lifted-Product Code/Lifted product code.md`。并按 PRO_REQUEST 指定的范围读取相邻 canonical 材料，实际核对正文所依赖的原始来源。不要依据上一轮作者解释、自评或摘要作结论。

用户认为旧文写得不好，要求交 Pro 整篇重写。审查目标是让已有 HGP 基础的读者形成能计算和继续使用的 LP 理解；不能仅核对关键词是否出现。

# 审查重点

- 从头连续读全文，检查是否有持续的构造主线，开头是否可理解，各节是否推进必要一步；避免依赖清单、维护者语言及相关结果堆放。
- 新对象、符号、定义域、指标、方向、当前作用是否在首次承重使用前闭合；读者能力是否在章节间连续。
- 关键结论能否追踪到明确条件与中间关系；直觉是否只是总结已建立内容；例子是否真正展示操作并返回一般构造。
- 正则表示与一般忠实表示的范围、循环移位方向、共轭转置、环值 blocks 维度、交叉对易、CSS 展开是否准确。
- 在环上取乘积与展开后 ordinary HGP 的差别、balanced relation 的侧别、自由群作用下的压缩计数是否成立。
- 一般二进制秩、QC 特殊维数、一般环 Künneth、非阿贝尔左右作用、LDPC／距离／解码等条件是否被正确区分；保留的来源特例是否核查且不过度一般化。
- 主线与参数／硬件／解码支线的深度是否适当，必要推导不藏入唯一链接或选读；上游完整理论不无必要重证。
- 是否保留唯一文件职责及已用标题 `循环 lift 的环表示`、`反对合与二进制转置`，链接是否有效。
- 自然中文、数学含义、符号一致性、重复与失效解释；不能只因措辞偏好重写已清晰正确的内容。

# 输出

纯 Markdown、数学分隔符、换行、callout 引用或可唯一判断的 LaTeX 语法问题由 Codex 修复，不单独构成整篇重写理由。格式暴露实质数学错误或存在多种解释时须处理实质问题。

全文达到目标且无实质问题：按协议返回 REVIEW_PASS。存在实质问题：直接返回 COMPLETE 和唯一 allowlist 目标的完整修正版，不只列建议，不修改其他文件。若必需材料无法读取或来源条件冲突，按协议明确返回相应状态；结构／ownership 变化返回 DECISION_REQUIRED。

严格遵守 PRO_OUTPUT_PROTOCOL 的 binding、至少五反引号文件 fence、完整文件及 END_RESPONSE；不修改 GitHub，不声称执行过本地操作。
