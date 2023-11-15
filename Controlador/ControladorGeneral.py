from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QHBoxLayout, QLabel
from Controlador.ControladorAnimales import ControladorSeccionAnimales
from Controlador.ControladorEmpleados import ControladorSeccionEmpleado
from Vista.Elementos.Encabezado import EncabezadoVista
from Controlador.ControladorAdopciones import ControladorSeccionAdopciones
from Modelo.database import DataBase


class ControladorGeneral:
    def __init__(self, user) -> None:
        self.__window = QMainWindow()
        self.__window.setWindowTitle("BestFriends")
        self.__window.setGeometry(100, 100, 800, 600)
        with open("C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Estilos/estilo_general.qss") as f:
            self.__window.setStyleSheet(f.read())
        self.__usuario = user


        self.vista_actual = QStackedWidget()
        self.encabezado = EncabezadoVista()

        # Crear vistas
        self.vistaAnimal = ControladorSeccionAnimales()
        self.vistaEmpleado = ControladorSeccionEmpleado()
        self.vistaAdopcion = ControladorSeccionAdopciones()
        self.vistaBienvenida = VistaBienvenida(self.__usuario[4])

        # Agregar vistas al QStackedWidget
        self.vista_actual.addWidget(self.vistaBienvenida)
        self.vista_actual.addWidget(self.vistaAnimal.window)
        self.vista_actual.addWidget(self.vistaEmpleado.window)
        self.vista_actual.addWidget(self.vistaAdopcion.window)


        self.boton_actual = None

        self.encabezado.get_boton_empleado().clicked.connect(self.mostrar_vista_empleado)
        self.encabezado.get_boton_empleado().clicked.connect(lambda: self.resaltar_boton(self.encabezado.get_boton_empleado()))

        self.encabezado.get_boton_animales().clicked.connect(self.mostrar_vista_animal)
        self.encabezado.get_boton_animales().clicked.connect(lambda: self.resaltar_boton(self.encabezado.get_boton_animales()))

        self.encabezado.get_boton_adopciones().clicked.connect(self.mostrar_vista_adopcion)
        self.encabezado.get_boton_adopciones().clicked.connect(lambda: self.resaltar_boton(self.encabezado.get_boton_adopciones()))

        boton_actualizar = QPushButton("Actualizar Vista")
        boton_actualizar.clicked.connect(self.actualizar_vista_animal)

        layout = QVBoxLayout()
        layout.addLayout(self.encabezado)
        layout.addWidget(boton_actualizar)
        layout.addWidget(self.vista_actual)  # stacked

        widget = QWidget()
        widget.setLayout(layout)

        self.__window.setCentralWidget(widget)
        self.__window.show()


    def actualizar_vista_animal(self):
        nuevos_datos = self.vistaAnimal.obtener_datos()
        self.vistaAnimal.window.tabla_datos.actualizar_tabla(nuevos_datos)


    def actualizar_vista_empleado(self):
        nuevos_datos = self.vistaEmpleado.obtener_datos()
        self.vistaEmpleado.window.tabla_datos.actualizar_tabla(nuevos_datos)


    def mostrar_vista_empleado(self):
        self.vista_actual.setCurrentWidget(self.vistaEmpleado.window)


    def mostrar_vista_animal(self):
        self.vista_actual.setCurrentWidget(self.vistaAnimal.window)

    def mostrar_vista_adopcion(self):
        self.vista_actual.setCurrentWidget(self.vistaAdopcion.window)
        print("deberia mostrar adopciones")


    def resaltar_boton(self, boton):
        if self.boton_actual is not None:
            # Restablecer el estilo del botón previamente seleccionado
            self.boton_actual.setStyleSheet("")
        # Establecer el nuevo botón como el botón actual
        self.boton_actual = boton
        # Aplicar un estilo para resaltarlo
        boton.setStyleSheet("background-color: #e655c4;")


class VistaBienvenida(QWidget):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        layout = QVBoxLayout()
        self.label = QLabel()
        fuente = self.label.font()
        fuente.setPointSize(50)
        self.label.setFont(fuente)
        layout.addWidget(self.label)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        self.seteaLabel()
    def seteaLabel (self):
        self.label.setText(f"BIENVENID@ {self.nombre}")

    @property
    def window(self):
        return self.__window