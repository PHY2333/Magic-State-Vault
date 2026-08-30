---
task_id: 20260830-hgp-v7-pro-first-rewrite
request_id: R02
request_type: fresh-whole-file-review
binding_nonce: 8151dda721a142e89cc300a76c7c394d
response_token: d78df7fee1e44d9798c0ea82b199feac
target_files:
  - Notes/07-Lifted-Product Code/Hypergraph product code.md
---

# 审查目标

从头连续审查当前 GitHub checkpoint 中的完整目标文件。不要只核对上一轮要求是否执行，也不要依赖作者会话的自我说明。

# 原始目标

见同任务的 `PRO_REQUEST.md`。九项 reader outcomes、真实读者反馈、reader assumptions、来源边界和唯一文件 allowlist 全部继续生效。

# 必须读取

- `Notes/WORKING/pro-tasks/20260830-hgp-v7-pro-first-rewrite/PRO_REQUEST.md`
- `Notes/07-Lifted-Product Code/Hypergraph product code.md`
- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `CANONICAL_KNOWLEDGE.md` 中 HGP、Künneth 与 LP ownership 条目
- `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md`
- `Notes/07-Lifted-Product Code/Lifted product code.md`
- `Notes/07-Lifted-Product Code/Künneth 分解.md`

原始 `PRO_REQUEST.md` 所列的其余 owner notes 与 S007 来源材料按需要继续核对。

# 整篇审查重点

- 整篇是否持续服务目标读者，而不是只在前半详细、后半退回专家压缩；
- 二项链复形、total degree、两个物理扇区、四个 Kronecker blocks、两路径抵消与 Tanner 四类边是否首尾闭合；
- 每个 block 是否说明 source、target、尺寸、转置、作用扇区和恒等矩阵固定的坐标；
- logical-$Z$ 同调、logical-$X$ 上同调、物理扇区和编码 Hilbert space 是否始终区分；
- 定义和工具是否在合适时机出现，复杂推导是否先给总体目标或 proof map；
- S007、Künneth、平方根距离和 LP 是否各自有明确入口、出口与可跳过性；
- 一般理论、论文特例、参数支线和应用是否放置合理；
- 中文是否自然统一，是否存在重复、竞争性解释、失效链接或维护者语言；
- 数学是否全部使用 Obsidian `$` 与 `$$`。

# 已知必须验收的回归项

以下项目来自应用前只读审计，不能因为其余正文质量良好而忽略：

1. 当前稿删除了两个既有稳定 heading，导致三个正式入链锚点失效。只能修改本目标文件，因此最终稿必须在自然位置恢复精确 heading `从两张经典校验矩阵开始` 与 `行与列的乘积方向`，使以下链接重新解析：
   - `Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md` 指向 `Hypergraph product code#行与列的乘积方向`；
   - `Notes/07-Lifted-Product Code/Lifted product code.md` 与 `Notes/07-Lifted-Product Code/Künneth 分解.md` 指向 `Hypergraph product code#从两张经典校验矩阵开始`。
2. 当前稿对 CSS logical quotient、Künneth kernel/cokernel 推导和 LP 安全接口展开较长。依据 canonical ownership，应压缩为本篇主线真正需要的定义、结果、两项语义与安全边界，再链接 owner；不要在 HGP 中重做完整 owner 推导。压缩后仍须保持九项 reader outcomes 和后半解释深度，不能退化成只给链接的专家摘要。
3. 当前平方根距离节把“标准 HGP 距离下界”列为假设后推出精确等式。Tillich–Zémor 与 Panteleev–Kalachev 尚未在本地来源登记中稳定登记；最终稿不得把未登记定理强化成仓库已核验事实。请把这一节收束为明确的条件化 benchmark：若保留精确等式，必须清楚说明它依赖作为前提引入的标准下界和相应适用条件，而不是在本文内无来源证明；来源不足时应弱化结论，不要补猜。
4. 检查来源列表中的外部 Tillich–Zémor 链接与正文 claim 是否匹配；旧稿虽已有该链接，但最终稿不得把它当作已完成的本地稳定来源登记。
5. 当前 frontmatter 的 `status: draft` 表示作者候选尚未通过本轮审查。若全文通过，返回 `REVIEW_PASS`，Codex 将只机械提升为 `status: reviewed`；若返回 `COMPLETE`，完整修正版请使用 `status: reviewed`。

# 写入边界

- 唯一允许返回的文件仍是 `Notes/07-Lifted-Product Code/Hypergraph product code.md`，且必须是完整 replace block；
- 不得修改入链文件、canonical、索引、Papers、Translations 或任何旧 artifact；
- 不得只返回零散意见、patch 或审查表；需要修改时直接返回完整修正文件。

# 输出

若全文通过且上述回归项全部解决，返回 `REVIEW_PASS`。

若需要修改，返回 `COMPLETE` 和完整修正文件。不要只给零散建议。

严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。
