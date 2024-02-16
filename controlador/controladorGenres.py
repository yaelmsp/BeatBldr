from controlador.gestores.Genres import Genres
from modelo.mock import CARGAR_LISTA_GENEROS

class controladorGenres:
    def __init__(self):  
        self.generos = CARGAR_LISTA_GENEROS()
        self.gestor_usuarios = Genres(self.generos)
        
    def mostrar_generos(self):
        return self.gestor_usuarios.MOSTRAR_LISTA()

    mostrar_generos()

