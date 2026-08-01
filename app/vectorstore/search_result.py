from pydantic import BaseModel
from app.schemas.chunk import Chunk

class SearchResult(BaseModel):
    chunk: Chunk
    score: float