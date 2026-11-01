"""
Configuration Module

This module handles configuration and environment variables for the stock analyst.
We use Pydantic Settings to automatically load and validate environment variables
from a .env file, ensuring type safety and providing helpful error messages.

Key Concepts:
- Environment variables: Values stored outside your code (for security)
- Pydantic Settings: Automatic loading and validation of environment variables
- Type safety: Ensuring variables have the correct type before use
- Validation: Checking that values meet specific requirements

Best Practice:
- Environment variables (.env) should only contain SECRETS and deployment-specific values
- Application constants (like model names and prompts) belong in code, not .env
"""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

from src.utils.filesystem import get_project_root

ValidLLMModel = Literal["gpt-4o-mini"]


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    OPENAI_API_KEY: str
    OPENAI_MODEL: ValidLLMModel = "gpt-4o-mini"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Configuration for Pydantic Settings
    # This tells it to look for a .env file in the project root
    model_config = SettingsConfigDict(
        env_file=get_project_root() / ".env",
    )


# Create a singleton instance of the Settings class
# This instance will be imported and used throughout the application
settings = Settings()
