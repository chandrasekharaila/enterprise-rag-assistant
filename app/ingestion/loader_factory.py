from pathlib import Path

from app.ingestion.docx_loader import DOCXLoader
from app.ingestion.pdf_loader import PDFLoader
from app.ingestion.txt_loader import TXTLoader


class LoaderFactory:

    LOADERS = {
        ".pdf": PDFLoader,
        ".docx": DOCXLoader,
        ".txt": TXTLoader,
    }

    @classmethod
    def get_loader(cls, file_path: str):

        extension = Path(file_path).suffix.lower()

        loader = cls.LOADERS.get(extension)

        if loader is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loader(file_path)