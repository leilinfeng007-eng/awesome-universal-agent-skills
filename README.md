# awesome-universal-agent-skills

高质量通用 Agent Skills 精选导航与使用指南：重视来源、固定版本、许可、依赖和可验证的能力边界。

> A curated directory of reusable Agent Skills with pinned upstream references, licensing notes, dependency guidance, and explicit validation limits. A navigation resource—not a bundled installer or a compatibility certification.

**11 项资源：精选推荐 2 项 · 按需使用 5 项 · 参考资源 4 项**  
审阅基线：2026-10-20。此日期表示审阅记录，不承诺自动追踪最新版。

本仓库只提供原创导览和结构化元数据，不分发第三方 Skill 源码，不运行安装器，也不提供网站或后台服务。推荐等级是选择建议，不能当成功能验证等级。

- **精选推荐**：优先考虑，但仍要检查自己的任务与环境。
- **按需使用**：有明确缺口且满足依赖/版本门槛时考虑。
- **参考资源**：已有等效能力时复用现有工具，不必重复安装。

“上游维护方”指公开仓库的组织/项目归属，不代表已经核实每个文件的个人作者。

## 办公文档

| Skill / 建议 | 用途 | 上游维护方 | 固定基线 | Skill 许可 | 依赖 | 推荐理由 / 限制 |
|---|---|---|---|---|---|---|
| [markitdown](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/markitdown) / 按需使用 | 将多种文档提取为 Markdown，供检索、摘要和批处理使用。 | K-Dense Inc. | [`593377bb0487`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/markitdown) | [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md) | Python >=3.10,<3.15；包装指南使用 uv；仅选择必要的转换器 extras。 | Microsoft 底层工具有发行和测试基础；适合有持续跨格式提取需求的项目。 |
| [pdf (OpenAI)](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf) / 参考资源 | 编排 PDF 生成、提取、页面渲染和视觉校对。 | OpenAI | [`49f948faa925`](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf) | [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf/LICENSE.txt) | 按任务选择 reportlab、pdfplumber、pypdf 和 Poppler；不需要每次全部安装。 | 来源与 Apache-2.0 目录许可清楚，可供缺少 PDF 能力的环境参考。 |

## 数据与图表

| Skill / 建议 | 用途 | 上游维护方 | 固定基线 | Skill 许可 | 依赖 | 推荐理由 / 限制 |
|---|---|---|---|---|---|---|
| [exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/exploratory-data-analysis) / 精选推荐 | 有界 CSV/TSV 数据画像、缺失与重复检查、异常敏感性及严格 JSON 结构检查。 | K-Dense Inc. | [`593377bb0487`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/exploratory-data-analysis) | [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md) | Python 3.11+ 标准库；可选科学格式不属于核心。 | 标准库核心依赖轻、输入输出边界明确，并有小型合成样例的结果核对记录。 |
| [matplotlib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/matplotlib) / 按需使用 | 设计静态图表、布局并导出 PNG、PDF、SVG。 | K-Dense Inc. | [`593377bb0487`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/matplotlib) | [MIT](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/LICENSE.md) | Python 3.11+；指南目标 Matplotlib 3.11.2；附带脚本还导入 NumPy、SciPy 或 cycler。 | 补充数据画像以外的图表表达能力；可以优先利用已有绘图环境。 |

## 开发工程

| Skill / 建议 | 用途 | 上游维护方 | 固定基线 | Skill 许可 | 依赖 | 推荐理由 / 限制 |
|---|---|---|---|---|---|---|
| [systematic-debugging](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging) / 精选推荐 | 以复现、日志和单一假设定位根因，再提出最小修复与验证。 | obra / Superpowers 项目 | [`bb92a7774141`](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging) | [MIT](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/LICENSE) | 文本核心无新增包；需要目标项目已有日志和验证工具。 | 可独立采用的低依赖方法；无需默认安装整套开发框架。 |
| [gh-fix-ci](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci) / 按需使用 | 读取 GitHub Actions 失败检查和日志，归纳原因并提出修复方案。 | OpenAI | [`49f948faa925`](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci) | [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/LICENSE.txt) | Python 标准库、Git、GitHub CLI（gh）和经授权的网络/仓库权限。 | 独立标准库脚本，针对 CI 排障，与通用代码审查有不同价值。 |
| [create-readme](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/create-readme) / 参考资源 | 组织项目 README 的用途、安装、用法和交付说明。 | GitHub awesome-copilot 社区贡献者 | [`613efc8c21d9`](https://github.com/github/awesome-copilot/tree/613efc8c21d9b3ce642dff361d17006cd9967e28/skills/create-readme) | [MIT](https://github.com/github/awesome-copilot/blob/613efc8c21d9b3ce642dff361d17006cd9967e28/LICENSE) | 纯文本指南；部分示例引用远端 README。 | 短小的文档结构参考；已有项目写作能力时不必增加全局入口。 |

## 自动化

| Skill / 建议 | 用途 | 上游维护方 | 固定基线 | Skill 许可 | 依赖 | 推荐理由 / 限制 |
|---|---|---|---|---|---|---|
| [playwright-cli](https://github.com/microsoft/playwright-cli/tree/b1a5903c5b633b8c9f843ad7b629c2a78437040c/skills/playwright-cli) / 按需使用 | 通过浏览器 CLI 进行页面交互、截图、日志观察和功能测试。 | Microsoft / Playwright CLI 项目 | [`b1a5903c5b63`](https://github.com/microsoft/playwright-cli/tree/b1a5903c5b633b8c9f843ad7b629c2a78437040c/skills/playwright-cli) | [Apache-2.0](https://github.com/microsoft/playwright-cli/blob/b1a5903c5b633b8c9f843ad7b629c2a78437040c/LICENSE) | Node.js 18+、配套 CLI、浏览器和相应执行权限。 | Microsoft 维护，工具与 Skill 分层清楚，可形成可重复的浏览器测试工件。 **配套 CLI 尚未核定，暂不直接安装。** |

## Agent 通用能力

| Skill / 建议 | 用途 | 上游维护方 | 固定基线 | Skill 许可 | 依赖 | 推荐理由 / 限制 |
|---|---|---|---|---|---|---|
| [mcp-builder](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder) / 按需使用 | 为明确的 API 设计 MCP 工具契约、错误处理与评估方案。 | Anthropic | [`dbd4588f9e10`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder) | [Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/LICENSE.txt) | 阅读指南无新增包；开发需选定 Python/FastMCP 或 TypeScript MCP SDK 与目标 API。 | 官方指南覆盖工具设计、结构化返回和评估；可按真实集成需求独立选用。 |
| [skill-creator (OpenAI)](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator) / 参考资源 | 设计小而专注的 SKILL.md、相对资源和按需加载结构。 | OpenAI | [`49f948faa925`](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator) | [Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/LICENSE.txt) | 阅读指南无新增包；辅助脚本需要 Python/PyYAML；Codex 界面元数据属于可选适配。 | 官方创建指南可作标准参考；已有创建器时无需再引入一套。 |
| [verification-before-completion](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion) / 参考资源 | 在完成声明前核对真实命令、结果与尚未验证范围。 | obra / Superpowers 项目 | [`bb92a7774141`](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion) | [MIT](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/LICENSE) | 纯文本核心；使用目标项目已有的验证工具。 | 原则值得复用；已有验证约束时应避免重复门禁和上下文负担。 |

## 验证状态

- 11 项均完成已述范围的静态审阅和基础 Frontmatter 检查；不代表资源、依赖或运行行为全部通过。
- EDA 标准库核心有维护者记录的 **16 次本地调用、41 项合成样例核对**；大文件、可选格式和完整上游测试未验证。
- 其余条目的功能运行未验证；**所有条目的跨客户端端到端运行均未验证**。目录规范支持不等于结果正确。
- Playwright 的已审 Skill 与候选 CLI 发行版不同；MarkItDown、Matplotlib、MCP 等仍有依赖/许可门槛。没有“全部安装即可稳定运行”的承诺。

## 使用与维护

1. 先查[逐项版本、依赖与限制](docs/skills.md)，选择真正需要的单项。
2. 按[获取、安装与回滚指南](docs/installation.md)使用固定上游 Commit，不复制整个合集，不覆盖已有同名条目。
3. 对照[客户端机制说明](docs/clients.md)准备资源和工具；无需为使用目录安装所有客户端。
4. 新增条目遵循[选择与维护规则](docs/selection-policy.md)，结构化数据见[catalog.json](catalog.json)与[数据结构](catalog.schema.json)。

另见[验证记录范围](docs/validation.md)和[贡献说明](CONTRIBUTING.md)。本目录优先[Agent Skills 开放规范](https://agentskills.io/specification)，不绑定某个管理器。

## 许可证

本仓库原创导览文字、说明文档及受保护的编辑表达采用 **CC BY 4.0**，见 [LICENSE](LICENSE) 与[许可范围说明](LICENSE-NOTICE.md)。转载或改编时请按许可要求署名、附来源与许可链接，并说明修改。

每个第三方 Skill、依赖、资产及服务分别受自己的许可或条款约束。本仓库的文档许可证不覆盖这些内容，也不暗示原作者为本项目背书。未来可执行代码须另行明确代码许可证。
