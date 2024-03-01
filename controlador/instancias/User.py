class User:

    def __init__(self,id,nombre,ape,usu,contra,pais):
        self.__id=id
        self.__nombre=nombre
        self.__apellido=ape
        self.__nombre_usuario=usu
        # self.__anio_nacimiento=anio_nacimiento
        self.__pais=pais
        self.__contrasenia=contra
      
    @property   
    def id(self):
        return self.__id

    @property   
    def name(self):
        return self.__nombre
    
    @name.setter
    def name(self,nuevoNombre):
      self.__nombre = nuevoNombre

    @property
    def userName(self):
        return self.__nombre_usuario
    
    @userName.setter
    def userName(self,usuNuevo):
        self.__nombre_usuario = usuNuevo
        
    @property
    def password(self):
        return self.__contrasenia
    
    @password.setter
    def setpassword(self,passw):
        self.__contrasenia = passw
        
    # @property    
    # def birth_date(self):
    #     return self.__anio_nacimiento
    
    # @birth_date.setter
    # def  birth_date(self,newBirth):
    #     self.__anio_nacimiento=newBirth
        
    @property    
    def country(self):
        return self.__pais
    
    @country.setter
    def  country(self,newPais):
        self.__pais=newPais
    
    def GET_EDAD(self):
        anio_actual = 2023
        return anio_actual - self.anio_nacimiento
    
    def GET_USER(self):
       usuario = 'Nombre:', self.__nombre, 'Apellido:', self.__apellido ,'Usuario:', self.__nombre_usuario, 'Pais:', self.__pais,'contra',self.__contrasenia
       return usuario
    





