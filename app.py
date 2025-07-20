from functools import partial
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from modultool.logger import logger
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

    def handle_card_clicked(self, index: int) -> None:
        """Log which card was clicked."""
        logger.info("Card %s clicked", index + 1)

    def handle_nav_clicked(self, index: int) -> None:
        """Log which navigation button was clicked."""
        logger.info("Nav %s clicked", index + 1)


def main() -> int:
    """Start the GUI application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
