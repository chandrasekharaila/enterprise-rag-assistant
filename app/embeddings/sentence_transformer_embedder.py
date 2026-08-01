from sentence_transformers import SentenceTransformer

from app.embeddings.base_embedder import BaseEmdder
from app.schemas.embedding import Embedding
from app.schemas.chunk import Chunk
from app.core.config import settings


model_name = settings.EMBEDDING_MODEL
class SentenceTransformerEmbedder(BaseEmdder):
    def __init__(self,model_name:str = model_name):
        self.model_name = model_name
        self.embedder = SentenceTransformer(self.model_name)

    def embed(self, chunk: Chunk):
        text = chunk.content
        vector = self.embedder.encode(text,convert_to_numpy=True).tolist()
        return Embedding(
            chunk=chunk,
            vector=vector
        )
    def embed_text(self,query)->list[float]:

        vector = self.embedder.encode(query,convert_to_numpy=True)
        return vector.tolist()
    
    def batch_embed(self, chunks: list[Chunk]) -> list[Embedding]:
        texts = [chunk.content for chunk in chunks]
        vectors = self.embedder.encode(texts,convert_to_numpy=True)
        embeddings = []
        for chunk, vector in zip(chunks,vectors):
            embeddings.append(
                Embedding(
                    chunk=chunk,
                    vector=vector.tolist()
                )
            )
        return embeddings
