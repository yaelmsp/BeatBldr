class User:

    def __init__(self,id,nombre,ape,usu,contra):
        self.id=id
        self.nombre=nombre
        self.apellido=ape
        self.nombre_usuario=usu
        self.contrasenia=contra
      
        
    @property   
    def name(self):
        # print(self.nombre)
        return self.nombre
    
    @name.setter
    def name(self,nuevoNombre):
      self.nombre = nuevoNombre
      # print(self.GET_NOMBRE())

    @property
    def userName(self):
        return self.nombre_usuario
    
    @userName.setter
    def userName(self,usuNuevo):
        self.nombre_usuario = usuNuevo
        # print(self.GET_NOMBRE_USUARIO())
        
    @property
    def password(self):
        # print(self.contrasenia)
        return self.contrasenia
    
    @password.setter
    def setpassword(self,passw):
        self.contrasenia = passw
        
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
       usuario = 'Nombre:', self.nombre, 'Apellido:', self.apellido ,'Usuario:', self.nombre_usuario
       # print(usuario)
       return usuario
    





