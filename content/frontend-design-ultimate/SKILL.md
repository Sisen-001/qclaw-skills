---
name: frontend-design-ultimate
description: |
  公众号排版终极技能。支持Terminal Elegance暗黑金融风（深海蓝#1e3a5f+中国红#c9302c+金色#d4af37）+ JetBrains Mono字体，专为老黄财经公众号（老黄早参/老黄收评/财姐周末）定制。
  也支持通用网页设计（React/Tailwind/shadcn/ui）。
metadata:
  openclaw:
    emoji: "🎨"
    requires:
      bins: ["node", "npm"]
    triggers:
      - "排版"
      - "老黄早参"
      - "老黄收评"
      - "财姐"
      - "公众号"
      - "Terminal"
      - "深蓝"
      - "财经"
      - "收评"
      - "早参"
---

# Frontend Design Ultimate - 公众号排版版

> 2026-04-14 进化版 · 专为老黄财经公众号定制

## 🎯 进化背景

大秘确定的老黄财经公众号排版规范：

| 元素 | 值 |
|------|-----|
| 主色 | 深海蓝 #1e3a5f |
| 强调色 | 中国红 #c9302c（涨）|
| 点缀色 | 金色 #d4af37 |
| 背景色 | #0a1628 或 #0d1117 |
| 字体 | JetBrains Mono |
| 风格 | Terminal Elegance（暗黑终端风）|

---

## 🔥 公众号排版模式（主模式）

### 触发关键词

当用户提及以下任一关键词时，**自动切换到公众号排版模式**：

| 关键词组 | 示例 |
|----------|------|
| 栏目名 | 老黄早参、老黄收评、财姐周末、财姐早参 |
| 操作指令 | 排版、发公众号、公众号排版 |
| 风格描述 | Terminal、暗黑、金融风、深蓝 |
| 公众号相关 | 公众号文章、推送、群发 |

### 排版规范

#### 1. HTML结构

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{标题}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'JetBrains Mono', -apple-system, monospace;
  background: #0d1117;
  line-height: 1.75;
  color: #e8e8e8;
}
.container { max-width: 414px; margin: 0 auto; background: #0a1628; min-height: 100vh; }
.header { background: linear-gradient(180deg, #1e3a5f 0%, #0d1f33 100%); padding: 28px 20px; text-align: center; border-bottom: 2px solid #d4af37; }
.header-title { color: #fff; font-size: 22px; font-weight: 700; letter-spacing: 2px; }
.header-date { color: #d4af37; font-size: 13px; margin-top: 8px; }
.section { padding: 18px 16px; border-bottom: 1px solid #1e3a5f; }
.section-title { font-size: 14px; font-weight: 700; color: #d4af37; margin-bottom: 14px; padding-left: 12px; border-left: 3px solid #c9302c; text-transform: uppercase; letter-spacing: 1px; }
.lead { background: linear-gradient(135deg, #1e3a5f 0%, #2d4a6f 100%); padding: 18px; border-radius: 10px; margin-bottom: 16px; }
.lead-text { color: #fff; font-size: 14px; line-height: 1.9; }
.lead-highlight { color: #d4af37; font-weight: 600; }
.direction-item { padding: 12px 0; border-bottom: 1px dashed #1e3a5f; }
.direction-name { color: #d4af37; font-weight: 700; font-size: 14px; }
.direction-desc { color: #b0b0b0; font-size: 12px; margin-top: 6px; }
.forecast-box { background: linear-gradient(135deg, #1e3a5f 0%, #2d4a6f 100%); padding: 16px; border-radius: 10px; margin: 14px 0; }
.forecast-item { display: flex; justify-content: space-between; padding: 8px 0; font-size: 13px; border-bottom: 1px dashed rgba(212,175,55,0.3); }
.forecast-label { color: #b0b0b0; }
.forecast-value { color: #d4af37; font-weight: 600; }
.discipline-box { background: rgba(201,48,44,0.15); border: 1px solid #c9302c; border-radius: 8px; padding: 14px; }
.discipline-item { padding: 8px 0; font-size: 13px; color: #e8e8e8; }
.discipline-highlight { color: #c9302c; font-weight: 600; }
.disclaimer { background: #0d1f33; padding: 16px; font-size: 11px; color: #666; line-height: 1.8; text-align: center; border-top: 1px solid #1e3a5f; }
.footer { text-align: center; padding: 16px; color: #d4af37; font-size: 12px; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="header-title">📊 {栏目名}</div>
    <div class="header-date">{日期}</div>
  </div>
  <div class="section">{内容}</div>
  <div class="disclaimer">{免责声明}</div>
  <div class="footer">{签名}</div>
</div>
</body>
</html>
```

#### 2. 配色变量

```css
:root {
  --bg-primary: #0a1628;
  --bg-secondary: #0d1117;
  --bg-card: #1e3a5f;
  --text-primary: #e8e8e8;
  --text-secondary: #b0b0b0;
  --accent-gold: #d4af37;
  --accent-red: #c9302c;
  --accent-green: #2d8f4e;
  --border: #1e3a5f;
}
```

#### 3. 数据展示规范

- **涨跌幅**：用颜色区分（红涨绿跌）
- **表格**：手机端414px自适应
- **关键数字**：加粗+金色高亮

#### 4. 板块标题规范

```
【板块名】→ <div class="section-title">板块名</div>
```

### 标题生成规则

**每次产出必须自带标题**（老板指令）：
- 格式：`栏目名 | 日期 · 核心判断`
- 字数：≤20字
- 示例：
  - 老黄早参 | 4.15 · 高开站稳4000？
  - 老黄收评 | 4.14 · 92涨停别急追

### 输出文件

生成后保存到：
```
/tmp/{栏目名}_{YYYYMMDD}.html
```

---

## 🌐 通用网页设计模式（备用模式）

当用户未提及公众号关键词时，使用原有React/Tailwind模式。

### 支持的场景

- Landing Page
- 营销页面
- Portfolio
- Dashboard
- 任何静态网站

### 技术栈

- React 18 + TypeScript
- Tailwind CSS + shadcn/ui
- Framer Motion
- Vite 或 Next.js

### 快速开始

```bash
# Vite模式
bash scripts/init-vite.sh my-site

# Next.js模式  
bash scripts/init-nextjs.sh my-site
```

### 设计原则

| 原则 | 说明 |
|------|------|
| Bold Aesthetic | 选择一个风格并坚持（Brutal/Maximalist/Retro-Future等）|
| Typography | 禁用Inter/Roboto，用Clash/Space Grotesk/Playfair |
| Color | 主色+强调色，禁用均匀分布的5色 |
| Motion | 整体编排 > 零散微交互 |
| Mobile-First | 桌面端需适配移动端 |

---

## 🧬 进化日志

| 日期 | 进化内容 |
|------|---------|
| 2026-04-14 | 新增公众号排版模式，集成Terminal Elegance风格 |
| 2026-04-14 | 添加配色变量：#1e3a5f / #c9302c / #d4af37 |
| 2026-04-14 | 添加触发关键词识别（老黄早参/老黄收评/财姐等）|
| 2026-04-14 | 添加标题生成规则（≤20字，含日期+核心判断）|

---

*Based on Anthropic's frontend-design + 大秘公众号排版规范*
