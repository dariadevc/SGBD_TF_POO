import sys
from Controlador.ControladorLogin import ControladorLogin
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorLogin()
    controlador.window.show()
    sys.exit(app.exec())