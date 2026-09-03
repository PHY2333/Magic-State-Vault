---
task_id: 20260903-tensor-direct-sum-up-interface
route: pro-write-review
status: PREPARE
target_files:
  - Notes/07-Lifted-Product Code/张量积与直和泛性质的 HGP-Künneth 接口.md

integrity: fast
review_policy: fresh
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
  branch: codex/tensor-direct-sum-up-interface-20260903
  base_commit: b52ede176daea174f956411f474b2966f7256dea

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

把用户给出的“张量积泛性质与直和泛性质”长篇素材整理成一份连贯、可继续使用的中文笔记，放在 `Notes/07-Lifted-Product Code/`。正文既要建立两种泛性质的数学含义，也要让读者看见它们怎样进入 HGP 的分量组织和 Künneth 比较映射。

# Ownership 冲突与本任务处理

仓库现有 `[[Tensor product 对 direct sum 的分配律]]` 已是普通域上 tensor product 与 direct sum 的 canonical owner，并且已经用两种泛性质证明分配律。若新建一篇不加边界的泛称笔记，会形成第二个 owner。

用户已明确指定新笔记位于 `Notes/07-Lifted-Product Code/`。本任务据此把新稿限定为 HGP–Künneth 的应用接口：允许为自足理解重述两条泛性质和必要构造，但不接管分配律、tensor-product complex、完整 Künneth 或 balanced tensor 的既有 ownership，也不重复这些笔记的完整证明。

# 本次授权

- 由 ChatGPT Pro 新写唯一目标文件的完整正文；
- 可以重新组织用户素材，删除超出主线的支线，补足定义、映射方向、良定义性与必要例子；
- 可以在正文中链接现有 canonical notes，并用最短充分桥梁连接 HGP、Künneth 与 LP；
- Codex按上下文处理纯 Obsidian / Markdown / 唯一确定的 LaTeX 格式问题；
- 完成 R01 后由全新 Pro 会话运行 R02 全文审查；
- 在本任务分支自动 commit/push。

# 本次不处理

- 不修改 `[[Tensor product 对 direct sum 的分配律]]`、`[[Cochain complex 的 tensor product]]`、`[[Künneth 分解]]`、HGP、LP 或 balanced tensor 正文；
- 不修改 `CANONICAL_KNOWLEDGE.md` 或 `Notes/00-index.md`：新文只作为应用桥梁，不改变现有 canonical owner 或主学习路线；
- 不删除、移动、拆分、合并或重命名正式文件；
- 不修改 Papers、Translations 或其它任务产物；
- 不合并主分支。

# 当前阶段

`PREPARE`：R01、R02 请求已准备，等待 checkpoint commit/push。
