---
task_id: <YYYYMMDD-short-name>
route: codex-only | pro-write | pro-write-review
status: request-prepared
target_files:
  - <path>
git:
  remote: origin
  branch: notes/<task-id>
  base_commit: <commit-before-task>
automation:
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 2
  audit_retention: task-branch-only
---

# 用户目标

# 当前真实问题

# 本次授权

# 本次不处理

# 当前阶段
