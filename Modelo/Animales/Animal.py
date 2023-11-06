class Animal:
    def __init__(self):
        # self.id_persona =
        self.__codigo = ""
        self.__tipo = ""
        self.__nombre = ""
        self.__sexo = ""
        self.__etapa_vida = None
        self.__edad_estimada = ""
        self.__peso = False
        self.__tamanio = ""
        self.__descripcion = ""
        self.__flag_castrado = False
        self.__fecha_nac_estimada = None
        self.__ingreso_refugio = None
        self.__flag_eliminado = False
        self.__causa_baja = ""

    def get_codigo(self):
        print("codigo obtenido")
        return self.__codigo

    def set_codigo(self, codigo: int):
        print(f"codigo antigüo: {self.__codigo}")
        self.__codigo = codigo
        print(f"codigo actualizado: {self.__codigo}")

    def get_tipo(self):
        print("tipo obtenido")
        return self.__tipo

    def set_tipo(self, tipo: str):
        print(f"tipo antigüo: {self.__tipo}")
        self.__tipo = tipo
        print(f"tipo actualizado: {self.__tipo}")

    def get_nombre(self):
        print("nombre obtenido")
        return self.__nombre

    def set_nombre(self, nombre: str):
        print(f"nombre antigüo: {self.__nombre}")
        self.__nombre = nombre
        print(f"nombre actualizado: {self.__nombre}")

    def get_sexo(self):
        print("sexo obtenido")
        return self.__sexo

    def set_sexo(self, sexo: int):
        print(f"sexo antigüo: {self.__sexo}")
        self.__sexo = sexo
        print(f"sexo actualizado: {self.__sexo}")

    def get_etapa_vida(self):
        print("etapa_vida obtenido")
        return self.__etapa_vida

    def set_etapa_vida(self, etapa_vida: str):
        print(f"etapa_vida antigüo: {self.__etapa_vida}")
        self.__etapa_vida = etapa_vida
        print(f"etapa_vida actualizado: {self.__etapa_vida}")

    def get_edad_estimada(self):
        print("edad_estimada obtenido")
        return self.__edad_estimada

    def set_edad_estimada(self, edad_estimada: str):
        print(f"edad_estimada antigüo: {self.__edad_estimada}")
        self.__edad_estimada = edad_estimada
        print(f"edad_estimada actualizado: {self.__edad_estimada}")

    def get_peso(self):
        print("peso obtenido")
        return self.__peso

    def set_peso(self, peso: str):
        print(f"peso antigüo: {self.__peso}")
        self.__peso = peso
        print(f"peso actualizado: {self.__peso}")

    def get_tamanio(self):
        print("tamanio obtenido")
        return self.__tamanio

    def set_tamanio(self, tamanio: str):
        print(f"tamanio antigüo: {self.__tamanio}")
        self.__tamanio = tamanio
        print(f"tamanio actualizado: {self.__tamanio}")

    def get_descripcion(self):
        print("descripcion obtenido")
        return self.__descripcion

    def set_descripcion(self, descripcion: str):
        print(f"descripcion antigüo: {self.__descripcion}")
        self.__descripcion = descripcion
        print(f"descripcion actualizado: {self.__descripcion}")

    def get_flag_castrado(self):
        print("flag_castrado obtenido")
        return self.__flag_castrado

    def set_flag_castrado(self, flag_castrado: bool):
        print(f"flag_castrado antigüo: {self.__flag_castrado}")
        self.__flag_castrado = flag_castrado
        print(f"flag_castrado actualizado: {self.__flag_castrado}")

    def get_fecha_nac_estimada(self):
        print("fecha_nac_estimada obtenido")
        return self.__fecha_nac_estimada

    def set_fecha_nac_estimada(self, fecha_nac_estimada: str):
        print(f"fecha_nac_estimada antigüo: {self.__fecha_nac_estimada}")
        self.__fecha_nac_estimada = fecha_nac_estimada
        print(f"fecha_nac_estimada actualizado: {self.__fecha_nac_estimada}")

    def get_ingreso_refugio(self):
        print("ingreso_refugio obtenido")
        return self.__ingreso_refugio

    def set_ingreso_refugio(self, ingreso_refugio: str):
        print(f"ingreso_refugio antigüo: {self.__ingreso_refugio}")
        self.__ingreso_refugio = ingreso_refugio
        print(f"ingreso_refugio actualizado: {self.__ingreso_refugio}")

    def get_flag_eliminado(self):
        print("flag_eliminado obtenida")
        return self.__flag_eliminado

    def set_flag_eliminado(self, flag_eliminado: bool):
        print(f"flag_eliminado antigüo: {self.__flag_eliminado}")
        self.__flag_eliminado = flag_eliminado
        print(f"flag_eliminado actualizado: {self.__flag_eliminado}")
        # if self.__flag_eliminado == True:
        #   self.__fecha_baja = date(today)? --> No se como poner la fecha actual

    def get_causa_baja(self):
        print("causa_baja obtenida")
        return self.__causa_baja

    def set_causa_baja(self, causa_baja: str):
        print(f"causa_baja antigüo: {self.__causa_baja}")
        self.__causa_baja = causa_baja
        print(f"causa_baja actualizado: {self.__causa_baja}")
