
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFormLayout, QWidget,QLineEdit,QPushButton,QVBoxLayout,QApplication,QWidget,QFormLayout,QVBoxLayout)
from PySide6.QtCore import Qt
import sys
from controlador.controladorUsers import controladorUsers
from vista.CanbioPss import CambioPss
from vista.NuevoUsu import NuevoUsu
from vista.PantallaEleccion import Eleccion


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.titulo=QLabel("LOG IN")
        self.titulo.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.controlador_usuario=controladorUsers()
       
        
        self.formulario()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.titulo)
             
    def formulario(self):
        formulario = QFormLayout()

        # configuraciones extra
        formulario.setLabelAlignment(Qt.AlignRight)
        formulario.setFormAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        #Construccion Formulario  
        Usuario=QLabel('Nombre Usuario: ')
        self.huecoUsu = QLineEdit()
        self.huecoUsu.setPlaceholderText("Escribe el nombre")
        pss=QLabel('Contrasenia: ')
        self.huecoPss = QLineEdit()
        self.huecoPss.setEchoMode(QLineEdit.Password)
        self.huecoPss.setPlaceholderText("Escribe la contrasenia")
        self.botonEnviar=QPushButton('Enviar')

        # añadimos los elemntos a las columnas
        formulario.addRow(Usuario, self.huecoUsu)
        formulario.addRow(pss,self.huecoPss)
        formulario.addRow(self.botonEnviar)
        
        self.botonEnviar.clicked.connect(self.devolverNyC)

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)
        
    def devolverNyC(self):
        nombre=str(self.huecoUsu.text())
        contra=str(self.huecoPss.text())
        rest=self.controlador_usuario.login(nombre,contra)
        
        if rest==1:
            self.mostrarApplicacion()
        elif rest == 2:
            self.mostrarSubVentana()
        elif rest==3:
            self.mostrarRegistro()
            
    def mostrarApplicacion(self):
        self.aplicacion = Eleccion()
        self.aplicacion.show()     
        
    def mostrarSubVentana(self):
        self.subventana = CambioPss()
        self.subventana.show()  
        self.subventana.closed.connect(self.show)
        
    def mostrarRegistro(self):
        self.registro = NuevoUsu()
        self.registro.show()
        self.registro.closed.connect(self.mostrarLogin)
        
        
    def mostrarLogin(self):
        self.show()
       
 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
