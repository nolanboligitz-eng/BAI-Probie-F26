from dataclasses import dataclass

import httpx

from src.settings import settings


@dataclass
class EmbeddingService:
    """Service for generating text embeddings using OpenRouter."""

    async def generate_embedding(self, text: str) -> list[float]:
        """
        This function generates an embedding for a given string of text.
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/embeddings",
                headers={
                    "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={"model": settings.OPENAI_EMBEDDING_MODEL, "input": text},
            )
            response.raise_for_status()
            data = response.json()
            return data["data"][0]["embedding"]
