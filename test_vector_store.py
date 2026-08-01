from app.embeddings.embedding_pipeline import EmbeddingPipeline
from app.ingestion.loader_factory import LoaderFactory
from app.processing.chunk_pipeline import ChunkPipeline
from app.vectorstore.vector_pipeline import VectorPipeline


loader = LoaderFactory.get_loader("data/sample.pdf")
document = loader.load()

chunks = ChunkPipeline().process(document)

embeddings = EmbeddingPipeline().process(chunks)

pipeline = VectorPipeline()

pipeline.process(embeddings)

print("Vectors successfully stored in Qdrant!")