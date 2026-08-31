# Notes/AGENTS.md

本文件是 Notes Pro-First 1.1 的唯一活动路由入口。

## 1. 路线

### `codex-only`

仅限不改变读者理解路径的机械操作：错字、链接、路径、frontmatter、纯格式，以及用户已经给出完整成文内容的精确替换。

### `pro-write`

概念解释、新笔记、局部或中等规模重写。ChatGPT Pro 直接输出最终文件，Codex检查、进行必要的格式规范化、应用并推送。

### `pro-write-review`

整篇笔记、复杂证明、多个章节、论文一般化，或用户反馈“像百科”“视角错误”“失去目标”。Pro 先写完整文件，随后按任务指定的 review policy 审查整篇。

只要任务需要决定读者怎样理解、概念为什么此时出现、复杂内容如何组织，就不能降为 `codex-only`。

## 2. 必读文件

- `Notes/WRITING_GUIDE.md`
- `Notes/PRO_WORKFLOW.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `Notes/OBSIDIAN_MATH.md`

旧版本流程只保留在 Git 历史中，不再作为活动规则来源。

## 3. Codex 的职责

- 读取本地仓库并生成简洁请求；
- 建立任务分支与 GitHub checkpoint；
- 通过 `@Browser` 调用 chatgpt.com 的 Pro 模式；
- 捕获完整响应到临时目录；
- 验证 binding、响应完整性和路径 allowlist；
- 把文件提取到 staging；
- 运行 Obsidian 数学与 Markdown 检查；
- 依据 `Notes/OBSIDIAN_MATH.md`，直接修复纯格式问题和可唯一判断的 LaTeX 语法问题；
- 应用文件并自动 commit/push；
- 按任务 review policy 运行 R02；
- 不自动合并主分支。

Codex不得对 Pro 正文做教学性、数学性或语义性改写。

格式规范化不属于教学性改写。只要修复后的数学陈述与正文含义唯一且不变，Codex应直接处理，不得仅因格式问题要求 Pro 重发完整文件，也不得询问用户。

## 4. 格式问题的责任边界

### Codex 直接修复

- Markdown 数学分隔符；
- 行内公式与块公式的布局；
- 块公式周围的换行和空行；
- callout 的引用前缀；
- 明显由 Browser、代码块或字符串转义造成的反斜杠问题；
- 其它不改变数学陈述、正文措辞和内容顺序的 Obsidian / Markdown 问题；
- 可由上下文或已读取来源唯一确定的 LaTeX 语法错误。

### 返回 Pro 或来源核验

- 修复会改变数学符号、运算、指标、正负号、转置、量词、等式或条件；
- 存在两个以上合理的数学解释；
- 无法判断公式边界；
- 正文与公式相互矛盾；
- 来源之间发生冲突；
- 缺失的不是格式，而是数学内容或解释。

现有 Python checker 只负责诊断，不负责修改文件。Codex必须结合全文作判断，不得机械套用全局替换。

## 5. Pro 的职责

- 实际读取 GitHub checkpoint 中的请求和指定材料；
- 在内部完成必要的教学规划；
- 直接输出完整 reader-visible Markdown；
- 按请求审查完整文件；
- 尽量遵守 Obsidian 数学规范；
- 不修改 GitHub，不声称已执行本地或 Git 操作。

Pro 不需要为孤立的纯格式问题重新生成整篇文件；Codex在应用层负责规范化。

## 6. Fast binding

每轮请求含一个只存在于请求文件中的 `binding_id`。Browser 提示不公开其值。Pro 必须从 GitHub 文件读取并返回。

Codex只核对 task、request、binding ID、repository、branch、checkpoint commit、allowlist 和 `END_RESPONSE`。不默认计算 request/response hash。

## 7. 自动连续执行

当 `TASK.md` 中 `automation.run_to_completion: true` 时，Codex已经获得以下 standing authorization：

- commit/push request checkpoint；
- 发送并捕获 R01；
- 解析、格式规范化、应用 R01 并 commit/push；
- 按 review policy 自动发送 R02；
- 捕获、格式规范化并应用 R02；
- 在任务分支中完成最终 commit/push。

不要在这些阶段询问用户是否继续。

## 8. 必须暂停的情况

- Browser 或账户权限需要用户处理；
- Pro 返回 `NEEDS_CONTEXT`、`DECISION_REQUIRED` 或 `BLOCKED`；
- 删除、移动、拆分、合并或重命名正式文件；
- 输出路径不在 allowlist；
- 来源或数学条件冲突；
- 格式问题存在多个合理解释，或修复可能改变数学含义；
- Codex完成上下文修复后，文件仍无法通过 Obsidian 数学检查；
- 需要合并主分支。

纯格式错误本身不是暂停条件。

## 9. Git 安全

- 使用任务分支；
- 显式暂存路径，禁止 `git add -A`；
- 不向 `main` 直接 push；
- 不 force push；
- push 失败即停止；
- 最终是否合并由用户决定。
