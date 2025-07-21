from __future__ import annotations

from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QTextEdit, QVBoxLayout


def create_error_dialog(text: str, details: str) -> QDialog:
    """Return a dialog showing an error message with details."""
    dialog = QDialog()
    dialog.setWindowTitle("Fehler")

    layout = QVBoxLayout(dialog)

    label = QLabel(text)
    layout.addWidget(label)

    viewer = QTextEdit()
    viewer.setReadOnly(True)
    viewer.setPlainText(details)
    layout.addWidget(viewer)

    button = QPushButton("OK")
    button.clicked.connect(dialog.accept)
    layout.addWidget(button)

    dialog.setLayout(layout)
    return dialog
