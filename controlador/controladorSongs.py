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
        cancion=self.gestor_Canciones.COGER_GENEROS(1)
        print(cancion)
        
    

cancion=controladorSongs()
cancion.mostrarDatosCancion()
