# Notes/WORKFLOWS/pro-final-review.md

Whole-Note Reviewer 由新的 ChatGPT Pro 会话承担，是最终教学与行文 gate。

## 1. 独立性

Reviewer 只读取：

- `PRO_REQUESTS/FINAL-REVIEW.md`；
- `PRO_REVIEW_CARD.md`；
- 完整 `ASSEMBLED_DRAFT.md`；
- `Notes/OBSIDIAN_MATH.md`；
- `Notes/LANGUAGE_PROFILE.md`。

不得读取 unit packets、domain/source mapping、Sol Contract Audit、先前 Pro review 或 detailed design ledger。

## 2. 必查内容

### Whole-note purpose

- 文件究竟是 reference、lesson、derivation 还是 paper-guide；
- 整篇是否完成 review card 的入口到出口；
- 是否存在互相竞争主线。

### Capability continuity

- 每节入口是否由前文形成；
- validated opening 后是否切回专家压缩；
- 工具名称、公式和 source-specific 记号是否在需求后出现；
- 跨 unit 的末问、首句、子问题和回返是否连续。

### Exposition and prose

- 无依赖声明、ownership、前置清单等维护者视角；
- 未经逐句提示的部分是否仍像教材；
- 定义、动机、整体图、worked example 和 proof map 是否合适；
- 中文行文是否自然，不像 checklist 翻译；
- 复杂推导是否先给足够目标或框架。

### Depth and structure

- 辅助证明是否压过主对象；
- optional / conditional_optional 是否真正可跳过；
- source-specific adapter 是否打断一般主线；
- reference 是否混入应独立的 lesson、derivation 或 paper-guide；
- section 删除后下游首次使用是否仍有落点。

### Obsidian rendering

- 所有 reader-visible 数学使用 `$` 与 `$$`；
- 不出现 `\(...\)`、`\[...\]`、`/(...)` 或字符串双重转义；
- callout、表格和块公式结构可在 Obsidian 中正常渲染。

## 3. 输出

生成 `PRO_FINAL_REVIEW.md`：

```yaml
---
status: pass | changes_required | blocked
role: whole-note-reviewer
based_on_repository:
based_on_branch:
based_on_commit:
based_on_request_sha256:
reviewed_assembled_sha256:
review_independence: fresh-pro-session
math_profile: obsidian-dollar-v1
whole_note_scope: true
---
```

正文包括 whole-note verdict、findings、severity、route、必须修改、可选编辑和是否允许整篇标记 `reviewed`。

## 4. Pro 回复合同

Pro 必须：

1. 生成可下载的 `PRO_FINAL_REVIEW.md`；
2. 不修改仓库；
3. 在回复末尾按 `SOL_RECEIVE_PRO_FINAL_REVIEW_TEMPLATE.md` 输出完整 `NEXT_SOL_PROMPT`。

若 status 为 pass，下一 Sol prompt 可以触发自动 Integration Preview 与预授权 integration。若 changes required，prompt 必须指明返回 Pro Design、Pro Draft 或 Sol Mapping。
