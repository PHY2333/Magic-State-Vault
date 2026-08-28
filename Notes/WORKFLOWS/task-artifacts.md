# Notes/WORKFLOWS/task-artifacts.md

本文件是 Notes v5 任务产物模板的唯一来源。

## 1. TASK.md

```md
---
task_id: <id>
status: brief_ready | mapped | learner_ready | designed | design_validated | packet_ready | drafting | contract_audited | cold_read_audited | manuscript_validated | integration_previewed | integrating | published | blocked | reopened
retain_mode: full | summary
target_files:
  - <path>
---
# 目标
# 授权范围
# 非目标
# 当前阶段
```

## 2. BRIEF.md

```md
# 学习目标
- 可观察表现：
# 目标材料
# 当前真实问题
# 已有证据
# 非目标
# 可能需要用户决定
```

## 3. DOMAIN_MODEL.md

```md
# 已实际读取
# 知识单元
# Formal dependencies
# Explanatory dependencies
# Motivational relations
# Reference relations
# Explanatory premise inventory
| premise_id | statement | supports_claims | source_anchor | verification |
# Canonical detail inventory
| detail_id | topic | canonical_owner | available_depth | stable_anchor | local_restatement_allowed | notes |
# 约定与边界
# 缺失与冲突
# 可供设计使用的结论
```

## 4. SOURCE_PACKET.md

```md
# 来源范围
# 术语与约定
# 公式、图表、定理和局部计算锚点
# 禁止补猜
```

## 5. LEARNER_SNAPSHOT.md

```md
---
learner_revision: <n>
---
# 当前目标
# Faceted capabilities
| capability_id | subject | facet | evidence_state | scope | evidence | confidence | risk_flags |
# 可以直接使用
# 不得直接假设
# 近期真实问题
# 可能改变路线的不确定项
```

## 6. DIDACTIC_DESIGN.md

```md
---
design_revision: <n>
based_on_learner_revision: <n>
---
# 目标表现
# 文件决策
# Units
## U01
- entry_capabilities:
- exit_capability:
- why_now:
- primary_pattern:
### Phases
### Concept action ledger
### Definition cards
### Explanation claim ledger
| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | closure_deadline | source_anchor | first_allowed_phase |
### Depth and placement ledger
| item_id | capability_or_claim | centrality | explanation_depth | placement | closure_deadline | mainline_cost | canonical_detail | duplication_rationale |
### Mainline contract
- main_question:
- mainline_result:
- supporting_details:
- return_to_mainline:
- latency_budget:
- optional_skip_test:
- proportionality_rationale:
### Opening contract
### Language contract
### Math and sources
### Reader card
# 拆分与整合决定
# 需要用户决定
```

## 7. DESIGN_AUDIT.md

```md
---
status: pass | changes_required | blocked
reviewed_design_revision: <n>
---
# Findings
# 结论
```

## 8. PACKETS/Uxx.md

```md
---
unit: Uxx
note_type:
entry_mode:
target_file:
draft_strategy:
compiled_from_design_revision:
---
# Reader entry capabilities
# Exit capability
# Phase sequence
# Faceted concept actions
# Definition instructions
# Explanation claims and closure deadlines
# Depth and placement
# Mainline contract
# Notation and load budget
# Required mathematics and examples
# Source excerpts/anchors
# Language contract
# Opening and transition contract
# Link policy
# Forbidden language/topics
# Packet preflight
```

## 9. READER_CARDS/Uxx.md

```md
---
unit: Uxx
---
# Reading situation
# Assumed entry capabilities
# Explicitly not assumed
# Expected exit capability
# Language register
```

## 10. DRAFTS/Uxx.md

只保存读者正文或替换片段。

## 11. CONTRACT_AUDIT.md

```md
---
status: pass | changes_required | blocked
reviewed_draft_revision: <n>
---
# Findings
# 结论
```

## 12. COLD_READ_AUDIT.md

```md
---
status: pass | changes_required | blocked
reviewed_draft_revision: <n>
---
# Reader trace
# Mainline latency
# Explanation proportionality
# Optional skip test
# Findings
# 结论
```

## 13. MANUSCRIPT_VERDICT.md

```md
---
status: pass | changes_required | blocked
contract_audit_status: pass | changes_required | blocked
cold_read_audit_status: pass | changes_required | blocked
reviewed_draft_revision: <n>
---
# 合并结论
# 返修路由
```

## 14. INTEGRATION_PREVIEW.md

```md
---
status: ready | changes_required | blocked
reviewed_draft_revision: <n>
---
# Target placement
# Replacement / deletion range
# Assembled reading flow
# Local bridge and links
# Duplication and ownership check
# Frontmatter
# Index / canonical impact
# Repository checks
# Required return route
```

## 15. INTEGRATION_REPORT.md

记录实际修改、preview 一致性、links、frontmatter、index/canonical、diff 与未解决事项。

## 16. AUTHORING_SUMMARY.md

记录目标、最终状态转移、关键设计、来源边界、审查与保留反馈。
