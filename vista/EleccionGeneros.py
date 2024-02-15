from PySide6.QtWidgets import (
    QApplication, QComboBox,QInputDialog,QWidget,QFormLayout,QDialog,QVBoxLayout,QDialogButtonBox)
import sys
from controlador.controladorGenres import controladorGenres


class Generos(QWidget):
    def __init__(self,oyentesElec):
        super().__init__()
        self.setWindowTitle("Elegir generos")
        self.oyentes = int(oyentesElec)
        self.controlador_generos=controladorGenres()
        self.ListaGeneros=[]
        self.ConversionArray()
        self.formulario()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
    def ConversionArray(self):
         gen=self.controlador_generos.mostrar_generos()
         for genero in gen:
             self.ListaGeneros.append(genero)
         
        
    def formulario(self):
        dialogo = Dialogo(self.ListaGeneros,self.oyentes)
        rest=dialogo.exec()
        if rest:
            lista = dialogo.enviarParam()
            self.ListaGeneros=set(lista[-self.oyentes:])
        else:
            print('ERROR')
       
#Clase dialogo Eleccion
class Dialogo(QDialog):
    def __init__(self,listaGeneros,noyentes):
        super().__init__(None)
        self.setWindowTitle("Elige Genero Musical")
        self.lista=[]
        layout = QVBoxLayout()
        self.setLayout(layout)
        terminar = 0
        while terminar < noyentes:
            despleglabe=QComboBox()
            despleglabe.addItems(listaGeneros)
            layout.addWidget(despleglabe)
            despleglabe.setCurrentIndex(-1)
            despleglabe.currentTextChanged.connect(self.texto_cambiado)
            terminar=terminar+1
            
        botones = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        botones.button(QDialogButtonBox.Cancel).setText("Cancelar")

        layout.addWidget(botones)      
            
    def texto_cambiado(self, texto):
        self.lista.append(texto)
        
    def enviarParam(self):
        return self.lista

 


        
            
