from pydantic import BaseModel
from app.schemas.chunk import Chunk
class RAGResponse(BaseModel):
    answer: str
    sources : list[str]
    retrieved_chunks: list[Chunk]
