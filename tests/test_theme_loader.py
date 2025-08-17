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


def test_apply_light_theme(tmp_path, monkeypatch):
    theme_dir = tmp_path / "themes"
    theme_dir.mkdir()
    qss = "QWidget { background-color: #ffffff; color: #000000; }"
    (theme_dir / "light.qss").write_text(qss, encoding="utf-8")

    monkeypatch.setattr(config, "get_theme_dir", lambda: theme_dir)

    theme_loader = importlib.import_module("modultool.theme_loader")
    importlib.reload(theme_loader)

    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    theme_loader.apply_theme(app, "light")

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


def test_apply_material_theme(tmp_path, monkeypatch):
    theme_dir = tmp_path / "themes"
    theme_dir.mkdir()
    qss = "QWidget { background-color: #121212; color: #ffffff; }"
    (theme_dir / "material.qss").write_text(qss, encoding="utf-8")

    monkeypatch.setattr(config, "get_theme_dir", lambda: theme_dir)

    theme_loader = importlib.import_module("modultool.theme_loader")
    importlib.reload(theme_loader)

    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    theme_loader.apply_theme(app, "material")

    assert qss in app.styleSheet()
    app.quit()


def test_load_user_theme(tmp_path, monkeypatch):
    cfg = tmp_path / "config.json"
    cfg.write_text('{"theme": "light"}', encoding="utf-8")
    monkeypatch.setattr(config, "get_user_config_file", lambda: cfg)
    theme_loader = importlib.import_module("modultool.theme_loader")
    importlib.reload(theme_loader)
    assert theme_loader.load_user_theme() == "light"


def test_user_theme_dir_overrides(tmp_path, monkeypatch):
    user_dir = tmp_path / "user"
    user_dir.mkdir()
    (user_dir / "dark.qss").write_text(
        "QWidget { background-color: #123123; }", encoding="utf-8"
    )
    theme_dir = tmp_path / "themes"
    theme_dir.mkdir()
    (theme_dir / "dark.qss").write_text(
        "QWidget { background-color: #000000; }", encoding="utf-8"
    )
    monkeypatch.setattr(config, "get_user_theme_dir", lambda: user_dir)
    monkeypatch.setattr(config, "get_theme_dir", lambda: theme_dir)
    theme_loader = importlib.import_module("modultool.theme_loader")
    importlib.reload(theme_loader)
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    theme_loader.apply_theme(app, "dark")
    assert "#123123" in app.styleSheet()
    app.quit()
