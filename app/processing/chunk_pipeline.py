from app.processing.recursive_chunker import RecursiveChunker
from app.schemas.chunk import Chunk
from app.schemas.document import Document

class ChunkPipeline:

    def __init__(self):
        self.chunker = RecursiveChunker()

    def process(self,document: Document) ->list[Chunk]:
        return self.chunker.split(document)