import os

from PySide6.QtWidgets import QApplication

from modultool.modules.genre_archive_module import GenreArchiveWidget


def test_add_and_generate(tmp_path):
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    app = QApplication.instance() or QApplication([])
    widget = GenreArchiveWidget()
    widget.data_file = tmp_path / "genre_archive.json"
    widget.log_file = tmp_path / "genre_archive.log"
    widget.categories = {}
    widget._save()
    widget.add_genres("Hard", ["Techno", "Trance", "Techno"])
    assert widget.categories["Hard"] == ["Techno", "Trance"]
    widget.mode_combo.setCurrentText("Hard")
    result = widget.generate(1)
    assert result[0] in {"Techno", "Trance"}
