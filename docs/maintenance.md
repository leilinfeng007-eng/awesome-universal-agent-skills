# 小目录，轻维护

[← 回到首页](../README.md) · [贡献方法](../CONTRIBUTING.md)

## 一个数据源，三种阅读方式

`catalog.json` 是当前 20 项的权威记录。用户层字段（用途、任务、准备条件、同类选择）与固定来源/原证据放在同一个条目中，不重新抄多份事实。

原创标准库脚本 `tools/build.py` 生成 README、`skills/*.md` 和独立 `index.html`。后者的模板是 `tools/directory.html`，数据与资源均内嵌，下载后双击可用，不需要 npm、构建框架、数据库、账号或服务器。不发请求、不加载字体/CDN，不追踪搜索词。GitHub 分支预览以 Markdown 为主；没有启用 Pages。

```sh
python3 tools/build.py
python3 tools/build.py --check
python3 -m unittest discover -s tests -v
```

这些命令只检查和生成本目录的自有内容，不下载或运行任何第三方 Skill。生成器不会改动历史区。

## 选择与变化

- 看是否能解决具体问题、有独立价值、资源与来源明确；不以 Stars 或收录数量排名。
- “优先了解 / 专项选择”描述选择成本与场景，不是运行质量认证。
- 新增/替换必须讲清“为什么不是现有那一项”。功能不同可并列。
- 暂停推荐时保留简短原因和固定记录，避免把“缺少证据”写成“确定失败”。
- 本轮从原 32 项中保留 20 项当前入口，另 12 项转为历史参考；没有加入凑数的新候选。

[历史调整清单](../archive/README.md)。只有 EDA 有历史有限核心样例；所有条目跨客户端运行均未验证。保留原证据，不把重构页面当成运行验收。

## 借鉴了什么

- [skills.sh](https://www.skills.sh/)：先搜索，再在详情集中呈现用途、来源和下一步；不借用热度当质量证明。
- [Awesome Copilot](https://awesome-copilot.github.com/skills/)：列表负责查找，详情负责行动；共享数据生成不同展示，避免手工维护两套目录。
- [Anthropic Skills](https://github.com/anthropics/skills)：将任务示例紧挨使用说明；不把其客户端例子泛化到所有平台。
- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md)：精选要说明独特价值，不做穷尽清单。
- [VoltAgent](https://github.com/VoltAgent/awesome-agent-skills)：短描述和工具入口可快速扫描；不照搬大型合集结构。

没有复制这些项目的界面代码、图标或 Skill 源码。当前设计选择 GitHub 原生首页与单项卡片为基础；离线页只补真正有用的搜索/筛选，不让网站部署成为使用前提。

## 当前还没有完成的事

没有新增 Skill 功能测试或客户端运行验收；导入型客户端资源保留、符号链接、完整环境配置仍须单独验证。OfficeCLI 和 CodeQL 是专项准备路线，不承诺零基础即用。浏览器自动化仍缺少可复现固定组合，暂不填充低证据替代品。

静态页不是在线市场，不能替你判断本机已有依赖、客户端登录或权限；它不会自动添加 Skill。后续如确有必要，可以沿用相同数据部署静态页，但不需要先建设后台。

## 本轮页面检查

8 项本地目录检查通过：固定来源/许可/证据未改写、目录唯一性、无效记录拒绝、生成漂移、当前内部链接、单页流程完整、GitHub 表格结构和离线页嵌入安全。真实浏览器已核对桌面版 Excel 搜索、常用筛选、Kimi 路径展开、复制实际文本、空结果提示与详情链接。手机视口覆盖未在当前预览环境生效，因此不宣称手机端完成实测；样式已包含窄屏布局。上述只验证本库界面与内容，不是第三方 Skill 功能测试。
