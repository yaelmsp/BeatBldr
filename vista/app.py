# from PySide6.QtWidgets import (QWidget,QHBoxLayout,QPushButton,QDockWidget,QLabel,QVBoxLayout,QApplication,QCoreApplication)
# from PySide6.QtCore import Qt,Signal,Slot
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainApp(QWidget):
    def __init__(self,generos):
        super().__init__()
        self.setWindowTitle("App")
        self.elegirOyentes()
        # Le damos un tamaño y un título
    def elegirOyentes(self):
        print('Hola')
        
  
            
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)