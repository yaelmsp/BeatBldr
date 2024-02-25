

from controlador.instancias.Playlist import Playlist
from controlador.controladorUsers import controladorUsers


class Playlists:
    def __init__(self,playlists):
        self.__listaPlaylists=playlists


    def AGREGAR_PLAYLIST(self):
        
        idUserApp=controladorUsers()
        idPropietario=idUserApp.mostrarIdUsuario()
        
        idPlay=self.CREAR_ID()
        titulo=self.CREAR_TITULO_ALEATORIO(idPlay)
                   
        nuevaPlaylist=Playlist(idPlay,titulo,idPropietario)
        self.__listaPlaylists.append(nuevaPlaylist)
        
        
    def CREAR_TITULO_ALEATORIO(self,idPlay):
        idPlaylist=idPlay
        titulo="Playlist Nueva",idPlaylist
        return titulo
    
        
    def CAMBIAR_TITULO_PLAYLIST(self,nPlaylist,nuevoTitle):
           posicion = self.BUSCAR_POSICION_PLAYLIST(nPlaylist)
           if posicion != -1:
            self.__listaPlaylists[posicion].title = nuevoTitle 
           else:
               return -1

    def BUSCAR_POSICION_PLAYLIST(self,titulo):
        count=0
        found=False 
        playl=-1
        while count<len(self.__listaPlaylists) and found == False:
            if self.__listaPlaylists[count].title == titulo:
                 playl = self.__listaPlaylists.index(self.__listaPlaylists[count]) 
                 found = True
            count+=1  
        return playl
    
            
    def CREAR_ID(self):
        ultimoId = self.__listaPlaylists[-1].id
        return ultimoId +1
    
    def MOSTRAR_PLAYLIST(self,idPlay):
        print( self.__listaPlaylists[idPlay].MOSTRAR_INFO_PLAYLIST())