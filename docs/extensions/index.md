# Extension Host

明确声明权限，通过受限 Host API 扩展业务能力。

Canonical: https://brivya.com/docs/extensions/
Version: 0.1.0-alpha.1
Language: zh

## Alpha 基线

Extension Host 包含 Extension Manifest / Package、权限授权、权限扩张检测、安装计划、Registry Client 契约及 worker / remote 执行边界。



这些是框架层契约与基线能力，不代表已有公开托管 Registry 或第三方扩展市场。

## 有效权限

```
请求权限 ∩ 租户策略 ∩ 管理员授权 = 有效权限
```



扩展声明权限并不自动获得权限。新版本扩大权限时，需要重新批准；宿主只授予最终交集允许的能力。

## 执行与凭据边界

```
Extension → Host API
→ canonical Brivya Runtime / governed platform service
```



Host API 按权限限制访问，凭据通过不透明 secret binding 引用。不存在原始 secret-read Host API，也不应把凭据明文交给扩展。

## 当前限制

Phase 1 使用 worker 与 remote 执行模型。WASM 延后，任意第三方进程内执行不属于当前基线。上线前需验证宿主隔离、授权和外部网络策略。



[回到运行时安全模型 →](https://brivya.com/docs/architecture/)
