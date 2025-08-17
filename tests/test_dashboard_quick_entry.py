import os
from PySide6.QtWidgets import QApplication
from app import MainWindow


def test_quick_entry_adds_genres(tmp_path):
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    app = QApplication.instance() or QApplication([])
    win = MainWindow()
    win.genre_archive.data_file = tmp_path / "genre_archive.json"
    win.genre_archive.log_file = tmp_path / "log.log"
    win.genre_archive.categories = {}
    win.genre_archive._save()
    win.refresh_quick_entry_categories()
    win.quick_cat_combo.setCurrentText("Hard")
    win.quick_genre_edit.setText("Techno, Trance")
    win.add_genres_quick()
    assert win.genre_archive.categories["Hard"] == ["Techno", "Trance"]
