from __future__ import annotations

import json
from pathlib import Path

from .logger import logger


def load_json(path: Path, default) -> object:
    """Return JSON data or create file with default content if missing."""
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        path.write_text(
            json.dumps(default, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        logger.info("error handler: %s created with default", path.name)
        return default
