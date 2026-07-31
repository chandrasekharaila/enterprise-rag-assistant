from pydantic import BaseModel,Field
from app.schemas.chunk import Chunk

class Embedding(BaseModel):
    """
    Represents a vector embedding
    """

    chunk: Chunk
    vector: list[float] = Field(default_factory=list)