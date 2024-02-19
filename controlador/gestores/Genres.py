
from controlador.instancias.Genre import Genre


class Genres:
    def __init__(self,generos):
        self.__listaGeneros=generos

    def MOSTRAR_LISTA(self):
        lista=[]
        for generos in self.__listaGeneros:
            lista.append(generos.name)
        return lista
       
    def AGREGAR_GENERO(self,nombre):
         
        id=self.CREAR_ID()
       
        posicion=self.BUSCAR_POSICION_GENERO(nombre)
        
        while posicion != -1:
            nombre=str(input('indique otro genero: '))
            posicion=self.BUSCAR_POSICION_GENERO(nombre)
            
        nuevoGenero=Genre(id,nombre)
        self.__listaGeneros.append(nuevoGenero)
        
    def ELIMINAR_GENERO(self,generoElim):
        posicion = self.BUSCAR_POSICION_GENERO(generoElim)
        if posicion == -1:
            print('No existe ese genero')
        else:
            print(self.__listaGeneros[posicion].name)
            self.__listaGeneros.remove(posicion)
            
    def CREAR_ID(self):
        ultimoId = self.__listaGeneros[-1].id
        return ultimoId +1
    
    def BUSCAR_POSICION_GENERO(self,genero):
        count=0
        found=False 
        gen=-1
        while count<len(self.__listaGeneros) and found == False:
            if self.__listaGeneros[count].name== genero:
                 gen = self.__listaGeneros.index(self.__listaGeneros[count]) 
                 found = True
            count+=1  
        return gen



