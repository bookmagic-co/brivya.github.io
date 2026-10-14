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
