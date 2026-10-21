# awesome-universal-agent-skills

高质量 Agent Skills 精选导航与使用指南：提供固定来源、选择理由、许可与依赖边界，帮助读者按任务选择通用或平台专项能力。

> A curated directory of reusable Agent Skills with pinned upstream references, licensing notes, dependency guidance, and explicit validation limits. A navigation resource—not a bundled installer or a compatibility certification.

**32 项资源 · 8 个领域 · 精选推荐 7 项 · 按需使用（含专项）18 项 · 参考资源 7 项（其中受限参考 3 项）**

审阅基线：2026-10-20。11 项既有记录原样保留，新增 21 项；日期不是自动追踪最新版或稳定性认证。

本仓库是导航与原创说明，不是安装器、运行平台或第三方源码镜像。**推荐等级与验证等级分开**：新增 21 项均未做本地功能或客户端端到端测试；既有 EDA 的有限合成样例记录见[验证说明](docs/validation.md)。

- **精选**：有突出选择价值，仍须满足任务、依赖与权限条件。
- **按需 / 专项**：适合明确场景；并列互补不自动升级为精选。
- **参考**：用于方法查询或有边界的选择；标为 **受限参考** 的 Anthropic Office 三项仅提供原创介绍与原始链接，不提供源码提取、外部安装执行或再分发授权。

[逐项版本与依赖](docs/skills.md) · [同类选择指南](docs/comparisons.md) · [获取与回滚](docs/installation.md) · [客户端机制](docs/clients.md) · [数据目录](catalog.json)

## 分类导航

| 领域 | 数量 | 主要能力 |
|---|---:|---|
| [办公文档](#office) | 8 | Office 原生编辑、PDF 与文档提取 |
| [数据与图表](#data) | 3 | 数据画像、实验载体与图表 |
| [开发工程](#development) | 4 | 排障、测试与项目说明 |
| [自动化](#automation) | 1 | 浏览器 CLI |
| [Agent 通用能力](#agent) | 4 | Skill/MCP 创建、架构与完成证据 |
| [信息研究](#research) | 1 | AI 论文来源与关联信息 |
| [安全与质量](#security) | 7 | 安全规范、威胁、变更、扫描和供应链 |
| [前端与设计](#design) | 4 | 视觉、Python UI、React 性能与组件架构 |

<a id="office"></a>
## 办公文档

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [markitdown](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/markitdown) | 按需 / 专项 | 将多格式文档提取为 Markdown | 适合跨格式提取；不保留完整 Office 版式与对象。 [详情](docs/skills.md#k-dense-ai--markitdown) |
| [pdf (OpenAI)](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf) | 参考 | PDF 创建、提取、渲染与视觉检查 | 可按任务选库；不等于已验证版式。 [详情](docs/skills.md#openai--pdf) |
| [officecli-docx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-docx) | 按需 / 专项 | Word 对象、样式、页眉页脚与局部编辑 | 固定工具并禁自动安装/更新/刷新；分页保真未实测。 [详情](docs/skills.md#iofficeai--officecli-docx) |
| [officecli-xlsx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-xlsx) | 按需 / 专项 | 工作簿公式、样式、图表与透视表操作 | 专项采用；公式缓存、外链和结果须另验。 [详情](docs/skills.md#iofficeai--officecli-xlsx) |
| [officecli-pptx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx) | 按需 / 专项 | PPT 对象、文本、图表与模板修订 | 源与发行有实现差异；母版/字体/动画未验证。 [详情](docs/skills.md#iofficeai--officecli-pptx) |
| [docx (Anthropic)](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/docx) | **受限参考** | Word、批注和修订方法的原始资料介绍 | 专有许可；仅原创介绍与原链，不提供外部安装执行路线。 [详情](docs/skills.md#anthropics--docx) |
| [xlsx (Anthropic)](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/xlsx) | **受限参考** | 工作簿编辑、公式缓存与重算方法介绍 | 专有许可；服务合同及外链/宏限制独立适用。 [详情](docs/skills.md#anthropics--xlsx) |
| [pptx (Anthropic)](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/pptx) | **受限参考** | 演示文稿创建与模板编辑方法介绍 | 专有许可；不复制或打包脚本、模板和资产。 [详情](docs/skills.md#anthropics--pptx) |

<a id="data"></a>
## 数据与图表

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/exploratory-data-analysis) | 精选 | 有界 CSV/TSV 画像与严格 JSON 结构检查 | 标准库核心有有限合成样例记录；非通用 Excel 引擎。 [详情](docs/skills.md#k-dense-ai--exploratory-data-analysis) |
| [matplotlib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/matplotlib) | 按需 / 专项 | 静态图表、布局和 PNG/PDF/SVG 导出 | 补充数据表达；字体和可选科学包未完成功能验证。 [详情](docs/skills.md#k-dense-ai--matplotlib) |
| [jupyter-notebook](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook) | 按需 / 专项 | 实验/教程 notebook 脚手架与整理 | 与 EDA 互补；脚手架用标准库，路径需适配。 [详情](docs/skills.md#openai--jupyter-notebook) |

<a id="development"></a>
## 开发工程

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [systematic-debugging](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging) | 精选 | 复现、日志、单一假设与根因定位 | 低依赖排障方法；项目测试与附带脚本未验证。 [详情](docs/skills.md#obra--systematic-debugging) |
| [gh-fix-ci](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci) | 按需 / 专项 | GitHub Actions 失败检查与排障 | 标准库辅助脚本；需授权 gh/Git/网络。 [详情](docs/skills.md#openai--gh-fix-ci) |
| [create-readme](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/create-readme) | 参考 | README 结构与项目使用说明 | 轻量文档参考；远端示例与实际写作效果未验证。 [详情](docs/skills.md#github--create-readme) |
| [property-based-testing](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/property-based-testing/skills/property-based-testing) | 精选 | 属性、生成器与失败样例分析 | 识别空真/同义反复；新增依赖由用户决定。 [详情](docs/skills.md#trailofbits--property-based-testing) |

<a id="automation"></a>
## 自动化

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [playwright-cli](https://github.com/microsoft/playwright-cli/tree/b1a5903c5b633b8c9f843ad7b629c2a78437040c/skills/playwright-cli) | 按需 / 专项 | CLI 页面交互、截图、日志与测试 | 可留浏览器工件；配套 CLI 尚未核定，暂不直接安装。 [详情](docs/skills.md#microsoft--playwright-cli) |

<a id="agent"></a>
## Agent 通用能力

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [mcp-builder](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder) | 按需 / 专项 | MCP 工具契约、错误处理与评估 | 面向具体 API 集成；SDK、权限和部署版本另核。 [详情](docs/skills.md#anthropics--mcp-builder) |
| [skill-creator (OpenAI)](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator) | 参考 | 小而专注的 Skill 与资源结构设计 | 开放规范参考；辅助脚本与客户端路径有适配边界。 [详情](docs/skills.md#openai--skill-creator) |
| [verification-before-completion](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion) | 参考 | 完成声明前核对实际证据 | 复用证据纪律；文字规则不能替代真实门禁。 [详情](docs/skills.md#obra--verification-before-completion) |
| [agent-architecture](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/agent-architecture) | 按需 / 专项 | Agent 需求、控制边界与验证契约 | 架构设计不等于实现；PDF/图形交付工具另备。 [详情](docs/skills.md#github--agent-architecture) |

<a id="research"></a>
## 信息研究

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [huggingface-papers](https://github.com/huggingface/skills/tree/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-papers) | 按需 / 专项 | AI 论文正文、元数据与代码/模型关联 | 专项推荐公共读取；写端点另获授权。 [详情](docs/skills.md#huggingface--huggingface-papers) |

<a id="security"></a>
## 安全与质量

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [security-best-practices](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices) | 精选 | 支持语言/框架的安全最佳实践审阅 | 按需加载参考；不是完整安全认证。 [详情](docs/skills.md#openai--security-best-practices) |
| [security-threat-model](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model) | 精选 | 资产、信任边界和攻击路径建模 | 先确认关键假设；不执行利用或自动修复。 [详情](docs/skills.md#openai--security-threat-model) |
| [differential-review](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/differential-review/skills/differential-review) | 按需 / 专项 | 基于 diff、Git 历史的安全变更审查 | 与故障调查互补；CC BY-SA 4.0，插件集成可选。 [详情](docs/skills.md#trailofbits--differential-review) |
| [codeql](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/static-analysis/skills/codeql) | 按需 / 专项 | 数据库、查询套件与扫描质量守卫 | 工具许可与隔离构建是前提；不可信构建会执行代码。 [详情](docs/skills.md#trailofbits--codeql) |
| [supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor) | 按需 / 专项 | 清单/锁文件的供应链信号审计 | 包名/版本会外发；不支持所有锁文件，不是许可审计。 [详情](docs/skills.md#trailofbits--supply-chain-risk-auditor) |
| [agentic-actions-auditor](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/agentic-actions-auditor/skills/agentic-actions-auditor) | 按需 / 专项 | GitHub Actions 中 Agent 输入与权限路径 | 静态 Agent/CI 专项；不运行 CI 或自动改工作流。 [详情](docs/skills.md#trailofbits--agentic-actions-auditor) |
| [variant-analysis](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/variant-analysis/skills/variant-analysis) | 按需 / 专项 | 从已确认根因找其他同类实例 | 与 Debugging 并列；不是首次漏洞发现。 [详情](docs/skills.md#trailofbits--variant-analysis) |

<a id="design"></a>
## 前端与设计

| Skill（原始 GitHub 目录） | 建议 | 核心用途 | 选择理由与边界 |
|---|---|---|---|
| [frontend-design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design) | 精选 | 视觉方向、排版、配色与 UI 自检 | 不强制框架；设计质量与可访问性未实测。 [详情](docs/skills.md#anthropics--frontend-design) |
| [huggingface-gradio](https://github.com/huggingface/skills/tree/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-gradio) | 按需 / 专项 | Python 数据/模型交互界面 | 适合 Python 团队；匹配项目版本，不默认公开服务。 [详情](docs/skills.md#huggingface--huggingface-gradio) |
| [vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices) | 精选 | React/Next.js 取数、打包与渲染性能模式 | 70 份固定规则；MIT 声明及名称适配有边界，未测提速。 [详情](docs/skills.md#vercel-labs--react-best-practices) |
| [vercel-composition-patterns](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns) | 按需 / 专项 | 组合组件、状态归属与 React API 设计 | 与性能指南并列；React 19 规则不能套旧项目。 [详情](docs/skills.md#vercel-labs--composition-patterns) |

## 先看采用边界

- **OfficeCLI**：不自动安装、更新或刷新 Skill；固定 Skill 与 CLI 发行不是完整源码一致，复杂 Office 保真未实测。[采用条件](docs/installation.md#officecli)。
- **Vercel**：MIT 声明存在，第三方材料权利独立；名称/目录和已发现链接需适配，不宣称性能提升已实测。[React 选择](docs/comparisons.md#react)。
- **Anthropic Office**：仅受限参考导航；服务合同及专有条款独立适用，不因公开可读就取得复制、修改、商业或分发授权。
- **Trail of Bits**：本次条目为 CC BY-SA 4.0，不属于本仓库 CC BY 4.0；CodeQL 的工具许可、构建权限和供应链审计的数据外发条件另核。

E1 静态审阅、E2 上游示例/测试源码/设计/特定成功记录、E3 本地功能与 E4 客户端运行分别记录。**E2 不自动等于测试通过；所有条目的跨客户端运行均未验证。** 详见[证据范围](docs/validation.md)。

## 维护与许可证

新增资源、同类比较和版本更新遵循[选择规则](docs/selection-policy.md)与[贡献说明](CONTRIBUTING.md)；不以 Stars、个人安装状态或是否零依赖直接决定入库。

本仓库原创导览及有权许可的编辑表达采用 **CC BY 4.0**，见 [LICENSE](LICENSE) 与[许可边界](LICENSE-NOTICE.md)。第三方 Skill、代码、资产、依赖、字体及服务保留各自许可；本项目不复制这些材料，也不提供对其重新授权。

以 [Agent Skills 开放规范](https://agentskills.io/specification)为格式基础；不要求安装全部客户端或使用任何特定管理器。
