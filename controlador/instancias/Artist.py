class Artist:
    def __init__(self,id,nombre):
        self.id=id,
        self.nombre=nombre
        
    @property
    def name(self):
        return self.nombre
    
    @name.setter
    def name(self,nuevoNombre):
        self.nombre=nuevoNombre




