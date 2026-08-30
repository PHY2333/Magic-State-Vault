# Notes/AGENTS.md

本文件是 Notes v7 的稳定入口。复杂写作由 ChatGPT Pro 主导；Codex App负责仓库、Browser、文件和 Git。

## 1. 路由

### `codex-only`

仅限不改变理解路径的机械操作：错字、链接、路径、frontmatter、纯格式、用户已经给出精确成文内容的替换。

### `pro-write`

概念解释、新笔记、局部或中等规模重写。Pro 直接输出最终文件，Codex 应用、检查并推送。

### `pro-write-review`

整篇笔记、复杂证明、多个章节、论文一般化，或用户反馈“像百科”“视角错误”“失去目标”。先由 Pro 写完整文件，再由新的 Pro 会话整篇审查。

只要任务需要决定读者怎样理解、为什么此时引入概念或复杂内容如何组织，就不能降为 `codex-only`。

## 2. 必读文件

- `Notes/WRITING_GUIDE.md`
- `Notes/PRO_WORKFLOW.md`
- `Notes/PRO_OUTPUT_PROTOCOL.md`
- `Notes/OBSIDIAN_MATH.md`

## 3. Codex 的职责

- 读取本地仓库并生成简洁 `PRO_REQUEST.md`；
- 建立任务分支和 GitHub checkpoint；
- 通过 `@Browser` 调用 chatgpt.com 的 Pro 模式；
- 验证 GitHub 绑定；
- 原样保存完整网页回复；
- 使用解析脚本提取完整文件；
- 检查路径、Obsidian 数学和 diff；
- 应用文件并 commit/push；
- 复杂任务在新 Pro 会话中完成 fresh review；
- 不自动合并主分支。

Codex 不得在保存或应用时重写 Pro 的教学正文。若 Pro 输出不合格，应要求 Pro 重发完整文件。

## 4. Pro 的职责

- 根据请求中列出的 GitHub 文件自行完成必要规划；
- 直接写最终 reader-visible Markdown；
- 复杂任务在 fresh review 中从头连续审查整篇；
- 不修改仓库；
- 不声称已执行 Git 操作。

## 5. Snapshot 与绑定

Pro 只处理 Browser 提示绑定的 repository、branch、commit 和 request SHA-256。`binding_nonce` 与 `response_token` 只存在于请求文件中，不在 Browser 提示中公开。

无法返回正确 nonce/token 时，Codex 必须停止，不得应用结果。

## 6. 原始响应优先

顺序必须是：

```text
Browser 读取完整回复
→ 保存 response.raw.md
→ 计算 SHA-256
→ 解析 binding 与文件块
→ 静态检查
→ 应用
```

不得先概括回复后只保存摘要。

## 7. Obsidian 数学

所有 reader-visible Markdown 只能使用 `$...$` 与独立成行的 `$$...$$`。提交前运行：

```bash
python Notes/TOOLS/check_obsidian_math.py <file-or-directory>
```

发现 `\\(...\\)`、`\\[...\\]`、`/(...)` 或未配对分隔符时停止；不要静默改写 Pro 正文。

## 8. Git 自动化

- 使用任务分支；
- 只显式暂存 allowlist，禁止 `git add -A`；
- 不向 `main` 直接 push；
- 不 force push；
- push 失败时停止；
- 合并主分支始终由用户决定。

## 9. 用户决定边界

仅在以下情况暂停用户：删除、移动、拆分、合并、重命名正式文件；显著改变学习范围；关键来源冲突；两条长期路线互斥；最终是否合并分支。

普通教学结构、解释深度和正文行文交给 Pro。
