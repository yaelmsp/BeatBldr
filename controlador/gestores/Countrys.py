class Countrys:
    def __init__(self,paises):
        self.__listaPaises=paises
     
    def MOSTRAR_LISTA(self):
        lista=[]
        for paises in self.__listaPaises:
            lista.append(paises.name)
        return lista

                
    def BUSCAR_POSICION_PAIS(self,pais):
        count=0
        found=False 
        paisFinal=-1
        while count<len(self.__listaPaises) and found == False:
            if self.__listaPaises[count].name == pais:
                 paisFinal = self.__listaPaises.index(self.__listaPaises[count]) 
                 found = True
            count+=1  
        return paisFinal



