from Controlador.ControladorLogin.ControladorLogin1 import ControladorLogin
from Controlador.ControladorJefe.ControladorSeccionEmpleado1 import ControladorSeccionEmpleado
from Controlador.ControladorJefe.ControladorSeccionAnimales import ControladorSeccionAnimales
from PyQt6.QtWidgets import QApplication
import sys

# ControladorSeccionEmpleado("C:/Users/LENOVO/Desktop/SGBD_TF_POO-vj_se_ver1/Vista/VistaJefe/style.qss")
# ControladorSeccionAnimales("C:/Users/Nico/Desktop/TP FINAL/SGBD_TF_POO-vj_se_ver1/Vista/VistaJefe/style.qss")

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    controlador = ControladorSeccionEmpleado("Vista\VistaJefe\style.qss")
    app.exec()



# app = QApplication(sys.argv)

# MiLogin = login()

# sys.exit(app.exec())  
    