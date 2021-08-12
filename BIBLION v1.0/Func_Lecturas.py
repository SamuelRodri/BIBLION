import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from ventana_principal import Ui_BIBLION
from borrar_todo import Ui_Borrar_Base
from eliminar_libro import Ui_Eliminar_Libro
from ver_libros import Ui_ver_libros
from lecturas import Ui_Proximas_Lecturas
from estadisticas import Ui_Estadisticas
from Func_VerLecturas import VerLecturas

miconexion = sqlite3.connect("BASE DE DATOS.DB")
micursor = miconexion.cursor()
try:
    micursor.execute("CREATE TABLE LECTURAS(TITULO VARCHAR(20), AUTOR VARCHAR(20))")
    micursor.execute("CREATE TABLE LIBROS(TITULO VARCHAR(20), AUTOR VARCHAR(20), GENERO VARCHAR(20), PUNTUACION INTEGER)")
    
except:
    sqlite3.OperationalError

class Lecturas(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_Proximas_Lecturas()
        self.ui_d.setupUi(self)
    
        self.ui_d.lecturas_aniadir.clicked.connect(self.anadirlectura)
        self.ui_d.lectura_ver.clicked.connect(self.verlecturas)
    
    
    def verlecturas(self):
    	self.w = VerLecturas()
    	self.w.show()
    
    
    def anadirlectura(self):
        if self.ui_d.linel_titulo.text() == "":
            self.ui_d.label_lecturas_mensaje.setText("Debe rellenar al menos el título")
        else:
        	if self.ui_d.linel_autor.text() == "":
        		autor = "Desconocido"
        	else:
        		autor = self.ui_d.linel_autor.text()
        	lista = []
        	micursor.execute("SELECT TITULO FROM LECTURAS")
        	lecturas = micursor.fetchall()
        	for lectura in lecturas:
        		lista += [lectura[0]]
        	if self.ui_d.linel_titulo.text() in lista:
        		self.ui_d.label_lecturas_mensaje.setText("Este libro ya estaba registrado")

        	else:
        		sql = ("INSERT INTO LECTURAS VALUES (?,?)")
        		t = (self.ui_d.linel_titulo.text(), autor,)
        		micursor.execute(sql, t)
        		miconexion.commit()
        		self.ui_d.label_lecturas_mensaje.setText("{} añadido a la base de datos".format(self.ui_d.linel_titulo.text()))
    