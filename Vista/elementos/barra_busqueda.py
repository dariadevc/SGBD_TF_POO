from __future__ import annotations
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
)
from PyQt6.QtCore import Qt


class BarraBusqueda(QWidget):
    def __init__(self):
        # barra_busqueda | input de busqueda
        self.barra_busqueda_layout = QHBoxLayout()

        self.boton_busqueda = QPushButton("Buscar")
        self.boton_busqueda.setFixedWidth(50)
        self.input_busqueda = QLineEdit()
        self.input_busqueda.setPlaceholderText("Buscar...")
        self.input_busqueda.setFixedWidth(200)

        # barra_busqueda - composición
        self.barra_busqueda_layout.addWidget(self.input_busqueda)
        self.barra_busqueda_layout.addWidget(self.boton_busqueda)
        self.barra_busqueda_layout.setAlignment(
            self.input_busqueda, Qt.AlignmentFlag.AlignRight
        )

    def genera_barra(self):
        return self.barra_busqueda_layout
