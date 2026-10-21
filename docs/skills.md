# Skill 条目详情

[先看通俗用途与中文示例](usage.md)，再查本页固定版本、依赖与完整边界。

本页与 catalog.json 的 **32 项**一一对应，按下方分类索引查找。完整 Commit 是审阅基线，不是最佳稳定版认证。推荐/参考定位、安装授权和运行证据互不替代；新增 21 项 function=not_tested，所有条目 cross_client_runtime=not_verified。

受限参考条目仅供原创介绍与原链查询，[一般获取步骤](installation.md)不适用于它们。比较技术路线见[同类选择指南](comparisons.md)。

| 分类 | 数量 | 条目索引 |
|---|---:|---|
| 办公文档 | 8 | [markitdown](#k-dense-ai--markitdown) · [pdf (OpenAI)](#openai--pdf) · [officecli-docx](#iofficeai--officecli-docx) · [officecli-xlsx](#iofficeai--officecli-xlsx) · [officecli-pptx](#iofficeai--officecli-pptx) · [docx (Anthropic)](#anthropics--docx) · [xlsx (Anthropic)](#anthropics--xlsx) · [pptx (Anthropic)](#anthropics--pptx) |
| 数据与图表 | 3 | [exploratory-data-analysis](#k-dense-ai--exploratory-data-analysis) · [matplotlib](#k-dense-ai--matplotlib) · [jupyter-notebook](#openai--jupyter-notebook) |
| 开发工程 | 4 | [systematic-debugging](#obra--systematic-debugging) · [gh-fix-ci](#openai--gh-fix-ci) · [create-readme](#github--create-readme) · [property-based-testing](#trailofbits--property-based-testing) |
| 自动化 | 1 | [playwright-cli](#microsoft--playwright-cli) |
| Agent 通用能力 | 4 | [mcp-builder](#anthropics--mcp-builder) · [skill-creator (OpenAI)](#openai--skill-creator) · [verification-before-completion](#obra--verification-before-completion) · [agent-architecture](#github--agent-architecture) |
| 信息研究 | 1 | [huggingface-papers](#huggingface--huggingface-papers) |
| 安全与质量 | 7 | [security-best-practices](#openai--security-best-practices) · [security-threat-model](#openai--security-threat-model) · [differential-review](#trailofbits--differential-review) · [codeql](#trailofbits--codeql) · [supply-chain-risk-auditor](#trailofbits--supply-chain-risk-auditor) · [agentic-actions-auditor](#trailofbits--agentic-actions-auditor) · [variant-analysis](#trailofbits--variant-analysis) |
| 前端与设计 | 4 | [frontend-design](#anthropics--frontend-design) · [huggingface-gradio](#huggingface--huggingface-gradio) · [vercel-react-best-practices](#vercel-labs--react-best-practices) · [vercel-composition-patterns](#vercel-labs--composition-patterns) |

<a id="k-dense-ai--exploratory-data-analysis"></a>
## exploratory-data-analysis

- **分类 / 建议**：数据与图表 / 精选推荐。
- **用途**：有界 CSV/TSV 数据画像、缺失与重复检查、异常敏感性及严格 JSON 结构检查。
- **原始来源**：[K-Dense-AI/scientific-agent-skills — skills/exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/exploratory-data-analysis)。上游维护方：K-Dense Inc.。
- **完整 Commit**：`593377bb048752abb0152deab9fbb1083a6087df`。版本说明：metadata 1.4；review 2026-09-30。
- **许可**：[MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：Python 3.11+ 标准库；可选科学格式不属于核心。
- **推荐原因**：标准库核心依赖轻、输入输出边界明确，并有小型合成样例的结果核对记录。
- **采用门槛**：确认使用范围仅为标准库核心，并保留源文件与输出覆盖保护。
- **功能验证**：维护者记录：16 次本地核心 CLI 调用、41 项独立数值与保护核对；仅合成小样例，非完整上游测试。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：对授权测试 CSV 报告行列、缺失、重复与异常风险，写新报告并保留源文件。
- **限制**：
  - JSON 核心仅作结构画像，不是通用表格统计引擎。
  - 分组金额求和不是原生功能；缺失分组键不能静默当成普通组。
  - Excel、大文件及可选科学格式未获得本目录的功能验证。

<a id="obra--systematic-debugging"></a>
## systematic-debugging

- **分类 / 建议**：开发工程 / 精选推荐。
- **用途**：以复现、日志和单一假设定位根因，再提出最小修复与验证。
- **原始来源**：[obra/superpowers — skills/systematic-debugging](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging)。上游维护方：obra / Superpowers 项目。
- **完整 Commit**：`bb92a77741419a4ab5f06e711a283343f1ada0c3`。版本说明：仓库v7.0.0对应Commit。
- **许可**：[MIT](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/LICENSE)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：文本核心无新增包；需要目标项目已有日志和验证工具。
- **推荐原因**：可独立采用的低依赖方法；无需默认安装整套开发框架。
- **采用门槛**：只选择单项及相对参考资料；项目测试副作用单独审查。
- **功能验证**：已审阅文本与关键风险；没有执行附带脚本或项目行为测试。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：先给故障复现和根因证据，再按授权决定是否修改项目。
- **限制**：
  - 流程行为与代理遵守度未验证。
  - 附带 find-polluter.sh 会执行项目 npm test，并用 || true 处理失败；不能把它当作测试成功证明。

<a id="k-dense-ai--markitdown"></a>
## markitdown

- **分类 / 建议**：办公文档 / 按需使用。
- **用途**：将多种文档提取为 Markdown，供检索、摘要和批处理使用。
- **原始来源**：[K-Dense-AI/scientific-agent-skills — skills/markitdown](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/markitdown)。上游维护方：K-Dense Inc.。
- **完整 Commit**：`593377bb048752abb0152deab9fbb1083a6087df`。版本说明：包装metadata2.5；底层Microsoft库候选0.1.8。
- **许可**：[MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：Python >=3.10,<3.15；包装指南使用 uv；仅选择必要的转换器 extras。
- **推荐原因**：Microsoft 底层工具有发行和测试基础；适合有持续跨格式提取需求的项目。
- **采用门槛**：包装与底层库分别固定；只审并安装实际所需格式的 extras。
- **功能验证**：静态审阅；底层候选版本 0.1.8 和具体转换器运行未验证。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：把指定测试文档提取到新的 Markdown 输出目录，并列出转换局限。
- **限制**：
  - 该 Skill 包装由 K-Dense 提供，不是 Microsoft 官方 Skill。
  - 文本提取不保留完整 Office 版式、公式或原生对象。
  - 转换器、extras 和传递依赖未完成运行验证；不默认启用云、OCR、URL 或插件。
- **底层工具候选（不等于已验证配套）**：
  - [Microsoft MarkItDown 0.1.8](https://github.com/microsoft/markitdown/releases/tag/v0.1.8)；状态 `candidate_not_runtime_verified`。

<a id="microsoft--playwright-cli"></a>
## playwright-cli

- **分类 / 建议**：自动化 / 按需使用。
- **用途**：通过浏览器 CLI 进行页面交互、截图、日志观察和功能测试。
- **原始来源**：[microsoft/playwright-cli — skills/playwright-cli](https://github.com/microsoft/playwright-cli/tree/b1a5903c5b633b8c9f843ad7b629c2a78437040c/skills/playwright-cli)。上游维护方：Microsoft / Playwright CLI 项目。
- **完整 Commit**：`b1a5903c5b633b8c9f843ad7b629c2a78437040c`。版本说明：已审Skill Commit；已核CLI v0.1.22另指b85c7a736bb473bf55b584e54a09ffa698d6d871。
- **许可**：[Apache-2.0](https://github.com/microsoft/playwright-cli/blob/b1a5903c5b633b8c9f843ad7b629c2a78437040c/LICENSE)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：Node.js 18+、配套 CLI、浏览器和相应执行权限。
- **推荐原因**：Microsoft 维护，工具与 Skill 分层清楚，可形成可重复的浏览器测试工件。
- **采用门槛**：先核同一发行版的 Skill/CLI 配套版本，再决定是否采用；不使用 latest。
- **功能验证**：静态审阅；CLI、浏览器及手册版本配对未验证。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：使用本地测试页和虚构表单，核对断言与截图，关闭临时会话。
- **限制**：
  - 已审 Skill Commit 与候选 CLI v0.1.22 不同，当前没有已验证的配套安装组合。
  - 浏览器会话可能访问网络或提交表单；不默认使用生产账号。
  - allowed-tools 声明不是跨客户端权限保证。
- **底层工具候选（不等于已验证配套）**：
  - [Playwright CLI 0.1.22](https://github.com/microsoft/playwright-cli/releases/tag/v0.1.22)；状态 `not_paired_with_reviewed_skill_commit`。 Commit `b85c7a736bb473bf55b584e54a09ffa698d6d871`。

<a id="anthropics--mcp-builder"></a>
## mcp-builder

- **分类 / 建议**：Agent 通用能力 / 按需使用。
- **用途**：为明确的 API 设计 MCP 工具契约、错误处理与评估方案。
- **原始来源**：[anthropics/skills — skills/mcp-builder](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder)。上游维护方：Anthropic。
- **完整 Commit**：`dbd4588f9e1033efb41dad4bef2f7947c8993d44`。版本说明：无单项稳定发行版核实；按Commit固定。
- **许可**：[Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：阅读指南无新增包；开发需选定 Python/FastMCP 或 TypeScript MCP SDK 与目标 API。
- **推荐原因**：官方指南覆盖工具设计、结构化返回和评估；可按真实集成需求独立选用。
- **采用门槛**：固定所选 SDK/服务版本，独立核对许可与鉴权；不得把示例视为部署授权。
- **功能验证**：入口和目录许可证已审；完整评估资源、SDK 和服务运行未验证。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：先为经授权的只读 API 提出工具契约和权限边界，不自动部署服务。
- **限制**：
  - 它是开发指南，不是现成连接器、MCP 服务或通用 API 执行器。
  - 指南中的 main、最新 SDK 和 Inspector 示例不是固定依赖锁。
  - SDK、API 权限、资产及具体服务依赖需另核。

<a id="k-dense-ai--matplotlib"></a>
## matplotlib

- **分类 / 建议**：数据与图表 / 按需使用。
- **用途**：设计静态图表、布局并导出 PNG、PDF、SVG。
- **原始来源**：[K-Dense-AI/scientific-agent-skills — skills/matplotlib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/matplotlib)。上游维护方：K-Dense Inc.。
- **完整 Commit**：`593377bb048752abb0152deab9fbb1083a6087df`。版本说明：metadata1.4；文档目标Matplotlib3.11.2。
- **许可**：[MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 frontmatter 另指 Matplotlib 本身的许可，须保留相关声明。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：Python 3.11+；指南目标 Matplotlib 3.11.2；附带脚本还导入 NumPy、SciPy 或 cycler。
- **推荐原因**：补充数据画像以外的图表表达能力；可以优先利用已有绘图环境。
- **采用门槛**：先核最小依赖、字体与新输出路径；不为简单图强装科学环境。
- **功能验证**：入口与两个附带脚本已静态审阅、AST 解析通过；未运行或核对真实图像。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：对虚构汇总数据生成带单位与图例的静态图，使用 Agg 和全新输出目录。
- **限制**：
  - 不是只安装 Matplotlib 就能运行全部附带脚本；其他依赖版本尚未完整锁定。
  - savefig 可能直接覆盖输出，不能继承 EDA 的覆盖保护。
  - 图像、字体、GUI、LaTeX 和交互组件未验证。
- **底层工具候选（不等于已验证配套）**：
  - [Matplotlib 3.11.2](https://github.com/matplotlib/matplotlib/tree/v3.11.2)；状态 `guide_target_not_runtime_verified`。

<a id="openai--gh-fix-ci"></a>
## gh-fix-ci

- **分类 / 建议**：开发工程 / 按需使用。
- **用途**：读取 GitHub Actions 失败检查和日志，归纳原因并提出修复方案。
- **原始来源**：[openai/skills — skills/.curated/gh-fix-ci](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci)。上游维护方：OpenAI。
- **完整 Commit**：`49f948faa9258a0c61caceaf225e179651397431`。版本说明：无单项稳定发行版核实；按Commit固定。
- **许可**：[Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/LICENSE.txt)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：Python 标准库、Git、GitHub CLI（gh）和经授权的网络/仓库权限。
- **推荐原因**：独立标准库脚本，针对 CI 排障，与通用代码审查有不同价值。
- **采用门槛**：确认现有 gh 权限与日志处理范围；不自动登录、提权或更改仓库设置。
- **功能验证**：入口、许可证与检查脚本已静态审阅、AST 解析通过；没有 PR/API 运行验证。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：只读分析指定 PR 的失败检查，给出日志证据与修复建议，不自动提交。
- **限制**：
  - 仅覆盖 GitHub Actions；外部 CI 通常只报告详情链接。
  - 修复代码需要单独明确授权。
  - 脚本发现失败检查时可返回 1，不能直接将其视为脚本崩溃。

<a id="openai--pdf"></a>
## pdf (OpenAI)

- **分类 / 建议**：办公文档 / 参考资源。
- **用途**：编排 PDF 生成、提取、页面渲染和视觉校对。
- **原始来源**：[openai/skills — skills/.curated/pdf](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf)。上游维护方：OpenAI。
- **完整 Commit**：`49f948faa9258a0c61caceaf225e179651397431`。版本说明：按Commit；不是Anthropic同名实现。
- **许可**：[Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf/LICENSE.txt)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：按任务选择 reportlab、pdfplumber、pypdf 和 Poppler；不需要每次全部安装。
- **推荐原因**：来源与 Apache-2.0 目录许可清楚，可供缺少 PDF 能力的环境参考。
- **采用门槛**：优先复用已有能力；新环境按实际需要核对工具、字体和分发包许可。
- **功能验证**：入口、目录许可与结构已核；该固定 GitHub 版本未执行验证。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：在已有 PDF 工作流中渲染测试页面，检查文字、表格和布局。
- **限制**：
  - 这是 OpenAI 的条目，不能与其他仓库同名 PDF Skill 混用许可证。
  - 文本提取不证明页面版式正确；仍需渲染校对。
  - 现成 PDF 能力足够时无需重复注册该条目。

<a id="openai--skill-creator"></a>
## skill-creator (OpenAI)

- **分类 / 建议**：Agent 通用能力 / 参考资源。
- **用途**：设计小而专注的 SKILL.md、相对资源和按需加载结构。
- **原始来源**：[openai/skills — skills/.system/skill-creator](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator)。上游维护方：OpenAI。
- **完整 Commit**：`49f948faa9258a0c61caceaf225e179651397431`。版本说明：按Commit；目录有3个创建/验证辅助脚本。
- **许可**：[Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/LICENSE.txt)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：阅读指南无新增包；辅助脚本需要 Python/PyYAML；Codex 界面元数据属于可选适配。
- **推荐原因**：官方创建指南可作标准参考；已有创建器时无需再引入一套。
- **采用门槛**：优先复用既有创建器，并按官方开放规范人工复核工具差异。
- **功能验证**：入口、许可与 quick_validate 静态核对；其他辅助脚本未全审或执行。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：对照开放规范检查拟新增 Skill 的触发条件、相对引用、依赖和权限边界。
- **限制**：
  - 固定版本 quick_validate.py 的允许字段遗漏 compatibility，可能误拒合法入口。
  - 辅助验证器不是 Agent Skills 标准的唯一判据。
  - Codex 专属元数据、路径和工具名需要适配其他客户端。

<a id="github--create-readme"></a>
## create-readme

- **分类 / 建议**：开发工程 / 参考资源。
- **用途**：组织项目 README 的用途、安装、用法和交付说明。
- **原始来源**：[github/awesome-copilot — skills/create-readme](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/create-readme)。上游维护方：GitHub awesome-copilot 社区贡献者。
- **完整 Commit**：`613efc8c21d9b3ce642dff361d17006cd9967e28`。版本说明：按Commit；纯文本入口。
- **许可**：[MIT](https://github.com/github/awesome-copilot/blob/613efc8c21d9b3ce642dff361d17006cd9967e28/LICENSE)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：纯文本指南；部分示例引用远端 README。
- **推荐原因**：短小的文档结构参考；已有项目写作能力时不必增加全局入口。
- **采用门槛**：作为参考资源使用；如无独立收益，不重复安装提示词入口。
- **功能验证**：入口与仓库许可已静态审阅；写作效果与代理行为未验证。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：用现有写作能力核对项目 README 的安装、用法、限制是否与事实一致。
- **限制**：
  - GitHub 组织下的社区条目，不表示每条由 GitHub 核心团队直接维护。
  - 远端 main 示例可能变化；不构成可重复输出保证。
  - 只读取授权项目，不能因指南措辞扫描无关工作区。

<a id="obra--verification-before-completion"></a>
## verification-before-completion

- **分类 / 建议**：Agent 通用能力 / 参考资源。
- **用途**：在完成声明前核对真实命令、结果与尚未验证范围。
- **原始来源**：[obra/superpowers — skills/verification-before-completion](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion)。上游维护方：obra / Superpowers 项目。
- **完整 Commit**：`bb92a77741419a4ab5f06e711a283343f1ada0c3`。版本说明：仓库v7.0.0对应Commit；单文件文本。
- **许可**：[MIT](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/LICENSE)。仅指已审 Skill/仓库许可；依赖、资产及服务另行核对。 未完成所选分发版本全部传递依赖/资产的许可审计。
- **依赖**：纯文本核心；使用目标项目已有的验证工具。
- **推荐原因**：原则值得复用；已有验证约束时应避免重复门禁和上下文负担。
- **采用门槛**：已有等效约束时直接沿用，不叠加全局工作流。
- **功能验证**：文本静态审阅；行为压力测试未验证。
- **跨平台状态**：开放格式基础检查通过；官方机制和工具条件见客户端指南；跨客户端运行未验证。
- **使用示例**：交付时仅报告实际检查的结果，并区分静态通过和运行未验证。
- **限制**：
  - 文字规则不能替代程序门禁、安全沙箱或真实结果。
  - 验证命令本身也可能有副作用。
  - 不要求每次回复都重跑全量测试。

<a id="anthropics--frontend-design"></a>
## frontend-design

- **分类 / 建议**：前端与设计 / 精选推荐。
- **用途**：为新 UI 或既有界面建立明确视觉方向、排版、配色和自检流程。
- **原始来源**：[anthropics/skills — skills/frontend-design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design)；上游维护方：anthropics 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`dbd4588f9e1033efb41dad4bef2f7947c8993d44`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：文本及项目文件读写；实现和截图工具按项目已有环境选择。
- **联网 / 数据**：纯指导无需网络；字体、图片或外部资产须另获许可。
- **推荐原因**：不强制 React、特定 UI 包、MCP 或模型供应商；可以作为轻量设计指导层。 与框架性能规则、视觉缺陷检查互补，不替代自动化测试。
- **采用门槛**：设计品味不能替代可访问性或性能审计；只对授权的前端文件实施设计。 无可核实的效果评测结果；设计质量高度依赖模型和任务，E1 不等于成品保证。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：为新 UI 或既有界面建立明确视觉方向、排版、配色和自检流程。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 无可核实的效果评测结果；设计质量高度依赖模型和任务，E1 不等于成品保证。
  - 设计品味不能替代可访问性或性能审计；只对授权的前端文件实施设计。

<a id="openai--jupyter-notebook"></a>
## jupyter-notebook

- **分类 / 建议**：数据与图表 / 按需使用。
- **用途**：从实验或教程模板创建可读、可复现的 Jupyter notebook。
- **原始来源**：[openai/skills — skills/.curated/jupyter-notebook](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook)；上游维护方：openai 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`49f948faa9258a0c61caceaf225e179651397431`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook/LICENSE.txt)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：脚手架用 Python；原文示范 uv/Python 3.12。执行 notebook 另需项目内核和依赖。
- **联网 / 数据**：只生成文件无需网络；uv 拉解释器或安装内核可能联网，非本次动作。
- **推荐原因**：脚手架仅用 Python 标准库，已有输出默认拒绝覆盖。 与现有 EDA 并列：EDA 分析数据，Jupyter 组织可重复实验和教程；不是替换 EDA。
- **采用门槛**：示例硬编码 CODEX_HOME 安装位置；应使用实际 Skill 根目录和明确 --out，不自动 --force。不能执行不可信 notebook 单元。 只检查了脚本和两个模板结构；未创建或运行 notebook。跨客户端需改路径调用说明。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：从实验或教程模板创建可读、可复现的 Jupyter notebook。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 只检查了脚本和两个模板结构；未创建或运行 notebook。跨客户端需改路径调用说明。
  - 示例硬编码 CODEX_HOME 安装位置；应使用实际 Skill 根目录和明确 --out，不自动 --force。不能执行不可信 notebook 单元。

<a id="openai--security-best-practices"></a>
## security-best-practices

- **分类 / 建议**：安全与质量 / 精选推荐。
- **用途**：按 Python、JavaScript/TypeScript、Go 及框架加载安全最佳实践，形成定位到代码的报告。
- **原始来源**：[openai/skills — skills/.curated/security-best-practices](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices)；上游维护方：openai 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`49f948faa9258a0c61caceaf225e179651397431`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices/LICENSE.txt)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：项目源码和引用文档读取；报告写入；修复另受项目授权约束。
- **联网 / 数据**：核心指南离线可用；缺少框架证据时允许查官方资料。
- **推荐原因**：明确触发边界和语言范围，参考资料按需加载，不必安装扫描引擎。 与现有 systematic-debugging 不同：面向安全规范，而非定位一般故障。
- **采用门槛**：不能把模型审阅当扫描器、完整漏洞审计或安全认证；不自动扩大修复范围。 语言/框架覆盖有限；无本轮或可核对的端到端测试结果。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：按 Python、JavaScript/TypeScript、Go 及框架加载安全最佳实践，形成定位到代码的报告。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 语言/框架覆盖有限；无本轮或可核对的端到端测试结果。
  - 不能把模型审阅当扫描器、完整漏洞审计或安全认证；不自动扩大修复范围。

<a id="openai--security-threat-model"></a>
## security-threat-model

- **分类 / 建议**：安全与质量 / 精选推荐。
- **用途**：从源码提取资产、信任边界和攻击路径，给出带假设和代码依据的威胁模型。
- **原始来源**：[openai/skills — skills/.curated/security-threat-model](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model)；上游维护方：openai 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`49f948faa9258a0c61caceaf225e179651397431`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/LICENSE.txt)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：源码读取与 Markdown 报告写入；无必需第三方执行工具。
- **联网 / 数据**：核心可离线；外部系统细节必须由授权信息提供。
- **推荐原因**：将架构事实与假设分开，并要求用户确认影响威胁优先级的上下文。 最佳实践检查实现方式；威胁模型检查资产、边界与滥用场景，应并行使用而非相互替代。
- **采用门槛**：不执行渗透、利用或自动修复；报告不是证明不存在漏洞。 质量取决于架构信息和人工澄清；没有功能评测通过证据。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：从源码提取资产、信任边界和攻击路径，给出带假设和代码依据的威胁模型。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 质量取决于架构信息和人工澄清；没有功能评测通过证据。
  - 不执行渗透、利用或自动修复；报告不是证明不存在漏洞。

<a id="huggingface--huggingface-papers"></a>
## huggingface-papers

- **分类 / 建议**：信息研究 / 按需使用。
- **用途**：从 arXiv/Hugging Face paper 标识读取论文 Markdown 与结构化关联信息。
- **原始来源**：[huggingface/skills — skills/huggingface-papers](https://github.com/huggingface/skills/tree/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-papers)；上游维护方：huggingface 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`c3ff942be3e07116b475253f0a8fc4f54682c1a8`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Apache-2.0](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：HTTP/curl 或等效请求能力；公共读取不必预先找令牌。
- **联网 / 数据**：Hugging Face/arXiv；API 限流和来源覆盖需处理。
- **推荐原因**：围绕 AI 论文的作者、模型、数据集、代码链接及原文回退；没有必需的重型本地包。 与 MarkItDown/PDF 并列使用：这些解析给定文件，此项发现和关联 AI 论文来源。
- **采用门槛**：也列出作者认领、索引和改链接的写端点；本库建议范围仅公共读取，任何写端点另行明确授权。 主要覆盖 AI/计算机论文，不是综合文献检索、文献管理或事实核查系统；论文及下载内容保留各自许可。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：从 arXiv/Hugging Face paper 标识读取论文 Markdown 与结构化关联信息。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 主要覆盖 AI/计算机论文，不是综合文献检索、文献管理或事实核查系统；论文及下载内容保留各自许可。
  - 也列出作者认领、索引和改链接的写端点；本库建议范围仅公共读取，任何写端点另行明确授权。

<a id="huggingface--huggingface-gradio"></a>
## huggingface-gradio

- **分类 / 建议**：前端与设计 / 按需使用。
- **用途**：构建 Python Gradio 交互式数据与模型演示界面。
- **原始来源**：[huggingface/skills — skills/huggingface-gradio](https://github.com/huggingface/skills/tree/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-gradio)；上游维护方：huggingface 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`c3ff942be3e07116b475253f0a8fc4f54682c1a8`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Apache-2.0](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：Python、匹配项目版本的 Gradio；可启动本地服务、编辑应用。
- **联网 / 数据**：本地最小 Demo 可不调用模型；Spaces、远端 predict 或分享服务有网络和费用边界。
- **推荐原因**：为 Python 数据/ML 团队提供快速 UI，与 React 产品前端有不同最佳场景。 与 frontend-design 互补：提供具体 Python 组件实现，后者提供视觉原则。
- **采用门槛**：不默认公开服务、分享链接或上传文件；外部模型端点和依赖许可另行检查。 文档含较新的组件/CLI 接口，但未锁定验证过的 Gradio 版本；需要先对照已有项目版本。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：构建 Python Gradio 交互式数据与模型演示界面。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 文档含较新的组件/CLI 接口，但未锁定验证过的 Gradio 版本；需要先对照已有项目版本。
  - 不默认公开服务、分享链接或上传文件；外部模型端点和依赖许可另行检查。

<a id="trailofbits--differential-review"></a>
## differential-review

- **分类 / 建议**：安全与质量 / 按需使用。
- **用途**：对 PR、提交或 diff 进行风险优先的安全审查，追溯历史及影响范围。
- **原始来源**：[trailofbits/skills — plugins/differential-review/skills/differential-review](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/differential-review/skills/differential-review)；上游维护方：trailofbits 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：Git、源码/历史读取及报告写入；可手工使用附属方法文档。
- **联网 / 数据**：本地已有历史可离线；获取 PR/上游上下文另需只读网络权限。
- **推荐原因**：基于变化和 Git 历史，不把整仓库扫描当差异分析。 与现有 systematic-debugging 并列：一个审查安全变更，一个调查可复现故障；也不同于静态规范检查。
- **采用门槛**：不要执行被审项目构建/脚本来获取证据；可选命名子代理和 issue-writer 不属于独立核心，不能假定已安装。 只支持有比较基线的变更；模型安全结论仍需人工复核。独立使用需明确可选插件集成不启用。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：对 PR、提交或 diff 进行风险优先的安全审查，追溯历史及影响范围。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 只支持有比较基线的变更；模型安全结论仍需人工复核。独立使用需明确可选插件集成不启用。
  - 不要执行被审项目构建/脚本来获取证据；可选命名子代理和 issue-writer 不属于独立核心，不能假定已安装。

<a id="trailofbits--codeql"></a>
## codeql

- **分类 / 建议**：安全与质量 / 按需使用。
- **用途**：构建 CodeQL 数据库、补充数据模型、生成显式查询套件并检查结果质量。
- **原始来源**：[trailofbits/skills — plugins/static-analysis/skills/codeql](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/static-analysis/skills/codeql)；上游维护方：trailofbits 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)。CodeQL CLI 许可独立于 Skill：优先限公开开源项目或已具备有效授权的私有仓库。查询包（含社区包）的许可未全审，只能选择另行明确许可并锁版的必要包。构建不可信项目会执行其代码，必须在独立受控环境并单独批准。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：CodeQL CLI、Git、Bash、jq、uv、Python>=3.11、相应语言工具链；编译语言会运行构建并消耗磁盘/CPU。
- **联网 / 数据**：查询包、构建依赖或语言工具链可能联网；不默认上传 SARIF。
- **推荐原因**：空数据库/空查询集必须失败，针对“零发现是假干净”有实际守卫和测试。 作为成本较高的深度分析专项，与轻量指南/差异审查并列；不以此替换现有任何条目。
- **采用门槛**：CodeQL CLI 许可独立于 Skill：优先限公开开源项目或已具备有效授权的私有仓库。查询包（含社区包）的许可未全审，只能选择另行明确许可并锁版的必要包。构建不可信项目会执行其代码，必须在独立受控环境并单独批准。 查询包版本、工具链和平台组合未实际验证；macOS 构建有专门 workaround，不能自动安装 Homebrew/Rosetta。
- **验证范围**：E1 静态审阅；E2 材料类型：upstream_test_source；审阅空套件、CLI 非零退出、损坏输出及数据库质量测试；不是 CodeQL 引擎扫描通过证明。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：构建 CodeQL 数据库、补充数据模型、生成显式查询套件并检查结果质量。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 查询包版本、工具链和平台组合未实际验证；macOS 构建有专门 workaround，不能自动安装 Homebrew/Rosetta。
  - CodeQL CLI 许可独立于 Skill：优先限公开开源项目或已具备有效授权的私有仓库。查询包（含社区包）的许可未全审，只能选择另行明确许可并锁版的必要包。构建不可信项目会执行其代码，必须在独立受控环境并单独批准。

<a id="trailofbits--property-based-testing"></a>
## property-based-testing

- **分类 / 建议**：开发工程 / 精选推荐。
- **用途**：为序列化、归一化、排序、数值与状态不变量设计、审查并解释属性测试。
- **原始来源**：[trailofbits/skills — plugins/property-based-testing/skills/property-based-testing](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/property-based-testing/skills/property-based-testing)；上游维护方：trailofbits 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：按项目已有语言/测试框架选择 Hypothesis、fast-check、proptest 等；指导本体不强制新增依赖。
- **联网 / 数据**：已有框架可离线；新增库先核实版本和对应许可、再审批。
- **推荐原因**：明确识别同义反复、空真和无合适属性的场景；新增测试依赖由用户决定。 与现有验证声明 Skill 不同：此项指导如何构造有意义的测试，而非仅要求提供完成证据。
- **采用门槛**：运行项目测试也会执行项目代码；控制生成规模和运行预算，不自动写依赖清单。扩展字段 effort 需客户端容忍或适配。 上游评估场景和失败判据存在，但本轮未运行，不能推断缺陷检出率。
- **验证范围**：E1 静态审阅；E2 材料类型：upstream_usage_example, upstream_evaluation_design；检查生成器/边界示例及 Skill 外评估用例：依赖由用户决定，grader 要求不写依赖文件；未运行模型或评估。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：为序列化、归一化、排序、数值与状态不变量设计、审查并解释属性测试。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 上游评估场景和失败判据存在，但本轮未运行，不能推断缺陷检出率。
  - 运行项目测试也会执行项目代码；控制生成规模和运行预算，不自动写依赖清单。扩展字段 effort 需客户端容忍或适配。

<a id="trailofbits--supply-chain-risk-auditor"></a>
## supply-chain-risk-auditor

- **分类 / 建议**：安全与质量 / 按需使用。
- **用途**：从清单/锁文件检查 npm、PyPI、Go 依赖公告、发布集中度、废弃和安装脚本信号。
- **原始来源**：[trailofbits/skills — plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor)；上游维护方：trailofbits 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：Python>=3.11、uv、可选已授权 gh；只读目标清单，报告与缓存写目标仓库之外。
- **联网 / 数据**：OSV、npm/PyPI、Go proxy、deps.dev、GitHub、Scorecard；会外传包名和版本等依赖元数据。
- **推荐原因**：Python 标准库收集器区分 assessed/unassessable，按锁定版本核对公告，支持结果缓存。 补齐依赖供应链，与源码安全、凭据扫描及现有 CI 修复不同，不能互替。
- **采用门槛**：仅对已批准公开的依赖元数据使用；私有包名同样可能保密，必须先确认可外发。脚本通过既有 gh 获取 GitHub 凭据，不应把令牌输出、缓存或传给非 GitHub 端点。 不读 pnpm/yarn/poetry 锁文件；无测量不表示安全；不是许可证合规审计，也不检验包能否安装。
- **验证范围**：E1 静态审阅；E2 材料类型：upstream_test_source；核对精确 pin/范围、锁文件闭包、无法验证数据、缓存与渲染等测试断言；测试使用模拟数据，不代表在线数据源端到端已验证。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：从清单/锁文件检查 npm、PyPI、Go 依赖公告、发布集中度、废弃和安装脚本信号。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 不读 pnpm/yarn/poetry 锁文件；无测量不表示安全；不是许可证合规审计，也不检验包能否安装。
  - 仅对已批准公开的依赖元数据使用；私有包名同样可能保密，必须先确认可外发。脚本通过既有 gh 获取 GitHub 凭据，不应把令牌输出、缓存或传给非 GitHub 端点。

<a id="trailofbits--agentic-actions-auditor"></a>
## agentic-actions-auditor

- **分类 / 建议**：安全与质量 / 按需使用。
- **用途**：静态追踪 GitHub Actions 中外部输入到 AI Agent 的提示词、命令和权限路径。
- **原始来源**：[trailofbits/skills — plugins/agentic-actions-auditor/skills/agentic-actions-auditor](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/agentic-actions-auditor/skills/agentic-actions-auditor)；上游维护方：trailofbits 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：YAML/源码读取，远程模式可用只读 gh api；不要求运行 CI 或修改工作流。
- **联网 / 数据**：本地审阅可离线；远端模式使用每次都带同一 ref 的 GitHub API。
- **推荐原因**：覆盖 env 中介、复用 workflow、危险 sandbox、通配权限及 AI 输出再执行等特定路径。 属于新的 Agent+CI 安全交叉能力，现有 MCP 开发或一般安全规范不覆盖同样的路径。
- **采用门槛**：攻击样例中的危险命令是待检测对象，不是执行建议；报告必须保留可达条件和调用上下文。 跨文件解析有深度边界；Action 版本持续变化，不能视为覆盖所有供应商配置。{baseDir} 引用在非插件客户端需适配。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：静态追踪 GitHub Actions 中外部输入到 AI Agent 的提示词、命令和权限路径。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 跨文件解析有深度边界；Action 版本持续变化，不能视为覆盖所有供应商配置。{baseDir} 引用在非插件客户端需适配。
  - 攻击样例中的危险命令是待检测对象，不是执行建议；报告必须保留可达条件和调用上下文。

<a id="trailofbits--variant-analysis"></a>
## variant-analysis

- **分类 / 建议**：安全与质量 / 按需使用。
- **用途**：从一个已确认根因逐步泛化搜索其他实例，并保留失败模式和误报判断。
- **原始来源**：[trailofbits/skills — plugins/variant-analysis/skills/variant-analysis](https://github.com/trailofbits/skills/tree/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/plugins/variant-analysis/skills/variant-analysis)；上游维护方：trailofbits 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[CC-BY-SA-4.0](https://github.com/trailofbits/skills/blob/5c99c03fb8a9ea568432ecbcba5d86e9f4ac2bf0/LICENSE)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：Git/文本搜索可完成基本流程；可选 Semgrep/CodeQL，模板与查询资源须随 Skill 固定。
- **联网 / 数据**：基本本地检索不需网络；可选引擎按各自许可、版本与规则审查。
- **推荐原因**：要求先命中已知实例，逐步泛化，防止无基准的大范围猜测。 与现有 systematic-debugging 并列：先确认根因，再用本项找同类变体；没有证据支持替换原项。
- **采用门槛**：并行 workflow 是可选插件能力，不自动启用无限扩展或创建子代理；应限制搜索范围、迭代和输出。 不是首次漏洞发现或补丁验证；10 个查询资源仅确认存在，未审完所有语言查询语义。
- **验证范围**：E1 静态审阅；未取得可核实的功能成功记录。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：从一个已确认根因逐步泛化搜索其他实例，并保留失败模式和误报判断。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 不是首次漏洞发现或补丁验证；10 个查询资源仅确认存在，未审完所有语言查询语义。
  - 并行 workflow 是可选插件能力，不自动启用无限扩展或创建子代理；应限制搜索范围、迭代和输出。

<a id="github--agent-architecture"></a>
## agent-architecture

- **分类 / 建议**：Agent 通用能力 / 按需使用。
- **用途**：以需求、失效代价、控制边界和验证契约设计或诊断 Agent 架构。
- **原始来源**：[github/awesome-copilot — skills/agent-architecture](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/agent-architecture)；上游维护方：Stanislav Bankovskii；github/awesome-copilot 社区贡献。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`613efc8c21d9b3ce642dff361d17006cd9967e28`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[MIT](https://github.com/github/awesome-copilot/blob/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/agent-architecture/LICENSE.txt)。Skill 许可不覆盖依赖、服务、字体、数据或模型。未审计完整传递依赖许可；使用时按所选工具版本和用途另核。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：文本/代码阅读与输出；默认 PDF 和可视化需渲染工具，也允许用户明确要求只交付文本。
- **联网 / 数据**：选择具体模型/框架时检查官方资料；来源指南自包含，不需取得原教材。
- **推荐原因**：架构设计不等于实现，强调权限、预算、停止条件和证据来源分离。 与现有 mcp-builder 并列：本项先设计边界和评估，后者实现具体 MCP 服务。
- **采用门槛**：资料较多，默认报告成本偏高；不能将架构建议视作已授权实现、部署或训练。 2026-09 才加入该目录，长期有效性未知；来源综合与自定义场景不等于独立质量评测。
- **验证范围**：E1 静态审阅；E2 材料类型：upstream_evaluation_design；核对 T1–T12 等合成任务及可观察判据；仅评估设计存在，不是任务已经通过。 E3/E4 未执行；推荐建议不代表运行验证。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在明确授权的任务范围内使用：以需求、失效代价、控制边界和验证契约设计或诊断 Agent 架构。 记录未验证范围；不自动安装工具或扩大权限。
- **限制**：
  - 2026-09 才加入该目录，长期有效性未知；来源综合与自定义场景不等于独立质量评测。
  - 资料较多，默认报告成本偏高；不能将架构建议视作已授权实现、部署或训练。

<a id="iofficeai--officecli-docx"></a>
## officecli-docx

- **分类 / 建议**：办公文档 / 按需使用。
- **用途**：以 OfficeCLI 对已有 DOCX 做段落、样式、表格、页眉页脚和 OOXML 局部编辑，并进行结构与视觉复查。
- **原始来源**：[iOfficeAI/OfficeCLI — skills/officecli-docx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-docx)；上游维护方：iOfficeAI 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`fb98e593612dee2cec36847666671dba502e60aa`。Skill 以源码 Commit 固定；CLI 项目字段 1.0.157，发行标签对应关系及差异见限制。
- **许可**：[Apache-2.0](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE)。Skill 及同仓原创代码按根 Apache-2.0；NOTICE 须保留；捆绑依赖按 THIRD-PARTY-NOTICES，不能称为零依赖。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：OfficeCLI 自包含平台二进制；源码构建需 .NET 10。项目引用 Open XML SDK 3.4.1、System.CommandLine preview；目标查看器/字体另核。
- **联网 / 数据**：缺工具时 curl|bash/PowerShell 远程执行；根入口还有 load_skill 动态输出规则。
- **推荐原因**：补齐原生 Word 对象编辑；详细格式规则和已有模板优先原则有固定文本依据，CLI 源码使用 Open XML 包并区分只读/编辑路径。
- **采用门槛**：仅导航专项，不执行上游默认 setup；未来采用时选择固定发行 v1.0.157 的正确平台资产，先核对来源与已记录 digest/SHA256SUMS，使用自管完整路径；首次及每次调用都用进程级 OFFICECLI_NO_AUTO_INSTALL=1 与 OFFICECLI_SKIP_UPDATE=1，不改全局配置；不调用 install、skills install、MCP 安装或升级入口。仅设置 autoUpdate=false 不足以阻止 Skill 刷新。确认实际用户配置、日志及临时/驻留进程的写入边界，先处理副本。上述是静态采用方案，未实测。
- **验证范围**：E1：Skill、处理器与安装/更新控制静态证据；E2-success-record（CLI 构建范围）：发行提交的 GitHub Actions 记录 linux-x64、mac-arm64、win-x64 create document 步骤 success，其余平台该步骤 skipped。步骤只创建/添加/读取/关闭 DOCX，未核对版式/公式数值，不证明 XLSX/PPTX 或 Skill 端到端成功。E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在已授权的 Word 副本上修改指定段落和页眉，尽量沿用既有样式，写出新文件并说明未验证的分页差异。
- **限制**：
  - 页码、TOC、交叉引用等字段缓存可能需 Word 兼容引擎更新；不保证分页/字体与 Word 完全一致。
  - 处理器和原子写回设计是实现证据，不是原格式保留的测试通过记录。
  - 源提交版本字段为 1.0.157；发行标签 v1.0.157 指向另一提交。三个 SKILL.md、版本文件及 4 个关键控制文件逐项 blob 相同；源提交比标签多 5 个提交、11 个 Word/PPT 实现文件变化，不能说两者完整源码一致或发行二进制已覆盖这些修复。
- **底层工具候选（非配对验证）**：
  - [OfficeCLI CLI 1.0.157](https://github.com/iOfficeAI/OfficeCLI/releases/tag/v1.0.157)，Commit `b65272a18aef891941451705ff93e8a287f3eb72`；upstream_release_exists; Skill/control blobs match; full source differs by 5 commits/11 files; downloaded_binary_hash_and_function_not_verified。

<a id="iofficeai--officecli-xlsx"></a>
## officecli-xlsx

- **分类 / 建议**：办公文档 / 按需使用。
- **用途**：以 OfficeCLI 编辑 XLSX 单元格、公式、样式、工作表、图表及透视表，并核查引用和缓存值。
- **原始来源**：[iOfficeAI/OfficeCLI — skills/officecli-xlsx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-xlsx)；上游维护方：iOfficeAI 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`fb98e593612dee2cec36847666671dba502e60aa`。Skill 以源码 Commit 固定；CLI 项目字段 1.0.157，发行标签对应关系及差异见限制。
- **许可**：[Apache-2.0](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE)。Skill 及同仓原创代码按根 Apache-2.0；NOTICE 须保留；捆绑依赖按 THIRD-PARTY-NOTICES，不能称为零依赖。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：OfficeCLI 自包含二进制；不把 Excel/LibreOffice 列为所有操作的强制依赖。目标 Excel/WPS 等查看器及复杂公式复核仍需按用途准备。
- **联网 / 数据**：缺工具时执行远程安装脚本；动态规则链另需审查。
- **推荐原因**：将工作簿对象与格式维护作为独立能力，区别于 EDA；固定 Skill 含公式/样式/图表/pivot 操作和数值核查步骤。
- **采用门槛**：仅导航专项，不执行上游默认 setup；未来采用时选择固定发行 v1.0.157 的正确平台资产，先核对来源与已记录 digest/SHA256SUMS，使用自管完整路径；首次及每次调用都用进程级 OFFICECLI_NO_AUTO_INSTALL=1 与 OFFICECLI_SKIP_UPDATE=1，不改全局配置；不调用 install、skills install、MCP 安装或升级入口。仅设置 autoUpdate=false 不足以阻止 Skill 刷新。确认实际用户配置、日志及临时/驻留进程的写入边界，先处理副本。上述是静态采用方案，未实测。
- **验证范围**：E1：Skill、处理器与安装/更新控制静态证据；E2-success-record（CLI 构建范围）：发行提交的 GitHub Actions 记录 linux-x64、mac-arm64、win-x64 create document 步骤 success，其余平台该步骤 skipped。步骤只创建/添加/读取/关闭 DOCX，未核对版式/公式数值，不证明 XLSX/PPTX 或 Skill 端到端成功。E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在已授权工作簿副本上更新指定输入区，保留原样式和公式，独立核对汇总值、图表及跨表引用后交付新副本。
- **限制**：
  - 内置公式计算不能等同 Excel 全引擎；必须独立核对公式字符串和关键数值，不能只看退出码或 validate。
  - Skill 明示新公式缓存、不可变图表 series、跨表 ! 的 shell 引用陷阱及不同查看器颜色差异。
  - 透视表存在操作说明不等于所有缓存刷新、外部引用、宏或复杂模板往返已验证。
  - 源提交版本字段为 1.0.157；发行标签 v1.0.157 指向另一提交。三个 SKILL.md、版本文件及 4 个关键控制文件逐项 blob 相同；源提交比标签多 5 个提交、11 个 Word/PPT 实现文件变化，不能说两者完整源码一致或发行二进制已覆盖这些修复。
- **底层工具候选（非配对验证）**：
  - [OfficeCLI CLI 1.0.157](https://github.com/iOfficeAI/OfficeCLI/releases/tag/v1.0.157)，Commit `b65272a18aef891941451705ff93e8a287f3eb72`；upstream_release_exists; Skill/control blobs match; full source differs by 5 commits/11 files; downloaded_binary_hash_and_function_not_verified。

<a id="iofficeai--officecli-pptx"></a>
## officecli-pptx

- **分类 / 建议**：办公文档 / 按需使用。
- **用途**：以 OfficeCLI 编辑 PPTX 幻灯片、文本、形状、表格和原生图表，沿用既有主题与母版并复查布局。
- **原始来源**：[iOfficeAI/OfficeCLI — skills/officecli-pptx](https://github.com/iOfficeAI/OfficeCLI/tree/fb98e593612dee2cec36847666671dba502e60aa/skills/officecli-pptx)；上游维护方：iOfficeAI 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`fb98e593612dee2cec36847666671dba502e60aa`。Skill 以源码 Commit 固定；CLI 项目字段 1.0.157，发行标签对应关系及差异见限制。
- **许可**：[Apache-2.0](https://github.com/iOfficeAI/OfficeCLI/blob/fb98e593612dee2cec36847666671dba502e60aa/LICENSE)。Skill 及同仓原创代码按根 Apache-2.0；NOTICE 须保留；捆绑依赖按 THIRD-PARTY-NOTICES，不能称为零依赖。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：OfficeCLI 自包含二进制；视觉 QA 另需可用字体与目标查看器/截图能力。无需为本导航安装 Office、Docker 或 .NET SDK。
- **联网 / 数据**：安装和动态加载规则可能联网；非本轮允许行为。
- **推荐原因**：提供单一 CLI 对象层、定点修改和视觉 QA；与代码生成/直接 XML 编辑有不同工程成本，适合按对象修订已有演示文稿。
- **采用门槛**：仅导航专项，不执行上游默认 setup；未来采用时选择固定发行 v1.0.157 的正确平台资产，先核对来源与已记录 digest/SHA256SUMS，使用自管完整路径；首次及每次调用都用进程级 OFFICECLI_NO_AUTO_INSTALL=1 与 OFFICECLI_SKIP_UPDATE=1，不改全局配置；不调用 install、skills install、MCP 安装或升级入口。仅设置 autoUpdate=false 不足以阻止 Skill 刷新。确认实际用户配置、日志及临时/驻留进程的写入边界，先处理副本。上述是静态采用方案，未实测。
- **验证范围**：E1：Skill、处理器与安装/更新控制静态证据；E2-success-record（CLI 构建范围）：发行提交的 GitHub Actions 记录 linux-x64、mac-arm64、win-x64 create document 步骤 success，其余平台该步骤 skipped。步骤只创建/添加/读取/关闭 DOCX，未核对版式/公式数值，不证明 XLSX/PPTX 或 Skill 端到端成功。E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：在已授权 PPTX 副本中修改指定文本和数据图表，保留既有主题/母版，输出新副本并报告未验证的字体与动画。
- **限制**：
  - 模板/母版匹配是 Skill 要求，不是任意复杂模板不变的保证；字体、主题、动画及不同查看器渲染需另验。
  - 形状布局坐标由调用者负责，没有通用自动排版保证；高级编辑能力不能由 README 宣传直接认定通过。
  - 源提交版本字段为 1.0.157；发行标签 v1.0.157 指向另一提交。三个 SKILL.md、版本文件及 4 个关键控制文件逐项 blob 相同；源提交比标签多 5 个提交、11 个 Word/PPT 实现文件变化，不能说两者完整源码一致或发行二进制已覆盖这些修复。
- **底层工具候选（非配对验证）**：
  - [OfficeCLI CLI 1.0.157](https://github.com/iOfficeAI/OfficeCLI/releases/tag/v1.0.157)，Commit `b65272a18aef891941451705ff93e8a287f3eb72`；upstream_release_exists; Skill/control blobs match; full source differs by 5 commits/11 files; downloaded_binary_hash_and_function_not_verified。

<a id="vercel-labs--react-best-practices"></a>
## vercel-react-best-practices

- **分类 / 建议**：前端与设计 / 精选推荐。
- **用途**：按优先级检查 React/Next.js 数据瀑布、包体积、服务端、客户端和渲染性能模式。
- **原始来源**：[vercel-labs/agent-skills — skills/react-best-practices](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices)；上游维护方：vercel-labs 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`063bee94c3f4df8453406c830b0a7df0f2860278`。Skill metadata 1.0.0；完整 Commit 固定实际规则。
- **许可**：[MIT](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md#L4)。SKILL 本体明示 MIT，根 README 为仓库级 MIT 声明；未见两目录的冲突许可标记，但不推定第三方片段或外链内容获相同授权。未随附完整许可正文。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：指导层只需源码读取/授权编辑；React/Next.js 工具链由项目提供。贡献者 pnpm 构建及可选 npx svgo 不是阅读规则的必要步骤。
- **联网 / 数据**：固定规则阅读不强制联网；外链、可选工具和项目依赖另获授权。
- **推荐原因**：70 份具体规则及前后对照代码均在固定目录；与视觉设计、组件 API 架构各有独立任务边界，不必依赖 Vercel 部署服务。
- **采用门槛**：仅导航与原创评述；Skill frontmatter 明示 MIT，根 README 同样声明 MIT，固定目录未随附完整许可正文。不据此断言未授权第三方片段/外链内容都是 MIT，也不宣称取得逐文件权利确认。若未来获取，固定整个目标目录及必要 rules/AGENTS/metadata，按 name 值设置客户端落地目录、保留上游来源与许可声明；分发/改编前核对覆盖范围和必要版权/许可通知。无需运行贡献者构建流程。
- **验证范围**：E1：固定资源与名称/引用检查；E2-upstream_usage_example：前后对照代码可核对；没有测得性能提升或组件回归通过记录。E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：只读审查现有 React/Next.js 的数据瀑布和打包问题，按规则给出代码位置与验证计划；没有基准时不声称提速。
- **限制**：
  - 源目录 react-best-practices 与 name=vercel-react-best-practices 不一致；需客户端目录适配，未实测发现机制。
  - 76 个文件齐全，SKILL 列出的 70 份规则均存在；AGENTS.md 中 3 个 ./规则.md 相对链接有误，应直接读取同 Commit 的 rules/ 对应文件。
  - metadata 为 1.0.0，根 README/metadata 的 40+ 描述落后于实际 70；完整 Commit 才是精确版本锚点。
  - 没有测得任何性能提升；新 React API 规则和可选第三方库仅用于匹配项目版本，不自动安装依赖。

<a id="vercel-labs--composition-patterns"></a>
## vercel-composition-patterns

- **分类 / 建议**：前端与设计 / 按需使用。
- **用途**：重构布尔属性膨胀，设计组合组件、状态归属和可复用 React 组件 API。
- **原始来源**：[vercel-labs/agent-skills — skills/composition-patterns](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns)；上游维护方：vercel-labs 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`063bee94c3f4df8453406c830b0a7df0f2860278`。Skill metadata 1.0.0；完整 Commit 固定实际规则。
- **许可**：[MIT](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns/SKILL.md#L9)。SKILL 本体明示 MIT，根 README 为仓库级 MIT 声明；未见两目录的冲突许可标记，但不推定第三方片段或外链内容获相同授权。未随附完整许可正文。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：现有 React 项目和普通文件工具；无必需云服务、构建器或平台 MCP。
- **联网 / 数据**：固定规则阅读不强制联网；外链、可选工具和项目依赖另获授权。
- **推荐原因**：解决组件架构与可维护性，区别于性能规则；8 份具体规则、前后示例与编译指南全部在固定目录，可独立阅读。
- **采用门槛**：仅导航与原创评述；Skill frontmatter 明示 MIT，根 README 同样声明 MIT，固定目录未随附完整许可正文。不据此断言未授权第三方片段/外链内容都是 MIT，也不宣称取得逐文件权利确认。若未来获取，固定整个目标目录及必要 rules/AGENTS/metadata，按 name 值设置客户端落地目录、保留上游来源与许可声明；分发/改编前核对覆盖范围和必要版权/许可通知。无需运行贡献者构建流程。
- **验证范围**：E1：固定资源与名称/引用检查；E2-upstream_usage_example：前后对照代码可核对；没有测得性能提升或组件回归通过记录。E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：对布尔属性过多的 React 组件提出组合 API 方案，说明状态提升、兼容性与回归测试；先给方案再按授权改代码。
- **限制**：
  - 源目录 composition-patterns 与 name=vercel-composition-patterns 不一致；需在目标客户端适配落地名称，未实测。
  - 14 个目录文件、8 份 SKILL 所列具体规则均存在，未发现相对文件链接缺失；不是组件运行正确的测试结果。
  - React 19 特定规则不适用于 React 18 或更早版本；不要把组合模式当自动性能提升。

<a id="anthropics--docx"></a>
## docx (Anthropic)

- **分类 / 建议**：办公文档 / 受限参考导航。
- **用途**：介绍 Anthropic DOCX Skill 的 Word 创建、OOXML 编辑、批注与修订流程，帮助读者识别其能力和适用条款。
- **原始来源**：[anthropics/skills — skills/docx](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/docx)；上游维护方：anthropics 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`dbd4588f9e1033efb41dad4bef2f7947c8993d44`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Proprietary](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/docx/LICENSE.txt)。仅用于受限参考导航：目录服务合同及附加限制覆盖 Skill、代码、提示词、资产；不属于本项目 CC BY 4.0，不宣称可下载、改编、运行或再分发。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：上游流程涉及 Node/docx、Python、pandoc、LibreOffice、Poppler。预装假设来自上游运行环境；本项目不提供这些材料的提取安装方案。
- **联网 / 数据**：若补装包会联网；文档处理本身不必上传。
- **推荐原因**：有具体 DOCX 包结构、编辑及验证方法，可与 OfficeCLI 的对象级 CLI 路线并列比较；专有许可不用于降低功能质量判断。
- **采用门槛**：仅以原创简述与固定原始目录链接作受限参考导航，不复制、镜像、改编或分发 Skill、脚本、模板、资产，也不提供外部客户端安装/执行命令。许可没有明示第三方原创介绍或原始链接的条款；不将此解释为授予源码使用权。实际使用须由读者依据适用 Anthropic 服务合同及目录附加限制确认；未知合同、商业用途和环境适用性不能由本项目代为批准。本项目 CC BY 4.0 不覆盖该材料。
- **验证范围**：E1：复用固定 SKILL.md 与目录专有许可证静态证据；上游生产用途或验证陈述不作为该版本功能通过记录。没有本轮或已核实的指定场景成功结果；E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：仅介绍此原始 Skill 的 Word 批注/修订流程和许可限制，并提供原始链接；不提取或执行源材料。
- **限制**：
  - 目录许可证覆盖代码、提示词、资产和其他组件；限制服务外提取/保留、复制、改编、分发等行为。
  - 运行权利取决于读者适用的 Anthropic 服务合同；不是对所有 Claude Code、本地代理或商业场景的通用授权。
  - docx-js 不读取编辑已有文件，已有文件走 OOXML；接受段落删除、字体/分页和 Word 字段有明确限制。
  - 没有本轮功能测试或可核实的指定版本成品保真结果。

<a id="anthropics--xlsx"></a>
## xlsx (Anthropic)

- **分类 / 建议**：办公文档 / 受限参考导航。
- **用途**：介绍 Anthropic XLSX Skill 的工作簿创建、公式/格式编辑和重算核查方法及限制。
- **原始来源**：[anthropics/skills — skills/xlsx](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/xlsx)；上游维护方：anthropics 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`dbd4588f9e1033efb41dad4bef2f7947c8993d44`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Proprietary](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/xlsx/LICENSE.txt)。仅用于受限参考导航：目录服务合同及附加限制覆盖 Skill、代码、提示词、资产；不属于本项目 CC BY 4.0，不宣称可下载、改编、运行或再分发。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：上游流程涉及 Python/openpyxl/pandas/markitdown 与 LibreOffice；包/字体和服务条件另受各自条款约束。
- **联网 / 数据**：缺包时上游允许安装；本轮不安装。
- **推荐原因**：明确区分公式缓存、评估成功、结果正确和退出码；与 OfficeCLI 内置对象/公式路径有独立比较价值。
- **采用门槛**：仅以原创简述与固定原始目录链接作受限参考导航，不复制、镜像、改编或分发 Skill、脚本、模板、资产，也不提供外部客户端安装/执行命令。许可没有明示第三方原创介绍或原始链接的条款；不将此解释为授予源码使用权。实际使用须由读者依据适用 Anthropic 服务合同及目录附加限制确认；未知合同、商业用途和环境适用性不能由本项目代为批准。本项目 CC BY 4.0 不覆盖该材料。
- **验证范围**：E1：复用固定 SKILL.md 与目录专有许可证静态证据；上游生产用途或验证陈述不作为该版本功能通过记录。没有本轮或已核实的指定场景成功结果；E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：仅比较此 Skill 与 OfficeCLI 的公式缓存、重算及外链限制，链接原始说明和专有许可证，不下载或执行材料。
- **限制**：
  - 与 DOCX/PPTX 目录同样的专有服务许可及附加复制/保留/改编/分发限制；不能提供跨客户端复制安装教程。
  - LibreOffice 重算会原位改写；外部链接、动态数组、宏与不同查看器可能受影响。
  - openpyxl 的 data_only 保存可丢失公式；脚本退出 0 或无错误不证明业务数值正确。
  - 未执行重算脚本，未证明模板往返或 Excel 原生所有功能兼容。

<a id="anthropics--pptx"></a>
## pptx (Anthropic)

- **分类 / 建议**：办公文档 / 受限参考导航。
- **用途**：介绍 Anthropic PPTX Skill 的 PptxGenJS 创建、OOXML 模板编辑、缩略图及结构/视觉验证流程。
- **原始来源**：[anthropics/skills — skills/pptx](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/pptx)；上游维护方：anthropics 原始维护仓库。复用原始维护仓库证据；维护方身份不等于单项所有材料的独家作者或运行保证。
- **完整 Commit**：`dbd4588f9e1033efb41dad4bef2f7947c8993d44`。未核实 Skill 语义版本；以完整 Commit 固定。
- **许可**：[Proprietary](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/pptx/LICENSE.txt)。仅用于受限参考导航：目录服务合同及附加限制覆盖 Skill、代码、提示词、资产；不属于本项目 CC BY 4.0，不宣称可下载、改编、运行或再分发。 第三方依赖/资产/服务单独许可。未完成完整传递依赖或所有使用合同的许可审计；原始材料不复制入本项目。
- **依赖与环境**：上游流程涉及 Node/PptxGenJS、Python、LibreOffice、Poppler；不把这些库的开源许可扩大到专有 Skill。
- **联网 / 数据**：补装组件及取外部素材可能联网。
- **推荐原因**：模板解包与关系校验、程序化创建和版式检查的组合具有具体工程价值；可与 OfficeCLI 定点对象编辑并列。
- **采用门槛**：仅以原创简述与固定原始目录链接作受限参考导航，不复制、镜像、改编或分发 Skill、脚本、模板、资产，也不提供外部客户端安装/执行命令。许可没有明示第三方原创介绍或原始链接的条款；不将此解释为授予源码使用权。实际使用须由读者依据适用 Anthropic 服务合同及目录附加限制确认；未知合同、商业用途和环境适用性不能由本项目代为批准。本项目 CC BY 4.0 不覆盖该材料。
- **验证范围**：E1：复用固定 SKILL.md 与目录专有许可证静态证据；上游生产用途或验证陈述不作为该版本功能通过记录。没有本轮或已核实的指定场景成功结果；E3/E4 未执行。 `function=not_tested`；`cross_client_runtime=not_verified`。
- **使用示例**：仅介绍原始 PPTX Skill 的新建与模板编辑路径、依赖和许可边界，并提供原始链接。
- **限制**：
  - 专有许可覆盖 Skill 代码和资产，导航不授予复制、改编、商业运行或分发权；适用服务合同未知。
  - PptxGenJS 创建与已有模板的 OOXML 编辑是两条不同路径；不能以库 API 熟悉程度保证模板保真。
  - 缩略图默认命名可能覆盖其他输出，清理/重打包和脚本会改文件，合法使用时仍须使用副本。
  - 本轮未渲染、未修改任何演示文稿；未取得该固定版本跨查看器版式通过证明。

## 需要保留的来源区别


- K-Dense 的 MarkItDown 包装与 Microsoft 的底层库分别锁版本、核许可，不当成同一个作者或发行单元。
- Matplotlib Skill 的仓库许可与 Matplotlib 本身、NumPy/SciPy/cycler、字体等许可分别处理；脚本可能直接覆盖图像输出。
- OpenAI 的 pdf 与其他仓库同名实现不同。不要依据名称推断可复制性。
- skill-creator 固定版本验证脚本遗漏开放规范允许的 compatibility 字段；工具误报不能替代标准判断。相关[公开路径讨论](https://github.com/openai/skills/issues/420)也说明目录默认值需要按客户端核实。
- gh-fix-ci 的发现失败退出码语义与“脚本崩溃”不同；GitHub Actions 以外的 CI 不自动纳入范围。

新增来源还需区分：OfficeCLI 嵌入 Skill 与完整发行实现、Vercel 本体 MIT 声明与第三方引用、Anthropic 专有材料与本项目原创说明，以及 Trail of Bits CC BY-SA 与工具自己的许可。具体选择见[比较指南](comparisons.md)，权利边界见[许可说明](../LICENSE-NOTICE.md)。
