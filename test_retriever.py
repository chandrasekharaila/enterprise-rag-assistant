from app.retrieval.retrieval_pipeline import RetrievalPipeline

retriver = RetrievalPipeline()

results = retriver.process(query="What machine learning projects has chandra built?",top_k=3)

print("="*80)

for index, chunk in enumerate(results, start=1):

    print(f"Result {index}")

    print("-" * 80)

    print(chunk.content)

    print(chunk.metadata)

    print("=" * 80)