from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QWidget


def create_onboarding(parent: QWidget | None = None) -> QDialog:
    """Return a simple onboarding overlay dialog."""
    dialog = QDialog(parent, Qt.Tool | Qt.FramelessWindowHint)
    dialog.setObjectName("onboarding")
    dialog.setWindowTitle("Willkommen")

    layout = QVBoxLayout(dialog)

    label = QLabel(
        "Willkommen! Klicken Sie auf 'Nav 1', um die Hauptansicht zu öffnen.",
        dialog,
    )
    label.setWordWrap(True)
    layout.addWidget(label)

    button = QPushButton("Los geht's", dialog)
    button.clicked.connect(dialog.accept)
    layout.addWidget(button)

    dialog.setLayout(layout)
    dialog.setModal(True)
    return dialog


def show_onboarding(parent: QWidget | None = None) -> None:
    """Display the onboarding dialog modally."""
    create_onboarding(parent).exec()
