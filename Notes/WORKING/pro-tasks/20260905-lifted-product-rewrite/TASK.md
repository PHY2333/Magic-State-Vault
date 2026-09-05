---
task_id: 20260905-lifted-product-rewrite
route: pro-write-review
status: DONE
target_files:
  - Notes/07-Lifted-Product Code/Lifted product code.md
integrity: fast
review_policy: independent
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
  branch: codex/lifted-product-rewrite-20260905
  base_commit: c88b1eb136a0a4465e28fadf6af90830941d8ca8
automation:
  run_to_completion: true
  standing_authorization: true
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 1
  preauthorized_browser_rounds:
    - R01
    - R02
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

用户原话：“Notes/07-Lifted-Product Code/Lifted product code我觉得写的不算很好，按照流程交给pro重写一份”。由 ChatGPT Pro 完整重写原文件，再由全新 Pro 对话独立审查。

# 当前真实问题

用户没有指定某个公式或局部句子错误。本次让 Pro 自行判断旧文的教学问题并重建连续主线，不把 Codex 的初步观察当作用户追加要求。旧文开头列出依赖，随后并列涉及循环 lift、环值 blocks、商、QC 维数、距离、非阿贝尔、硬件与解码；需使核心构造与来源支线各居其位。

# 本次授权

- Pro 在原路径整篇重写；Codex 不代写教学正文。
- 保留既有主笔记职责与已用锚点；不新增前置笔记。
- Codex 捕获、验证 binding 与 allowlist、提取 staging、规范格式、检查并应用。
- R01 应用后自动发送独立 R02，按协议处理完整修订或 REVIEW_PASS。
- 自动 commit/push 任务分支；不合并 main。

# 仓库隔离与放置理由

在 `.tmp/worktrees/lifted-product-rewrite-20260905/` 建立隔离工作树，基于任务启动时已提交 HEAD。主工作树中 Künneth、张量接口、SOURCES 与 S008 文献／翻译的未提交修改不进入此任务。任务材料放在本任务目录，正式产物只替换原笔记；`CANONICAL_KNOWLEDGE.md` 与 `Notes/00-index.md` 的归属不变，原则上无需修改。

# 本次不处理

不更动 Papers、Translations、其他任务及其他正式笔记；不删除、移动、拆分、合并或重命名文件。若必须改变 ownership、文件结构或出现来源条件冲突，按协议明确返回并暂停相关步骤。

# 当前阶段

DONE：R01 完整重写已在 ab3905d1a3a9b218485ee92bcefb9f76b6979ea7 应用并推送。全新 ChatGPT 6 Pro 对话对该提交完成独立 R02 并返回 REVIEW_PASS；绑定、完整性、Obsidian 数学、链接／脚注和 diff 检查通过。正文没有 Codex 教学性或数学性改写，无未解决标记；完成报告随最终任务提交保留，不合并 main。R01 会话：https://chatgpt.com/c/6a9b69f6-9504-83e8-9fdf-4a9ec03ebff5 。R02 会话：https://chatgpt.com/c/6a9b725c-0ad8-83ee-806c-e4e0115a901c 。
