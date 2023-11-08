import sys
from PyQt6.QtWidgets import QApplication
from Vista.vista_secciones.SeccionEmpleadoVista1 import SeccionEmpleadoVista
from Modelo.DataBase import DataBase


class ControladorSeccionEmpleado:
    def __init__(self, estilo):
        # app = QApplication(sys.argv)
        self.__base = DataBase()
        self.obtener_empleados()
        self.__window = SeccionEmpleadoVista()
        self.__window.setWindowTitle("Best Friends")
        self.__window.show()
        # empleado = self.__window.obtener_usuario_buscado()
        self.__window.get_input_busqueda().editingFinished.connect(self.buscar_empleado)
        self.__window.get_input_busqueda().textChanged.connect(self.buscar_empleado)
        # empleado = self.__window.obtener_usuario_buscado()
        # self.__window.get_input_busqueda().editingFinished.connect(self.buscar_empleado)

        self.__window.get_input_busqueda().textChanged.connect(self.buscar_empleado)
        self.__window.get_boton_eliminar().clicked.connect(self.mostrar_ventana_eliminar_empleado)
        self.__window.get_boton_agregar().clicked.connect(self.mostrar_ventana_agregar_empleado)

        with open(estilo) as f:
            self.__window.setStyleSheet(f.read())
        # app.exec()

    def obtener_empleados(self):
        SeccionEmpleadoVista.set_tabla_datos(
            self.__base.getAll(
                "SELECT dni_usuario, alias_usuario, nombre_usuario, apellido_usuario FROM public.usuario"
            )
        )

    # def get_ventana (self):
    #     return self.__window

    # def mostrar_ventana (self):
    #     return self.__window.show()

    def buscar_empleado(self):
        print("Buscando empleado")
        texto_busqueda = self.__window.obtener_usuario_buscado()
        resultados = self.__base.getAll("SELECT dni_usuario, nombre_usuario, nombre, apellido FROM public.usuario WHERE nombre_usuario = '{}'".format(texto_busqueda))
        self.__window.set_tabla_datos(resultados)

    def buscar_empleado(self):
        SeccionEmpleadoVista.set_tabla_datos(
            self.__base.getAll(
                "SELECT dni, nombre_usuario, nombre, apellido FROM public.usuarios WHERE nombre_usuario = '{}'".format(
                    self.__window.obtener_usuario_buscado()
                )
            )
        )
    def eliminar_empleado(self):
        print("Elimino empleado")
        texto_buscado = self.eliminar_button.text()
        if texto_buscado:
            consulta = ("DELETE FROM public.usuario WHERE dni_usuario = '{}'".format(texto_buscado))
            try:
                resultado = self.__base.query(consulta)
                if resultado is not None:
                    if self.__base.query("SELECT 1 FROM public.usuario WHERE dni_usuario = '{}'".format(texto_buscado,)):
                        print("Empleado eliminado")
                        self.dialogo_eliminar.close()
                    else:
                        mensaje = QMessageBox()
                        mensaje.setIcon(QMessageBox.Icon.Warning)
                        mensaje.setWindowTitle("Mensaje de Error")
                        mensaje.setText("No hay ningún usuario con ese DNI")
                        mensaje.exec()
                else:
                    print("Error en la consulta")
            except Exception as e:
                print("Error en la base de datos")
        else:
            print("El campo DNI esta vacio")

    def mostrar_ventana_eliminar_empleado(self):
        self.dialogo_eliminar = QDialog()
        self.dialogo_eliminar.setWindowTitle("Eliminar Empleado")

        layout = QVBoxLayout()

        dni_label = QLabel("DNI del empleado a eliminar:")
        self.dni_input = QLineEdit()
        self.eliminar_button = QPushButton("Eliminar")
        self.eliminar_button.clicked.connect(self.eliminar_empleado)
        layout.addWidget(dni_label)
        layout.addWidget(self.dni_input)
        layout.addWidget(self.eliminar_button)

        self.dialogo_eliminar.setLayout(layout)
        self.dialogo_eliminar.exec()

    def mostrar_ventana_agregar_empleado(self):
        dialog = QDialog()
        dialog.setWindowTitle("Agregar Empleado")
        dialog.setGeometry(100, 100, 400, 600)  # Aumenta la altura del cuadro de diálogo

        # Etiquetas y campos de entrada
        self.tipo_usuario_label = QLabel("Tipo de Usuario:")
        self.tipo_usuario_input = QLineEdit()
        self.dni_label = QLabel("DNI:")
        self.dni_input = QLineEdit()
        self.apellido_label = QLabel("Apellido:")
        self.apellido_input = QLineEdit()
        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.nro_cel_label = QLabel("Número de Celular:")
        self.nro_cel_input = QLineEdit()
        self.email_label = QLabel("Correo Electrónico:")
        self.email_input = QLineEdit()
        self.cuil_label = QLabel("CUIL:")
        self.cuil_input = QLineEdit()

    # Permiso de adopción (checkbox)
        self.permiso_adopcion_label = QLabel("Permiso de Adopción:")
        self.permiso_adopcion_checkbox = QCheckBox()

        # Botón para guardar
        guardar_button = QPushButton("Guardar")

        # Diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.tipo_usuario_label)
        layout.addWidget(self.tipo_usuario_input)
        layout.addWidget(self.dni_label)
        layout.addWidget(self.dni_input)
        layout.addWidget(self.apellido_label)
        layout.addWidget(self.apellido_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.nro_cel_label)
        layout.addWidget(self.nro_cel_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.cuil_label)
        layout.addWidget(self.cuil_input)
        layout.addWidget(self.permiso_adopcion_label)
        layout.addWidget(self.permiso_adopcion_checkbox)
        layout.addWidget(guardar_button)

        guardar_button.clicked.connect(self.guardar_datos)
        dialog.setLayout(layout)
        dialog.exec()

    def mostrar_mensaje_error(mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(mensaje)
        msg.setWindowTitle("Error")
        msg.exec()

    def mostrar_mensaje_exito(mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle("Éxito")
        msg.exec()

    def guardar_datos(self):
        # Validaciones
        tipo_usuario = self.tipo_usuario_input.text()
        dni = self.dni_input.text()
        apellido = self.apellido_input.text()
        nombre = self.nombre_input.text()
        nro_cel = self.nro_cel_input.text()
        email = self.email_input.text()
        cuil = self.cuil_input.text()
        permiso_adopcion = self.permiso_adopcion_checkbox.isChecked()

        if tipo_usuario not in ["Administrador", "Encargado"]:
            self.mostrar_mensaje_error("El tipo de usuario debe ser 'Administrador' o 'Encargado'.")
        elif not dni.isdigit() or len(dni) != 8:
            self.mostrar_mensaje_error("DNI debe ser un número de 8 dígitos.")
        elif len(nombre) > 20 or len(apellido) > 20:
            self.mostrar_mensaje_error("Nombre y apellido no deben superar los 20 caracteres.")
        elif len(nro_cel) != 10 or not nro_cel.isdigit():
            self.mostrar_mensaje_error("Número de celular debe tener 10 dígitos numéricos.")
        elif len(email) > 30:
            self.mostrar_mensaje_error("Correo electrónico no debe superar los 30 caracteres.")
        elif len(cuil) > 13:
            self.mostrar_mensaje_error("CUIL debe tener 13 caracteres.")
        else:
        # Si todas las validaciones son exitosas, procede a guardar los datos en la base de datos
            try:
            # Utiliza la conexión existente de la clase DataBase
                consulta = "INSERT INTO public.usuario (tipo_usuario, dni_usuario, apellido_usuario, nombre_usuario, nro_cel_usuario, email_usuario, cuil_usuario, permiso_adopcion) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(tipo_usuario,dni,apellido,nombre,nro_cel,email,cuil,permiso_adopcion)

                self.__base.query(consulta)

                print("Datos guardados exitosamente.")
            except Exception as e:
                print("Error al guardar los datos")