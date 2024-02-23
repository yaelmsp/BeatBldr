from controlador.gestores.Songs import Songs
from modelo.mock import ListaSongs
from modelo.mock import ListaGenerosCanciones
from modelo.mock import ListaArtstasCanciones

class controladorSongs:
    def __init__(self):
        self.canciones=ListaSongs
        self.generosCancion=ListaGenerosCanciones
        self.artistasCancion=ListaArtstasCanciones
        self.gestor_Canciones= Songs(self.canciones,self.generosCancion,self.artistasCancion)
           
    def mostrarDatosCancion(self):
        self.gestor_Canciones.MOSTRAR_LISTA_CANCIONES()
        
    

cancion=controladorSongs()
cancion.mostrarDatosCancion()
