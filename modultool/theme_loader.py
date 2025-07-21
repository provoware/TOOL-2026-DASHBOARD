from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import QApplication

from . import config
from .logger import logger


def get_theme_path(name: str) -> Path:
    """Return path to the given theme stylesheet."""
    return config.get_theme_dir() / f"{name}.qss"


def apply_theme(app: QApplication, name: str = "dark") -> None:
    """Load stylesheet and apply it to the application."""
    path = get_theme_path(name)
    try:
        style = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.warning("theme file not found: %s", path)
        return
    app.setStyleSheet(style)
    logger.info("theme applied: %s", name)
