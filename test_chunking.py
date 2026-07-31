from app.ingestion.loader_factory import LoaderFactory
from app.processing.chunk_pipeline import ChunkPipeline


loader = LoaderFactory.get_loader("data/sample.pdf")

document = loader.load()

pipeline = ChunkPipeline()

chunks = pipeline.process(document)

print("=" * 80)

print(f"Total Chunks : {len(chunks)}")

print("=" * 80)

for chunk in chunks:

    print(chunk.id)

    print(chunk.metadata)

    print(chunk.content[:200])

    print("-" * 80)