from __future__ import annotations

from PySide6.QtWidgets import QWidget

from .logger import logger


def register_help(widget: QWidget, text: str) -> None:
    """Assign tooltip text to a widget."""
    widget.setToolTip(text)
    logger.info("help text registered for %s", widget.objectName() or widget.text())
