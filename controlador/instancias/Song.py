# from clases.Genre import Genre
class Song:
    def __init__(self,id,nombre,anio_publicacion,duracion):
        self.id=id
        self.nombre=nombre
        self.anio_publicacion=anio_publicacion
        self.duracion=duracion
    
    def MOSTRAR_NFORMACION_CANCION(self):
        respuesta= 'Nombre: ' , self.GET_NOMBRE(),  'artistas: ', self.GET_ARTISTAS() ,'generos: ', self.GET_GENEROS() ,'duracion: ', self.GET_DURACION(), 'anio publicacion: ', self.GET_ANIO_PUBLICACION() 
        return respuesta
    @property
    def name(self):
        return self.nombre

    @name.setter
    def name(self,nuevoNom):
      self.nombre=nuevoNom
    
    @property
    def publishDate(self):
        return self.anio_publicacion
    
    @publishDate.setter
    def publishDate(self,setAnio):
        self.anio_publicacion=setAnio
     
     @property
    def duration(self):
        return self.duracion
    
    @duration.setter
    def duration(self,nDuracion):
        self.duracion=nDuracion

        