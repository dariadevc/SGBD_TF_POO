import sys
from PyQt6.QtWidgets import QApplication
from Vista.VistaJefe.SeccionEmpleadoVista import SeccionEmpleadoVista
from Modelo.DataBase import DataBase

class ControladorSeccionEmpleado:

    def __init__(self, estilo):
        app = QApplication(sys.argv)
        self.__base = DataBase()
        self.obtener_empleados()
        self.__window = SeccionEmpleadoVista()
        self.__window.setWindowTitle("Best Friends")
        self.__window.show()

        with open(estilo) as f:
            app.setStyleSheet(f.read())
        app.exec()

    def obtener_empleados(self):
        SeccionEmpleadoVista.set_tabla_datos(self.__base.getAll("SELECT * FROM empleado"))
        
    

