from Vista.VistaPrincipal.vistaPrincipal import VistaPrincipal
from Vista.VistaPrincipal.directorVistaPrincipal import DirectorVistaPrincipal
from Vista.VistaPrincipal.builderVistaPrincipal import BuilderVistaPrincipal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from Vista.VistaPrincipal.concreteBuilderVistaPrincipal import ConcreteBuilderVistaPrincipal
import sys
from PyQt6.QtWidgets import QApplication


director = DirectorVistaPrincipal()
builder = ConcreteBuilderVistaPrincipal()

director.builder = builder

director.build_vista_empleado() #hay problemas al momento de construir el encabezado, se interrumpe el proceso

v_principal = builder.vista_principal

if __name__ == '__main__':
    app = QApplication([])
    with open("C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/vista_secciones/style.qss") as f:
        app.setStyleSheet(f.read())
    v_principal.show()
    app.exec()



