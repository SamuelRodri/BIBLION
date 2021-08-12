import sys
import sqlite3
from PyQt5 import QtGui, QtCore, QtWidgets
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

class EliminarLibro(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_Eliminar_Libro()
        self.ui_d.setupUi(self)
        self.ui_d.pushButton.clicked.connect(self.EliminarLibro)

    def EliminarLibro(self):

    	if self.ui_d.lineEdit.text() == "":
    		self.ui_d.label_2.setText("Debe introducir un titulo a eliminar")

    	else:
    		micursor.execute("SELECT TITULO FROM LIBROS")
    		titulos = micursor.fetchall()
    		if len(titulos) == 0:
    			self.ui_d.label_2.setText("No hay libros en la base de datos")
    		else:
    			for titulo in titulos:
    				if titulo[0] == self.ui_d.lineEdit.text():
    					micursor.execute("DELETE TITULO FROM LIBROS WHERE TITULO = {}".format(titulo[0]))

    				else:
    					self.ui_d.label_2.setText("No existe libro con ese título")

     