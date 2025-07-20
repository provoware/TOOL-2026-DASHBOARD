import os
import sys

# Ensure the repository root is in the import path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from PySide6.QtWidgets import QApplication, QPushButton, QWidget  # noqa: E402
from modultool.logger import logger  # noqa: E402
from app import MainWindow  # noqa: E402


def test_window_title():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    assert window.windowTitle() == "ModulTool"
    window.close()
    app.quit()


def test_dashboard_has_nine_cards():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    dashboard = window.findChild(QWidget, "dashboard")
    buttons = dashboard.findChildren(QPushButton)
    assert len(buttons) == 9
    window.close()
    app.quit()


def test_sidebar_navigation_logs(monkeypatch):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    logs = []

    def fake_log(msg, *args):
        logs.append(msg % args)

    monkeypatch.setattr(logger, "info", fake_log)

    sidebar = window.findChild(QWidget, "sidebar")
    buttons = sidebar.findChildren(QPushButton)
    assert len(buttons) == 3
    buttons[0].click()
    assert any("Nav 1 clicked" in m for m in logs)
    window.close()
    app.quit()
