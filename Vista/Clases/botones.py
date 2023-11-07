from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon

class BotonNavegador (QPushButton):
    def __init__(self, text: str, icon: str):
        super().__init__()
        self.setText(text)
        self.setIcon(QIcon(icon))
        self.setObjectName("boton-nav")

class BotonAccionTabla (QPushButton):
    def __init__(self, text: str, icon: str):
        super().__init__()
        self.setText(text)
        self.setIcon(QIcon(icon))
        self.setObjectName("boton-tabla")