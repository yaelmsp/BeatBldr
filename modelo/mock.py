from controlador.instancias.Artist import Artist
from controlador.instancias.User import User
from controlador.instancias.Genre import Genre
from controlador.instancias.Song import Song
from controlador.instancias.Playlist import Playlist
from controlador.instancias.Country import Country
import pyodbc

global ListaUsuario
global ListaGeneros
global ListaArtitas
global ListaSongs
global ListaPlaylists


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=INKAULA110;'
                      'Database=BeatBldr;'
                      'Trusted_Connection=yes;')

ListaUsuario=[]
cursor = conn.cursor()
sql='Select u.id,u.Nombre,u.Apellido,u.Usuario,c.id as pais, p.Contrasenia FROM Users as u, Passwords as p, Countrys as c WHERE u.id=p.id_Usuario and u.Pais=c.id'
cursor.execute(sql)
for row in cursor:
    nuevousu=User(row.id,row.Nombre,row.Apellido,row.Usuario,row.Contrasenia,row.pais)
    ListaUsuario.append(nuevousu)
# cursor.close
        
# def CARGAR_LISTA_USUARIOS():
# global ListaUsuario
# ListaUsuario=[User(1,'yael','martinez','yaelmsp','1234',1),User(2,'jose','p','joseluuu','1234',4)]
    # return ListaUsuario

# def CARGAR_LISTA_GENEROS():
# global ListaGeneros

ListaGeneros=[]
# cursor = conn.cursor()
sql='Select * from Genres'
cursor.execute(sql)
for row in cursor:
    nuevoGenero=Genre(row.id,row.Tipo)
    ListaGeneros.append(nuevoGenero)
# cursor.close
# ListaGeneros=[Genre(1,'Rock'),Genre(2,'Pop'),Genre(3,'Metal'),Genre(4,'Techno')]
     # return ListaGeneros
    
# def CARGAR_LISTA_ARTISTAS():
# global ListaArtitas
ListaArtitas=[]
# cursor = conn.cursor()
sql='Select * from Artista'
cursor.execute(sql)
for row in cursor:
    nuevoartista=Artist(row.id,row.nombre)
    ListaArtitas.append(nuevoartista)
# cursor.close
# ListaArtitas=[Artist(1,'Ic3peak'),Artist(2,'Rosalia'),Artist(3,'Siniestro Total'),Artist(4,'BABYMETAL'),Artist(5,'The Whistlers')]
     # return ListaArtitas

# def CARGAR_LISTA_SONGS():
# global  ListaSongs
ListaSongs=[]
# cursor = conn.cursor()
sql='Select * from Songs'
cursor.execute(sql)
for row in cursor:
    nuevaCancion=Song(row.id,row.nombre,row.anio_publicacion,row.duracion)
    ListaSongs.append(nuevaCancion)
# cursor.close
# ListaSongs=[Song(1,'Death But Pretty',2020,147000),Song(2,'G3 N15',2020,247200),Song(3,'Bailare Sobre Tu Tumba',1985,183000),Song(4,'Gimme Chocolate!!',2014,211200),
#                 Song(5,'Broken Ties',2019,190200)] 
    # return ListaSongs

# def CARGAR_PLAYIST():
# global ListaPlaylists
ListaPlaylists=[Playlist(1,'Playlist Prueba',1)] 
    # return ListaPlaylists

# def CARGAR_PAISES():
# global ListaPaises
ListaPaises=[]
# cursor = conn.cursor()
sql='Select * from Countrys'
cursor.execute(sql)
for row in cursor:
    nuevoPais=Country(row.id,row.Nombre)
    ListaPaises.append(nuevoPais)
# cursor.close
# ListaPaises=[Country(1,'Espania'),Country(2,'Francia'),Country(3,'Portugal'),Country(4,'Italia'),Country(5,'Alemania'),Country(6,'Holanda'),
#                  Country(7,'Dinamarca'),Country(8,'Suiza'),Country(9,'Suecia'),Country(10,'Islas Britanicas'),Country(11,'Irlanda')]

global ListaGenerosCanciones
ListaGenerosCanciones=[]
# cursor = conn.cursor()
sql='Select * from ConexionCG'
cursor.execute(sql)
for row in cursor:
    conexionesCG=(row.id,row.idCanciones,row.idGenero)
    ListaGenerosCanciones.append(conexionesCG)
# cursor.close
# ListaGenerosCanciones=[(1,1,3),(2,1,2),(3,2,2),(4,3,1),(5,4,3),(6,5,4)]

global ListaArtstasCanciones
ListaArtstasCanciones=[]
# cursor = conn.cursor()
sql='Select * from ConexionCA'
cursor.execute(sql)
for row in cursor:
    conexionesCA=(row.id,row.idCancion,row.idArtista)
    ListaArtstasCanciones.append(conexionesCA)
cursor.close
# ListaArtstasCanciones=[(1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5)]

global ListaCancionesPlaylist
ListaCancionesPlaylist=[(1,1,1)]


