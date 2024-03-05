from re import S
from controlador.gestores.Songs import Songs
from modelo.mock import ListaSongs
from modelo.mock import ListaGenerosCanciones
from modelo.mock import ListaArtstasCanciones
from controlador.controladorGenres import controladorGenres
from controlador.controladorArtist import controladorArtistas


class controladorSongs:
    def __init__(self):
        self.canciones=ListaSongs
        self.generosCancion=ListaGenerosCanciones
        self.artistasCancion=ListaArtstasCanciones
        self.gestor_Canciones= Songs(self.canciones,self.generosCancion,self.artistasCancion)
        self.controlador_generos=controladorGenres()
        self.controlador_artista=controladorArtistas()
        
           
    def mostrarDatosCancion(self):
        self.gestor_Canciones.MOSTRAR_LISTA_CANCIONES()
        
    def mostrarGenerosElegidos(self,generos):
       self.gestor_Canciones.ADJUNTAS_ARTISTAS_GENEROS()
       idGeneros= self.controlador_generos.buscarIdGenero(generos)
       canciones=self.buscarCancionesGeneros(idGeneros)
       return canciones
    
    def mostrarArtistaCancion(self,idArtista):
      for artista in idArtista:
            return self.controlador_artista.mostrarNombresArtistas(artista)
       
     
    def buscarCancionesGeneros(self,idGeneros):
      count=0
      listaReproduccion=[]
      listaCanciones=[]
      canciones= self.gestor_Canciones.BUSCAR_CANCIONES_GENERO(idGeneros) 
      for cancion in canciones:
          cancionPlay = canciones[count][0]
          rest=self.mostrarArtistaCancion(cancion[1])[0] 
          frase= '{} - {}'.format(cancionPlay, rest)
          count=count+1
          
          listaReproduccion.append(frase)
      return listaReproduccion
