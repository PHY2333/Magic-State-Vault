# Notes/WORKFLOWS/execution-contract.md

本文件规定 Executor 如何验证、执行和交付已批准的计划。正文文体只以 `Notes/WRITING_GUIDE.md` 为准。

## 1. 执行前置条件

Executor 修改正式笔记前必须确认：

- `TASK.md`、`CONTEXT.md` 和 `PLAN.md` 属于同一 `task_id`；
- `TASK.md` 中 `status: plan_approved`；
- `PLAN.md` 中 `approval: approved`；
- `PLAN.md.based_on_context_version` 等于当前 `CONTEXT.md.context_version`；
- 计划引用的路径、标题和来源仍然存在；
- 相关文件在生成上下文后没有发生使计划失效的实质变化；
- 用户未给出与计划冲突的新指令。

任一项不满足时，不修改正式笔记。创建或更新 `REVIEW.md`，说明需要返回 Context Builder、Planner 还是用户。

## 2. 执行权限

Executor 可以自行处理：

- 不改变数学含义的措辞和段落连接；
- 主题短语标题；
- LaTeX、链接、文件内局部符号统一；
- 计划明确要求的文件创建、移动和索引更新。

Executor 必须停止并升级：

- 需要改变任务范围、主线、证明策略或定理条件；
- 需要新增或取消主要前置笔记；
- 计划与当前仓库、canonical ownership 或来源冲突；
- 计划中的关键推导不能成立；
- 必须依靠未核对资料才能继续。

不得以“更顺”“更完整”或“通常如此”为理由静默扩展计划。

## 3. 执行顺序

1. 将 `TASK.md` 状态改为 `executing`。
2. 只修改计划涉及的文件，保护无关的本地改动。
3. 按 `PLAN.md` 完成草稿，不把计划、验收和工具语言写入正式正文。
4. 将 `TASK.md` 状态改为 `review_required`，再按 `subagents.md` 调用必要的只读检查。
5. 修复 implementation-level 问题；semantic-level 问题写入 `REVIEW.md` 并停止。
6. 检查正式正文是否符合 `Notes/WRITING_GUIDE.md`。
7. 按第 4 节判断是否更新索引。
8. 检查通过后，将 `TASK.md` 状态改为 `done`。

## 4. 索引更新边界

### 4.1 `Notes/00-index.md`

它只负责面向读者的主题导航、阅读顺序和主要入口。

仅在以下情况更新：

- 新建、删除、移动或重命名正式笔记；
- 主题层级或推荐阅读顺序发生变化；
- 新增了需要长期暴露的主要入口。

不得加入单次 `WORKING` 任务、计划、验收稿或 subagent 记录。

### 4.2 `CANONICAL_KNOWLEDGE.md`

它是面向 agent 的知识索引，记录概念、定义、结论或协议的 canonical ownership，以及必要的别名、适用范围和来源关系。

仅在以下情况更新：

- canonical 文件发生变化；
- 新增可复用的正式概念或结论；
- 发现重复定义并确定唯一归属；
- 别名、符号约定或来源关系需要长期记录。

不得把它写成阅读顺序、正文复述或任务日志。未触及的旧条目不要机械重写。

## 5. `REVIEW.md` 最小结构

```md
---
task_id: <task-id>
executed_against_context_version: <number>
status: pass | blocked | changes_required
---

# 执行结果

- 修改文件：
- 新建、移动或删除文件：
- 索引更新：

# 与计划的偏差

- 无；或
- 偏差、原因、影响和严重程度：

# 检查结果

- 仓库一致性：
- 数学与来源：
- 正文与格式：

# 未解决事项

- blocker：
- major：
- minor：

# 下一步

- 可交付；或
- 返回 Context Builder / Planner / 用户；或
- 由 Executor 修复后重新检查。
```

严重程度：

- `blocker`：不能继续或不能交付；
- `major`：必须修复并重新检查；
- `minor`：Executor 可直接修复。

## 6. 交付

交付时按 `AGENTS.md` 输出流程回执，并明确：

- 正式文件是否已经可用；
- 是否仍有未解决事项；
- `00-index` 与 `CANONICAL_KNOWLEDGE.md` 是否更新及原因；
- 任务目录建议删除、暂留还是归档；
- 下一步唯一动作。
