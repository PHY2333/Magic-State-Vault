---
status: pass
reviewed_draft_revision: 5
task_id: 20260828-hgp-v5-pilot
reviewed_units:
  - U01
  - U02
---

# Contract Audit

## 审查边界与隔离

Auditor 在独立上下文中只读取 `PACKETS/U01.md`、`PACKETS/U02.md`、`SOURCE_PACKET.md`、`DRAFTS/U01.md`、`DRAFTS/U02.md` 与 `Notes/LANGUAGE_PROFILE.md`。未读取 Reader Cards、Didactic Design、Domain Model、Learner Snapshot、canonical/index、正式 HGP、Cold Read、旧审查或 verdict；未修改文件。

## Audit history

| draft revision | result | outcome |
|---|---|---|
| 1 | pass | packet compliance 通过；等待独立 cold read |
| 2 | pass | 局部措辞返修未引入合同偏差；等待独立 cold read |
| 3 | pass | design revision 4 packet 下的完整最终重审通过 |
| 4 | pass | design revision 5 packet 下的 heading-only 返修完整重审通过 |
| 5 | pass | 重新审查 U01/U02 全文；U02 新过渡句与 design revision 5 packet 一致 |

每次 draft 改动后均重新执行完整 Contract Audit；旧 pass 没有自动覆盖新文本。

## Findings

无 blocker、major、minor 或 advisory finding。未发现 `待核对`、`TODO：补引用` 或 `待补推导`。

## U01 compliance

| 检查项 | 结果 | 核验 |
|---|---|---|
| 首句与定义 | PASS | 首句建立构造方法；紧邻第二句说明每行规定模 2 奇偶校验；同段区分构造与 HGP 码 |
| 输入／输出 | PASS | \(A,B\) 明确接回两张经典输入矩阵；\(H_X,H_Z\) 明确为量子校验矩阵输出而非输入别名 |
| 支撑闭合 | PASS | 在首次依赖前说明一行中为 1 的列对应的位置构成支撑，再给出 X 型／Z 型行角色 |
| Claim ledger | PASS | U1-C01–U1-C08 依赖顺序闭合；只把对易保证留作末问 |
| Depth / placement | PASS | 恰为三个短段落；提醒和 CSS local bridge 均未扩展成上游长证明 |
| Notation / language / links | PASS | 两组新符号；自然中文；链接 0；无禁止主题或流程语言 |
| Exit | PASS | 方法、所得码、经典输入、量子输出及下一问题均可区分和复述 |

唯一末句为：

> 怎样由构造本身保证两类校验彼此对易？

## U02-P1 compliance

| 检查项 | 结果 | 核验 |
|---|---|---|
| 五段主线 | PASS | 支撑表示 → 同比特推导 → 异比特推导 → 总符号／偶数重叠 → 矩阵汇总／反例 |
| DEF05 | PASS | 支撑只记录非零位置；\(H_X/H_Z\) 归属决定 \(X/Z\) 类型；0 对应 \(I\) |
| 张量积记号 | PASS | \(\bigotimes_q\) 被解释为组合各量子比特上的局部作用 |
| Pauli premises | PASS | 计算基短推导得到 \(XZ=-ZX\)；当前 \(X/I/Z\) 张量因子特例闭合异比特对易 |
| 总符号 | PASS | 每个共同位置贡献负号，得到 \((-1)^w\) 与偶数重叠判据 |
| 矩阵元 | PASS | 展开 \((H_XH_Z^T)_{ij}\)，逐项说明其为对应两行的重叠奇偶 |
| 全部对易 | PASS | \(H_XH_Z^T=0\) 精确汇总每条 X 型校验与每条 Z 型校验对易 |
| 最小反例 | PASS | \([1]\) 只说明共享列不自动保证零乘积 |
| P1 boundary | PASS | 无 \(C_2,C_1,C_0\)、链复形、HGP blocks 或“已证明具体输出”的断言 |

Revision 5 的首句为：

> 要回答上一节的问题，第一步是把输出必须满足的对易要求化成一个可检验的矩阵条件。

该句正确承接 U01 末问，并把 U02 的当前任务限定为“第一步”：先求输出必须满足的矩阵条件。它没有提前声称具体 HGP 输出已满足该条件，也没有改变后续 claim 顺序、depth 或段落预算。

两处阶段标题严格使用 packet 规定的三级标题：`### 从局部交换到矩阵条件` 与 `### 三个空间与两支映射`。标题文字不变，正文未引入其它 ATX 标题。

## Optional block

- 完整 \(2\times2\) 计算只在可折叠 `补充推导` callout 中。
- 跳过后，计算基推导、异比特规则、总符号、偶数重叠和零矩阵条件仍独立闭合。
- callout 后第一句明确回到整条校验与“每个共同位置贡献一个负号”。
- 后文不依赖 callout 独有步骤。

结论：optional skip test `pass`。

## U02-P2 compliance

| 检查项 | 结果 | 核验 |
|---|---|---|
| 五段主线 | PASS | 三空间 → \(H_Z^T\) → \(H_X\) → 零复合 → 链复形命名／下一步 |
| 三空间 | PASS | \(C_2,C_1,C_0\) 分别以 Z 校验、物理量子比特、X 校验为坐标 |
| 第一映射 | PASS | 所选 Z 行按模 2 相加；所得二进制向量中为 1 的物理坐标构成支撑 |
| 第二映射 | PASS | 每个输出分量记录物理支撑与相应 X 型校验支撑的重叠奇偶 |
| 零复合 | PASS | 连续作用为 \(H_XH_Z^T\)，其为零统一表达全部跨类型校验对易 |
| DEF06 | PASS | 只有对象、映射、复合和用途闭合后才命名链复形 |
| Boundary / exit | PASS | 无尺寸、额外向量、同调或 blocks；末句只期待从 \(A,B\) 构造并证明零复合 |

## 数学与来源一致性

- 计算基与矩阵核验都正确给出 \(XZ=-ZX\)。
- 异比特张量因子等式正确，未引入未登记的一般规则。
- \(\sum_qx_qz_q\) 计数共同位置，矩阵元在 \(\mathbb F_2\) 上记录其奇偶。
- 采用的方向
  \[
  C_2\xrightarrow{H_Z^T}C_1\xrightarrow{H_X}C_0
  \]
  与零复合 \(H_XH_Z^T=0\) 一致。
- 所有承重内容均由 packet 的 M01–M08 与 Source Packet 的 LD00–LD07 授权；没有模型常识偷渡。

# 结论

Draft revision 5 通过完整 Contract Audit。U01 虽未修改，仍从头复核；U02 也按全文而非只按新句复核。无需返回 Mapper、Design、Packet Builder 或 Writer；等待同 revision 的独立 Blind Cold Read 合并 verdict。
