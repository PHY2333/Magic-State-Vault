# AGENTS.md

本仓库是研究知识库。除非用户明确给出不同指令，所有 agent 均遵守本文件；`.md` 文件按 UTF-8 读取。

## 1. 目录与文件职责

- `AGENTS.md`：入口规则和执行边界。
- `Notes/`：可长期复用的正式笔记；`Notes/00-index.md` 是面向读者的知识路线图。
- `Notes/AGENTS.md`：Notes 类型、教学设计、写作、审查与读者反馈的统一入口。
- `Notes/WORKING/`：Notes 任务的临时交接区；新任务路径与阶段由 `Notes/AGENTS.md` 规定，历史任务目录只作保留。
- `CANONICAL_KNOWLEDGE.md`：面向 agent 的 canonical ownership、固定记号、适用范围和必要来源关系索引。
- `Papers/`：论文原文、论文管理和论文关系；管理入口为 `Papers/PAPER_MANAGEMENT.md`。
- `Translations/`：全文或局部翻译稿；规则入口为 `Translations/TRANSLATION_GUIDE.md`。
- `Translations/Snapshots/<文献ID>/`：翻译中使用的原文截图，按来源自身的稳定 ID 分目录保存。

不要在多个文件中重复展开同一条规则。Notes 写作统一路由到 `Notes/AGENTS.md`；`Notes/WORKING/` 是系统区，不属于正式知识笔记。正式知识笔记位于 `Notes/00-index.md` 和各主题目录中；单次任务产物按 `Notes/AGENTS.md` 指定的路径保存，不得散落在正式主题目录。

## 2. Notes 任务入口

新增正式笔记、整篇重写、长推导整理、论文转写、合并、拆分、学习路径重组，或处理教学设计与读者反馈时，先读取 `Notes/AGENTS.md`，再按其路由执行活动流程。

改错字、修链接、移动文件、纯格式化和用户明确指定的短小局部修改可跳过完整 Notes 流程，但不得改变数学含义、笔记边界或 canonical ownership。

## 3. 文献与翻译任务分流

以下文献来源管理任务必须先读取 `Papers/PAPER_MANAGEMENT.md`：新增、去重、替换、改名或删除 paper/book；登记新版本；改变阅读状态；登记主文献与辅助文献关系。

全文翻译或局部摘译必须先读取 `Papers/PAPER_MANAGEMENT.md`，确认文献 ID、文件和版本，再执行 `Translations/TRANSLATION_GUIDE.md`。翻译本身不属于正式知识笔记；若任务同时新增、改写、拆分知识笔记或从文献迁移概念，转交 `Notes/AGENTS.md`。

全文翻译的写入条件、进度记录和验收按 `Translations/TRANSLATION_GUIDE.md` 执行。不得以“只是翻译”为由把重组解释或新推导写入译文，也不得用译文绕过正式知识笔记的写作流程。

## 4. 不同问题的权威来源

- 任务范围和目标：用户最新的明确指令。
- 仓库事实：当前工作树和 `Notes/AGENTS.md` 指定的当前阶段产物。
- 数学事实与出处：已核对的论文、教材、翻译及 canonical note。
- Notes 类型、教学设计、正文写作与流程阶段：`Notes/AGENTS.md`。

这些来源发生冲突时，不得静默选择、折中或猜测。停止相关步骤，按对应权威入口记录冲突，并在交付回执中写明所需决定。

## 5. 角色边界

Notes 任务的角色、阶段门、修改权限与上下文隔离统一由 `Notes/AGENTS.md` 规定；文献管理与翻译任务分别遵守各自入口。

不得声称读取了未实际读取的文件，不得根据文件名推断内容。

## 6. 知识归属

同一概念、构造或完整推导只保留一个主笔记。规划新文件前必须检查：

- 是否已有主笔记；
- 是否应合并到旧笔记；
- 是否应拆成前置笔记；
- 是否需要更新 `CANONICAL_KNOWLEDGE.md` 或 `Notes/00-index.md`。

已有主笔记能承担的背景是否在当前笔记局部重述，按 `Notes/AGENTS.md` 与 `Notes/WRITING_GUIDE.md` 判断，不得另立第二个 canonical owner。引用已有笔记时，说明采用哪个结论，以及它用于当前哪一步。新增、合并、拆分或迁移方案必须按 `Notes/AGENTS.md` 完成设计、审查与整合阶段，不得绕过阶段门实施。

## 7. 强制交付回执

Notes 任务使用 `Notes/AGENTS.md` 规定的流程回执；其它任务使用以下格式。

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
