# 真正用得上的 Agent Skills

> 为 AI 加一份专门的做事指南：先找到要解决的事，再选适合你工具的那一项。

**20 项认真选择的 Skill，8 项优先了解，12 项专项选择。** 不堆数量，不要求先学 Git，也不把“能添加”写成“已运行成功”。

**[按任务找 ↓](#find) · [按 AI 工具找 ↓](#clients) · [第一次使用 ↓](#start) · [可搜索目录](#search)**

想让 AI 改 Excel、排查错误、画图或做网页？这里帮你判断选谁、先准备什么，并在**一张卡片内**给出固定来源、添加路径、中文示例和撤销方法。下载的是原作者材料，本仓库不打包第三方 Skill。

<a id="find"></a>

## 你想让 AI 帮什么忙？

| 我想…… | 从这里开始 | 开始前知道 |
| --- | --- | --- |
| 看懂 CSV / TSV 数据 | [先看懂一份数据](skills/k-dense-ai--exploratory-data-analysis.md) | 需要 Python；先体检，不改原表 |
| 把数据画成图 | [把数据画成清晰的图](skills/k-dense-ai--matplotlib.md) | 需要绘图环境；检查字体和数据 |
| 读一批文档、提取文字 | [把文档变成 AI 易读的文字](skills/k-dense-ai--markitdown.md) | 提取内容，不保留原版式 |
| 修改 Word、Excel、PPT | [Word](skills/iofficeai--officecli-docx.md) · [Excel](skills/iofficeai--officecli-xlsx.md) · [PPT](skills/iofficeai--officecli-pptx.md) | 专项：先准备 OfficeCLI，尚非即装即用 |
| 让 AI 修复代码错误 | [让 AI 先找原因，再修代码](skills/obra--systematic-debugging.md) | 沿用项目日志和测试工具 |
| 让网页更好看、更好维护 | [做一个有设计感的网页](skills/anthropics--frontend-design.md) · [React 性能](skills/vercel-labs--react-best-practices.md) · [组件结构](skills/vercel-labs--composition-patterns.md) | 后两项面向 React；无需 Vercel 账号 |
| 查代码或依赖的安全风险 | [变更安全审查](skills/trailofbits--differential-review.md) · [依赖风险](skills/trailofbits--supply-chain-risk-auditor.md) | 不能代替专业验收；外发数据先确认 |
| 创建 Agent 或工具接口 | [Agent 设计](skills/github--agent-architecture.md) · [MCP 接口](skills/anthropics--mcp-builder.md) | 面向开发者，不是现成服务 |
| 读 AI 论文 | [论文与关联资料](skills/huggingface--huggingface-papers.md) | 需要联网，只读公开资料 |

**想自动操作网页？** 目前没有给新手推荐可复现的固定组合；[原 Playwright CLI 记录](archive/README.md)保留供参考，不用其他能力冒充浏览器自动化。

<a id="start"></a>

## 第一次用，从这里开始

Skill 通常是一个带 `SKILL.md` 的文件夹，告诉 AI 如何完成特定任务；它不会自动给电脑装好 Python、Office 或其他工具。

1. **先看卡片的“适合我吗”和“开始前要有什么”。** 普通办公用户可以先看上面的文档/数据入口；开发者可从[系统排障](skills/obra--systematic-debugging.md)开始。缺工具就先停，不必照抄命令。

2. **在同一张卡片展开你使用的 AI 工具。** 直接复制准备任务，让 AI 只获取固定单项；也可按卡片手工下载。已有同名项时停止。

3. **按该工具的方式加载，再复制中文任务试一个副本。** 请 AI 说出实际读取的文件路径，核对真正生成的结果。能说出名字不等于已经生效。

不会操作也没关系：把卡片的准备任务交给当前 AI。若它没有网络/文件权限，卡片会提供原文件入口；不要让它凭空补出资源。所有添加说明均待各客户端实际验收。

<a id="clients"></a>

## 我使用的是哪个 AI 工具？

来源公司不是使用限制。下面按**官方发现或导入机制**分组；每项仍要满足自己的工具条件，不代表我们已逐项实测。

| 工具 | 这份目录怎么用 |
| --- | --- |
| [Codex App / CLI](docs/clients.md#codex) | 项目内 `.agents/skills/技能名/`；卡片内有专属步骤 |
| [OpenCode](docs/clients.md#opencode) | 项目内 `.agents/skills/技能名/`；卡片内有专属步骤 |
| [Claude Code](docs/clients.md#claude) | 项目内 `.claude/skills/技能名/`；卡片内有专属步骤 |
| [Cursor](docs/clients.md#cursor) | 项目内 `.agents/skills/技能名/`；卡片内有专属步骤 |
| [Kimi Code](docs/clients.md#kimi) | 项目内 `.agents/skills/技能名/`；卡片内有专属步骤 |
| [Qoder IDE / CLI](docs/clients.md#qoder) | 项目内 `.qoder/skills/技能名/`；卡片内有专属步骤 |
| [QoderWork](docs/clients.md#qoderwork) | 独立技能面板导入；包格式/资源保留待验证；卡片内有专属步骤 |
| [WorkBuddy](docs/clients.md#workbuddy) | 独立技能面板导入；包格式/资源保留待验证；卡片内有专属步骤 |

<a id="search"></a>

## 查找与筛选

- **直接在 GitHub 用：** 下方按任务浏览；电脑按 `Ctrl + F`（Mac：`Command + F`）搜索中文任务或英文名称。

- **想搜索、按任务与门槛筛选，并选择 AI 配置路径：** [打开在线 Skill 目录](https://leilinfeng007-eng.github.io/awesome-universal-agent-skills/)，无需下载文件。搜索词只在本机浏览器内处理，无后端或追踪。

<a id="all"></a>

## 全部当前推荐

“优先了解”表示用途常见、入口相对清楚；“专项选择”表示需要更多工具或有特定场景。它们不是测试成绩。

### 处理 Word、Excel、PPT / 文档

| Skill / 用途 | 选择条件 |
| --- | --- |
| [把文档变成 AI 易读的文字](skills/k-dense-ai--markitdown.md)<br><sub>markitdown · 优先了解</sub> | 提取内容，不保留 Word/PPT 原版式；K-Dense 指南使用 Microsoft 工具。 |
| [按对象修改 Word 文档](skills/iofficeai--officecli-docx.md)<br><sub>officecli-docx · 专项选择</sub> | 尚非添加即用；复杂分页、字段与修订效果要检查副本。 |
| [修改 Excel 单元格、公式和图表](skills/iofficeai--officecli-xlsx.md)<br><sub>officecli-xlsx · 专项选择</sub> | 不保证复杂公式、宏、缓存与 Excel 引擎完全一致。 |
| [按模板修改 PPT 内容与图表](skills/iofficeai--officecli-pptx.md)<br><sub>officecli-pptx · 专项选择</sub> | 母版、动画、字体和实际版面仍需核对；先改副本。 |

### 看数据、做图表

| Skill / 用途 | 选择条件 |
| --- | --- |
| [先看懂一份数据](skills/k-dense-ai--exploratory-data-analysis.md)<br><sub>exploratory-data-analysis · 优先了解</sub> | 先做数据体检，不直接改 Excel；JSON 仅做结构画像。 |
| [把数据画成清晰的图](skills/k-dense-ai--matplotlib.md)<br><sub>matplotlib · 优先了解</sub> | 适合静态图；必须另查字体、标注、裁切和输出覆盖。 |

### 修错误、补测试

| Skill / 用途 | 选择条件 |
| --- | --- |
| [让 AI 先找原因，再修代码](skills/obra--systematic-debugging.md)<br><sub>systematic-debugging · 优先了解</sub> | 先复现，再拿证据验证一个原因；不会代替项目测试。 |
| [让测试发现更多边界问题](skills/trailofbits--property-based-testing.md)<br><sub>property-based-testing · 优先了解</sub> | 围绕不变量生成用例；不能替代业务验收。入口 effort 字段可能需适配。 |

### 做网页与交互界面

| Skill / 用途 | 选择条件 |
| --- | --- |
| [做一个有设计感的网页](skills/anthropics--frontend-design.md)<br><sub>frontend-design · 优先了解</sub> | 不限定 React 或模型品牌；审美建议不等于无障碍验收。 |
| [检查 React 与 Next.js 性能写法](skills/vercel-labs--react-best-practices.md)<br><sub>vercel-react-best-practices · 优先了解</sub> | 先选与项目版本匹配的规则，不承诺测得提速。 |
| [整理越来越复杂的 React 组件](skills/vercel-labs--composition-patterns.md)<br><sub>vercel-composition-patterns · 优先了解</sub> | 用组合设计组件边界，不为简单组件强加架构。 |
| [给 Python 功能做一个演示界面](skills/huggingface--huggingface-gradio.md)<br><sub>huggingface-gradio · 专项选择</sub> | 不默认公开分享、上传数据或连接收费模型。 |

### 创建 Agent 与工具接口

| Skill / 用途 | 选择条件 |
| --- | --- |
| [给 AI 做一个能用的工具接口](skills/anthropics--mcp-builder.md)<br><sub>mcp-builder · 专项选择</sub> | 先设计输入、错误处理与评估，再实现；不默认部署。 |
| [先想清楚 Agent 怎么分工与停下](skills/github--agent-architecture.md)<br><sub>agent-architecture · 专项选择</sub> | 先给边界、预算和停止条件，不自动实施、部署或训练。 |

### 读论文与找资料

| Skill / 用途 | 选择条件 |
| --- | --- |
| [读取 AI 论文与关联资料](skills/huggingface--huggingface-papers.md)<br><sub>huggingface-papers · 专项选择</sub> | 仅推荐公共读取，不执行作者认领、索引等写操作。 |

### 查代码与依赖风险

| Skill / 用途 | 选择条件 |
| --- | --- |
| [检查一次代码改动的安全风险](skills/trailofbits--differential-review.md)<br><sub>differential-review · 专项选择</sub> | 只读审查；不运行被审项目脚本，可选子代理不默认可用。 |
| [找到同一漏洞的其他藏身处](skills/trailofbits--variant-analysis.md)<br><sub>variant-analysis · 专项选择</sub> | 没有已确认实例时先排障；限制搜索范围和迭代次数。 |
| [看看项目依赖有没有风险信号](skills/trailofbits--supply-chain-risk-auditor.md)<br><sub>supply-chain-risk-auditor · 专项选择</sub> | 会向公开服务查询包名与版本；私有依赖先确认是否可外发。 |
| [检查 GitHub Actions 中 AI 的权限风险](skills/trailofbits--agentic-actions-auditor.md)<br><sub>agentic-actions-auditor · 专项选择</sub> | 分析攻击路径，不执行示例攻击命令，不运行 CI。 |
| [用 CodeQL 深入查代码漏洞](skills/trailofbits--codeql.md)<br><sub>codeql · 专项选择</sub> | 构建会执行项目代码；先确认授权和受控环境，不面向零基础。 |

## 我们怎样做选择

看独立实用价值、原始维护方、资源是否完整、必要工具与长期获取条件；不按 Stars 排名。能清楚说明适用场景和限制，才放进当前目录。相似但用途不同的项可以并列；暂停推荐的内容保留在[历史参考区](archive/README.md)。

**验证说清楚：** 只有 EDA 的受限核心有历史本地合成样例记录；本轮没有安装或运行第三方 Skill，所有条目的跨客户端运行仍未验证。每张卡片可展开原始证据，不把推荐当成功保证。

## 维护与来源

[怎么贡献和更新](CONTRIBUTING.md) · [数据与构建方式](docs/maintenance.md) · [结构化目录](catalog.json) · [许可证边界](LICENSE-NOTICE.md) · [历史参考](archive/README.md)

原创导览采用 CC BY 4.0；原创构建代码采用 MIT。第三方 Skill 和依赖保留各自许可，仓库不镜像它们的代码。

---

**English:** A carefully curated, Chinese-first guide to practical Agent Skills. Find a task, understand the prerequisites, and get a pinned-source setup and usage card for your AI tool. Optional online search; no backend, tracking, or bundled third-party Skills.
