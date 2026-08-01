from app.llm.llm_factory import LLMFactory
from app.llm.prompt_builder import PromptBuilder
from app.retrieval.retrieval_pipeline import RetrievalPipeline


class RAGPipeline:

    def __init__(self):

        self.retriever = RetrievalPipeline()

        self.llm = LLMFactory.get_llm()

    def ask(
        self,
        question: str,
    ) -> str:

        chunks = self.retriever.process(question)

        prompt = PromptBuilder.build(
            question,
            chunks,
        )

        return self.llm.generate(prompt)