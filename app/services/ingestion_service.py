from app.embeddings.embedding_pipeline import EmbeddingPipeline
from app.ingestion.loader_factory import LoaderFactory
from app.processing.chunk_pipeline import ChunkPipeline
from app.vectorstore.vector_pipeline import VectorPipeline

class IngestionService:

    def ingest(self,file_path:str):

        loader = LoaderFactory.get_loader(file_path)

        document = loader.load()

        chunks = ChunkPipeline().process(document)

        embeddings = EmbeddingPipeline().process(chunks)

        VectorPipeline().process(embeddings)