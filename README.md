# 多模型学术生产流水线 · M&A Case Study Pipeline

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Methodology Demo](https://img.shields.io/badge/Status-Methodology%20Demo-blue.svg)](#⚠️-重要免责声明)
[![Phase: 8-stage pipeline](https://img.shields.io/badge/Pipeline-8%20stages%20%2B%20open%2Fblind%20experiment-green.svg)](#流水线总览)

[![中文](https://img.shields.io/badge/lang-中文-red)]()
[![English](https://img.shields.io/badge/lang-English-blue)](./en/README.md)
[![正體中文](https://img.shields.io/badge/lang-正體中文-green)](./zh-Hant/README.md)

> **A battle-tested, multi-model collaborative academic pipeline — from research design through blind peer review, defense simulation, and open/closed-book controlled experiment.**
>
> 一条经过实战验证的多模型协同学术生产流水线——从选题设计、交叉盲审、答辩模拟到开卷/盲答对照实验。**这不是一篇可送审的论文，而是一套可移植的方法演示。**

> **📎 关于命名**：本仓库的短名是 `ma-case-study-pipeline`（M&A Case Study Pipeline），侧重**方法/流水线**；项目的完整中文标题是"中国上市公司并购重组成功案例研究"，侧重**内容/案例**。二者指向同一个项目——案例研究是流水线的"测试用例"，流水线才是核心交付物。仓库以方法命名，是因为这套流水线可以被移植到任何学术写作任务中，不限于并购重组。

> **📂 计划 Fork 本项目？** 先读 [`docs/fork-modification-directions.md`](docs/fork-modification-directions.md) —— 12 个修改方向的全景分析（v2.0，经 GPT-5.6-Sol 独立审查）。含**决策树**（3 个问题 30 秒定位你的起点）、**实现门槛排序表**（11 个可直接开工的方向）、和 **10 条反模式**（本项目实际踩过的坑）。

---

## ⚠️ 重要免责声明

**本项目定位为方法演示（methodology demonstration），而非可送审的学术论文。**

- 论文正文（`中国上市公司并购重组成功案例研究_v2.md`）存在**三处已知且未修复的缺陷**：商誉口径矛盾、杜邦分解不自洽、CAR t 值硬编码。这些缺陷已在文中标注，并在 `项目复盘归档报告.md` 中详细记录。
- 论文中的 CAR 数据、杜邦分解、商誉数字**不可作为实证结论引用**——数据为真实年报数据（R 类）与模拟估算值（S 类）的混合。
- 本项目的价值在于**方法**而非**论文**：八阶段流水线设计、prompt+config 双文件机制、交叉双盲审、开卷/盲答对照实验、数据溯源四级分类、以及可移植的复用 playbook。

**如果你在找一篇关于并购重组的论文来引用——请绕行。如果你在找一套让多个 AI 模型以结构化方式协作生产学术内容的方法——来对了。**

---

## 📑 目录

- [⚠️ 重要免责声明](#⚠️-重要免责声明)
- [流水线总览](#流水线总览)
- [目录结构](#目录结构)
- [快速入门](#快速入门)
- [关键数字](#关键数字)
- [方法论核心：五条铁律](#方法论核心五条铁律)
- [关联项目](#关联项目)
- [📂 Fork 修改指南](#📂-fork-修改指南)
- [许可证](#许可证)
- [引用](#引用)

---

## 流水线总览

```mermaid
graph LR
 P0[Phase 0<br/>选题+否决位] --> P1[Phase 1<br/>方案设计]
 P1 --> P2[Phase 2<br/>领域专家审核]
 P2 --> P3[Phase 3<br/>内容撰稿]
 P3 --> P4[Phase 4<br/>总装+质保]
 P4 --> P5A[Phase 5A<br/>交叉复审·合规]
 P4 --> P5B[Phase 5B<br/>交叉复审·规范]
 P5A --> P6[Phase 6<br/>整合裁决+修订]
 P5B --> P6
 P6 --> P7[Phase 7<br/>设计回溯]
 P7 --> P8[Phase 8<br/>答辩模拟]
 P8 --> P9[Phase 9<br/>定稿闭环]

 P8A[8A 主席出题] --> P8D[8D 学生作答]
 P8B[8B 会计出题] --> P8D
 P8C[8C 方法论出题] --> P8D
 P8D --> P8E[8E 零卷入评分]
```

**核心设计原则**：没有任何模型审查/评分自己做过的环节。角色是槽位，模型是填进槽位的人——每个新项目重新分配。

---

## 目录结构

```
├── README.md ← 本文件（简体中文原文）
├── en/README.md ← English translation
├── zh-Hant/README.md ← 正體中文翻譯
│
├── [元数据] LICENSE ← CC BY 4.0
├── [元数据] CLAUDE.md ← 项目 AI 协作指南
├── [元数据] CHANGELOG.md ← 版本历史
├── [元数据] CONTRIBUTING.md ← 贡献指南
├── [元数据] CITATION.cff ← 引用元数据
├── [元数据] reference_files.md ← 关键文件索引
│
├── [方法论] 流水线复用包/ ← ★ 最有价值的资产
│ ├── 多模型论文流水线_playbook.md │ 方法手册（五条铁律+Phase 0-9+量化剖面）
│ ├── 多模型论文流水线_playbook.json │ 机读版
│ └── 阶段模板件.md │ prompt+config 参数化骨架
│
├── [方法论] 数据溯源方案模板.md + .json ← 四级分类规范 [R][E][S][P]
│
├── [交付物] 项目复盘归档报告.md + .json ← 完整项目复盘（v3.0, CLOSED-FINAL）
├── [交付物] 起点评估分析.md + .json ← 方法论反思（四模型+红队+镜像参照）
│
├── [交付物] 中国上市公司并购重组成功案例研究_v2.md + .json ← 论文终稿（带缺陷标注）
│
├── phases/ ← 完整流水线快照（59 文件）
│ ├── phase1_kimi_k2.6/ │ 方案设计
│ ├── phase2_glm5.1/ │ 领域专家审核
│ ├── phase3_gpt5.5/ │ 内容撰稿
│ ├── phase4_claude_opus4.7/ │ 总装交付（注：仅含 prompt + config，交付物未保留）
│ ├── phase5a_gpt5.5/ │ 交叉复审（合规事实层）
│ ├── phase5b_glm5.1/ │ 交叉复审（学术规范层）
│ ├── phase6_claude_opus4.7/ │ 整合裁决+修订
│ ├── phase7_kimi_k2.6/ │ 设计回溯
│ └── phase8/ │ 答辩模拟（出题+作答+评分+盲答对照）
│
├── scripts/ ← 论文生成脚本
│ └── generate_docx_v2.py │ v2 生成（Phase 6 修订版；v1 脚本已废弃）
│
├── figures/ ← 论文图表
│ ├── figure1_roe_trend.png
│ └── figure2_car.png
│
└── docs/ ← 项目文档
  └── fork-modification-directions.md ← ★ Fork 修改方向全景分析（详见下方 §📂）
```

> **注**：`.docx` 二进制文件不包含在 Git 仓库中，可通过 [GitHub Releases](https://github.com/redamancy231-create/ma-case-study-pipeline/releases) 下载。
>
> **🌐 翻译范围**：核心方法论文件（README、playbook、阶段模板件）提供三语言版本（简体中文 / English / 正體中文）。论文正文和分析报告（案例研究 v2、项目复盘、起点评估、数据溯源方案）仅提供中文原文——论文是中文案例研究的产物，翻译论文本身意义有限。详见 [`en/`](en/) 和 [`zh-Hant/`](zh-Hant/) 目录。

---

## 快速入门

### 如果你只想了解方法

1. 读 `流水线复用包/多模型论文流水线_playbook.md` — 方法手册，约 25K 字
2. 读 `项目复盘归档报告.md` — 了解这套方法在一篇真实论文上的执行结果
3. 读 `起点评估分析.md` — 了解方法的局限和反思

### 如果你想复用这套方法

1. 复制 `流水线复用包/` 到你的项目
2. 按 playbook §5 确定你的论文类型，选择对应的承重阶段
3. 打开 `阶段模板件.md`，把 `{{占位符}}` 填成你的选题
4. 按 playbook §4 分配模型角色（角色=槽位，每个项目重配）
5. 严格执行铁律 2/3：不让任何模型审查自己做过的环节

### 如果你想查看论文产物

```bash
# 生成 v2 docx（需要 python-docx, matplotlib, numpy）
pip install python-docx matplotlib numpy
cd scripts
python generate_docx_v2.py
```

### 如果你想 Fork 并修改

→ **[`docs/fork-modification-directions.md`](docs/fork-modification-directions.md)** — Fork 修改方向全景分析（v2.0，经 GPT-5.6-Sol 独立审查）

这份 25K 字的文档覆盖了 fork 后**所有可能的修改方向**，按实现门槛和外部依赖分组：
- **可直接开工**（11 个方向）：换领域复用、教学/工作坊、审查方法论泛化、工程化 M1-M2 等
- **需要外部资料**（12 个方向）：修复论文缺陷、法学迁移、多语言扩展、GitHub Pages 等
- **纯元研究**（5 个方向）：开卷/盲答方法论文、对齐税量化、流水线脆弱性测试等

内含**决策树**（3 个问题 30 秒定位起点）、**前置知识假设表**、**反模式清单**（10 条，本项目实际踩过的坑）和**安全隐私治理**章节。

---

## 关键数字

| 指标 | 数值 | 说明 |
|------|------|------|
| 流水线阶段 | 8 + 2 新增（Phase 0 + Phase 9） | Phase 0-9，含开卷/盲答对照 |
| 使用模型 | 5 个独立模型 | Kimi/GLM/GPT/Claude/Qwen，零角色重叠 |
| 交叉双盲审 | 68（退回重写）→ 84（修改后通过） | Phase 5A/5B 独立盲审 |
| 答辩得分 | 开卷 78 / 盲答 75 | 开卷红利仅 -2.6，方法论维度零衰减 |
| 论文体量 | ~22.5K 汉字 / 16 篇文献 / 7 表 2 图 | 本科毕业论文标准 |
| 已知缺陷 | 3 处未修复 | 商誉/杜邦/CAR；已标注，决定不修 |

---

## 方法论核心：五条铁律

1. **每阶段配 `prompt.md` + `config.json` 双件** — 人机皆可读，防提示词漂移
2. **没有任何模型审查/评分自己做过的环节** — 撰稿人不审自己的稿，出题人不评自己的题
3. **出题人与评分人分离** — 评分官必须是"零卷入"模型（没参与过任何前序环节）
4. **审核早于撰写，总装最后做** — 领域硬伤在动笔前拦截
5. **诚信红线不可谈判** — 模拟数据绝不标成真实来源，每个数字登记来源等级

---

## 关联项目

- [**ai-collaboration-framework**](https://github.com/redamancy231-create/ai-collaboration-framework) — AI 协作项目全生命周期框架，本项目的流水线方法论被提取转化为框架内容
- [**independent-review-toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) — 独立审查工具包，从框架 §9.2 提取的独立审查 SOP
- [**prompt-tdd-methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) — Prompt-TDD 对照实验方法论案例手册
- [**etf-pattern-match-pybind11**](https://github.com/redamancy231-create/etf-pattern-match-pybind11) — pybind11/C++20 加速度量策略核心（DTW 37× / pattern match 61×）
- [**docx-pipeline**](https://github.com/redamancy231-create/docx-pipeline) — Markdown → 中文 DOCX 泛化管道，经 3 轮异后端审查闭合
- [**claude-skills**](https://github.com/redamancy231-create/claude-skills) — 3 个实战验证的 Claude Code Skill
- [**methodology-handbook**](https://github.com/redamancy231-create/methodology-handbook) — 50 条 AI 协作踩坑速查手册；本项目流水线是该手册方法论在完整学术场景中的实证

---

## 📂 Fork 修改指南

**[`docs/fork-modification-directions.md`](docs/fork-modification-directions.md)**（v2.0 · ~25K 字 · 经 GPT-5.6-Sol 独立审查）

这是一份 **fork 后的全景导航文档**——覆盖 12 个修改方向，从"换领域复用流水线"到"工程化为 CLI 工具"。每个方向标注了实现门槛、外部依赖和独立价值，方便你按自己的资源和目标选择起点。

| 如果你想要... | 从这里开始 |
|-------------|-----------|
| 用这套流水线写其他学科的论文 | → §1 换领域复用（法学/金融实证/计算机系统/公共政策） |
| 把 M&A 论文修成可送审的真论文 | → §2 把论文"做真"（商誉/杜邦/CAR/文献） |
| 只要方法论模板，不要 M&A 论文 | → §3 精简为纯方法论模板 |
| 改进流水线本身 | → §4 扩展流水线 / §6 方法论改进 |
| 教学/培训用 | → §5 教学/培训用途 |
| 做成可执行工具 | → §11 工程化方向（Validator→Scaffolder→Runner→Provenance） |
| 先了解不该做什么 | → §12 反模式（10 条，本项目实际踩过的坑） |

> **不知道怎么选？** 文档开头的**决策树**（3 个问题）可以在 30 秒内帮你定位起点。

---

## 许可证

本项目采用**分层许可**：

- **文档、数据、图表**（README、playbook、论文、报告、模板、JSON 配置、图片）：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — 可自由分享、改编，需注明出处
- **代码**（`scripts/*.py`、`.githooks/pre-push`）：[MIT](LICENSE-CODE) — 可自由使用、修改、分发，需保留版权声明

详见 [`LICENSE`](LICENSE)（CC BY 4.0）和 [`LICENSE-CODE`](LICENSE-CODE)（MIT）。

---

## 引用

如果你在学术工作中引用了本项目的方法论，请使用以下格式：

> Acerolaorion. (2026). *多模型学术生产流水线：中国上市公司并购重组成功案例研究* [Methodology demonstration]. GitHub. https://github.com/redamancy231-create/ma-case-study-pipeline

```bibtex
@misc{acerolaorion2026mapipeline,
 author = {Acerolaorion},
 title = {Multi-Model Academic Production Pipeline: M\&A Case Study},
 year = {2026},
 howpublished = {GitHub repository},
 url = {https://github.com/redamancy231-create/ma-case-study-pipeline}
}
```

---

*生成模型：DeepSeek-V4-Pro（via Claude Code CLI） · 2026-07-22*