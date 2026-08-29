# Notes/WORKFLOWS/sol-design-validation.md

Codex Sol 接收 `PRO_DESIGN.md` 后，验证来源、数学和仓库可执行性，输出 `SOL_DESIGN_VALIDATION.md`。

## 1. 接收

- 按 Pro 的 `NEXT_SOL_PROMPT` 保存附件；
- 不改写 Pro 内容；
- 核对 task、role、branch、commit、request path/hash；
- 运行 `check_obsidian_math.py PRO_DESIGN.md`；
- 登记文件 SHA-256。

## 2. 可以检查

- 路径、branch、commit 和 target blob；
- source anchors 是否存在并支持对应 claim；
- 公式、类型、维数、转置、约定和适用条件；
- owner、入站 links、文件职责和拟议移动影响；
- learner evidence 是否被错误读取；
- legacy section 是否都在 final unit map 中得到处理；
- author mode 是否可执行；
- Pro draft request 所需材料是否齐全。

## 3. 不可以做

Sol 不得重排 Pro 主线、改变教学模式/depth、把 `pro_full` 降为 Sol 起草，或以更易执行的 unit map 代替 Pro design。

## 4. 结果

```yaml
status: pass | pro_revision_required | user_decision_required | blocked
reviewed_pro_design_sha256:
reviewed_based_on_commit:
```

### pass

- 编译 `PRO_REQUESTS/DRAFT-BATCH-xx.md`；
- 更新 `TASK.md` 为 `awaiting_pro_drafts`；
- 运行检查；
- 自动 commit/push；
- 输出精确 Pro Draft Prompt。

### pro_revision_required

- 生成 `PRO_REVISION_REQUEST.md`；
- 更新状态；
- 自动 commit/push；
- 输出精确 Pro design revision prompt。

### user_decision_required

只在文件删除、移动、拆分、合并、改名、互斥长期路线或关键来源冲突时停给用户。
