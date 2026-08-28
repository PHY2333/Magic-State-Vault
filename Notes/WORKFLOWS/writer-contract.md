# Notes/WORKFLOWS/writer-contract.md

本文件规定 Packet Builder、Reader Card Builder 与 Writer 接口。

`depth-and-mainline.md` 的设计决定必须由 Packet Builder 编译进当前 packet；Writer 不得为取得这些决定而读取 design 或其它污染上下文。

## 1. Packet Builder 输入与输出

只在 Design Audit pass 后读取通过的 design、learner snapshot、source packet、language profile 和目标片段。输出 `PACKETS/Uxx.md` 与 `READER_CARDS/Uxx.md`。

## 2. Writer Packet 必须包含

- note type、entry mode、目标位置；
- reader entry 与 exit capability；
- phase sequence；
- concept actions；
- definition/claim instructions 与 closure deadlines；
- depth and placement ledger；
- mainline contract 与 latency budget；
- notation/load；
- required math/examples；
- source excerpts；
- language、opening、transition、link contract；
- forbidden topics。

## 3. Reader Card

只含 reading situation、assumed entry、explicitly not assumed、expected exit、language register。不得含 phase、claim、depth 选择、标准答案、来源或 audit 状态。

## 4. Packet 清洗与 preflight

删除 ownership、前置清单、维护边界和流程状态。检查：

- capabilities/actions 完整；
- definitions/claims 可执行；
- closure deadline 自然；
- depth/placement 与 mainline budget 一致；
- optional detail 明确可跳过；
- source 足够；
- language contract 完整；
- packet 单独可写；
- reader card 不泄露答案。

## 5. Writer 强隔离与 staged draft

Writer 在干净上下文中只读当前 packet、授权来源和目标片段，写入 `DRAFTS/Uxx.md`，不直接修改正式文件。

## 6. Writer 规则

- 保持 claim 依赖顺序，但可自然重组句子；
- definition 只需在 closure deadline 前完成，不机械挤在同句；
- 不擅自加深 explanation depth；
- optional block 与主线明确区分，并在结束后回到主问题；
- `upstream_bridge` 必须先写自足 local bridge，再允许链接；
- 遵守 latency budget 与 return-to-mainline；
- 不把 checklist 逐项改写成正文；
- packet 不足时请求补充，不自行重新设计。

## 7. 交付

报告 staged draft 路径、exit capability、depth/packet 变更请求和未处理单元。
