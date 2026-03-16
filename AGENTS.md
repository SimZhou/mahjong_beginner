# 麻将站点重建说明

## 当前分支

- 本分支用于基于本地镜像的日文原站页面，从零重建整站。
- 源内容位于 `site_src/`。
- 用于 GitHub Pages 部署的静态产物必须输出到 `docs/`。
- 原始镜像页面与素材位于 `raw_site/`。

## 关键目录

- `site_src/docs/`：翻译后的中文 Markdown 页面
- `site_src/mkdocs.yml`：MkDocs 配置
- `docs/`：可部署的静态站点输出
- `raw_site/articles/`：原始日文文章页面的本地快照
- `raw_site/assets/`：原始图片及其它素材的本地镜像
- `scripts/build_site.sh`：标准构建入口

## 当前项目状态

- 当前已完成对本地镜像原站内容的整站中文覆盖：
  - `raw_site/articles/` 中的镜像源页面：`110`
  - `site_src/docs/` 中的对应翻译页面：`110`
  - 已知缺失的镜像页面：`0`
- 当前章节顺序已与原始 `sitemap` 对齐：
  1. 麻将基础
  2. 牌理与牌效率
  3. 麻将役种
  4. 宝牌与红宝牌
  5. 鸣牌
  6. 立直
  7. 防守
  8. 局势判断
  9. 押引
- 左侧导航和各章节首页标题统一使用 `第N章：...` 前缀。
- 首页已不再作为粗糙的旧首页归档使用：
  - 教程章节改为章节卡片入口
  - 原站首页的欢迎语与更新履历保留在重建后的首页中
  - 附录内容已与首页正文拆分，并移到导航底部
- 当前附录包含：
  - 作者介绍
  - 麻将链接集
  - 站外推荐资源
  - 全站目录
- `site_src/docs/blog/home_archive.md` 已有意从重建站点流程中移除，除非用户明确要求，否则不要重新加回。

## 构建规则

- 一律使用以下命令构建：

```bash
scripts/build_site.sh
```

- 不要输出到 `docs/` 之外的其它目录。
- 是否验收通过，必须以生成后的 `docs/` 为准，不能只看 Markdown 源文件。

## SEO 与发现机制规则

- 页面级 SEO 优先通过 Markdown 头部元数据维护：
  - `title`
  - `description`
  - `image`
- 对正文页补 `description` 时，不要改写可见正文内容；优先只新增 YAML 头部元数据。
- 当前项目已提供批量补描述脚本：

```bash
/opt/miniforge3/bin/python scripts/add_page_descriptions.py
```

- `IndexNow` 已接入本项目，当前密钥文件位于：
  - `site_src/docs/6f0d3cf671bf4bb3b4dfe2dfef4f11d6.txt`
- 提交脚本位于：
  - `scripts/submit_indexnow.py`
- 使用 `IndexNow` 时，先完成构建并确认 `docs/sitemap.xml` 已更新，再执行：

```bash
/opt/miniforge3/bin/python scripts/submit_indexnow.py
```

- `IndexNow` 提交时不要包含 `404.html` 这类 `noindex` 页面。
- 页面级 `description` 和 `IndexNow` 提交，原则上只影响搜索引擎抓取与摘要展示，不应引入正文可见内容变更。

## 翻译规则

- 翻译必须基于 `raw_site/articles/` 下的本地日文源快照。
- 不要使用外部翻译 API。
- 保持与原文一致的文章逻辑、例题顺序和结论结构。
- 页面底部必须保留原始来源链接：

```md
原始日文页：<http://beginners.biz/...>
```

## 首页与附录规则

- 原始首页要视为真实内容页，而不是单纯导航壳子。
- 原站首页的欢迎语、更新履历等信息要尽量忠实保留，不要随意压缩。
- 如果需要在首页和附录之间重新分配内容：
  - 教程导入与更新履历属于首页
  - 作者介绍、外链、推荐资源属于附录
  - 不要让首页和附录首页重复承载同一大段内容
- 修改首页文案时，必须重新对照 `raw_site/articles/index.html`，不要凭记忆改写。
- 首页章节卡片需要：
  - 保持原始章节顺序
  - 语义上保留原始导语说明
  - 构建后同时验证桌面端和移动端

## 图示规则

- 文章中的图示属于正文内容，不是装饰。
- 对每一页，都要把原始 `../images/...` 引用与以下位置进行比对：
  - `site_src/docs/...`
  - 生成后的 `docs/...`
- 如果原页存在文章图示，翻译页也必须保留。
- 文章内图示优先级高于正文之外的装饰性素材。

## 回归检查清单

逐页复查时，始终检查以下三项：

1. 是否缺少文章图示
2. 翻译含义是否漂移或出错
3. 排版是否存在缺陷

最低检查流程：

1. 对比 `raw_site/articles/<page>.html` 与 `site_src/docs/<page>.md`
2. 对比原始 `../images/...` 引用与生成后的 `docs/<page>.html`
3. 检查生成 HTML 的标题结构和页尾原始链接
4. 检查翻译后的 Markdown 中是否残留日文假名

## 牌河表格规则

- 有些原页把舍牌示意渲染成非常紧凑的两行 HTML 表格：
  - 第一行：`例N` 与 `↓` 等摸切标记
  - 第二行：纯牌图
- 这类表格属于正文内容，不要把它当成普通数据表处理。
- 不要在原始 HTML 表格单元格里直接写 Markdown 图片语法 `![tile](...)`。在本项目里，这种写法可能会原样出现在生成 HTML 中，而不会被转成 `<img>`。
- 对这类牌河表示意表格：
  - 在 `<td>` 中使用真实的 `<img ...>` 标签
  - 外层用 `.river-block` 之类的容器包裹
  - 应用 `site_src/docs/stylesheets/extra.css` 里的 `.river-table` 专用样式
- 这样做的目的：
  - 保留原站紧凑的旧式视觉效果
  - 避免 Material 默认表格样式把它拉成宽表
  - 在窄屏上允许横向滚动，而不是把牌图压坏
- 页面包含这种牌河表格时，构建后必须额外检查：
  1. 生成的 `docs/<page>.html` 里单元格必须是 `<img>`，不能出现字面量 `![...]`
  2. 生成 HTML 中必须存在 `river-block` / `river-table` 类名
  3. 视觉上要确认桌面端和窄屏端都仍然紧凑、可读
  4. 如果检查线上页面，也要确认部署后仍然保持紧凑样式，而不是退回 Material 默认表格外观

## 资源缩略图规则

- `site_src/docs/images` 是指向 `raw_site/assets/images` 的符号链接。向 `site_src/docs/images/...` 增删改图片，实际上就是在修改原始镜像素材目录。
- 如果翻译页对应原站那种带缩略图的推荐区或侧栏内容，不要把它扁平成纯链接列表，要尽量保留“图 + 标题 + 说明”的结构。
- 优先使用本地镜像缩略图，不要依赖远程热链。
- 对必须保留的外站缩略图：
  1. 下载或镜像到 `raw_site/assets/images/`
  2. 在翻译页中通过 `../images/...` 引用
  3. 检查生成后的 `docs/...` 页面引用的是本地图片，而不是远程图片 URL
- 使用卡片式推荐布局时，图片区必须使用固定高度容器，这样各卡片正文起点才能横向对齐。

## 线上抽样检查清单

- 本地 `docs/` 正确，不代表线上一定已经更新。
- 做完一批有意义的修改后，要对 `https://simzhou.com/mahjong_beginner/` 抽样检查。
- 线上抽样至少要确认：
  - 页面返回的是真实文章，而不是 `404`
  - 部署域名下文章图示能够正常加载
  - 页面底部存在原始日文页链接

- 网络重置、TLS 失败等问题，要和真实内容错误分开判断。
- 如果某个页面在 live 域名上持续稳定返回 `404 - Not found`，那就是实际部署问题，不是偶发网络抖动。
- 浏览器 CSS 缓存属于另一类问题：
  - 如果本地 `docs/...` 与线上 HTML/CSS 实际内容都正确，但浏览器仍显示旧布局，应先强制刷新，再判断是否发布失败

## 当前抽样结论

已确认线上正常的抽样页面：

- `kihon/kihon08.html`
- `teyaku/teyaku07.html`
- `dora/dora04.html`
- `naki/naki12.html`
- `reach/reach04.html`
- `osihiki/osihiki02.html`

曾确认过的线上部署问题：

- `https://simzhou.com/mahjong_beginner/joukyou/joukyou09.html`
  - 一度返回 `404 - Not found`
  - 但本地 `docs/joukyou/joukyou09.html` 实际存在且已追踪
  - 这说明问题在部署指向或发布状态，而不是本地构建缺失

## 部署验证更新

- 之前 `joukyou/joukyou09.html` 的 live `404`，原因是 GitHub Pages 当时还没有指向本分支的 `docs/`。
- 当 Pages 切到当前分支的 `docs/` 后，线上抽样已确认重建站点正在被正常提供服务。

复查后确认正常的 live 页面包括：

- `joukyou/joukyou09.html`
- `reach/reach04.html`
- `mamori/mamori12.html`
- `naki/naki12.html`
- `dora/dora04.html`
- `teyaku/teyaku07.html`
- `pairi/pairi20.html`

对这些页面，线上检查已确认：

1. 页面返回真实文章内容，而不是 `404`
2. 文章图示在部署域名下可正常加载
3. 页面底部保留原始日文页链接
4. 抽样 HTML 中未发现日文假名残留

## 实用规则

- 当用户反馈线上页面有问题时，先验证部署后的 URL。
- 不要因为本地 `docs/` 正确，就假定 live 站点也已经同步正确。

## 构建与提交卫生规则

- 在执行 `scripts/build_site.sh` 期间，`git status` 可能会暂时显示 `docs/` 下大量文件被删除，因为 MkDocs 会先清空输出目录再重建。不要把这个中间态误判为真实回归，必须等构建结束后再看。
- `docs/sitemap.xml` 与 `docs/sitemap.xml.gz` 经常会随重建变化，但当前工作流中默认不提交，除非用户明确要求。
