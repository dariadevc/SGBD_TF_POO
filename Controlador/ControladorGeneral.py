
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from Controlador.ControladorAnimales import ControladorSeccionAnimales
from Controlador.ControladorEmpleados import ControladorSeccionEmpleado
from Vista.Elementos.Encabezado import EncabezadoVista


class ControladorGeneral:
    def __init__(self) -> None:
        self.__window = QMainWindow()
        self.__window.setWindowTitle("BestFriends")
        self.__window.setGeometry(100, 100, 800, 600)

        # boton = QPushButton("entraste!!!")
        # layout = QVBoxLayout()
        # layout.addWidget(boton)
        # widget = QWidget()
        # widget.setLayout(layout)
        # self.__window.setCentralWidget(widget)
        self.__window.show()

        self.vista_actual = QStackedWidget()

        self.encabezado = EncabezadoVista()

        # Crear vistas
        self.vistaAnimal = ControladorSeccionAnimales()
        self.vistaEmpleado = ControladorSeccionEmpleado()

        # Agregar vistas al QStackedWidget
        self.vista_actual.addWidget(self.vistaAnimal.window)
        self.vista_actual.addWidget(self.vistaEmpleado.window)

        self.boton_actual = None

        self.encabezado.get_boton_empleado().clicked.connect(self.mostrar_vista_empleado)
        self.encabezado.get_boton_empleado().clicked.connect(lambda: self.resaltar_boton(self.encabezado.get_boton_empleado()))

        self.encabezado.get_boton_animales().clicked.connect(self.mostrar_vista_animal)
        self.encabezado.get_boton_animales().clicked.connect(lambda: self.resaltar_boton(self.encabezado.get_boton_animales()))

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

        # with open(estilo) as f:
        #     self.__window.setStyleSheet(f.read())


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