from app.llm.base_llm import BaseLLM
from app.core.config import settings
from openai import OpenAI


class OpenaAILLM(BaseLLM):
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate(self, prompt:str) ->str:
        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=[{
                'role': "user",
                "content": prompt
            }],
            temperature = settings.TEMPERATURE,
            max_completion_tokens= settings.MAX_TOKENS
        )

        return response.choices[0].message.content