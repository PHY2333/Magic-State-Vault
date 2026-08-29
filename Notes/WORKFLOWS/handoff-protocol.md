# Notes/WORKFLOWS/handoff-protocol.md

本文件规定 Codex Sol 与 ChatGPT Pro 之间的可复制提示词协议。

## 1. 基本原则

- Request artifact 是阶段权威；聊天中的提示词只负责精确定位 request 和 remote snapshot。
- Sol→Pro handoff 必须发生在 commit/push 成功之后。
- Pro→Sol handoff 必须同时提供 artifact 和 `NEXT_SOL_PROMPT`。
- 提示词必须是一段完整命令，不要求用户重新解释任务或选择下一步。
- 所有 prompt 和 artifact 均记录 task、role、branch、commit、request path 和 expected output。

## 2. Sol → Pro

Sol 在当前阶段：

1. 生成 `PRO_REQUESTS/<stage>.md`；
2. 更新 `TASK.md`；
3. 执行检查；
4. commit/push；
5. 获取 `git rev-parse HEAD`；
6. 在聊天中输出：

```md
### COPY THIS PROMPT TO CHATGPT PRO
```text
@GitHub
读取仓库 <repository> 的分支 <branch>，固定到提交 <commit>。
打开 <request_path>，严格按其中的角色、读取白名单、数学格式和输出合同执行。
不要读取其它分支的更新，不要修改仓库。
完成后生成 <expected_artifacts> 为可下载 Markdown 文件，并在回复末尾给出 request 规定的 NEXT_SOL_PROMPT。
```
```

不得只输出文件路径。

## 3. Pro → Sol

每个 Pro request 必须要求 Pro：

1. 生成约定名称的 `.md` artifact；
2. artifact frontmatter 记录 `based_on_repository`、`based_on_branch`、`based_on_commit`、`based_on_request_sha256`；
3. 使用原始 Markdown 和 Obsidian `$` 数学格式；
4. 在最终回复中给出 artifact 下载入口；
5. 按对应的 `SOL_RECEIVE_*.md` 模板输出完整 `NEXT_SOL_PROMPT`。

默认交付模式为 `attachment`：用户将 Pro artifact 附给 Sol，然后复制 `NEXT_SOL_PROMPT`。小文件可以使用 inline fallback，但必须保留完整文件边界。

## 4. Stale protection

Sol 接收 Pro artifact 后必须核对：

- task id；
- Pro role；
- request path/hash；
- based-on branch/commit；
- 目标 artifact 路径；
- 数学 delimiter；
- artifact 未被截断。

任一不匹配时不得继续，生成错误报告。

## 5. 下一提示词的职责

### Pro design 后

`NEXT_SOL_PROMPT` 要求 Sol 保存 `PRO_DESIGN.md`、验证、自动 commit/push，并生成下一份 Pro draft prompt 或 Pro design revision prompt。

### Pro draft 后

`NEXT_SOL_PROMPT` 要求 Sol 保存所有 draft、运行数学检查、完成机械插槽、组装和合同审查、自动 commit/push，并生成下一份 Pro draft batch 或 final review prompt。

### Pro final review 后

`NEXT_SOL_PROMPT` 要求 Sol 保存 review、核对 assembled hash；若 pass 且自动 integration 已授权，则先 commit/push review 与 preview checkpoint，再重新锁定远端并执行 integration commit/push；若 changes required，则生成相应 Pro revision prompt。

## 6. Prompt receipt

Sol 和 Pro 的回复都只能给一个“下一步唯一动作”。不得同时给用户多条互斥操作。
