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

        # barra_busqueda | input de busqueda
        barra_busqueda_layout = QHBoxLayout()

        boton_busqueda = QPushButton("Buscar")
        boton_busqueda.setFixedWidth(50)
        self.input_busqueda = QLineEdit()
        self.input_busqueda.setPlaceholderText("Buscar...")
        self.input_busqueda.setFixedWidth(200)

        # barra_busqueda - composición
        barra_busqueda_layout.addWidget(self.input_busqueda)
        barra_busqueda_layout.addWidget(boton_busqueda)
        barra_busqueda_layout.setAlignment(
            self.input_busqueda, Qt.AlignmentFlag.AlignRight
        )

        # Si hacemos una clase para barra_busqeuda, como la usamos varias veces, sirve?
        # self.barra_busqueda = BarraBusqueda()

        # acciones_tabla_layout <-- acá estarán contenidos los botones y la tabla de datos
        acciones_usuario_layout = QHBoxLayout()
        acciones_botones_layout = QVBoxLayout()

        # acciones_botones_layout | botones
        agregar_e = BotonAccionTabla(
            "   Agregar\n   animal", "Vista/Media/add-animal.png"
        )
        self.modificar_e = BotonAccionTabla(
            " Modificar\n animal", "Vista/Media/edit-animal.png"
        )
        eliminar_e = BotonAccionTabla(
            "  Eliminar\n  animal", "Vista/Media/subtract-animal.png"
        )

        # acciones_tabla_layout - composición
        self.componer_layout(
            acciones_botones_layout, [agregar_e, self.modificar_e, eliminar_e]
        )

        acciones_botones_widget = QWidget()
        acciones_botones_widget.setLayout(acciones_botones_layout)
        acciones_botones_widget.setObjectName("contenedor-botones-tabla")

        # tabla

        self.tabla_datos = Tabla()

        # acciones_tabla_layout - composición
        acciones_usuario_layout.addWidget(acciones_botones_widget)
        acciones_usuario_layout.addWidget(self.tabla_datos.info_tabla)

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(barra_busqueda_layout)
        layout_principal.addLayout(acciones_usuario_layout)

        self.setLayout(layout_principal)

    def componer_layout(self, layout, widgets):
        for w in widgets:
            layout.addWidget(w)

    def get_boton_modif_empleado(self):
        return self.modificar_e

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

    def get_input_busqueda(self):
        return self.input_busqueda

    def obtener_animal_buscado(self):
        return self.input_busqueda.text()

    # @classmethod
    # def set_tabla_datos(cls, datos):
    #     cls.info_tabla.extend(datos)
