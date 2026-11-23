# EIA Research Skill | 环评资料检索

一个可复用的 `SKILL.md`，帮助 Agent 从主管部门原文追溯环评政策、标准、审批文件、同类报告、行业数据和生产工艺资料。附带按主题整理的官网入口和逐份文件链接台账。

资料库是检索起点，不是自动更新的法规库，也不替代对原文、附件、适用地区和现行效力的核验。截至 2026-11-23，包含 14 个主题、31 个来源入口和 14 条文件记录；`full_text_reviewed: false` 表示尚未核对全文。

## 安装到 Codex

```bash
git clone https://github.com/ziren926/eia-research-skill.git
mkdir -p ~/.codex/skills
cp -R eia-research-skill/skills/eia-research ~/.codex/skills/
```

重开 Codex 对话后，可直接提问：

> 用 eia-research 查水泥熟料生产工艺，列出权威来源、典型流程、主要产污环节，并标明哪些是已核原文、哪些只是待核线索。

若已有同名目录，请先比对本地修改，再更新目录。Codex 的技能安装路径也可参考其内置 `skill-installer`。

Claude Code 的个人技能目录是 `~/.claude/skills/`，项目技能目录是 `.claude/skills/`；把同一个 `eia-research` 目录放入其中即可。WorkBuddy 使用 `SKILL.md` 和 `references/` 结构，可按[官方 Skill 文档](https://open.workbuddy.cn/docs/skill)打包导入。水镜平台需由对应部署加载该目录。这里提供的是可移植文件格式，不表示四个平台的运行环境已全部实测或上架。

## 代码怎么读

入口在 [`skills/eia-research/SKILL.md`](skills/eia-research/SKILL.md)：它告诉 Agent 先限定地区、行业、工艺和时间，再从官网找原文，最后把适用性和核实状态说清楚。`references/wiki/catalog.json` 把主题映射到来源；`references/wiki/documents.json` 记录具体原文页、附件和核对状态；`references/wiki/README.md` 是人工可读的索引。

```text
用户问题 -> SKILL.md 判断检索范围 -> catalog.json 选官网
         -> documents.json 找已有线索 -> 联网核原文/附件 -> 带状态回答
```

这个仓库没有爬虫、定时同步、全文索引或自动判断法规效力的能力。每次要求“现行”“最新”或具体项目适用性，都必须重新查原发文机关和当地要求。

## 一起维护

欢迎通过 Issue 提出失效链接、错漏和新行业需求，通过 Pull Request 补充可追溯的官方原文。新增记录前请阅读 [贡献指南](CONTRIBUTING.md)，运行 `python3 scripts/validate_wiki.py`。许可证见 [MIT License](LICENSE)。
