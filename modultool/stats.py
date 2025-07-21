from __future__ import annotations

import json
from pathlib import Path

from .config import get_data_dir
from .error_handler import load_json
from .event_bus import event_bus
from .logger import logger


class StatsManager:
    """Collect simple statistics about module usage."""

    def __init__(self, path: Path | None = None) -> None:
        self.file = path or get_data_dir() / "stats.json"
        self.stats: dict[str, int] = load_json(self.file, {})
        event_bus.subscribe("module.open", self.record_open)

    def record_open(self, module: str) -> None:
        """Increase counter for the given module name."""
        self.stats[module] = self.stats.get(module, 0) + 1
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(self.stats, f, indent=2, ensure_ascii=False)
        logger.info("stats recorded: %s -> %s", module, self.stats[module])

    def get_stats(self) -> dict[str, int]:
        """Return a copy of the stats dictionary."""
        return dict(self.stats)


stats = StatsManager()
