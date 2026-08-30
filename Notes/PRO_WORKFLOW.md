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

异常：`PERMISSION_REQUIRED`、`NEEDS_CONTEXT`、`DECISION_REQUIRED`、`CHECK_FAILED`、`BLOCKED`。

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
3. 比较完整候选和旧文件；
4. 复制到目标；
5. 再运行数学检查和 `git diff --check`；
6. 生成或更新 `APPLY_REPORT.md`；
7. 显式暂存目标和任务报告；
8. commit/push；
9. 成功后删除临时原始响应。

Codex不得对 Pro 正文做教学性润色。

## 8. Pro 的其它状态

- `NEEDS_CONTEXT`：将消息保存到 `FAILURES/`，补充请求后重新 checkpoint；
- `DECISION_REQUIRED`：只有文件结构、互斥路线或范围变化时暂停用户；
- `BLOCKED` / `BINDING_FAILED`：停止；
- 输出截断或数学格式失败：在同一 Pro chat 中要求重发完整响应，不应用部分文件。

## 9. 自动 R02

当 `review_policy: fresh`：

1. R01 应用 commit/push 成功后，Codex自动打开新的 Pro chat；
2. 使用初始 checkpoint 已创建的 `REVIEW_REQUEST.md`，但 Browser 提示绑定最新应用 commit；
3. 不询问用户是否发送 R02；
4. Reviewer从头读取最新完整目标文件；
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
