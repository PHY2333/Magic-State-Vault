---
task_id: 20260828-hgp-v4-pilot
status: manuscript_validated
retain_mode: full
base_commit: 800575575cd2cb4f110869120b50c91b06ce5e78
target_files:
  - Notes/07-Lifted-Product Code/Hypergraph product code.md
---

# 目标

- 完整验证 Notes v4 从 mapping 到双正文审查与最终 manuscript verdict 的流程。
- 只设计并起草 HGP 开头的 U01、U02，让读者从构造类别与输入／输出推进到 CSS 对易、Pauli 局部交换规则和三项零复合。
- 最终状态最多到 `manuscript_validated`。

# 授权范围

- 读取 v4 指导文件、目标 HGP 笔记、相关正式笔记、canonical/index 与历史 pilot，完成 mapping、设计和审查。
- 只在本任务目录创建 v4 任务产物、Writer packets、Reader Cards、staged drafts 与审查文件。
- 使用隔离 Writer、Contract Auditor 与 Blind Reader；Writer 和 Blind Reader 均不得越过各自允许上下文。

# 非目标

- 不修改 `Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- 不修改 `Notes/00-index.md`、`CANONICAL_KNOWLEDGE.md`、任何其它正式笔记或长期 learner 文件。
- 不执行 integration，不生成 `INTEGRATION_REPORT.md` 或 `AUTHORING_SUMMARY.md`。
- 不引入 Kronecker blocks、输入矩阵尺寸、total degree、两路径抵消、homology 或 Künneth。

# 当前阶段

- 分支：`codex/notes-v4-install`。
- 基线干净；目标正式文件在 pilot 开始时无未提交改动。
- `DOMAIN_MODEL.md` 与 `SOURCE_PACKET.md` 已闭合四类关系和解释 premise inventory；状态经过 `mapped`。
- `LEARNER_SNAPSHOT.md` 已按 facet 建立；状态经过 `learner_ready`。
- `DIDACTIC_DESIGN.md` 经 3 次内部返修到 revision 4；`DESIGN_AUDIT.md` 已 `pass`。
- `PACKETS/U01.md`、`PACKETS/U02.md` 与独立的 `READER_CARDS/U01.md`、`U02.md` 已完成 preflight。
- draft revision 1 的 Contract Audit 通过，Blind Cold Read 要求补充 `I`、`\mathbb F_2` 的局部说明并统一数学字体。
- draft revision 2 的 Contract Audit 通过，Blind Cold Read 要求区分“通用判据”与“具体 HGP 构造的自动满足性”。
- 已完成第 2 次 manuscript 返修到 draft revision 3；Contract Audit 与 Blind Cold Read 均 `pass`。
- `MANUSCRIPT_VERDICT.md` 为 `pass`。当前状态：`manuscript_validated`；按授权停止，不进入 integration。
