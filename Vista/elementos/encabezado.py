from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from Vista.elementos.botones import BotonNavegador

class EncabezadoVista (QVBoxLayout): #encabezado común para todas las vistas de VistaJefe
    
    def __init__(self):
        super().__init__()

        #elementos que contiene el encabezado
        banner_layout = QHBoxLayout()
        barra_nav_layout = QHBoxLayout()

        #banner | logo 
        logo = QPixmap("C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/logo-bsf.png")
        logo = logo.scaled(43,32)
        logo_refugio_label = QLabel()
        logo_refugio_label.setPixmap(logo)


        #banner | titulo
        nombre_refugio_label = QLabel("Best Friends")
        nombre_refugio_label.setObjectName("nombre_refugio_label")

        #banner | usuario_layout
        usuario_layout = QHBoxLayout()
        tipo_usuario_label = QLabel("Usuario\nJefe")
        tipo_usuario_label.setAlignment(Qt.AlignmentFlag.AlignCenter) #centra el texto

        ruedita_png = QPixmap("C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/configuration-wheel-svgrepo-com.png")
        ruedita_png = ruedita_png.scaled(30,30)
        boton_opciones_usuario = QLabel()
        boton_opciones_usuario.setPixmap(ruedita_png)
        boton_opciones_usuario.setFixedSize(30,30)
        boton_opciones_usuario.setCursor(Qt.CursorShape.PointingHandCursor)

        usuario_layout.addWidget(tipo_usuario_label)
        usuario_layout.addWidget(boton_opciones_usuario)

        #banner - composición
        banner_layout.addWidget(logo_refugio_label)
        banner_layout.addWidget(nombre_refugio_label)
        banner_layout.addStretch(1) #<-- añade un espacio elastico entre los elementos entre los que esté puesto, puede haber más de un addStretch para generar espacios de distintos tamaños
        banner_layout.addLayout(usuario_layout)

        #barra_nav | botones
        # boton_seccion_empleado = BotonNavegador("Empleados", "Vista/Media/icon-empleado.png")
        self.boton_seccion_informes = BotonNavegador("Informes", "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/informe-icon.png")
        self.boton_seccion_animales = BotonNavegador("Animales", "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/icon-animales.png")
        self.boton_seccion_empleado = BotonNavegador("Empleados", "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/icon-empleado.png")
        self.boton_seccion_adoptantes = BotonNavegador("Adoptantes", "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/icon-adoptantes.png")
        self.boton_seccion_visitas = BotonNavegador("Visitas", "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/icon-citas.png")
        self.boton_seccion_visitantes = BotonNavegador("Visitantes", "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/icon-visitantes.png")
        self.boton_seccion_adopciones = BotonNavegador("Adopciones", "C:/Users/Fiore/OneDrive/Escritorio/SGBD_TF_POO/Vista/Media/icon-adopciones.png")

        #barra_nav - composición
        self.componer_layout(barra_nav_layout, [self.boton_seccion_informes, self.boton_seccion_empleado, self.boton_seccion_animales, self.boton_seccion_animales, self.boton_seccion_adoptantes, self.boton_seccion_visitas, self.boton_seccion_visitantes])

        #barra_nav - color fondo
        barra_nav_widget = QWidget()
        barra_nav_widget.setLayout(barra_nav_layout)
        barra_nav_widget.setObjectName("contenedor_botones_nav")

        self.addLayout(banner_layout)
        self.addWidget(barra_nav_widget)

    def componer_layout (self, layout:QHBoxLayout|QVBoxLayout, widgets:list):
        for w in widgets:
            layout.addWidget(w)

    def get_boton_empleado (self):
        return self.boton_seccion_empleado
    
    def get_boton_animales(self):
        return self.boton_seccion_animales