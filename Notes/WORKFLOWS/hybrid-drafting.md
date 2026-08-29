# Notes/WORKFLOWS/hybrid-drafting.md

本文件规定 Pro 与 Sol 的混合起草、artifact 接收、装配和下一 handoff。

## 1. Draft batch request

Sol 在 design validation pass 后生成一个或多个 `PRO_REQUESTS/DRAFT-BATCH-xx.md`。每批建议包含 1–3 个高关联 unit。

Request 包含：

- remote branch/commit；
- whole-note mainline 摘要；
- unit entry/exit、main question 和 transition；
- 已核验数学、公式、条件和来源摘录；
- explanation depth、optional placement 与 file action；
- 前后 unit 的短职责；
- Obsidian math 与中文合同；
- 不可承诺内容；
- 期望输出路径；
- `NEXT_SOL_PROMPT` 模板。

Request 不恢复逐句脚本。Pro 是作者，不是 checklist 转译器。

## 2. Author mode

### `pro_full`

Pro 输出完整 reader-visible unit 到 `PRO_DRAFTS/Uxx.md`。

### `pro_core_sol_mechanical`

Pro 写主线正文，并使用明确插槽：

```html
<!-- SOL_INSERT: verified-table-id -->
```

Sol 只能插入经验证内容，不改写 Pro prose。

### `sol_mechanical`

只允许确定内容，例如来源表、精确记号转换表、由已有矩阵机械展开的表格、frontmatter、links 和 anchors。

### `retain_exact`

保留 exact validated text，仍进入 assembled whole-note review。

## 3. Pro 数学合同

Pro draft 必须是原始 Markdown：

- 行内 `$...$`；
- 块公式使用独立 `$$`；
- 禁止 `\(...\)`、`\[...\]` 和双重转义；
- callout 中公式按 `OBSIDIAN_MATH.md`；
- 不把公式放入反引号代码。

## 4. Pro 回复合同

Pro 生成所有约定 draft artifact，并在回复末尾按 `SOL_RECEIVE_PRO_DRAFTS_TEMPLATE.md` 给出完整 `NEXT_SOL_PROMPT`。

## 5. Sol 接收

Sol：

1. 原样保存所有 Pro draft；
2. 核对 based-on request/commit；
3. 运行 math linter；
4. 若失败，生成行号明确的 Pro revision request，commit/push 并提示 Pro；
5. 填充 mechanical slots；
6. 生成 `ASSEMBLY_MAP.md` 与 `ASSEMBLED_DRAFT.md`；
7. 运行 math linter、来源和合同审查；
8. 生成 `PRO_REVIEW_CARD.md` 与 `PRO_REQUESTS/FINAL-REVIEW.md`；
9. 自动 commit/push；
10. 输出精确 Pro Final Review Prompt。

## 6. Assembly origin

`ASSEMBLY_MAP.md` 为每段记录：

- `pro_draft`；
- `sol_mechanical`；
- `retain_validated`；
- `retain_legacy_with_pro_authorization`。

Whole-note task 不得无说明带入 `legacy-unreviewed` 或 `changes-required` 段落。

## 7. PRO_REVIEW_CARD

只包含整篇阅读场景、assumed entry、whole-note exit、note type/entry mode、core/optional routes、用户真实问题和中文语体。不得含 packet、source verdict、Sol audit 结论或标准答案。
