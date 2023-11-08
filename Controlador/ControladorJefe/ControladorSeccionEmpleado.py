import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLineEdit, QLabel, QVBoxLayout, QPushButton, QMessageBox
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
        # self.__window.get_input_busqueda().editingFinished.connect(self.buscar_empleado)

        self.__window.get_input_busqueda().textChanged.connect(self.buscar_empleado)
        self.__window.get_boton_eliminar().clicked.connect(self.mostrar_ventana_eliminar_empleado)
    
        with open(estilo) as f:
            self.__window.setStyleSheet(f.read())
        # app.exec()

    def obtener_empleados(self):
        SeccionEmpleadoVista.set_tabla_datos(
            self.__base.getAll(
                "SELECT dni_usuario, alias_usuario, nombre_usuario, apellido_usuario FROM public.usuario"
            )
        )

    # def get_ventana (self):
    #     return self.__window

    # def mostrar_ventana (self):
    #     return self.__window.show()

    def buscar_empleado(self):
        print("Buscando empleado")
        texto_busqueda = self.__window.obtener_usuario_buscado()
        resultados = self.__base.getAll(
            "SELECT dni_usuario, nombre_usuario, nombre, apellido FROM public.usuario WHERE nombre_usuario = '{}'".format(
                texto_busqueda
            )
        )
        self.__window.set_tabla_datos(resultados)

    def eliminar_empleado(self):
        print("Elimino empleado")
        texto_buscado = self.eliminar_button.text()
        if texto_buscado:
            self.__base.query(
                "DELETE FROM public.usuario WHERE dni_usuario LIKE '%{}%'".format(
                    texto_buscado
                )
            )
            print("Empleado eliminado")
            self.dialogo_eliminar.close()

    def mostrar_ventana_eliminar_empleado(self):
        self.dialogo_eliminar = QDialog(self)
        self.dialogo_eliminar.setWindowTitle("Eliminar Empleado")

        layout = QVBoxLayout()

        dni_label = QLabel("DNI del empleado a eliminar:")
        self.dni_input = QLineEdit()
        self.eliminar_button = QPushButton("Eliminar")
        self.eliminar_button.clicked.connect(self.eliminar_empleado)
        layout.addWidget(dni_label)
        layout.addWidget(self.dni_input)
        layout.addWidget(self.eliminar_button)

        self.dialogo_eliminar.setLayout(layout)
        self.dialogo_eliminar.exec()
        