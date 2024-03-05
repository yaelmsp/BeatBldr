# from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QApplication, QDialog, QLabel, QFormLayout, QWidget,QLineEdit,QPushButton,QVBoxLayout,QMessageBox)
from PySide6.QtCore import Qt,Signal,Slot
from controlador.controladorUsers import controladorUsers


class CambioPss(QWidget):
    closed=Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recuperar contraseña")
        self.mensage()
        self.controlador_usuario=controladorUsers()

        self.formulario()
        
       
    def formulario(self):
            formulario = QFormLayout()
            formulario.setLabelAlignment(Qt.AlignRight)
            formulario.setFormAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
            #Construccion Formulario  
            Usuario=QLabel('Nombre Usuario: ')
            self.huecoUsu = QLineEdit()
            self.huecoUsu.setPlaceholderText("Escribe el nombre")
            pss=QLabel('Contraseña nueva: ')
            self.huecoPss = QLineEdit()
            self.huecoPss.setEchoMode(QLineEdit.Password) 
            self.huecoPss.setPlaceholderText("Escribe nueva contraseña")
            pss2=QLabel('Contraseña otra vez: ')
            self.huecoPss2 = QLineEdit()
            self.huecoPss2.setEchoMode(QLineEdit.Password)
            self.huecoPss2.setPlaceholderText("Escribe nueva contraseña otra vez")
            self.botonEnviar=QPushButton('Enviar')

            # añadimos los elemntos a las columnas
            formulario.addRow(Usuario, self.huecoUsu)
            formulario.addRow(pss,self.huecoPss)
            formulario.addRow(pss2,self.huecoPss2)
            formulario.addRow(self.botonEnviar)
            self.botonEnviar.clicked.connect(self.confirmacionContra)
            
            self.setLayout(formulario)

    def mensage(self):
         dialogo = QMessageBox.about(
         self, "Acerca de", "<p>Error de Contraseña</p><p>Tienes que resetearla</p>")
         print(dialogo)
         
    def confirmacionContra(self):
        usuario=self.huecoUsu.text()
        contra1=self.huecoPss.text()
        contra2=self.huecoPss2.text()
        
        if contra1 != contra2:
            self.mensageErrorContra()
        else:
            self.controlador_usuario.modificarContrasenia(usuario,contra2)
            self.close()
        
            
    def mensageErrorContra(self):
         dialogo = QMessageBox.about(
         self, "Acerca de", "<p>Error de Contraseña</p><p>Las contraseñas no son iguales</p>")
         print(dialogo)
         
    @Slot()
    def closeEvent(self,event):
       self.closed.emit()
       super().closeEvent(event)

        
    

