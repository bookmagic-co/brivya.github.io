# TypeScript SDK

复用公开业务类型、Manifest 校验器与 canonical 运行时。

Canonical: https://brivya.com/docs/sdk/
Version: 0.1.0-alpha.1
Language: zh

## 安装

```
npm install @brivya/sdk@0.1.0-alpha.1
```



SDK 是 Core、Manifest、Policy 与 Runtime 的公开接口门面，不创建第二套授权或运行时真相。

## 解析和校验 Manifest

以下示例读取由 CLI init 生成的 Manifest，并运行同一 canonical 解析与校验逻辑：



```
import { readFileSync } from "node:fs";
import { loadBusinessAgentManifest } from "@brivya/sdk";

const source = readFileSync("business.agent.yaml", "utf8");
const agent = loadBusinessAgentManifest(source);
console.log(agent.metadata.id);
```



解析或校验失败时应处理错误，不要将无效 Manifest 继续用于业务执行。

## 运行时与类型

```
import {
  BusinessRuntime,
  CapabilityRegistry,
  runtime,
  type ActionRequest,
  type CapabilityContract,
  type Principal,
  type Delegation,
} from "@brivya/sdk";
```



BusinessRuntime 和 CapabilityRegistry 指向 canonical 实现。实际配置需要能力注册、Connector、授权上下文和相关运行时依赖；仅导入 SDK 不会创建可执行业务服务。

## 应用集成顺序

- 定义能力输入、输出与业务安全要求。
- 通过 CapabilityRegistry 注册能力契约。
- 提供真实业务 Connector 与所需的策略、审批、幂等和审计实现。
- 由可信服务端构造身份与委托上下文。
- 使用 BusinessRuntime 执行，或通过 REST / MCP 适配器调用同一运行时。



参考 [Restaurant 示例](https://brivya.com/docs/restaurant/) 学习注册能力和执行测试；参考 [适配器指南](https://brivya.com/docs/adapters/) 连接协议入口。

