---
task_id: 20260831-kunneth-kappa-clarity
route: pro-write
status: DONE
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md

integrity: fast
review_policy: internal
audit_retention: errors-only

format_handling:
  policy: codex-contextual
  auto_repair: true
  rule_based_fixer: false
  allow_markdown_and_delimiter_repair: true
  allow_unambiguous_latex_syntax_repair: true
  escalate_only_when_meaning_is_ambiguous: true

git:
  remote: main
  branch: codex/kunneth-kappa-clarity-20260831
  base_commit: 13cd033af91eb309200373b5f4152d119687552d

automation:
  run_to_completion: true
  standing_authorization: true
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 0
  preauthorized_browser_rounds:
    - R01
  stop_only_on:
    - permission_required
    - account_mismatch
    - needs_context
    - decision_required
    - blocked
    - source_conflict
    - structural_file_change
    - path_outside_allowlist
    - ambiguous_format_or_latex_repair
    - math_content_uncertain
    - format_check_failed_after_codex_repair
    - push_failure
    - merge_to_main
---

# 用户目标

改写 Künneth 分解笔记中比较映射 $\kappa_n$ 的单射与满射解释，使读者能把两个性质分别还原为源元素、目标同调类、cycle 与 boundary 的精确逐元素条件，并能在后文域上证明中看见这两个条件怎样被实际证明。

# 当前真实问题

用户指出以下文字“有点跳跃和模糊”：

- $\kappa_n$ 是否单射：若若干因子同调类的张量和在乘积复形中变成 boundary，它在源空间中是否已经为零？
- $\kappa_n$ 是否满射：乘积复形的每个 degree-$n$ 同调类，是否都能写成若干 $[c\otimes d]$ 之和？

问题不只是措辞：当前定义处没有把“它”、源元素为零和目标类为零写成明确公式；证明末尾也没有从任意目标 cycle 与任意源元素逐项闭合满射、单射。

# 本次授权

- 由 ChatGPT Pro 输出唯一目标文件的完整修正版；
- 重点重写比较映射定义后的单射/满射解释，以及域上证明末尾与之对应的论证；
- 允许为保持前后连续性调整最少量相邻过渡和重复句；
- 保留当前工作树中“这个候选规则”的用户修改；
- Codex按上下文处理纯 Obsidian / Markdown / 唯一确定的 LaTeX 格式问题；
- 完成后在本任务分支自动 commit/push。

# 本次不处理

- 不改变 Künneth 定理、HGP、PID、一般交换环、LP 或反例的数学内容；
- 不修改其它正式笔记、canonical、索引、来源、论文或译文；
- 不删除、移动、拆分、合并或重命名正式文件；
- 不把 S003 补充材料式 (91) 当作一般定理；
- 不合并主分支。

# 当前阶段

DONE：R01 基于 checkpoint 0d4686a9e5d52c9d7ba392527cd484b043420a28 返回 COMPLETE，binding、完整性和 allowlist 均通过。完整候选经范围规范化后应用于唯一目标文件；内部数学、教学、格式与范围审查均通过，应用提交为 34495dbb90e6d7b0fe561f9902a463b1cb489551。
