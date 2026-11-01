from dataclasses import dataclass
from typing import Any, Dict, Optional

import chromadb
import asyncio
import uuid

from src.services.embedding.service import EmbeddingService


@dataclass
class VectorDatabaseService:
    """Service for storing and retrieving text embeddings in ChromaDB."""

    embedding_service: Optional[EmbeddingService] = None
    vector_db_client: Optional[chromadb.PersistentClient] = None
    vector_db_collection: Optional[chromadb.Collection] = None
    collection_name: str = "bai_probie_vector_database"
    persist_directory: str = "vector_db_instance"

    def __post_init__(self):
        if self.vector_db_client is None:
            self.vector_db_client = chromadb.PersistentClient(
                path=self.persist_directory
            )

        if self.vector_db_collection is None:
            self.vector_db_collection = self.vector_db_client.get_or_create_collection(
                name=self.collection_name
            )
        if self.embedding_service is None:
            self.embedding_service = EmbeddingService()

    async def add_fact(self, text: str) -> str:
        """
        TODO: Add a fact to the vector database.

        Requirements:
        - Generate an id (use uuid.uuid4()) for the document
        - Call self.embedding_service.generate_embedding(text)
        - Add to `self.vector_db_collection` with ids, documents, embeddings
        - Return the generated id as a string
        """
        fact_id = str(uuid.uuid4())

        embedding = await self.embedding_service.generate_embedding(text)

        await asyncio.to_thread(
            self.vector_db_collection.add,
            ids=[fact_id],
            documents=[text],
            embeddings=[embedding],
        )

        return fact_id

    async def query(self, query_text: str, n_results: int = 10) -> Dict[str, Any]:
        embedding = await self.embedding_service.generate_embedding(query_text)

        results = await asyncio.to_thread(
            self.vector_db_collection.query,
            query_embeddings=[embedding],
            n_results=n_results,
            include=["documents", "distances"],
        )

        return results

    async def format_query_results(self, query_result: chromadb.QueryResult) -> str:
        documents = query_result.get("documents") or []

        if not documents or not documents[0]:
            return "No relevant documents found."

        formatted = "Relevant documents from the knowledge base:\n\n"

        for index, doc in enumerate(documents[0], start=1):
            formatted += f"<fact_{index}>\n{doc}\n</fact_{index}>\n\n"

        return formatted.strip()

    def clear(self) -> None:
        """Delete all facts from the vector database."""
        self.vector_db_client.delete_collection(name=self.collection_name)
        self.vector_db_collection = self.vector_db_client.create_collection(
            name=self.collection_name
        )
