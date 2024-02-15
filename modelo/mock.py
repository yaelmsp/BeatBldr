from controlador.instancias.User import User
from controlador.instancias.Genre import Genre
        
def CARGAR_LISTA_USUARIOS():
    ListaUsuario=[User(1,'yael','martinez','yaelmsp','1234'),User(2,'jose','p','joseluuu','1234')]
    return ListaUsuario

def CARGAR_LISTA_GENEROS():
     ListaGeneros=[Genre(1,'Rock'),Genre(2,'Pop'),Genre(3,'Metal'),Genre(4,'Techno')]
     return ListaGeneros
    
        