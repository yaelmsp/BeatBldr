class   Playlist:
    def __init__(self,id,titulo,id_propietario):
        self.__id=id
        self.__titulo=titulo
        self.__id_propietario=id_propietario

        
    @property
    def title(self):
        return self.__titulo

    @title.setter
    def name(self,nuevoTitulo):
      self.__titulo=nuevoTitulo
      
    @property
    def property_user(self):
        return self.__id_propietario

    @property_user.setter
    def property_user(self,nuevoPropetario):
      self.__id_propietario=nuevoPropetario
