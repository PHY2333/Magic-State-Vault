---
task_id: 20260831-kunneth-pro-rerun
route: pro-write-review
status: PREPARE
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md

integrity: fast
review_policy: fresh
audit_retention: errors-only

git:
  remote: main
  branch: codex/kunneth-pro-rerun-20260831
  base_commit: 9fdc692302b92de2383e4522b5e1d1fc039e9c2a

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

用户已更新 `Notes/WRITING_GUIDE.md` 与 `Notes/TEMPLATES/REVIEW_REQUEST.md`，并要求先把这两项更新推送到远程 `main`，再对 `Notes/07-Lifted-Product Code/Künneth 分解.md` 完整重跑 Pro 写作与独立全文审查流程。

# 当前真实问题

- 上一轮 fresh-review 最终稿已修复原稿的主要数学与组织问题，本轮以该稿为内容基线，不退回主分支旧稿。
- 新版 Writing Guide 进一步要求：新对象在首次承重前闭合定义；关键结论的条件、对象、中间关系和用途可追踪；抽象总结可以还原为具体数学内容；前后章节的读者能力连续。
- 现有基线仍有若干需要整篇处理的问题：系数域与分次对象出现顺序不够稳；“自然同构”先于自然性的可操作说明；“干净、隐藏、额外、意外识别”等抽象语言压缩了单射与满射的具体含义；早段 HGP 公式与后文 chain-complex 角色之间的桥梁较晚；谱序列虽列出微分与 $E^\infty$，但缺少“下一页取当前页同调”的最短操作桥梁。
- 这些不是追加补丁的理由。Pro 应从头连续复读并完整重写目标文件，使整篇在新版指南下成为一条自然连续的知识过程。
- 用户先前的数学决定继续生效：以 `CANONICAL_KNOWLEDGE.md`、May 与 Stacks 为边界；S003 补充材料式 (91) 不作为一般定理。

# 本次授权

- 只完整替换 `Notes/07-Lifted-Product Code/Künneth 分解.md`。
- 可以重组目标文件内部标题、段落顺序、例子和证明展开，删除竞争性或不能还原的表述。
- 可以在本任务目录保存请求、应用报告、最终报告和失败响应。
- 可以在本任务分支自动完成 R01、独立 R02、显式暂存、commit 和 push。

# 本次不处理

- 不修改其他正式笔记、`CANONICAL_KNOWLEDGE.md`、`Notes/00-index.md`、Papers 或 Translations。
- 不删除、移动、拆分、合并或重命名正式文件。
- 不改变 Künneth、HGP、LP 或 S007 的 canonical ownership 与学习路线角色。
- 不把任务分支自动合并到 `main`。

# 基线说明

`base_commit` 同时包含：上一轮任务分支经 fresh review 后的 Künneth 正文，以及已从远程 `main` 合入的 Writing Guide / Review Request 更新。旧任务 artifact 保留为历史审计；本轮使用新的 task、request 与 binding，不把旧会话视为已经遵守新指南。

# 当前阶段

`PREPARE`：正在建立并推送新的 R01/R02 初始 checkpoint。
