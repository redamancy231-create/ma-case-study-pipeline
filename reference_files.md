# 关键文件索引

> 最后更新: 2026-07-23（GPT-5.6-Sol 审查修正闭合 + GitNexus 深度分析）

## 代码
- [generate_docx_v2.py](scripts/generate_docx_v2.py) — v2 论文 docx 生成脚本
- [generate_og_image.py](scripts/generate_og_image.py) — OG 图片生成脚本

## 数据
- [数据溯源方案模板.md](数据溯源方案模板.md) — 四级数据溯源分类规范
- [数据溯源方案模板.json](数据溯源方案模板.json) — 机读版

## 文档
- [README.md](README.md) — 项目主页（zh-CN，含 ToC + 文件标签 + 翻译范围说明）
- [en/README.md](en/README.md) — 英文 README
- [zh-Hant/README.md](zh-Hant/README.md) — 繁体中文 README
- [CLAUDE.md](CLAUDE.md) — AI 协作项目指南
- [CONTRIBUTING.md](CONTRIBUTING.md) — 贡献指南（含 CLOSED-FINAL 声明）
- [CHANGELOG.md](CHANGELOG.md) — 版本历史 [CLOSED-FINAL]
- [LICENSE](LICENSE) — CC BY 4.0（文档/数据/图表）
- [LICENSE-CODE](LICENSE-CODE) — MIT（Python 脚本、Shell hook）
- [CITATION.cff](CITATION.cff) — GitHub 原生引用元数据
- [项目复盘归档报告.md](项目复盘归档报告.md) — 完整项目复盘 v3.0
- [起点评估分析.md](起点评估分析.md) — 方法论反思
- [中国上市公司并购重组成功案例研究_v2.md](中国上市公司并购重组成功案例研究_v2.md) — 论文终稿
- [流水线复用包/多模型论文流水线_playbook.md](流水线复用包/多模型论文流水线_playbook.md) — 可复用方法手册
- [流水线复用包/阶段模板件.md](流水线复用包/阶段模板件.md) — 参数化 prompt+config 骨架
- [en/多模型论文流水线_playbook.md](en/多模型论文流水线_playbook.md) — 英文 playbook
- [zh-Hant/多模型论文流水线_playbook.md](zh-Hant/多模型论文流水线_playbook.md) — 繁体中文 playbook
- [docs/fork-modification-directions.md](docs/fork-modification-directions.md) — Fork 修改方向全景分析 v2.0
- [GitNexus分析报告_2026-07-23.md](GitNexus分析报告_2026-07-23.md) — GitNexus 图分析 + 异后端审查闭环
- [docs/social-preview.png](docs/social-preview.png) — 自定义 Social Preview 图片（1280×640）

## CI / 治理
- [.github/workflows/translation-drift.yml](.github/workflows/translation-drift.yml) — 翻译漂移双层门禁（时间提醒 + 结构一致性）
- [.github/workflows/repository-integrity.yml](.github/workflows/repository-integrity.yml) — 仓库完整性 CI（UTF-8/JSON/YAML/Python AST/链接/清单）
- [.githooks/pre-push](.githooks/pre-push) — 敏感信息检测（commit-range 扫描 + NUL 分隔 + 规则级白名单）
- [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) — PR 模板（CLOSED-FINAL 声明）

## Git 历史敏感信息确认
- 2026-07-21 已扫描全部 257 个唯一历史 blob（254 个文本、3 个二进制）；敏感关键词共命中 6 处，均为 `gh auth token` 或 `token + 插件启用` 等概念性描述，凭据形态匹配为 0。
- `project_status.md`：8 个历史 blob 中仅 2 个版本出现普通术语 `token`，未包含令牌值、密码、API 密钥或私钥。
- `_reviews/retrospect_2026-07-02.md`：1 个历史 blob，未命中敏感关键词或凭据形态。
