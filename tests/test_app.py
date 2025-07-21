import os
import sys

# Ensure the repository root is in the import path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from PySide6.QtWidgets import QApplication  # noqa: E402
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


def test_statusbar_updates_on_click():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    statusbar = window.findChild(QWidget, "statusbar")
    assert statusbar.currentMessage() == "Bereit"

    dashboard = window.findChild(QWidget, "dashboard")
    button = dashboard.findChildren(QPushButton)[0]
    button.click()

    assert statusbar.currentMessage() == "Card 1 clicked"
    window.close()
    app.quit()


def test_help_tooltip_on_first_nav():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    sidebar = window.findChild(QWidget, "sidebar")
    button = sidebar.findChildren(QPushButton)[0]
    assert button.toolTip() == "\u00d6ffnet die Hauptansicht"
    window.close()
    app.quit()


def test_toggle_theme_switches_stylesheet(tmp_path, monkeypatch):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    theme_dir = tmp_path / "themes"
    theme_dir.mkdir()
    dark_qss = "QWidget { background-color: #111; }"
    hc_qss = "QWidget { background-color: #000; color: #ff0; }"
    (theme_dir / "dark.qss").write_text(dark_qss, encoding="utf-8")
    (theme_dir / "highcontrast.qss").write_text(hc_qss, encoding="utf-8")

    from modultool import config, theme_loader

    monkeypatch.setattr(config, "get_theme_dir", lambda: theme_dir)
    app = QApplication.instance() or QApplication([])
    theme_loader.apply_theme(app, "dark")

    window = MainWindow()
    assert dark_qss in app.styleSheet()
    window.toggle_theme()
    assert hc_qss in app.styleSheet()
    window.close()
    app.quit()
