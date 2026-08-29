# Notes/WORKFLOWS/math-render-audit.md

本文件规定 Obsidian 数学渲染审查。

## 1. 检查对象

必须检查：

- Pro 生成的 reader-visible drafts；
- Sol 生成的 mechanical reader-visible 内容；
- `ASSEMBLED_DRAFT.md`；
- formal integration 后的目标文件；
- Pro review 中引用的公式片段若会进入正文。

## 2. 命令

```bash
python Notes/TOOLS/check_obsidian_math.py \
  Notes/WORKING/authoring-tasks/<task-id>/PRO_DRAFTS \
  Notes/WORKING/authoring-tasks/<task-id>/SOL_DRAFTS \
  Notes/WORKING/authoring-tasks/<task-id>/ASSEMBLED_DRAFT.md
```

正式 integration 后再对目标文件运行一次。

## 3. Blocker

以下任一为 blocker：

- `\(`、`\)`、`\[`、`\]`；
- `/(`、`/)`、`/[`、`/]`；
- 未配对的 `$` 或 `$$`；
- `$$` 与公式写在同一行；
- display math 未单独成行；
- reader-visible artifact 是 JSON 转义字符串；
- callout 中块公式缺少引用前缀而导致结构断裂。

## 4. 修复权

- Sol 可直接修复自己生成的 mechanical 内容；
- Pro-authored prose 出错时，Sol不得静默改写。生成 `PRO_REVISION_REQUEST.md`，列出文件、行号和期望格式，再 commit/push 并输出 Pro 修订提示词；
- 仅文件编码和行尾正规化不视为 reader-visible 改写。

## 5. 输出

生成或更新 `MATH_RENDER_AUDIT.md`：

```yaml
status: pass | changes_required | blocked
profile: obsidian-dollar-v1
checked_paths: []
```

正文记录命令、错误位置和返修路由。
