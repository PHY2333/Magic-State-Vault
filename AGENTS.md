# AGENTS.md

本仓库是研究知识库。除非用户明确给出不同指令，所有 agent 均遵守本文件；`.md` 文件按 UTF-8 读取。

## 1. 目录与文件职责

- `AGENTS.md`：入口规则和执行边界。
- `Notes/`：可长期复用的正式笔记；`Notes/00-index.md` 是面向读者的知识路线图。
- `Notes/WRITING_GUIDE.md`：正式知识笔记的正文写作判断。
- `Notes/WORKFLOWS/note-writing.md`：复杂笔记任务的阶段、交接和停止条件。
- `Notes/WORKFLOWS/planning-contract.md`：Context Builder 与 Planner 的输入、输出和边界。
- `Notes/WORKFLOWS/execution-contract.md`：Executor 的执行前检查、修改权限和交付规则。
- `Notes/WORKFLOWS/subagents.md`：只读 Reviewer/Subagent 的检查规则。
- `Notes/WORKING/note-tasks/<task-id>/`：复杂写作任务的临时交接区，不属于正式知识。
- `CANONICAL_KNOWLEDGE.md`：面向 agent 的 canonical ownership、固定记号、适用范围和必要来源关系索引。
- `Papers/`：论文原文、论文管理和论文关系；管理入口为 `Papers/PAPER_MANAGEMENT.md`。
- `Translations/`：全文或局部翻译稿；规则入口为 `Translations/TRANSLATION_GUIDE.md`。
- `Translations/Snapshots/<文献ID>/`：翻译中使用的原文截图，按来源自身的稳定 ID 分目录保存。

不要在多个文件中重复展开同一条规则。`Notes/WRITING_GUIDE.md`、`Notes/WORKFLOWS/` 和 `Notes/WORKING/` 是系统区，不属于正式知识笔记；正式知识笔记位于 `Notes/00-index.md` 和各主题目录中。单次任务产物只能放入对应的 `Notes/WORKING/note-tasks/<task-id>/`，不得散落在正式主题目录或 `Notes/WORKFLOWS/`。

## 2. 复杂笔记任务的入口

新增正式笔记、整篇重写、长推导整理、论文转写、合并、拆分或学习路径重组时，必须依次读取：

1. `Notes/WRITING_GUIDE.md`
2. `Notes/WORKFLOWS/note-writing.md`
3. 与当前角色对应的 contract
4. `CANONICAL_KNOWLEDGE.md`
5. `Notes/00-index.md`
6. 目标文件及相关上下游文件

改错字、修链接、移动文件、纯格式化和用户明确指定的短小局部修改可跳过规划流程，但不得改变数学含义、笔记边界或 canonical ownership。

## 3. 文献与翻译任务分流

以下文献来源管理任务必须先读取 `Papers/PAPER_MANAGEMENT.md`：新增、去重、替换、改名或删除 paper/book；登记新版本；改变阅读状态；登记主文献与辅助文献关系。

全文翻译或局部摘译必须先读取 `Papers/PAPER_MANAGEMENT.md`，确认文献 ID、文件和版本，再执行 `Translations/TRANSLATION_GUIDE.md`。翻译本身不属于正式知识笔记；若任务同时新增、改写、拆分知识笔记或从文献迁移概念，仍须执行复杂笔记流程。

全文翻译的写入条件、进度记录和验收按 `Translations/TRANSLATION_GUIDE.md` 执行。不得以“只是翻译”为由把重组解释或新推导写入译文，也不得用译文绕过正式知识笔记的写作流程。

## 4. 不同问题的权威来源

- 任务范围和目标：用户最新的明确指令。
- 仓库事实：当前工作树和有效的 `CONTEXT.md`。
- 数学事实与出处：已核对的论文、教材、翻译及 canonical note。
- 教学与正文主线：用户批准的 `PLAN.md`。
- 正式正文文体：`Notes/WRITING_GUIDE.md`。
- 流程与阶段：`Notes/WORKFLOWS/` 中的 contract。

这些来源发生冲突时，不得静默选择、折中或猜测。停止相关步骤，在 `REVIEW.md` 或交付回执中写明冲突及所需决定。

## 5. 角色边界

- Context Builder：建立仓库上下文，不设计教学主线。
- Planner：根据上下文设计计划，不修改仓库。
- Executor：只执行已批准且未过期的计划；不得静默改变范围、证明策略或拆分方案。
- Reviewer/Subagent：只读检查，不修改文件。

不得声称读取了未实际读取的文件，不得根据文件名推断内容。

## 6. 知识归属

同一概念、构造或完整推导只保留一个主笔记。规划新文件前必须检查：

- 是否已有主笔记；
- 是否应合并到旧笔记；
- 是否应拆成前置笔记；
- 是否需要更新 `CANONICAL_KNOWLEDGE.md` 或 `Notes/00-index.md`。

已有主笔记能承担的背景，不在当前笔记重复展开。引用已有笔记时，说明采用哪个结论，以及它用于当前哪一步。新增、合并、拆分或迁移方案必须进入 `PLAN.md` 并由用户批准后，Executor 才能实施。

## 7. 强制交付回执

每次任务结束或被阻塞时，向用户输出：

```md
### 流程回执
- `task_id`：
- 当前阶段：
- 已完成：
- 阻塞或待确认：
- 下一位执行者：
- 下一步唯一动作：
- 用户可直接回复：
```

不得只报告“已完成”，也不得在未满足阶段条件时自动进入下一阶段。交付还应按任务实际情况说明：修改文件和内容放置理由；是否新增前置笔记；是否更新 `CANONICAL_KNOWLEDGE.md` 或 `Notes/00-index.md`；任务目录是创建、保留、归档还是删除；若涉及文献或翻译，来源登记、版本、阅读状态、主辅关系、翻译范围、截图与验收状态；以及是否仍有 `待核对`、`TODO：补引用` 或 `待补推导`。
