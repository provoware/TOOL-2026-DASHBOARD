from __future__ import annotations

import shutil

from .config import get_data_dir
from .logger import logger
from .selfcheck import run_selfcheck


class ResetManager:
    """Remove user data and recreate default files."""

    def reset(self) -> None:
        data_dir = get_data_dir()
        for item in data_dir.iterdir():
            if item.name == "themes":
                continue
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
            else:
                item.unlink(missing_ok=True)
        run_selfcheck()
        logger.info("factory reset executed")


reset_manager = ResetManager()


if __name__ == "__main__":
    reset_manager.reset()
