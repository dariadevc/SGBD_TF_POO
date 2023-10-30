from Modelo.UsuarioDao import UsuarioDao


class Usuario:

    def __init__(self, usuario, contrasenia):
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.__usuariodao = UsuarioDao()
    
    def login(self):
        result = self.__usuariodao.login(self.__usuario, self.__contrasenia)
        return result