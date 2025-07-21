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

from modultool.logger import logger
from modultool.theme_loader import apply_theme
import sys


class MainWindow(QMainWindow):
    """Simple start window for the tool."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ModulTool")

        central = QWidget()
        layout = QHBoxLayout(central)

        sidebar = QWidget(objectName="sidebar")
        side_layout = QVBoxLayout(sidebar)
        for i in range(3):
            nav_button = QPushButton(f"Nav {i + 1}")
            nav_button.clicked.connect(partial(self.handle_nav_clicked, i))
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


def main() -> int:
    """Start the GUI application."""
    app = QApplication(sys.argv)
    apply_theme(app, "dark")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
