from persona import Persona
from datetime import date


class AdoptanteVistante(Persona):
    def __init__(self):
        super().__init__()
        self.__tipo = ""
        self.__direccion = ""
        self.__fecha_registro = None

    def get_tipo(self):
        print("tipo obtenido")
        return self.__tipo

    def set_tipo(self, tipo: str):
        print(f"tipo antigüo: {self.__tipo}")
        self.__tipo = tipo
        print(f"tipo actualizado: {self.__tipo}")

    def get_direccion(self):
        print("direccion obtenido")
        return self.__direccion

    def set_direccion(self, direccion: str):
        print(f"direccion antigüo: {self.__direccion}")
        self.__direccion = direccion
        print(f"direccion actualizado: {self.__direccion}")

    def get_fecha_registro(self):
        print("fecha_registro obtenido")
        return self.__fecha_registro

    def set_fecha_registro(self, fecha_registro: date):
        print(f"fecha_registro antigüo: {self.__fecha_registro}")
        self.__fecha_registro = fecha_registro
        print(f"fecha_registro actualizado: {self.__fecha_registro}")
