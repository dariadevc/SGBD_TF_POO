from Controlador.ControladorLogin.ControladorLogin1 import ControladorLogin
from Controlador.ControladorJefe.ControladorSeccionEmpleado1 import ControladorSeccionEmpleado
from Controlador.ControladorJefe.ControladorSeccionAnimales import ControladorSeccionAnimales
from PyQt6.QtWidgets import QApplication
import sys

# ControladorSeccionEmpleado("Vista/VistaJefe/style.qss")
# ControladorSeccionAnimales("Vista/VistaJefe/style.qss")
# ControladorLogin("Vista/VistaLogin/estilos.qss")


if  __name__ == '__main__':
    app = QApplication(sys.argv)
    controlador = ControladorLogin("Vista\VistaLogin\estilos.qss")
    # if controlador.login():
    #     controlador.mostrar_ventana_seccion_empleado()
    app.exec()
