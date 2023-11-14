import sys
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMessageBox
from Vista.VistaLogin.vista_login import VistaLogin

# from Modelo.DataBase import DataBase
from Modelo.Usuario import Usuario
from Controlador.ControladorJefe.controlador_seccion_empleado import (
    ControladorSeccionEmpleado,
)
from Controlador.controlador_general import ControladorGeneral


class ControladorLogin:
    def __init__(self, estilo):
        # self.app = QApplication(sys.argv)
        self.__window = VistaLogin()
        self.__window.setWindowTitle("Inicio de sesión")
        self.__window.show()
        self.__window.get_boton_login().clicked.connect(self.login)
        self.ventanaEmpleado = None

        with open(estilo) as f:
            self.__window.setStyleSheet(f.read())
            # self.app.exec()
            # sys.exit(self.app.exec())

    def login(self):
        usuario = Usuario(self.__window.get_usuario(), self.__window.get_contrasenia())
        usuario.login()
        print("listo")
        # if usuario.login():
        #
        #     if self.ventanaEmpleado is None:
        #         # self.mostrar_ventana_seccion_empleado()
        #         #     # self.app.exit()
        #
        #         # self.ventanaEmpleado = ControladorSeccionEmpleado(
        #         #     "Vista/vista_secciones/estilo_main.qss"
        #         # )
        #         self.ventanaPrincipal = ControladorGeneral()
        #
        #         self.__window.close()
        # else:
        #     mensaje = QMessageBox()
        #     mensaje.show()
        #     mensaje.setIcon(QMessageBox.Icon.Information)
        #     mensaje.setWindowTitle("Error")
        #     mensaje.setText("Credenciales erroneas.")
        #     mensaje.exec()
        #     # interfaz.get_ventana().show()
        # self.__window.close()

    # def mostrar_ventana_seccion_empleado(self):
    #     ventana_seccion_empleado = ControladorSeccionEmpleado("Vista/VistaJefe/style.qss")
    #     ventana_seccion_empleado.mostrar_ventana()
