from modelgauge.secret_values import InjectSecret
from modelgauge.sut_registry import SUTS
from modelgauge.suts.huggingface_client import HuggingFaceToken, HuggingFaceSUT

SUTS.register(HuggingFaceSUT, "openai-gpt", "openai-gpt", InjectSecret(HuggingFaceToken))