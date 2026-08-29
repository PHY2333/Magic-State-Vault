# Sol Receive Pro Final Review Prompt Template

继续任务 `<task-id>`。当前角色是 Codex Sol：Pro whole-note review 接收者、Gatekeeper 和 Repository Integrator。

我将附加 ChatGPT Pro 生成的 `PRO_FINAL_REVIEW.md`。它审查：

```text
assembled_sha256: <assembled-sha256>
repository: <repository>
branch: <branch>
commit: <commit>
request: <request-path>
request_sha256: <request-sha256>
```

请严格执行：

1. 原样保存附件，不改写 Pro review。
2. 核对 task、fresh-session 标记、branch/commit/request 和 assembled SHA-256。
3. 生成或更新 `MANUSCRIPT_VERDICT.md`。
4. 若 Pro status 为 `changes_required`：按 finding route 生成下一份 Pro revision request，更新 `TASK.md` 与 `AUTOMATION_LOG.md`，自动 commit/push；push 成功后输出精确 Pro prompt，并停止。
5. 若 Pro status 为 `pass`：生成 read-only `INTEGRATION_PREVIEW.md`，并核对是否存在用户级结构决定。
6. 对 Pro review、verdict、preview 和相关任务产物运行元数据、hash、Obsidian math 与 `git diff --check` 检查。
7. **先完成 review/preview checkpoint**：只暂存任务目录中的本阶段 allowlist，commit 并 push；获取该 pushed commit。不得把尚未锁定的 preview 与正式正文写入混在同一个 commit 中。
8. 若 Preview ready、`TASK.automation.auto_integrate_after_pro_pass: true`，且没有用户级结构决定：在上述 push 后重新 fetch/锁定任务分支、目标 blob、assembled hash 和 preview，按 `integration-contract.md` 自动整合正式文件。
9. 对 assembled draft 和正式目标运行 Obsidian math linter、hash、links、anchors 与 `git diff --check`。
10. 生成或更新 `TASK.md`、`AUTOMATION_LOG.md`、`INTEGRATION_REPORT.md` 和 `AUTHORING_SUMMARY.md`，使其准确记录本次正式写入、检查结果和目标 blob。
11. **再完成 integration checkpoint**：只暂存 Preview allowlist 内的正式文件与本次 integration 产物，commit 并 push 到任务分支；不得合并主分支。若因提交后才能得到最终 commit hash 而需要补写报告，只允许再做一个纯报告 commit/push。
12. 最终只输出任务分支、各 pushed commit、检查结果和“由用户决定是否合并任务分支”。

若第 7 步 push 失败，不得进入正式 integration。若任一 target/hash 漂移，立即停止，不得近似执行。
