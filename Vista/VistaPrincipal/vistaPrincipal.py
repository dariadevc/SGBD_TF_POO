from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class VistaPrincipal(QMainWindow):
    def __init__(self):
        self.encabezado = None
        self.secciones = []
        self.setGeometry(100, 100, 800, 600)

    def agregar_seccion(self, seccion):
        self.secciones.append(seccion)

    def eliminar_seccion(self):
        del self.secciones[-1]

    def componer_vista (self):
        layout_vista = QVBoxLayout()
        for seccion in self.secciones:
            if isinstance(seccion, QHBoxLayout) or isinstance(seccion, QVBoxLayout):
                layout_vista.addLayout(seccion)
            else:
                layout_vista.addWidget(seccion)
        widget_principal = QWidget()
        widget_principal.setLayout(layout_vista)
        self.setCentralWidget(widget_principal)

        return self
        
    


    def ejecutar_vista(self):
        pass
        # Agregar código para ejecutar ventana
        