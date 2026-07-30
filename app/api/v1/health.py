from fastapi import APIRouter

from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/health")
async def health():

    logger.info("Health endpoint accessed.")

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }