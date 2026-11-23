"""bf16.ai model provider plugin for Hermes Agent.

bf16.ai serves uncensored open-weight models (refusal behavior removed from the
weights rather than papered over with a system prompt) over an OpenAI-compatible
API at https://api.bf16.ai/v1, with 1M context windows, vision, structured tool
calling, and prepaid USD billing.

The live model list is fetched from GET https://api.bf16.ai/v1/models (public,
no key required); fallback_models is used when that call is unreachable.
"""

from providers import register_provider
from providers.base import ProviderProfile

# Context windows and capabilities published by GET https://api.bf16.ai/v1/models.
_MODEL_SPECS: dict[str, dict[str, object]] = {
    "deepseek/deepseek-v4.1-flash-uncensored": {
        "supports_tools": True,
        "supports_vision": True,
        "context_window": 1_048_576,
    },
    "deepseek/deepseek-v4.1-flash-uncensored-fast": {
        "supports_tools": True,
        "supports_vision": True,
        "context_window": 1_048_576,
    },
    "zai-org/glm-5.3-uncensored": {
        "supports_tools": True,
        "supports_vision": False,
        "context_window": 1_048_576,
    },
    "zai-org/glm-5.3-flash-uncensored": {
        "supports_tools": True,
        "supports_vision": True,
        "context_window": 1_048_576,
    },
    "moonshotai/kimi-k3.1-pro-uncensored": {
        "supports_tools": True,
        "supports_vision": True,
        "context_window": 1_048_576,
    },
    "bf16/deepseek-v4.1-flash-1017-exl3-2.5bpw": {
        "supports_tools": True,
        "supports_vision": True,
        "context_window": 524_288,
    },
    "bf16/auto": {
        "supports_tools": True,
        "supports_vision": True,
        "context_window": 1_048_576,
    },
    "bf16/auto:fast": {
        "supports_tools": True,
        "supports_vision": True,
        "context_window": 1_048_576,
    },
    "bf16/auto:coding": {
        "supports_tools": True,
        "supports_vision": False,
        "context_window": 1_048_576,
    },
    "bf16/auto:reasoning": {
        "supports_tools": True,
        "supports_vision": False,
        "context_window": 1_048_576,
    },
}

bf16_provider = ProviderProfile(
    name="bf16",
    aliases=("bf16.ai", "bf16-ai"),
    display_name="bf16.ai",
    description=(
        "bf16.ai: uncensored open-weight models (DeepSeek V4.1 Flash, GLM-5.3, "
        "Kimi K3.1 Pro, bf16 Auto) with 1M context, tool calling, and low refusal rates"
    ),
    signup_url="https://bf16.ai/dashboard/keys",
    env_vars=("BF16_API_KEY", "BF16_BASE_URL"),
    base_url="https://api.bf16.ai/v1",
    auth_type="api_key",
    default_aux_model="deepseek/deepseek-v4.1-flash-uncensored",
    fallback_models=tuple(_MODEL_SPECS),
    model_capabilities=_MODEL_SPECS,
)

register_provider(bf16_provider)
