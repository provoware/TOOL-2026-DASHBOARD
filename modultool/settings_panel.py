from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QDialogButtonBox,
    QApplication,
)
from PySide6.QtGui import QFont

import json
from . import config
from .theme_loader import apply_theme


class SettingsDialog(QDialog):
    """Simple settings panel for theme and font size."""

    def __init__(self, app: QApplication, current_theme: str, parent=None) -> None:
        super().__init__(parent)
        self.app = app
        self.setWindowTitle("Einstellungen")

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Theme"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["dark", "light", "highcontrast", "material"])
        self.theme_combo.setCurrentText(current_theme)
        layout.addWidget(self.theme_combo)

        layout.addWidget(QLabel("Schriftgröße"))
        self.font_spin = QSpinBox()
        self.font_spin.setRange(8, 24)
        self.font_spin.setValue(app.font().pointSize())
        layout.addWidget(self.font_spin)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.apply_settings)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def apply_settings(self) -> None:
        apply_theme(self.app, self.theme_combo.currentText())
        font = QFont(self.app.font())
        font.setPointSize(self.font_spin.value())
        self.app.setFont(font)
        cfg = config.get_user_config_file()
        cfg.parent.mkdir(parents=True, exist_ok=True)
        cfg.write_text(
            json.dumps({"theme": self.theme_combo.currentText()}, ensure_ascii=False),
            encoding="utf-8",
        )
        self.accept()
