from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from .config import get_data_dir, get_root_dir
from .logger import logger


class BackupManager:
    """Create manual backups of the data directory."""

    def __init__(self, keep: int = 3) -> None:
        self.keep = keep

    def create_backup(self) -> Path:
        src = get_data_dir()
        backups_dir = get_root_dir() / "backups"
        backups_dir.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = backups_dir / f"data_{stamp}"
        shutil.copytree(src, dest)
        self._cleanup_old(backups_dir)
        logger.info("backup: %s created", dest.name)
        return dest

    def _cleanup_old(self, backups_dir: Path) -> None:
        backups = sorted(p for p in backups_dir.glob("data_*") if p.is_dir())
        while len(backups) > self.keep:
            old = backups.pop(0)
            shutil.rmtree(old, ignore_errors=True)
            logger.info("backup removed: %s", old.name)

backup = BackupManager()
