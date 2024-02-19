from controlador.instancias.User import User

class Users:    
    def __init__(self,usuarios):
        self.listaUsuario=usuarios
        
    def AGREGAR_USUARIO(self,nombre,ape,usu,pss):
         
        id=self.CREAR_ID()
       
        posicion=self.BUSCAR_POSICION_USUARIO(usu)
        
        while posicion != -1:
            usu=str(input('indique otro nombre usuario del alumno: '))
            posicion=self.BUSCAR_POSICION_USUARIO(usu)
            
        nuevousu=User(id,nombre,ape,usu,pss)
        self.listaUsuario.append(nuevousu)
        # self.MOSTRAR_LISTA()
          
    
    def ELIMINAR_USUARIO_BY_USUARIO(self,usuEliminar):
        posicion = self.BUSCAR_POSICION_USUARIO(usuEliminar)
        if posicion == -1:
            print('No existe ese usuario')
        else:
            print(self.listaUsuario[posicion].GET_USER())
            self.listaUsuario.remove(posicion)
            # self.MOSTRAR_LISTA()

    
    def BUSCAR_USUARIO_BY_USUARIO(self):   
           usuBusqueda=str(input('indica el nombre de usuario que quiere buscar: '))
           posicion = self.BUSCAR_POSICION_USUARIO(usuBusqueda)
           if posicion == -1:
               print('No existe ese usuario')
           else:
            print(self.listaUsuario[posicion].GET_USER())

                      
    def LOG_IN(self,usuarioname,contraCom):
        count = 0
        fin=False
        respuesta=0
        
        while count <= len(self.listaUsuario) and fin == False:
            if self.listaUsuario[count].userName == usuarioname and self.listaUsuario[count].password == contraCom:
                fin=True
                respuesta = 1
            elif self.listaUsuario[count].userName == usuarioname and self.listaUsuario[count].password != contraCom:
                print(self.listaUsuario[count].password)
                fin=True
                respuesta= 2
            elif self.listaUsuario[count].userName != usuarioname and self.listaUsuario[count].password != contraCom:
               fin=True
               respuesta = 3
            count+=1
        return respuesta
   
    def MOSTRAR_LISTA(self):
        for usu in self.listaUsuario:
            print(usu.GET_USER())
            
    def BUSCAR_POSICION_USUARIO(self,usuario):
        count=0
        found=False 
        user=-1
        while count<len(self.listaUsuario) and found == False:
            if self.listaUsuario[count].userName== usuario:
                 user = self.listaUsuario.index(self.listaUsuario[count]) 
                 found = True
            count+=1  
        return user
            
    def CREAR_ID(self):
        ultimoId = self.listaUsuario[-1].id
        return ultimoId +1
    
    def CAMBIAR_CONTRA(self,usu,passw):
        busqueda=self.BUSCAR_POSICION_USUARIO(usu)
        self.listaUsuario[busqueda].setpassword=passw       

          
