from abc import ABC, abstractmethod
from app.schemas.embedding import Embedding
from app.schemas.chunk import Chunk

class BaseEmdder(ABC):

    @abstractmethod
    def embed(self,chunk:Chunk)->Embedding:
        """
        Generate embedding for a single chunk
        """
        pass

    def embed_batch(self, chunks: list[Chunk]) -> list[Embedding]:
        """
        Generate embeddings for multiple chunks
        """
        pass