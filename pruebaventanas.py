from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class SegundaVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Segunda Ventana")

class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primera Ventana")

        # Declarar la instancia de la segunda ventana como una variable miembro
        self.segunda_ventana = None

        boton_abrir_segunda_ventana = QPushButton("Abrir Segunda Ventana")
        boton_abrir_segunda_ventana.clicked.connect(self.abrir_segunda_ventana)

        layout = QVBoxLayout()
        layout.addWidget(boton_abrir_segunda_ventana)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def abrir_segunda_ventana(self):
        # Verificar si la segunda ventana ya está abierta
        if self.segunda_ventana is None:
            self.segunda_ventana = SegundaVentana()
        self.segunda_ventana.show()

if __name__ == "__main__":
    app = QApplication([])
    ventana_principal = PrimeraVentana()
    ventana_principal.show()
    app.exec()
