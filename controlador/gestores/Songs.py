from controlador.instancias.Song import Song

class Songs:
        def __init__(self,songs):
            self.__listaCanciones=songs
        
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
            # return 
            for canciones in self.__listaCanciones:
                print(canciones.MOSTRAR_NFORMACION_CANCION())
            
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
               

   

            
          




