# Notes/PRO_WORKFLOW.md

Framework: Notes Pro-First 1.0

## 1. 任务目录

```text
Notes/WORKING/pro-tasks/<task-id>/
├── TASK.md
├── PRO_REQUEST.md
├── REVIEW_REQUEST.md      # 仅 review_policy=fresh
├── APPLY_REPORT.md
├── FINAL_REPORT.md
└── FAILURES/              # 仅失败时保留原始响应
```

成功响应默认只在本地临时目录中存在，解析和应用完成后删除。Git 提交和报告构成最小审计。

## 2. 路线

- `codex-only`
- `pro-write`
- `pro-write-review`

普通概念笔记默认 `pro-write + review_policy: internal`。整篇、复杂证明和已发生教学失败的任务默认 `pro-write-review + review_policy: fresh`。

## 3. 简化状态

```text
PREPARE
→ CHECKPOINT_PUSHED
→ R01_RUNNING
→ R01_APPLIED
→ R02_RUNNING        # 仅 fresh
→ DONE
```

异常：`PERMISSION_REQUIRED`、`NEEDS_CONTEXT`、`DECISION_REQUIRED`、`CHECK_FAILED`、`BLOCKED`。其中数学格式的 `CHECK_FAILED` 只指修复需要语义判断、无法形成可审计的语义等价 diff，或机械修复后检查仍失败；首次发现可安全机械修复的格式问题不单独进入异常状态。

内部捕获、解析和临时 staging 不单独成为需要用户感知的状态。

## 4. 初始 checkpoint

Codex一次性生成：

- `TASK.md`；
- `PRO_REQUEST.md`；
- fresh review 时同时生成 `REVIEW_REQUEST.md`。

两个 request 各有不同的隐藏 `binding_id`。Codex显式暂存这些文件，commit 并 push。R02 不再需要单独创建 review-request checkpoint。

## 5. 自动 R01

push 成功后，Codex根据 `BROWSER_AUTHOR_PROMPT.md` 自动打开或复用 ChatGPT Pro 会话，不询问用户是否发送。

Browser 提示包含：repository、branch、checkpoint commit、request path 和 protocol path；不包含 `binding_id`。

Codex等待 `END_RESPONSE::<binding_id>`。捕获内容先保存到：

```text
.tmp/pro-responses/<task-id>/R01.raw.md
```

再解析，不先摘要。

## 6. Fast parse

运行：

```bash
python Notes/TOOLS/parse_pro_response.py \
  --input <R01.raw.md> \
  --output-dir <staging-dir> \
  --task-id <task-id> \
  --request-id R01 \
  --repository <owner/repo> \
  --branch <task-branch> \
  --commit <checkpoint-commit> \
  --binding-id <hidden-binding-id> \
  --allow-path <target> [--allow-path ...]
```

解析器只写 staging，不覆盖正式文件。

## 7. 应用 R01

`COMPLETE` 时：

1. 检查 allowlist；
2. 对 staging 运行 Obsidian 数学检查；
3. 若失败，先按下述“纯格式机械修复”规则分类；允许修复时只修改 staging，并重新运行检查；
4. 比较完整候选和旧文件；
5. 复制到目标；
6. 再运行数学检查和 `git diff --check`；
7. 生成或更新 `APPLY_REPORT.md`；
8. 显式暂存目标和任务报告；
9. commit/push；
10. 成功后删除临时原始响应；若发生过失败或 Codex 机械修复，则按审计保留规则处理原始响应。

Codex不得对 Pro 正文做教学性润色。

### 纯格式机械修复

Codex可以修复能够逐字符说明、且不改变数学语义或读者理解路径的问题，包括：

- 把仓库禁止的圆括号式、方括号式或同行块公式定界，规范为本仓库允许的行内或独立块定界格式；
- 修正已经确认由传输产生、且不会被解释为 LaTeX 换行的重复反斜杠，补上闭合位置唯一的定界符，以及调整 MathJax 所需的空白或换行；
- 在上下文已经明确同一对象时，把会触发检查器的记号改成等价规范记号，例如把已明确表示生成理想的 `(a)` 写成 `\langle a\rangle`。

Codex不得借此改变变量、上下标、运算符、箭头、等号或不等号、求和范围、量词、假设、结论、证明文字或章节结构。修复只能发生在 staging；原始 Pro 响应保持不变。`APPLY_REPORT.md` 必须记录文件、原文与修正、出现次数、判定为语义等价的依据、修复前后 SHA-256、最小 unified diff，以及修复前后的检查结果。若无法机械证明等价，要求 Pro 重发完整文件。

## 8. Pro 的其它状态

- `NEEDS_CONTEXT`：将消息保存到 `FAILURES/`，补充请求后重新 checkpoint；
- `DECISION_REQUIRED`：只有文件结构、互斥路线或范围变化时暂停用户；
- `BLOCKED` / `BINDING_FAILED`：停止；
- 输出截断：在同一 Pro chat 中要求重发完整响应，不应用部分文件；
- 数学格式失败：先执行“纯格式机械修复”分类。可安全修复时由 Codex 修复 staging 并留下审计记录；超出边界时要求 Pro 重发完整响应。重发后仍不能安全通过时停止。

## 9. 自动 R02

当 `review_policy: fresh`：

1. R01 应用 commit/push 成功后，Codex自动打开新的 Pro chat；
2. 使用初始 checkpoint 已创建的 `REVIEW_REQUEST.md`，但 Browser 提示绑定最新应用 commit；
3. 不询问用户是否发送 R02；
4. Reviewer从头读取最新完整目标文件；若 `APPLY_REPORT.md` 记录 R01 的 Codex 机械修复，同时核对其 diff 只改变格式而未改变数学或叙述语义；
5. 返回 `REVIEW_PASS` 或完整修正文件。

若返回修正文件，Codex按相同方式检查、应用并 commit/push。默认只进行一次 fresh review；Reviewer 返回的完整修正版视为审查后的最终稿，不再自动启动 R03。

## 10. Standing authorization

`TASK.md` 中 `run_to_completion: true` 表示用户已授权任务分支内的 R01、R02、commit 和 push。只有 `stop_only_on` 命中时暂停。

该授权不能绕过 Codex App 自身的 Browser host、登录或系统权限确认；这些属于 `PERMISSION_REQUIRED`。

## 11. 最小保留

成功任务保留：

- `TASK.md`
- `PRO_REQUEST.md`
- `REVIEW_REQUEST.md`（若有）
- `APPLY_REPORT.md`
- `FINAL_REPORT.md`
- Git commits

原始响应默认 `errors-only`。需要完整外部审计时，单个任务可设置 `audit_retention: full`。

## 12. 完成

`FINAL_REPORT.md` 记录分支、checkpoint/application/review commits、目标文件、Pro 状态、数学检查和下一步。Codex push 完成后停止；不自动合并 main。
