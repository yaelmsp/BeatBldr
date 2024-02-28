
from controlador.instancias.Artist import Artist


class Artists:
    def __init__(self,artista):
        self.__listaArtistas=artista

    def MOSTRAR_LISTA(self):
        lista=[]
        for artista in self.__listaArtistas:
            lista.append(artista.name)
        return lista
       
    def AGREGAR_ARTISTA(self,nombre):
         
        id=self.CREAR_ID()
       
        posicion=self.BUSCAR_POSICION_ARTISTA(nombre)
        
        while posicion != -1:
            nombre=str(input('indique otro artista: '))
            posicion=self.BUSCAR_POSICION_ARTISTA(nombre)
            
        nuevoArtista=Artist(id,nombre)
        self.__listaArtistas.append(nuevoArtista)
        
    def ELIMINAR_GENERO(self,artistElim):
        posicion = self.BUSCAR_POSICION_ARTISTA(artistElim)
        if posicion == -1:
            print('No existe ese artista')
        else:
            print(self.__listaArtistas[posicion].name)
            self.__listaArtistas.remove(posicion)
            
    def CREAR_ID(self):
        ultimoId = self.__listaArtistas[-1].id
        return ultimoId +1
    
    def BUSCAR_POSICION_ARTISTA(self,artista):
        count=0
        found=False 
        art=-1
        while count<len(self.__listaArtistas) and found == False:
            if self.__listaArtistas[count].name== artista:
                 art = self.__listaArtistas.index(self.__listaArtistas[count]) 
                 found = True
            count+=1  
        return art

    def BUSCAR_ARTISTA(self,idArtista):
        listaNombreArtistas=[]
        for artista in self.__listaArtistas:
            if idArtista == artista.id:
                listaNombreArtistas.append(artista.name)
        return listaNombreArtistas

