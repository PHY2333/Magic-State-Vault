---
task_id: 20260831-kunneth-pro-rerun
request_id: R02
request_type: whole-file-review
review_mode: independent
binding_id: 037741f2252d4809a2bdbe23c0ae4566
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md
---

# 审查对象

审查 Browser 提示所绑定的 GitHub commit 中的完整目标文件。以该 commit 中的实际文件为准，不依据上一轮作者对正文的解释、自评或摘要作出结论。

# 原始目标

见同任务的 `PRO_REQUEST.md`。审查时同时判断目标本身是否在全文中真正实现，而不是只核对若干显式要求是否出现。

# 审查原则

把目标文件视为一篇待发表的完整笔记，从头连续阅读。不要因为某段与上一轮输出一致而默认保留，也不要仅因个人措辞偏好重写已经清楚、准确且连续的内容。

需要判断的是正文能否让目标读者形成可继续使用的理解。

# 必须读取

- `Notes/WORKING/pro-tasks/20260831-kunneth-pro-rerun/PRO_REQUEST.md`
- `Notes/WORKING/pro-tasks/20260831-kunneth-pro-rerun/APPLY_REPORT.md`（若已存在；核对其中 R01 的 Codex 机械格式修复）
- Browser 提示所绑定 commit 中的完整 `Notes/07-Lifted-Product Code/Künneth 分解.md`
- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `CANONICAL_KNOWLEDGE.md` 中 Künneth、HGP 与 LP 的范围
- `PRO_REQUEST.md` 列出的上游、下游、May、Stacks 与 S003 来源边界

# 审查重点

## 1. 整篇目标与主线

- 开头是否建立了合适的对象、问题或整体图景；
- 全文是否持续服务“何时能由因子同调读出乘积同调”这一学习目标；
- 各节是否真正推进“比较映射 → 域上同构 → 二项复形 / HGP 回报 → 一般系数边界”的主线；
- 是否存在维护者视角、依赖清单、canonical ownership、任务范围或链接串侵入正文。

## 2. 读者能力与章节连续性

- 系数域、分次同调、tensor 下标和 chain convention 是否在首次承重前得到说明；
- 前一节的出口是否足以支撑下一节，尤其是域上预告、长证明、HGP 应用和一般环进阶层之间；
- 是否出现突然切回专家压缩、符号密度突增或未经铺垫的自然性、导出范畴或谱序列术语；
- 选读一般环内容跳过后，域上主线与 HGP 回报是否仍然成立。

## 3. 定义、术语与对象角色

- $\kappa_n$、chain map、$H_p(f)$、$f\otimes g$、contracting homotopy、flat/K-flat 与谱序列页是否在承重前得到足够说明；
- HGP / LP 的全称与当前角色、逻辑比特数 $K$、任意链复形 $X$ 和 PID 的当前含义是否在首次使用时闭合；
- 是否区分概念的一般含义与它在当前证明或应用中的作用；
- 是否区分 Künneth 直和项的两类逻辑来源、logical-support quotient 与 HGP 物理比特扇区；
- 工具和高级术语是否在其用途出现后才引入。

## 4. 推理、公式与抽象总结

- 关键公式是否说明对象、条件、映射方向和用途；
- cycle 性、代表元无关性、可逆性、自然性及二项 / HGP 维数推导是否能沿前文追踪；
- 是否用“干净、隐藏、额外、意外识别、显然、自然、良定义、相容”等词跳过关键步骤；
- 每条直觉或总结是否只压缩已经建立的内容，并能还原为具体对象、条件、关系和后果。

## 5. 解释深度与复杂推导

- 域上证明是否先给目标、困难和地图；complement、可缩部分、两个 tensor 因子上的收缩与 Koszul 符号是否完整；
- 初等 bookkeeping 是否压过当前主题，或反过来省略了唯一承重理由；
- 成功例子是否展示一般机制、说明不能推广之处并返回主线；
- 一般环层是否给出谱序列的页间同调、后续微分、$E^\infty$、filtration、associated graded 与 extension 之间的可追踪关系。

## 6. 一般理论、来源与文件职责

- 域、PID、一般交换环的假设和结论是否分层准确；May 的 flat/free 条件、Tor 指标与非自然 splitting 是否正确；
- PID 短正合列是否说明单射、满射与像等于核，使 $\operatorname{Tor}_1$ 的位置可以沿公式追踪；
- derived tensor 的 K-flat 条件、Stacks 指标重编号、微分方向和收敛目标是否正确；
- $R_2$ 是否注明为本文直接计算、非 PID，并正确展示 $\kappa_1$ 秩 $1$、非单射且非满射；
- 是否严格遵守用户决定，不把 S003 式 (91) 当作一般定理；
- 是否避免重写 HGP blocks、CSS 对易、距离、LP balanced relation、环值 blocks、二进制展开、非交换左右模或 S007 执行。

## 7. 行文、重复与 Obsidian 渲染

- 中文是否自然统一，不像计划、审查表或 checklist 的改写；
- 是否存在重复定义、竞争性解释、补丁式段落或无效过渡；
- 是否保留 `# Künneth 分解` 和文字精确为 `PID 与一般系数环` 的二级 heading；
- 所有数学是否遵守 `Notes/OBSIDIAN_MATH.md` 的行内与独立块公式规范；
- 是否存在被禁用的公式定界、双重转义或其它无法正常渲染的形式。
- 若 `APPLY_REPORT.md` 记录了 Codex 机械格式修复，其最小 diff 是否只改变格式且保持数学与叙述语义不变；若否，不得返回 `REVIEW_PASS`。

# 写入边界

- 唯一允许返回的文件是 `Notes/07-Lifted-Product Code/Künneth 分解.md`，必须是完整 replace block；
- 不得修改其他正式笔记、canonical、索引、Papers、Translations 或任务 artifact；
- 不得只返回意见、patch、审查表或部分章节；
- 若只有删除、移动、拆分、合并或重命名正式文件才能解决问题，返回 `DECISION_REQUIRED`，不要擅自实施结构变更。

# 审查输出

若完整目标文件已经达到原始目标，并且没有需要修改的实质问题，返回：

```text
PRO_STATUS: REVIEW_PASS
```

若存在需要修改的问题：

- 不要只列建议；
- 直接返回唯一目标文件的完整修正版；
- 不修改未列入 `target_files` 的文件；
- 保留来源支持、正确公式和已有有效内容；
- 严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`；
- 使用 `PRO_STATUS: COMPLETE`；
- 在 `END_RESPONSE` 后不再输出内容。

若无法读取目标文件或完成审查所必需的来源，只返回协议规定的 `NEEDS_CONTEXT`，并准确列出缺失路径；不得根据旧对话内容补猜。
