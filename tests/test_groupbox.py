import os
from PySide6.QtWidgets import QApplication, QGroupBox

from app import MainWindow


def test_right_panel_groupbox_layout():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    for name in ("settings_box", "help_box", "stats_box"):
        box = window.findChild(QGroupBox, name)
        assert box is not None

    window.close()
    app.quit()
