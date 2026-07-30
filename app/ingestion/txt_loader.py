from app.ingestion.base_loader import BaseLoader
from app.schemas.document import Document


class TXTLoader(BaseLoader):

    def load(self) -> Document:

        with open(
            self.file_path,
            "r",
            encoding="utf-8",
        ) as file:

            content = file.read()

        metadata = {
            "source": self.file_path.name,
            "type": "txt",
        }

        return Document(
            content=content,
            metadata=metadata,
        )