# Notes/WORKFLOWS/integration-contract.md

Repository Integrator 只在 `MANUSCRIPT_VERDICT.md: pass` 后把 staged drafts 写入正式仓库。

## 1. 输入

- 通过双审查的 staged drafts；
- `DIDACTIC_DESIGN.md` 的文件与插入决策；
- 目标正式文件；
- `Notes/NOTE_TYPES.md`；
- `Notes/LANGUAGE_PROFILE.md`；
- `CANONICAL_KNOWLEDGE.md`、`Notes/00-index.md`；
- 相关链接与来源文件。

## 2. 权限

Integrator 可以：

- 按 design 替换、插入或新建正文；
- 删除被新正文完全替代的旧竞争开头；
- 补 frontmatter；
- 在句子已经独立成立后添加自然 wikilinks；
- 必要时更新 index 和 canonical；
- 修复路径、anchors 和局部格式。

Integrator 不得：

- 改变教学顺序、claim 依赖或数学主张；
- 为避免重复删除 guided reference 的必要局部解释；
- 用 canonical 摘要替换通过审查的读者正文；
- 在整合时重新引入中英混合速记或维护语言。

## 3. 索引职责

- `Notes/00-index.md`：读者路线、入口和各入口能获得什么；
- `CANONICAL_KNOWLEDGE.md`：稳定知识归属、约定、边界和来源关系。

只有实际职责变化时更新。

## 4. 最终检查

- 正式文件无 WORKING 链接；
- note type 与 entry mode 一致；
- 旧开头和新开头不并存；
- links、anchors、相对路径有效；
- 中文术语与语言规范一致；
- 无无关 diff；
- `git diff --check` 通过。

## 5. Retention

按 TASK 的 `retain_mode` 处理任务文件，并生成 `AUTHORING_SUMMARY.md`。

## 6. 输出

生成 `INTEGRATION_REPORT.md`，记录修改文件、draft 位置、frontmatter、links、index/canonical 更新、未解决事项和 diff 检查。
