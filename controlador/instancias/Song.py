# from clases.Genre import Genre
from controlador.instancias.Genre import Genre
from controlador.instancias.Artist import Artist


class Song:
    def __init__(self,id,nombre,anio_publicacion,duracion):
        self.__id=id
        self.__nombre=nombre
        self.__anio_publicacion=anio_publicacion
        self.__duracion=duracion
        self.__listaGenerosCancion=[]
        self.__listaArtistasCancion=[]
        
    def MOSTRAR_NFORMACION_CANCION(self):
        # respuesta= 'Nombre: ' , self.name,'duracion: ', self.duration, 'anio publicacion: ', self.publishDate
        respuesta=self.name, "-", self.artist
        return respuesta
    
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__nombre

    @name.setter
    def name(self,nuevoNom):
      self.__nombre=nuevoNom
    
    @property
    def publishDate(self):
        return self.__anio_publicacion
    
    @publishDate.setter
    def publishDate(self,setAnio):
        self.__anio_publicacion=setAnio
     
    @property
    def duration(self):
        return self.__duracion
    
    @duration.setter
    def duration(self,nDuracion):
        self.__duracion=nDuracion
        
    @property
    def artist(self):
        artistas=[]
        for artista in self.__listaArtistasCancion:
            artistas.append(artista) 
        return artistas
        
    @artist.setter   
    def artist(self,artistas):
        for artista in artistas:
            self.__listaArtistasCancion.append(artista)
            
    @property
    def genre(self):
        generos=[]
        for genero in self.__listaGenerosCancion:
            generos.append( genero)
        return generos
        
    @genre.setter   
    def genre(self,generos):
        for genero in generos:
          self.__listaGenerosCancion.append(genero)

        