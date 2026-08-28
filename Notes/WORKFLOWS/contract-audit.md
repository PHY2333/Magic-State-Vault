# Notes/WORKFLOWS/contract-audit.md

Contract Auditor 是 packet-aware 正文审查。它不改文件。

## 1. 允许读取

- 当前 `PACKETS/Uxx.md`；
- packet 授权来源；
- `DRAFTS/Uxx.md`；
- `Notes/LANGUAGE_PROFILE.md`。

不得读取 Blind Reader 的首次结论后再形成初始 verdict。

## 2. 检查项

### 2.1 数学与来源

检查定义、公式、尺寸、指标、条件、约定和来源边界。Writer 不得用模型常识补齐 packet 缺口。

### 2.2 Packet compliance

- phase 顺序；
- concept actions；
- delay/omit 边界；
- notation/load budget；
- link 和 language contract。

### 2.3 Definition cards

正文中的局部定义是否完成：

- category；
- current function；
- 非循环；
- 可区分；
- 可操作；
- 不使用未授权专名。

### 2.4 Claim ledger

逐 claim 建立：

```text
packet claim
→ draft 位置
→ capability premises
→ prior claims
→ closure method
→ source/calculation
```

不得只因 claim 出现在 packet 中就判通过；正文必须实际闭合。

### 2.5 Exit capability

正文是否真正支持 unit 出口能力，而不只是提到相关词。

### 2.6 Language contract

检查术语、英文缩写、标题和中文连续性；避免设计文件中的中英混合速记直接进入正文。

## 3. 输出

生成 `CONTRACT_AUDIT.md`：

```yaml
status: pass | changes_required | blocked
reviewed_draft_revision: <n>
```

发现写明 severity、位置、问题、影响、return_to 和 suggested_fix。

## 4. 路由

- 数学、来源、premise 缺失：Mapper 或 Design；
- definition card / claim order / phase：Design；
- 局部表达、术语渲染、公式执行：Writer；
- blocker：用户。
