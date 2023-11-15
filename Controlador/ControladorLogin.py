import sys
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from Vista.login import Login
from Modelo.Persona.Usuario import Usuario
from Controlador.ControladorGeneral import ControladorGeneral

class ControladorLogin:
    def __init__(self):
        self.__window = Login()
        self.__window.get_boton_login().clicked.connect(self.login)
        with open("C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Estilos/estilo_login.qss") as f:
            self.__window.setStyleSheet(f.read())
        self.__correcto = None

    @property
    def window (self):
        return self.__window

    # def login(self):
    #     usuario = Usuario(self.__window.get_usuario(), self.__window.get_contrasenia())
    #     usuario.login()
    #     if usuario.login():
    #         self.__window.hide()
    #         interfaz_general = ControladorGeneral()
    #         interfaz_general.window.show()
    #     else:
    #         mensaje = QMessageBox()
    #         mensaje.show()
    #         mensaje.setIcon(QMessageBox.Icon.Information)
    #         mensaje.setWindowTitle("Error")
    #         mensaje.setText("Credenciales erroneas.")
    #         mensaje.exec()

    def login (self):
        usuario = Usuario(self.__window.get_usuario(), self.__window.get_contrasenia())
        user = usuario.login()
        if user:
            self.__window.hide()
            self.__correcto = ControladorGeneral()
        else:
            # dialogo_ingreso_incorrecto = QDialog()
            # dialogo_ingreso_incorrecto.setWindowTitle("Error")
            # layout = QVBoxLayout()
            # label = QLabel("Credenciales erroneas.")
            # layout.addWidget(label)
            # dialogo_ingreso_incorrecto.setLayout(layout)
            # dialogo_ingreso_incorrecto.exec()
            self.__window.unLabel.setText("CREDENCIALES INCORRECTAS")
