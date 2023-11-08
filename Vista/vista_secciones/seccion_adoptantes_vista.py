from __future__ import annotations
from PyQt6.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QHeaderView
from PyQt6.QtCore import Qt
from Vista.elementos.botones import BotonAccionTabla
from Vista.elementos.tabla import Tabla
class SeccionAdoptantesVista(QWidget):

    def __init__(self):

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
        barra_busqueda_layout.setAlignment(self.input_busqueda, Qt.AlignmentFlag.AlignRight)

        # acciones_tabla_layout <-- acá estarán contenidos los botones y la tabla de datos
        acciones_usuario_layout = QHBoxLayout()
        acciones_botones_layout = QVBoxLayout()

        # acciones_botones_layout | botones
        self.registrar_adoptante = BotonAccionTabla("   Registrar\n   adopcion",
                                     "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/aniadir_registro.png")
        self.modificar_adoptante = BotonAccionTabla(" Modificar\n registro",
                                            "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/modificar-registro.png")
        self.eliminar_adoptante = BotonAccionTabla("  Eliminar\n  registro",
                                      "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/eliminar-registro.png")

        # acciones_tabla_layout - composición
        self.componer_layout(acciones_botones_layout, [self.registrar_adoptante, self.modificar_adoptante, self.eliminar_adoptante])

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

    def get_boton_modif_adoptante(self):
        return self.modificar_adoptante

    def get_input_busqueda(self):
        return self.input_busqueda

    def obtener_adoptante_buscado(self):
        return self.input_busqueda.text()
