---
status: ready
task_id: 20260828-hgp-v5-pilot
reviewed_draft_revision: 4
manuscript_verdict: pass
target: Notes/07-Lifted-Product Code/Hypergraph product code.md
formal_integration_authorized: false
---

# Target placement

本 preview 绑定到以下只读基线：

- Git HEAD：`40ed879dab4601858db6a1a56742ad4fdb4fdaf6`
- 目标 HGP blob：`d18e00e59d71aa1615417dbfadf4f60d4b27bd69`

未来若另获 formal integration 授权，装配顺序为：

1. 在正式文件顶部加入本 preview 规划的最小 frontmatter。
2. 用 `DRAFTS/U01.md` revision 4 全文逐字替换当前第 1 行旧 opening。
3. 紧接 U01 放入 `DRAFTS/U02.md` revision 4 全文，不添加中间说明。
4. U02 末句之后直接接当前第 3 行 `### 从两张经典校验矩阵开始`。
5. 删除当前第 39–70 行的竞争／重复背景；其余正文保持原顺序。

U01 无标题。U02 的两个标题为：

- `### 从局部交换到矩阵条件`
- `### 三个空间与两支映射`

当前正式文件的 11 个正文标题全部是 `###`。模拟拼接后 13 个标题全部同级、文字唯一；没有错误 nesting，也不需要 reset heading、包装标题或再次调整层级。

# Replacement / deletion range

| 当前正式范围 | 动作 | 理由 |
|---|---|---|
| 文件首部 | 插入最小 frontmatter | 目标笔记被实质修改时须满足 `NOTE_TYPES.md` |
| 第 1 行 | 以 U01 全文替换 | 旧 opening 与 guided opening 竞争，并预载前置链接／Künneth 边界 |
| 第 2 行 | 保留 | 空行分隔 |
| 第 3–38 行 | 逐字保留 | 承担 \(A,B\) 尺寸、二项复形和指标约定 |
| 第 39–51 行 | 删除 | 与 U02 的三空间、两映射及 chain 零复合视角直接重复 |
| 第 53–70 行 | 删除 | logical quotient 与 chain/cochain 对偶完整解释已有 owner；不承担后续核心构造 |
| 第 71–447 行 | 逐字保留 | product sectors、blocks、构造证明、S007、Tanner、参数、qLDPC、LP 与来源 |

唯一具有 reader-visible 内容的旧正文删除是当前第 1 行和第 39–70 行。不得移动、压缩、改写或顺手格式化其它正式正文。

当前第 102–165 行的构造性证明必须完整保留。它给出 \(\partial_1,\partial_2\) blocks、两条 product paths、特征 2 抵消、\(H_X=\partial_1\)、\(H_Z=\partial_2^T\) 与 \(H_XH_Z^T=0\)。U02 建立判据及需求，这一正式段落兑现具体 HGP 构造，不是竞争证明。

# Assembled reading flow

1. U01 区分超图乘积构造／HGP 码与 \(A,B\) 输入／\(H_X,H_Z\) 输出。
2. U01 建立共享物理列、行支撑与 CSS 对易问题。
3. U02 从 \(XZ=-ZX\)、异位置对易和共同位置数推出偶数重叠及 \(H_XH_Z^T=0\)。
4. U02 解释三个空间、两支映射和零复合，并以“由 \(A,B\) 构造并证明复合恒为零”交接。
5. 下一标题立即是 `### 从两张经典校验矩阵开始`，中间不插链接、提示框或维护说明。
6. 当前第 72–100 行建立乘积空间与物理扇区。
7. 当前第 102–165 行写出 blocks 并证明构造满足 U02 判据。
8. 后续 S007、Tanner、行列方向、参数、qLDPC、平方根基准、LP 与来源保持原顺序。

# Local bridge and links

| detail | HGP local bridge | full owner |
|---|---|---|
| 奇偶校验矩阵、输入／输出、行支撑与 CSS 当前要求 | U01 | `CSS码中的cochain complex.md` 承担完整 stabilizer/logical/syndrome |
| 同比特／异比特规则、重叠奇偶、矩阵条件 | U02-P1 | CSS owner 承担更完整结构；本地解释继续承重 |
| 三空间、两映射、零复合与链复形当前名称 | U02-P2 | `Chain complex 与 cochain complex.md` 承担 degree/cycle/boundary/homology/cochain |
| 完整 \(2\times2\) 核验 | U02 optional block | 无独立 canonical owner；非出口能力 |
| HGP blocks 与两路径抵消 | 后续正式第 102–165 行 | 当前 HGP 主笔记 |

新增链接计划为 **0**：U01/U02 已自足，index/canonical 已登记 owners；尤其不得在 U02 末句与 `### 从两张经典校验矩阵开始` 之间插入链接。现有后文链接全部保留。

# Duplication and ownership check

- 旧第 1 行与 U01 竞争首次入口，删除。
- 旧第 39–51 行与 U02-P2 和后续 blocks 中的正式 convention 连续重复，删除。
- 旧第 53–70 行展开 generic logical quotient 与对偶方向，不是 U01/U02 出口或后续核心构造的本地前提，删除并由既有 owners 承担。
- U02 的 Pauli、重叠与零复合说明是首次依赖前的必要 local bridge，不得替换为承重链接。
- U02 不展开 HGP blocks、尺寸、Künneth 或 homology，不与后文竞争。
- 当前第 102–165 行保留为“判据之后的构造性验证”。

当前第 309 行后的依赖仍闭合：

- \(N\) 与 rank 公式只依赖物理扇区和 \(H_X,H_Z\)，不依赖被删除的 \(H_1/H^1\) orientation 段。
- 可选 product logical sectors 已在首次使用处链接 Künneth，并局部定义 \(k_A,k_A^T,k_B,k_B^T\)。
- qLDPC、平方根基准和 LP 过渡依赖后文各自的局部条件，不依赖旧第 53–70 行。

# Frontmatter

未来正式整合只添加：

```yaml
---
note_type: reference
entry_mode: guided
status: stable
---
```

`reference` 保持 HGP canonical owner 职责；`guided` 对应新 opening；现有 ownership 与成熟度不变，因此规划 `stable`。不添加 aliases、tags、标题或额外状态字段。

# Index / canonical impact

- `Notes/00-index.md`：无需修改。文件路径、学习顺序、主题边界和下游关系不变。
- `CANONICAL_KNOWLEDGE.md`：无需修改。HGP owner、chain convention、blocks、\(N/K\)、qLDPC 与 owner 关系均未迁移或新增。
- 不新增前置笔记，不拆分、合并、改名或移动正式笔记。

# Anchors

新增 anchors：

- `#从局部交换到矩阵条件`
- `#三个空间与两支映射`

被删除范围无标题，现有 11 个 heading anchors 保持不变。U01 不新增 heading anchor。

# Repository checks

核验工作树：`D:/MyKnowledgeBase/Magic State Vault/.tmp/notes-v5-install`，分支 `codex/notes-v5-install`。

- `git diff --name-only`：空。
- `git diff --cached --name-only`：空。
- `git status --short`：只有本 task 目录未跟踪；没有 tracked 或 staged 修改。
- 正式目标、两份 owner note、index 与 canonical 均与 HEAD blob 一致。

受保护 blobs：

| file | blob |
|---|---|
| `Hypergraph product code.md` | `d18e00e59d71aa1615417dbfadf4f60d4b27bd69` |
| `CSS码中的cochain complex.md` | `dbdbf098bf73fedcb8a497c9a38eaaba6952cec5` |
| `Chain complex 与 cochain complex.md` | `9439db87d5a5b01c19ff6fa7e763ae8e4966208c` |
| `Notes/00-index.md` | `847c0b231fd7471f49a445cb7f0d0426a53285cb` |
| `CANONICAL_KNOWLEDGE.md` | `12b3fdb92c5214f4c6e48b54d3a6777cd76ead67` |

审稿正文 SHA-256：

| draft | SHA-256 |
|---|---|
| `DRAFTS/U01.md` | `3713ad6565c3f992f402b4372db00efa37b798e56f6ac2d0fde9a04b5a46c585` |
| `DRAFTS/U02.md` | `4e8ebdece7f95c48009c45c684e11d1a88e2df66d56d59bc63cdc022ddbacd5f` |

任一保护基线或 draft 指纹变化时，本 preview 失效，必须停止并重新生成。

# Required return route

当前无需返回 Design、Writer 或双审查。Placement、删除范围、assembled flow、heading/anchors、duplication、links、frontmatter、index/canonical 与保护基线均明确，且整合可逐字保留 draft revision 4，因此状态为 `ready`。

本 preview **不授权 formal integration**。若未来 Integrator 发现必须改 U01/U02 任一 reader-visible 字句、标题、公式、段落、callout，或必须新增链接／扩大删除范围，应停止并返回 Design / Writer，重新双审查与 preview。
