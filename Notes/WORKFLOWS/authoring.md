# Notes/WORKFLOWS/authoring.md

本文件规定 Notes v6.1 的混合主流程。模型分工见 `../MODEL_ROUTING.md`，跨模型接口见 `handoff-protocol.md`，Git 写入见 `git-automation.md`。

## 1. 状态机

```text
brief_ready
→ sol_mapped
→ whole_note_audited             # whole-note / legacy 任务
→ awaiting_pro_design            # Sol 已 commit/push 并输出 Pro prompt
→ pro_design_ready               # Sol 已接收 Pro artifact
→ sol_design_validated
→ awaiting_pro_drafts            # Sol 已 commit/push 并输出 Pro prompt
→ drafts_ready                   # Sol 已接收并验证 Pro drafts
→ assembled
→ sol_contract_validated
→ awaiting_pro_final_review       # Sol 已 commit/push 并输出 Pro prompt
→ pro_final_reviewed              # Sol 已接收 Pro final review
→ integration_previewed
→ integrated
→ published_branch
```

任意阶段可进入 `blocked`；发布后可因真实读者反馈进入 `reopened`。

## 2. Route

### `sol-only`

只处理不改变读者理解路径的机械任务。Sol 可以自动 commit/push，但不得顺便重写概念正文。

### `hybrid-local`

Sol mapping → Pro design/author → Sol validation/assembly → 新 Pro 会话 final review → Sol integration。

小型 local task 可以让 Pro 在同一次输出中给出 design 与 draft，但最终 review 必须是新 Pro 会话。

### `hybrid-whole-note`

```text
Sol mapping + whole-note coverage
→ Sol commit/push + Pro Architecture Prompt
→ Pro whole-note architecture + Next Sol Prompt
→ Sol source/repository validation
→ Sol commit/push + Pro Draft Prompt
→ Pro core drafts + Next Sol Prompt
→ Sol mechanical content + assembly + contract audit
→ Sol commit/push + Pro Final Review Prompt
→ fresh Pro whole-note review + Next Sol Prompt
→ Sol preview / integration / commit / push
```

Coverage audit 结束后不得要求用户批准 technical unit boundaries；下一位必须是 Pro Architect。

## 3. Handoff invariant

每次跨模型 handoff 均满足：

1. 当前模型完成并验证自己的 artifact；
2. Sol 阶段必须先通过数学格式检查；
3. Sol 更新 `TASK.md` 的状态和 `next_actor`；
4. Sol 只暂存 allowlist；
5. Sol commit 并 push；
6. Sol 获取精确 commit；
7. 当前模型输出下一模型的完整提示词；
8. 下一模型 artifact 记录它依据的 commit 和 request hash。

push 失败时不得进入 `awaiting_pro_*`。

## 4. 三个 Pro gate

### Architecture

Sol 生成并推送 `PRO_REQUESTS/ARCHITECTURE.md`。Pro 输出 `PRO_DESIGN.md` 和精确 `NEXT_SOL_PROMPT`。

### Authoring

Sol 验证设计后生成并推送一个或多个 `PRO_REQUESTS/DRAFT-BATCH-xx.md`。Pro 输出 `PRO_DRAFTS/` artifact 和精确 `NEXT_SOL_PROMPT`。

### Whole-note review

Sol 组装并通过合同审查后生成并推送 `PRO_REQUESTS/FINAL-REVIEW.md`。新的 Pro 会话输出 `PRO_FINAL_REVIEW.md` 和精确 `NEXT_SOL_PROMPT`。

## 5. Sol 自动 Git

当 `TASK.md` 授权自动化时，以下 Sol 阶段结束后自动 commit/push：

- mapping / coverage / Pro handoff；
- Pro design 接收与 Sol validation；
- Pro draft 接收、assembly 与 contract audit；
- Pro final review 接收与 integration preview；
- 正式 integration。

具体 allowlist、分支和失败策略见 `git-automation.md`。

## 6. 数学渲染 gate

以下内容在 commit 前必须通过 `check_obsidian_math.py`：

- `PRO_DRAFTS/`；
- `SOL_DRAFTS/`；
- `ASSEMBLED_DRAFT.md`；
- 正式目标文件的 reader-visible diff。

Pro artifact 使用错误 delimiter 时，Sol 不静默转换，而是生成精确 revision request 并交回 Pro。

## 7. 自动返修

- Sol validation 发现来源或数学问题：生成 revision request，commit/push，再输出 Pro 修订提示词。
- Pro final review 为 `changes_required`：Sol 按 route 生成 design 或 draft revision request，commit/push，再输出 Pro 提示词。
- 同一 required finding 连续三轮未关闭时进入 `blocked`。

## 8. 自动 integration

若同时满足：

- Pro final review 与 Sol contract audit 审查同一 assembled hash 并均为 pass；
- Integration Preview 为 ready；
- `TASK.automation.auto_integrate_after_pro_pass: true`；
- 没有删除、移动、拆分、合并、改名或其它用户级结构决定；
- 目标 blob、draft hash 和 remote branch 未漂移；

Sol 可以在同一次调用中执行正式 integration、检查、commit 和 push，无需再要求用户批准。

自动 integration 只发生在任务分支。合并到主分支始终由用户决定。

## 9. 用户只处理什么

用户负责：真实目标、真实阅读反馈、文件级结构决定、把提示词和 artifact 在两个模型之间转交、最终是否合并任务分支。

用户不负责 technical unit map、learner facet、depth、普通返修或每次 commit/push。
