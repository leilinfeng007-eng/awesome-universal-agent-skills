# 同类 Skill 的选择指南

先按任务、环境、许可和证据选择，不给不同技术路线强行排名。并列表示互补，不表示同级或均已运行成功。所有固定来源、依赖和限制以[条目详情](skills.md)与 [catalog.json](../catalog.json)为准。

<a id="office"></a>
## Office：专项采用与受限参考并列

OfficeCLI 三项是有条件的专项导航；Anthropic Office 三项只是原创介绍和原链参考，**本项目不提供服务外提取、安装、执行或再分发路线**。专有许可不降低对方法价值的评价，也不因导航收录而改变权利。

### Word

| 维度 | [OfficeCLI DOCX](skills.md#iofficeai--officecli-docx) | [Anthropic DOCX](skills.md#anthropics--docx) |
|---|---|---|
| 擅长什么 | 用统一 CLI 对段落、样式、表格、节、页眉页脚和字段做定点编辑 | 介绍程序化新建、已有 OOXML 编辑、批注和修订的专门处理方法 |
| 实现/环境 | 自包含 .NET CLI、Open XML SDK；视觉复查需字体/查看器 | 上游涉及 Node/docx、Python、pandoc、LibreOffice、Poppler；预装假设属于上游环境 |
| 何时优先 A | 需要对已有文档对象修改，能满足固定版本与副作用控制 | — |
| 何时参考 B | — | 需要了解批注/修订和包结构处理方法及其限制；实际使用须确认服务合同 |
| 已有格式/限制 | 要求遵循模板；Word 字段缓存、分页/字体和原子写回设计不等于无损往返证明 | 有接受修订、段落删除等边界；程序生成和已有文件编辑不是同一路径 |
| 许可/证据 | Apache-2.0 与 NOTICE/依赖条款；只有有界 CLI CI 记录，未实测完整 Skill | 专有条款及读者服务合同；无本目录确认的指定场景成功结果 |

没有同一文档与目标查看器的对照结果，不宣称任何一方一定更保真。

### Excel

| 维度 | [OfficeCLI XLSX](skills.md#iofficeai--officecli-xlsx) | [Anthropic XLSX](skills.md#anthropics--xlsx) |
|---|---|---|
| 擅长什么 | 工作簿对象、公式、样式、图表、命名范围、透视表等 CLI 操作 | 介绍库编辑、公式缓存、重算与数值检查规则 |
| 实现/环境 | OfficeCLI 的对象/公式路径；不能等同 Excel 全引擎 | 上游涉及 openpyxl/pandas/markitdown 与 LibreOffice 重算 |
| 何时优先 A | 希望用统一 CLI 更新原生对象，能独立检查汇总和引用 | — |
| 何时参考 B | — | 需要比较库保存/重算的边界与 QA 方法；实际使用资格独立确认 |
| 已有格式/限制 | 新公式缓存、图表 series 修改、跨表 shell 引用、pivot/外链须逐项验证 | data_only 保存可能丢公式，重算会改写；宏、外链与动态数组受限 |
| 许可/证据 | Apache-2.0；没有本目录 XLSX 结果，DOCX smoke 不可迁移成 Excel 通过 | 专有条款；不以脚本退出 0、无公式错误推断数值正确 |

两条路线都需要真实值核对；不能把 EDA 当原生 Excel 编辑，也不能凭库支持范围声称 Skill 已完成所有功能。

### PowerPoint

| 维度 | [OfficeCLI PPTX](skills.md#iofficeai--officecli-pptx) | [Anthropic PPTX](skills.md#anthropics--pptx) |
|---|---|---|
| 擅长什么 | 幻灯片、形状、文本、图表的对象编辑和现有主题/母版修订 | 介绍程序化创建、模板包编辑及结构/视觉校验方法 |
| 实现/环境 | OfficeCLI 自包含二进制，视觉检查另需字体/查看器 | 上游涉及 Node/PptxGenJS、Python、LibreOffice、Poppler |
| 何时优先 A | 对已有演示文稿定点修订并希望使用统一对象 CLI | — |
| 何时参考 B | — | 需要了解程序化生成与模板包校验的差异；不据导航提取源材料 |
| 版式/限制 | 坐标由调用者负责，复杂母版、字体、动画和查看器保真未知 | 模板关系、默认输出命名、清理/重打包均有风险，未验证模板保真 |
| 许可/证据 | Apache-2.0；源码/发行实现有差异，没有 PPTX 功能通过结果 | 专有条款；不镜像脚本/模板/资产，没有本目录渲染通过记录 |

### OfficeCLI 的版本与采用门槛

已审 Skill 源 Commit `fb98e593612dee2cec36847666671dba502e60aa` 的版本字段为 1.0.157；[v1.0.157 发行](https://github.com/iOfficeAI/OfficeCLI/releases/tag/v1.0.157)指向 `b65272a18aef891941451705ff93e8a287f3eb72`。三个 Skill、版本和关键安装/更新控制 blob 相同，但[完整差异](https://github.com/iOfficeAI/OfficeCLI/compare/b65272a18aef891941451705ff93e8a287f3eb72...fb98e593612dee2cec36847666671dba502e60aa)还有 5 个提交、11 个 Word/PPT 实现文件。不能写完整一致或配对已通过。

采用须固定资产、核实际哈希、禁自动安装/更新/刷新并保护副本、日志和驻留进程；[采用指南](installation.md#officecli)只作条件性说明，不自动执行。CLI 构建 smoke 的具体成功/跳过范围见[验证说明](validation.md)，不是三项 Skill 的通用成功记录。

<a id="react"></a>
## React 性能与组件架构

| 维度 | [React Best Practices](skills.md#vercel-labs--react-best-practices) | [Composition Patterns](skills.md#vercel-labs--composition-patterns) |
|---|---|---|
| 擅长什么 | 数据瀑布、包加载、服务端/客户端取数和重渲染模式 | 布尔属性膨胀、组合组件、上下文接口与状态归属 |
| 优先场景 | 性能问题、加载路径和包体积审查 | 组件 API、复用与状态管理复杂，需要重构方案 |
| 环境/依赖 | 现有 React/Next.js 项目；可选规则库和 API 匹配项目版本 | 现有 React 项目；React 19 章节不适用于旧版 |
| 固定资源 | 同一 Commit 内 76 文件、70 份具体规则，列出的规则均存在 | 同一 Commit 内 14 文件、8 份具体规则，列出的规则均存在 |
| 目录适配 | 源 react-best-practices，name 为 vercel-react-best-practices | 源 composition-patterns，name 为 vercel-composition-patterns |
| 许可/证据 | 本体和根 README 声明 MIT；无随附全文；只有示例/配置，未测提速 | 同样许可边界；只有组件示例，未运行编译或回归 |

两项值得同时收录：性能优化不等同组件架构；与 frontend-design 的视觉方向也互补，不需要强行二选一。无需安装 Vercel 服务或执行贡献者 pnpm 构建来阅读固定指南。

本体/仓库级 MIT 声明不自动证明第三方片段、外链或文档获重新授权；分发前核对覆盖与通知。本项目不复制规则库。固定源缺完整 LICENSE 文本，不将它误写成无许可；也不把全部资源的作者权利当成已逐件确认。

React 汇总 AGENTS 中三处 `./规则.md` 跳转有误，规则本身存在，可直接使用固定原始文件：

- [async-defer-await](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/rules/async-defer-await.md)
- [async-cheap-condition-before-await](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/rules/async-cheap-condition-before-await.md)
- [server-hoist-static-io](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/rules/server-hoist-static-io.md)

不修改上游，且不将两项混同于必须获取远端浮动规则的其他入口。metadata 1.0.0 与完整 Commit 的作用不同；没有客户端发现或性能提升实测。

## 数据分析与实验载体

| | [EDA](skills.md#k-dense-ai--exploratory-data-analysis) | [Jupyter Notebook](skills.md#openai--jupyter-notebook) |
|---|---|---|
| 擅长/优先任务 | 对已有 CSV/TSV 等做有界画像、缺失和重复检查 | 将实验/教程组织为可阅读、可重跑 notebook |
| 环境与选择 | 已述标准库核心，重点在真实数据值核对 | 标准库脚手架与执行内核/项目依赖分开；路径需适配 |
| 许可/证据边界 | MIT；已有有限 16 次调用/41 项核对，不认证全部格式 | Apache-2.0；未运行脚手架/内核，不能执行不可信单元 |

获取分析结果优先 EDA，组织实验载体优先 Notebook；可以组合，后者不替代前者的数值检查。

## 排障、安全变更与根因变体

| 选择 | 最适合的问题 | 环境和限制 |
|---|---|---|
| [Systematic Debugging](skills.md#obra--systematic-debugging) | 已有可复现故障，需要日志、单一假设和根因 | MIT；项目验证工具，附带脚本可能执行测试；行为未验证 |
| [Differential Review](skills.md#trailofbits--differential-review) | 有提交/diff 基线，需要判断安全影响、历史回归和波及范围 | CC BY-SA 4.0；需 Git/历史/源码；可选插件不假定存在 |
| [Variant Analysis](skills.md#trailofbits--variant-analysis) | 根因已确认，追问还有哪些同类实例 | CC BY-SA 4.0；文本搜索可起步，查询引擎另核；不是首次发现 |

故障调查选 Debugging，变更安全审查选 Differential Review，已知根因扩展搜索选 Variant Analysis。三者可衔接，均不能借审查自动修改项目、扩大权限或声称全覆盖。

## MCP 实现与 Agent 架构

| | [MCP Builder](skills.md#anthropics--mcp-builder) | [Agent Architecture](skills.md#github--agent-architecture) |
|---|---|---|
| 优先任务 | 明确 API 的工具契约、错误处理与评估，再按授权实施服务 | 澄清需求、失败代价、权限/预算、停止条件和验证契约 |
| 环境 | 选定 Python/TypeScript SDK 与目标 API，不默认安装整套服务 | 文本/源码与报告工具；PDF/图形交付有成本，可按用户约束简化 |
| 许可/验证 | Apache-2.0；SDK/API 独立，示例浮动引用需核实，运行未验证 | MIT 社区条目；合成评估设计不是通过记录，架构不等于部署授权 |

需要先决定边界和方案时选架构指南；需要构建具体 MCP 接口时选实现指南。两者并列，工具/模型选择与实际效果仍须在项目中验证。
