import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication , QLabel , QWidget , QLineEdit , QPushButton , QMessageBox , QCheckBox, QVBoxLayout
from PyQt6.QtGui import QFont , QPixmap, QIcon, QPalette, QBrush
from pathlib import Path

class Login (QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Inicio de sesion'
        self.generarInterfaz()
    
    def generarInterfaz (self):
        # self.setGeometry(500,100,350,400)
        self.setFixedSize(350,600)
        self.setWindowTitle(self.title) 
        self.setWindowIcon(QIcon("TP FINAL/logo_TPFINAL.png"))
        label = QLabel(self)
        pixmap = QPixmap('TP FINAL/logo_TPFINAL.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        # self.setStyleSheet("background-color:#ffffffff")
        self.generar_formulario()
        self.show()



    def contrasenia_visible (self, clicked):
        if clicked:
            self.contra_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.contra_input.setEchoMode(QLineEdit.EchoMode.Password)


    def iniciar_sesion (self):
        pass
    
    def realizar_registro(self):
        pass
    
    
    def generar_formulario (self):
        self.si_logueo = False 
        user_Label = QLabel(self)
        user_Label.setText("Usuario")
        user_Label.setFont(QFont('Arial', 10))
        user_Label.move(150,105)
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Usuario")
        self.user_input.resize(250,24)
        self.user_input.move(70,139)
        
        titulo_label = QLabel(self);
        titulo_label.setText("Best Friends")
        titulo_label.move(87,50)
        titulo_label.setObjectName("titulo")
        titulo_label.setFont(QFont('Helvetica',30))
        
        contrasenia_Label = QLabel(self)
        contrasenia_Label.setText("Contraseña")
        contrasenia_Label.setFont(QFont('Arial', 10))
        contrasenia_Label.move(145,175)
        self.contra_input = QLineEdit(self)
        self.contra_input.setPlaceholderText("Contraseña")
        self.contra_input.resize(250,24)
        self.contra_input.move(70,200)
        self.contra_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.ver_contrasenia = QCheckBox(self)
        self.ver_contrasenia.setText("Ver contraseña")
        self.ver_contrasenia.move(70,230)
        self.ver_contrasenia.toggled.connect(self.contrasenia_visible)
        
        boton_loggin = QPushButton(self)
        boton_loggin.setText("Loggin")
        boton_loggin.resize(250,24)
        boton_loggin.move(70,280)
        boton_loggin.clicked.connect(self.iniciar_sesion)
        
        boton_registrarse = QPushButton(self)
        boton_registrarse.setText("Registrarse")
        boton_registrarse.resize(250,24)
        boton_registrarse.move(70,330)
        boton_registrarse.clicked.connect(self.realizar_registro)
        
        # label = QLabel(self)
        # pixmap = QPixmap('TP FINAL/logo_TPFINAL.png')
        # label.setPixmap(pixmap)
        # self.resize(pixmap.width(),pixmap.height())
        
        
        # cuadrado = QVBoxLayout()
        # cuadrado.addWidget(user_Label)
        # cuadrado.addWidget(self.user_input)
        # cuadrado.addWidget(contrasenia_Label)
        # cuadrado.addWidget(self.contra_input)
        # cuadrado.addWidget(label)
        # self.setLayout(cuadrado)
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('TP FINAL/estilos.qss').read_text())
    login = Login()
    sys.exit(app.exec())