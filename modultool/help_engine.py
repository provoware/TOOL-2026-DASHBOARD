from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


_HELP_REGISTRY: dict[str, str] = {}

from .logger import logger


def register_help(widget: QWidget, text: str) -> None:
    """Assign tooltip text to a widget."""
    widget.setToolTip(text)
    _HELP_REGISTRY[widget.objectName() or widget.text()] = text
    logger.info("help text registered for %s", widget.objectName() or widget.text())


def create_help_dialog() -> QDialog:
    """Return a dialog listing all registered help texts."""
    dialog = QDialog()
    dialog.setWindowTitle("Hilfe")

    layout = QVBoxLayout(dialog)

    viewer = QTextEdit()
    viewer.setReadOnly(True)
    for name, tip in _HELP_REGISTRY.items():
        viewer.append(f"{name}: {tip}")
    layout.addWidget(viewer)

    button = QPushButton("Schließen")
    button.clicked.connect(dialog.accept)
    layout.addWidget(button)

    dialog.setLayout(layout)
    return dialog
