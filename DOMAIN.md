# brivya.com 域名配置

用户已确认购买 `brivya.com`。主站使用 `https://brivya.com/`，`www.brivya.com` 作为别名。

## 操作顺序

1. 在 GitHub 的 **bookmagic-co 组织 Settings → Pages** 添加并验证 `brivya.com`。将 GitHub 当场生成的 TXT 主机名与值原样填入域名管理后台；不猜测验证码。成功后保留 TXT 记录。
2. 在官网仓库 **Settings → Pages** 配置站点来源，并将 Custom domain 设为 `brivya.com`。仓库根目录的 `CNAME` 已准备好。
3. 检查现有 DNS 记录后添加下表记录。只调整网站相关且冲突的记录，保留邮件、域名验证及其他业务记录。

| 类型 | 主机记录 | 值 |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `bookmagic-co.github.io` |

`@` 表示根域名；部分服务商要求填写完整的 `brivya.com`。TTL 使用服务商默认值即可。`www` 指向 GitHub Pages 域名，不填写协议、路径或 `brivya.com`。不配置通配符。若 DNS 服务有代理功能，首次验证使用 DNS only；若已有根域名 AAAA 指向其他服务，需先处理该冲突。

4. 等待 Pages DNS 检查与证书签发完成，再启用 **Enforce HTTPS**。
5. 检查 `https://brivya.com/` 返回首页，`https://www.brivya.com/` 跳转至主域名，HTTP 自动跳转 HTTPS，CSS/JS/SVG、robots 与 sitemap 可访问。

## 当前状态

源码已推送到公开仓库 `bookmagic-co/brivya.github.io`，CI 构建已通过。当前集成调用 Pages 启用 API 被拒绝，需要管理员在仓库设置选择 GitHub Actions，并填写 Custom domain。DNS 后台与证书设置尚未操作。购买域名本身不会自动应用这些设置。

GitHub 官方说明：https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

DNS A 记录已于 2026-10-14 对照 GitHub 官方文档仓库内容核实：https://github.com/github/docs/blob/main/content/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site.md
