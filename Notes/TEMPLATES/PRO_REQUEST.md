---
task_id: <task-id>
request_id: R01
request_type: create | rewrite | local-rewrite
route: pro-write | pro-write-review
output_mode: full-file
review_policy: none | fresh-pro-review
binding_nonce: <random-secret-not-copied-into-browser-prompt>
response_token: <random-secret-not-copied-into-browser-prompt>
target_files:
  - <path>
---

# 用户目标

用可观察的能力描述读者最终应能做什么。

# 当前真实读者反馈

保留用户的实际问题，不把它改写成知识库维护目标。

# Reader assumptions

## 可以直接依赖

## 不能直接依赖

仓库存在相关笔记不代表读者已经掌握。

# 必须读取

- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- <目标文件>
- <必要上游、下游和来源>

# 来源与数学边界

- 哪些事实可以采用；
- 哪些尚未核验；
- 哪些论文特例不能一般化；
- 哪些结论不得补猜。

# 写作权限

## 允许

## 禁止

涉及删除、移动、拆分、合并或重命名正式文件时，返回 `DECISION_REQUIRED`，不要自行执行。

# 写作要求

- 内部自行完成教学规划；
- 直接输出完整、可替换的目标 Markdown；
- 不输出单独的学习路径、设计稿或审查表；
- 使用自然中文教材语体；
- 复杂推导自行选择合适的整体图、proof map、worked example 或逐步构造；
- 遵守 Obsidian `$` / `$$`。

# 完成标准

# 输出协议

严格按照 `Notes/PRO_OUTPUT_PROTOCOL.md`。只输出 allowlist 中的完整文件。
