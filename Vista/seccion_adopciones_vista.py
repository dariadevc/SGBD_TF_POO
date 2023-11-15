from __future__ import annotations
from PyQt6.QtWidgets import (
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
    QLabel,
    QLineEdit,
    QApplication,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt6.QtCore import Qt
import sys
from Vista.Elementos.Boton import BotonAccionTabla
from Vista.Elementos.Tabla import Tabla


class FormularioAdopcionVista(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.__dni_label = QLabel("Adoptante (DNI):")
        self.__dni_input = QLineEdit()

        self.__animal_label = QLabel("Animal (Código):")
        self.__animal_input = QLineEdit()

        self.__boton_enviar = QPushButton("Enviar Solicitud")
        # self.submit_button.clicked.connect(self.submit_form)

        layout.addWidget(self.__dni_label)
        layout.addWidget(self.__dni_input)
        layout.addWidget(self.__animal_label)
        layout.addWidget(self.__animal_input)
        layout.addWidget(self.__boton_enviar)

        self.setLayout(layout)

    def get_dni_adoptante(self):
        return self.__dni_input

    def get_cod_animal(self):
        return self.__animal_input

    def nuevo_adoptante(self):
        super().__init__()

        layout = QVBoxLayout()

        self.dni_label = QLabel(f"DNI del Adoptante:")
        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()
        self.lastname_label = QLabel("Apellido:")
        self.lastname_input = QLineEdit()
        self.phone_label = QLabel("Número de Celular:")
        self.phone_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.address_label = QLabel("Dirección:")
        self.address_input = QLineEdit()

        self.submit_button = QPushButton("Enviar Solicitud")
        # self.submit_button.clicked.connect(self.submit_form)

        layout.addWidget(self.dni_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.lastname_label)
        layout.addWidget(self.lastname_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def visitante_a_adoptante(self):
        super().__init__()

        layout = QVBoxLayout()

        self.address_label = QLabel("Dirección:")
        self.address_input = QLineEdit()

        self.submit_button = QPushButton("Enviar Solicitud")
        # self.submit_button.clicked.connect(self.submit_form)

        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)


class AdopcionesAntiguasVista(QWidget):
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

        # acciones_tabla_layout <-- acá estarán contenidos los botones y la tabla de datos
        acciones_usuario_layout = QHBoxLayout()
        acciones_botones_layout = QVBoxLayout()

        # acciones_botones_layout | botones
        self.registrar_adopcion = BotonAccionTabla(
            "   Registrar\n   adopcion",
            "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/aniadir_registro.png",
        )
        self.modificar_registro = BotonAccionTabla(
            " Modificar\n registro",
            "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/modificar-registro.png",
        )
        self.eliminar_registro = BotonAccionTabla(
            "  Eliminar\n  registro",
            "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/eliminar-registro.png",
        )

        # acciones_tabla_layout - composición
        self.componer_layout(
            acciones_botones_layout,
            [self.registrar_adopcion, self.modificar_registro, self.eliminar_registro],
        )

        acciones_botones_widget = QWidget()
        acciones_botones_widget.setLayout(acciones_botones_layout)
        acciones_botones_widget.setObjectName("contenedor-botones-tabla")

        # tabla

        self.tabla_datos = Tabla()

        # acciones_tabla_layout - composición
        acciones_usuario_layout.addWidget(acciones_botones_widget)
        acciones_usuario_layout.addWidget(self.tabla_datos.info_tabla)
        # acciones_usuario_layout.addWidget(self.tabla_datos)

        self.boton_volver = QPushButton("Volver")

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(barra_busqueda_layout)
        layout_principal.addLayout(acciones_usuario_layout)
        layout_principal.addWidget(self.boton_volver)

        self.setLayout(layout_principal)

    def componer_layout(self, layout, widgets):
        for w in widgets:
            layout.addWidget(w)

    def get_boton_modif_registro(self):
        return self.modificar_registro

    def get_input_busqueda(self):
        return self.input_busqueda

    def obtener_adopcion_buscada(self):
        return self.input_busqueda.text()


class SeccionAdopcionVista(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana Principal")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QStackedWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.central_widget)
        self.setLayout(layout)

        self.button_widget = QWidget()
        layout = QVBoxLayout()

        self.boton_adopciones_antiguas = QPushButton("Acceder a \nAdopciones Antiguas")
        self.boton_genera_adopcion = QPushButton("Generar \nNueva Adopción")

        layout.addWidget(self.boton_adopciones_antiguas)
        layout.addWidget(self.boton_genera_adopcion)

        self.button_widget.setLayout(layout)

        self.central_widget.addWidget(self.button_widget)

    def mostrar_formulario_adopcion(self):
        formulario_adopcion = FormularioAdopcionVista()
        self.central_widget.addWidget(formulario_adopcion)
        self.central_widget.setCurrentWidget(formulario_adopcion)

    def get_boton_adopciones_antiguas(self):
        return self.boton_adopciones_antiguas

    def get_boton_genera_adopcion(self):
        return self.boton_genera_adopcion
