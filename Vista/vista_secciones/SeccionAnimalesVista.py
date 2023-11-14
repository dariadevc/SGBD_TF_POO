from __future__ import annotations
from PyQt6.QtWidgets import (
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QHeaderView,
)
from PyQt6.QtCore import Qt
from Vista.elementos.botones import BotonAccionTabla
from Vista.elementos.tabla import Tabla
from Vista.elementos.barra_busqueda import BarraBusqueda


class SeccionAnimalesVista(QWidget):
    info_tabla = []

    def __init__(self):
        super().__init__()

        # barra_busqueda
        self.barra_busqueda = BarraBusqueda()

        # acciones_tabla_layout <-- acá estarán contenidos los botones y la tabla de datos
        acciones_usuario_layout = QHBoxLayout()
        acciones_botones_layout = QVBoxLayout()

        # acciones_botones_layout | botones
        self.agregar_animal = BotonAccionTabla("   Agregar\n   animal", "Vista/Media/add-animal.png")
        self.modificar_animal = BotonAccionTabla(" Modificar\n animal", "Vista/Media/edit-animal.png")
        self.eliminar_animal = BotonAccionTabla("  Eliminar\n  animal", "Vista/Media/subtract-animal.png")

        # acciones_tabla_layout - composición
        self.componer_layout(
            acciones_botones_layout, [self.agregar_animal, self.modificar_animal, self.eliminar_animal])

        acciones_botones_widget = QWidget()
        acciones_botones_widget.setLayout(acciones_botones_layout)
        acciones_botones_widget.setObjectName("contenedor-botones-tabla")

        #tabla

        self.tabla_datos = Tabla()

        #acciones_tabla_layout - composición
        acciones_usuario_layout.addWidget(acciones_botones_widget)
        acciones_usuario_layout.addWidget(self.tabla_datos.info_tabla)

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(self.barra_busqueda)
        layout_principal.addLayout(acciones_usuario_layout)


        self.setLayout(layout_principal)



    # METODOS

    def componer_layout(self, layout, widgets):
        for w in widgets:
            layout.addWidget(w)

    def get_boton_modificar_animal (self):
        return self.modificar_animal

    def get_input_busqueda(self):
        return self.barra_busqueda.input_busqueda

    def get_boton_busqueda(self):
        return self.barra_busqueda.boton_busqueda

    def obtener_animal_buscado(self):
        return self.barra_busqueda.input_busqueda.text()


    @classmethod
    def set_tabla_datos(cls, datos):
        if datos is not None:
            cls.info_tabla.clear()
            cls.info_tabla.extend(datos)
        else:
            mensaje = QMessageBox()
            mensaje.show()
            mensaje.setIcon(QMessageBox.Icon.Information)
            mensaje.setWindowTitle("Error")
            mensaje.setText("No hay datos para lo que esta buscando")
            mensaje.exec()