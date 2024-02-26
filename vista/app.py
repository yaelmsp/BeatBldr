
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

    def devolverGeneros(self):
      self.controlador_canciones.mostrarGenerosElegidos(self.generos)
       