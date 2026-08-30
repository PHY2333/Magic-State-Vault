---
task_id: <task-id>
request_id: R02
request_type: fresh-whole-file-review
binding_nonce: <new-random-secret>
response_token: <new-random-secret>
target_files:
  - <path>
---

# 审查目标

从头连续审查当前 GitHub checkpoint 中的完整目标文件。不要只核对上一轮要求是否执行。

# 原始目标

见同任务的 `PRO_REQUEST.md`。

# 审查重点

- 整篇是否持续服务目标读者；
- 是否有能力断崖或突然切回专家压缩；
- 复杂推导是否有总体目标或证明地图；
- 定义和工具是否在合适时机出现；
- optional 内容是否真的可跳过；
- 一般理论、论文特例、参数支线和应用是否放置合理；
- 中文是否自然统一；
- 数学是否全部使用 Obsidian `$` 与 `$$`；
- 是否存在重复、竞争性解释、失效链接或维护者语言。

# 输出

若全文通过，返回 `REVIEW_PASS`。

若需要修改，返回 `COMPLETE` 和完整修正文件。不要只给零散建议。

严格遵守 `Notes/PRO_OUTPUT_PROTOCOL.md`。
