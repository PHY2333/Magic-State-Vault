# Notes/WORKFLOWS/task-artifacts.md

本文件是 Notes v6.1 任务产物和状态字段的唯一模板来源。

## 1. TASK.md

```yaml
---
task_id:
route: sol-only | hybrid-local | hybrid-whole-note | hybrid-paper-guide
status: brief_ready | sol_mapped | whole_note_audited | awaiting_remote_sync | awaiting_pro_design | pro_design_ready | sol_design_validated | awaiting_pro_drafts | drafts_ready | assembled | sol_contract_validated | awaiting_pro_final_review | pro_final_reviewed | integration_previewed | integrated | published_branch | blocked | reopened
retain_mode: full | summary
target_files: []
remote:
  repository:
  base_branch:
  base_commit:
  task_branch:
automation:
  auto_commit: true
  auto_push: true
  remote: origin
  task_branch: notes/<task-id>
  worktree: .tmp/<task-id>
  auto_integrate_after_pro_pass: true
  auto_open_pr: false
  merge_to_main: false
  structural_changes_require_user: true
handoff:
  artifact_delivery: attachment
  require_exact_next_prompt: true
math:
  profile: obsidian-dollar-v1
  linter: Notes/TOOLS/check_obsidian_math.py
next_actor: codex-sol | chatgpt-pro | user
next_request:
whole_note_reviewed: false
---
# 目标
# 授权范围
# 非目标
# 当前阶段
```

## 2. Sol mapping artifacts

```text
BRIEF.md
DOMAIN_MODEL.md
SOURCE_PACKET.md
LEARNER_SNAPSHOT.md
SECTION_COVERAGE.md
WHOLE_NOTE_AUDIT.md
```

## 3. Pro requests

```text
PRO_HANDOFF.md
PRO_REQUESTS/ARCHITECTURE.md
PRO_REQUESTS/DRAFT-BATCH-xx.md
PRO_REQUESTS/FINAL-REVIEW.md
PRO_REQUESTS/REVISION-xx.md
```

Request 必须包含 `request_manifest_sha256`；精确 pushed commit 由 Sol chat prompt 注入。

## 4. Pro outputs

```text
PRO_DESIGN.md
PRO_DRAFTS/Uxx.md
PRO_FINAL_REVIEW.md
```

所有 Pro artifact frontmatter 至少含：

```yaml
task_id:
role:
based_on_repository:
based_on_branch:
based_on_commit:
based_on_request_path:
based_on_request_sha256:
math_profile: obsidian-dollar-v1
status:
```

## 5. Sol validation / assembly

```text
SOL_DESIGN_VALIDATION.md
PRO_REVISION_REQUEST.md
SOL_DRAFTS/
ASSEMBLY_MAP.md
ASSEMBLED_DRAFT.md
PRO_REVIEW_CARD.md
SOL_CONTRACT_AUDIT.md
MATH_RENDER_AUDIT.md
```

## 6. Final gates and integration

```text
MANUSCRIPT_VERDICT.md
INTEGRATION_PREVIEW.md
INTEGRATION_REPORT.md
AUTHORING_SUMMARY.md
AUTOMATION_LOG.md
```

## 7. PRO_DESIGN.md unit schema

```md
## Uxx — <semantic title>
- semantic_scope:
- entry_capability:
- exit_capability:
- why_now / main_question:
- primary_pattern:
- explanation_depth:
- placement / optionality:
- transition_in:
- transition_out:
- source_requirements:
- author_mode: pro_full | pro_core_sol_mechanical | sol_mechanical | retain_exact
- file_action: retain | rewrite | move | split | delete | new
```

## 8. PRO_FINAL_REVIEW.md

```yaml
status: pass | changes_required | blocked
role: whole-note-reviewer
reviewed_assembled_sha256:
review_independence: fresh-pro-session
whole_note_scope: true
math_profile: obsidian-dollar-v1
```

## 9. AUTOMATION_LOG.md

记录每次 Sol stage：

```md
| stage | branch | commit | pushed | allowlist | math audit | next actor | request |
```

当前 commit 的 hash 主要在聊天 handoff 中交付；下一阶段可将前一 commit 写入 log。

## 10. Handoff receipt

每个模型完成后必须输出一个精确下一提示词。Sol 提示词引用刚推送 commit；Pro 提示词要求 Sol接收附件并继续自动 Git。
