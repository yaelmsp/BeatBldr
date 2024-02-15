
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFormLayout, QWidget,QLineEdit,QPushButton,QVBoxLayout,QMessageBox)
from PySide6.QtCore import Qt
from controlador.controladorUsers import controladorUsers


class NuevoUsu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo Usuario")
        self.controlador_usuario=controladorUsers()
        
        self.mensages()
        
    def formulario(self):
        formulario = QFormLayout()

        # configuraciones extra
        formulario.setLabelAlignment(Qt.AlignRight)
        formulario.setFormAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        #Construccion Formulario  
        Usuario=QLabel('Nombre: ')
        self.huecoUsua = QLineEdit()
        self.huecoUsua.setPlaceholderText("Escribe el nombre")
        Ape=QLabel('Apellido: ')
        self.huecoApe = QLineEdit()
        self.huecoApe.setPlaceholderText("Escribe Apellido")
        Usu=QLabel('Nombre Usuario: ')
        self.huecoUsu = QLineEdit()
        self.huecoUsu.setPlaceholderText("Escribe Nombre de Usuario")
        pss2=QLabel('Contrasenia: ')
        self.huecoPss2 = QLineEdit()
        self.huecoPss2.setPlaceholderText("Escribe nueva contrasenia")
        self.botonCrear=QPushButton('Crear Usuario')

        # añadimos los elemntos a las columnas
        formulario.addRow(Usuario, self.huecoUsua)
        formulario.addRow(Ape,self.huecoApe)
        formulario.addRow(Usu,self.huecoUsu)
        formulario.addRow(pss2,self.huecoPss2)
        formulario.addRow(self.botonCrear)
        self.botonCrear.clicked.connect(self.agregarUsuario)
    
        # cremos el widget dummy y le asignamos el layout
        self.setLayout(formulario)
        
    def mensages(self):
        # creamos un diálogo de tipo cuestión
        dialogo = QMessageBox.question(
            self, "Cuenta nueva", "Te gustaria hacerte una cuenta")

        # ahora debemos comprobar qué tipo de botón se devuelve
        if dialogo == QMessageBox.Yes:
            print("Si")
            self.formulario()
        else:
            print("No")
            dialogo = QMessageBox.about(
            self, "En ese caso", "<p>No puedes acceder</p><p>a la applicacion</p>")
        # podemos analizar el tipo de botón clicado para actuar en consecuencia
            print(dialogo)

    def agregarUsuario(self):
        nombre=str(self.huecoUsua.text())
        ape=str(self.huecoApe.text())
        usu= str(self.huecoUsu.text())
        pss=str(self.huecoPss2.text())
        self.controlador_usuario.agregarUsu(nombre,ape,usu,pss)



