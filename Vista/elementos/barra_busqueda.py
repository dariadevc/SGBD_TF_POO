from __future__ import annotations
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QLineEdit,
)
from PyQt6.QtCore import Qt


class BarraBusqueda(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.boton_busqueda = QPushButton("Buscar")
        self.boton_busqueda.setFixedWidth(50)
        self.input_busqueda = QLineEdit()
        self.input_busqueda.setPlaceholderText("Buscar...")
        self.input_busqueda.setFixedWidth(200)

        # barra_busqueda - composición
        self.addWidget(self.input_busqueda)
        self.addWidget(self.boton_busqueda)
        self.setAlignment(self.input_busqueda, Qt.AlignmentFlag.AlignRight)

