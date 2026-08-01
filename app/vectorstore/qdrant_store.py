import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from app.core.config import settings
from app.schemas.chunk import Chunk
from app.schemas.embedding import Embedding
from app.vectorstore.base_vector_store import BaseVectorStore
from app.vectorstore.search_result import SearchResult
from app.vectorstore.collection_manager import CollectionManager

class QdrantStore(BaseVectorStore):

    def __init__(self):
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )

    def create_collection(self):
        CollectionManager().create()

    def add_embeddings(self, embeddings):
        points = []

        for embedding in embeddings:
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding.vector,
                    payload={
                        "content": embedding.chunk.content,
                        "metadata": embedding.chunk.metadata
                    }
                )
            )
        self.client.upsert(
            collection_name=settings.QDRANT_COLLECTION,
            points=points
        )

    def search(self, query_vector: list[float], limit: int = 5) -> list[SearchResult]:
        response = self.client.query_points(
            collection_name=settings.QDRANT_COLLECTION,
            query=query_vector,
            limit=limit
        )

        # Handle tuple unpacking if query_points returns (points, offset) or QueryResponse
        hits = response[0] if isinstance(response, tuple) else response.points

        results = []

        for hit in hits:
            chunk = Chunk(
                id=str(hit.id),
                content=hit.payload["content"],
                metadata=hit.payload.get("metadata", {})
            )

            results.append(
                SearchResult(
                    chunk=chunk,
                    score=hit.score
                )
            )
        return results