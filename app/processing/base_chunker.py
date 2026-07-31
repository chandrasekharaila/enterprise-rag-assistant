from abc import abstractmethod,ABC
from app.schemas.chunk import Chunk
from app.schemas.document import Document

class BaseChunker(ABC):

    @abstractmethod
    def split(self, document: Document) -> list[Chunk]:
        pass