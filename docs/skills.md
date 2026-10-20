# 精选条目详情

本页与 catalog.json 一一对应。Commit 是固定审阅基线，不是“最佳稳定版”认证。上游组织、发行基础、示例和测试目录只是证据的一部分；未运行的功能仍标未验证。

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

## 需要保留的来源区别

- K-Dense 的 MarkItDown 包装与 Microsoft 的底层库分别锁版本、核许可，不当成同一个作者或发行单元。
- Matplotlib Skill 的仓库许可与 Matplotlib 本身、NumPy/SciPy/cycler、字体等许可分别处理；脚本可能直接覆盖图像输出。
- OpenAI 的 pdf 与其他仓库同名实现不同。不要依据名称推断可复制性。
- skill-creator 固定版本验证脚本遗漏开放规范允许的 compatibility 字段；工具误报不能替代标准判断。相关[公开路径讨论](https://github.com/openai/skills/issues/420)也说明目录默认值需要按客户端核实。
- gh-fix-ci 的发现失败退出码语义与“脚本崩溃”不同；GitHub Actions 以外的 CI 不自动纳入范围。
