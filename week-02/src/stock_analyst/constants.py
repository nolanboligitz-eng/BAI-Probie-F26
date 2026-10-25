"""
Constants Module

This module contains application-level constants that define the stock analyst's
behavior. These values are hard-coded because they're part of the application
logic, not environment-specific configuration.

Key Concepts:
- Constants: Values that don't change during execution
- Hard-coding: Putting values directly in code (appropriate for non-secrets)
- Type annotations: UPPER_CASE names indicate these are constants

The difference between constants and environment variables:
- Environment variables (.env): Secrets and deployment-specific values (API keys)
- Constants (this file): Application behavior that's the same everywhere (prompts, stock symbols)
"""

from typing import Literal

# Valid OpenAI models for chat completions
# Using Literal type to enforce type checking at development time
ValidModel = Literal[
    "gpt-4o-mini",
    "gpt-4o",
    "gpt-4-turbo",
]

# The OpenAI model to use for chat completions
# gpt-4o-mini is recommended: fast, capable, and cost-effective
DEFAULT_MODEL: ValidModel = "gpt-4o-mini"

# Popular stock symbols for examples
# These are well-known companies that students will recognize
EXAMPLE_STOCKS = [
    "AAPL",  # Apple Inc.
    "GOOGL", # Alphabet Inc. (Google)
    "MSFT",  # Microsoft Corporation
    "TSLA",  # Tesla, Inc.
    "AMZN",  # Amazon.com, Inc.
    "META",  # Meta Platforms, Inc. (Facebook)
    "NVDA",  # NVIDIA Corporation
    "NFLX",  # Netflix, Inc.
]

# System prompt for the Data Agent
# This agent is responsible for fetching and validating stock data
DATA_AGENT_PROMPT = """You are a data retrieval specialist for stock market analysis.

Your role is to:
- Fetch accurate stock market data using the available tools
- Validate that the data is complete and reasonable
- Handle errors gracefully if a stock symbol is invalid
- Provide clear, concise responses about the data you've retrieved

Always use the tools provided to you. Never make up stock prices or data."""

# System prompt for the Analysis Agent
# This agent performs technical analysis on stock data
ANALYSIS_AGENT_PROMPT = """You are a technical analysis expert for stock market data.

Your role is to:
- Analyze stock price trends and patterns
- Identify support and resistance levels based on recent price history
- Determine if the trend is bullish (upward), bearish (downward), or neutral
- Calculate technical indicators like moving averages
- Provide objective, data-driven analysis

Focus on clear, beginner-friendly explanations. Avoid jargon when possible, and
explain technical terms when you must use them."""

# System prompt for the Research Agent
# This agent generates insights and recommendations
RESEARCH_AGENT_PROMPT = """You are a friendly stock market research analyst helping students learn about investing.

Your role is to:
- Generate clear, educational insights about stocks
- Explain what the technical analysis means in simple terms
- Provide balanced, educational perspectives (not financial advice!)
- Help beginners understand market concepts
- Be encouraging and supportive

IMPORTANT: Always include a disclaimer that this is for educational purposes only,
not financial advice. Encourage students to do their own research and consult
with financial professionals before making investment decisions.

Keep your tone friendly, educational, and accessible to first-year college students."""

# Time periods for stock data
# These define how far back to look when fetching historical data
VALID_PERIODS = Literal["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"]
DEFAULT_PERIOD: str = "3mo"  # Default to 1 month of data

