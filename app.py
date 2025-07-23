from functools import partial
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QStatusBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QStyle,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from modultool.settings_panel import SettingsDialog
from modultool import config

from modultool.logger import logger
from modultool.theme_loader import apply_theme
from modultool.help_engine import register_help, create_help_dialog
from modultool.selfcheck import selfcheck_scheduler
from modultool.onboarding import show_onboarding
import sys


class MainWindow(QMainWindow):
    """Simple start window for the tool."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ModulTool")

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
            "#f8a",
            "#8fa",
            "#acf",
            "#fc8",
            "#8cf",
            "#faf",
            "#faa",
            "#afa",
            "#aaf",
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

            button = QPushButton(f"Card {i + 1}", objectName=f"card_button{i + 1}")
            button = QPushButton(f"Card {i + 1}")
            button.setStyleSheet(
                f"border: 2px solid {colors[i]}; background-color: {colors[i]}33;"
            )
            button.clicked.connect(partial(self.handle_card_clicked, i))
            card_layout.addWidget(button)

            grid.addWidget(card, i // 3, i % 3)
        layout.addWidget(dashboard)

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
    apply_theme(app, "dark")
    window = MainWindow()
    window.show()
    show_onboarding(window)
    selfcheck_scheduler.start()
    app.aboutToQuit.connect(selfcheck_scheduler.stop)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
