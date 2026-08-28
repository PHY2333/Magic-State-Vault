# Notes/WORKFLOWS/task-artifacts.md

本文件是 Notes v4 任务产物模板的唯一来源。其它 contract 只引用，不复制完整模板。

## 1. TASK.md

```md
---
task_id: <id>
status: brief_ready | mapped | learner_ready | designed | design_validated | packet_ready | drafting | contract_audited | cold_read_audited | manuscript_validated | integrating | published | blocked | reopened
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
## K01
- formal_statement:
- conditions:
- canonical_owner:
- source_anchors:
- verification:

# Formal dependencies
| dependent | requires | reason |

# Explanatory dependencies
| target_explanation | requires_reader_capability | reason |

# Motivational relations
| predecessor_problem_or_result | motivates | reason |

# Reference relations
| knowledge_unit | owner | owned_scope |

# Explanatory premise inventory
| premise_id | statement | supports_claims | source_anchor | verification |

# 约定与边界
# 缺失与冲突
# 可供设计使用的结论
```

## 4. SOURCE_PACKET.md

```md
# 来源范围
## S01
- source:
- version:
- location:
- classification:
- supported_claim:
- unsupported_or_missing:
- intended_use:

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
| file | note_type | entry_mode | draft_strategy | action | reason |

# Units
## U01
- entry_capabilities:
- exit_capability:
- why_now:
- primary_pattern:
- supporting_pattern:

### Phases
#### P1
- cognitive_job:
- new_entities:
- new_relations:
- new_notation:
- holding_set:
- consolidation:

### Concept action ledger
| capability_id | subject | facet | evidence_state | action | first_allowed_phase | local_treatment |

### Definition cards

### Explanation claim ledger
| claim_id | reader_surface_claim | claim_type | purpose | capability_dependencies | claim_dependencies | closure_method | source_anchor | first_allowed_phase |

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
1. severity:
   - location:
   - issue:
   - impact:
   - return_to:
   - suggested_fix:
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
# Explanation claims
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

只保存读者正文或替换片段，不放审查语言。

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
# Findings
# 结论
```

## 13. MANUSCRIPT_VERDICT.md

```md
---
status: pass | changes_required | blocked
contract_audit_status:
cold_read_audit_status:
reviewed_draft_revision:
---
# 合并结论
# 返修路由
```

## 14. INTEGRATION_REPORT.md

```md
# 修改文件
# Draft 到正式位置
# Frontmatter
# Links
# Index 与 canonical
# Diff 检查
# 未解决事项
```

## 15. AUTHORING_SUMMARY.md

```md
# 任务目标
# 最终读者状态转移
# 采用的文件与教学决策
# 关键数学与来源边界
# 最终审查结论
# 保留的读者反馈
```
