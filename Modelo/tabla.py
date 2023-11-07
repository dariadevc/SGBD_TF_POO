import sys
from PyQt6.QtWidgets import QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QVBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt6.QtCore import Qt
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\Clases')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\vista_secciones')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\VistaPrincipal')

sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador\\ControladorJefe')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador\\ControladorJefe\\ControladorSeccionAnimales.py')

sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Modelo')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Modelo\\tabla')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Modelo\\Animal')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Modelo\\AnimalDao')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Modelo\\DataBase')

class Tabla(QTableWidget):

    def actualizar_tabla(self, nuevos_datos):
        self.setRowCount(0) #vacia las filas de la tabla
        self.setColumnCount(0)

        nuevos_datos = nuevos_datos

        self.rowCount(len(nuevos_datos))
        self.setColumnCount(len(nuevos_datos[0]))
        self.verticalHeader().setVisible(False)

        for fila_idx, fila_info in enumerate(nuevos_datos):
            for columna_idx, columna_info in enumerate(fila_info):
                item = QTableWidgetItem(str(columna_info))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.setItem(fila_idx, columna_idx, item)

        for col in range(4):
            self.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)


    def add_fila (self, datos_fila):
        posicion_fila = self.rowCount()
        self.insertRow(posicion_fila)

        for posicion_columna, item in enumerate(datos_fila):
            celda = QTableWidgetItem(item)
            self.setItem(posicion_fila, posicion_columna, celda)


        