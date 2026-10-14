# Quick Start

Create your first business contract and validate the local development configuration.

Canonical: https://brivya.com/en/docs/quickstart/
Version: 0.1.0-alpha.1
Language: en

## Prerequisites

Use Node.js 20 or newer and npm. The local CLI flow does not require a cloud account, LLM API key or database.



```
node --version
npm --version
npm install -g @brivya/cli@0.1.0-alpha.1
```

## Create a business contract

```
mkdir my-business
cd my-business
brivya init
brivya validate
brivya inspect
brivya dev
```



`init` creates `business.agent.yaml`; `validate` checks the Manifest; `inspect` shows the resolved definition; `dev` validates and displays local configuration.



The generated Manifest is a contract scaffold. It is not connected to a real business system. CLI dev does not start an HTTP server or replace BusinessRuntime execution.

## Edit and observe

Maintain business identity, capabilities, protocols and security requirements in the generated Manifest. Inspect the scaffold before editing and keep validation in your workflow. To observe changes:



```
brivya dev business.agent.yaml --watch
```



You can pass an explicit Manifest path to validate, inspect and dev. Init does not silently overwrite existing files.

## Connect real capabilities

Use the SDK to register contracts, supply authorization and policy, implement Connectors and attach protocol adapters. Discovering a capability never grants permission to mutate business state.



Continue with the [SDK](https://brivya.com/en/docs/sdk/) or the [Restaurant reference](https://brivya.com/en/docs/restaurant/).
