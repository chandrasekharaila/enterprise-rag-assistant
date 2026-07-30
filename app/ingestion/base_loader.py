from abc import ABC, abstractmethod
from pathlib import Path

from app.schemas.document import Document


class BaseLoader(ABC):

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    @abstractmethod
    def load(self) -> Document:
        pass