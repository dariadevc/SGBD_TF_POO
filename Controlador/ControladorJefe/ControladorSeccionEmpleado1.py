import sys
from PyQt6.QtWidgets import QApplication
from Vista.VistaJefe.SeccionEmpleadoVista1 import SeccionEmpleadoVista
from Modelo.DataBase import DataBase


class ControladorSeccionEmpleado:

    def __init__(self, estilo):
        # app = QApplication(sys.argv)
        self.__base = DataBase()
        self.obtener_empleados()
        self.__window = SeccionEmpleadoVista()
        self.__window.setWindowTitle("Best Friends")
        self.__window.show()
        # empleado = self.__window.obtener_usuario_buscado()
        self.__window.get_input_busqueda().editingFinished.connect(self.buscar_empleado)
        self.__window.get_input_busqueda().textChanged.connect(self.buscar_empleado)

    
        with open(estilo) as f:
            self.__window.setStyleSheet(f.read())
        # app.exec()

    def obtener_empleados(self):
        SeccionEmpleadoVista.set_tabla_datos(self.__base.getAll("SELECT dni, nombre_usuario, nombre, apellido FROM public.usuarios"))
        
    # def get_ventana (self):
    #     return self.__window
    
    # def mostrar_ventana (self):
    #     return self.__window.show()

    def buscar_empleado(self):
        SeccionEmpleadoVista.set_tabla_datos(self.__base.getAll("SELECT dni, nombre_usuario, nombre, apellido FROM public.usuarios WHERE nombre_usuario = '{}'".format(self.__window.obtener_usuario_buscado())))
