class Persona:
    def __init__(self):
        # self.id_persona =
        self.__dni = None
        self.__nombre = ""
        self.__apellido = ""
        self.__nro_celular = None
        self.__email = ""
        self.__flag_eliminado = False
        self.__causa_baja = ""

    def get_dni(self):
        print("dni obtenido")
        return self.__dni

    def set_dni(self, dni: int):
        print(f"dni antigüo: {self.__dni}")
        self.__dni = dni
        print(f"dni actualizado: {self.__dni}")

    def get_nombre(self):
        print("nombre obtenido")
        return self.__nombre

    def set_nombre(self, nombre: str):
        print(f"nombre antigüo: {self.__nombre}")
        self.__nombre = nombre
        print(f"nombre actualizado: {self.__nombre}")

    def get_apellido(self):
        print("apellido obtenido")
        return self.__apellido

    def set_apellido(self, apellido: str):
        print(f"apellido antigüo: {self.__apellido}")
        self.__apellido = apellido
        print(f"apellido actualizado: {self.__apellido}")

    def get_nro_celular(self):
        print("nro_celular obtenido")
        return self.__nro_celular

    def set_nro_celular(self, nro_celular: int):
        print(f"nro_celular antigüo: {self.__nro_celular}")
        self.__nro_celular = nro_celular
        print(f"nro_celular actualizado: {self.__nro_celular}")

    def get_email(self):
        print("email obtenido")
        return self.__email

    def set_email(self, email: str):
        print(f"email antigüo: {self.__email}")
        self.__email = email
        print(f"email actualizado: {self.__email}")

    def get_flag_eliminado(self):
        print("flag_eliminado obtenida")
        return self.__flag_eliminado

    def set_flag_eliminado(self, flag_eliminado: bool):
        print(f"flag_eliminado antigüo: {self.__flag_eliminado}")
        self.__flag_eliminado = flag_eliminado
        print(f"flag_eliminado actualizado: {self.__flag_eliminado}")

    def get_causa_baja(self):
        print("causa_baja obtenida")
        return self.__causa_baja

    def set_causa_baja(self, causa_baja: str):
        print(f"causa_baja antigüo: {self.__causa_baja}")
        self.__causa_baja = causa_baja
        print(f"causa_baja actualizado: {self.__causa_baja}")
