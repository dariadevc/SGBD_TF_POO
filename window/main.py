import sys

from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
