# Notes/WORKFLOWS/integration-contract.md

Repository Integrator 由 Codex Sol 承担。

## 1. 前提

- Pro review、`MANUSCRIPT_VERDICT.md` 与 ready `INTEGRATION_PREVIEW.md` 已先在任务分支完成独立 commit/push checkpoint；
- `MANUSCRIPT_VERDICT.md: pass`；
- `INTEGRATION_PREVIEW.md: ready`；
- task 已授权 formal integration 或用户另行授权；
- 在 preview checkpoint push 后重新 fetch，并确认 target blobs、assembled hash、Pro draft hashes 与 preview 一致；
- `MATH_RENDER_AUDIT.md: pass`。

## 2. 执行

- 严格按 Preview 写入；
- 不修改已通过 reader-visible text；
- 只执行授权的机械插入、删除、links、frontmatter、index/canonical；
- 不顺手格式化其它段落；
- 公式保持 `$` / `$$`；
- 无法 exact assemble 时立即停止。

## 3. Status

只有 whole-note Pro review 覆盖整篇且 exact integration 成功，才可写：

```yaml
status: reviewed
```

Partial scope 使用 `partially-reviewed` 或 `draft`，并记录 `review_scope`。

## 4. 自动 commit/push

Integration 完成后：

1. 对正式目标运行 `check_obsidian_math.py`；
2. 运行 assembled slice hash、links、anchors、index/canonical 和 `git diff --check`；
3. 只暂存 Preview allowlist；
4. commit `notes(<task-id>): integrate reviewed manuscript`；
5. push 到任务分支；
6. 生成 `INTEGRATION_REPORT.md` 与 `AUTHORING_SUMMARY.md`；
7. 若报告文件形成第二次变更，单独 commit/push；
8. 不合并主分支。

## 5. 输出

最终回执包含 branch、commit、正式 diff、数学格式、链接、status 和下一步唯一动作：用户决定是否合并任务分支。
