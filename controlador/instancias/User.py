class User:

    def __init__(self,id,nombre,ape,usu,contra):
        self.__id=id
        self.__nombre=nombre
        self.__apellido=ape
        self.__nombre_usuario=usu
        self.__contrasenia=contra
      
        
    @property   
    def name(self):
        # print(self.nombre)
        return self.__nombre
    
    @name.setter
    def name(self,nuevoNombre):
      self.__nombre = nuevoNombre
      # print(self.GET_NOMBRE())

    @property
    def userName(self):
        return self.__nombre_usuario
    
    @userName.setter
    def userName(self,usuNuevo):
        self.__nombre_usuario = usuNuevo
        # print(self.GET_NOMBRE_USUARIO())
        
    @property
    def password(self):
        # print(self.contrasenia)
        return self.__contrasenia
    
    @password.setter
    def setpassword(self,passw):
        self.__contrasenia = passw
        
    # @property    
    # def country(self):
    #     return self.pais
    
    # @country.setter
    # def  country(self,newCount):
    #     self.pais=newCount
    
    def GET_EDAD(self):
        anio_actual = 2023
        return anio_actual - self.anio_nacimiento
    
    def GET_USER(self):
       usuario = 'Nombre:', self.__nombre, 'Apellido:', self.__apellido ,'Usuario:', self.__nombre_usuario
       # print(usuario)
       return usuario
    





