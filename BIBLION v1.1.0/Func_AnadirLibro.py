#Módulo que controla la subventana "Añadir Libro" 

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from anadir_libro import Ui_Aniadir_Libro
from ventana_principal import Ui_BIBLION
from borrar_todo import Ui_Borrar_Base
from eliminar_libro import Ui_Eliminar_Libro
from ver_libros import Ui_ver_libros
from lecturas import Ui_Proximas_Lecturas
from estadisticas import Ui_Estadisticas

miconexion = sqlite3.connect("BASE DE DATOS.DB")
micursor = miconexion.cursor()
try:
    micursor.execute("CREATE TABLE LECTURAS(TITULO VARCHAR(20), AUTOR VARCHAR(20))")
    micursor.execute("CREATE TABLE LIBROS(TITULO VARCHAR(20), AUTOR VARCHAR(20), GENERO VARCHAR(20), PUNTUACION INTEGER)")
    
except:
    sqlite3.OperationalError
    
class AnadirLibro(QtWidgets.QDialog):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_Aniadir_Libro()
        self.ui_d.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icono.png'))
        QtWidgets.QDialog.setFixedSize(self,400,300)
        self.ui_d.aniadir_aceptar.clicked.connect(self.anadirlibro)

        """Añadimos los géneros al comboBox"""

        self.ui_d.comboBox.addItem("BIOGRAFÍA")
        self.ui_d.comboBox.addItem("CIENCIA FICCIÓN")
        self.ui_d.comboBox.addItem("CÓMIC")
        self.ui_d.comboBox.addItem("FANTASÍA")
        self.ui_d.comboBox.addItem("FILOSOFÍA")
        self.ui_d.comboBox.addItem("HISTORICO")
        self.ui_d.comboBox.addItem("HUMOR")
        self.ui_d.comboBox.addItem("INFANTIL")
        self.ui_d.comboBox.addItem("NARRATIVO")
        self.ui_d.comboBox.addItem("POESÍA")
        self.ui_d.comboBox.addItem("POLICIACO")
        self.ui_d.comboBox.addItem("ROMANCE")
        self.ui_d.comboBox.addItem("TERROR")


    def anadirlibro(self):

        item = self.ui_d.comboBox.currentText()
        lista = []
        sql1 = "INSERT INTO LIBROS VALUES (?,?,?,?)"

        """Comprobamos los campos Título y Autor"""

        if self.ui_d.line_titulo.text() == "":
            self.ui_d.label_mensaje.setText("Debe rellenar al menos el título")
        else:
            if self.ui_d.line_autor.text() =="":
                autor = "Desconocido" 
            else:
                autor = self.ui_d.line_autor.text()
            
                
            """Introducimos todos los títulos en una lista"""

            micursor.execute("SELECT TITULO FROM LIBROS")
            libros = micursor.fetchall()
            for libro in libros:
                lista +=[libro[0]]

            """Comprobamos que el título no esté en la lista"""

            if self.ui_d.line_titulo.text() in lista:
                    self.ui_d.label_mensaje.setText("Este libro ya estaba registrado")
            else:
                    """Introducimos el libro en la base de datos"""
                    
                    t = (self.ui_d.line_titulo.text(), autor, item,self.ui_d.spinBox.value(),)
                    micursor.execute(sql1,t,)
                    miconexion.commit()
                    self.ui_d.label_mensaje.setText("{} añadido a la base de datos".format(self.ui_d.line_titulo.text()))
