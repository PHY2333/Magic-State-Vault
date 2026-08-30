# Notes/PRO_WORKFLOW.md

## 1. 任务目录

```text
Notes/WORKING/pro-tasks/<task-id>/
├── TASK.md
├── PRO_REQUEST.md
├── PRO_OUTPUTS/
│   └── R01/
│       ├── response.raw.md
│       ├── response.manifest.json
│       └── extracted/
├── APPLY_REPORT.md
├── REVIEW_REQUEST.md
├── PRO_OUTPUTS/R02/
└── FINAL_REPORT.md
```

只有复杂路线需要 review 文件。

## 2. 状态

```text
request-prepared
→ checkpoint-pushed
→ pro-authoring
→ author-output-captured
→ author-applied-pushed
→ review-request-pushed       # 仅 pro-write-review
→ pro-review
→ review-output-captured
→ review-applied-pushed
→ done
```

异常状态：`needs-context`、`decision-required`、`binding-failed`、`blocked`。

## 3. 请求准备

Codex 生成 `TASK.md` 和 `PRO_REQUEST.md`。请求只包含：

- 真实学习目标；
- 具体读者反馈；
- 可以直接假设的知识；
- 不能直接假设的知识；
- 必须读取的文件；
- 来源边界；
- 允许和禁止修改；
- 输出完整文件的要求；
- 随机 `binding_nonce` 和 `response_token`。

不要在请求中预先替 Pro 设计数千行教学路线。

## 4. GitHub checkpoint

Codex：

```bash
git status --short
git add -- <TASK.md> <PRO_REQUEST.md>
git commit -m "notes(<task-id>): prepare GPT Pro request"
git push -u origin HEAD
```

然后计算：

```bash
sha256sum <PRO_REQUEST.md>
git rev-parse HEAD
```

请求文件内不写自引用的 commit 或自身 SHA-256；commit 和 request SHA 由 Browser 提示传给 Pro。

## 5. Browser authoring

Codex 使用 `TEMPLATES/BROWSER_AUTHOR_PROMPT.md`，在 ChatGPT 中选择 Pro 模式并使用 GitHub App。

`binding_nonce` 和 `response_token` 的值不能出现在 Browser 提示中。Pro 必须从请求文件读取并返回。

Codex等待完整 `END_RESPONSE::<response_token>`。看不到结束标记时，要求 Pro重新输出完整响应，不应用截断内容。

## 6. 捕获与解析

Codex先将完整回复保存为：

```text
PRO_OUTPUTS/R01/response.raw.md
```

再运行：

```bash
python Notes/TOOLS/parse_pro_response.py \
  --input <response.raw.md> \
  --output-dir <PRO_OUTPUTS/R01/extracted> \
  --manifest <PRO_OUTPUTS/R01/response.manifest.json> \
  --task-id <task-id> \
  --request-id R01 \
  --repository <owner/repo> \
  --branch <branch> \
  --commit <checkpoint-commit> \
  --request-sha256 <sha256> \
  --binding-nonce <nonce> \
  --response-token <token> \
  --allow-path <target-file> [--allow-path ...]
```

解析器只写 staging，不直接覆盖仓库。

## 7. 应用

当状态为 `COMPLETE`：

1. 对 extracted files运行 Obsidian 数学检查；
2. 比较旧文件和完整候选；
3. 确认没有未授权路径；
4. 将 extracted file复制到目标路径；
5. 再次运行数学检查和 `git diff --check`；
6. 生成 `APPLY_REPORT.md`；
7. 显式暂存目标和任务审计文件；
8. commit/push。

Codex不对 Pro 正文做教学性润色。

## 8. 其它 Pro 状态

### `NEEDS_CONTEXT`

保存原始回复和 manifest，将 Pro 说明转成 `PRO_REQUEST` 的补充材料，生成新 request id，再 push 后重新调用同一 authoring chat。

### `DECISION_REQUIRED`

只在文件级不可逆操作、互斥路线或范围变化时暂停用户。

### `BLOCKED` / `BINDING_FAILED`

停止，不应用任何内容。

## 9. Fresh Pro review

`pro-write-review` 在第一次应用并 push 后生成 `REVIEW_REQUEST.md`，其目标是审查 GitHub 上完整、已经应用的文件，而不是上一轮聊天草稿。

使用新的 Pro chat 和新的 nonce/token。Reviewer 返回：

- `REVIEW_PASS`；或
- `COMPLETE`，包含完整修正文件；或
- `NEEDS_CONTEXT / DECISION_REQUIRED / BLOCKED`。

若返回完整修正文件，Codex按同样流程捕获、解析、检查、应用并 push。默认最多两轮 review。

## 10. 完成

最终 `FINAL_REPORT.md` 记录：

- 分支和 commits；
- request/response SHA-256；
- binding 结果；
- 修改文件；
- Obsidian 数学检查；
- fresh review 结果；
- 是否仍有 TODO；
- 下一步：用户决定是否合并任务分支。
