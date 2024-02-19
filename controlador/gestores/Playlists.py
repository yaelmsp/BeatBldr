

class Playlists:
    def __init__(self,canciones):
        self.__listaPlaylists=canciones
        
    def MOSTRAR_CANCIONES_PLAYLIST(self):
        for cancion in self.__listaPlaylists:
            print(cancion.MOSTRAR_NFORMACION_CANCION())
