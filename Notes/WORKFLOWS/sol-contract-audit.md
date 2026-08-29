# Notes/WORKFLOWS/sol-contract-audit.md

Codex Sol 对完整 `ASSEMBLED_DRAFT.md` 做数学、来源、装配和 Obsidian 渲染审查。它不作最终教材行文判决。

## 1. 输入

- 经验证的 `PRO_DESIGN.md`；
- `SOL_DESIGN_VALIDATION.md`；
- Domain/Source/Learner artifacts；
- Pro/Sol drafts 与 hashes；
- `ASSEMBLY_MAP.md`；
- `ASSEMBLED_DRAFT.md`；
- `OBSIDIAN_MATH.md`、Language Profile 与 Writing Guide。

## 2. 检查

- 每个数学 claim、条件、公式、约定和类型有来源或可复算推导；
- core/optional/conditional 边界未被 assembly 改变；
- author origins 与 hashes 正确；
- 所有旧 section 有 retain/rewrite/move/delete 决定；
- 无 task 元语言、临时路径、失效链接和意外重复；
- Sol mechanical 内容严格机械；
- frontmatter status 未过度升级；
- assembled note 与 target scope 一致；
- `check_obsidian_math.py ASSEMBLED_DRAFT.md` 通过。

## 3. 不作的判断

Sol 不因数学都正确、packet 都满足或自己的 cold read 无 finding 而给 whole-note pedagogy pass。全局视角、行文质量和能力阶梯属于 Pro Final Review。

## 4. 输出与自动 handoff

生成 `SOL_CONTRACT_AUDIT.md`：

```yaml
status: pass | changes_required | blocked
assembled_draft_sha256:
reviewed_pro_design_sha256:
math_render_status:
```

若 pass：

- 生成 `PRO_REQUESTS/FINAL-REVIEW.md`；
- 更新任务为 `awaiting_pro_final_review`；
- 自动 commit/push；
- 输出精确 Pro Final Review Prompt。

Draft 或 assembly 改变后必须完整重跑。
