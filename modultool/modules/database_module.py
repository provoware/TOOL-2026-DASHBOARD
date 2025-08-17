import sqlite3
from pathlib import Path

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox

from .base_module import BaseModule
from ..config import get_data_dir
from ..logger import logger


class DatabaseWindow(QDialog):
    """Simple dialog to manage the SQLite database."""

    def __init__(self, path: Path):
        super().__init__()
        self.setWindowTitle("Datenbank")
        layout = QVBoxLayout(self)
        self.path = path
        if not path.exists():
            reply = QMessageBox.question(
                self,
                "Datenbank fehlt",
                "Keine Datenbank gefunden. Neue erstellen?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                sqlite3.connect(path).close()
                QMessageBox.information(self, "Erstellt", "Neue Datenbank angelegt.")
            else:
                QMessageBox.information(self, "Abbruch", "Keine Datenbank erstellt.")
        else:
            layout.addWidget(QLabel("Datenbank vorhanden."))


class DatabaseModule(BaseModule):
    """Module to handle database operations."""

    name = "database"

    def __init__(self):
        super().__init__()
        self.file = get_data_dir() / "app.db"

    def start(self) -> None:
        """Show the database window."""
        self.window = DatabaseWindow(self.file)
        self.window.show()
        logger.info("Datenbankmodul geöffnet")
