import sys
from Controlador.ControladorLogin import ControladorLogin
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorLogin()
    controlador.window.show()
    sys.exit(app.exec())