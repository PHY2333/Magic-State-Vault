# Notes/WORKFLOWS/integration-preview.md

Repository Fit Planner 由 Codex Sol 承担，只在 whole-note manuscript verdict pass 后生成只读预览。

## 1. 必须检查

- target placement、替换/删除范围和完整 assembled flow；
- 每个 reader-visible section 的 origin 与 review coverage；
- 不得含 `legacy-unreviewed` 或 `changes-required` 内容；
- local bridge、owner、links 和 optional route；
- 被删段落首次引入的概念，在后文首次再次出现时是否仍有本地落点或准确 owner link；
- heading、anchor、frontmatter、index、canonical；
- Pro drafts、assembled hash 和 math-render status；
- current target blobs 与 remote snapshot。

## 2. Whole-note status

- whole-note Pro review pass 且可精确保持 assembled text：可规划 `status: reviewed`；
- 只整合部分 units：只能 `draft` 或 `partially-reviewed`；
- Fit Planner 不得自行升级 status。

## 3. 不得静默改稿

Preview 可以规划机械插入、删除竞争文本、非承重链接和 frontmatter。若需要改变已通过正文、unit 顺序、解释深度、公式 delimiter 或过渡，返回 Pro Design / Pro Author 并重跑 gate。

## 4. 自动化

若 Preview 为 ready，且 `TASK.automation.auto_integrate_after_pro_pass: true`，并且没有用户级结构决定，Sol可以在同一次调用中：

1. 先把 Preview 与 Pro review artifact commit/push；
2. 重新锁定 remote 和 target blob；
3. 按 Preview 执行 formal integration；
4. 运行 math linter、链接和 diff 检查；
5. 再 commit/push integration。

## 5. 输出

```yaml
status: ready | changes_required | blocked
reviewed_assembled_sha256:
math_render_status:
auto_integration_eligible: true | false
formal_integration_authorized_by_task: true | false
```
