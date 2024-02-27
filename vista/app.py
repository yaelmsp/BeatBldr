
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from controlador.controladorSongs import controladorSongs

class MainApp(QWidget):
    def __init__(self,generos):
        super().__init__()
        self.setWindowTitle("App")
        self.controlador_canciones=controladorSongs()
        self.generos=generos
        self.devolverGeneros()
        self.mainWidget=QHBoxLayout()
        self.CancionesSelect=self.devolverGeneros()
        self.Pantalla()
        
        
    def Pantalla(self):
       count=0
       BoxLayout=QVBoxLayout()
       
       while count >= len(self.CancionesSelect):
           boton=QPushButton("boton", self)
           BoxLayout.addWidget(boton)
           count+=1
       
       scrollArea = QScrollArea()
       scrollArea.setBackgroundRole(QPalette.Dark)
       scrollArea.setLayout(BoxLayout)
       self.mainWidget.addWidget(scrollArea)
       self.setLayout(self.mainWidget)

    def devolverGeneros(self):
      canciones = self.controlador_canciones.mostrarGenerosElegidos(self.generos)
      return canciones
           

       