from .logger import logger

__all__ = ["logger"]
from .selfcheck import run_selfcheck

run_selfcheck()

__all__ = ["logger", "run_selfcheck"]
