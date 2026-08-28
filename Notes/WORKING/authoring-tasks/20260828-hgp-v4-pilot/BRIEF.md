# 学习目标

- 可观察表现 1：能说明超图乘积构造是一种从两张经典二进制奇偶校验矩阵构造 CSS 量子码的方法，并说明由该构造得到的码称为 HGP 码。
- 可观察表现 2：能把 `A、B` 指认为构造的两份经典输入，把 `H_X,H_Z` 指认为两类量子校验输出。
- 可观察表现 3：能说明任意矩阵 pair 不自动满足 CSS 对易条件。
- 可观察表现 4：能从同一量子比特上的 X、Z 反对易与不同量子比特上的作用对易，推出偶数重叠时一对异型校验对易。
- 可观察表现 5：能解释 `H_XH_Z^T` 的元素记录行重叠奇偶，并用三项箭头说明连续两步为零统一表达全部 CSS 对易条件。
- 可观察表现 6：能在自然、统一的中文教材语体中完成上述理解，不依赖 wikilink、前置清单或维护边界。

# 目标材料

- 目标文件：`Notes/07-Lifted-Product Code/Hypergraph product code.md`。
- 只设计与起草 U01、U02；正文写入本任务的 `DRAFTS/`。
- 目标文件长期职责维持 `reference`，入口模式采用 `guided`；本 pilot 不整合。

# 当前真实问题

- 现有开头把构造、所得码、自动对易、前置链接与 Künneth 边界压在同一段，第一对象不稳定。
- 历史 v3 staged draft 使用“既指……也指……”的词典式首句，并混用 `X-type checks`、`row pair`、`support space` 等中英速记。
- 历史 v3 审查主要验证 packet compliance，缺少独立 Blind Reader，也没有逐项追踪 Pauli 交换 premises。
- 本次要验证 v4 的 faceted capability、definition cards、claim ledger、中文 language contract 与双审查门能否闭合这些问题。

# 已有证据

- 用户明确指定 HGP 构造类别、构造与所得码关系、`A、B` 的当前角色为 `unseen`。
- 用户只展示了 CSS 与链复形名称，因此名称 facet 为 `named`，不授权其数学操作能力。
- 经典奇偶校验矩阵的一般含义、行列读取、Pauli 交换理由、矩阵重叠奇偶和零复合作用均无直接掌握证据，按相应 facet 标为 `unverified`。
- Künneth 只有名称证据；U01/U02 明确 `omit`。

# 非目标

- 不教授 stabilizer group、logical quotient、HGP blocks、矩阵尺寸、product complex 的具体生成、距离、qLDPC、LP 或 Künneth 用途。
- 不把 onboarding 拆成新正式文件。
- 不修改正式正文、索引、canonical 或长期 learner 状态。

# 可能需要用户决定

- 无。目标、范围、停止点、隔离要求和正文语言均已明确。
