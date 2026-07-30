from pydantic import BaseModel, Field

class Document(BaseModel):
    content: str = Field(...,description="Extracted document test")
    metadata: dict = Field(
        default_factory=dict,
        description="Document metadata"
    )