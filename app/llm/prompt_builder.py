from app.schemas.chunk import Chunk

class PromptBuilder:
    @staticmethod
    def build(question:str , chunks: list[Chunk]) -> str:
        context = "\n\n".join(chunk.content for chunk in chunks)
        prompt = f"""
                    You are an AI assistant.

                    Answer ONLY using the provided context.

                    If the answer is not available,
                    say you don't know.

                    Context
                    ------------------------

                    {context}

                    ------------------------

                    Question:

                    {question} """
        return prompt
