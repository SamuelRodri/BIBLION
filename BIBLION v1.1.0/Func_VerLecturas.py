#Módulo que controla la subventana "Ver Lecturas" 
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout,QTableWidgetItem
from ventana_principal import Ui_BIBLION
from borrar_todo import Ui_Borrar_Base
from eliminar_libro import Ui_Eliminar_Libro
from ver_libros import Ui_ver_libros
from lecturas import Ui_Proximas_Lecturas
from estadisticas import Ui_Estadisticas
from ver_lecturas import Ui_VerLecturas

miconexion = sqlite3.connect("BASE DE DATOS.DB")
micursor = miconexion.cursor()
try:
    micursor.execute("CREATE TABLE LECTURAS(TITULO VARCHAR(20), AUTOR VARCHAR(20))")
    micursor.execute("CREATE TABLE LIBROS(TITULO VARCHAR(20), AUTOR VARCHAR(20), GENERO VARCHAR(20), PUNTUACION INTEGER)")
    
except:
    sqlite3.OperationalError

class VerLecturas(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_VerLecturas()
        self.ui_d.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icono.png'))
        QtWidgets.QDialog.setFixedSize(self,400,298)
        self.initUI()
    def initUI(self):

        micursor.execute("SELECT TITULO FROM LECTURAS")
        libros = micursor.fetchall()
        contador = 0

        for libro in libros:
            contador += 1

        grid = QGridLayout()
        self.setLayout(grid)
        self.ui_d.tableWidget.setRowCount(contador)
        self.ui_d.tableWidget.setColumnCount(2)
        header = ['TITULO','AUTOR']
        self.ui_d.tableWidget.setHorizontalHeaderLabels(header)
        micursor.execute("SELECT * FROM LECTURAS")
        todos = micursor.fetchall()
        y = 0
        x = 0
        for titulo, autor in todos:
            new_titulo = QTableWidgetItem(titulo)
            self.ui_d.tableWidget.setItem(x,y, new_titulo)
            y += 1
            new_autor = QTableWidgetItem(autor)
            self.ui_d.tableWidget.setItem(x,y, new_autor)
            y +=1
            x += 1
        
            
        
        #Add Table to Grid
        grid.addWidget(self.ui_d.tableWidget, 0,0)     

        self.show()
        