from Modelo.DataBase import DataBase

class UsuarioDao:

    def __init__(self):
        self.base = DataBase()
    
    # def get_all(self):
    #     return self.base.getAll("SELECT * FROM Usuarios")

    # def get(self, id):
    #     return self.base.get("SELECT * FROM Usuarios WHERE id = {}".format(id))
    
    def login(self, usuario, contrasenia):
        return self.base.get("SELECT * FROM public.usuario as d WHERE nombre_usuario = '{}' and contrasenia_usuario  = '{}'".format(usuario, contrasenia))
    
    # def insert(self):
    #     pass

    # def update(self):
    #     pass

    # def delete(self):
    #     pass