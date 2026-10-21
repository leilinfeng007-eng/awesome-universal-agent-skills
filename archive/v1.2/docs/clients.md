# 不同 AI 客户端的获取与使用

先用[客户端选择表](client-guides.md#platform-picker)找到你正在使用的具体产品，再走对应步骤。本页汇总目录和迁移边界，不按模型品牌判定 Skill 是否通用。

以下是已审官方机制与通用适配条件，**不是已验证的跨客户端运行矩阵**。目录支持、正文加载、资源可见、脚本执行、结果正确是不同层次。

| 客户端 | 可参考的入口/获取方式 | 使用条件与限制 | 机制状态 / 官方来源 |
|---|---|---|---|
| Codex App / CLI | 项目 `.agents/skills/<name>/SKILL.md` | App 与 CLI 工具环境不同；Python、shell、渲染工具与资源必须可见 | 官方机制支持；功能未验证。[说明](https://learn.chatgpt.com/docs/build-skills) |
| Cursor 本地 | 按支持版本使用 `.agents/skills` 或 `.cursor/skills` | 云端/远程工作区不推断自动同步 | 官方机制支持；功能未验证。[说明](https://cursor.com/help/customization/skills) |
| OpenCode | 项目 `.agents/skills` 及其原生/兼容目录 | skill 读取权限、命令权限、Provider 可用性各自独立 | 官方机制支持；功能未验证。[说明](https://opencode.ai/docs/skills) |
| Kimi Code CLI / Desktop（现行） | Git 项目 `.agents/skills` / `.kimi-code/skills`；用户默认 `~/.agents/skills` / `~/.kimi-code/skills` | `/skill:名称`；项目根有 `.git` 条件，不套用旧 kimi-cli 路径 | 官方机制支持；具体 Skill 未验证。[CLI](https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html) / [Desktop](https://www.kimi.com/code/docs/kimi-code-desktop/settings-and-extensions.html) / [步骤](client-guides.md#kimi-code) |
| Kimi 网页 Agent | 独立技能面板 | 未确认本库 GitHub Skill 的完整网页导入路径；不使用本机 CLI 目录 | 有技能机制，本库导入未确认。[官方说明](https://www.kimi.com/help/plugins-and-skills/use-skills-in-agent) |
| Claude Code | 项目 `.claude/skills/<name>/SKILL.md` | 保留相对资源，按当前环境映射执行工具 | 官方机制支持；功能未验证。[说明](https://code.claude.com/docs/en/skills) |
| DeepSeek Harness | 文件系统 Provider 的 `.agents/skills` / `.dsh/skills` | 需启用对应 Provider 并核对优先级与资源 base；基础模型本身不扫描文件 | 需要 Provider 适配；未验证。[机制基线](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/docs/subsystems/skills.md) |
| WorkBuddy（腾讯桌面） | 技能面板上传单项包 | 手工目录、包层级/冲突机制未确认；不是 CodeBuddy CLI | 官方支持导入，打包适配待确认；未运行。[说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) / [步骤](client-guides.md#workbuddy) |
| Qoder IDE / CLI | 项目 `.qoder/skills`，用户 `~/.qoder/skills` | IDE 重启后 `/`；CLI `/skills`、`/skills reload`；两份文档同名优先级不同 | 官方机制支持；未运行。[IDE](https://docs.qoder.com/extensions/skills) / [CLI](https://docs.qoder.com/cli/Skills) / [步骤](client-guides.md#qoder) |
| QoderWork | 扩展 → 技能 → 安装技能；独立 `.qoderwork/skills` | 不能假设与 IDE、Codex 共享目录；同名与改写行为待验证 | 官方支持导入；未运行。[说明](https://docs.qoder.com/zh/qoderwork/skills) / [步骤](client-guides.md#qoderwork) |
| 新 Qoder 桌面 | Extensions → Skills → Add Skills → Upload Skill | 与 Qoder IDE、CLI、Work 分开确认版本与入口 | 官方支持上传；本库未运行。[说明](https://docs.qoder.com/qoder/skills) |

这些机制按审阅基线记录，客户端后续版本可能改变。其他支持 Agent Skills 的客户端，在确认发现目录、资源定位、工具与权限前标为未验证。

## 导航收录与客户端入口分开

目录现含 32 项；没有因此安装、启动或实测任一客户端。新增 21 项的功能状态仍是 not_tested，跨客户端仍是 not_verified。

**先检查 catalog 的 navigation_scope。** Anthropic DOCX/XLSX/PPTX 标为 restricted_reference，只供原创介绍、原始链接和许可查询；以下普通入口建议不适用于它们，不提供向任何第三方客户端提取、导入或运行的路线。服务合同与专有条款不能因客户端支持 SKILL.md 而跳过。

其他条目即使格式可读，也可能需要 CODEX_HOME 路径、{baseDir}、MCP 工具名、命名子代理或任务工具的映射。共享目录不等于共享运行环境；可选插件能力不假定已安装。

## 按能力准备工具

- EDA：Python 3.11+、普通真实输入文件和受限 root；Skill 目录链接与输入数据链接的限制不是一回事。
- Debugging / README / 验证原则：按项目已有工具工作；文本指令不能扩大授权或保证模型遵守。
- PDF / 图表：相应库、渲染/图像查看工具、字体和新输出目录；数据可读不等于版式正确。
- GitHub CI：经授权的 gh / Git 与网络；不为了采用资源自动登录或改变权限。
- MCP：所选 SDK、目标 API 与明确权限；指南不提供现成连接器。
- Playwright：先确定配套版本、浏览器和临时会话策略，再决定采用。
- OfficeCLI：只在另获采用授权后考虑固定二进制与独立资源，禁止自动安装、升级或刷新客户端入口；双禁用开关及版本差异见[采用条件](installation.md#officecli)。本目录没有核验实际客户端与 CLI 配对。
- React 两项：源目录与 name 不同，可在未来落地目录使用 vercel-react-best-practices / vercel-composition-patterns，保留固定来源元数据，不改上游 SKILL.md。规则在同一 Commit 内；此建议不代表发现测试已通过。
- 安全审阅：一般指南可用文件工具；CodeQL 构建、Git 历史、只读 gh 和远程依赖查询有各自权限。供应链审计会披露包名/版本，不对保密依赖直接联网。
- 数据与研究：Notebook 生成和执行内核不同；Gradio 可启动服务，不能默认公开分享；论文读取与修改作者/索引等写端点分开授权。
- Agent Architecture：交付设计而非实施系统；默认 PDF/图形需要渲染能力，可按用户约束只交付文本，不把报告授权扩成部署权限。

## 不强制统一目录

原生支持的项目可以复用同一固定核心；需要导入或可能改写内容的客户端使用受控副本。不要让多个客户端各自编辑上游权威源码，也不要未经检查覆盖已有入口。无需为这份目录安装所有客户端或调整登录、代理、证书与全局配置。

不同客户端的安装或导入操作都需独立选择；受限参考不参与此共享方案。理论条件只能写“理论兼容”或“需要适配”，未运行就保留“未验证”。
