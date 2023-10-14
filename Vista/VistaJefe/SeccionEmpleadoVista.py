import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QHeaderView
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class SeccionEmpleadoVista (QMainWindow):

    def __init__(self):
        super().__init__()

        widget_principal = QWidget()
        self.setCentralWidget(widget_principal) #establece el widget principal de la ventana
        self.setGeometry(100, 100, 800, 600) #establece dimensiones y posición de la ventana (x, y, ancho, alto)

        #encabezado común para todas las vistas de VistaJefe --- ¿debería ir en una clase propia?
        encabezado_layout = QVBoxLayout()

        #elementos que contiene encabezado_layout
        banner_layout = QHBoxLayout()
        barra_nav_layout = QHBoxLayout()


        #banner | logo 
        logo = QPixmap("Vista/Media/logo-bsf.png")
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

        ruedita_png = QPixmap("Vista/Media/configuration-wheel-svgrepo-com.png")
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

        boton_seccion_empleado = QPushButton("Empleados")
        boton_seccion_animales = QPushButton("Animales")
        boton_seccion_clientes = QPushButton("Clientes")
        boton_seccion_citas = QPushButton("Citas")

        boton_seccion_empleado.setIcon(QIcon("Vista/Media/icon-empleado.png"))
        boton_seccion_animales.setIcon(QIcon("Vista/Media/icon-animales.png"))
        boton_seccion_clientes.setIcon(QIcon("Vista/Media/icon-cliente.png"))
        boton_seccion_citas.setIcon(QIcon("Vista/Media/icon-citas.png"))

        boton_seccion_empleado.setObjectName("boton-nav")
        boton_seccion_animales.setObjectName("boton-nav")
        boton_seccion_clientes.setObjectName("boton-nav")
        boton_seccion_citas.setObjectName("boton-nav")

        #barra_nav - composición
        barra_nav_layout.addWidget(boton_seccion_empleado)
        barra_nav_layout.addWidget(boton_seccion_animales)
        barra_nav_layout.addWidget(boton_seccion_clientes)
        barra_nav_layout.addWidget(boton_seccion_citas)


        barra_nav_widget = QWidget()
        barra_nav_widget.setLayout(barra_nav_layout)
        barra_nav_widget.setObjectName("contenedor_botones_nav")

        #barra_busqueda | input de busqueda 
        barra_busqueda_layout = QHBoxLayout()

        input_busqueda = QLineEdit()
        input_busqueda.setPlaceholderText("Buscar...")
        input_busqueda.setFixedWidth(200)

        #barra_busqueda - composición
        barra_busqueda_layout.addWidget(input_busqueda)
        barra_busqueda_layout.setAlignment(input_busqueda, Qt.AlignmentFlag.AlignRight)


        #acciones_tabla_layout <-- acá estarán contenidos los botones y la tabla de datos
        acciones_tabla_layout = QHBoxLayout()
        acciones_botones_layout = QVBoxLayout()

            #acciones_botones_layout | botones 
        agregar_e = QPushButton("   Agregar\n   empleado")
        modificar_e = QPushButton(" Modificar\n empleado")
        eliminar_e = QPushButton("  Eliminar\n  empleado")

        agregar_e.setIcon(QIcon("Vista/Media/user-plus-svgrepo-com.png"))
        modificar_e.setIcon(QIcon("Vista/Media/user-pen-svgrepo-com.png"))
        eliminar_e.setIcon(QIcon("Vista/Media/user-xmark-svgrepo-com.png"))

        agregar_e.setObjectName("boton-tabla")
        modificar_e.setObjectName("boton-tabla")
        eliminar_e.setObjectName("boton-tabla")

        acciones_botones_layout.addWidget(agregar_e)
        acciones_botones_layout.addWidget(modificar_e)
        acciones_botones_layout.addWidget(eliminar_e)
        accion_bot = QWidget()
        accion_bot.setLayout(acciones_botones_layout)
        accion_bot.setObjectName("contenedor-botones-tabla")


        #tabla

        tabla_datos = QTableWidget()
        tabla_datos.setRowCount(4)
        tabla_datos.setColumnCount(4)

        encabezados_tabla = ["DNI", "APELLIDO", "NOMBRE", "FECHA DE INGRESO"]
        tabla_datos.setHorizontalHeaderLabels(encabezados_tabla)

        for col in range(3):
            tabla_datos.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)

        tabla_datos.setColumnWidth(3, 200) #para que el ancho no corte el titulo de la columna en esa columna

        for i in range(4):
            for j in range(4):
                tabla_datos.setItem(i, j, QTableWidgetItem(f"Celda {i}, {j}"))


        #acciones_tabla_layout - composición
        acciones_tabla_layout.addWidget(accion_bot)
        acciones_tabla_layout.addWidget(tabla_datos)


        #encabezado_layout - composición
        encabezado_layout.addLayout(banner_layout)
        encabezado_layout.addWidget(barra_nav_widget)
        

        #layout principal - del widget principal
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(encabezado_layout)
        layout_principal.addLayout(barra_busqueda_layout)
        layout_principal.addLayout(acciones_tabla_layout)

        widget_principal.setLayout(layout_principal)
        
