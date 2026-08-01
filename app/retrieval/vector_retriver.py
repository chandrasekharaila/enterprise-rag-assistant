from app.embeddings.embedding_factory import EmbedderFactory
from app.retrieval.base_retriever import BaseRetriever
from app.schemas.chunk import Chunk
from app.vectorstore.qdrant_store import QdrantStore

class VectorRetriever(BaseRetriever):
    def __init__(self):
        self.embedder = EmbedderFactory.get_embedder()
        self.vector_store = QdrantStore()

    def retrieve(self, query:str, top_k:int = 5) -> list[Chunk]:
        query_vector = self.embedder.embed_text(query)

        results = self.vector_store.search(
            query_vector=query_vector,
            limit=top_k
        )

        return [result.chunk for result in results]