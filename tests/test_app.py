import os
import sys

# Ensure the repository root is in the import path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QWidget,
    QLineEdit,
)  # noqa: E402
from modultool.logger import logger  # noqa: E402
from app import MainWindow  # noqa: E402
from modultool import config  # noqa: E402


def test_window_title():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    assert window.windowTitle() == "ModulTool"
    window.close()
    app.quit()


def test_header_text():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    header = window.findChild(QLabel, "header")
    assert header.text() == "Genrenarchiv \u2013 alle \u00c4nderungen gespeichert"
    window.close()
    app.quit()


def test_dashboard_has_nine_cards():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    dashboard = window.findChild(QWidget, "dashboard")
    cards = [dashboard.findChild(QWidget, f"card{i+1}") for i in range(9)]
    assert all(card is not None for card in cards)
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
    expected = f"Version {config.APP_VERSION} - {config.get_root_dir()}"
    assert statusbar.currentMessage() == expected

    dashboard = window.findChild(QWidget, "dashboard")
    button = dashboard.findChild(QPushButton, "card_button3")
    button.click()

    assert statusbar.currentMessage() == "Card 3 clicked"
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


def test_sidebar_has_search_field():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    sidebar = window.findChild(QWidget, "sidebar")
    search = sidebar.findChild(QLineEdit, "search")
    assert search is not None
    assert search.placeholderText() == "Suchen..."
    window.close()
    app.quit()


def test_nav_buttons_have_icons():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    sidebar = window.findChild(QWidget, "sidebar")
    buttons = [sidebar.findChild(QPushButton, f"nav{i+1}") for i in range(3)]
    assert all(not btn.icon().isNull() for btn in buttons)
    window.close()
    app.quit()


def test_cards_have_colored_frames():
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    dashboard = window.findChild(QWidget, "dashboard")
    buttons = [
        btn
        for btn in dashboard.findChildren(QPushButton)
        if btn.objectName().startswith("card_button")
    ]
    assert len(buttons) == 8 and all("border" in btn.styleSheet() for btn in buttons)
    window.close()
    app.quit()


def test_cards_have_edit_icons_and_log(monkeypatch):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    logs = []

    def fake_log(msg, *args):
        logs.append(msg % args)

    monkeypatch.setattr(logger, "info", fake_log)

    dashboard = window.findChild(QWidget, "dashboard")
    edit_buttons = [dashboard.findChild(QPushButton, f"edit{i+1}") for i in range(9)]
    assert all(btn is not None for btn in edit_buttons)

    edit_buttons[0].click()
    assert any("Card 1 edit" in m for m in logs)
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


def test_toggle_maximize_restores_state(monkeypatch):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    window.toggle_maximize()
    assert window.isMaximized()

    window.toggle_maximize()
    assert not window.isMaximized()
    window.close()
    app.quit()
