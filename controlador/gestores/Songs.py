from controlador.instancias.Song import Song
from modelo.mock import ListaGeneros

class Songs:
        def __init__(self,songs,generos,artistas):
            self.__listaCanciones=songs
            self.__listaCancionGeneros=generos
            self.__listaCancionArtista=artistas
            
           
        def AGREGAR_CANCION(self,nombre,anio,duracion):
            idc=self.CREAR_ID()
            nuevaCancion=Song(idc,nombre,anio,duracion)
            self.__listaCanciones.append(nuevaCancion)
    
        def ELIMINAR_CANCION_BY_NAME(self,cancionEliminar):
            # return
            posicion = self.BUSCAR_POSICION_CANCION(cancionEliminar)
            if posicion == -1:
                print('No existe esa cancion')
            else:
                print(self.__listaCanciones[posicion].MOSTRAR_NFORMACION_CANCION())
                self.__listaCanciones.remove(posicion)
                print(self.MOSTRAR_LISTA_CANCIONES())

    
        def BUSCAR_CANCION_BY_NAME(self,cancionBusqueda):   
            # return
               posicion = self.BUSCAR_POSICION_CANCION(cancionBusqueda)
               if posicion == -1:
                   print('No existe esa cancion')
               else:
                print(self.__listaCanciones[posicion].MOSTRAR_NFORMACION_CANCION())
       
        def MOSTRAR_LISTA_CANCIONES(self):
            for canciones in self.__listaCanciones:
                canciones.MOSTRAR_NFORMACION_CANCION()
                
        def ADJUNTAS_ARTISTAS_GENEROS(self):
            for cancion in self.__listaCanciones:
                idCancion=cancion.id
                genero=self.COGER_GENEROS(idCancion)
                artistas=self.COGER_ARTISTAS(idCancion)
                cancion.genre=genero
                cancion.artist=artistas

                
                   
        def BUSCAR_POSICION_CANCION(self,cancion):
            count=0
            found=False 
            cancions=-1
            while count<len(self.__listaCanciones) and found == False:
                if self.__listaCanciones[count].GET_NOMBRE_USUARIO() == cancion:
                     cancions = self.__listaCanciones.index(self.__listaCanciones[count]) 
                     found = True
                count+=1  
            return cancions
            
        def CREAR_ID(self):
            ultimoId=1
            if len(self.__listaCanciones) != 0:
                ultimoId = self.__listaCanciones[-1].id +1
            return ultimoId
               
        def COGER_GENEROS(self,idCancion):
            lista_generos=[]
            for genero in self.__listaCancionGeneros:
                if genero[1] == idCancion:
                    idGenero=genero[2]
                    lista_generos.append(idGenero)
            return lista_generos
            
                
        def COGER_ARTISTAS(self,idCancion):
            lista_artistas=[]
            for artista in self.__listaCancionArtista:
                if artista[1] == idCancion:
                   idArtistas=artista[2]
                   lista_artistas.append(idArtistas)
            return lista_artistas
   
        def BUSCAR_CANCIONES_GENERO(self,IdGeneros):
            listCancionesEncontradas=[]
            for cancion in self.__listaCanciones:
                for genero in cancion.genre:
                    if genero in IdGeneros:
                        listCancionesEncontradas.append(cancion.name)
            return listCancionesEncontradas
                        
            
            
          




