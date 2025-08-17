from __future__ import annotations

from pathlib import Path
import re

from PySide6.QtWidgets import QApplication
import json

from . import config
from .logger import logger


def _hex_to_luminance(hex_color: str) -> float:
    """Convert a hex color (z.B. #ffffff) to relative luminance."""
    r, g, b = [int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4)]

    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(r), channel(g), channel(b))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast_ratio(bg: str, fg: str) -> float:
    """Return contrast ratio between two hex colors (ohne #)."""
    l1 = _hex_to_luminance(bg)
    l2 = _hex_to_luminance(fg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


def load_user_theme() -> str:
    """Return theme name stored in user config file."""
    cfg = config.get_user_config_file()
    if cfg.exists():
        try:
            data = json.loads(cfg.read_text(encoding="utf-8"))
            return data.get("theme", "dark")
        except json.JSONDecodeError:
            logger.warning("invalid config file: %s", cfg)
    return "dark"


def get_theme_path(name: str) -> Path:
    """Return path to the given theme stylesheet."""
    user_file = config.get_user_theme_dir() / f"{name}.qss"
    if user_file.exists():
        return user_file
    return config.get_theme_dir() / f"{name}.qss"


def apply_theme(app: QApplication, name: str = "dark") -> None:
    """Load stylesheet and apply it to the application."""
    path = get_theme_path(name)
    try:
        style = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.warning("theme file not found: %s", path)
        return
    match = re.search(
        r"background-color:\s*#([0-9a-fA-F]{6}).*?color:\s*#([0-9a-fA-F]{6})",
        style,
        re.DOTALL,
    )
    if match:
        ratio = _contrast_ratio(match.group(1), match.group(2))
        if ratio < 4.5:
            logger.warning("low contrast %.2f:1 in theme %s", ratio, name)
    app.setStyleSheet(style)
    logger.info("theme applied: %s", name)
