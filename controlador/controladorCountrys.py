from controlador.gestores.Countrys import Countrys
from modelo.mock import CARGAR_PAISES

class controladorCountrys:
    def __init__(self):  
        self.paises = CARGAR_PAISES()
        self.gestor_usuarios = Countrys(self.paises)
        
    def mostrar_paises(self):
        return self.gestor_usuarios.MOSTRAR_LISTA()


