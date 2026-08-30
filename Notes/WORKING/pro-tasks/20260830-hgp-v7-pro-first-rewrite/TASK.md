---
task_id: 20260830-hgp-v7-pro-first-rewrite
route: pro-write-review
status: request-prepared
target_files:
  - Notes/07-Lifted-Product Code/Hypergraph product code.md
git:
  remote: main
  branch: notes/20260830-hgp-v7-pro-first-rewrite
  base_commit: 66536a54b0fa488ade5c4b313bc7b64edff61cf3
automation:
  auto_commit: true
  auto_push: true
  merge_to_main: false
  max_author_rounds: 2
  max_review_rounds: 2
  audit_retention: task-branch-only
---

# 用户目标

运行 Notes v7 的 HGP 端到端测试：由 ChatGPT Pro 内部自行规划并整篇重写 `Hypergraph product code.md`，再由一个全新的 Pro 会话做整篇审查。最终笔记应让目标读者能够：

1. 解释为什么两个经典校验矩阵可以视为二项链复形；
2. 从张量积的 total degree 推出三个链群；
3. 解释中间链群为什么给出两个物理量子比特扇区；
4. 逐块构造 $H_X,H_Z$，说明每个恒等矩阵固定哪个坐标；
5. 解释为什么两条 product path 在 $\mathbb F_2$ 中相消；
6. 从 Kronecker blocks 读出 Tanner 图副本与行／列方向；
7. 区分一般 HGP 记号与 S007 的来源特定记号；
8. 只在逻辑空间问题出现时引入 Künneth；
9. 准确限定 qLDPC、平方根距离基准和 HGP 到 LP 的接口。

# 当前真实问题

- “依赖”“不是前置”“ownership”一类维护语言不能替代面向读者的教学解释。
- 当前笔记前段细致，后段突然退回专家压缩，整篇解释深度不一致。
- 不能让读者独自从矩阵公式反推四个 blocks 的 source、target、坐标和转置语义。
- 长推导需要先给总目标或 proof map，再展开局部步骤。
- S007 适配、Künneth、距离支线与 HGP 到 LP 应分别放置，且不应挤压一般 HGP 主线。

# 本次授权

- 只完整替换 `Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- 可以重组该文件标题、删除重复解释，并把当前文件中的可选细节明确设为选读。
- 可以在本任务目录保存请求、原始 Pro 响应、解析 manifest、检查结果、应用报告和最终报告。
- 可以在本任务分支显式暂存、提交并 push；不合并主分支。

# 本次不处理

- 不修改任何其他正式笔记、`CANONICAL_KNOWLEDGE.md`、`Notes/00-index.md`、Papers 或 Translations。
- 不删除、移动、拆分、合并或重命名正式文件。
- 不改写旧任务 artifact，不接入旧 v1–v6.1 工作流。
- 不修改或合并脏 `main`，不重写 Git 历史。

# 当前阶段

`request-prepared`：R01 作者请求已准备，等待 checkpoint commit/push 后通过 Browser 交给 ChatGPT Pro。
