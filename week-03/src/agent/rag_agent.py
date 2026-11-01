from dataclasses import dataclass

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

from src.agent.llm import llm
from src.agent.system_prompt import RAG_AGENT_SYSTEM_PROMPT
from src.services.embedding.service import EmbeddingService
from src.services.vector_database.service import VectorDatabaseService


class RAGAgentOutput(BaseModel):
    answer: str
    sources: list[str] = Field(
        description="The sources used to answer the question (VERBATIM)"
    )


@dataclass
class RAGAgentDependencies:
    vector_db: VectorDatabaseService
    embedder: EmbeddingService


rag_agent = Agent(
    model=llm,
    output_type=RAGAgentOutput,
    retries=2,
    deps_type=RAGAgentDependencies,
    system_prompt=RAG_AGENT_SYSTEM_PROMPT,
)


@rag_agent.tool
async def perform_rag(context: RunContext[RAGAgentDependencies], query: str) -> str:
    """
    TODO: Implement RAG retrieval.

    Requirements:
    - Call `context.deps.vector_db.query(query)` to retrieve similar documents
    - Format with `context.deps.vector_db.format_query_results(...)`
    - Return the formatted string
    - Call this tool at most once per agent run
    """
    results = await context.deps.vector_db.query(query)
    formatted = await context.deps.vector_db.format_query_results(results)
    return formatted


async def run_rag_agent(query: str) -> RAGAgentOutput:
    """Run the RAG agent to answer the user's question"""
    return await rag_agent.run(query)
