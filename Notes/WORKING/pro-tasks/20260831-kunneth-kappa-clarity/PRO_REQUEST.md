---
task_id: 20260831-kunneth-kappa-clarity
request_id: R01
request_type: local-rewrite
route: pro-write
output_mode: full-file
review_policy: internal
binding_id: 999011c9b4e64a87a96f35b147bde364
target_files:
  - Notes/07-Lifted-Product Code/Künneth 分解.md
---

# 用户目标

局部重写比较映射 $\kappa_n$ 的单射与满射解释。完成后，读者应能够：

1. 从任意源元素 $\alpha$ 出发，准确说明 $\kappa_n$ 单射要求什么；
2. 从任意目标同调类 $[z]$ 出发，准确说明 $\kappa_n$ 满射要求什么；
3. 区分“链本来就是纯张量之和”与“一个同调类同调于由两个因子的 cycles 构成的纯张量之和”；
4. 在域上证明末尾逐元素看见满射和单射分别怎样由链复形直和分解推出；
5. 说明证明得到的是先前定义的具体比较映射 $\kappa_n$ 可逆，而不只是两个空间抽象同构或维数相同。

# 当前真实读者反馈

用户指出下面两句“有点跳跃和模糊”：

- $\kappa_n$ 是否单射：若若干因子同调类的张量和在乘积复形中变成 boundary，它在源空间中是否已经为零？
- $\kappa_n$ 是否满射：乘积复形的每个 degree-$n$ 同调类，是否都能写成若干 $[c\otimes d]$ 之和？

当前文字有三处需要真正解决，而不是换同义词：

1. “它”没有被命名；读者看不清源空间中的一般元素、它的像，以及“像为零”为什么等价于某个代表链是 boundary。
2. 满射表述容易像代数恒真式，因为 tensor product 中的链本来就可写成纯张量之和；真正要说的是每个目标 cycle 在模去 boundaries 后，是否可由两个因子各自的 cycles 的张量有限和代表。
3. 后文证明只说“消去含 $Q$ 的部分”和“位于零边界的直和分量”，没有明确说明只能消去其中的 cycles，也没有证明环境中的 boundaries 不能进入同调代表元分量。

不要把这份诊断作为维护说明贴进正文；请重写相关正文，让数学对象和推理自然出现。

# Reader assumptions

## 可以直接依赖

- 基本线性代数、线性映射的 kernel、image、单射与满射；
- 链复形中的 cycle、boundary 与 $H_n=Z_n/B_n$；
- tensor product 中一般元素是纯张量的有限和；
- 本文在当前段落前已经定义的 $\kappa_{p,q}$ 与 $\kappa_n$。

## 不能直接依赖

- 读者已经能自动把抽象的单射、满射翻译成同调商空间中的逐元素条件；
- 读者会自行区分“链的纯张量展开”与“由因子 cycles 的张量给出同调类代表”；
- 读者能从未命名的同构自动判断它恰好是 $\kappa_n$；
- 读者会自行补出直和子复形中 cycle、boundary 与 ambient boundary 的关系。

仓库中存在相关笔记不代表读者已经掌握。正文应在承重位置给出最短充分桥梁。

# 必须读取

- Notes/WRITING_GUIDE.md
- Notes/OBSIDIAN_MATH.md
- Notes/PRO_OUTPUT_PROTOCOL.md
- Notes/07-Lifted-Product Code/Künneth 分解.md
- CANONICAL_KNOWLEDGE.md：只核对 Künneth、HGP 与 LP 的主笔记归属和数学边界
- Notes/WORKING/pro-tasks/20260831-kunneth-pro-rerun/PRO_REQUEST.md：沿用已核验的 canonical、May / Stacks 与 S003 边界，不重开整篇重写目标

# 来源与数学边界

- 固定比较映射方向与公式：

  $$
  \kappa_n:
  \bigoplus_{p+q=n}H_p(C)\otimes_kH_q(D)
  \longrightarrow H_n(C\otimes_kD),
  \qquad
  [c]\otimes[d]\longmapsto[c\otimes d].
  $$

- 在定义后的解释中，应明确允许源的一般元素是有限和，例如

  $$
  \alpha=\sum_i[c_i]\otimes[d_i],
  \qquad
  \kappa_n(\alpha)=\left[\sum_i c_i\otimes d_i\right],
  $$

  其中每个 $c_i,d_i$ 是相应 degree 的 cycle，且各项 total degree 为 $n$。表达式可以按不同 $(p,q)$ 分量分组，不得暗示 tensor 表达唯一，也不得声称每一项分别为零。

- 单射要求：若 $\kappa_n(\alpha)=0$，也就是某组代表下的 $\sum_i c_i\otimes d_i$ 是乘积复形中的 boundary，则 $\alpha=0$ 于源的直和中。
- 满射要求：对每个 cycle $z\in(C\otimes_kD)_n$，存在因子 cycles $c_i,d_i$ 及某个 $w\in(C\otimes_kD)_{n+1}$ 使

  $$
  z-\sum_i c_i\otimes d_i=\partial w.
  $$

  等价地，$[z]$ 位于 $\kappa_n$ 的像中。不要把满射误写成“每个链都是纯张量和”。
- 域上证明应保持现有假设、Koszul 符号和非典范补空间机制。可显式命名

  $$
  S=\widetilde{\mathcal H}(C)\otimes_k\widetilde{\mathcal H}(D)
  $$

  以及由另外三个含可缩因子分量组成的子复形 $A$，使用

  $$
  C\otimes_kD=S\oplus A.
  $$

  必须只声称 $A$ 中的 cycles 是 boundaries，不能声称 $A$ 的任意链都是 boundary。
- 可定义 $j_n:S_n\to H_n(C\otimes_kD)$, $s\mapsto[s]$，逐元素证明：
  - 对 cycle $z=s+a$，由直和与 $\partial z=0$ 得 $\partial a=0$，再由 $H(A)=0$ 得 $a=\partial w$，所以 $[z]=[s]$；
  - 若 $[s]=0$，则 $s=\partial w$。把 $w$ 按 $S\oplus A$ 分解并用 $\partial|_S=0$，得到 $s\in S\cap A=\{0\}$，所以 $s=0$。
- 应明确把 $\kappa_n$ 分解为上述具体 $j_n$ 与代表元识别的复合，并对纯张量核对后用线性推广到有限和；不得只写未命名的抽象同构。
- 保持自然的 $\kappa_n$ 与证明中非自然的补空间、链级投影和收缩同伦之间的区别。不得把 $S$ 说成 canonical chain-level summand。
- 保持当前域、有界有限维、降次数 chain convention，以及后文所有已核验数学结论。
- 继续采用 canonical + May / Stacks 的边界。S003 补充材料式 (91) 不作为一般定理；不得借本次局部改写改变 PID、一般交换环、HGP、LP 或 $R_2$ 反例的内容。
- 不新增来源未支持的定理、参数或一般化。若来源或数学条件发生冲突，返回 NEEDS_CONTEXT，不要补猜。

# 写作权限

## 允许

- 完整替换唯一目标文件；
- 重写比较映射定义后、自然性小节之前的单射/满射说明；
- 重写域上分解证明末尾与单射、满射、$\kappa_n$ 身份核对直接相关的段落；
- 为消除重复或保证连续性，最小调整这两处相邻过渡；
- 保留当前基线中“这个候选规则”的用户修改。

## 禁止

- 修改 allowlist 外的任何文件；
- 删除、移动、拆分、合并或重命名正式文件；
- 改变 Künneth 定理、Koszul differential、自然性、HGP 公式、PID 短正合列、一般环谱序列、LP 安全接口或 $R_2$ 反例；
- 把局部反馈扩成整篇风格重写，或顺手改写无关段落；
- 用维数相等代替对具体映射的单射、满射证明；
- 把每个同调类说成由一个纯张量代表；
- 把任务、审查、allowlist、canonical ownership 或工作流语言写入正文。

必须保留 H1 “Künneth 分解”，并保留标题文字精确为“PID 与一般系数环”的二级 heading。若只能通过结构性文件操作解决问题，返回 DECISION_REQUIRED。

# 写作要求

- 内部完成教学规划，直接输出完整、可替换的目标 Markdown；不输出设计稿、修改建议、审查表或 patch；
- 在首次提问单射与满射时，先命名一般源元素及其像，再分别说明 kernel 条件与代表目标同调类的条件；
- 公式后用自然中文解释每个零、等式和 boundary 条件位于哪个空间；
- 让前面的两个问题成为后文域上证明真正回答的问题：从任意目标 cycle 出发证明满射，从像为 boundary 的任意源元素出发证明单射；
- 避免“它”“消去”“零边界分量”等没有明确指代或缺失中间关系的压缩表达；
- 只展开完成这条主线所需的最短充分内容，避免把局部澄清变成长篇抽象代数旁支；
- 保持现有自然中文教材语体、有效链接和全篇已有正确内容；
- 严格使用 Obsidian 数学格式，并严格遵守 Notes/PRO_OUTPUT_PROTOCOL.md；
- 输出前从头连续复读完整文件。

# 完成标准

1. 读者能写出任意源元素 $\alpha$、它的像，以及“$\kappa_n(\alpha)=0$”的 boundary 含义。
2. 读者能从任意目标 cycle $z$ 写出满射所要求的同调等式，并知道这不是纯张量展开的恒真式。
3. 文字明确指出单射不要求张量和中的每一项分别为零，也不依赖一种唯一的 tensor 表达。
4. 域上证明显式说明含可缩因子子复形中只有 cycles 必为 boundaries，并证明环境 boundaries 不会进入同调代表元分量。
5. 证明把具体 $\kappa_n$ 写成已证明双射的映射与代表元识别的复合，方向正确，不能只给抽象同构。
6. 自然的比较同构与非自然链级分裂仍被准确区分。
7. 除上述局部及最小过渡外，全文数学内容、标题、顺序和范围保持不变；当前“这个候选规则”保留。
8. canonical + May / Stacks 边界保持；S003 式 (91) 不作为一般定理。
9. 中文、链接和 Obsidian 数学格式通过检查，无待核对、TODO 或待补推导。
