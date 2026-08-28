---
task_id: 20260828-hgp-v5-pilot
recorded_at: 2026-08-28
draft_revision: 4
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

# Conclusion

Writer 只交付文本，实际写入由 Orchestrator 限定在任务目录。Git 状态和受保护 blob 证明 draft revision 4 之后没有正式笔记、index、canonical 或其它 tracked 文件变化。
