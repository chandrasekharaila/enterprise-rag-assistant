from app.llm.openai_llm import OpenaAILLM

class LLMFactory:

    @staticmethod
    def get_llm():
        return OpenaAILLM()