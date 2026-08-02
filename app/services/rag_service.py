from app.llm.llm_factory import LLMFactory
from app.llm.prompt_builder import PromptBuilder
from app.retrieval.retrieval_pipeline import RetrievalPipeline
from app.schemas.rag_response import RAGResponse

class RAGServcie:

    def __init__(self):
        self.retriver = RetrievalPipeline()
        self.llm = LLMFactory.get_llm()

    def ask(self, question: str) -> RAGResponse:
        chunks = self.retriver.process(query=question)

        prompt = PromptBuilder.build(question=question,chunks=chunks)

        answer = self.llm.generate(prompt=prompt)

        sources = []

        for chunk in chunks:
            sources.append(chunk.metadata.get("source"))

        return RAGResponse(
            answer=answer,
            sources=sources,
            retrieved_chunks=chunks
        )