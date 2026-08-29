# Notes/WORKFLOWS/git-automation.md

本文件规定 Codex Sol 的自动 worktree、commit 和 push 行为。

## 1. Task automation schema

`TASK.md` 使用：

```yaml
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
```

## 2. 分支与 worktree

- 优先在隔离 worktree 中工作，不触碰脏 `main`；
- 任务分支必须与 `task_branch` 一致；
- 禁止直接向 `main`、`master` 或受保护分支 push；
- 禁止 force push、history rewrite 和未经授权的 rebase；
- 已有远程任务分支时先 fetch 并确认没有分叉。

## 3. Commit 前置检查

每个 Sol 阶段结束时：

1. 确认当前分支和 worktree；
2. 列出 `git status --short`；
3. 确认修改只在本阶段 allowlist；
4. 对 reader-visible Markdown 运行 Obsidian math linter；
5. 运行 `git diff --check`；
6. 运行阶段要求的来源、hash、链接或装配检查；
7. 使用 `git add -- <explicit paths>`，不得使用 `git add -A`；
8. 再次核对 staged diff；
9. commit；
10. `git push -u <remote> HEAD`；
11. 获取 pushed commit；
12. 只有此时才输出下一模型提示词。

## 4. Commit message

建议：

```text
notes(<task-id>): map sources and prepare Pro design handoff
notes(<task-id>): validate Pro design and prepare draft handoff
notes(<task-id>): ingest Pro drafts and assemble whole note
notes(<task-id>): record Pro final review and prepare integration
notes(<task-id>): integrate reviewed manuscript
```

修订可用：

```text
notes(<task-id>): request Pro design revision
notes(<task-id>): request Pro draft revision
```

## 5. Stage allowlist

### Mapping / Pro handoff

只允许任务目录及必要的新 task branch metadata。

### Pro artifact ingestion

只允许任务目录；除非当前阶段明确授权，不修改正式笔记。

### Integration

只允许 Preview 明确列出的正式文件、任务目录，以及获授权的 index/canonical 文件。

## 6. Push 失败

push 失败时：

- 状态保持或改为 `awaiting_remote_sync`；
- 不输出 Pro request prompt；
- 不声称 remote 可读；
- 报告失败命令、stderr 和安全的重试步骤；
- 不改用 force push。

## 7. 自动 integration 限制

`auto_integrate_after_pro_pass: true` 只授权在任务分支中按 ready preview 写入。以下任一仍需用户决定：

- 删除、移动、拆分、合并或重命名正式文件；
- 新建长期正式 note；
- 改变 canonical ownership；
- 扩大目标文件集合；
- source conflict；
- 合并到主分支。

## 8. 最终交付

Integration commit/push 后输出：

- branch；
- commit；
- 修改文件；
- 数学格式与 `git diff --check` 结果；
- 是否创建 PR；
- 下一步唯一动作：由用户检查分支并决定是否合并。
