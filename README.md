# 麻将入门教程

一个面向中文读者的日式立直麻将教程网站项目，内容覆盖：

- 麻将基础
- 牌理与牌效率
- 麻将役种
- 宝牌与红宝牌
- 鸣牌
- 立直
- 防守
- 局势判断
- 押引

网站地址：

- <https://simzhou.com/mahjong_beginner/>

## 本地构建

构建命令：

```bash
scripts/build_site.sh
```

构建产物输出到：

```text
docs/
```

## 项目结构

- `site_src/docs/`：站点正文 markdown
- `site_src/mkdocs.yml`：MkDocs 配置
- `docs/`：静态部署目录
- `raw_site/articles/`：原始日文页面正文快照
- `raw_site/assets/`：原始图片等资源

## 说明

- 页面末尾保留了原始日文页链接，方便对照原文。
- 正文示意图与例题图片会随页面一同维护。
