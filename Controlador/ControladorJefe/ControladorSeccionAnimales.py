import sys
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\Clases')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\vista_secciones')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\vista_secciones\\SeccionAnimalesVista')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\VistaPrincipal')

sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador\\ControladorJefe')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador\\ControladorJefe\\ControladorSeccionAnimales.py')

sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Modelo')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Modelo\\tabla')



from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QDialog
from PyQt6.QtWidgets import QMainWindow
# from Vista.VistaJefe.SeccionAnimalesVista import SeccionAnimalesVista
# from Modelo.DataBase import DataBase


from Vista.vista_secciones.SeccionAnimalesVista import SeccionAnimalesVista


class ControladorSeccionAnimales:

    def __init__(self):
        # self.__base = DataBase()
        self.obtener_animales()
        self.__window = SeccionAnimalesVista()
        self.__window.get_boton_modif_empleado().clicked.connect(self.mostrar_ventana_modificar_empleado)


    @property
    def window (self) -> SeccionAnimalesVista:
        return self.__window

    def mostrar_ventana_modificar_empleado(self):
        self.dialogo_eliminar = QDialog()
        self.dialogo_eliminar.setWindowTitle("Modificar Empleado")

        layout = QVBoxLayout()

        dni_label = QLabel("DNI del empleado a Modificar:")
        self.dni_input = QLineEdit()
        self.eliminar_button = QPushButton("Modificar")
        layout.addWidget(dni_label)
        layout.addWidget(self.dni_input)
        layout.addWidget(self.eliminar_button)
        
        self.dialogo_eliminar.setLayout(layout)
        self.dialogo_eliminar.exec()


