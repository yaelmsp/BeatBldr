from controlador.gestores.Countrys import Countrys
from modelo.mock import ListaPaises

class controladorCountrys:
    def __init__(self):  
        self.paises = ListaPaises
        self.gestor_usuarios = Countrys(self.paises)
        
    def mostrar_paises(self):
        return self.gestor_usuarios.MOSTRAR_LISTA()

    def obtener_id(self,pais):
        posicion= self.gestor_usuarios.BUSCAR_POSICION_PAIS(pais)
        return posicion +1

