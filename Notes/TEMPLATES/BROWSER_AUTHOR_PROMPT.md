使用已连接的 GitHub App读取以下固定项目快照，并使用 ChatGPT Pro 完成笔记写作。

repository: <owner/repo>
branch: <task-branch>
commit: <checkpoint-commit>
request_path: <PRO_REQUEST.md path>
protocol_path: Notes/PRO_OUTPUT_PROTOCOL.md

首先实际读取 request_path 和 protocol_path，并读取 request 中列出的全部必读文件。

从 request 文件读取 task_id、request_id 和 binding_id。本消息没有给出 binding_id 的值。回复顶部必须严格按协议返回它。

若无法读取、字段不一致或必读文件不可访问，返回协议规定的 BINDING_FAILED 或 NEEDS_CONTEXT。不得根据本消息摘要猜测任务正文。

绑定成功后，在同一回复中执行 request。严格按协议返回完整文件，不修改 GitHub，不在 END_RESPONSE 后继续写内容。
