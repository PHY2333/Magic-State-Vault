# Notes/WORKFLOWS/planning-contract.md

本文件规定 Context Builder 与 Planner 的输入、输出和边界。它不规定正式正文文体。

## 1. Context Builder（通常为 Codex Sol）

### 1.1 任务

把当前仓库压缩成 Planner 可验证、可去重的上下文。只陈述实际读取到的内容，不设计教学主线，不修改正式笔记。

### 1.2 必须读取

除 `AGENTS.md` 和 `note-writing.md` 外，至少读取：

- `Notes/WRITING_GUIDE.md`；
- `CANONICAL_KNOWLEDGE.md`；
- `Notes/00-index.md`；
- 目标文件；
- 与任务直接相关的上游、下游笔记；
- 任务指定的论文、翻译或其他来源。

### 1.3 `TASK.md` 最小结构

```md
---
task_id: <YYYYMMDD-short-name>
status: new
target_files:
  - <path>
---

# 任务目标

# 用户当前卡点或动机

# 本次范围

# 本次不处理

# 完成标准
```

### 1.4 `CONTEXT.md` 最小结构

```md
---
task_id: <task-id>
context_version: 1
base_commit: <commit-or-unavailable>
working_tree: <clean-or-summary>
generated_by: codex-sol
---

# 已实际读取的文件

- `<path>`
  - 采用内容：

# 当前目标文件

- 当前主线：
- 已有可保留内容：
- 已发现的问题：

# Canonical ownership

| 概念或结论 | canonical 文件 | 当前任务的处理方式 |
|---|---|---|

# 上游与下游

- 上游可直接继承：
- 下游确实需要：

# 不得重复

- 已在其他笔记完整处理的定义、证明或例子：

# 来源锚点

- 文件、标题、页码、定理号或公式号：

# 缺失与不确定

- 未找到：
- 需要 Planner 判断：
- 需要补充来源：

# 上下文结论

- 足够规划 / 仍需补充：
```

### 1.5 版本规则

- 每次实质补充或重建上下文，递增 `context_version`。
- `CONTEXT.md` 必须列出实际读取文件；不得以“已检查相关资料”代替。
- 不得把文件名、目录名或模型记忆当作仓库事实。
- 完成后将 `TASK.md` 状态改为 `context_ready`，并提示用户下一步交给 Planner。

## 2. Planner（通常为 ChatGPT Pro）

### 2.1 输入

必须读取：

- `TASK.md`；
- `CONTEXT.md`；
- 本文件；
- `Notes/WRITING_GUIDE.md`；
- `CONTEXT.md` 明确列出的必要原文。

Planner 能直接读取仓库时，也应先以 `CONTEXT.md` 控制范围；额外读取的文件必须在计划中列出。

### 2.2 上下文不足时

不得猜测、补写仓库事实或生成半成品计划。只输出：

```md
# 上下文补充请求

- 缺失内容：
- 为什么影响规划：
- 建议 Sol 读取的具体路径或检索目标：
- 补充后应递增的 `context_version`：

## 下一步

让 Sol 更新 `CONTEXT.md`，不要修改正式笔记。
```

### 2.3 `PLAN.md` 最小结构

```md
---
task_id: <task-id>
based_on_context_version: <number>
approval: pending
planner: chatgpt-pro
---

# 上下文检查

- 已采用：
- 仍有但不阻塞规划的不确定项：
- Planner 额外实际读取的文件：

# 与现有知识库的衔接

- 直接复用的 canonical 内容：
- 只建立链接的内容：
- 需要新增、拆出、合并或迁移的内容：
- 必须避免的重复：

# 正文主线

用完整句子说明正文从哪里开始，经过哪些必要对象和推导，最后停在哪里。

# 分节计划

## <标题>

- 已有前提：
- 本节新增：
- 必须写出的关系或推导：
- 本节结束后后文可使用：
- 不在本节重复：

# 数学承诺

- 必须完整写出的定义、映射、等式链或证明片段：
- 必须说明用途的条件：
- 必须核对的 degree、sign、index、domain/codomain：
- 一般情形与特殊系数情形的边界：

# 例子安排

- 是否需要：
- 具体对象与计算：
- 只说明什么：
- 不承担什么：
- 如何回到一般构造：

# 执行边界

## Executor 可自行决定

- 局部措辞、标题短语、LaTeX 排版、链接和不改变数学含义的符号统一。

## 必须停止并升级

- 改变任务范围或正文主线；
- 改变证明策略或定理条件；
- 新增或取消主要前置笔记；
- 与来源或 canonical note 冲突；
- 计划依赖的仓库事实已经过期。

# 验收条件

- 内容：
- 数学：
- 仓库一致性：
- 正文：按 `Notes/WRITING_GUIDE.md`。

# 下一步

请用户审阅本计划。批准时回复：`批准任务 <task-id> 的 PLAN，进入执行。`
```

计划被用户或 Sol 原样保存到任务目录后，将 `TASK.md` 状态改为 `plan_proposed`；不得同时把 `approval` 改为 `approved`。

### 2.4 Planner 的边界

- 不修改仓库，不替 Executor 决定文件操作细节。
- 不虚构文件、链接、已有定义或来源位置。
- 不必写完整最终笔记，但困难的证明步骤、映射关系和例子可在“数学承诺”中写到足以直接执行。
- 不把规划语言设计成正式正文；最终正文仍受 `Notes/WRITING_GUIDE.md` 约束。
