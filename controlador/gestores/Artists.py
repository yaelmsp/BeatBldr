
from controlador.instancias.Artist import Artist


class Artists:
    def __init__(self,artista):
        self.ListaArtistas=artista

    def MOSTRAR_LISTA(self):
        lista=[]
        for artista in self.ListaArtistas:
            lista.append(artista.name)
        return lista
       
    def AGREGAR_ARTISTA(self,nombre):
         
        id=self.CREAR_ID()
       
        posicion=self.BUSCAR_POSICION_ARTISTA(nombre)
        
        while posicion != -1:
            nombre=str(input('indique otro artista: '))
            posicion=self.BUSCAR_POSICION_ARTISTA(nombre)
            
        nuevoArtista=Artist(id,nombre)
        self.ListaArtistas.append(nuevoArtista)
        
    def ELIMINAR_GENERO(self,artistElim):
        posicion = self.BUSCAR_POSICION_ARTISTA(artistElim)
        if posicion == -1:
            print('No existe ese artista')
        else:
            print(self.ListaArtistas[posicion].name)
            self.ListaArtistas.remove(posicion)
            
    def CREAR_ID(self):
        ultimoId = self.ListaArtistas[-1].id
        return ultimoId +1
    
    def BUSCAR_POSICION_ARTISTA(self,artista):
        count=0
        found=False 
        art=-1
        while count<len(self.ListaArtistas) and found == False:
            if self.ListaArtistas[count].name== artista:
                 art = self.ListaArtistas.index(self.ListaArtistas[count]) 
                 found = True
            count+=1  
        return art


