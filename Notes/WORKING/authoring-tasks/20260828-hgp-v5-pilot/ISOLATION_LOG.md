---
task_id: 20260828-hgp-v5-pilot
recorded_at: 2026-08-29
draft_revision: 5
---

# Isolation and write-scope log

## Repository baseline

- worktree: `D:/MyKnowledgeBase/Magic State Vault/.tmp/notes-v5-install`
- branch: `codex/notes-v5-install`
- HEAD / clean tracked baseline: `40ed879dab4601858db6a1a56742ad4fdb4fdaf6`
- pilot authorization: task directory only；正式 HGP、index、canonical 及其它 tracked 正式文件只读

## Writer handoff

两个 Writer 均由 Orchestrator 以 `fork_turns: none` 建立为全新上下文：

| writer | allowed read | forbidden context | write behavior |
|---|---|---|---|
| U01 Writer | 仅 `PACKETS/U01.md` | Reader Card、Design、Domain、Source Packet、canonical/index、正式 HGP、audits、U02 packet | 明确指令“不要修改文件系统”；只在 agent message 中返回 reader-visible text |
| U02 Writer | 仅 `PACKETS/U02.md` | Reader Card、Design、Domain、Source Packet、canonical/index、正式 HGP、audits、U01 packet | 明确指令“不要修改文件系统”；只在 agent message 中返回 reader-visible text |

返修时复用各自仍保持同一白名单的 Writer 上下文；Writer 只重新读取更新后的当前 unit packet，不读取 Cold Read 或其它任务产物。Revision 4 只由 U02 Writer 把两个标题标记从 `##` 改为 `###`，U01 正文不变。Orchestrator 将 Writer 返回文本用 `apply_patch` 写入 `DRAFTS/U01.md` 与 `DRAFTS/U02.md`。Writer 本身没有获得正式文件写入任务，也没有写入任何路径。

## Auditor separation

| role | context | allowed read | expressly excluded |
|---|---|---|---|
| Contract Auditor | 每个 draft revision 使用新的 `fork_turns: none` 上下文 | 当前 packets、Source Packet、drafts、Language Profile | Reader Cards、Cold Read、design、canonical/index、正式 HGP、旧 verdict |
| Blind Reader | 每个 draft revision 使用另一个新的 `fork_turns: none` 上下文 | Reader Cards、drafts、Language Profile | packets、design、domain、source、Contract Audit、canonical/index、正式 HGP、旧 Cold Read/verdict |

Blind Reader 的首次 verdict 及后续每轮 verdict 均在看不到 Contract Audit 的上下文中产生。

## Git write-scope verification after draft revision 4

命令与结果：

```text
git status --short
?? Notes/WORKING/authoring-tasks/20260828-hgp-v5-pilot/

git diff --name-only
<empty>

git diff --cached --name-only
<empty>
```

因此当前工作树没有任何 tracked 文件修改或 staged 修改；唯一变化是本任务目录中的未跟踪 task artifacts。

当前审稿正文 SHA-256：

| draft | SHA-256 |
|---|---|
| `DRAFTS/U01.md` | `3713ad6565c3f992f402b4372db00efa37b798e56f6ac2d0fde9a04b5a46c585` |
| `DRAFTS/U02.md` | `4e8ebdece7f95c48009c45c684e11d1a88e2df66d56d59bc63cdc022ddbacd5f` |

受保护文件当前 blob 与 pilot 前基线一致：

| protected file | baseline blob | current blob | result |
|---|---|---|---|
| `Notes/07-Lifted-Product Code/Hypergraph product code.md` | `d18e00e59d71aa1615417dbfadf4f60d4b27bd69` | `d18e00e59d71aa1615417dbfadf4f60d4b27bd69` | unchanged |
| `Notes/00-index.md` | `847c0b231fd7471f49a445cb7f0d0426a53285cb` | `847c0b231fd7471f49a445cb7f0d0426a53285cb` | unchanged |
| `CANONICAL_KNOWLEDGE.md` | `12b3fdb92c5214f4c6e48b54d3a6777cd76ead67` | `12b3fdb92c5214f4c6e48b54d3a6777cd76ead67` | unchanged |

## Revision 5 final-review reopen

- reopen baseline HEAD: `d320a790f6f1aea459e2e828280f20e279a1edd7`
- user-authorized reader-visible change: Orchestrator 只替换 `DRAFTS/U02.md` 首段的第一句；`DRAFTS/U01.md` 未改
- process-metadata repair: `DESIGN_AUDIT.md` 末行的 `design revision 3` 更正为 `design revision 5`
- Writer: 本轮不重开 Writer；用户已给出唯一允许的精确正文替换，不授权其它 reader-visible 改动

### Revision 5 auditor separation

| role | context | allowed read | expressly excluded | result |
|---|---|---|---|---|
| Contract Auditor | 全新 `fork_turns: none` 上下文 | `PACKETS/U01.md`、`PACKETS/U02.md`、`SOURCE_PACKET.md`、U01/U02 drafts、Language Profile | Reader Cards、design/domain/learner、Cold Read、旧 Contract Audit/verdict、canonical/index、正式 HGP | revision 5 全量重审 `pass` |
| Blind Reader | 另一个全新 `fork_turns: none` 上下文 | `READER_CARDS/U01.md`、`READER_CARDS/U02.md`、U01/U02 drafts、Language Profile | packets、design/domain/source/learner、Contract Audit、旧 Cold Read/verdict、canonical/index、正式 HGP | 从 U01 开始全量重读；含 cross-unit continuity；`pass` |

Blind Reader 首次输出使用了非 schema 状态 `minor_revision_required`，同时又判定所有出口、latency、proportionality、optional skip 与 cross-unit continuity 均通过。Orchestrator 只要求同一 blind context 按 `pass | changes_required | blocked` 合法枚举校准 required finding 与 non-blocking observation；未提供 Contract 结论或任何新文件。Blind Reader 不再读取文件，将两条不阻断出口的观察归类为 non-blocking，最终状态为 `pass`。

### Revision 5 draft fingerprints

| draft | SHA-256 |
|---|---|
| `DRAFTS/U01.md` | `3713ad6565c3f992f402b4372db00efa37b798e56f6ac2d0fde9a04b5a46c585` |
| `DRAFTS/U02.md` | `b5fe54e31c51308230fb356373ae3c13c86325991805eff92cc43ebb36de531a` |

### Revision 5 protected scope

Gate 前 `git diff --name-only` 只包含本 task 目录中的 U02、Design Audit 与新双审查产物；`git diff --cached --name-only` 为空。受保护文件仍与 HEAD blob 一致：

| protected file | HEAD / worktree blob | result |
|---|---|---|
| `Notes/07-Lifted-Product Code/Hypergraph product code.md` | `d18e00e59d71aa1615417dbfadf4f60d4b27bd69` | unchanged |
| `Notes/00-index.md` | `847c0b231fd7471f49a445cb7f0d0426a53285cb` | unchanged |
| `CANONICAL_KNOWLEDGE.md` | `12b3fdb92c5214f4c6e48b54d3a6777cd76ead67` | unchanged |

### Revision 5 Repository Fit Planner

Repository Fit Planner 由新的 `fork_turns: none` 上下文执行。它只读 manuscript verdict、revision 5 drafts、U01/U02 的 depth/placement ledger、目标正式 HGP、相关 owner notes、NOTE_TYPES/LANGUAGE_PROFILE、index/canonical 和只读 Git 基线；明确不读 stale `INTEGRATION_PREVIEW.md`、双审查、packets/cards 或其它任务背景。

Fit Planner 只在 agent message 中返回 preview，未修改文件。Orchestrator 将返回结果写入任务目录的 `INTEGRATION_PREVIEW.md`。结果为 `ready`，且 `formal_integration_authorized: false`。

# Conclusion

Revision 5 的唯一正文改动是用户指定的 U02 首句；新 Contract Auditor 与新 Blind Reader 的输入白名单相互隔离。Git 状态和受保护 blob 证明没有正式笔记、index、canonical 或其它 task 目录外文件变化。
