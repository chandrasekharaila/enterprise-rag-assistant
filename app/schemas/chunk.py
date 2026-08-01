from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional,Union
class Chunk(BaseModel):
    """
        represents a single text chunk
    """

    id: Optional[Union[str,int,UUID]] = None
    content: str
    metadata: dict = Field(default_factory=dict)