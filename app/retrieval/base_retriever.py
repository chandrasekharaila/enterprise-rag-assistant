from abc import ABC, abstractmethod
from app.schemas.chunk import Chunk

class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str, top_k: int = 5) -> list[Chunk]:
        pass