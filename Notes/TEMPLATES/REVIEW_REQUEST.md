---
task_id: <task-id>
request_id: R02
request_type: fresh-whole-file-review
binding_id: <new-random-hidden-id>
target_files:
  - <path>
---

# 审查目标

从头连续审查 Browser 提示所绑定的最新 GitHub commit 中的完整目标文件。不要依赖上一轮作者对自己的说明。

# 原始目标

见同任务的 `PRO_REQUEST.md`。

# 审查重点

- 整篇是否持续服务目标读者；
- 是否存在能力断崖或突然切回专家压缩；
- 复杂推导是否先给总体目标或证明地图；
- 定义和工具是否在合适时机出现；
- optional 内容是否真正可跳过；
- 一般理论、论文特例、参数支线和应用是否放置合理；
- 中文是否自然统一；
- 所有数学是否使用 Obsidian `$` 与 `$$`；
- 是否存在重复、竞争性解释、失效链接或维护者语言。

# 输出

全文通过则返回 `REVIEW_PASS`。需要修改则返回 `COMPLETE` 和完整修正文件，不只给建议。严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。
