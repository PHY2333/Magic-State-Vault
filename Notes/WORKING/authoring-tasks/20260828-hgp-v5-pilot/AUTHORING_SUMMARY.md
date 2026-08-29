---
task_id: 20260828-hgp-v5-pilot
status: integration_previewed
retain_mode: full
final_design_revision: 5
final_draft_revision: 5
---

# Goal and stop point

为 `Notes/07-Lifted-Product Code/Hypergraph product code.md` 的 U01/U02 完成一次 Notes v5 全流程 pilot：mapping、faceted learner snapshot、didactic/definition/claim/depth/mainline design、Design Audit、隔离 packets/cards、staged drafts、双审查、manuscript verdict 与只读 Integration Preview。

最终状态为 `integration_previewed`。没有执行 formal integration，也没有修改任何正式笔记、index 或 canonical。

# Final artifacts

```text
TASK.md
BRIEF.md
DOMAIN_MODEL.md
SOURCE_PACKET.md
LEARNER_SNAPSHOT.md
DIDACTIC_DESIGN.md
DESIGN_AUDIT.md
PACKETS/U01.md
PACKETS/U02.md
READER_CARDS/U01.md
READER_CARDS/U02.md
DRAFTS/U01.md
DRAFTS/U02.md
CONTRACT_AUDIT.md
COLD_READ_AUDIT.md
MANUSCRIPT_VERDICT.md
ISOLATION_LOG.md
INTEGRATION_PREVIEW.md
AUTHORING_SUMMARY.md
```

`retain_mode: full`：全部任务产物保留，不创建 `INTEGRATION_REPORT.md`，不归档或删除历史。

# Revision history

## Design

| revision | gate | result / return |
|---:|---|---|
| 1 | Design Audit | changes_required：5 major、1 minor |
| 2 | Design Audit | changes_required：1 major、2 minor |
| 3 | Design Audit | pass |
| 4 | Cold-read feedback reopen | 修复支撑／泡利类型的 definition 边界；完整 Design Audit pass |
| 5 | Integration Preview feedback reopen | 两个 U02 标题改为同级 `###`；完整 Design Audit pass |

Design 返修次数：**4**（初稿之后四次 revision）。

## Manuscript

| draft revision | Contract Audit | Blind Cold Read | outcome |
|---:|---|---|---|
| 1 | pass | changes_required | 局部概念表述、模 2 表述、标题／数学排版与 A/B 回指返修 |
| 2 | pass | changes_required | 支撑闭合暴露 design definition 矛盾；返回 Design revision 4 |
| 3 | pass | pass | Manuscript pass；Integration Preview 返回 heading hierarchy |
| 4 | pass | pass | heading-only 返修后最终 manuscript pass |
| 5 | pass | pass | 最终审查返修：U02 首句明确“第一步”与“矩阵条件”；新 blind context 增加 cross-unit continuity 并通过 |

Revision 4 首次 Blind run 因 Reader Card 将“两支映射”误写成“三项映射”而 blocked；Card Builder 只修正该数量笔误，draft 未变，新的 blind context 全量重读后 pass。

Manuscript 返修次数：**4**（draft 1→2→3→4→5）。

# Key design result

- U01：三短段；稳定首句；相邻第二句说明奇偶校验矩阵；明确构造／HGP 码、A/B 输入／H_X/H_Z 输出、共享列／行支撑及 CSS 当前对易问题；唯一末问不变。
- U02-P1：五个必要主线阶段；计算基短推导和异比特张量因子规则在主线；完整 \(2\times2\) 计算可折叠；得到 \((-1)^w\)、偶数重叠、矩阵元和 \(H_XH_Z^T=0\)，并用 \([1]\) 封闭共享列误读。
- U02-P2：五段解释三个坐标空间、两支映射与零复合；对象和用途闭合后才命名链复形；末句返回由 \(A,B\) 构造并证明恒零。
- Explanation depth 由出口能力、centrality、risk、mainline cost 和 duplication 决定；`unverified` 没有自动触发 full derivation。
- 两个 U02 标题最终使用 `###`，与正式 HGP 既有 sections 同级；标题文字和正文不变。

# Sources and canonical detail boundary

- 同比特 \(XZ=-ZX\) 有仓库稳定 Pauli 锚点，并在正文用计算基 local derivation 真正闭合。
- 异比特对易、总符号与矩阵元重叠奇偶由 Source Packet 的显式 local derivations 闭合，没有未说明的模型常识。
- CSS 的完整 logical/syndrome 与对偶细节由 `CSS码中的cochain complex.md` 承担。
- generic chain/cochain、cycle/boundary/homology 由 `Chain complex 与 cochain complex.md` 承担。
- HGP blocks 与两路径抵消继续由正式 HGP 当前第 102–165 行承担。

# Isolation

- U01/U02 Writer：两个 `fork_turns: none` 上下文，各自只读当前 unit packet，只返回正文文本，不写文件。
- Contract Auditor：每个 draft revision 使用新上下文，只读 packets、Source Packet、drafts、Language Profile；不得见 Blind verdict。
- Blind Reader：每个 draft revision 使用另一新上下文，只读 Reader Cards、drafts、Language Profile；不得见 packet、design、source、canonical/index、正式 HGP 或 Contract Audit。
- Gatekeeper：只合并同 revision audits，并由 `ISOLATION_LOG.md` 与 Git 基线核验 Writer 写入范围。
- Integration Preview：新 Fit Planner 上下文，只读 passed drafts、正式目标、owner/index/canonical 和允许的 design duplication ledger；不写文件。

# Final gates

| artifact | final status | reviewed revision |
|---|---|---:|
| `DESIGN_AUDIT.md` | pass | design 5 |
| `CONTRACT_AUDIT.md` | pass | draft 5 |
| `COLD_READ_AUDIT.md` | pass | draft 5 |
| `MANUSCRIPT_VERDICT.md` | pass | draft 5 |
| `INTEGRATION_PREVIEW.md` | ready | draft 5 |

Mainline latency、explanation proportionality 与 optional skip test 均 pass。

# Integration Preview result

- U01 替换当前第 1 行；U02 紧接 U01；其末句直接交给当前 `### 从两张经典校验矩阵开始`。
- 保留当前第 39–51 行，用于把 U02 的映射语义绑定到后续计算使用的 \(\partial_2,\partial_1\) 与 \(H_X,H_Z\) convention。
- 只删除当前第 53–70 行的 logical quotient / dual cochain 提前说明；保留第 3–51 行及第 72–447 行，尤其完整保留第 102–165 行 HGP 构造性证明。
- 删除第 53–70 行后，首次 \(H_1(\mathcal A\otimes\mathcal B)\) 仍在“长度、秩与可选逻辑空间分解”标题下；公式前的“进一步分解逻辑空间”句与现有 `Künneth 分解#二项复形与 HGP 逻辑空间` owner anchor 提供足够落点，无需新桥梁。
- 新增 link 计划 0。
- 规划最小 frontmatter：`reference + guided + reviewed`。
- index 与 canonical 无需改变。
- Preview `ready` 只表示适配方案可执行；`formal_integration_authorized: false`。

# Repository and protection result

- `git status --short`：只有本任务目录未跟踪。
- `git diff --name-only` 与 `git diff --cached --name-only`：空。
- 正式 HGP、`Notes/00-index.md`、`CANONICAL_KNOWLEDGE.md` blobs 与 pilot 前基线一致。
- 没有修改正式主题笔记、学习路线、canonical 条目、论文、译文或截图。
- 没有新增前置笔记。
- 没有 `待核对`、`TODO：补引用` 或 `待补推导`。

# Blocker and next action

Blocker：无。

下一步唯一动作：由用户与 ChatGPT Pro 审查 v5 结果；本任务不执行 formal integration。
