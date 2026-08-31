# Notes/PRO_WORKFLOW.md

Framework: Notes Pro-First 1.1

## 1. 任务目录

```text
Notes/WORKING/pro-tasks/<task-id>/
├── TASK.md
├── PRO_REQUEST.md
├── REVIEW_REQUEST.md      # 仅需要 R02 时
├── APPLY_REPORT.md
├── FINAL_REPORT.md
└── FAILURES/              # 仅失败时保留原始响应
```

成功响应默认只在本地临时目录中存在，解析和应用完成后删除。Git 提交和报告构成最小审计。

## 2. 路线

- `codex-only`
- `pro-write`
- `pro-write-review`

普通概念笔记默认 `pro-write + review_policy: internal`。整篇、复杂证明和已发生教学失败的任务使用 `pro-write-review`。

## 3. 简化状态

```text
PREPARE
→ CHECKPOINT_PUSHED
→ R01_RUNNING
→ R01_APPLIED
→ R02_RUNNING        # 仅需要 R02 时
→ DONE
```

异常：`PERMISSION_REQUIRED`、`NEEDS_CONTEXT`、`DECISION_REQUIRED`、`CHECK_FAILED`、`BLOCKED`。

捕获、解析、格式规范化和 staging 是内部步骤，不单独成为需要用户感知的状态。

## 4. 初始 checkpoint

Codex一次性生成：

- `TASK.md`；
- `PRO_REQUEST.md`；
- 需要 R02 时同时生成 `REVIEW_REQUEST.md`。

两个 request 各有不同的隐藏 `binding_id`。Codex显式暂存这些文件，commit 并 push。

## 5. 自动 R01

push 成功后，Codex根据 Browser 模板发送 R01，不询问用户是否继续。

Codex等待 `END_RESPONSE::<binding_id>`。捕获内容先保存到：

```text
.tmp/pro-responses/<task-id>/R01.raw.md
```

再解析，不先摘要。

## 6. Fast parse

运行 `parse_pro_response.py`，只把文件写入 staging，不直接覆盖正式文件。

Parser 只负责协议、路径、binding 和完整性，不判断正文质量或数学格式。

## 7. Codex 上下文格式规范化

对 staging 中的每个 reader-visible Markdown：

1. 运行 `check_obsidian_math.py`；
2. 若通过，继续；
3. 若失败，Codex读取完整段落、公式和必要来源，判断错误属于：
   - Markdown / Obsidian 外层格式；
   - 可唯一确定的 LaTeX 语法；
   - 数学内容或多义问题；
4. 前两类由 Codex直接编辑 staging；
5. 第三类停止并返回 Pro 或来源核验；
6. Codex复读修复前后句子，确认数学陈述、正文措辞和内容顺序没有被改变；
7. 再次运行 `check_obsidian_math.py`；
8. 记录简洁的格式修复摘要。

不使用规则式 Python auto-fixer。现有 checker 只提供错误位置，实际修复由 Codex结合上下文完成。

纯格式修复不启动新的 Pro 轮次，也不询问用户。

## 8. 应用 R01

`COMPLETE` 时：

1. 检查 allowlist；
2. 完成第 7 节的格式规范化；
3. 比较完整候选和旧文件；
4. 复制到目标；
5. 对目标再次运行 Obsidian 数学检查；
6. 运行 `git diff --check`；
7. 生成或更新 `APPLY_REPORT.md`；
8. 显式暂存目标和任务报告；
9. commit/push；
10. 成功后删除临时原始响应。

Codex不得借格式修复重写 Pro 的教学表达、数学论证或段落顺序。

## 9. 需要返回 Pro 的情况

- 输出截断、文件块不完整、binding 错误或路径越权；
- 公式或正文存在两个以上合理解释；
- 需要增加、删除或改变数学 token 才能形成确定命题；
- 正文与公式不一致；
- 来源或数学条件冲突；
- Codex完成上下文格式修复后仍无法通过检查。

仅有数学分隔符、块公式布局、callout 引用、明显转义或其它可唯一确定的格式问题时，不返回 Pro。

## 10. R02

R02 审查实质内容。纯格式缺陷不应单独触发整篇重写。

若 Reviewer 返回 `COMPLETE`：

1. 仍先提取到 staging；
2. 执行相同的 Codex 上下文格式规范化；
3. 纯格式修复不触发 R03；
4. 检查、应用并 commit/push。

若 Reviewer 返回 `REVIEW_PASS`，Codex仍对当前目标执行一次最终 Obsidian 数学检查；发现纯格式问题时直接修复、记录并提交，不重新调用 Pro。

## 11. Pro 的其它状态

- `NEEDS_CONTEXT`：保存到 `FAILURES/`，补充请求后重新 checkpoint；
- `DECISION_REQUIRED`：只有文件结构、互斥路线或范围变化时暂停用户；
- `BLOCKED` / `BINDING_FAILED`：停止；
- 纯格式问题：Codex处理；
- 数学或语义不明确：返回 Pro。

## 12. Standing authorization

`TASK.md` 中 `run_to_completion: true` 表示用户已授权任务分支内的 R01、R02、格式规范化、commit 和 push。只有 `stop_only_on` 命中时暂停。

## 13. 最小保留

成功任务保留：

- `TASK.md`
- `PRO_REQUEST.md`
- `REVIEW_REQUEST.md`（若有）
- `APPLY_REPORT.md`
- `FINAL_REPORT.md`
- Git commits

原始响应默认 `errors-only`。

## 14. 完成

`FINAL_REPORT.md` 记录分支、各提交、Pro 状态、Codex格式规范化、数学检查和下一步。Codex push 完成后停止；不自动合并 main。
