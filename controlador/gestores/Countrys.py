class Countrys:
    def __init__(self,paises):
        self.__listaPaises=paises
     
    def MOSTRAR_LISTA(self):
        lista=[]
        for paises in self.__listaPaises:
            lista.append(paises.name)
        return lista

    



