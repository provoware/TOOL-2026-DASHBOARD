from __future__ import annotations

import json
from pathlib import Path

from .config import get_data_dir
from .error_handler import load_json
from .logger import logger


class OrderManager:
    """Manage and persist the order of modules."""

    def __init__(self, path: Path | None = None):
        self.file = path or get_data_dir() / "module_order.json"
        self.order = load_json(self.file, [])

    def move(self, module: str, index: int) -> None:
        """Move a module to a new index and save the order."""
        if module in self.order:
            self.order.remove(module)
        self.order.insert(index, module)
        self.save()

    def save(self) -> None:
        with self.file.open("w", encoding="utf-8") as f:
            json.dump(self.order, f, indent=2, ensure_ascii=False)
        logger.info("order saved")

    def get_order(self) -> list[str]:
        """Return the current order list."""
        return list(self.order)


order_manager = OrderManager()
