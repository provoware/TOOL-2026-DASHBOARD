import os
from PySide6.QtWidgets import QApplication

from modultool import config
from modultool.settings_panel import SettingsDialog


def test_settings_dialog_applies_changes(tmp_path, monkeypatch):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    theme_dir = tmp_path / "themes"
    theme_dir.mkdir()
    (theme_dir / "dark.qss").write_text("QWidget { color: #111; }", encoding="utf-8")
    (theme_dir / "highcontrast.qss").write_text(
        "QWidget { color: #ff0; }", encoding="utf-8"
    )

    monkeypatch.setattr(config, "get_theme_dir", lambda: theme_dir)
    monkeypatch.setattr(
        config, "get_user_config_file", lambda: tmp_path / "config.json"
    )
    app = QApplication.instance() or QApplication([])
    dialog = SettingsDialog(app, "dark")
    dialog.theme_combo.setCurrentText("highcontrast")
    dialog.font_spin.setValue(app.font().pointSize() + 1)
    dialog.apply_settings()
    assert (tmp_path / "config.json").read_text(
        encoding="utf-8"
    ) == '{"theme": "highcontrast"}'

    assert "#ff0" in app.styleSheet()
    assert app.font().pointSize() == dialog.font_spin.value()
    app.quit()
