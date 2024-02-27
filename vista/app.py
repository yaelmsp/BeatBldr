
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from controlador.controladorSongs import controladorSongs
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
                                QStyle, QToolBar)
from PySide6.QtMultimedia import (QAudioOutput,
                                  QMediaPlayer)


class MainApp(QWidget):
    def __init__(self,generos):
        super().__init__()
        self.setWindowTitle("App")
        self.mainWidget=QHBoxLayout()
        self.controlador_canciones=controladorSongs()
        self.generos=generos
        # self.devolverGeneros()
        self.CancionesSelect=self.devolverGeneros()
        self.Pantalla()
        
    def Pantalla(self):
       count=0
       BoxLayout=QVBoxLayout()
       BoxHLayout=QHBoxLayout()
       while count < len(self.CancionesSelect):
           boton=QPushButton(self.CancionesSelect[count], self)
           boton.setStyleSheet("QPushButton{background:transparent;}");
           BoxLayout.addWidget(boton)
           count+=1
           
       playIcon=QtGui.QPixmap("./assets/start.png")
       self.playbutton = QPushButton()
       self.playbutton.setIcon(QtGui.QIcon(playIcon))
       BoxHLayout.addWidget(self.playbutton)
       # self.playbutton.clicked.connect(self.play_pause)
       
       SkipIcon=QtGui.QPixmap("./assets/skip.png")
       self.Skipbutton = QPushButton()
       self.Skipbutton.setIcon(QtGui.QIcon(SkipIcon))
       BoxHLayout.addWidget(self.Skipbutton)
       
       PauseIcon=QtGui.QPixmap("./assets/pause.png")
       self.pausebutton = QPushButton()
       self.pausebutton.setIcon(QtGui.QIcon(PauseIcon))
       BoxHLayout.addWidget(self.pausebutton)
       
       Skip_derIcon=QtGui.QPixmap("./assets/skip_der.png")
       self.skip_derbutton = QPushButton()
       self.skip_derbutton.setIcon(QtGui.QIcon(Skip_derIcon))
       BoxHLayout.addWidget(self.skip_derbutton)
       
       StopIcon=QtGui.QPixmap("./assets/stop.png")
       self.stopbutton = QPushButton()
       self.stopbutton.setIcon(QtGui.QIcon(StopIcon))
       BoxHLayout.addWidget(self.stopbutton)
       
       scrollArea = QScrollArea()
       scrollArea.setBackgroundRole(QPalette.Dark)
       scrollArea.setLayout(BoxLayout)
       widget = QWidget()
       widget.setLayout(BoxHLayout)
       self.mainWidget.addWidget(scrollArea)
       self.mainWidget.addWidget(widget)
       
       self.setLayout(self.mainWidget)
    
       


    def devolverGeneros(self):
      canciones = self.controlador_canciones.mostrarGenerosElegidos(self.generos)
      # print(canciones)
      return canciones
           

       