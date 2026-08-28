# Notes/WORKFLOWS/integration-preview.md

Repository Fit Planner 在 `MANUSCRIPT_VERDICT.md: pass` 后生成只读仓库适配预览。它不修改正式文件。

## 1. 允许读取

- 通过双审查的 staged drafts；
- 通过审查的 `DIDACTIC_DESIGN.md` 中与目标 unit 对应的 depth and placement ledger；只用于核对 duplication rationale；
- 目标正式文件及其相邻段落；
- NOTE_TYPES、LANGUAGE_PROFILE；
- 相关正式笔记、links、00-index、CANONICAL_KNOWLEDGE；
- manuscript verdict。

## 2. 预览内容

生成 `INTEGRATION_PREVIEW.md`：

```md
---
status: ready | changes_required | blocked
reviewed_draft_revision:
---
# Target placement
# Replacement / deletion range
# Assembled reading flow
# Local bridge and links
# Duplication and ownership check
# Frontmatter
# Index / canonical impact
# Repository checks
# Required return route
```

## 3. 检查项

- 新旧开头是否竞争或重复；
- staged units 与后续正文是否自然连接；
- local bridge 是否足够，完整细节是否已有 owner；
- 需要添加的链接是否只作扩展，不承担核心解释；
- detail duplication 是否与 design rationale 一致；
- frontmatter、anchors、index、canonical 是否需要最小变化；
- 是否存在计划外删除或大范围格式化。

## 4. 不得静默改稿

Preview 可以规划替换、删除旧竞争段落、添加非承重链接和补 frontmatter；不得压缩、移动、重写或改变已通过文本的 explanation depth。

若仓库适配需要 reader-visible 文本变化，`status: changes_required`，返回 Didactic Design / Writer，并重新双审查。

## 5. Ready 条件

只有 replacement range、assembled flow、duplication、links 和索引影响都明确，且无需改动已审查正文，才能 `status: ready` 并进入 integration。
