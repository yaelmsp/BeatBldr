
from ctypes import alignment
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
        self.resize(500,500)
        self.mainWidget=QVBoxLayout()
        self.controlador_canciones=controladorSongs()
        self.generos=generos
        # self.devolverGeneros()
        self.CancionesSelect=self.devolverGeneros()
        self.Pantalla()
        self.playerMenu()
        
    def Pantalla(self):
       count=0
       BoxLayout=QVBoxLayout()
       widget = QWidget()
       widget.setLayout(BoxLayout)

       while count < len(self.CancionesSelect):
           boton=QPushButton(self.CancionesSelect[count], self)
           boton.setStyleSheet("""
                                QPushButton {
                                    background-color: transparent; 
                                    font-size:35px
                                }
                                QPushButton:hover {
                                    color: purple;
                                }""");
           BoxLayout.addWidget(boton)
           boton.clicked.connect(self.comprobar)
           count+=1
        
       scrollArea = QScrollArea()
       scrollArea.setBackgroundRole(QPalette.Dark)
       scrollArea.setWidget(widget)
    
       self.mainWidget.addWidget(scrollArea)

       
       self.setLayout(self.mainWidget)
          
    def playerMenu(self):
       
       BoxHLayout=QHBoxLayout()
       playIcon=QtGui.QPixmap("./assets/start.png")
       self.playbutton = QPushButton()
       self.playbutton.setIcon(QtGui.QIcon(playIcon))
       BoxHLayout.addWidget(self.playbutton)
       self.playbutton.setStyleSheet("""
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple; 
                                }""");
       # self.playbutton.clicked.connect(self.play_pause)
       
       SkipIcon=QtGui.QPixmap("./assets/skip.png")
       self.Skipbutton = QPushButton()
       self.Skipbutton.setIcon(QtGui.QIcon(SkipIcon))
       BoxHLayout.addWidget(self.Skipbutton)
       self.Skipbutton.setStyleSheet("""
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple; 
                                }""");
       
       PauseIcon=QtGui.QPixmap("./assets/pause.png")
       self.pausebutton = QPushButton()
       self.pausebutton.setIcon(QtGui.QIcon(PauseIcon))
       BoxHLayout.addWidget(self.pausebutton)
       self.pausebutton.setStyleSheet("""
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple; 
                                }""");
       
       Skip_derIcon=QtGui.QPixmap("./assets/skip_der.png")
       self.skip_derbutton = QPushButton()
       self.skip_derbutton.setIcon(QtGui.QIcon(Skip_derIcon))
       BoxHLayout.addWidget(self.skip_derbutton)
       self.skip_derbutton.setStyleSheet("""
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple; 
                                }""");
       
       StopIcon=QtGui.QPixmap("./assets/stop.png")
       self.stopbutton = QPushButton()
       self.stopbutton.setIcon(QtGui.QIcon(StopIcon))
       BoxHLayout.addWidget(self.stopbutton)
       self.stopbutton.setStyleSheet("""
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple; 
                                }""");
       
       widget = QWidget()
       widget.setLayout(BoxHLayout)
       self.mainWidget.addWidget(widget,alignment=Qt.AlignBottom)
       
       self.setLayout(self.mainWidget)
       
    def comprobar(self):
       print('boton clicado')

    def devolverGeneros(self):
      canciones = self.controlador_canciones.mostrarGenerosElegidos(self.generos)
      # print(canciones)
      return canciones
           

       