from functools import partial
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QStatusBar,
    QPushButton,
    QGroupBox,
    QVBoxLayout,
    QWidget,
    QStyle,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut, QFont
from modultool.settings_panel import SettingsDialog
from modultool import config

from modultool.logger import logger
from modultool.theme_loader import apply_theme
from modultool.help_engine import register_help, create_help_dialog
from modultool.selfcheck import selfcheck_scheduler
from modultool.onboarding import show_onboarding
from modultool.event_bus import event_bus
from modultool.stats import stats
from modultool.modules.database_module import DatabaseModule
from modultool.modules.genre_archive_module import GenreArchiveWidget
import sys


class MainWindow(QMainWindow):
    """Simple start window for the tool."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ModulTool")
        self.setMinimumSize(800, 600)

        self.genre_archive = GenreArchiveWidget()
        self.genre_archive.hide()

        self.current_theme = "dark"
        self._module_maximized = False
        QShortcut(QKeySequence("F1"), self, activated=self.show_help)
        QShortcut(QKeySequence("F6"), self, activated=self.toggle_theme)
        QShortcut(QKeySequence("F7"), self, activated=self.toggle_maximize)
        QShortcut(QKeySequence("F8"), self, activated=self.open_settings)

        central = QWidget()
        outer_layout = QVBoxLayout(central)
        header = QLabel(
            "Genrenarchiv \u2013 alle \u00c4nderungen gespeichert",
            objectName="header",
        )
        header.setAlignment(Qt.AlignCenter)
        outer_layout.addWidget(header)
        layout = QHBoxLayout()
        outer_layout.addLayout(layout)

        sidebar = QWidget(objectName="sidebar")
        side_layout = QVBoxLayout(sidebar)

        title = QLabel("ModulTool", objectName="sidebar_title")
        title_font = title.font()
        title_font.setBold(True)
        title.setFont(title_font)
        side_layout.addWidget(title)

        search = QLineEdit(objectName="search")
        search.setPlaceholderText("Suchen...")
        side_layout.addWidget(search)

        icons = [
            self.style().standardIcon(QStyle.SP_FileIcon),
            self.style().standardIcon(QStyle.SP_DirIcon),
            self.style().standardIcon(QStyle.SP_DesktopIcon),
        ]
        for i in range(3):
            nav_button = QPushButton(
                f"Nav {i + 1}", icon=icons[i], objectName=f"nav{i + 1}"
            )
            nav_button.clicked.connect(partial(self.handle_nav_clicked, i))
            if i == 0:
                register_help(nav_button, "\u00d6ffnet die Hauptansicht")
            side_layout.addWidget(nav_button)
        layout.addWidget(sidebar)

        dashboard = QWidget(objectName="dashboard")
        grid = QGridLayout(dashboard)
        colors = [
            "#ff88aa",
            "#88ffaa",
            "#aaccff",
            "#ffcc88",
            "#88ccff",
            "#ffaaff",
            "#ffaaaa",
            "#aaffaa",
            "#aaaaff",
        ]
        for i in range(9):
            card = QWidget(objectName=f"card{i + 1}")
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(0, 0, 0, 0)

            top_row = QHBoxLayout()
            top_row.setContentsMargins(0, 0, 0, 0)
            top_row.addStretch()
            edit_btn = QPushButton(
                "",
                icon=self.style().standardIcon(QStyle.SP_FileDialogDetailedView),
                objectName=f"edit{i + 1}",
            )
            edit_btn.setFixedSize(16, 16)
            edit_btn.setStyleSheet("border: none;")
            edit_btn.clicked.connect(partial(self.handle_edit_clicked, i))
            top_row.addWidget(edit_btn)

            card_layout.addLayout(top_row)
            if i == 0:
                button = QPushButton("Datenbank", objectName="card_button1")
                button.setStyleSheet(
                    f"border: 2px solid {colors[i]}; background-color: {colors[i]}33;",
                )
                button.clicked.connect(partial(self.handle_card_clicked, i))
                button.clicked.connect(self.open_database_module)
                card_layout.addWidget(button)
                hint = QLabel("Verwaltet die Datenbank", objectName="db_hint")
                hint.setAlignment(Qt.AlignCenter)
                card_layout.addWidget(hint)
            elif i == 1:
                self.quick_cat_combo = QComboBox(objectName="quick_cat")
                self.quick_cat_combo.setEditable(True)
                self.quick_genre_edit = QLineEdit(objectName="quick_genre")
                self.quick_genre_edit.setPlaceholderText("Genre1, Genre2")
                add_btn = QPushButton("Hinzufügen", objectName="quick_add")
                add_btn.clicked.connect(self.add_genres_quick)
                self.quick_genre_edit.returnPressed.connect(self.add_genres_quick)
                card_layout.addWidget(self.quick_cat_combo)
                card_layout.addWidget(self.quick_genre_edit)
                card_layout.addWidget(add_btn)
                self.refresh_quick_entry_categories()
            else:
                button = QPushButton(f"Card {i + 1}", objectName=f"card_button{i + 1}")
                button.setStyleSheet(
                    f"border: 2px solid {colors[i]}; background-color: {colors[i]}33;",
                )
                button.clicked.connect(partial(self.handle_card_clicked, i))
                card_layout.addWidget(button)
            grid.addWidget(card, i // 3, i % 3)
        layout.addWidget(dashboard)

        right_panel = QWidget(objectName="right_panel")
        right_layout = QVBoxLayout(right_panel)

        settings_box = QGroupBox("Einstellungen", objectName="settings_box")
        sb_layout = QVBoxLayout(settings_box)
        settings_btn = QPushButton("\u00d6ffnen", objectName="open_settings")
        settings_btn.clicked.connect(self.open_settings)
        sb_layout.addWidget(settings_btn)
        right_layout.addWidget(settings_box)

        help_box = QGroupBox("Schnellhilfe", objectName="help_box")
        hb_layout = QVBoxLayout(help_box)
        help_btn = QPushButton("Hilfe", objectName="open_help")
        help_btn.clicked.connect(self.show_help)
        hb_layout.addWidget(help_btn)
        right_layout.addWidget(help_box)

        stats_box = QGroupBox("Nutzerstatistik", objectName="stats_box")
        st_layout = QVBoxLayout(stats_box)
        self.error_label = QLabel("Fehler: 0", objectName="error_label")
        self.module_label = QLabel("Beliebtestes Modul: -", objectName="module_label")
        st_layout.addWidget(self.error_label)
        st_layout.addWidget(self.module_label)
        right_layout.addWidget(stats_box)

        layout.addWidget(right_panel)

        event_bus.subscribe("module.open", self.update_stats_labels)
        event_bus.subscribe("error.occurred", self.update_stats_labels)

        self.update_stats_labels()

        self.setCentralWidget(central)
        status = QStatusBar(objectName="statusbar")
        version = config.APP_VERSION
        path = str(config.get_root_dir())
        status.showMessage(f"Version {version} - {path}")
        self.setStatusBar(status)

    def handle_card_clicked(self, index: int) -> None:
        """Log which card was clicked."""
        logger.info("Card %s clicked", index + 1)
        self.statusBar().showMessage(f"Card {index + 1} clicked")

    def handle_nav_clicked(self, index: int) -> None:
        """Log which navigation button was clicked."""
        logger.info("Nav %s clicked", index + 1)
        self.statusBar().showMessage(f"Nav {index + 1} clicked")

    def handle_edit_clicked(self, index: int) -> None:
        """Log edit button presses for each card."""
        logger.info("Card %s edit", index + 1)
        self.statusBar().showMessage(f"Edit card {index + 1}")

    def open_database_module(self) -> None:
        """Open the database management window."""
        db = DatabaseModule()
        db.start()

    def refresh_quick_entry_categories(self) -> None:
        self.quick_cat_combo.clear()
        self.quick_cat_combo.addItems(
            sorted(self.genre_archive.categories.keys(), key=str.lower)
        )

    def add_genres_quick(self) -> None:
        category = self.quick_cat_combo.currentText().strip()
        genres = [
            g.strip() for g in self.quick_genre_edit.text().split(",") if g.strip()
        ]
        if not category or not genres:
            return
        self.genre_archive.add_genres(category, genres)
        self.quick_genre_edit.clear()
        self.refresh_quick_entry_categories()
        self.statusBar().showMessage("Genres hinzugefügt")

    def update_stats_labels(self, *args) -> None:
        """Refresh statistics labels with current values."""
        top = stats.get_most_used_module() or "-"
        self.module_label.setText(f"Beliebtestes Modul: {top}")
        self.error_label.setText(f"Fehler: {stats.get_error_count()}")

    def toggle_theme(self) -> None:
        """Switch between dark and high contrast themes."""
        self.current_theme = "highcontrast" if self.current_theme == "dark" else "dark"
        app = QApplication.instance()
        if app:
            apply_theme(app, self.current_theme)

    def toggle_maximize(self) -> None:
        """Maximize or restore the main window."""
        if self._module_maximized:
            self.showNormal()
        else:
            self.showMaximized()
        self._module_maximized = not self._module_maximized

    def open_settings(self) -> None:
        """Open settings dialog to change theme and font size."""
        app = QApplication.instance()
        if not app:
            return
        dialog = SettingsDialog(app, self.current_theme, self)
        if dialog.exec() == dialog.Accepted:
            self.current_theme = dialog.theme_combo.currentText()

    def show_help(self) -> None:
        dialog = create_help_dialog()
        dialog.exec()


def main() -> int:
    """Start the GUI application."""
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial", 12))
    apply_theme(app, "dark")
    window = MainWindow()
    window.show()
    show_onboarding(window)
    selfcheck_scheduler.start()
    app.aboutToQuit.connect(selfcheck_scheduler.stop)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
