from controlador.instancias.Artist import Artist
from controlador.instancias.User import User
from controlador.instancias.Genre import Genre
from controlador.instancias.Song import Song
from controlador.instancias.Playlist import Playlist
from controlador.instancias.Country import Country
import pyodbc
#Cargado Datos

global ListaUsuario
global ListaGeneros
global ListaArtitas
global ListaSongs
global ListaPlaylists

#Listas Cambios
global ListaCambioPss
ListaCambioPss=[]

conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=INKAULA110;'
                          'Database=BeatBldr;'
                          'Trusted_Connection=yes;')


try:

    ListaUsuario=[]
    cursor = conn.cursor()
    sql='Select u.id,u.Nombre,u.Apellido,u.Usuario,c.id as pais, p.Contrasenia FROM Users as u, Passwords as p, Countrys as c WHERE u.id=p.id_Usuario and u.Pais=c.id'
    cursor.execute(sql)
    for row in cursor:
        nuevousu=User(row.id,row.Nombre,row.Apellido,row.Usuario,row.Contrasenia,row.pais)
        ListaUsuario.append(nuevousu)

    ListaGeneros=[]
    sql='Select * from Genres'
    cursor.execute(sql)
    for row in cursor:
        nuevoGenero=Genre(row.id,row.Tipo)
        ListaGeneros.append(nuevoGenero)

    ListaArtitas=[]
    sql='Select * from Artists'
    cursor.execute(sql)
    for row in cursor:
        nuevoartista=Artist(row.id,row.nombre)
        ListaArtitas.append(nuevoartista)
        
    ListaSongs=[]
    sql='Select * from Songs'
    cursor.execute(sql)
    for row in cursor:
        nuevaCancion=Song(row.id,row.nombre,row.anio_publicacion,row.duracion)
        ListaSongs.append(nuevaCancion)

    ListaPlaylists=[Playlist(1,'Playlist Prueba',1)] 

    ListaPaises=[]
    sql='Select * from Countrys'
    cursor.execute(sql)
    for row in cursor:
        nuevoPais=Country(row.id,row.Nombre)
        ListaPaises.append(nuevoPais)

    global ListaGenerosCanciones
    ListaGenerosCanciones=[]
    sql='Select * from ConexionCG'
    cursor.execute(sql)
    for row in cursor:
        conexionesCG=(row.id,row.idCanciones,row.idGenero)
        ListaGenerosCanciones.append(conexionesCG)

    global ListaArtstasCanciones
    ListaArtstasCanciones=[]
    sql='Select * from ConexionCA'
    cursor.execute(sql)
    for row in cursor:
        conexionesCA=(row.id,row.idCancion,row.idArtista)
        ListaArtstasCanciones.append(conexionesCA)

    global ListaCancionesPlaylist
    ListaCancionesPlaylist=[(1,1,1)]
    
except Exception as e:
    print("Ocurrio un error al cargar los datos: ", e)
finally:
    cursor.close()


def CAMBIO_CONTRASENIA_MOCK():
    id=ListaCambioPss[0][0]
    pss=ListaCambioPss[0][1]
    
    try:
        cursor = conn.cursor()
        sql='UPDATE Passwords SET Contrasenia=? WHERE id_Usuario= ? '
        cursor.execute(sql, (pss, id))
        cursor.commit()
    except Exception as e:
        print("Ocurrio un error al cargar los datos: ", e)
    finally:
        cursor.close()