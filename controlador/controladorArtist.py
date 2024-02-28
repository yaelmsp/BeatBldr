
from controlador.gestores.Artists import Artists
from modelo.mock import ListaArtitas

class controladorArtistas:
    def __init__(self):  
        self.artistas = ListaArtitas
        self.gestor_usuarios = Artists(self.artistas)
        
    def mostrar_artistas(self):
        print(self.gestor_usuarios.MOSTRAR_LISTA())    
        
    def mostrarNombresArtistas(self,idArtista):
        print('IDaRTISTA:',idArtista)
        return self.gestor_usuarios.BUSCAR_ARTISTA(idArtista)
        