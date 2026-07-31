from pydantic import BaseModel, Field

class Chunk(BaseModel):
    """
        represents a single text chunk
    """

    id: int
    content: str
    metadata: dict = Field(default_factory=dict)