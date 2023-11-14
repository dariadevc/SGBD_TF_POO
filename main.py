from Controlador.ControladorLogin.controlador_login import ControladorLogin
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorLogin("C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/VistaLogin/estilo_login.qss")
    app.exec()
