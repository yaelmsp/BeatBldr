from controlador.gestores.Artists import Artists
from modelo.mock import CARGAR_LISTA_ARTISTAS

class controladorArtistas:
    def __init__(self):  
        self.artistas = CARGAR_LISTA_ARTISTAS()
        self.gestor_usuarios = Artists(self.artistas)
        
    def mostrar_artistas(self):
        print(self.gestor_usuarios.MOSTRAR_LISTA())      
        