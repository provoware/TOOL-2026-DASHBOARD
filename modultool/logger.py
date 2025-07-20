import logging
from pathlib import Path
from .config import get_log_dir

LOG_DIR = get_log_dir()
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "modultool.log"


def get_logger() -> logging.Logger:
    """Return the application logger, creating it if needed."""
    logger = logging.getLogger("modultool")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
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
