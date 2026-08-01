from abc import ABC, abstractmethod
from app.schemas.chunk import Chunk
from app.schemas.embedding import Embedding
from app.vectorstore.search_result import SearchResult


class BaseVectorStore(ABC):

    @abstractmethod
    def create_collection(self):
        pass

    @abstractmethod
    def add_embeddings(self, embeddings: list[Embedding]):
        pass

    @abstractmethod
    def search(self,query_vector: list[float], limit: int = 5) -> list[SearchResult]:
        pass