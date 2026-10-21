# Agent Skills 精选库｜让 AI 助手掌握更专业的工作方法

Agent Skills 是给 AI 助手的“专业工作手册”：把可复用的步骤、规则和资料交给它，用来排查错误、整理数据、制作内容等。本库精选 **32 项**，告诉你适合选谁、需要准备什么，以及如何开始。

**先从下面的任务表选你要做的事。** 办公与数据用户看[不写代码的入门路径](docs/quickstart.md#everyday)；想亲手添加 Skill 的开发者看[Codex App 完整案例](docs/hands-on.md#create-readme)。你不用先学会 Git 或读源码；教程中的客户端操作仍待实际环境验证。

> A curated guide to 32 Agent Skills: choose by task, follow beginner walkthroughs, and check actual loading and results. English readers: [client guide and official links](docs/client-guides.md#sources) · [pinned sources and details](docs/skills.md).

<a id="tasks"></a>
## 我想让 AI 做什么？

| 我想做的事 | 先了解哪个 | 下一步点这里 |
|---|---|---|
| 处理 Word、Excel、PPT | OfficeCLI 三项分别处理文档、工作簿、演示文稿；需额外工具 | [先分清 Excel 分析与原生编辑](docs/quickstart.md#excel) · [Office 选择](docs/usage.md#office) |
| 修复代码错误 | systematic-debugging：先复现、找根因，再提修复 | [调试案例](docs/hands-on.md#systematic-debugging) |
| 分析数据、生成图表 | exploratory-data-analysis 检查数据；matplotlib 画图 | [数据选择与示例](docs/usage.md#data) |
| 自动操作网页 | playwright-cli：测试页交互、截图与日志 | [使用条件与版本配对缺口](docs/usage.md#microsoft--playwright-cli) |
| 制作网页 | frontend-design 帮你定视觉方向；React 项目再看性能规则 | [网页设计用途与示例](docs/usage.md#anthropics--frontend-design) |
| 创建自己的 Agent 或 Skill | skill-creator 写工作手册；agent-architecture 设计 Agent；mcp-builder 设计工具接口 | [怎么选择](docs/usage.md#agent) |
| 查找论文、整理资料 | huggingface-papers 读取指定 AI 论文及关联信息 | [研究用途与边界](docs/usage.md#research) |
| 检查代码安全 | security-best-practices 看常见写法；security-threat-model 看应用风险 | [安全选择](docs/usage.md#security) |

每行都指向现有介绍或案例。Office、浏览器和绘图通常要额外工具，暂不能当作“复制一段话就装好”。Anthropic Office 三项只作受限参考。

## 第一次使用？选适合你的路线

| 你现在的情况 | 从哪里开始 | 这条路能帮你完成什么 |
|---|---|---|
| 我主要处理文档或数据，不写代码 | [普通用户入门](docs/quickstart.md#everyday) | 按任务选 Skill、判断是否需要额外工具；不要求先做编程练习 |
| 我是开发者，想亲手添加一个 Skill | [Codex App 跟做案例](docs/hands-on.md#create-readme) | 获取固定文件、放入练习项目、请求加载并检查结果 |
| 我已经选好 Skill，要查看客户端操作 | [客户端教程](docs/client-guides.md) | 选择 Codex App/CLI、Claude Code 或 OpenCode 的独立路径 |

共同顺序是：**选任务 → 看条件 → 按客户端添加或使用已有能力 → 检查发现、加载和结果**。没有匹配工具时先停在条件确认，不必为了读本库安装一套开发环境。[怎么确认真的生效？](docs/quickstart.md#success)

## 开发者可先练习的四项

| Skill | 能帮什么 | 准备什么 / 谁适合 | 教程 |
|---|---|---|---|
| create-readme | 给小项目写清楚的说明书 | 纯文本编辑器；第一次添加 Skill 的用户 | [Codex App 从零跟做](docs/hands-on.md#create-readme) |
| systematic-debugging | 先找原因再改程序 | 项目已有复现工具；初级开发者 | [可复核的排障案例](docs/hands-on.md#systematic-debugging) |
| verification-before-completion | 完成前核对真实证据 | 项目已有检查工具；开发与交付人员 | [故意失败的检查案例](docs/hands-on.md#verification-before-completion) |
| security-threat-model | 看清应用资产、边界与风险 | 可读的项目源码；了解架构的开发者 | [只读威胁分析案例](docs/hands-on.md#security-threat-model) |

这是开发者的**可选学习顺序**，不改变原有推荐等级，也不表示教程已通过客户端测试。办公用户可直接进入下面的办公、数据目录。

## 完整目录：32 项，八个领域

点击“介绍与示例”看通俗用途、场景、额外工具、使用限制和原始 GitHub 来源；详细安装只对有明确方案的案例提供。

<a id="office"></a>
### 办公文档（8）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| markitdown | 把文档转成可读文本 | 文档处理开发者 | [介绍与示例](docs/usage.md#k-dense-ai--markitdown) |
| pdf (OpenAI) | 生成并检查 PDF | 文档人员/开发者 | [介绍与示例](docs/usage.md#openai--pdf) |
| officecli-docx | 用命令工具修改 Word | 办公技术人员 | [介绍与示例](docs/usage.md#iofficeai--officecli-docx) |
| officecli-xlsx | 用命令工具修改 Excel | 办公技术人员 | [介绍与示例](docs/usage.md#iofficeai--officecli-xlsx) |
| officecli-pptx | 用命令工具修改 PPT | 办公技术人员 | [介绍与示例](docs/usage.md#iofficeai--officecli-pptx) |
| docx (Anthropic) **仅受限参考** | 了解 Anthropic 的 Word 方法（受限参考） | 比较 Office 处理方法的读者 | [介绍，不提供安装](docs/usage.md#anthropics--docx) |
| xlsx (Anthropic) **仅受限参考** | 了解 Anthropic 的 Excel 方法（受限参考） | 比较 Excel 技术路线的读者 | [介绍，不提供安装](docs/usage.md#anthropics--xlsx) |
| pptx (Anthropic) **仅受限参考** | 了解 Anthropic 的 PPT 方法（受限参考） | 比较演示文稿方法的读者 | [介绍，不提供安装](docs/usage.md#anthropics--pptx) |

<a id="data"></a>
### 数据与图表（3）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| exploratory-data-analysis | 数据体检 | 数据分析人员 | [介绍与示例](docs/usage.md#k-dense-ai--exploratory-data-analysis) |
| matplotlib | 把数据画成图 | 有 Python 环境的数据人员 | [介绍与示例](docs/usage.md#k-dense-ai--matplotlib) |
| jupyter-notebook | 整理可复现的分析笔记 | Jupyter 用户 | [介绍与示例](docs/usage.md#openai--jupyter-notebook) |

<a id="development"></a>
### 开发工程（4）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| systematic-debugging | 有条理地排障 | 能读基本代码的开发者 | [介绍与示例](docs/usage.md#obra--systematic-debugging) |
| gh-fix-ci | 排查 GitHub 自动检查失败 | 已有 GitHub 项目权限的开发者 | [介绍与示例](docs/usage.md#openai--gh-fix-ci) |
| create-readme | 给项目写说明书 | 项目作者 | [介绍与示例](docs/usage.md#github--create-readme) |
| property-based-testing | 用通用性质设计测试 | 已有测试环境的开发者 | [介绍与示例](docs/usage.md#trailofbits--property-based-testing) |

<a id="automation"></a>
### 自动化（1）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| playwright-cli | 让 AI 操作测试网页 | 有测试环境的开发者和测试人员 | [介绍与示例](docs/usage.md#microsoft--playwright-cli) |

<a id="agent"></a>
### Agent 通用能力（4）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| mcp-builder | 为 AI 设计工具接口 | 已有 API 需求的开发者 | [介绍与示例](docs/usage.md#anthropics--mcp-builder) |
| skill-creator (OpenAI) | 编写自己的 Skill | 工作流维护者 | [介绍与示例](docs/usage.md#openai--skill-creator) |
| verification-before-completion | 完成前先看证据 | 开发/交付人员 | [介绍与示例](docs/usage.md#obra--verification-before-completion) |
| agent-architecture | 设计 AI Agent 的工作结构 | 准备开发 Agent 的工程人员 | [介绍与示例](docs/usage.md#github--agent-architecture) |

<a id="research"></a>
### 信息研究（1）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| huggingface-papers | 读取 AI 论文资料 | 主要阅读 AI/计算机论文的研究者 | [介绍与示例](docs/usage.md#huggingface--huggingface-papers) |

<a id="security"></a>
### 安全与质量（7）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| security-best-practices | 检查常见代码安全问题 | 相关语言开发者 | [介绍与示例](docs/usage.md#openai--security-best-practices) |
| security-threat-model | 画清应用面临的安全风险 | 开发/安全人员 | [介绍与示例](docs/usage.md#openai--security-threat-model) |
| differential-review | 重点审查代码变更的安全影响 | 代码审查者 | [介绍与示例](docs/usage.md#trailofbits--differential-review) |
| codeql | 规划和检查 CodeQL 扫描 | 有受控扫描环境的安全工程师 | [介绍与示例](docs/usage.md#trailofbits--codeql) |
| supply-chain-risk-auditor | 检查软件依赖的风险信号 | 开发/安全人员 | [介绍与示例](docs/usage.md#trailofbits--supply-chain-risk-auditor) |
| agentic-actions-auditor | 检查 AI 自动工作流的输入与权限 | CI 维护者 | [介绍与示例](docs/usage.md#trailofbits--agentic-actions-auditor) |
| variant-analysis | 寻找同一根因的其他实例 | 已掌握明确漏洞根因的安全人员 | [介绍与示例](docs/usage.md#trailofbits--variant-analysis) |

<a id="design"></a>
### 前端与设计（4）

| Skill | 中文用途 | 适合谁 | 使用指南 |
|---|---|---|---|
| frontend-design | 设计有明确风格的网页 | 前端开发者与设计协作人员 | [介绍与示例](docs/usage.md#anthropics--frontend-design) |
| huggingface-gradio | 搭建简单交互演示界面 | 有 Python 环境的开发者和研究者 | [介绍与示例](docs/usage.md#huggingface--huggingface-gradio) |
| vercel-react-best-practices | 检查 React 页面性能写法 | React 开发者 | [介绍与示例](docs/usage.md#vercel-labs--react-best-practices) |
| vercel-composition-patterns | 整理 React 组件接口 | 维护 React 组件库的开发者 | [介绍与示例](docs/usage.md#vercel-labs--composition-patterns) |

## 遇到问题与进阶资料

[找不到 / 没调用 / 缺工具 / 重名 / 安全撤销](docs/quickstart.md#faq) · [如何确认真的生效](docs/quickstart.md#success)

需要精确选择时再看：[同类比较](docs/comparisons.md) · [固定来源、许可证和依赖](docs/skills.md) · [采用门槛与回滚](docs/installation.md) · [其他客户端机制](docs/clients.md) · [验证证据 E1～E4](docs/validation.md)。

原创导览采用 [CC BY 4.0](LICENSE)，不替代[第三方许可与权利边界](LICENSE-NOTICE.md)。Anthropic Office 三项仅限原创介绍与原链导航，不提供未经授权的源码提取、外部安装执行或再分发路线。

目录事实沿用已批准的 V1.1：精选 7、按需/专项 18、参考 7（受限参考 3）。新增 21 项没有本地功能或客户端端到端通过记录；既有 EDA 仅有有限核心样例，范围见验证说明。本轮只改善使用指南，不改变这些结论。

维护者入口：[收录原则](docs/selection-policy.md) · [贡献方法](CONTRIBUTING.md) · [结构化目录](catalog.json) · [数据约束](catalog.schema.json)。
