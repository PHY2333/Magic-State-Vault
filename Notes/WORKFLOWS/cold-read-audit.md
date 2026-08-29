# Notes/WORKFLOWS/cold-read-audit.md

v6.1 中 Sol Blind Cold Read 是可选 preflight，不替代 Pro Whole-Note Review。

## 1. 输入隔离

只读取 `PRO_REVIEW_CARD.md`、`ASSEMBLED_DRAFT.md`、`OBSIDIAN_MATH.md` 与语言规范；不读 packets、source、design、Sol contract verdict 或旧 review。

## 2. 检查

- hidden premises；
- 前一 unit 实际末问、当前 unit 首句、子问题和回返的连续性；
- mainline latency 与 explanation proportionality；
- optional / conditional skip；
- 中文术语与明显 checklist prose；
- section 间难度断崖；
- 删除或迁移后概念首次再次出现是否有落点；
- 公式在 Obsidian 中是否可读，不出现错误 delimiter。

## 3. 地位

- 发现问题时在交给 Pro Final Reviewer 前修复；
- `pass` 只表示 Sol preflight；
- 它不能生成 whole-note `reviewed`，也不能替代 `PRO_FINAL_REVIEW.md`。
