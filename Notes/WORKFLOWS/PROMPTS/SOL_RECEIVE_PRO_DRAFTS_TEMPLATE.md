# Sol Receive Pro Drafts Prompt Template

继续任务 `<task-id>`。当前角色是 Codex Sol：Pro draft 接收者、Mechanical Editor、Assembler 和 Contract Auditor。

我将附加以下 ChatGPT Pro artifact：

```text
<artifact-list>
```

它们基于：

```text
repository: <repository>
branch: <branch>
commit: <commit>
request: <request-path>
request_sha256: <request-sha256>
```

请严格执行：

1. 读取 Notes v6.1 的 handoff、Git、math、hybrid-drafting 与 contract-audit 合同。
2. 将附件原样保存到 request 指定的 `PRO_DRAFTS/` 路径，不改写 Pro prose。
3. 核对 metadata 和文件完整性。
4. 运行 Obsidian math linter。若失败，生成带行号的 Pro revision request；不得静默转换 delimiter。
5. 按 `author_mode` 填充机械插槽，只插入已验证内容。
6. 若仍有下一 Pro draft batch，生成下一 request；否则生成 `ASSEMBLY_MAP.md`、`ASSEMBLED_DRAFT.md`、`MATH_RENDER_AUDIT.md` 和 `SOL_CONTRACT_AUDIT.md`。
7. Contract pass 后生成 `PRO_REVIEW_CARD.md` 与 `PRO_REQUESTS/FINAL-REVIEW.md`。
8. 更新 `TASK.md` 与 `AUTOMATION_LOG.md`。
9. 自动 commit/push。
10. push 成功后输出下一条可直接复制给 ChatGPT Pro 的完整提示词。
11. 不修改正式笔记，除非当前已经处于获授权 integration 阶段。
