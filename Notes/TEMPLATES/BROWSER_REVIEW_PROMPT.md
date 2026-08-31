使用已连接的 GitHub App读取以下固定项目快照，并在一个全新的 ChatGPT Pro 会话中进行整篇审查。

repository: <owner/repo>
branch: <task-branch>
commit: <latest-applied-commit>
request_path: <REVIEW_REQUEST.md path>
protocol_path: Notes/PRO_OUTPUT_PROTOCOL.md

首先实际读取 request_path、protocol_path、同任务的 PRO_REQUEST.md、同任务的 APPLY_REPORT.md（若已存在），以及 request 中列出的完整目标文件。

从 request 文件读取 task_id、request_id 和 binding_id。本消息没有给出 binding_id 的值。绑定失败时不要猜测。

请从头连续审查最新 commit 中的完整文件，不依赖上一轮对话。全文通过则按协议返回 REVIEW_PASS；需要修改则返回 COMPLETE 和完整修正文件。不要只给建议，不修改 GitHub。
