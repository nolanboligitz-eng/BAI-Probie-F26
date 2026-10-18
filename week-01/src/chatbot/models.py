"""
Data Models Module

This module defines the data structures used throughout the chatbot application.
We use Pydantic models to ensure all data is valid and type-safe.

Key Concepts:
- Pydantic models: Classes that automatically validate data
- Immutability: Data that can't be changed after creation (safer!)
- Type hints: Declaring what type each field should be
- Literal types: Restrict a field to specific allowed values

Why use models?
- Catch errors early (before sending bad data to OpenAI)
- Self-documenting code (clear what data looks like)
- IDE support (autocomplete and type checking)
- Type safety: Prevent invalid data from being created
"""

from typing import Literal

from pydantic import BaseModel


# TODO: Create a ChatMessage Pydantic model
# This model represents a single message in the conversation.
# Each message has a "role" (who sent it) and "content" (what they said).
#
# The OpenAI API expects messages in this exact format:
# {"role": "user", "content": "Hello!"}
# {"role": "assistant", "content": "Hi there!"}
# {"role": "system", "content": "You are a helpful assistant."}
#
# Important: The role field should ONLY accept specific values!
# We use Literal to restrict role to exactly: "user", "assistant", or "system"
#
class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str
