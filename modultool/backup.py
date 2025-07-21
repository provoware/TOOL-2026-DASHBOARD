from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from .config import get_data_dir, get_root_dir
from .logger import logger


class BackupManager:
    """Create manual backups of the data directory."""

    def create_backup(self) -> Path:
        src = get_data_dir()
        backups_dir = get_root_dir() / "backups"
        backups_dir.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = backups_dir / f"data_{stamp}"
        shutil.copytree(src, dest)
        logger.info("backup: %s created", dest.name)
        return dest


backup = BackupManager()
