---
task_id: 20260827-s007-lp-learning-path
status: done
target_files:
  - Notes/07-Lifted-Product Code/Hypergraph product code.md
  - Notes/07-Lifted-Product Code/Lifted product code.md
  - Notes/07-Lifted-Product Code/S007 中 LP 码的分层执行.md
  - Notes/00-index.md
  - CANONICAL_KNOWLEDGE.md
---

# 任务目标

重构 `Notes/07-Lifted-Product Code/` 中与 HGP、LP 和 S007 第 6 节直接相关的学习路径，使读者能够从 HGP 的乘积坐标与四类 Tanner 边，推进到 LP 的循环 lift 数据，并最终读懂：

`Translations/S007.full.zh-CN.md` 第 6 节“码的推广：提升乘积码”。

`Translations/S007.full.zh-CN.md` 是本任务的下游验收来源，不是正文修改目标。

# 用户当前卡点或动机

当前 Künneth、HGP 与 LP 三篇笔记虽然已经包含大量数学内容，但现有阅读顺序没有围绕 S007 第 6 节组织。

本任务需要区分：

- HGP 的外层乘积坐标与两个物理比特扇区；
- Kronecker blocks 产生的四类 Tanner 边；
- 行／列方向的一维执行分解；
- LP 中的 lift-level 节点与单个 lift 内的副本指标；
- 单项式 `x^k` 表示的循环移位；
- S007 图 12 中提升间重排、提升内重排、门执行和定向转移的关系；
- Künneth 对构造、逻辑空间和维数公式的不同作用。

# 本次范围

详细文件处理、数学承诺、执行批次和验收条件以本任务目录中的 `PLAN.md` 为准。

本任务包括：

- 重写 `Hypergraph product code.md` 的核心构造主线；
- 重写并重排 `Lifted product code.md` 的核心构造主线；
- 新建 `S007 中 LP 码的分层执行.md`；
- 最小更新 `Notes/00-index.md`；
- 最小更新 `CANONICAL_KNOWLEDGE.md`；
- 将 Künneth 标记为逻辑空间、维数公式和一般系数边界的可选数学支线。

未经用户明确批准 `PLAN.md`，不得开始修改正式文件。

# 本次不处理

- 不修改 `Künneth 分解.md` 正文；
- 不猜测或补建 S007 具体 LP 码未展示的第二个因子；
- 不从式 (2) 独立推导 `2610`、`744` 或距离界；
- 不仅凭矩阵 `A` 重建完整 data/X/Z-check sector；
- 不修改 S007 译文、PDF、截图或 Papers 管理文件；
- 不展开 ONEX 的 SMT、MILP 或完整编译算法；
- 不对 HGP、LP 中已冻结的距离、渐近参数、非阿贝尔构造和解码结论做语义重写；
- 不修改与本任务无关的正式笔记。

# 完成标准

- HGP 笔记能够从两张经典校验矩阵推出两个物理扇区、CSS blocks、四类 Tanner 边及行／列分解；
- LP 笔记能够区分外层 product skeleton、lift-level 节点和单个 lift 内的循环副本；
- S007 应用笔记能够解释式 (2)、图 12 和四阶段执行，同时明确来源不能支持的结论；
- Künneth 不再被误设为理解 HGP/LP 构造与 S007 执行的强制前置；
- `Notes/00-index.md` 与 `CANONICAL_KNOWLEDGE.md` 和正式正文保持一致；
- 各执行批次通过 `PLAN.md` 与 `subagents.md` 要求的只读检查；
- 正文符合 `Notes/WRITING_GUIDE.md`；
- 不残留未说明的来源缺口、计划语言、工具痕迹或失效链接。
