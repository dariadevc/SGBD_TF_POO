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
)
from PyQt6.QtCore import Qt
import sys
from Vista.elementos.botones import BotonAccionTabla
from Vista.elementos.tabla import Tabla


class FormularioAdopcionVista(QWidget):
    def __init__(self, parent_window):
        super().__init__()

        self.parent_window = parent_window

        layout = QVBoxLayout()

        self.dni_label = QLabel("Adoptante (DNI):")
        self.dni_input = QLineEdit()

        self.animal_label = QLabel("Animal (Código):")
        self.animal_input = QLineEdit()

        self.submit_button = QPushButton("Enviar Solicitud")
        self.submit_button.clicked.connect(self.submit_form)

        layout.addWidget(self.dni_label)
        layout.addWidget(self.dni_input)
        layout.addWidget(self.animal_label)
        layout.addWidget(self.animal_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def nuevo_adoptante(self):
        super().__init()

        layout = QVBoxLayout()

        self.dni_label = QLabel(f"DNI del Adoptante: {dni}")
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
        self.submit_button.clicked.connect(self.submit_form)

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
        super().__init()

        layout = QVBoxLayout()

        self.address_label = QLabel("Dirección:")
        self.address_input = QLineEdit()

        self.submit_button = QPushButton("Enviar Solicitud")
        self.submit_button.clicked.connect(self.submit_form)

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

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(barra_busqueda_layout)
        layout_principal.addLayout(acciones_usuario_layout)

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
        self.setCentralWidget(self.central_widget)

        button_widget = QWidget()
        layout = QVBoxLayout()

        boton_adopciones_antiguas = QPushButton("Acceder a \nAdopciones Antiguas")
        boton_genera_adopcion = QPushButton("Generar \nNueva Adopción")

        layout.addWidget(boton_adopciones_antiguas)
        layout.addWidget(boton_genera_adopcion)

        button_widget.setLayout(layout)

        self.central_widget.addWidget(button_widget)

        boton_adopciones_antiguas.clicked.connect(self.mostrar_adopciones_antiguas)
        boton_genera_adopcion.clicked.connect(self.muestra_formulario_adopcion)

    def mostrar_adopciones_antiguas(self):
        adopciones_antiguas_ventana = AdopcionesAntiguasVista()
        self.central_widget.addWidget(adopciones_antiguas_ventana)
        self.central_widget.setCurrentWidget(adopciones_antiguas_ventana)

    def muestra_formulario_adopcion(self):
        formulario_adopcion = FormularioAdopcionVista(self)
        self.central_widget.addWidget(formulario_adopcion)
        self.central_widget.setCurrentWidget(formulario_adopcion)
