# Notes/WORKFLOWS/pro-handoff.md

本文件规定 task-specific Pro request 的内容。通用提示词传递规则见 `handoff-protocol.md`。

## 1. Snapshot

每份 Pro request 必须列出：

```yaml
repository:
branch:
base_snapshot_commit:
target_blobs:
request_manifest_sha256:
math_profile: obsidian-dollar-v1
artifact_delivery: attachment
```

精确 pushed commit 由 Sol 在 push 后写入聊天提示词。Pro artifact 必须记录该 commit。

## 2. PRO_HANDOFF.md

必须包含：

- 用户真实学习目标和阅读反馈；
- task route 与当前状态；
- 已核对数学、来源和 convention；
- learner evidence 与不能假设的能力；
- whole-note coverage 和风险；
- canonical owner 与 source-specific 边界；
- Sol unit hypotheses，并标明“非最终设计”；
- 缺失来源和不可承诺事项；
- Pro 必须实际读取的最小路径；
- target blobs 与 request manifest；
- 期望 Pro artifact；
- Pro 完成后必须使用的 `NEXT_SOL_PROMPT` 模板。

Handoff 不得将维护判断改写成建议正文。

## 3. Request 文件

```text
PRO_REQUESTS/ARCHITECTURE.md
PRO_REQUESTS/DRAFT-BATCH-xx.md
PRO_REQUESTS/FINAL-REVIEW.md
PRO_REQUESTS/REVISION-xx.md
```

每份 request 必须可独立执行，包含：

- 角色；
- GitHub branch/commit 的运行时占位说明；
- 允许读取范围；
- 输出文件名；
- Obsidian math contract；
- artifact frontmatter；
- 精确的下一 Sol 提示词模板；
- 停止点。

## 4. Pro 输出保存

用户将 Pro artifact 附给 Sol并粘贴 `NEXT_SOL_PROMPT`。Sol只能：

1. 保存到约定路径；
2. 登记 hash；
3. 运行 math linter；
4. 验证 source/repository/task metadata；
5. 进入相应 Sol 阶段。

Sol不得在保存时优化 Pro 的教学结构或行文。
