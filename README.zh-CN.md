<h1 align="center">日麻: 从入门到精通</h1>

<p align="center">
  <a href="./README.md">English</a> | <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://simzhou.com/riichi_mahjong_book/"><img alt="在线站点" src="https://img.shields.io/badge/site-online-0f766e?style=flat-square"></a>
  <img alt="中文版" src="https://img.shields.io/badge/chinese-complete-2563eb?style=flat-square">
  <img alt="英文版" src="https://img.shields.io/badge/english-complete-2563eb?style=flat-square">
  <img alt="构建框架" src="https://img.shields.io/badge/built%20with-MkDocs-526CFE?style=flat-square">
  <img alt="许可证" src="https://img.shields.io/badge/license-MIT-16a34a?style=flat-square">
</p>

这是一个把经典日文麻将教程站点完整重构为现代文档站的项目。

忠实保留原始教学内容，重新整理结构与阅读体验，并完成为一个中英双语的长期维护仓库。

在线地址：<https://simzhou.com/riichi_mahjong_book/>

## 这是什么项目

这个仓库不是“麻将知识随手整理”，而是一次完整的站点级重建。目标是尽可能保留原始教程的教学顺序、例题逻辑、图示结构和阅读体验，同时把它变成一个现代、可持续维护的文档项目。

当前包含：

- 完整的中文版本
- 完整的英文版本
- 保留原文例题、表格、图示的页面级重构
- 可直接部署到 GitHub Pages 的静态产物
- 现代化的发布与维护工作流

## 为什么这个仓库值得看

很多老牌麻将教程站会出现两种情况：

- 内容非常扎实，但站点结构脆弱、难以维护
- 页面好读，但把原始教学深度压缩掉了

这个项目要保留的是两者兼得：

- 原站的教学价值
- 现代化的文档化工作流
- 更清晰的导航和呈现方式
- 已完成的中英双语阅读体验

## 项目亮点

- 已完整覆盖本地镜像中的全部中文正文页面
- `113` 个日文镜像源页，对应 `113` 个重建文章页
- 章节顺序与原始 `sitemap` 保持一致
- 正文图示不被扁平化，保留原有教学价值
- 首页、附录、资源页经过重新组织，适合现代阅读
- 英文站已完整上线，并与中文站保持镜像路径

## 快速开始

```bash
scripts/build_site.sh
```

输出目录：

```text
docs/
```

## 在线站点

- 中文站：<https://simzhou.com/riichi_mahjong_book/>
- 英文站：<https://simzhou.com/riichi_mahjong_book/en/>

## 当前可阅读内容

当前中英文站都已覆盖完整镜像教程：

1. 麻将基础
2. 牌理与牌效率
3. 麻将役种
4. 宝牌与红宝牌
5. 鸣牌
6. 立直
7. 防守
8. 局势判断
9. 押引

附录内容也已提供中英文版本：

- 作者介绍
- 麻将链接集
- 推荐书目、期刊、讲座和相关资源
- 全站目录

## 仓库结构

```text
site_src/
  docs/          Markdown 正文、元数据、模板、样式、多语言页面
  mkdocs.yml     MkDocs 配置
docs/            GitHub Pages 使用的静态输出目录
raw_site/
  articles/      原始日文文章 HTML 本地快照
  assets/        原始图片与素材镜像
scripts/         构建与维护脚本
```

## 翻译原则

- 以 `raw_site/articles/` 中的本地日文快照为准
- 不使用外部翻译 API
- 保持原始例题顺序、教学节奏和结论结构
- 正文图示视为强制保留内容，不当作装饰
- 每页底部保留原始日文页链接

## 多语言结构

当前采用的多语言路由策略：

- 中文：`/riichi_mahjong_book/`
- 英文：`/riichi_mahjong_book/en/`

英文页会尽量和中文页保持镜像路径，例如：

- 中文：`/riichi_mahjong_book/kihon/kihon01.html`
- 英文：`/riichi_mahjong_book/en/kihon/kihon01.html`

## 说明

- 原始日文页已在本仓库本地镜像保存，便于逐页对照。
- 翻译页会保留原始日文来源链接。

## 致谢

本项目基于原始日文教程站点的本地镜像内容重建：

- <http://beginners.biz/>

## 协作建议

如果你想继续改进这个项目，优先关注：

- 对原文教学逻辑的忠实度
- 麻将术语的准确性
- 图示与牌例的完整性
- 生成后的 `docs/` 是否正确，而不只是源 Markdown
