import sys
from PyQt6.QtWidgets import QApplication
from Vista.VistaJefe.SeccionAnimalesVista import SeccionAnimalesVista
from Modelo.DataBase import DataBase

class ControladorSeccionAnimales:

    def __init__(self, estilo):
        app = QApplication(sys.argv)
        self.__base = DataBase()
        self.__window = SeccionAnimalesVista()
        self.__window.setWindowTitle("Best Friends")
        self.__window.show()

        with open(estilo) as f:
            app.setStyleSheet(f.read())
        app.exec()