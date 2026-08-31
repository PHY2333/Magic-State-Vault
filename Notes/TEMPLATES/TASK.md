---
task_id: <YYYYMMDD-short-name>
route: codex-only | pro-write | pro-write-review
status: PREPARE
target_files:
  - <path>

integrity: fast
review_policy: none | internal | same-thread | independent
audit_retention: errors-only | minimal | full

format_handling:
  policy: codex-contextual
  auto_repair: true
  rule_based_fixer: false
  allow_markdown_and_delimiter_repair: true
  allow_unambiguous_latex_syntax_repair: true
  escalate_only_when_meaning_is_ambiguous: true

git:
  remote: origin
  branch: notes/<task-id>
  base_commit: <commit-before-task>

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

# 当前真实问题

# 本次授权

# 本次不处理

# 当前阶段
