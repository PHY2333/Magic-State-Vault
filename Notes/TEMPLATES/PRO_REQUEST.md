---
task_id: <task-id>
request_id: R01
request_type: create | rewrite | local-rewrite
route: pro-write | pro-write-review
output_mode: full-file
review_policy: none | internal | fresh
binding_id: <random-hidden-id>
target_files:
  - <path>
---

# 用户目标

用可观察的能力描述读者最终应能做什么。

# 当前真实读者反馈

保留实际问题，不改写成知识库维护目标。

# Reader assumptions

## 可以直接依赖

## 不能直接依赖

仓库存在相关笔记不代表读者已经掌握。

# 必须读取

- `Notes/WRITING_GUIDE.md`
- `Notes/OBSIDIAN_MATH.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- <目标文件>
- <必要上游、下游和来源>

# 来源与数学边界

- 可以采用的事实；
- 尚未核验的内容；
- 论文特例不能怎样一般化；
- 不得补猜的结论。

# 写作权限

## 允许

## 禁止

涉及删除、移动、拆分、合并或重命名正式文件时，返回 `DECISION_REQUIRED`。

# 写作要求

- 内部自行完成教学规划；
- 直接输出完整、可替换的目标 Markdown；
- 不输出单独的路径表、设计稿或审查表；
- 使用自然中文教材语体；
- 根据内容自行选择问题驱动、整体先行、逐步构造、worked example 或证明地图；
- 输出前从头复读全文一次；
- 严格使用 Obsidian `$` / `$$`；
- 严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。

# 完成标准
