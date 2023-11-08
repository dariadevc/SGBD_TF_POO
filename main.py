from PyQt6.QtWidgets import QApplication
import sys
from Controlador.controlador_login.controlador_login import ControladorLogin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = ControladorLogin("Vista/VistaLogin/estilo_login.qss")
    app.exec()
