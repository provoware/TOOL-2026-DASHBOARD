import importlib
import os

from PySide6.QtWidgets import QApplication

from modultool import config


def test_apply_dark_theme(tmp_path, monkeypatch):
    theme_dir = tmp_path / "themes"
    theme_dir.mkdir()
    qss = "QWidget { background-color: #123456; }"
    (theme_dir / "dark.qss").write_text(qss, encoding="utf-8")

    monkeypatch.setattr(config, "get_theme_dir", lambda: theme_dir)

    theme_loader = importlib.import_module("modultool.theme_loader")
    importlib.reload(theme_loader)

    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    theme_loader.apply_theme(app, "dark")

    assert qss in app.styleSheet()
    app.quit()


def test_apply_highcontrast_theme(tmp_path, monkeypatch):
    theme_dir = tmp_path / "themes"
    theme_dir.mkdir()
    qss = "QWidget { background-color: #000000; color: #ffff00; }"
    (theme_dir / "highcontrast.qss").write_text(qss, encoding="utf-8")

    monkeypatch.setattr(config, "get_theme_dir", lambda: theme_dir)

    theme_loader = importlib.import_module("modultool.theme_loader")
    importlib.reload(theme_loader)

    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    theme_loader.apply_theme(app, "highcontrast")

    assert qss in app.styleSheet()
    app.quit()
