from controlador.gestores.Songs import Songs
from modelo.mock import ListaSongs
from modelo.mock import ListaGenerosCanciones
from modelo.mock import ListaArtstasCanciones
from controlador.gestores.Genres import Genres

class controladorSongs:
    def __init__(self):
        self.canciones=ListaSongs
        self.generosCancion=ListaGenerosCanciones
        self.artistasCancion=ListaArtstasCanciones
        self.gestor_Canciones= Songs(self.canciones,self.generosCancion,self.artistasCancion)
        self.controlador_generos=Genres()
           
    def mostrarDatosCancion(self):
        self.gestor_Canciones.MOSTRAR_LISTA_CANCIONES()
        
    def mostrarGenerosElegidos(self,generos):
        #Hacer for para recorrer tupla y conseguir el id, que habra que guarda a una lista 
        self.controlador_generos.BUSCAR_ID_GENERO()
        print("Generos Controlador: ", generos)
    

cancion=controladorSongs()
cancion.mostrarDatosCancion()
