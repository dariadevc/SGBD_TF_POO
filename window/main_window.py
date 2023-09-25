import sys

from PyQt6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QWidget,
    QLabel,
    QLineEdit,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Best Friends")
        self.resize(1000, 700)

        self.label = QLabel("Hola Mundo")

        font = self.label.font()
        # font.setPointSize(30)
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        self.setCentralWidget(self.label)
