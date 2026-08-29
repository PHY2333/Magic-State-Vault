# Notes/OBSIDIAN_MATH.md

本文件规定所有 reader-visible Markdown 的公式格式。目标渲染器是 Obsidian / MathJax。

## 1. 唯一允许的分隔符

行内公式：

```md
矩阵必须满足 $H_XH_Z^T=0$。
```

块公式：

```md
$$
C_2 \xrightarrow{H_Z^T} C_1 \xrightarrow{H_X} C_0
$$
```

块公式的两个 `$$` 必须各自单独成行。

## 2. 禁止形式

Reader-visible 正文中禁止：

```text
\(...\)
\[...\]
/(...)
/[...]
$$ equation $$
```

也禁止把本应渲染的公式放入反引号代码中。

## 3. 原始 Markdown，不得 JSON 双重转义

Pro 和 Sol 交付的 `.md` 必须是原始 Markdown 文件：

- LaTeX 命令写成 `\mathbb`、`\otimes`、`\ker`；
- 不把整份 Markdown 包装为 JSON 字符串；
- 不把普通反斜杠重复写成 `\\mathbb`；
- 只有 LaTeX 矩阵换行本身需要 `\\`。

## 4. 中文与公式

- 公式外使用中文解释，避免在 `\text{...}` 中塞入长中文句子；
- 句子中的短数学对象用 `$...$`；
- 长等式、推导链和矩阵使用块公式；
- 一个公式首次出现后，应在相邻正文解释符号和用途。

## 5. 表格

Markdown 表格中只使用短行内公式，例如 `$C_1$`、$H_X$。复杂推导移到表格外，不在单元格中使用块公式。

## 6. Obsidian callout

在 callout 中使用块公式时，每一行都保留引用符号：

```md
> [!note]- 补充推导
> 下面核对一个等式。
>
> $$
> XZ=-ZX
> $$
```

## 7. 标题与链接

- 标题尽量不用公式；确需符号时使用纯文本短符号，不依赖复杂 MathJax；
- wikilink 不能承担公式定义；
- heading anchor 不应依赖数学渲染结果。

## 8. 静态检查

对 staged draft、assembled draft 和正式目标运行：

```bash
python Notes/TOOLS/check_obsidian_math.py <path> [<path> ...]
```

任何错误都阻止 commit、push handoff 或正式 integration。
