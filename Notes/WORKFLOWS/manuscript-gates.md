# Notes/WORKFLOWS/manuscript-gates.md

本文件合并 v6.1 的最终 gate。

## 1. Required gates

Hybrid task 必须同时满足：

1. `SOL_CONTRACT_AUDIT.md: pass`
2. `PRO_FINAL_REVIEW.md: pass`
3. 两者审查同一 `ASSEMBLED_DRAFT.md` SHA-256
4. `MATH_RENDER_AUDIT.md: pass`

Sol cold read 仅为 preflight。

## 2. MANUSCRIPT_VERDICT.md

Gatekeeper 只合并状态和 fingerprints：

```yaml
status: pass | changes_required | blocked
sol_contract_status:
pro_final_review_status:
math_render_status:
assembled_draft_sha256:
whole_note_scope: true
formal_integration_authorized_by_task: true | false
```

Gatekeeper 不新增教学判断，也不把 partial review 扩展为 whole-note pass。

## 3. 失效条件

以下任一发生，旧 verdict 失效：

- assembled reader-visible text 改变；
- unit 顺序、标题、optional placement 或链接承重关系改变；
- 数学 delimiter 被改动；
- target note / relevant source hash 改变；
- Pro final review 不是 fresh session；
- Sol/Pro 审查 hashes 不同。

## 4. 自动下一步

Manuscript pass 后 Sol 自动：

1. 保存和验证 Pro review；
2. 生成 `MANUSCRIPT_VERDICT.md`；
3. 生成 read-only `INTEGRATION_PREVIEW.md`；
4. 若 Preview ready 且 task 预授权自动 integration，则先 commit/push review 与 preview checkpoint；
5. 重新锁定 remote snapshot 后再继续正式写入；
6. 否则 commit/push 后停在相应 gate。
