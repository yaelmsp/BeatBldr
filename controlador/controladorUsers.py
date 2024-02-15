from controlador.gestores.Users import Users
from modelo.mock import CARGAR_LISTA_USUARIOS

class controladorUsers:
    def __init__(self):  
        self.usuarios = CARGAR_LISTA_USUARIOS()
        self.gestor_usuarios = Users(self.usuarios)
        
    def mostrar_usuarios(self):
        print(self.gestor_usuarios.MOSTRAR_LISTA())
        
    def login(self,nombre,contra):
       rest = self.gestor_usuarios.LOG_IN(nombre,contra)
       return rest
    
    def agregarUsu(self,nombre,ape,usu,pss):
        self.gestor_usuarios.AGREGAR_USUARIO(nombre,ape,usu,pss)    

    def modificarContrasenia(self,usu,passw):
        self.gestor_usuarios.CAMBIAR_CONTRA(usu,passw)


