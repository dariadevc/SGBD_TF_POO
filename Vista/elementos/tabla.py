import sys
from PyQt6.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt


class Tabla(QTableWidget):
    def __init__(self):
        super().__init__()
        self.encabezado_tabla = []
    def actualizar_tabla(self, nuevos_datos):
        self.setRowCount(0)  # vacia las filas de la tabla
        self.setColumnCount(0)

        nuevos_datos = nuevos_datos

        # self.rowCount(len(nuevos_datos))
        self.setRowCount(len(nuevos_datos))
        self.setColumnCount(len(nuevos_datos[0]))
        self.verticalHeader().setVisible(False)

        for c in range(len(nuevos_datos)):
            self.horizontalHeader().setSectionResizeMode(c, QHeaderView.ResizeMode.Stretch)

        for fila_idx, fila_info in enumerate(nuevos_datos):
            for columna_idx, columna_info in enumerate(fila_info):
                item = QTableWidgetItem(str(columna_info))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.setItem(fila_idx, columna_idx, item)

        for col in range(4):
            self.horizontalHeader().setSectionResizeMode(
                col, QHeaderView.ResizeMode.Stretch
            )

    def add_fila(self, datos_fila):
        posicion_fila = self.rowCount()
        self.insertRow(posicion_fila)

        for posicion_columna, item in enumerate(datos_fila):
            celda = QTableWidgetItem(item)
            self.setItem(posicion_fila, posicion_columna, celda)

    @property
    def info_tabla(self):
        return self
