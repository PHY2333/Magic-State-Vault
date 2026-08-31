---
task_id: 20260831-kunneth-pro-rewrite
route: pro-write-review
status: R02_APPLIED
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md

integrity: fast
review_policy: fresh
audit_retention: errors-only

git:
  remote: main
  branch: notes/20260831-kunneth-pro-rewrite
  base_commit: 76e859d91e733b08b89199506f20628fcdabe311

automation:
  run_to_completion: true
  standing_authorization: true
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 1
  preauthorized_browser_rounds:
    - R01
    - R02
  stop_only_on:
    - permission_required
    - account_mismatch
    - needs_context
    - decision_required
    - blocked
    - source_conflict
    - structural_file_change
    - path_outside_allowlist
    - math_check_failure
    - push_failure
    - merge_to_main
---

# 用户目标

按 Notes Pro-First 1.0 流程与 ChatGPT Pro 合作，整篇重写 `Notes/07-Lifted-Product Code/Künneth 分解.md`，再由一个全新的 Pro 会话从头审查整篇。最终稿应让读者先形成 Künneth 定理解决什么问题的整体认识，再理解域上证明、HGP 的 degree-$1$ 应用，以及系数不是域时结论为何改变。

# 当前真实问题

- 用户的直接反馈是“写得不好，需要重新写”，因此本任务不是局部修补。
- 现稿直到很后面才给出域上的主结论和 HGP 回报，读者先承担大量证明 bookkeeping，却不知道证明服务什么目标。
- 解释深度倒置：补空间、单射满射与自然性过度展开，而 derived tensor product、K-flat、谱序列、filtration 和 extension 在短篇幅内集中出现。
- 现稿缺少一个先展示域上分解如何工作的紧凑成功例子；唯一完整例子是一般环上的失败反例。
- “同调扇区”容易与 HGP 的两个物理比特扇区混淆，应改用“两类逻辑来源”或“Künneth 直和项”等准确说法。
- 一般环内容属于必要边界，但不应打断域上定理与 HGP 应用组成的主线。
- 来源核验发现真实冲突：S003 补充材料式 (91) 对有限维域代数给出无条件 Künneth 直和，而 May、Stacks、当前 canonical 边界以及本笔记的 $R_2$ 直接反例不支持这一推广。流程禁止静默选择，需由用户决定本任务是否以 canonical + May/Stacks 为准并把 S003 式 (91) 列为不得采用的缺失假设来源。

# 用户决定

用户已明确决定：本任务以 `CANONICAL_KNOWLEDGE.md`、May 与 Stacks 为数学边界；S003 式 (91) 不作为一般定理。Pro 不得引用该式支持无条件的一般环 Künneth 直和，也不得静默调和冲突。

# 本次授权

- 只完整替换 `Notes/07-Lifted-Product Code/Künneth 分解.md`。
- 可以重组整篇顺序、标题和证明展开，删除重复解释，并加入服务主线的紧凑 worked example。
- 可以在本任务目录保存请求、应用报告、最终报告以及失败响应。
- 可以在本任务分支完成 R01、R02 的显式暂存、commit 和 push。

# 本次不处理

- 不修改其他正式笔记、`CANONICAL_KNOWLEDGE.md`、`Notes/00-index.md`、Papers 或 Translations。
- 不删除、移动、拆分、合并或重命名正式文件。
- 不改变 Künneth、HGP、LP 或 S007 的 canonical ownership。
- 不把任务分支自动合并到 `main`。

# 当前阶段

`R02_APPLIED`：fresh reviewer 返回完整修正版；R02 已通过 binding、allowlist、Obsidian 数学、锚点和 diff 检查，并应用到唯一目标文件。应用 commit/push 后生成最终报告。
