# Notes/WORKFLOWS/pro-design.md

Lead Didactic Architect 由 ChatGPT Pro 承担，输出 `PRO_DESIGN.md`。

## 1. 输入

Pro 实际读取 Sol request 指定的 remote snapshot、handoff、Brief、Domain/Source、Learner、coverage/audit、目标文件和必要 owner/source。

Sol 的 unit boundary 只是勘察假设，不是待批准答案。

## 2. 输出 frontmatter

```yaml
---
task_id:
role: lead-didactic-architect
based_on_repository:
based_on_branch:
based_on_commit:
based_on_request_path:
based_on_request_sha256:
math_profile: obsidian-dollar-v1
status: ready_for_sol_validation | needs_source | user_decision_required
---
```

## 3. 正文结构

```text
# Note-level contract
# Whole-note mainline
# Final unit map
# Learner progression
# Unit designs
# Optional and conditional routes
# Author allocation
# File / ownership decisions
# Source requirements and uncertainty
# Whole-note acceptance criteria
# User decisions
```

## 4. Unit 要求

每个 unit 至少给出：

- semantic scope；
- entry / exit capability；
- why now / main question；
- primary teaching pattern；
- explanation depth 与 placement；
- transition in / out；
- core、optional、conditional_optional 或 paper_adapter；
- source requirements；
- `author_mode`；
- file action。

## 5. 作者分配

以下默认 `pro_full`：

- 复杂对象首次引入；
- 用户曾报告失败的部分；
- 复杂证明和长推导；
- unit 过渡与 whole-note mainline；
- general/source-specific 边界；
- explanation depth 仍需教学判断的内容。

表格、来源列表和确定的记号 crosswalk 可分给 Sol，但 framing 仍由 Pro 决定。

## 6. 粒度

Design 不写逐句脚本。它给出问题链、数学或证明地图、解释深度、误解边界和关键过渡。高风险公式可给精确等式链，但不把设计退化成 Sol 的逐句 checklist。

## 7. 数学格式

`PRO_DESIGN.md` 中所有公式也使用 `$` 与 `$$`。不得使用 `\(...\)` 或 `\[...\]`，不得输出 JSON 转义 Markdown。

## 8. Pro 回复合同

Pro 完成后必须：

1. 生成可下载的 `PRO_DESIGN.md`；
2. 报告 based-on branch/commit/request hash；
3. 不修改 GitHub 仓库；
4. 在回复末尾按 `PROMPTS/SOL_RECEIVE_PRO_DESIGN_TEMPLATE.md` 输出完整 `NEXT_SOL_PROMPT`。

下一位只能是 Codex Sol。Pro 不要求用户审批 technical unit map。
