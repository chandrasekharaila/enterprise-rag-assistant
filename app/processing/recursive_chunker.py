from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.processing.base_chunker import BaseChunker
from app.processing.text_cleaner import TextCleaner
from app.schemas.chunk import Chunk
from app.schemas.document import Document


class RecursiveChunker(BaseChunker):

    def __init__(self, chunk_size:int = 500, chunk_overlap=100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.spltter = RecursiveCharacterTextSplitter(chunk_size= chunk_size, chunk_overlap=chunk_overlap)

    def split(self, document):
        cleaned_text = TextCleaner.clean(document.content)
        texts = self.spltter.split_text(cleaned_text)
        chunks = []

        for index,text in enumerate(texts):
            metadata = document.metadata.copy()
            metadata["chunk_id"] = index
            chunks.append(
                Chunk(
                    id=index,
                    content=text,
                    metadata=metadata
                )
            )
        return chunks
