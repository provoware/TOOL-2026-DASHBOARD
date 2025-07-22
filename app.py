from functools import partial
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QStatusBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QKeySequence, QShortcut
from modultool.settings_panel import SettingsDialog

from modultool.logger import logger
from modultool.theme_loader import apply_theme
from modultool.help_engine import register_help, create_help_dialog
from modultool.help_engine import register_help
from modultool.selfcheck import selfcheck_scheduler
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
        layout = QHBoxLayout(central)

        sidebar = QWidget(objectName="sidebar")
        side_layout = QVBoxLayout(sidebar)
        for i in range(3):
            nav_button = QPushButton(f"Nav {i + 1}", objectName=f"nav{i + 1}")
            nav_button.clicked.connect(partial(self.handle_nav_clicked, i))
            if i == 0:
                register_help(nav_button, "\u00d6ffnet die Hauptansicht")
            side_layout.addWidget(nav_button)
        layout.addWidget(sidebar)

        dashboard = QWidget(objectName="dashboard")
        grid = QGridLayout(dashboard)
        for i in range(9):
            button = QPushButton(f"Card {i + 1}")
            button.clicked.connect(partial(self.handle_card_clicked, i))
            grid.addWidget(button, i // 3, i % 3)
        layout.addWidget(dashboard)

        self.setCentralWidget(central)
        status = QStatusBar(objectName="statusbar")
        status.showMessage("Bereit")
        self.setStatusBar(status)

    def handle_card_clicked(self, index: int) -> None:
        """Log which card was clicked."""
        logger.info("Card %s clicked", index + 1)
        self.statusBar().showMessage(f"Card {index + 1} clicked")

    def handle_nav_clicked(self, index: int) -> None:
        """Log which navigation button was clicked."""
        logger.info("Nav %s clicked", index + 1)
        self.statusBar().showMessage(f"Nav {index + 1} clicked")

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
    selfcheck_scheduler.start()
    app.aboutToQuit.connect(selfcheck_scheduler.stop)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
