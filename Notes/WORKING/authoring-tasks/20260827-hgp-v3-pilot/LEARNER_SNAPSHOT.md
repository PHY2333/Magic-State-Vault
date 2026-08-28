---
learner_revision: 1
---

# 当前目标

- 第一次接触 HGP 时，能够识别构造类别、两张经典输入和两类量子 check outputs。
- 能把 CSS 自动对易问题压缩为 \(H_XH_Z^T=0\)。
- 能用三项箭头说明连续两步为零如何从结构上承接该条件。
- 当前不要求计算 HGP blocks、逻辑空间、距离或任何下游构造。

# 概念与能力

| concept_or_capability | evidence_state | scope | evidence | confidence | risk_flags |
|---|---|---|---|---|---|
| 识别 HGP 是什么类别的构造 | `unseen` | HGP 第一次入口 | 用户明确要求“第一次接触”并强制该项为 unseen | high | notation-overload |
| 识别 HGP 的输入是两张经典二进制校验矩阵 | `unseen` | 只要求识别输入层级，不要求尺寸或运算 | 用户明确强制该项为 unseen | high | notation-overload |
| 区分输入 \(A,B\) 与输出 \(H_X,H_Z\) | `unseen` | 构造接口与两类 checks | 用户明确强制输入与输出为 unseen | high | transfer-gap |
| 见过“CSS”名称 | `named` | 名称层级 | 用户在任务中使用 CSS 名称 | high |  |
| 能用普通语言说明 CSS 的两类 checks | `unverified` | 同一批物理量子比特上的 X-type/Z-type checks | 没有直接能力证据；仓库存在正式笔记不算证据 | high | hidden-prerequisite |
| 能判断 CSS checks 是否对易 | `unverified` | 行对 overlap 与 \(H_XH_Z^T=0\) | 用户明确要求无直接证据时为 unverified | high | transfer-gap |
| 见过 \(X\)-type、\(Z\)-type check 名称 | `named` | 名称层级 | 用户在约束中使用两类 check 名称 | high |  |
| 能把 check matrix 的每行读成一条 check support | `unverified` | 经典／CSS 行角色 | 没有直接能力证据 | high | hidden-prerequisite |
| 能把两矩阵的共享列读成同一物理量子比特空间 | `unverified` | \(H_X,H_Z\) 列角色 | 没有直接能力证据 | high | hidden-prerequisite |
| 能把矩阵乘积读成所有行对 overlap | `unverified` | \(H_XH_Z^T\) | 没有直接能力证据 | high | notation-overload |
| 见过“链复形／cochain”名称 | `named` | 名称层级 | 用户明确提到 chain/cochain 迁移 | medium |  |
| 能在 chain 与 cochain convention 间迁移 | `unverified` | \(H_Z^T\to H_X\) 与 \(H_X^T\to H_Z\) | 用户明确要求该能力无证据时为 unverified | high | transfer-gap |
| 能解释三项箭头中的空间角色 | `unverified` | \(C_2\to C_1\to C_0\) | 没有直接能力证据 | high | notation-overload |
| 能把连续两步为零读成矩阵复合为零 | `unverified` | \(H_XH_Z^T=0\) | 没有直接能力证据 | high | hidden-prerequisite |
| 见过 Künneth 名称 | `named` | 仅名称 | 用户明确强制为 named | high |  |
| 能说明 Künneth 的用途 | `unverified` | 逻辑空间分析 | 用户明确说用途不假设；U01/U02 omit | high |  |
| 见过 Kronecker 名称 | `named` | 仅名称 | 用户在任务边界中使用该名称 | high |  |
| 能执行或解释 Kronecker 操作 | `unverified` | HGP blocks | 用户明确要求无直接证据时为 unverified | high | notation-overload |
| 能解释 \(\mathbb F_2\) 中两次相同项抵消 | `unverified` | \(A\otimes B+A\otimes B=0\) | 用户明确要求无直接证据时为 unverified | high | transfer-gap |
| 能区分“名称见过”与“能操作” | `operational` | 本任务的 learner-state 记录方式 | 用户明确要求二者必须拆分，并具体指定多项状态 | high |  |

# 可以直接使用

- 可以把 HGP、CSS、Künneth、Kronecker、chain/cochain 当作用户已经见过或指定过的名称标签，但名称本身不授权任何数学操作。
- 可以依照用户明确规定，区分 `unseen`、`named` 与 `unverified`，无需再次询问。
- 可以使用 \(A,B,H_X,H_Z\) 作为经过当前正文即时定义后的标签。
- 除上述证据外，不授权直接调用任何非平凡数学能力。

# 不得直接假设

- 不得假设读者知道 CSS 是哪类 code，或知道 stabilizer、stabilizer group、logical quotient。
- 不得假设读者会把 check rows、共享物理 columns 和矩阵乘积连接起来。
- 不得假设读者能操作 chain/cochain、Kronecker products 或 \(\mathbb F_2\) 抵消。
- 不得因仓库中已有 HGP、CSS、chain 或 Künneth 正式笔记而提升 evidence state。
- 不得把未验证能力降格成 `unseen`；只有 HGP 类别、输入和输出具有明确首次接触证据。

# 近期真实问题

- 用户要求开头呈现教材视角，而不是维护者视角。
- 用户特别防止工具名称、前置判断和 wikilinks 在读者理解对象之前出现。
- 用户要求把 U02 的对易问题和三项整体图分成两个 phase，以避免符号与关系同时过载。
- 主要风险是 `hidden-prerequisite` 与 `notation-overload`，不是缺少更多背景链接。

# 可能改变路线的不确定项

- 无。即使相关能力为 `unverified`，用户已经指定采用 guided entry、局部普通语言解释和两阶段 U02；不需要追加用户问卷。
- 若未来要进入具体 HGP blocks，Kronecker 操作、输入矩阵行列角色和 \(\mathbb F_2\) 抵消会成为新的路线分歧点，但不影响本 pilot。
