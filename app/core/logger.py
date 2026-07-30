import logging
import os

from app.core.config import settings

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name: str):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        os.path.join(LOG_DIR, "app.log")
    )

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger