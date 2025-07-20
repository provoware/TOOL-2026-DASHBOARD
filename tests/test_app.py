import os
import sys

# Ensure the repository root is in the import path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication
from app import MainWindow


def test_window_title():
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    assert window.windowTitle() == "ModulTool"
    window.close()
    app.quit()
