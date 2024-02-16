from controlador.instancias.Artist import Artist
from controlador.instancias.User import User
from controlador.instancias.Genre import Genre
# from controlador.instancias.Song import Song
        
def CARGAR_LISTA_USUARIOS():
    ListaUsuario=[User(1,'yael','martinez','yaelmsp','1234'),User(2,'jose','p','joseluuu','1234')]
    return ListaUsuario

def CARGAR_LISTA_GENEROS():
     ListaGeneros=[Genre(1,'Rock'),Genre(2,'Pop'),Genre(3,'Metal'),Genre(4,'Techno')]
     return ListaGeneros
    
def CARGAR_LISTA_ARTISTAS():
     ListaArtitas=[Artist(1,'Ic3peak'),Artist(2,'Rosalia'),Artist(3,'Siniestro Total'),Artist(4,'BABYMETAL'),Artist(5,'The Whistlers')]
     return ListaArtitas

# def CARGAR_LISTA_SONGS():
#     ListaSongs=[Song(1,'Death But Pretty',2020,147000),Song(2,'G3 N15',2020,247200),Song(3,'Bailare Sobre Tu Tumba',1985,183000),Song(4,'Gimme Chocolate!!',2014,211200),
#                 Song(5,'Broken Ties',2019,190200)] 
#     return ListaSongs