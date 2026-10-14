# 快速开始

用 CLI 创建第一份业务契约，验证本地开发配置。

Canonical: https://brivya.com/docs/quickstart/
Version: 0.1.0-alpha.1
Language: zh

## 环境准备

需要 Node.js 20 或更高版本与 npm。CLI 的本地流程无需云账号、LLM API Key 或数据库。



```
node --version
npm --version
npm install -g @brivya/cli@0.1.0-alpha.1
```

## 创建业务契约

```
mkdir my-business
cd my-business
brivya init
brivya validate
brivya inspect
brivya dev
```



`init` 创建 `business.agent.yaml`；`validate` 校验 Manifest；`inspect` 展示解析后的业务定义；`dev` 验证并展示本地配置。



初始化生成的是业务契约骨架，尚未连接实际业务系统。CLI dev 不启动 HTTP 服务，也不代替 BusinessRuntime 执行业务。

## 编辑与观察

在生成的 Manifest 中维护业务标识、能力声明、协议和安全要求。先运行 `brivya inspect` 了解骨架，不要跳过校验。要观察文件变化，使用：



```
brivya dev business.agent.yaml --watch
```



也可以向 validate、inspect 和 dev 显式传入 Manifest 文件路径。已有文件不会被 init 默默覆盖。

## 连接真实能力

下一步在应用内使用 SDK 注册能力契约、配置授权与策略、提供 Connector，并接入协议适配器。发现业务能力不等于获得变更权限。



[继续阅读 SDK](https://brivya.com/docs/sdk/)，或通过 [Restaurant 示例](https://brivya.com/docs/restaurant/) 理解完整执行路径。
