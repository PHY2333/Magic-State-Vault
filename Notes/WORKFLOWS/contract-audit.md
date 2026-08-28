# Notes/WORKFLOWS/contract-audit.md

Contract Auditor 是 packet-aware 正文审查，不改文件。

`depth-and-mainline.md` 的可执行决定由当前 packet 承载；本审查按该合同核对 depth、placement 与 mainline，不据此扩大允许输入。

## 1. 允许读取

当前 packet、packet 授权来源、draft、LANGUAGE_PROFILE。不得先看 Blind Reader verdict。

## 2. 检查项

### 数学与来源

定义、公式、尺寸、条件、约定和来源边界。

### Packet compliance

Phase、concept actions、delay/omit、notation/load、link/language。

### Definition 与 claim ledger

逐项核对正文位置、capability premises、prior claims、closure method/deadline、来源与实际闭合。不得因 packet 写了就判通过。

### Depth and placement

- Writer 是否按 depth 执行；
- 是否擅自把 reminder 写成 full derivation；
- optional block 是否可跳过；
- upstream bridge 是否本地自足；
- canonical detail 重复是否符合 design rationale。

### Mainline contract

- supporting paragraphs 与 notation 是否在预算内；
- 是否按约定回到主问题；
- 是否把辅助推导变成新的主线。

### Exit capability 与语言

正文是否真正支持出口能力，并符合中文语体。

## 3. 输出与路由

生成 `CONTRACT_AUDIT.md`。数学／来源返回 Mapper；definition/claim/depth/mainline 返回 Design；局部执行返回 Writer；blocker 交用户。
