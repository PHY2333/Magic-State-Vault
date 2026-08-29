---
task_id: 20260829-hgp-whole-note-coverage-audit
status: changes-required
audit_type: whole-note-coverage
retain_mode: full
target: Notes/07-Lifted-Product Code/Hypergraph product code.md
target_head: e837e97b8c35f0cad9f2a6b5ded7d9ea4c87f2ee
target_blob: 3251b0075281fdf4dc86fccb230ae44397732bad
reader_visible_writes: false
whole_note_reviewed: false
---

# 学习目标

- 可观察表现：按当前每个标题和标题前开头建立 coverage map，区分读者进入该节时实际具备的能力、正文额外假设的能力以及读完后的出口能力。
- 可观察表现：定位 whole-note 重构所需的 unit 边界、主线断点、解释深度失衡、术语问题、数学／来源风险和跨节重复。
- 可观察表现：只继承 revision 5 对 U01/U02 的既有 `validated` 结论，不把该结论推广到 legacy preserved text 或整篇文件。

# 目标材料

- 正式目标：`Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- 审计基线：HEAD `e837e97b8c35f0cad9f2a6b5ded7d9ea4c87f2ee`；目标 Git blob `3251b0075281fdf4dc86fccb230ae44397732bad`。
- 已知通过范围：标题前 U01（当前第 7–11 行）及 U02 的两个 phase（当前第 13–105 行）。依据是 `20260828-hgp-v5-pilot/MANUSCRIPT_VERDICT.md` 对 revision 5 U01/U02 的明确限定。
- Legacy 范围：当前第 107–532 行；上次 integration 只按 preview 保留该范围，没有对其执行 v5 manuscript gate。

# 当前真实问题

当前正式文件把 guided opening、一般 HGP 构造、S007 记号对照、Tanner 图方向、参数推导、Künneth 支线和 LP 预告放在同一连续 reference 中。需要判断这些 section 是否形成可持续的能力阶梯，以及哪些内容必须在未来 whole-note 重构中重新分 unit、重新 mapping 或改变 detail placement。

# 已有证据

- U01/U02 的 exact revision 5 fingerprints、Contract Audit、Blind Cold Read 和 Manuscript Verdict 均已通过；其 scope 明确只含 U01/U02。
- `Notes/00-index.md` 把 HGP 的核心入口职责限定为 HGP blocks、两个物理量子比特扇区、四类 Tanner 边与行／列乘积方向；Künneth 是可选数学支线。
- `CANONICAL_KNOWLEDGE.md` 把一般 product differential、Künneth 推导、CSS logical quotient、LP 代数和 S007 论文特例分配给不同 owner。
- 仓库中的 tensor-product complex、Künneth、LP、S007 paper-guide 和 S007 arXiv v1 译本／PDF 提供了可定位的本地锚点。
- Tillich–Zémor arXiv:0903.0566v2 与 Panteleev–Kalachev arXiv:2012.04068v2 的官方 arXiv 页面支持 HGP 平方根家族和 LP 的原始范围；但这两项尚未在 `Papers/SOURCES.md` 建立稳定本地版本记录。

# Review state 语义

- `validated`：只用于已经通过相应 v5 manuscript gate 的 exact reader-visible unit；本任务不能新增此状态。
- `legacy-audited`：本次已完成 coverage audit，未发现必须先改写才能继续使用的 section；它不等于 Contract Audit、Blind Cold Read 或 manuscript pass。
- `legacy-unreviewed`：本次没有获得足够内容或来源证据，不能完成 coverage 判断。
- `changes-required`：已发现能力跳变、premise／depth／placement、语言、数学范围、来源或 ownership 问题；未来须返回相应阶段处理。

# 非目标

- 不修改任何 reader-visible 正文、frontmatter、标题、公式、链接或来源列表。
- 不修改 `Notes/00-index.md`、`CANONICAL_KNOWLEDGE.md`、Papers、Translations 或旧任务。
- 不生成 Writer Packet、Reader Card、Draft、Contract Audit、Cold Read、Manuscript Verdict 或 Integration Preview。
- 不把当前正式文件标为整篇 reviewed，不把 `status: reviewed` 解释为 legacy 已通过。
- 不规定未来正文的逐句措辞；只给 unit 边界、能力合同和风险／返修路由。

# 可能需要用户决定

- 未来设计若要把完整 S007 convention adapter 从 HGP reference 迁到现有 paper-guide，需要同时决定 canonical ownership 与入站 anchor 的长期位置；本审计不执行迁移。
- `\sqrt N` 的完整证明可成为本文件 optional derivation，也可成为独立 derivation note；应由后续 Didactic Design 根据出口能力决定。
- 当前 formal frontmatter 的 `status: reviewed` 与 unit-level coverage 不一致；本轮按禁止写正式文件的要求只记录风险，不修改元数据。
