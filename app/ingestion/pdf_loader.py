import fitz

from app.ingestion.base_loader import BaseLoader
from app.schemas.document import Document


class PDFLoader(BaseLoader):

    def load(self) -> Document:

        pdf = fitz.open(self.file_path)

        pages = []

        for page in pdf:
            pages.append(page.get_text())

        content = "\n".join(pages)

        metadata = {
            "source": self.file_path.name,
            "type": "pdf",
            "pages": len(pdf),
        }

        pdf.close()

        return Document(
            content=content,
            metadata=metadata,
        )