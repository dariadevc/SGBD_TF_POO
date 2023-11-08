from __future__ import annotations
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
)
from Controlador.ControladorJefe.controlador_seccion_animales import (
    ControladorSeccionAnimales,
)
from Vista.elementos.encabezado import EncabezadoVista


class ControladorGeneral:
    def __init__(self, estilo) -> None:
        self.__window = QMainWindow()
        self.__window.setWindowTitle("BestFriends")
        self.__window.setGeometry(100, 100, 800, 600)

        self.vista_actual = QStackedWidget()

        self.encabezado = EncabezadoVista()

        # Crear vistas
        self.vistaAnimal = ControladorSeccionAnimales()
        self.vistaAdopciones = Vista1("Vista Adopciones")

        # Agregar vistas al QStackedWidget
        self.vista_actual.addWidget(self.vistaAnimal.window)
        self.vista_actual.addWidget(self.vistaAdopciones)

        self.boton_actual = None

        self.encabezado.get_boton_adopcion().clicked.connect(
            self.mostrar_vista_adopciones
        )
        self.encabezado.get_boton_adopcion().clicked.connect(
            lambda: self.resaltar_boton(self.encabezado.get_boton_adopcion())
        )

        self.encabezado.get_boton_animales().clicked.connect(self.mostrar_vista_animal)
        self.encabezado.get_boton_animales().clicked.connect(
            lambda: self.resaltar_boton(self.encabezado.get_boton_animales())
        )

        boton_actualizar = QPushButton("Actualizar Vista")
        boton_actualizar.clicked.connect(self.actualizar_vista)

        layout = QVBoxLayout()
        layout.addLayout(self.encabezado)
        layout.addWidget(boton_actualizar)
        layout.addWidget(self.vista_actual)  # stacked

        widget = QWidget()
        widget.setLayout(layout)

        self.__window.setCentralWidget(widget)

        with open(estilo) as f:
            self.__window.setStyleSheet(f.read())

    def actualizar_vista(self):
        # solo funciona para una vista, debería poder usar .currentWidget() para obtener los
        # datos de la vista que se está mostrando
        self.vista_actual.currentWidget()

        nuevos_datos = self.vistaAnimal.obtener_datos()
        nuevos_datos = self.vista_actual.currentWidget()
        self.vistaAnimal.window.tabla_datos.actualizar_tabla(nuevos_datos)

    def mostrar_vista_adopciones(self):
        self.vista_actual.setCurrentWidget(self.vistaAdopciones)

    def mostrar_vista_animal(self):
        self.vista_actual.setCurrentWidget(self.vistaAnimal.window)

    def resaltar_boton(self, boton):
        if self.boton_actual is not None:
            # Restablecer el estilo del botón previamente seleccionado
            self.boton_actual.setStyleSheet("")
        # Establecer el nuevo botón como el botón actual
        self.boton_actual = boton
        # Aplicar un estilo para resaltarlo
        boton.setStyleSheet("background-color: #e655c4;")

    @property
    def window(self):
        return self.__window


class Vista1(QWidget):
    def __init__(self, nombre, parent=None):
        super().__init__(parent)

        self.label = QLabel(nombre, self)
        self.wid = QPushButton("Un boton")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.wid)
        self.setLayout(layout)


# if __name__ == "__main__":
#     app = QApplication([])
#     with open(estilo) as f:
#         app.setStyleSheet(f.read())
#     ventana = ControladorGeneral()
#     ventana.window.show()
#     app.exec()
