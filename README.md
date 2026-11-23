# bf16.ai Model Provider for Hermes Agent

Official Hermes Agent model-provider plugin for [bf16.ai](https://bf16.ai).

## Why bf16.ai for autonomous agents

bf16.ai serves **uncensored open-weight models** (refusal behavior edited out of the weights, not papered over with system prompts) over a standard OpenAI-compatible API (`https://api.bf16.ai/v1`).

For long-running autonomous Hermes workflows — security code audits, log triage, shell/browser automation, and multi-step tool loops — eliminating false-positive safety refusals keeps tool chains completing end-to-end while your local Hermes permissions and sandboxes govern execution.

### Highlighted models

- `deepseek/deepseek-v4.1-flash-uncensored` (default) — 1M context, vision, reasoning, tool calling
- `deepseek/deepseek-v4.1-flash-uncensored-fast` — 1M context, vision, low-latency tool loops
- `zai-org/glm-5.3-uncensored` — 1M context flagship coding & analysis
- `zai-org/glm-5.3-flash-uncensored` — 1M context multimodal fast model
- `moonshotai/kimi-k3.1-pro-uncensored` — 1M context 2.8T multimodal flagship
- `bf16/auto`, `bf16/auto:fast`, `bf16/auto:coding`, `bf16/auto:reasoning` — smart routers

## Installation & Usage

```bash
hermes plugins install bf16-provider
export BF16_API_KEY="sk-bf16-v1-..."
hermes --provider bf16 -m deepseek/deepseek-v4.1-flash-uncensored
```

Get an API key at [bf16.ai/dashboard/keys](https://bf16.ai/dashboard/keys).

## Disclosure

- **Network:** Prompts, tool schemas, and responses go to `https://api.bf16.ai/v1` (or `BF16_BASE_URL` if set). Model discovery uses the public `GET https://api.bf16.ai/v1/models` endpoint.
- **Credentials:** `BF16_API_KEY` is read by Hermes through its standard provider credential path; this plugin never reads, writes, or logs credentials.
- **Privacy & billing:** Prepaid per token (free starter credit upon email verification). Zero prompt storage ([bf16.ai/legal/privacy](https://bf16.ai/legal/privacy)).
- No tools, hooks, middleware, shell commands, background processes, or telemetry.
