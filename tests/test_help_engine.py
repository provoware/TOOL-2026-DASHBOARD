import os
from PySide6.QtWidgets import QApplication, QPushButton

from modultool.help_engine import register_help


def test_register_help_sets_tooltip():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    btn = QPushButton("Test")
    register_help(btn, "Hilfe")
    assert btn.toolTip() == "Hilfe"
    app.quit()
