from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QLineEdit, QDialog
from Vista.vista_secciones.SeccionAnimalesVista import SeccionAnimalesVista
from Modelo.DataBase import DataBase


class ControladorSeccionAnimales:
    def __init__(self):
        self.__base = DataBase()
        # self.obtener_animales()
        self.__window = SeccionAnimalesVista()
        self.__window.tabla_datos.actualizar_tabla(self.obtener_datos())
        self.__window.get_boton_modif_empleado().clicked.connect(
            self.mostrar_ventana_modificar_empleado
        )
        self.__window.get_input_busqueda().editingFinished.connect(self.buscar_animal)
        self.__window.get_input_busqueda().textChanged.connect(self.buscar_animal)

    @property
    def window(self) -> SeccionAnimalesVista:
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

    def obtener_datos(self):
        datos = self.__base.getAll(
            'SELECT tipo_animal, nombre_animal, sexo_animal, etapa_vida_animal FROM public."ANIMAL"'
        )
        print((datos))
        return datos

    def buscar_animal(self):
        datos = self.__base.getAll(
            "SELECT tipo_animal, nombre_animal, sexo_animal, etapa_vida_animal FROM public.\"ANIMAL\" WHERE tipo_animal = '{}'".format(
                self.__window.obtener_animal_buscado()
            )
        )
        print((datos))
        return datos
