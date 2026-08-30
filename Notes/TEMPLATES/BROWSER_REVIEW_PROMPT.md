使用已连接的 GitHub App读取以下固定项目快照，并在一个全新的 ChatGPT Pro 会话中进行整篇审查。

repository: <owner/repo>
branch: <task-branch>
commit: <review-checkpoint-commit>
request_path: <REVIEW_REQUEST.md path>
request_sha256: <sha256>
protocol_path: Notes/PRO_OUTPUT_PROTOCOL.md

首先实际读取 request_path、protocol_path、该任务的原始 PRO_REQUEST.md，以及 request 中列出的完整目标文件。

从 request 文件读取 task_id、request_id、binding_nonce 和 response_token。本消息没有给出 nonce/token 的值。绑定失败时不要猜测。

请从头连续审查完整文件，不要依赖上一轮对话或作者的自我说明。

若全文通过，按协议返回 REVIEW_PASS；若需修改，返回 COMPLETE 和完整修正文件。不要只给建议。不要修改 GitHub。
