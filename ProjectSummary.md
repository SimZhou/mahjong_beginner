# 项目收尾总结

## 项目定位

本仓库将经典日文麻将教程站 `beginners.biz` 的本地镜像内容，重建为可维护的 MkDocs 多语言文档站，并部署在：

- 中文：<https://simzhou.com/riichi_mahjong_book/>
- 英文：<https://simzhou.com/riichi_mahjong_book/en/>

## 当前完成状态

- 原始日文镜像文章页：`113`
- 中文 Markdown 页面：`116`
- 英文 Markdown 页面：`116`
- 生成后的 HTML 页面总数：`233`

说明：

- `113` 指与原始教程正文对应的镜像文章页数量
- `116` 指每个语言站点的完整页面数，包含首页、9 个章节、附录和全站目录
- `404.md` 不计入单语言正文页面统计

## 当前内容覆盖

中文站与英文站均已覆盖：

1. 麻将基础 / Mahjong Basics
2. 牌理与牌效率 / Tile Efficiency and Tile Theory
3. 麻将役种 / Yaku
4. 宝牌与红宝牌 / Dora and Red Fives
5. 鸣牌 / Calling
6. 立直 / Riichi
7. 防守 / Defense
8. 局势判断 / Situational Judgment
9. 押引 / Push/Fold Decisions

附录也已双语覆盖：

- 作者介绍 / Author Profile
- 麻将链接集 / Mahjong Link Directory
- 推荐资源 / Recommended External Resources
- 全站目录 / Full Site Map

## 已完成的关键工程工作

- 中文整站重建完成，并与原始 `sitemap` 章节顺序对齐
- 英文站点完成镜像路径建设，并已正式上线
- 首页与附录重新分工，避免原站首页内容在重建站中重复堆叠
- 中英文页面均已补齐页面级 `title` / `description`
- 中英双向 `hreflang` 与 `x-default` 已落地
- 多语言 sitemap 已生成：
  - `docs/sitemap.xml`
  - `docs/sitemap-zh.xml`
  - `docs/sitemap-en.xml`
- `IndexNow` 已接入并可提交最新站点地图
- 英文站内误链到中文页的问题已清零
- 英文站内坏链问题已清零
- 多批缺失或损坏的原始示意图已补抓并纳入镜像素材库

## 当前维护脚本

- 构建：
  - `scripts/build_site.sh`
- 英文资源路径修复：
  - `scripts/check_fix_en_asset_paths.py`
- 英文站内链审计：
  - `scripts/check_en_internal_links.py`
- 多语言 sitemap 生成：
  - `scripts/generate_locale_sitemaps.py`
- 页面描述补全：
  - `scripts/add_page_descriptions.py`
- 英文页正式上线切换：
  - `scripts/release_english_pages.py`
- IndexNow 提交：
  - `scripts/submit_indexnow.py`
- 全站 SEO 审计：
  - `scripts/audit_seo.py`

## 本项目的经验总结

### 内容层

- 原始图示必须视为正文的一部分，不能当作装饰性图片。
- 牌例、表格、图示、绿色总结块、红字强调，都会影响原文教学节奏，翻译时应尽量保留。
- 首页并不只是导航页，原站欢迎语和更新履历都属于实际内容。

### 工程层

- `docs/` 必须始终视为验收标准，不能只看 `site_src/docs/`。
- MkDocs 构建期间 `docs/` 会先被清空，不能在构建中途根据 `git status` 误判。
- 英文页最容易出现的错误不是正文翻译，而是相对路径和内部链接。
- 原始镜像素材可能不完整，出现页面缺图时不能只检查路径，还要检查 `raw_site/assets/images/` 中的源文件是否为 0 字节或损坏。

### 多语言层

- 语言切换 UI 和搜索引擎语言映射是两件事。
- `hreflang` 必须逐页精确映射，不能偷懒统一指向首页。
- 英文版未完成前使用 `noindex` 是合理的，但正式上线时必须整体切回可索引状态。

### SEO 层

- 页面级描述优先放在 YAML 头部，不要直接改动正文首段。
- `robots.txt`、多语言 sitemap、`hreflang`、`x-default`、`IndexNow` 应视为同一套上线收尾动作。
- live 抽样检查很重要，本地生成正确不代表线上已更新。

## 当前可继续做的事情

- 对中英文站再做一轮抽样式人工校对
- 持续完善 README 与项目说明文档
- 如需继续扩展，可补更多站点级维护脚本或发布自动化流程

