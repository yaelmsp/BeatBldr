
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from controlador.controladorSongs import controladorSongs
from controlador.controladorPlaylist import ControladorPlaylist

from modelo.mock import CAMBIO_CONTRASENIA_MOCK,ADD_PLAYLIST,ADD_USUARIO


class MainApp(QWidget):
    def __init__(self,generos,idUsuApp):
        super().__init__()
        self.idUsuApp=idUsuApp
        self.setWindowTitle("App")
        self.resize(500,500)
        self.mainWidget=QVBoxLayout()
        self.controlador_canciones=controladorSongs()
        self.controlador_playlist=ControladorPlaylist()
        self.generos=generos
        self.CancionesSelect=self.devolverGeneros()
        self.ListaCancionesLimpia=list(set(self.CancionesSelect))
        self.functionMenu()
        self.Pantalla()
        self.playerMenu()

        
    def functionMenu(self): 
        BoxHLayout=QHBoxLayout()
        
        logout=QtGui.QPixmap("./assets/log_out.png")
        self.logoutbutton = QPushButton()
        self.logoutbutton.setToolTip('salir')
        self.logoutbutton.setIcon(QtGui.QIcon(logout))
       
        BoxHLayout.addWidget(self.logoutbutton)
       
        self.logoutbutton.setStyleSheet("""                                        
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple;
                                       
                                }""");
       
        self.logoutbutton.clicked.connect(self.Log_Out)
            
        guardar=QtGui.QPixmap("./assets/guardar.png")
        self.guardarbutton = QPushButton()
        self.guardarbutton.setToolTip('guardar')
        self.guardarbutton.setIcon(QtGui.QIcon(guardar))
        BoxHLayout.addWidget(self.guardarbutton) 
        self.guardarbutton.setStyleSheet("""                                        
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple;
                                       
                                }""");
       
        self.guardarbutton.clicked.connect(self.crearPlaylist)
        
        widget = QWidget()
        widget.setLayout(BoxHLayout)
        self.mainWidget.addWidget(widget,alignment=Qt.AlignBottom)
       
        self.setLayout(self.mainWidget)
        
        
    def Pantalla(self):
       BoxLayout=QVBoxLayout()
       widget = QWidget()
       widget.setLayout(BoxLayout)
       if len(self.ListaCancionesLimpia) != 0:
           count=0
           while count < len(self.ListaCancionesLimpia):
               boton=QPushButton(self.ListaCancionesLimpia[count], self)
               boton.setStyleSheet("""
                                    QPushButton {
                                        background-color: transparent; 
                                        font-size:20px
                                    
                                    }
                                    QPushButton:hover {
                                        color: purple;
                                    }""");
               BoxLayout.addWidget(boton)
               count+=1
           scrollArea = QScrollArea()
           scrollArea.setBackgroundRole(QPalette.Dark)
           scrollArea.setWidget(widget)
           scrollArea.setAlignment(Qt.AlignCenter)  
    
           self.mainWidget.addWidget(scrollArea)
           self.setLayout(self.mainWidget)
           
       else:
            label = QLabel()
            label.setText("No hay ninguna cancion de ese genero")
            label.setStyleSheet("QLabel { color : purple; font-size:20px }");
            BoxLayout.addWidget(label)
        
            scrollArea = QScrollArea()
            scrollArea.setBackgroundRole(QPalette.Dark)
            scrollArea.setWidget(widget)
            scrollArea.setAlignment(Qt.AlignCenter)  
    
            self.mainWidget.addWidget(scrollArea)
            self.setLayout(self.mainWidget)

          
    def playerMenu(self):
       
       BoxHLayout=QHBoxLayout()
       
       playIcon=QtGui.QPixmap("./assets/play.png")
       self.playbutton = QPushButton()
       self.playbutton.setIcon(QtGui.QIcon(playIcon))
       BoxHLayout.addWidget(self.playbutton)
       self.playbutton.setStyleSheet("""
                                QPushButton:hover {
                                    background-color: #DEC9E9;
                                    border:1px solid purple;
                                }""");
       
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
       

    def devolverGeneros(self):
      canciones = self.controlador_canciones.mostrarGenerosElegidos(self.generos)
      return canciones
  
    def crearPlaylist(self):
        id_propietario=self.idUsuApp
        self.controlador_playlist.crear_playlist(id_propietario)
        dialogo = QMessageBox.about(
        self, "Acerca de", "<p>La Playlist ha sido guardada</p>")
        print(dialogo)
  
    def Log_Out(self):
        dialogo = QMessageBox.question(
            self, "Log out", "Te gustaría salir de la aplicación")

        if dialogo == QMessageBox.Yes:
            CAMBIO_CONTRASENIA_MOCK()
            ADD_PLAYLIST()
            # ADD_USUARIO()
            self.close()

           
