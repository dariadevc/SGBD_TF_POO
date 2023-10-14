import sys
from PyQt6.QtWidgets import QApplication
from Vista.VistaJefe.SeccionEmpleadoVista import SeccionEmpleadoVista

class ControladorSeccionEmpleado:

    def __init__(self, estilo):
        app = QApplication(sys.argv)
        self.__window = SeccionEmpleadoVista()
        self.__window.setWindowTitle("Best Friends")
        self.__window.show()

        with open(estilo) as f:
            app.setStyleSheet(f.read())
        app.exec()
