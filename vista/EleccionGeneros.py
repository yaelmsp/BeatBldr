from PySide6.QtWidgets import (
    QApplication, QComboBox,QWidget,QDialog,QVBoxLayout,QDialogButtonBox)
import sys
from controlador.controladorGenres import controladorGenres
from vista.app import MainApp
from controlador.controladorPlaylist import ControladorPlaylist
from controlador.controladorUsers import controladorUsers




class Generos(QWidget):
    def __init__(self,oyentesElec,idUsuApp):
        super().__init__()
        self.idUsuApp=idUsuApp
        self.setWindowTitle("Elegir generos")
        self.oyentes = int(oyentesElec)
        self.controlador_generos=controladorGenres()
        self.controlador_playlist=ControladorPlaylist()
        self.controlador_usuarios=controladorUsers()
        self.ListaGeneros=[]
        self.ConversionArray()
        self.formulario()

        
    def ConversionArray(self):
         gen=self.controlador_generos.mostrar_generos()
         for genero in gen:
             self.ListaGeneros.append(genero)
         
        
    def formulario(self):
        dialogo = Dialogo(self.ListaGeneros,self.oyentes)
        rest=dialogo.exec()
        if rest:
            lista = dialogo.enviarParam()
            lista2=set(lista[-self.oyentes:])
            self.mostrarApp(lista2)
        else:
            print('ERROR')
            
    def mostrarApp(self,generos):
        self.subventana = MainApp(generos,self.idUsuApp)
        self.subventana.show()  

       
#Clase dialogo Eleccion
class Dialogo(QDialog):
    def __init__(self,listaGeneros,noyentes):
        super().__init__(None)
        self.setWindowTitle("Elige Genero Musical")
        self.lista=[]
        self.oyentes=noyentes
        self.listaGeneros=listaGeneros
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.EleccionGeneros()
        
    def EleccionGeneros(self):
        count = 0
        while count < self.oyentes:
            despleglabe=QComboBox()
            despleglabe.addItems(self.listaGeneros)
            self.layout.addWidget(despleglabe)
            despleglabe.setCurrentIndex(-1)
            despleglabe.currentTextChanged.connect(self.texto_cambiado)
            count+=1
            
        botones = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        botones.button(QDialogButtonBox.Cancel).setText("Cancelar")

        self.layout.addWidget(botones)      
            
    def texto_cambiado(self, texto):
        self.lista.append(texto)
        
    def enviarParam(self):
        return self.lista

 


        
            
