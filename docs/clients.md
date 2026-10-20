# 不同 AI 客户端的获取与使用

以下是已审官方机制与通用适配条件，**不是已验证的跨客户端运行矩阵**。目录支持、正文加载、资源可见、脚本执行、结果正确是不同层次。

| 客户端 | 可参考的入口/获取方式 | 使用条件与限制 | 机制状态 / 官方来源 |
|---|---|---|---|
| Codex App / CLI | 项目 `.agents/skills/<name>/SKILL.md` | App 与 CLI 工具环境不同；Python、shell、渲染工具与资源必须可见 | 官方机制支持；功能未验证。[说明](https://learn.chatgpt.com/docs/build-skills) |
| Cursor 本地 | 按支持版本使用 `.agents/skills` 或 `.cursor/skills` | 云端/远程工作区不推断自动同步 | 官方机制支持；功能未验证。[说明](https://cursor.com/help/customization/skills) |
| OpenCode | 项目 `.agents/skills` 及其原生/兼容目录 | skill 读取权限、命令权限、Provider 可用性各自独立 | 官方机制支持；功能未验证。[说明](https://opencode.ai/docs/skills) |
| Claude Code | 项目 `.claude/skills/<name>/SKILL.md` | 保留相对资源，按当前环境映射执行工具 | 官方机制支持；功能未验证。[说明](https://code.claude.com/docs/en/skills) |
| DeepSeek Harness | 文件系统 Provider 的 `.agents/skills` / `.dsh/skills` | 需启用对应 Provider 并核对优先级与资源 base；基础模型本身不扫描文件 | 需要 Provider 适配；未验证。[机制基线](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/docs/subsystems/skills.md) |
| WorkBuddy | 依产品文档上传/导入固定单项 | 受控副本优先；不假设与其他同名 CLI 目标等价或实时同步 | 需要导入适配；未验证。[说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) |
| Qoder IDE / CLI | 按产品及版本确认项目目录 | 区域版本与 QoderWork 不是同一目录机制 | 需要版本适配；未验证。[说明](https://docs.qoder.com/extensions/skills) |
| QoderWork | 按官方流程独立导入固定快照 | 客户端可能保存启用状态；不要把可写导入当作共享权威源码 | 需要导入适配；未验证。[说明](https://docs.qoder.com/qoderwork/skills) |

这些机制按审阅基线记录，客户端后续版本可能改变。其他支持 Agent Skills 的客户端，在确认发现目录、资源定位、工具与权限前标为未验证。

## 按能力准备工具

- EDA：Python 3.11+、普通真实输入文件和受限 root；Skill 目录链接与输入数据链接的限制不是一回事。
- Debugging / README / 验证原则：按项目已有工具工作；文本指令不能扩大授权或保证模型遵守。
- PDF / 图表：相应库、渲染/图像查看工具、字体和新输出目录；数据可读不等于版式正确。
- GitHub CI：经授权的 gh / Git 与网络；不为了采用资源自动登录或改变权限。
- MCP：所选 SDK、目标 API 与明确权限；指南不提供现成连接器。
- Playwright：先确定配套版本、浏览器和临时会话策略，再决定采用。

## 不强制统一目录

原生支持的项目可以复用同一固定核心；需要导入或可能改写内容的客户端使用受控副本。不要让多个客户端各自编辑上游权威源码，也不要未经检查覆盖已有入口。无需为这份目录安装所有客户端或调整登录、代理、证书与全局配置。
