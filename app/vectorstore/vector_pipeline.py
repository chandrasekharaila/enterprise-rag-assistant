from app.schemas.embedding import Embedding
from app.vectorstore.qdrant_store import QdrantStore


class VectorPipeline:

    def __init__(self):

        self.store = QdrantStore()

        self.store.create_collection()

    def process(
        self,
        embeddings: list[Embedding],
    ):

        self.store.add_embeddings(embeddings)