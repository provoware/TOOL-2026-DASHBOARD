import json
import os

from PySide6.QtWidgets import QApplication

from modultool.autosave import autosave
from modultool.modules import GenresModule


def test_autosave_saves_data(tmp_path, monkeypatch):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])

    genres_file = tmp_path / "genres.json"
    genres_file.write_text(json.dumps(["Rock"]), encoding="utf-8")
    module = GenresModule(path=genres_file)

    autosave.autosave(module)

    data = json.loads(genres_file.read_text(encoding="utf-8"))
    assert data == ["Rock"]
    app.quit()
