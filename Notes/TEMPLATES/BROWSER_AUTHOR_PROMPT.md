使用已连接的 GitHub App读取以下固定项目快照，并使用 ChatGPT Pro 完成笔记写作。

repository: <owner/repo>
branch: <task-branch>
commit: <checkpoint-commit>
request_path: <PRO_REQUEST.md path>
request_sha256: <sha256>
protocol_path: Notes/PRO_OUTPUT_PROTOCOL.md

首先实际读取 request_path 和 protocol_path。

绑定验证要求：

- 从 request 文件读取 task_id、request_id、binding_nonce 和 response_token；
- 本消息没有给出 binding_nonce 或 response_token 的值；
- 在回复顶部严格按协议返回它们；
- 若无法读取、字段不一致、无法访问必须读取的文件，返回协议规定的 BINDING_FAILED 或 NEEDS_CONTEXT；
- 不得根据本消息摘要猜测任务正文。

绑定成功后，在同一回复中执行 request。严格按 PRO_OUTPUT_PROTOCOL 输出完整文件。不要修改 GitHub，不要在 END_RESPONSE 后继续写内容。
