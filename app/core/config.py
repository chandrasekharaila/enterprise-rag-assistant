from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    HOST: str
    PORT: int
    LOG_LEVEL: str

    GEMINI_API_KEY: str = ""
    QDRANT_API_KEY: str = ""
    QDRANT_URL: str = ""

    MODEL_NAME: str
    EMBEDDING_MODEL: str  # Fixed typo and removed duplicate

    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()