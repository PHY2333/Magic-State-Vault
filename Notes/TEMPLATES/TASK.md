---
task_id: <YYYYMMDD-short-name>
route: codex-only | pro-write | pro-write-review
status: PREPARE
target_files:
  - <path>

integrity: fast
review_policy: none | internal | fresh
audit_retention: errors-only | minimal | full

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
    - math_check_failure
    - push_failure
    - merge_to_main
---

# 用户目标

# 当前真实问题

# 本次授权

# 本次不处理

# 当前阶段
