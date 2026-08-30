# Notes/OBSIDIAN_MATH.md

目标渲染器是 Obsidian / MathJax。

## 允许

行内：

```md
矩阵必须满足 $H_XH_Z^T=0$。
```

块公式：

```md
$$
C_2 \xrightarrow{H_Z^T} C_1 \xrightarrow{H_X} C_0
$$
```

两个 `$$` 必须分别独占一行。

## 禁止

```text
\(...\)
\[...\]
/(...)
/[...]
$$ equation $$
```

也禁止把本应渲染的公式放入反引号代码中。

## 原始 Markdown

LaTeX 命令正常写成 `\mathbb`、`\otimes`、`\ker`。不要把 Markdown 包装成 JSON 字符串，不要把普通命令双重转义成 `\\mathbb`。只有矩阵行换行本身使用 `\\`。

## Callout

```md
> [!note]- 补充推导
> 下面核对等式。
>
> $$
> XZ=-ZX
> $$
```

## 检查

```bash
python Notes/TOOLS/check_obsidian_math.py <path> [<path> ...]
```

任何错误阻止应用和 commit。
