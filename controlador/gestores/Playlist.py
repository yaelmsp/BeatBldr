

class Playlist:
    def __init__(self,id):
        self.id=id
        self.listaCanciones=[]
        
    def MOSTRAR_CANCIONES_PLAYLIST(self):
        for cancion in self.listaCanciones:
            print(cancion.MOSTRAR_NFORMACION_CANCION())
