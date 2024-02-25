from controlador.gestores.Users import Users
from modelo.mock import ListaUsuario

class controladorUsers:
    def __init__(self):  
        self.usuarios = ListaUsuario
        self.gestor_usuarios = Users(self.usuarios)
        self.idUsuarioApp=int 
        
    def mostrar_usuarios(self):
        self.gestor_usuarios.MOSTRAR_LISTA()
        
    def login(self,nombre,contra):
       rest = self.gestor_usuarios.LOG_IN(nombre,contra)
       posicion=self.gestor_usuarios.BUSCAR_POSICION_USUARIO(nombre)
       self.idUsuarioApp=self.usuarios[posicion].id
       return rest
    
    def agregarUsu(self,nombre,ape,usu,pss,pais):
        self.gestor_usuarios.AGREGAR_USUARIO(nombre,ape,usu,pss,pais)

    def modificarContrasenia(self,usu,passw):
        self.gestor_usuarios.CAMBIAR_CONTRA(usu,passw)
        
    def mostrarIdUsuario(self):
        return self.idUsuarioApp


