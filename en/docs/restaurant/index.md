# Restaurant reference

Follow discovery, reservations, orders and payment requests through deterministic contract tests.

Canonical: https://brivya.com/en/docs/restaurant/
Version: 0.1.0-alpha.1
Language: en

## Capabilities

| Capability | Business step | 
|  --- | --- |
| menu.search | Search the menu | 
| availability.check | Check availability | 
| reservation.create | Create a reservation | 
| order.create | Create an order | 
| payment.request | Request payment | 



REST and MCP use the same contracts and BusinessRuntime. The reference uses mock Connectors without an LLM provider or real payment SDK dependency.

## Get and run

```
git clone https://github.com/brivya/brivya.git
cd brivya
npm install --ignore-scripts --no-audit --no-fund
npm run ci
```



The current repository has no committed lockfile, so use the same npm install approach as CI. The root command builds, typechecks and tests, including the Restaurant RST-001..RST-024 contract matrix.

## Run reference tests only

```
npm run build
node --test examples/restaurant/dist/test/*.test.js
```



Build all workspaces first to prepare cross-package dependencies. Then run the compiled reference suite, covering execution, safety rejection and audit behavior with deterministic data.

## Reading path

- `examples/restaurant/src/manifest.ts`: business identity and capability declarations.
- `examples/restaurant/src/capabilities.ts`: capability definitions.
- `examples/restaurant/test/`: end-to-end evidence.
- `connectors/mock/`: mock business integration.



payment.request is a business payment request, not a connection to a real payment channel. The bootstrap URL is example identity, not a hosted live demo.

