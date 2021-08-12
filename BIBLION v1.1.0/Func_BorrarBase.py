#Módulo que controla la subventana "Borrar Base"
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
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

class BorrarBase(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_Borrar_Base()
        self.ui_d.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icono.png'))
        QtWidgets.QDialog.setFixedSize(self,273,116)
        self.ui_d.borrar_borrar.clicked.connect(self.borrartodo)

    def borrartodo(self):
        micursor.execute("DELETE FROM LIBROS")
        micursor.execute("DELETE FROM LECTURAS")
        miconexion.commit()