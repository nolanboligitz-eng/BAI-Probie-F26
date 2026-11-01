from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from src.settings import settings

llm = OpenAIChatModel(
    settings.OPENAI_MODEL,
    provider=OpenAIProvider(api_key=settings.OPENAI_API_KEY),
)
