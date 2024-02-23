# from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QInputDialog,QWidget)
from vista.EleccionGeneros import Generos

class Eleccion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elegir Oyentes")
        self.elegirOyentes()
        # Le damos un tamaño y un título
    def elegirOyentes(self):
        oyente, confirmado = QInputDialog.getInt(
        self, "Oyente", "Elige los generos que deseas mezclar", minValue=1, maxValue=4)
        if confirmado:
            self.mostrarSubVentana(oyente)
                        
    def mostrarSubVentana(self,oyente):
        self.subventana = Generos(oyente)
        self.subventana.show()  
        
            
