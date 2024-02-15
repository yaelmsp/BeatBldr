
from controlador.instancias.Genre import Genre


class Genres:
    def __init__(self,generos):
        self.ListaGeneros=generos

    def MOSTRAR_LISTA(self):
        lista=[]
        for generos in self.ListaGeneros:
            lista.append(generos.name)
        return lista
       
    def AGREGAR_GENERO(self,nombre):
         
        id=self.CREAR_ID()
       
        posicion=self.BUSCAR_POSICION_GENERO(nombre)
        
        while posicion != -1:
            nombre=str(input('indique otro genero: '))
            posicion=self.BUSCAR_POSICION_GENERO(nombre)
            
        nuevoGenero=Genre(id,nombre)
        self.ListaGeneros.append(nuevoGenero)
        
    def ELIMINAR_GENERO(self,generoElim):
        posicion = self.BUSCAR_POSICION_GENERO(generoElim)
        if posicion == -1:
            print('No existe ese genero')
        else:
            print(self.ListaGeneros[posicion].name)
            self.ListaGeneros.remove(posicion)
            
    def CREAR_ID(self):
        ultimoId = self.ListaGeneros[-1].id
        return ultimoId +1
    
    def BUSCAR_POSICION_GENERO(self,genero):
        count=0
        found=False 
        gen=-1
        while count<len(self.ListaGeneros) and found == False:
            if self.ListaGeneros[count].name== genero:
                 gen = self.ListaGeneros.index(self.ListaGeneros[count]) 
                 found = True
            count+=1  
        return gen



