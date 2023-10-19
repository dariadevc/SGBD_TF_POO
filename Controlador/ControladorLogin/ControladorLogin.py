import sys
from PyQt6.QtWidgets import QApplication
from Vista.VistaLogin.LoginView import Login
from Modelo.DataBase import DataBase

class ControladorLogin:

    def __init__(self,estilo):
        app = QApplication(sys.argv)
        self.__window = Login()
        self.__window.setWindowTitle("Inicio de sesión")
        self.__window.show()

        with open(estilo) as f:
            app.setStyleSheet(f.read())
        app.exec()



