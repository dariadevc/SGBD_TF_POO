from Persona import Persona

class Empleado (Persona):
    def __init__(self, dni, nombre, apellido, nro_celular, email,alias,contrasenia, cuil,permiso_adopcion):
        super().__init__(dni, nombre, apellido, nro_celular, email)
        self.alias = alias
        self.contrasenia = contrasenia
        self.cuil = cuil
        self.permiso_adopcion = permiso_adopcion