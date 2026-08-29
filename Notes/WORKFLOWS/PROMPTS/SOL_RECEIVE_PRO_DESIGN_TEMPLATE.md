# Sol Receive Pro Design Prompt Template

继续任务 `<task-id>`。当前角色是 Codex Sol：Pro artifact 接收者与 Design Validator。

我将附加 ChatGPT Pro 生成的 `PRO_DESIGN.md`。它基于：

```text
repository: <repository>
branch: <branch>
commit: <commit>
request: <request-path>
request_sha256: <request-sha256>
```

请严格执行：

1. 读取 `Notes/AGENTS.md`、`handoff-protocol.md`、`git-automation.md`、`sol-design-validation.md` 和 `OBSIDIAN_MATH.md`。
2. 将附件原样保存到任务目录 `PRO_DESIGN.md`；不得润色或改写。
3. 核对 task、role、branch、commit、request path/hash。
4. 运行 `python Notes/TOOLS/check_obsidian_math.py <task-dir>/PRO_DESIGN.md`。
5. 生成 `SOL_DESIGN_VALIDATION.md`。
6. 若 pass：编译下一批 `PRO_REQUESTS/DRAFT-BATCH-xx.md`；若需要 Pro 修订：生成精确 `PRO_REVISION_REQUEST.md`。
7. 更新 `TASK.md` 和 `AUTOMATION_LOG.md`。
8. 按阶段 allowlist 自动 commit 并 push 到任务分支。
9. push 成功后输出下一条可直接复制给 ChatGPT Pro 的完整提示词。
10. 不修改正式笔记，不替 Pro 重做教学设计。
