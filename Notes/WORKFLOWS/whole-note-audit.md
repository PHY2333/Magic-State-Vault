# Notes/WORKFLOWS/whole-note-audit.md

Whole-note Coverage Auditor 由 Codex Sol 承担。它只建立整篇勘察与风险地图，不作最终教学设计。

## 1. 适用条件

- legacy 正文与 validated units 混合；
- 整篇重写；
- 超过两个 section 的教学质量未知；
- 用户指出前后视角、难度或主线不一致；
- 文件可能混合 reference、lesson、derivation 或 paper-guide 职责。

## 2. 输出

生成：

```text
SECTION_COVERAGE.md
WHOLE_NOTE_AUDIT.md
PRO_HANDOFF.md
PRO_REQUESTS/ARCHITECTURE.md
```

Review state：

- `validated`：已有 exact unit gate；
- `legacy-audited`：已勘察，不等于 manuscript pass；
- `legacy-unreviewed`：证据不足；
- `changes-required`：需进入 Pro design。

## 3. 每节检查

- reader entry、实际假设和 exit；
- hidden premises；
- 当前讲解模式与主问题；
- explanation depth 与比例；
- 数学、来源和约定风险；
- source-specific/general 层级；
- 与前后 section 的能力跳变；
- 重复、owner 与 optional skip；
- 中文术语、Obsidian 数学和维护语言。

## 4. Unit boundary 的地位

Coverage Auditor 可以提出 future unit hypotheses，但必须明确：

- 行号只作 legacy evidence；
- unit map 不是已批准设计；
- Pro Architect 可以合并、拆分、重排或否决；
- 用户不审批 technical unit map。

## 5. 完成与自动 handoff

无 blocker 时：

1. 生成 `PRO_REQUESTS/ARCHITECTURE.md`；
2. 更新 `TASK.md` 为 `awaiting_pro_design`；
3. 按 `git-automation.md` 检查、commit、push；
4. 在 push 成功后输出可直接复制给 ChatGPT Pro 的 Architecture Prompt；
5. 停止。

若 push 失败，则状态为 `awaiting_remote_sync`，不得发出 Pro prompt。
