# Notes/OBSIDIAN_MATH.md

目标渲染器是 Obsidian / MathJax。

## 允许

行内公式：

```md
矩阵满足 $H_XH_Z^T=0$。
```

块公式：

```md
$$
C_2 \xrightarrow{H_Z^T} C_1 \xrightarrow{H_X} C_0
$$
```

两个 `$$` 必须各自单独成行。

## 禁止

```text
\(...\)
\[...\]
/(...)
/[...]
$$ equation $$
```

不得把需要渲染的公式放在反引号代码中；不得把整份 Markdown 作为 JSON 字符串输出；正常 LaTeX 命令只写一个反斜杠，例如 `\mathbb F_2`。

## 表格与 callout

表格中只使用短行内公式。复杂公式移到表格外。

Callout 中块公式的每一行都保留 `>`：

```md
> [!note]- 补充推导
>
> $$
> XZ=-ZX
> $$
```

## 检查

```bash
python Notes/TOOLS/check_obsidian_math.py <file-or-directory>
```

失败时不得直接提交 reader-visible 文件。Codex可以依 `Notes/PRO_WORKFLOW.md` 的“纯格式机械修复”规则修改 staging，但必须保持原始 Pro 响应不变、记录逐项替换并重新检查；需要判断数学含义时必须退回 Pro。只有检查通过的正式文件才可提交。
