# Restaurant 示例

通过确定性测试理解发现、预订、订单和支付请求的完整业务链路。

Canonical: https://brivya.com/docs/restaurant/
Version: 0.1.0-alpha.1
Language: zh

## 示例能力

| Capability | 业务步骤 | 
|  --- | --- |
| menu.search | 搜索菜单 | 
| availability.check | 检查可用性 | 
| reservation.create | 创建预订 | 
| order.create | 创建订单 | 
| payment.request | 请求支付 | 



REST 与 MCP 执行同一能力契约并共享 BusinessRuntime。示例使用 mock Connector，不依赖特定 LLM 或真实支付 SDK。

## 获取并运行

```
git clone https://github.com/brivya/brivya.git
cd brivya
npm install --ignore-scripts --no-audit --no-fund
npm run ci
```



当前仓库没有提交 lockfile，因此使用与 CI 一致的 npm install。根命令完成构建、类型检查及测试，包含 Restaurant RST-001..RST-024 契约矩阵。

## 只运行示例测试

```
npm run build
node --test examples/restaurant/dist/test/*.test.js
```



先构建所有工作区以准备跨包依赖，再运行已编译的示例测试。测试使用确定性数据，覆盖业务执行、安全拒绝和审计等行为。

## 阅读路径

- `examples/restaurant/src/manifest.ts`：业务身份与能力声明。
- `examples/restaurant/src/capabilities.ts`：业务能力定义。
- `examples/restaurant/test/`：端到端验证证据。
- `connectors/mock/`：模拟业务系统连接。



payment.request 表示业务支付请求，不表示示例已经接通真实支付渠道。Manifest 中的 bootstrap URL 是示例业务身份，不是官网提供的在线演示服务。

