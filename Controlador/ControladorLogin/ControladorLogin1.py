import sys
from PyQt6.QtWidgets import QApplication
from Vista.VistaLogin.LoginView import Login
# from Modelo.DataBase import DataBase
from Modelo.Usuario import Usuario
from Controlador.ControladorJefe.ControladorSeccionEmpleado import ControladorSeccionEmpleado

class ControladorLogin:

    def __init__(self,estilo):
        app = QApplication(sys.argv)
        self.__window = Login()
        self.__window.setWindowTitle("Inicio de sesión")
        self.__window.show()
        self.__window.get_boton_login().clicked.connect(self.login)
        
        with open(estilo) as f:
            self.__window.setStyleSheet(f.read())
            app.exec()

    def login(self):
        usuario = Usuario(self.__window.get_usuario(), self.__window.get_contrasenia())
        usuario.login()
        if usuario.login():
            ControladorSeccionEmpleado("C:/Users/LENOVO/Desktop/SGBD_TF_POO-vj_se_ver1/Vista/VistaJefe/style.qss")
            # self.__window.close()

