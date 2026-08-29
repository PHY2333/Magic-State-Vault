# Pro Architecture Request Template

你现在担任本任务的 **Lead Didactic Architect**。这是 ChatGPT Pro 的强制 gate，不是仓库编辑任务。

## GitHub snapshot

严格使用用户转交提示词给出的 repository、branch 和 commit。首先打开本 request，再读取其中白名单。不要使用其它分支的更新。

## 任务

按照 `Notes/WORKFLOWS/pro-design.md` 生成完整 `PRO_DESIGN.md`：

- 决定 note-level purpose、whole-note mainline 和最终 unit map；
- 设计 reader capability progression；
- 为每个 unit 选择教学模式、解释深度、placement 和 optionality；
- 决定 source-specific、derivation、reference、lesson 的职责；
- 指定每个 unit 的 author mode；
- 标出来源缺口和用户级文件操作；
- 给出整篇验收标准。

Codex Sol 的 unit map 只是勘察假设，不要机械批准。不要写逐句脚本，也不要修改仓库。

## Obsidian 数学

Artifact 必须是原始 Markdown：

- 行内公式使用 `$...$`；
- 块公式使用单独成行的 `$$`；
- 不得使用 `\(...\)`、`\[...\]`、`/(...)`；
- 不得输出 JSON 转义的 Markdown。

## 输出

1. 生成可下载的 `PRO_DESIGN.md`。
2. frontmatter 完整记录 based-on repository、branch、commit、request path 和 request SHA-256。
3. 若资料不足，status 使用 `needs_source`，不得补猜。
4. 最终回复末尾必须给出以下格式的完整提示词：

```text
NEXT_SOL_PROMPT
<按 SOL_RECEIVE_PRO_DESIGN_TEMPLATE.md 填写后的完整内容>
END_NEXT_SOL_PROMPT
```
