# Notes/AGENTS.md

本文件是 Notes Pro-First 1.0 的唯一活动路由入口。

## 1. 路线

### `codex-only`

仅限不改变读者理解路径的机械操作：错字、链接、路径、frontmatter、纯格式，以及用户已经给出完整成文内容的精确替换。

### `pro-write`

概念解释、新笔记、局部或中等规模重写。ChatGPT Pro 直接输出最终文件，Codex应用、检查并推送。

### `pro-write-review`

整篇笔记、复杂证明、多个章节、论文一般化，或用户反馈“像百科”“视角错误”“失去目标”。Pro 先写完整文件，随后新的 Pro 会话从头审查整篇。

只要任务需要决定读者怎样理解、概念为什么此时出现、复杂内容如何组织，就不能降为 `codex-only`。

## 2. 必读文件

- `Notes/WRITING_GUIDE.md`
- `Notes/PRO_WORKFLOW.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `Notes/OBSIDIAN_MATH.md`

旧版本的流程文件和任务目录只保留在 Git 历史中，不再作为活动规则来源。

## 3. Codex 的职责

- 读取本地仓库并生成简洁请求；
- 建立任务分支与 GitHub checkpoint；
- 通过 `@Browser` 自动调用 chatgpt.com 的 Pro 模式；
- 捕获完整响应到临时目录；
- 验证 binding、响应完整性和路径 allowlist；
- 检查 Obsidian 数学与 diff，并在安全边界内机械修复纯格式问题；
- 应用文件并自动 commit/push；
- 对 `pro-write-review` 自动开启新的 Pro 会话；
- 不自动合并主分支。

Codex不得在应用时教学性改写 Pro 正文。若问题只涉及数学定界符、转义、空白/换行，或已经明确的同义记号规范化，并且不改变公式对象、运算、指标、假设、结论、论证结构或读者理解路径，Codex可以只在 staging 中机械修复。每项修复必须在 `APPLY_REPORT.md` 中记录“原文 → 修正”、出现次数和理由，保留原始响应不变，修复后重新运行 Obsidian 数学检查与 diff，并让后续 fresh review 审查正式应用稿。只要修复需要判断或补写数学含义，仍要求 Pro 重发完整文件。

## 4. Pro 的职责

- 实际读取 GitHub checkpoint 中的请求和指定材料；
- 在内部完成必要的教学规划；
- 直接输出完整 reader-visible Markdown；
- 复杂任务在 fresh review 中从头连续审查整篇；
- 不修改 GitHub，不声称已执行本地或 Git 操作。

## 5. Fast binding

每轮请求含一个只存在于请求文件中的 `binding_id`。Browser 提示不公开其值。Pro 必须从 GitHub 文件读取并返回。

Codex只核对：task、request、binding ID、repository、branch、checkpoint commit、allowlist 和 `END_RESPONSE`。不默认计算 request/response hash。

## 6. 自动连续执行

当 `TASK.md` 中 `automation.run_to_completion: true` 时，Codex已经获得以下 standing authorization：

- commit/push request checkpoint；
- 发送并捕获 R01；
- 应用 R01 并 commit/push；
- 若 `review_policy: fresh`，自动打开新 Pro chat 发送 R02；
- 捕获并应用 R02；
- 在任务分支中完成最终 commit/push。

不要在这些阶段询问用户是否继续。

## 7. 必须暂停的情况

- Browser 或账户权限需要用户处理；
- Pro 返回 `NEEDS_CONTEXT`、`DECISION_REQUIRED` 或 `BLOCKED`；
- 删除、移动、拆分、合并或重命名正式文件；
- 输出路径不在 allowlist；
- 来源或数学条件冲突；
- Obsidian 数学检查失败，且不能在上述安全边界内机械修复，或机械修复后仍未通过；
- 需要合并主分支。

## 8. Git 安全

- 使用任务分支；
- 显式暂存路径，禁止 `git add -A`；
- 不向 `main` 直接 push；
- 不 force push；
- push 失败即停止；
- 最终是否合并由用户决定。
