from app.embeddings.embedding_pipeline import EmbeddingPipeline
from app.ingestion.loader_factory import LoaderFactory
from app.processing.chunk_pipeline import ChunkPipeline
from dotenv import load_dotenv
from app.core.config import settings

load_dotenv()

loader = LoaderFactory.get_loader("data/sample.pdf")

document = loader.load()

chunk_pipeline = ChunkPipeline()

chunks = chunk_pipeline.process(document)

embedding_pipeline = EmbeddingPipeline()

embeddings = embedding_pipeline.process(chunks)

print("=" * 80)

print(f"Total Embeddings : {len(embeddings)}")

print("=" * 80)

print("Vector Dimension :", len(embeddings[0].vector))

print("=" * 80)

print(embeddings[0].vector[:20])