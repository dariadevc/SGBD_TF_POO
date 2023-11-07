from Modelo.Personas.Persona import Persona
from Modelo.UsuarioDao import UsuarioDao


class Usuario(Persona):
    def __init__(self):
        super().__init__()
        self.__tipo_usuario = ""
        self.__alias = ""
        self.__contrasenia = ""
        self.__cuil = ""
        self.__permiso_adopcion = False
        self.__usuariodao = UsuarioDao()

    def login(self):
        result = self.__usuariodao.login(self.__alias, self.__contrasenia)
        return result

    def get_tipo_usuario(self):
        print("tipo_usuario obtenido")
        return self.__tipo_usuario

    def set_tipo_usuario(self, tipo_usuario: str):
        print(f"tipo_usuario antigüo: {self.__tipo_usuario}")
        self.__tipo_usuario = tipo_usuario
        print(f"tipo_usuario actualizado: {self.__tipo_usuario}")

    def get_alias(self):
        print("alias obtenido")
        return self.__alias

    def set_alias(self, alias: str):
        print(f"alias antigüo: {self.__alias}")
        self.__alias = alias
        print(f"alias actualizado: {self.__alias}")

    def get_contrasenia(self):
        print("contrasenia obtenido")
        return self.__contrasenia

    def set_contrasenia(self, contrasenia: str):
        print(f"contrasenia antigüo: {self.__contrasenia}")
        self.__contrasenia = contrasenia
        print(f"contrasenia actualizado: {self.__contrasenia}")

    def get_cuil(self):
        print("cuil obtenido")
        return self.__cuil

    def set_cuil(self, cuil: str):
        print(f"cuil antigüo: {self.__cuil}")
        self.__cuil = cuil
        print(f"cuil actualizado: {self.__cuil}")

    def get_permiso_adopcion(self):
        print("permiso_adopcion obtenido")
        return self.__permiso_adopcion

    def set_permiso_adopcion(self, permiso_adopcion: bool):
        print(f"permiso_adopcion antigüo: {self.__permiso_adopcion}")
        self.__permiso_adopcion = permiso_adopcion
        print(f"permiso_adopcion actualizado: {self.__permiso_adopcion}")
