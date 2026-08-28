# Notes/WORKFLOWS/cold-read-audit.md

Blind Reader 进行真正独立的冷启动审查。它不核对 packet，只判断正文是否实际像教材。

本文件承接 `depth-and-mainline.md` 的 cold-read gate；为保持 blind context，不向 Blind Reader 提供具体设计预算或该设计文件的内容。

## 1. 允许读取

只读取 Reader Cards、Drafts 与 LANGUAGE_PROFILE。不得读取 packet、design、domain、source、canonical/index、Contract Audit 或旧 verdict。

## 2. Reader trace

逐段记录：读完知道什么、预先接受什么、产生什么问题、下一段是否推进、同时记住什么。

## 3. 审查项

### 首句与定义

稳定对象、非词典式、定义非循环、在首次依赖前闭合，且没有为了即时解释形成过载句法。

### 隐含 claims

逐问“我凭前文为什么接受这句话？”发现 hidden premise。

### 问题流与主线

- 当前主问题能否持续辨认；
- 支持性细节结束后是否回到主问题；
- 工具是否在需求后出现；
- 是否像 checklist 句子化。

### Mainline latency

记录从问题到阶段主结论之间的支持性段落数、新记号组和明显绕行。若读者在返回前已忘记当前问题，标记 major。

### Explanation proportionality

- 辅助概念篇幅是否压过主要对象；
- 当前详细程度是否与出口能力相称；
- 是否存在安全但不必要的过度闭合。

### Optional skip test

跳过标记为 optional 的块后：

- 主线是否仍连续；
- 后文是否偷偷依赖其中未在主线出现的结论；
- 回返句是否存在。

### 认知负荷、中文语体与出口能力

检查新增对象／符号、consolidation、回读需求、术语自然度，以及 reader card 出口是否真实达到。

## 4. 输出与路由

生成 `COLD_READ_AUDIT.md`，包含 reader trace、latency/proportionality 记录、findings 和 verdict。

Hidden premise、深度、比例、问题流返回 Design；局部中文返回 Writer；Reader Card 冲突返回 Learner/Design；blocker 交用户。
