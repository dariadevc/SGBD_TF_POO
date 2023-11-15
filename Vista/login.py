import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap, QIcon, QPainter, QColor
from pathlib import Path


class RepeatedBackgroundWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Cargar la imagen de fondo
        self.background_image = QPixmap("C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Media/shelter-icon.png")
        self.background_image = self.background_image.scaled(100, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        background_color = QColor(236, 114, 11)
        painter.fillRect(self.rect(), background_color)
        for x in range(0, self.width(), self.background_image.width()):
            for y in range(0, self.height(), self.background_image.height()):
                painter.drawPixmap(x, y, self.background_image)


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 600)
        self.setWindowTitle("Inicio de sesión")
        fondo = RepeatedBackgroundWidget()
        self.setCentralWidget(fondo)
        self.layout().addWidget(self.generar_interfaz())
        # self.setCentralWidget(self.generar_interfaz())

    def generar_interfaz(self):
        interfaz_widget = QWidget()
        interfaz_widget.setFixedSize(300, 400)
        interfaz_widget.setGeometry(((self.width() - interfaz_widget.width()) // 2), ((self.height() - interfaz_widget.height()) // 2),
                                    interfaz_widget.width(), interfaz_widget.height())
        interfaz_widget.setObjectName("interfaz_widget")
        interfaz_layout = QVBoxLayout()
        logo = QLabel()
        logo.setFixedSize(90, 70)
        logo.setPixmap(QPixmap('C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Media/logo-bsf.png').scaled(logo.width(), logo.height()))
        logo.setObjectName("logo")
        interfaz_layout.addWidget(logo)
        interfaz_layout.addLayout(self.generar_formulario())
        interfaz_layout.setAlignment(logo, Qt.AlignmentFlag.AlignHCenter)
        interfaz_widget.setLayout(interfaz_layout)
        interfaz_widget.setObjectName("interfaz_widget")
        # self.show()

        return interfaz_widget

    def contrasenia_visible(self, clicked):
        if clicked:
            self.contrasenia_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.contrasenia_input.setEchoMode(QLineEdit.EchoMode.Password)

    # def login(self):
    #     usuario = Usuario(self.get_usuario(), self.get_contrasenia())
    #     usuario.login()

    def realizar_registro(self):
        pass

    def get_contrasenia(self):
        return self.contrasenia_input.text()

    def get_usuario(self):
        return self.user_input.text()

    def get_boton_login(self):
        return self.boton_login

    def generar_formulario(self):
        self.si_logueo = False
        formulario_layout = QVBoxLayout()
        user_label = QLabel("Usuario")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario")

        titulo_label = QLabel("Best Friends")
        titulo_label.setObjectName("titulo_label")

        contrasenia_label = QLabel("Contraseña")
        self.contrasenia_input = QLineEdit()
        self.contrasenia_input.setPlaceholderText("Contraseña")
        self.contrasenia_input.setEchoMode(QLineEdit.EchoMode.Password)  # oculta el texto ingresado

        self.ver_contrasenia = QCheckBox("Ver contraseña")
        self.ver_contrasenia.toggled.connect(self.contrasenia_visible)

        self.boton_login = QPushButton("Ingresar")
        # self.boton_login.clicked.connect(self.login())

        boton_registrarse = QPushButton("Registrarse")
        boton_registrarse.clicked.connect(self.realizar_registro)

        self.unLabel = QLabel()

        formulario_layout.addWidget(titulo_label)
        formulario_layout.addStretch(1)
        formulario_layout.addWidget(user_label)
        formulario_layout.addWidget(self.user_input)
        formulario_layout.addWidget(contrasenia_label)
        formulario_layout.addWidget(self.contrasenia_input)
        formulario_layout.addWidget(self.ver_contrasenia)
        formulario_layout.addWidget(self.unLabel)
        formulario_layout.addStretch(1)
        formulario_layout.addWidget(self.boton_login)
        formulario_layout.addWidget(boton_registrarse)
        formulario_layout.setAlignment(titulo_label, Qt.AlignmentFlag.AlignHCenter)
        formulario_layout.setAlignment(user_label, Qt.AlignmentFlag.AlignHCenter)
        formulario_layout.setAlignment(self.user_input, Qt.AlignmentFlag.AlignHCenter)
        formulario_layout.setAlignment(contrasenia_label, Qt.AlignmentFlag.AlignHCenter)
        formulario_layout.setAlignment(self.contrasenia_input, Qt.AlignmentFlag.AlignHCenter)
        formulario_layout.setAlignment(self.boton_login, Qt.AlignmentFlag.AlignHCenter)
        formulario_layout.setAlignment(boton_registrarse, Qt.AlignmentFlag.AlignHCenter)


        return formulario_layout


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Login()
#     window.show()
#     sys.exit(app.exec())