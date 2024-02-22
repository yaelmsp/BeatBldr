from PySide6.QtWidgets import (QWidget,QHBoxLayout,QPushButton)
from PySide6.QtCore import Qt,Signal,Slot

class MainApp(QWidget):
    def __init__(self,generos):
        super().__init__()
        self.ListaGenerosElegidos=generos
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2) 
       
        button1 = QPushButton("One")
        button2 = QPushButton("Two")  
        
            
