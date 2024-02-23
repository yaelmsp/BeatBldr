from controlador.gestores.Playlists import Playlists
from modelo.mock import ListaPlaylists

class ControladorPlaylist:
        def __init__(self):  
            self.playlist = ListaPlaylists
            self.gestor_Playlist = Playlists(self.playlist)





