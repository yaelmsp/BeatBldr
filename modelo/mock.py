from controlador.instancias.Artist import Artist
from controlador.instancias.User import User
from controlador.instancias.Genre import Genre
from controlador.instancias.Song import Song
from controlador.instancias.Playlist import Playlist
from controlador.instancias.Country import Country


        
# def CARGAR_LISTA_USUARIOS():
global ListaUsuario
ListaUsuario=[User(1,'yael','martinez','yaelmsp','1234',1),User(2,'jose','p','joseluuu','1234',4)]
    # return ListaUsuario

# def CARGAR_LISTA_GENEROS():
global ListaGeneros
ListaGeneros=[Genre(1,'Rock'),Genre(2,'Pop'),Genre(3,'Metal'),Genre(4,'Techno')]
     # return ListaGeneros
    
# def CARGAR_LISTA_ARTISTAS():
global ListaArtitas
ListaArtitas=[Artist(1,'Ic3peak'),Artist(2,'Rosalia'),Artist(3,'Siniestro Total'),Artist(4,'BABYMETAL'),Artist(5,'The Whistlers')]
     # return ListaArtitas

# def CARGAR_LISTA_SONGS():
global  ListaSongs
ListaSongs=[Song(1,'Death But Pretty',2020,147000),Song(2,'G3 N15',2020,247200),Song(3,'Bailare Sobre Tu Tumba',1985,183000),Song(4,'Gimme Chocolate!!',2014,211200),
                Song(5,'Broken Ties',2019,190200)] 
    # return ListaSongs

# def CARGAR_PLAYIST():
global ListaPlaylists
ListaPlaylists=[Playlist(1,'Playlist Prueba',1)] 
    # return ListaPlaylists

# def CARGAR_PAISES():
global ListaPaises
ListaPaises=[Country(1,'Espania'),Country(2,'Francia'),Country(3,'Portugal'),Country(4,'Italia'),Country(5,'Alemania'),Country(6,'Holanda'),
                 Country(7,'Dinamarca'),Country(8,'Suiza'),Country(9,'Suecia'),Country(10,'Islas Britanicas'),Country(11,'Irlanda')]
    # return ListaPaises

global ListaGenerosCanciones
ListaGenerosCanciones=[(1,1,3),(2,1,2),(3,2,2),(4,3,1),(5,4,3),(5,4,1)]

global ListaArtstasCanciones
ListaArtstasCanciones=[(1,1,1)]

global ListaCancionesPlaylist
ListaCancionesPlaylist=[(1,1,1)]


