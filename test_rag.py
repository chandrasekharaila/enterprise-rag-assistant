from app.llm.rag_pipeline import RAGPipeline

rag = RAGPipeline()

answer = rag.ask(
    "What machine learning projects has chandra sekhar aila built?"
)

print(answer)