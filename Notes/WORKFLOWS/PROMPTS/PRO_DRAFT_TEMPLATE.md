# Pro Draft Request Template

你现在担任本批 unit 的 **Lead Author**。

只读取当前 request 及其授权的相邻正文和来源。不要读取仓库维护规则，也不要把 mapping、ownership、unit contract、depth 或审查语言写入正文。

## 写作

- 直接写最终 reader-visible prose；
- 保持 whole-note 主问题和前后 transition；
- 自行组织自然句子，不把 request 逐项翻译成 checklist；
- 遵守 explanation depth 与 optional placement；
- 不补猜来源未支持内容；
- 不修改仓库。

## Obsidian 数学

所有 artifact 使用原始 Markdown：

- `$...$` 用于行内；
- `$$` 独立成行用于块公式；
- 禁止 `\(...\)`、`\[...\]`、`/(...)`；
- callout 中每行保留 `>`；
- 不输出 JSON 字符串。

## 输出

1. 为每个 unit 生成 request 指定名称的可下载 `.md` 文件。
2. 正文文件只含 reader-visible 内容，不附分析。
3. 最终回复列出所有 artifact。
4. 回复末尾必须给出：

```text
NEXT_SOL_PROMPT
<按 SOL_RECEIVE_PRO_DRAFTS_TEMPLATE.md 填写后的完整内容>
END_NEXT_SOL_PROMPT
```
