class Country:
    def __init__(self,id,nombre):
        self.__id=id,
        self.__nombre=nombre
              
    @property    
    def name(self):
        return self.__nombre
    
    @name.setter
    def name(self,nuevoNombre):
        self.__nombre=nuevoNombre


