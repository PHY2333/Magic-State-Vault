# Notes/PRO_OUTPUT_PROTOCOL.md

本协议供 ChatGPT Pro 输出可被 Codex App Browser 原样捕获和解析的结果。

## 1. 绑定区

回复必须从以下内容开始，不得在前面添加解释：

```text
BINDING_VERIFIED
task_id: <from request>
request_id: <from request>
binding_nonce: <from request; value is not present in Browser prompt>
response_token: <from request; value is not present in Browser prompt>
based_on_repository: <from Browser prompt>
based_on_branch: <from Browser prompt>
based_on_commit: <from Browser prompt>
request_sha256: <from Browser prompt>
END_BINDING
```

无法实际读取请求或字段不一致时，只返回：

```text
BINDING_FAILED
```

## 2. 状态

绑定区后写且只写一种：

```text
PRO_STATUS: COMPLETE
PRO_STATUS: REVIEW_PASS
PRO_STATUS: NEEDS_CONTEXT
PRO_STATUS: DECISION_REQUIRED
PRO_STATUS: BLOCKED
```

`REVIEW_PASS` 仅用于 fresh review。

## 3. 完整文件

`COMPLETE` 后可以有一个或多个文件块。分隔符中的 token 必须是请求文件里的 `response_token`。

``````text
BEGIN_FILE::<response_token>
path: Notes/example.md
mode: replace
`````markdown
# Title

正文中的行内公式使用 $x+y$。

$$
x+y=z
$$
`````
END_FILE::<response_token>
``````

要求：

- 只允许 `mode: replace`；
- 路径必须在请求 allowlist；
- 文件内容使用至少五个反引号的 `markdown` fenced block；
- 文件内容是原始 Markdown，不是 JSON 字符串；
- 不得省略文件前部或只给 patch；
- 代码块内不附带解释。

## 4. 消息状态

`NEEDS_CONTEXT`、`DECISION_REQUIRED` 或 `BLOCKED` 使用：

```text
BEGIN_MESSAGE::<response_token>
<简洁、具体、可执行的说明>
END_MESSAGE::<response_token>
```

不要同时返回文件块。

## 5. 结束

所有状态最后必须写：

```text
END_RESPONSE::<response_token>
```

结束标记之后不得继续写内容。

## 6. Review

Fresh review 如果全文通过：

```text
PRO_STATUS: REVIEW_PASS
END_RESPONSE::<response_token>
```

如果需要修订，必须返回 `COMPLETE` 和完整修正文件；不要只给零散意见。
