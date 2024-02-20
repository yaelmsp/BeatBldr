from controlador.gestores.Genres import Genres
from modelo.mock import ListaGeneros

class controladorGenres:
    def __init__(self):  
        self.generos = ListaGeneros
        self.gestor_usuarios = Genres(self.generos)
        
    def mostrar_generos(self):
        return self.gestor_usuarios.MOSTRAR_LISTA()


