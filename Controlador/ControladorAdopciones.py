from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QLineEdit, QDialog
from Vista.seccion_adopciones_vista import SeccionAdopcionVista
from Vista.seccion_adopciones_vista import AdopcionesAntiguasVista
from Vista.seccion_adopciones_vista import FormularioAdopcionVista
from Modelo.database import DataBase


class ControladorSeccionAdopciones:
    def __init__(self):
        self.__base = DataBase()
        self.__window = SeccionAdopcionVista()
        self.__window.get_boton_adopciones_antiguas().clicked.connect(self.mostrar_adopciones_antiguas)
        self.__window.get_boton_genera_adopcion().clicked.connect(self.mostrar_formulario_adopcion)



    @property
    def window(self) -> SeccionAdopcionVista:
        return self.__window


    def mostrar_adopciones_antiguas(self):
        adopciones_antiguas_ventana = AdopcionesAntiguasVista()
        adopciones_antiguas_ventana.tabla_datos.actualizar_tabla(self.obtener_datos())
        self.__window.central_widget.addWidget(adopciones_antiguas_ventana)
        self.__window.central_widget.setCurrentWidget(adopciones_antiguas_ventana)

        adopciones_antiguas_ventana.boton_volver.clicked.connect(self.volver_inicio)

    def mostrar_formulario_adopcion(self):
        formulario_adopcion = FormularioAdopcionVista()
        self.__window.central_widget.addWidget(formulario_adopcion)
        self.__window.central_widget.setCurrentWidget(formulario_adopcion)

    def volver_inicio(self):
        self.__window.central_widget.setCurrentWidget(self.__window.button_widget)

    def obtener_datos(self):
        datos = self.__base.getAll(
            "SELECT nom_adop, nom_anim, fecha FROM public.adop"
        )
        print((datos))
        return datos