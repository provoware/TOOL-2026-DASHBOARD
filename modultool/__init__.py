from .logger import logger
from .selfcheck import run_selfcheck

run_selfcheck()

__all__ = ["logger", "run_selfcheck"]
