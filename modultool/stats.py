from __future__ import annotations

import json
from pathlib import Path

from .config import get_data_dir
from .error_handler import load_json
from .event_bus import event_bus
from .logger import logger


class StatsManager:
    """Collect simple statistics about module usage and errors."""

    def __init__(self, path: Path | None = None) -> None:
        self.file = path or get_data_dir() / "stats.json"
        data = load_json(self.file, {"modules": {}, "errors": 0})

        if "modules" not in data:
            # fallback for old flat format
            data = {"modules": data if isinstance(data, dict) else {}, "errors": 0}

        self.modules: dict[str, int] = data.get("modules", {})
        self.error_count: int = data.get("errors", 0)

        event_bus.subscribe("module.open", self.record_open)
        event_bus.subscribe("error.occurred", self.record_error)

    def _save(self) -> None:
        try:
            with self.file.open("w", encoding="utf-8") as f:
                json.dump(
                    {"modules": self.modules, "errors": self.error_count},
                    f,
                    indent=2,
                    ensure_ascii=False,
                )
        except OSError as err:
            logger.error("Speichern fehlgeschlagen: %s", err)

    def record_open(self, module: str) -> None:
        """Increase counter for the given module name."""
        self.modules[module] = self.modules.get(module, 0) + 1
        self._save()
        logger.info("stats recorded: %s -> %s", module, self.modules[module])

    def record_error(self) -> None:
        """Increase the global error counter."""
        self.error_count += 1
        self._save()
        logger.info("error recorded: %s", self.error_count)

    def get_stats(self) -> dict[str, int]:
        """Return a copy of the module stats dictionary."""
        return dict(self.modules)

    def get_error_count(self) -> int:
        """Return total number of recorded errors."""
        return self.error_count

    def get_most_used_module(self) -> str | None:
        """Return the module with the highest usage count if available."""
        if not self.modules:
            return None
        return max(self.modules.items(), key=lambda item: item[1])[0]


stats = StatsManager()
