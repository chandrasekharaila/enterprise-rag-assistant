from app.retrieval.vector_retriver import VectorRetriever
from app.schemas.chunk import Chunk

class RetrievalPipeline:

    def __init__(self):
        self.retriever = VectorRetriever()

    def process(self, query: str, top_k: int = 5) -> list[Chunk]:
        return self.retriever.retrieve(query=query,top_k=top_k)