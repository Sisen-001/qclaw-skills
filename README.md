# QClaw Skills Pack

> 开源 OpenClaw Agent 技能包集合 | 开箱即用 | MIT License

本仓库包含鸿钿团队沉淀的 **49 个 OpenClaw AI Agent 技能**，按职能分为五大类，即刻为你的 AI 助手赋能。

---

## 📁 目录结构

```
qclaw-skills/
├── finance/        金融投资技能（A 股操盘 / 数据分析 / 监控预警）
├── content/         内容创作技能（封面设计 / 排版 / 视频生成 / 小红书运营）
├── growth/          增长外贸技能（市场调研 / 独立站 / 邮件开发 / Shopify）
├── productivity/     效率工具技能（自我进化 / 日程管理 / 知识库）
└── utilities/       通用工具技能（搜索 / OCR / Excel / PDF / 邮件）
```

---

## 🚀 快速安装

### 单个技能安装

```bash
# 方法1: 使用 openclaw CLI
openclaw skills install <skill-name>

# 方法2: 手动安装
cp -r <skill-folder> ~/.qclaw/workspace/skills/
```

### 批量导入（Git Submodule）

```bash
git submodule add https://github.com/<your-username>/qclaw-skills.git _skills
ln -sf _skills/finance/* ~/.qclaw/workspace/skills/
ln -sf _skills/content/* ~/.qclaw/workspace/skills/
ln -sf _skills/growth/* ~/.qclaw/workspace/skills/
ln -sf _skills/productivity/* ~/.qclaw/workspace/skills/
ln -sf _skills/utilities/* ~/.qclaw/workspace/skills/
```

---

## 📦 技能总览

### 💰 Finance（7 个技能）

| 技能 | 功能 | 数据源 |
|------|------|--------|
| `china-stock-analysis` | A 股/港股价量分析、均线、技术指标、买卖信号 | 东方财富 + 腾讯财经 |
| `astock-data` | 1/5/15/30/60 分钟 K 线、实时股价、分时数据 | QGData API |
| `stock-analysis` | 美股/加密货币行情追踪 | Yahoo Finance |
| `earnings-tracker` | AI 财报追踪器，自动扫描 A 股/美股财报日历 | 财报日历 |
| `macro-monitor` | 宏观政策监控 | RSS/新闻聚合 |
| `trading-coach` | 超短线交易训练指导 | 规则引擎 |
| `stock-monitor-skill` | 7 大预警规则（止损/止盈/均线/RSI/成交量/跳空/动态止盈）| 东方财富 |

**财姐底线（内置）：** 止损 -3% · 止盈 +5% · 超短线次日 10:30 前出 · 单票仓位 ≤15%

---

### 🎨 Content（10 个技能）

| 技能 | 功能 | 输出 |
|------|------|------|
| `canvas-design-pro` | AI 绘本封面/海报/信息图设计（波波 IP + 凯迪克风格）| PNG/PDF |
| `canvas-design` | 通用视觉艺术设计 | PNG/PDF |
| `frontend-design-ultimate` | 高审美响应式排版（shadcn/ui + React）| HTML/CSS |
| `humanizer-zh-pro` | 中文文案去 AI 味，专业资金人口吻改写 | 文本 |
| `content-strategy` | 内容营销策略（选题/分发/日历/复盘）| 策略文档 |
| `video-generator` | AI 视频生成（Runway/Pika/Kling/Veo）| MP4 |
| `xiaohongshu-writer-expert` | 小红书爆款文案写作专家 | 笔记文案 |
| `xiaohongshu-analyzer` | 小红书账号/内容/竞品分析 | 分析报告 |
| `xiaohongshu-image-auto` | 小红书封面图自动生成 | 图片 |
| `youtube-thumbnail-design` | YouTube 封面设计 | 缩略图 |

---

### 📈 Growth（6 个技能）

| 技能 | 功能 | 场景 |
|------|------|------|
| `market-research-agent` | 竞品调研/选品/市场分析/海关数据 | 选品决策 |
| `export-business-assistant` | 外贸全能助手（开发信/报价/合同/物流/报关）| 外贸全流程 |
| `shopify-expert` | Shopify 独立站搭建与运营 | 电商独立站 |
| `foreign-trade-email-writer` | 外贸英文开发信撰写（行业模板）| 客户开发 |
| `foreign-trade-email-sorter` | 外贸邮件分类与回复建议 | 客户管理 |
| `foreign-trade-customers-example` | 外贸客户激活系统（超 5 天未回复自动跟进）| 客户激活 |

---

### ⚡ Productivity（9 个技能）

| 技能 | 功能 |
|------|------|
| `self-improving` | 自我进化（错误记录/持续改进/GEPA 框架）|
| `proactivity` | 主动预判与持续跟进，不被动等待 |
| `tianyi-self-upgrade` | 系统自检/预防修复/版本维护 |
| `planning-with-files` | 文件规划管理 |
| `report-generator` | 报告生成 |
| `obsidian` | Obsidian 知识库管理 |
| `skill-vetter` | 技能安全审核（来源审查/权限检查）|
| `find-skills` | 技能发现与安装 |
| `evolver` | GEPA 风格自我进化（DSPy + GEPA 框架）|

---

### 🔧 Utilities（17 个技能）

| 技能 | 功能 |
|------|------|
| `multi-search-engine` | 17 引擎聚合搜索（8 中文 + 9 英文）|
| `super-ocr` | PaddleOCR 高精度文字识别 |
| `imap-smtp-email` | IMAP/SMTP 邮件收发（多账号支持）|
| `deep-research-pro` | 多源深度研究（Web/RSS/Twitter/GitHub）|
| `tech-news-digest` | 技术新闻聚合（RSS/Twitter/GitHub Trending/Reddit）|
| `agent-browser` | 浏览器自动化（Chrome CDP 控制）|
| `email-daily-summary` | 邮件每日摘要 |
| `news-summary` | 新闻每日摘要（RSS）|
| `pdf` | PDF 处理（提取/合并/表单填写）|
| `excel-pro` | Excel 专业处理（公式/图表/数据清洗）|
| `excel-xlsx` | XLSX 文件操作 |
| `ai-video-generation` | AI 视频生成（Veo/Seedance/Wan/Grok 等 40+ 模型）|
| `data-visualization-2` | 数据可视化（图表选择/配色/标注）|
| `web-scraper` | 网页爬虫 |
| `webapp-testing` | Web 应用测试 |
| `sql-generator` | SQL 查询生成 |
| `sql-toolkit` | SQL 工具包 |

---

## 🛠️ 开发自己的技能

参考 `skill-creator` 技能包：

```bash
# 方式1: 使用 SkillHub CLI
skillhub install skill-creator

# 方式2: 参考模板
openclaw skills create <your-skill-name>
```

**技能结构：**
```
your-skill/
├── SKILL.md          # 技能说明（必须）
├── scripts/           # 脚本目录（可选）
│   ├── main.py
│   └── utils.sh
└── references/        # 参考资料（可选）
    └── guide.md
```

---

## ⚠️ 免责声明

本仓库中的技能涉及：
- **投资建议类**（finance/）：仅供学习和研究，不构成任何投资建议。股市有风险，投资需谨慎。
- **邮件/外贸类**（growth/）：用户需自行配置 SMTP/IMAP 凭证。
- **API 密钥**：部分技能需要用户自行申请 API Key（已在文档中说明申请方式）。

**所有技能包不含任何硬编码的个人隐私数据或凭证。**

---

## 📄 License

MIT License - 可自由使用、修改、分发，商用请注明来源。

---

_鸿钿团队 · OpenClaw AI Agent · 2026_
