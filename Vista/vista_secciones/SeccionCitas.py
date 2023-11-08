from __future__ import annotations
from PyQt6.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QHeaderView
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from Vista.elementos.botones import BotonAccionTabla


class SeccionCitasVista (QWidget):

    info_tabla = []

    def __init__(self):
        super().__init__()

        #barra_busqueda | input de busqueda 
        barra_busqueda_layout = QHBoxLayout()

        boton_busqueda = QPushButton("Buscar")
        boton_busqueda.setFixedWidth(50)
        input_busqueda = QLineEdit()
        input_busqueda.setPlaceholderText("Buscar...")
        input_busqueda.setFixedWidth(200)

        #barra_busqueda - composición
        barra_busqueda_layout.addWidget(input_busqueda)
        barra_busqueda_layout.addWidget(boton_busqueda)
        barra_busqueda_layout.setAlignment(input_busqueda, Qt.AlignmentFlag.AlignRight)

        #acciones_tabla_layout <-- acá estarán contenidos los botones y la tabla de datos
        acciones_usuario_layout = QHBoxLayout()
        acciones_botones_layout = QVBoxLayout()

            #acciones_botones_layout | botones 
        agregar_e = BotonAccionTabla("   Agregar\n   animal","Vista/Media/add-animal.png")
        self.modificar_e = BotonAccionTabla(" Modificar\n animal","Vista/Media/edit-animal.png")
        eliminar_e = BotonAccionTabla("  Eliminar\n  animal","Vista/Media/subtract-animal.png")

        #acciones_tabla_layout - composición
        self.componer_layout(acciones_botones_layout, [agregar_e, self.modificar_e, eliminar_e])

        acciones_botones_widget = QWidget()
        acciones_botones_widget.setLayout(acciones_botones_layout)
        acciones_botones_widget.setObjectName("contenedor-botones-tabla")

        #tabla
        tabla_datos = QTableWidget(4,4) #4 filas y 4 columnas
        tabla_datos.setHorizontalHeaderLabels(["Nombre", "Sexo", "Edad", "Peso", "Tipo"])
        tabla_datos.verticalHeader().setVisible(False)

        for col in range(4):
            tabla_datos.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)


        for i in range(tabla_datos.rowCount()):
            for j in range(tabla_datos.columnCount()):
                tabla_datos.setItem(i, j, QTableWidgetItem(f"Celda {i}, {j}"))

    


        #acciones_tabla_layout - composición
        acciones_usuario_layout.addWidget(acciones_botones_widget)
        acciones_usuario_layout.addWidget(tabla_datos)


        layout_principal = QVBoxLayout()
        layout_principal.addLayout(barra_busqueda_layout)
        layout_principal.addLayout(acciones_usuario_layout)


        self.setLayout(layout_principal)


    def componer_layout (self, layout, widgets):
        for w in widgets:
            layout.addWidget(w)

    def get_boton_modif_empleado (self):
        return self.modificar_e

    @classmethod
    def set_tabla_datos (cls, datos):
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

    @classmethod
    def set_tabla_datos (cls, datos):
        cls.info_tabla.extend(datos)