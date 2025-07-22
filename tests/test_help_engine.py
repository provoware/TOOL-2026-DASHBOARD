import os
from PySide6.QtWidgets import QApplication, QPushButton, QTextEdit

from modultool.help_engine import register_help, create_help_dialog


def test_register_help_sets_tooltip():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    btn = QPushButton("Test")
    register_help(btn, "Hilfe")
    assert btn.toolTip() == "Hilfe"
    app.quit()


def test_create_help_dialog_lists_registered_help():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    btn = QPushButton("Test", objectName="btn")
    register_help(btn, "Hilfe")
    dlg = create_help_dialog()
    viewer = dlg.findChild(QTextEdit)
    assert "btn" in viewer.toPlainText()
    app.quit()
