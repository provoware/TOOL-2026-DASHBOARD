import json
import random
from pathlib import Path
from typing import Dict, List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from ..config import get_data_dir
from ..logger import logger


class GenreArchiveWidget(QWidget):
    """Widget to manage genres per category and generate random combinations."""

    def __init__(self) -> None:
        super().__init__()
        self.data_file = get_data_dir() / "genre_archive.json"
        self.log_file = get_data_dir() / "genre_archive.log"
        self.categories: Dict[str, List[str]] = {}
        self._load()
        self._setup_ui()
        self._refresh()

    # UI setup
    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        lists_layout = QHBoxLayout()
        layout.addLayout(lists_layout)

        self.category_list = QListWidget()
        lists_layout.addWidget(self.category_list)
        self.genre_list = QListWidget()
        lists_layout.addWidget(self.genre_list)

        cat_input_layout = QHBoxLayout()
        self.new_cat_edit = QLineEdit()
        self.new_cat_edit.setPlaceholderText("Kategorie hinzufügen")
        self.new_cat_edit.returnPressed.connect(self._add_category_from_edit)
        cat_btn = QPushButton("Add")
        cat_btn.clicked.connect(self._add_category_from_edit)
        cat_input_layout.addWidget(self.new_cat_edit)
        cat_input_layout.addWidget(cat_btn)
        layout.addLayout(cat_input_layout)

        genre_input_layout = QHBoxLayout()
        self.genre_edit = QLineEdit()
        self.genre_edit.setPlaceholderText("Genre1, Genre2")
        self.genre_edit.returnPressed.connect(self._add_genres_from_edit)
        genre_btn = QPushButton("Einfügen")
        genre_btn.clicked.connect(self._add_genres_from_edit)
        genre_input_layout.addWidget(self.genre_edit)
        genre_input_layout.addWidget(genre_btn)
        layout.addLayout(genre_input_layout)

        self.stats_label = QLabel()
        layout.addWidget(self.stats_label)

        gen_layout = QHBoxLayout()
        self.mode_combo = QComboBox()
        gen_layout.addWidget(self.mode_combo)
        for i in range(1, 6):
            btn = QPushButton(str(i))
            btn.clicked.connect(lambda _=False, x=i: self.generate(x))
            gen_layout.addWidget(btn)
        self.custom_spin = QSpinBox()
        self.custom_spin.setRange(1, 20)
        gen_layout.addWidget(self.custom_spin)
        custom_btn = QPushButton("Custom")
        custom_btn.clicked.connect(lambda: self.generate(self.custom_spin.value()))
        gen_layout.addWidget(custom_btn)
        super_btn = QPushButton("Super")
        super_btn.clicked.connect(self.generate_super)
        gen_layout.addWidget(super_btn)
        layout.addLayout(gen_layout)

        self.output_edit = QLineEdit()
        self.output_edit.setReadOnly(True)
        layout.addWidget(self.output_edit)

        self.category_list.currentTextChanged.connect(self._select_category)

    # Data persistence
    def _load(self) -> None:
        if self.data_file.exists():
            with self.data_file.open("r", encoding="utf-8") as f:
                self.categories = json.load(f)
        else:
            self.categories = {}

    def _save(self) -> None:
        with self.data_file.open("w", encoding="utf-8") as f:
            json.dump(self.categories, f, indent=2, ensure_ascii=False)

    # Category handling
    def _add_category_from_edit(self) -> None:
        name = self.new_cat_edit.text().strip()
        if name and name not in self.categories:
            self.categories[name] = []
            self.new_cat_edit.clear()
            self._save()
            self._refresh()

    def _add_genres_from_edit(self) -> None:
        current = self.category_list.currentItem()
        if not current:
            return
        name = current.text()
        genres = [g.strip() for g in self.genre_edit.text().split(",") if g.strip()]
        existing = set(self.categories.get(name, []))
        for g in genres:
            existing.add(g)
        self.categories[name] = sorted(existing, key=str.lower)
        self.genre_edit.clear()
        self._save()
        self._refresh()
        self.category_list.setCurrentRow(self.category_list.row(current))

    def _select_category(self, name: str) -> None:
        self.genre_list.clear()
        if not name:
            return
        for g in self.categories.get(name, []):
            self.genre_list.addItem(QListWidgetItem(g))

    def _refresh(self) -> None:
        self.category_list.clear()
        for name in sorted(self.categories.keys(), key=str.lower):
            self.category_list.addItem(QListWidgetItem(name))
        self.mode_combo.clear()
        self.mode_combo.addItems(sorted(self.categories.keys(), key=str.lower))
        total = sum(len(v) for v in self.categories.values())
        self.stats_label.setText(
            f"Kategorien: {len(self.categories)} | Genres: {total}"
        )

    # Public methods for tests
    def add_category(self, name: str) -> None:
        if name not in self.categories:
            self.categories[name] = []
            self._save()
            self._refresh()

    def add_genres(self, category: str, genres: List[str]) -> None:
        self.add_category(category)
        existing = set(self.categories[category])
        for g in genres:
            existing.add(g)
        self.categories[category] = sorted(existing, key=str.lower)
        self._save()
        self._refresh()

    # Generation
    def _handle_output(self, result: List[str]) -> None:
        text = ", ".join(result)
        self.output_edit.setText(text)
        QApplication.clipboard().setText(text)
        with self.log_file.open("a", encoding="utf-8") as f:
            f.write(text + "\n")
        logger.info("Genres generiert: %s", text)

    def generate(self, count: int) -> List[str]:
        category = self.mode_combo.currentText()
        genres = self.categories.get(category, [])
        if not genres:
            return []
        n = min(count, len(genres))
        result = random.sample(genres, n)
        self._handle_output(result)
        return result

    def generate_super(self) -> List[str]:
        all_genres = [g for lst in self.categories.values() for g in lst]
        if not all_genres:
            return []
        count = self.custom_spin.value()
        n = min(count, len(all_genres))
        result = random.sample(all_genres, n)
        self._handle_output(result)
        return result
