from app.services.rag_service import RAGServcie


rag = RAGServcie()

response = rag.ask(
    "What machine learning projects has chandra sekhar built?"
)

print("=" * 80)

print(response.answer)

print("=" * 80)

print(response.sources)

print("=" * 80)

for chunk in response.retrieved_chunks:

    print(chunk.metadata)