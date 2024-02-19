

class Playlists:
    def __init__(self,canciones):
        self.listaCanciones=canciones
        
    def MOSTRAR_CANCIONES_PLAYLIST(self):
        for cancion in self.listaCanciones:
            print(cancion.MOSTRAR_NFORMACION_CANCION())
