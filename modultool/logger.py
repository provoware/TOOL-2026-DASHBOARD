import logging
import os
from .config import get_log_dir

LOG_DIR = get_log_dir()
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "modultool.log"
LOG_LEVEL = os.getenv("MODULTOOL_LOG_LEVEL", "INFO").upper()


def _get_log_level() -> int:
    """Return numeric log level from environment variable."""
    name = os.getenv("MODULTOOL_LOG_LEVEL", "INFO").upper()
    return getattr(logging, name, logging.INFO)


def get_logger() -> logging.Logger:
    """Return the application logger, creating it if needed."""
    logger = logging.getLogger("modultool")
    logger.setLevel(_get_log_level())
    if not logger.handlers:
        logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
        fmt = "%(asctime)s [%(levelname)s] %(message)s"
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt)
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        logger.propagate = False
        logger.info("Logger initialisiert")
    return logger


logger = get_logger()
