from app.embeddings.embedding_factory import EmbedderFactory
from app.schemas.chunk import Chunk
from app.schemas.embedding import Embedding

class EmbeddingPipeline:
    def __init__(self):
        self.embedder = EmbedderFactory.get_embedder()

    def process(self, chunks: list[Chunk]) -> list[Embedding]:
        return self.embedder.batch_embed(chunks)