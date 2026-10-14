# 官网初稿验证

验证日期：2026-10-13。

- Chromium 实际访问静态站点：本地资源返回成功，无浏览器脚本错误。
- 1440、768、390、320 像素视口：页面没有水平溢出；已修复 320 像素导航布局。
- Quick Start 锚点导航正常。
- 复制按钮成功时写入正确命令；剪贴板拒绝时提示手动复制。
- HTML 内部锚点、本地 CSS、JavaScript 与 SVG 路径均存在。
- 从 npm registry 安装已发布的 `@brivya/cli@0.1.0-alpha.1`，实际执行 init、validate、inspect、dev，全部成功。安装采用临时 prefix 与可写缓存，不修改全局环境。
- 保留 desktop.png 与 mobile.png 作为本地审阅截图，已加入忽略列表。
- 两个原有仓库工作区干净；未推送代码、配置 Pages 或修改 DNS。

仍需在部署后验证 GitHub Pages 地址、正式域名、HTTPS 与外部链接。当前未声称站点已上线。

## 2026-10-14：CI 与部署产物验证

- CI 工作流 YAML 解析成功，检查 PR 与 main 触发条件、build/deploy 依赖、上传路径与权限。
- 执行实际 CI 中的静态检查、JavaScript 语法检查与构建命令，全部成功；构建重复执行成功。
- 检查器在临时副本中成功拒绝缺失 CSS、错误锚点与错误域名。
- 对 `_site` 构建产物运行 Chromium HTTP 检查：1440/768/390/320 视口、复制按钮、CNAME/robots/sitemap 均正常。
- GitHub Actions 尚未实际运行；本地 YAML 与命令检查不等于远端 CI 成功。
- GitHub API 当前被代理网络策略拦截；已保存添加 API 与正式站点域名的网络配置草稿，尚未确认运行时生效。
- 随后 GitHub API 已恢复响应：产品仓权限查询正常，官网仓查询返回 404；实际创建官网仓库请求被 GitHub 集成拒绝（403 Resource not accessible by integration）。未创建仓库或触发上线。

## 官网仓库接入后的远端验证

- 用户创建了公开仓库 `bookmagic-co/brivya.github.io`；接入前确认仓库为空，未覆盖已有文件。
- 初始源码与 CI 提交 `b7111c1` 已成功推送。
- GitHub Actions run 38524750819：Validate and build 成功，包括静态检查、JS 语法、构建与 Pages 产物上传。
- Deploy to GitHub Pages 在 Check Pages configuration 失败；Deploy 被跳过，未声称上线。
- Pages 创建 API 实际返回 403 Resource not accessible by integration，需要管理员在 Settings → Pages 启用 GitHub Actions。
