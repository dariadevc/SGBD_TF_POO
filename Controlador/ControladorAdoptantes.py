from PyQt6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QMessageBox,
    QDateEdit,
    QPushButton,
    QLineEdit,
    QDialog,
    QGridLayout,
    QComboBox,
    QCheckBox,
)
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QAction
from Vista.seccion_adopciones_vista import SeccionAdopcionVista
from Modelo.database import DataBase


class ControladorSeccionAdoptantes:
    def __init__(self):
        self.__base = DataBase()
        self.__window = SeccionAdopcionVista()

        self.__window.tabla_datos.actualizar_tabla(self.obtener_datos())

        self.__window.get_boton_eliminar_animal().clicked.connect(
            self.eliminar_elemento
        )
        self.__window.get_boton_agregar_animal().clicked.connect(
            self.mostrar_ventana_agregar_animal
        )
        self.__window.get_input_busqueda().editingFinished.connect(self.buscar_animal)
        self.__window.get_input_busqueda().textChanged.connect(self.buscar_animal)

    @property
    def window(self) -> SeccionAdopcionVista:
        return self.__window

    def mostrar_ventana_modificar_animal(self):
        self.dialogo_eliminar = QDialog()
        self.dialogo_eliminar.setWindowTitle("Modificar Adoptante")

        layout = QVBoxLayout()

        dni_label = QLabel("DNI del empleado a Modificar:")
        self.dni_input = QLineEdit()
        self.eliminar_button = QPushButton("Modificar")
        layout.addWidget(dni_label)
        layout.addWidget(self.dni_input)
        layout.addWidget(self.eliminar_button)

        self.dialogo_eliminar.setLayout(layout)
        self.dialogo_eliminar.exec()

    def eliminar_elemento(self):
        elemento_seleccionado = self.window.tabla_datos.info_tabla.selectedItems()
        if not elemento_seleccionado:
            QMessageBox.warning(
                self.window,
                "Advertencia",
                "No ha seleccionado un elemento para eliminar. \n Para eliminar seleccione un elemento de la tabla",
            )
            return
        fila_seleccionada = elemento_seleccionado[0].row()
        id_selec = self.window.tabla_datos.info_tabla.item(fila_seleccionada, 0).text()
        elemento = self.__base.getAll(
            "SELECT codigo_animal, nombre_animal FROM public.animal WHERE codigo_animal = '{}'".format(
                id_selec
            )
        )
        confirma = f"¿Está seguro de que desea eliminar a {elemento[0][1]}?"
        reply = QMessageBox.question(
            self.window,
            "Confirmar eliminación",
            confirma,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.baja_logica_animal(elemento[0][0])
                QMessageBox.information(
                    self.window,
                    "Eliminado",
                    "Ha sido eliminada correctamente. \n Actualice la tabla para ver los cambios reflejados",
                )
            except Exception as e:
                print("no se pudo rip")

        else:
            QMessageBox.information(
                self.window, "Cancelado", "La eliminación ha sido cancelada."
            )

    def baja_logica_animal(self, id_animal):
        consulta = "UPDATE public.animal SET animal_eliminado = TRUE WHERE codigo_animal = '{}'".format(
            id_animal
        )
        self.__base.query(consulta)
        print("se cambió!")

    def mostrar_ventana_agregar_animal(self):
        dialogo_agregar = QDialog()
        dialogo_agregar.setWindowTitle("Agregar animal")
        dialogo_agregar.setGeometry(100, 100, 700, 400)

        nombre_animal_label = QLabel("Nombre:")
        self.nombre_animal_input = QLineEdit()
        self.nombre_animal_input.setText("Algo")

        label_tipo = QLabel("Tipo")
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["PERRO", "GATO"])

        label_sexo = QLabel("Sexo")
        self.combo_sexo = QComboBox()
        self.combo_sexo.addItems(["HEMBRA", "MACHO"])

        label_etapa = QLabel("Etapa de vida del animal ")
        self.combo_etapa = QComboBox()
        self.combo_etapa.addItems(["CACHORRO", "ADULTO"])

        edad_animal_label = QLabel("Edad:")
        self.edad_animal_input = QLineEdit()

        peso_animal_label = QLabel("Peso:")
        self.peso_animal_input = QLineEdit()

        label_tamanio = QLabel("Tamaño")
        self.combo_tamanio = QComboBox()
        self.combo_tamanio.addItems(["PEQUEÑO", "GRANDE", "MEDIANO"])

        descripcion_animal_label = QLabel("Breve descripción (Limite: 20 caracteres)")
        self.desc_animal_input = QLineEdit()

        check_castrado_label = QLabel("¿Está castrado?")
        self.check_castrado = QCheckBox()

        fecha_nac_animal_label = QLabel("Fecha de nacimiento")
        self.fecha_nac_input = QDateEdit()
        self.fecha_nac_input.setCalendarPopup(True)
        self.fecha_nac_input.setDate(QDate.currentDate())
        self.fecha_nac_input.setMinimumDate(self.fecha_nac_input.minimumDate())

        fecha_ing_animal_label = QLabel("Fecha de ingreso al refugio")
        self.fecha_ing_input = QDateEdit()
        self.fecha_ing_input.setCalendarPopup(True)
        self.fecha_ing_input.setDate(QDate.currentDate())
        self.fecha_ing_input.setMinimumDate(self.fecha_ing_input.minimumDate())

        boton_guardar = QPushButton("Guardar datos")

        layout = QGridLayout()
        layout.addWidget(nombre_animal_label, 0, 0)
        layout.addWidget(self.nombre_animal_input, 0, 1)
        layout.addWidget(label_tipo, 1, 0)
        layout.addWidget(self.combo_tipo, 1, 1)
        layout.addWidget(label_sexo, 2, 0)
        layout.addWidget(self.combo_sexo, 2, 1)
        layout.addWidget(label_etapa, 3, 0)
        layout.addWidget(self.combo_etapa, 3, 1)
        layout.addWidget(edad_animal_label, 4, 0)
        layout.addWidget(self.edad_animal_input, 4, 1)
        layout.addWidget(peso_animal_label, 5, 0)
        layout.addWidget(self.peso_animal_input, 5, 1)
        layout.addWidget(label_tamanio, 6, 0)
        layout.addWidget(self.combo_tamanio, 6, 1)
        layout.addWidget(descripcion_animal_label, 7, 0)
        layout.addWidget(self.desc_animal_input, 7, 1)
        layout.addWidget(fecha_nac_animal_label, 8, 0)
        layout.addWidget(self.fecha_nac_input, 8, 1)
        layout.addWidget(fecha_ing_animal_label, 9, 0)
        layout.addWidget(self.fecha_ing_input, 9, 1)
        layout.addWidget(check_castrado_label, 10, 0)
        layout.addWidget(self.check_castrado, 10, 1)
        layout.addWidget(boton_guardar, 11, 0, 1, 2)

        boton_guardar.clicked.connect(self.guardar_datos)

        dialogo_agregar.setLayout(layout)
        dialogo_agregar.exec()

    # hay que agregar el def eliminar

    def guardar_datos(self):
        # validaciones
        tipo_animal = self.combo_tipo.currentText()
        nombre_animal = self.nombre_animal_input.text()
        sexo_animal = self.combo_sexo.currentText()
        etapa_vida_animal = self.combo_etapa.currentText()
        edad_estimada_animal = self.edad_animal_input.text()
        peso_animal = self.peso_animal_input.text()
        tamanio_animal = self.combo_tamanio.currentText()
        descripcion_animal = self.desc_animal_input.text()
        animal_castrado = self.check_castrado.isChecked()
        fecha_nac_est = self.fecha_nac_input.date().toString("yyyy-MM-dd")
        fecha_ing = self.fecha_ing_input.date().toString("yyyy-MM-dd")

        try:
            consulta = "INSERT INTO public.animal (tipo_animal, nombre_animal, sexo_animal, etapa_vida_animal, edad_estimada_animal, peso_animal, tamaño_animal, descripcion_animal ,animal_castrado, fecha_nacimiento_estimada_animal, ingreso_refugio_animal) VALUES ('{}', '{}', '{}', '{}', {}, {}, '{}', '{}',{},'{}','{}')".format(
                tipo_animal,
                nombre_animal,
                sexo_animal,
                etapa_vida_animal,
                edad_estimada_animal,
                peso_animal,
                tamanio_animal,
                descripcion_animal,
                animal_castrado,
                fecha_nac_est,
                fecha_ing,
            )
            self.__base.query(consulta)
            # print("Datos guardados exitosamente.")
            t_animal = self.__base.get(
                "SELECT tipo_animal FROM public.animal ORDER BY id_animal DESC LIMIT 1"
            )[0][:3]
            id_animal = self.__base.get(
                "SELECT id_animal FROM public.animal ORDER BY id_animal DESC LIMIT 1"
            )[0]
            sex_animal = self.__base.get(
                "SELECT sexo_animal FROM public.animal ORDER BY id_animal DESC LIMIT 1"
            )[0][0]

            codi = f"{t_animal}{sex_animal}-{id_animal}"

            consulta2 = "UPDATE public.animal SET codigo_animal = '{}' WHERE id_animal = {}".format(
                codi, id_animal
            )
            self.__base.query(consulta2)

            QMessageBox.information(
                self.window,
                "Añadido con éxito",
                "Datos guardados exitosamente. \n Actualice la vista para ver los cambios reflejados",
            )
            print("Datos guardados exitosamente.")

        except Exception as e:
            print("Error al guardar los datos")
            QMessageBox.information(self.window, "Error", "Error al guardar los datos")

    def obtener_datos(self):
        datos = self.__base.getAll(
            "SELECT dni_adoptante_visitante, nombre_adoptante_visitante, apellido_adoptante_visitante, nro_cel_adoptante_visitante, email_adoptante_visitante, direccion_adoptante, fecha_registro_adoptante FROM public.adoptante_visitante WHERE adoptante_visitante_eliminado = FALSE"
        )
        print((datos))
        return datos

    def buscar_animal(self):
        datos = self.__base.getAll(
            "SELECT dni_adoptante_visitante, nombre_adoptante_visitante, apellido_adoptante_visitante, nro_cel_adoptante_visitante, email_adoptante_visitante, direccion_adoptante, fecha_registro_adoptante FROM public.adoptante_visitante WHERE tipo_animal = '{}'".format(
                self.__window.obtener_adoptante_buscado()
            )
        )
        print((datos))
        return datos
