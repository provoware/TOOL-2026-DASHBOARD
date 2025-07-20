from functools import partial
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
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
        layout = QGridLayout(central)
        for i in range(9):
            button = QPushButton(f"Card {i + 1}")
            button.clicked.connect(partial(self.handle_card_clicked, i))
            layout.addWidget(button, i // 3, i % 3)
        self.setCentralWidget(central)

    def handle_card_clicked(self, index: int) -> None:
        """Log which card was clicked."""
        logger.info("Card %s clicked", index + 1)


def main() -> int:
    """Start the GUI application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
