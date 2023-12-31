from __future__ import annotations
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QHeaderView,
    QMessageBox,
    QDialog,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from Vista.elementos.barra_busqueda import BarraBusqueda
from Vista.elementos.botones import BotonNavegador, BotonAccionTabla
from Vista.elementos.encabezado_encargado import EncabezadoVista


class SeccionEmpleadoVista(QMainWindow):
    info_tabla = []

    def __init__(self):
        super().__init__()

        widget_principal = QWidget()
        self.setCentralWidget(
            widget_principal
        )  # establece el widget principal de la ventana
        self.setGeometry(
            100, 100, 800, 600
        )  # establece dimensiones y posición de la ventana (x, y, ancho, alto)
        self.setWindowIcon(QIcon("Vista/Media/logo-bsf.png"))

        # # barra_busqueda | input de busqueda
        barra_busqueda_layout = QHBoxLayout()

        self.input_busqueda = QLineEdit()
        self.input_busqueda.setPlaceholderText("Buscar...")
        self.input_busqueda.setFixedWidth(200)
        # self.input_busqueda.textChanged.connect(self.set_tabla_datos)

        # barra_busqueda - composición
        barra_busqueda_layout.addWidget(self.input_busqueda)
        barra_busqueda_layout.setAlignment(
            self.input_busqueda, Qt.AlignmentFlag.AlignRight
        )

        # acciones_tabla_layout <-- acá estarán contenidos los botones y la tabla de datos
        acciones_usuario_layout = QHBoxLayout()
        acciones_botones_layout = QVBoxLayout()

        # acciones_botones_layout | botones
        self.agregar_e = BotonAccionTabla(
            "   Agregar\n   empleado", "Vista/Media/user-plus-svgrepo-com.png"
        )
        self.modificar_e = BotonAccionTabla(
            " Modificar\n empleado", "Vista/Media/user-pen-svgrepo-com.png"
        )
        self.eliminar_e = BotonAccionTabla(
            "  Eliminar\n  empleado", "Vista/Media/user-xmark-svgrepo-com.png"
        )

        # acciones_tabla_layout - composición
        self.componer_layout(
            acciones_botones_layout, [self.agregar_e, self.modificar_e, self.eliminar_e]
        )

        acciones_botones_widget = QWidget()
        acciones_botones_widget.setLayout(acciones_botones_layout)
        acciones_botones_widget.setObjectName("contenedor-botones-tabla")

        # tabla
        tabla_datos = QTableWidget(4, 4)  # 4 filas y 4 columnas

        # info_tabla = [] <-- atributo de clase que estoy usando

        tabla_datos.setRowCount(len(SeccionEmpleadoVista.info_tabla))
        tabla_datos.setColumnCount(len(SeccionEmpleadoVista.info_tabla[0]))
        tabla_datos.setHorizontalHeaderLabels(["DNI", "USUARIO", "NOMBRE", "APELLIDO"])
        tabla_datos.verticalHeader().setVisible(False)

        for row_idx, row in enumerate(SeccionEmpleadoVista.info_tabla):
            for col_idx, col_data in enumerate(row):
                item = QTableWidgetItem(str(col_data))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                tabla_datos.setItem(row_idx, col_idx, item)

        #     for row_idx, row in enumerate(SeccionEmpleadoVista.info_tabla):
        #         dni = row[0]  # Índice 0 corresponde a la columna "nombre"
        #         nombre_usuario = row[1]  # Índice 1 corresponde a la columna "apellido"
        #         nombre = row[2]  # Índice 2 corresponde a la columna "edad"
        #         apellido = row[3]

        # # Llena la tabla con los valores seleccionados
        #     tabla_datos.setItem(row_idx, 0, QTableWidgetItem(dni))
        #     tabla_datos.setItem(row_idx, 1, QTableWidgetItem(nombre_usuario))
        #     tabla_datos.setItem(row_idx, 2, QTableWidgetItem(nombre))
        #     tabla_datos.setItem(row_idx, 3, QTableWidgetItem(apellido))
        # tabla_datos.setHorizontalHeaderLabels(["DNI", "APELLIDO", "NOMBRE", "FECHA DE INGRESO"])

        for col in range(4):
            tabla_datos.horizontalHeader().setSectionResizeMode(
                col, QHeaderView.ResizeMode.Stretch
            )

        tabla_datos.setColumnWidth(
            3, 200
        )  # para que el ancho no corte el titulo de la columna en esa columna

        # for i in range(tabla_datos.rowCount()):
        #     for j in range(tabla_datos.columnCount()):
        #         tabla_datos.setItem(i, j, QTableWidgetItem(f"Celda {i}, {j}"))

        # acciones_tabla_layout - composición
        acciones_usuario_layout.addWidget(acciones_botones_widget)
        acciones_usuario_layout.addWidget(tabla_datos)

        encabezado_layout = EncabezadoVista()  # construye el encabezado

        # layout principal - del widget principal
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(encabezado_layout)
        layout_principal.addLayout(barra_busqueda_layout)
        layout_principal.addLayout(acciones_usuario_layout)

        widget_principal.setLayout(layout_principal)

    def componer_layout(self, layout, widgets):
        for w in widgets:
            layout.addWidget(w)

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

    def obtener_usuario_buscado(self):
        return self.input_busqueda.text()

    def get_input_busqueda(self):
        return self.input_busqueda

    def get_boton_agregar(self):
        return self.agregar_e

    def get_boton_eliminar(self):
        return self.eliminar_e

    def get_boton_modificar(self):
        return self.modificar_e
