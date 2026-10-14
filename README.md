# Brivya 官网初稿

独立静态站点，公开仓库为 `bookmagic-co/brivya.github.io`。源码与 CI 已推送，首次远端检查通过；首次部署等待仓库管理员开启 Pages。

## 本地审阅

从此目录运行 `python3 scripts/check.py`、`node --check assets/site.js`、`python3 scripts/build.py`，再运行 `python3 -m http.server 8080 --bind 127.0.0.1 --directory _site`。构建仅使用 Python 标准库复制公开文件，不需要安装依赖或服务器端运行时。

首页包括产品介绍、可视化架构、Quick Start、SDK、适配器、扩展与文档入口。文档链接指向公开实现仓；不链接私有治理仓。内容依据当前 `v0.1.0-alpha.1` 发布状态，API 为预稳定版本。页面自带字体回退，不依赖第三方字体、分析服务或 CDN。

## GitHub Pages 发布步骤

1. 审阅页面与内容后，把此目录内容放入独立的 `bookmagic-co/brivya.github.io` 仓库的 `main` 分支根目录。保留已有文件，先检查目标仓库状态。
2. 在仓库 Settings → Pages 中将 Source 选择为 **GitHub Actions**。工作流 `.github/workflows/pages.yml` 在 PR 上执行检查；`main` 推送或手动触发后，检查成功才上传 `_site` 并部署 Pages。PR 不部署生产环境。
3. 确认默认 GitHub Pages 地址工作，检查首页、资源链接、移动布局与复制按钮。
4. 已确认正式域名为 `brivya.com`。先在 GitHub 组织 Settings → Pages 验证域名所有权，再将仓库 Pages 的 Custom domain 设为 `brivya.com`，按 [DOMAIN.md](DOMAIN.md) 配置 DNS。
5. 等待 GitHub DNS 检查与证书签发完成，启用 Enforce HTTPS，验证主域名和 `www` 跳转。仓库已准备 `CNAME`、canonical URL、`og:url`、robots 与 sitemap。

官方说明：https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

自定义域名：https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

本地开发与自动部署配置已完成，部署仓库已确定为公开的 `bookmagic-co/brivya.github.io`。DNS 需要腾讯云后台配置。npm 发布与 OIDC 绑定属于独立任务。

开发与部署的完整执行步骤见 [DEPLOYMENT.md](DEPLOYMENT.md)。GitHub Actions 模式以 Pages 设置中的 Custom domain 为准；`CNAME` 文件不代替该设置。

## 官网文档

中文文档位于 `/docs/`，英文文档位于 `/en/docs/`，均提供快速开始、架构、安全、SDK、适配器、扩展、Restaurant 示例、版本与贡献说明。中文内容维护于 `scripts/docs.py`，英文内容维护于 `scripts/docs_en.py`；运行 `python3 scripts/docs.py` 生成已提交的双语内页与 sitemap。不要直接编辑生成页；CI 检查生成结果是否一致。

检查器验证所有文档页的内部链接、跨页锚点、canonical URL 和 sitemap 覆盖；构建只复制公开 HTML 和静态资源。首页主要入口跳转到官网文档，源码与实际贡献渠道仍链接 GitHub。

## 语言与业务动画

中文首页为 `/`，英文首页为 `/en/`。中文首页是维护源，英文文案位于 `scripts/home_en.py`；运行 `python3 scripts/home_en.py` 生成英文首页。默认语言为中文，切换器使用当前页的对应路由；主动选择保存在本地浏览器中。直接打开文档 URL 时尊重链接语言。语言配置位于 `assets/language.js`，不使用第三方翻译服务。

首页业务价值演示使用原生 SVG/CSS 和 JavaScript，在四个阶段说明发现、结构化请求、治理、执行与审计。文案维护于 `assets/business-animation.js`；首屏静态文案同时维护在首页及英文翻译表中。动画支持暂停、手动选段、不可见时停止，以及系统减少动效设置。它不是在线交易演示，不发出业务 API 请求。

## AI 文档发现

`/llms.txt` 和 `/en/llms.txt` 提供双语文档目录；对应的 `llms-full.txt` 包含该语言全部文档正文。每个文档目录提供 `index.md`，`/ai/index.json` 提供本网站定义的结构化索引（不宣称为通用 Agent 协议）。页面通过 alternate 链接与可见 AI docs / Markdown 入口提供发现提示。

运行 `python3 scripts/agent_docs.py` 从同一文档维护源生成 AI 版本。它保留代码示例、链接和业务安全边界，不包含导航或动画脚本。CI 检查 HTML、Markdown、索引与全文的一致性。这些入口采用文档发现约定，不能保证所有 Agent 都会自动使用；网站未声明业务执行或授权服务。
