from __future__ import annotations
from PyQt6.QtWidgets import QMainWindow, QApplication , QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QStackedWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys 
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\Clases')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\vista_secciones')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Vista\\VistaPrincipal')

sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador\\ControladorJefe')
sys.path.append(r'C:\\Users\\Fiore\\Downloads\\prueba_build\\Controlador\\ControladorJefe\\ControladorSeccionAnimales.py')


from ControladorJefe.ControladorSeccionAnimales import ControladorSeccionAnimales
from ControladorJefe.ControladorSeccionAnimales import ControladorSeccionAnimales
from Vista.Clases.encabezado import EncabezadoVista



class ControladorGeneral():

    def __init__(self) -> None:

        self.__window = QMainWindow()
        self.__window.setWindowTitle("BestFriends")
        self.__window.setGeometry(100, 100, 800, 600)

        self.vista_actual = QStackedWidget()

        self.encabezado = EncabezadoVista()

        #Crear vistas
        self.vistaAnimal = ControladorSeccionAnimales()
        self.vistaAdopciones = Vista1("Vista Adopciones")
        
        # Agregar vistas al QStackedWidget
        self.vista_actual.addWidget(self.vistaAnimal.window)
        self.vista_actual.addWidget(self.vistaAdopciones)

        self.boton_actual = None 

        self.encabezado.get_boton_adopcion().clicked.connect(self.mostrar_vista_adopciones)
        self.encabezado.get_boton_adopcion().clicked.connect(lambda: self.resaltar_boton(self.encabezado.get_boton_adopcion()))

        self.encabezado.get_boton_animales().clicked.connect(self.mostrar_vista_animal)
        self.encabezado.get_boton_animales().clicked.connect(lambda: self.resaltar_boton(self.encabezado.get_boton_animales()))

        layout = QVBoxLayout()
        layout.addLayout(self.encabezado)
        layout.addWidget(self.vista_actual) #stacked

        widget = QWidget()
        widget.setLayout(layout)

        self.__window.setCentralWidget(widget)

    def mostrar_vista_adopciones (self):
        self.vista_actual.setCurrentWidget(self.vistaAdopciones)

    def mostrar_vista_animal (self):
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
    def window (self):
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



if __name__ == '__main__':
    app = QApplication([])
    with open("Vista/vista_secciones/style.qss") as f:
        app.setStyleSheet(f.read())
    ventana = ControladorGeneral()
    ventana.window.show()
    app.exec()
