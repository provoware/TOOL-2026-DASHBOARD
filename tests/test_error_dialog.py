import os
from PySide6.QtWidgets import QApplication, QLabel, QTextEdit

from modultool.error_dialog import create_error_dialog


def test_error_dialog_contents():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    dialog = create_error_dialog("Fehler aufgetreten", "Details")
    label = dialog.findChild(QLabel)
    text = dialog.findChild(QTextEdit)
    assert label.text() == "Fehler aufgetreten"
    assert text.toPlainText() == "Details"
    app.quit()
