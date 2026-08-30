# Notes/PRO_OUTPUT_PROTOCOL.md

本协议供 ChatGPT Pro 输出能被 Codex App Browser 原样捕获和解析的结果。默认使用 Fast Integrity。

## 1. 绑定区

回复必须从下列内容开始：

```text
BINDING_OK
task_id: <from request>
request_id: <from request>
binding_id: <from request; value is not present in Browser prompt>
based_on_repository: <from Browser prompt>
based_on_branch: <from Browser prompt>
based_on_commit: <from Browser prompt>
END_BINDING
```

无法实际读取请求文件、协议或必读材料时，只返回：

```text
BINDING_FAILED
```

不要根据 Browser 提示中的摘要猜测请求正文。

## 2. 状态

绑定区后只写一种：

```text
PRO_STATUS: COMPLETE
PRO_STATUS: REVIEW_PASS
PRO_STATUS: NEEDS_CONTEXT
PRO_STATUS: DECISION_REQUIRED
PRO_STATUS: BLOCKED
```

`REVIEW_PASS` 仅用于 fresh review。

## 3. 完整文件

`COMPLETE` 必须返回 allowlist 中的完整文件，不返回 patch：

``````text
BEGIN_FILE::<binding_id>
path: Notes/example.md
mode: replace
`````markdown
# Title

行内公式使用 $x+y$。

$$
x+y=z
$$
`````
END_FILE::<binding_id>
``````

要求：

- 只允许 `mode: replace`；
- 路径必须在 request allowlist；
- 文件内容使用至少五个反引号的 `markdown` fence；
- 内容是原始 Markdown，不是 JSON 字符串；
- 不得省略文件前部、用 `...` 代替正文或只给 diff；
- 文件块中不附带分析。

## 4. 消息状态

`NEEDS_CONTEXT`、`DECISION_REQUIRED` 或 `BLOCKED` 使用：

```text
BEGIN_MESSAGE::<binding_id>
<简洁、具体、可执行的说明>
END_MESSAGE::<binding_id>
```

不要同时返回文件块。

## 5. 结束

所有正常绑定状态最后必须写：

```text
END_RESPONSE::<binding_id>
```

结束标记后不得继续输出内容。

## 6. Fresh review

全文通过：

```text
PRO_STATUS: REVIEW_PASS
END_RESPONSE::<binding_id>
```

需要修订：返回 `COMPLETE` 和完整修正文件。不要只列建议。
