# 水镜适配说明

`eia-research/SKILL.md` 是按水镜当前受限仓库 Skill 格式写的只读流程。它依赖地图助手已声明的 `research.search`，只指导政府网站检索与证据表达，不增加工具权限。水镜加载器不会递归读取公开版的 `references/wiki/`，因此这份适配版不能宣称已使用来源 Wiki，也不能把搜索摘要称为已读 PDF 原文。

接入目标部署时，需由水镜维护者将此文件纳入 `apps/server/agent_runtime/skills/eia-research/SKILL.md`，并在地图助手的前后端技能白名单与卡片中登记 `eia-research`。随后按部署流程发布，在已登录页面确认 `/api/agent/capabilities` 出现可用技能，再实际提问并核对 `research.search` 的回执、来源链接和回答中的状态说明。单独复制文件或只看见技能卡片都不代表已执行。

公开仓库只提供适配材料；截至 2026-11-24，已用水镜当前解析器和选择器完成本地格式核验，尚未在目标部署安装或做浏览器实测。
