from Controlador.ControladorLogin.controlador_login import ControladorLogin
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorLogin("Vista\VistaLogin\estilo_login.qss")
    app.exec()
