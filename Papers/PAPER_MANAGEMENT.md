# Papers/PAPER_MANAGEMENT.md

本文件是 `Papers/` 的唯一管理入口，负责 paper、book 等来源的稳定身份、文件版本、阅读状态、主辅关系和链接安全。全文翻译规则见 `Translations/TRANSLATION_GUIDE.md`；从文献建立或改写知识笔记时，执行 `Notes/WORKFLOWS/note-writing.md`。

本文件只保留稳定规则。动态来源登记保存到 `Papers/SOURCES.md`，主辅关系保存到 `Papers/RELATIONS.md`。所有文献管理任务仍先读取本文件，再进入对应登记文件。

---

## 1. 目录职责

- `Papers/` 保存可独立引用的原始来源文件及其管理入口。
- 译文保存到 `Translations/`，不与原始来源混放。
- 论文导读、概念解释和继续推导保存到 `Notes/`，不写入本文件。
- Supplementary material、勘误和同一作品的其他格式属于来源版本管理，不自动获得新的作品 ID。

`Papers/SOURCES.md` 中的“主文献笔记”和“全文翻译”两个字段，只登记 paper/book 层面的主笔记和全文译本。由某篇来源支撑的全部主题概念笔记通过正文引用和反向链接查找，不在登记文件中重复维护完整清单。

---

## 2. 稳定文献 ID

每个可独立引用的作品分配一个作品级 ID：

```text
SNNN
```

- `S` 表示 source；paper、book、thesis 等共用编号，类型由登记字段区分。
- ID 一经分配不得改变；删除或废弃的 ID 不得复用。
- 新 ID 取当前最大编号加一，不为填补空号而重新编号旧来源。
- 同一作品的预印本、正式发表版、supplementary material 或不同文件格式通常沿用同一 ID。
- 内容和页码体系可被独立引用的新版书籍或实质不同作品应分配新 ID。
- 现有 legacy 文件可以保留原名，由来源登记建立 ID 与实际路径的映射。

辅助关系不是来源的固有类型。一本 book 或一篇 paper 即使只用于辅助阅读另一篇文献，也必须拥有自己的稳定 ID。

---

## 3. 文件命名与版本

新入库文件优先使用：

```text
SNNN_<year-or-nd>_<first-author-or-editor>_<short-title>.<ext>
```

同一作品的其他版本或配套文件在相同 ID 后增加用途后缀，例如：

```text
S004_2025_Author_short-title_v2.pdf
S004_2025_Author_short-title_publisher.pdf
S004_2025_Author_short-title_supp.pdf
```

不得静默覆盖已经被笔记或译文引用的版本。新增版本时应登记版本、实际路径及其与旧版本的关系。

同一 ID 同时保留多个版本文件时，必须把版本与路径写成一一对应的嵌套列表，例如：

```md
- 文件与版本：
  - arXiv v2：[文件](S004_2025_Author_short-title_v2.pdf)
  - publisher：[文件](S004_2025_Author_short-title_publisher.pdf)
  - supplementary material：[文件](S004_2025_Author_short-title_supp.pdf)
```

只有一个版本时，可以继续使用来源记录模板中的“本地文件”和“版本或版次”两个字段。

已有文件不因格式不统一而自动改名。改名、移动或删除来源前，必须全文检索旧路径；文件操作、全部反向链接更新和旧路径零匹配检查应在同一次任务中完成。不要依赖编辑器自动更新链接。

---

## 4. 判重与入库流程

新增来源前按以下顺序判断：

1. 搜索 DOI、arXiv ID 或 ISBN。
2. 无稳定外部标识时，比对规范化题名、第一作者或编者、年份和版次。
3. 对疑似相同的本地文件比较 SHA-256。
4. 同一作品且文件内容相同：不新增文件和 ID。
5. 同一作品的新版本、正式发表版或其他格式：沿用原 ID，在原条目中增加版本和路径。
6. Supplementary material 通常沿用原 ID，并使用 `_supp` 后缀。
7. 独立作品或可独立引用的新版书籍：分配新 ID。
8. 在 `Papers/SOURCES.md` 完成来源登记后，再建立翻译、主文献笔记或 `Papers/RELATIONS.md` 中的辅助关系。

---

## 5. 来源记录格式

新增来源使用以下字段：

```md
### SNNN

- 类型：paper / book / thesis / report
- 题名：
- 作者或编者：
- 年份：
- 外部标识：DOI / arXiv / ISBN
- 本地文件：
- 版本或版次：
- 阅读状态：待核对 / 待读 / 在读 / 已选读 / 已通读 / 归档
- 主文献笔记：无 / 路径
- 全文翻译：未计划 / 不需要 / 计划 / 翻译中 / 待核对 / 已核对；路径
```

“已选读”表示已经核对任务所需章节，不表示通读全文。“已通读”只能用于已经覆盖全文的来源。

“全文翻译”字段只登记全文译本，不登记局部摘译。译本位于 `Translations/` 时，从 `Papers/SOURCES.md` 链接应使用 `../Translations/<文献ID>.full.zh-CN.md`；若存在多个版本，明确链接当前译本，并在译文文件名中包含版本标识。

---

## 6. 来源登记入口

- 来源登记：[Papers/SOURCES.md](SOURCES.md)

新增来源、登记新版本、改变阅读状态、关联主文献笔记或更新全文翻译状态时，只修改 `Papers/SOURCES.md`，不得在本文件保留来源记录副本。

---

## 7. 主文献与辅助文献关系

主辅关系描述本知识库中的阅读安排，不表示出版物之间存在从属关系。关系采用多对多登记，不写入文献 ID、文件名或目录层级。

- 主辅关系：[Papers/RELATIONS.md](RELATIONS.md)

新增关系时必须写明辅助范围。只写“相关”“背景”或“补充材料”不足以说明该来源用于主文献的哪一步。关系记录只写入 `Papers/RELATIONS.md`，不得在本文件保留副本。

---

## 8. 登记文件与维护边界

当前结构为：

```text
Papers/
├── PAPER_MANAGEMENT.md
├── SOURCES.md
└── RELATIONS.md
```

- `PAPER_MANAGEMENT.md` 只保留稳定规则和两个登记入口。
- `SOURCES.md` 只保存来源登记，不展开管理规则。
- `RELATIONS.md` 只保存主辅关系，不展开管理规则。
- 同一来源记录或关系不得同时出现在多个文件中。
- 规则变化只修改 `PAPER_MANAGEMENT.md`；来源状态变化只修改 `SOURCES.md`；关系变化只修改 `RELATIONS.md`。

`AGENTS.md` 和 `Translations/TRANSLATION_GUIDE.md` 始终只把本文件作为文献管理入口，不直接把动态登记文件设为任务入口。

---

## 9. 交付检查

涉及文献管理的任务交付时说明：

- 新增、替换、移动或删除了哪些来源文件；
- 分配或沿用了哪个稳定 ID；
- 登记了哪个版本或版次；
- 是否改变阅读状态、主文献笔记或全文翻译状态；
- 是否新增、修改或删除主辅关系，以及辅助范围；
- 是否检查并修复所有旧路径和反向链接；
- 是否把动态记录写入正确登记文件，并确认不存在重复副本。
