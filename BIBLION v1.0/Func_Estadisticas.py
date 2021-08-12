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
class Estadisticas(QtWidgets.QDialog):
    def __init__(self):
        contador = 0
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_Estadisticas()
        self.ui_d.setupUi(self)
        sql3 = "SELECT TITULO FROM LIBROS"
        micursor.execute(sql3)
        libros = micursor.fetchall()
        for libro in libros:
            contador += 1
        self.ui_d.label_libros.setText(str(contador))
        lista_autores = []
        sql4 = "SELECT AUTOR FROM LIBROS"
        micursor.execute(sql4)
        autores = micursor.fetchall()
        for autor in autores:
            lista_autores += [autor[0]]

        lista_puntos = []
        sql5 = "SELECT PUNTUACION FROM LIBROS"
        micursor.execute(sql5)
        puntos = micursor.fetchall()
        for punto in puntos:
            lista_puntos += str(punto[0])
        try:
            maximo = max(lista_puntos)
            sql6 = "SELECT TITULO FROM LIBROS WHERE PUNTUACION == ({})".format(int(maximo))
            micursor.execute(sql6)
            favorito = micursor.fetchall()
            self.ui_d.label_libro_fav.setText(str(favorito[0][0])) 
            micursor.execute("SELECT AUTOR FROM LIBROS")
            autores = micursor.fetchall()
            repe = 0
            for autor in autores:
            	if autor == None:
            		pass
            	else:
            		variable = autores.count(autor)
            		if variable > repe:
            			repe == variable
            self.ui_d.label_autor_fav.setText(autor[0])
            micursor.execute("SELECT GENERO FROM LIBROS")
            generos = micursor.fetchall()
            repe = 0

            for genero in generos:
            	if genero == None:
            		pass
            	else:
            		variable = generos.count(genero)
            		if variable > repe:
            			repe == variable
            self.ui_d.label_genero_fav.setText(genero[0])  
            micursor.execute("SELECT AUTOR FROM LIBROS")     
            autores = micursor.fetchall()
            repe = 0
            micursor.execute("SELECT TITULO FROM LIBROS")
            titulos = micursor.fetchall()
            ultimo = len(titulos)
            posicion = ultimo - 1
            self.ui_d.label_ultimo_libro.setText(titulos[posicion][0])
       	except:
            self.ui_d.label_autor_fav.setText("Ninguno")
            self.ui_d.label_genero_fav.setText("Ninguno")
            self.ui_d.label_libro_fav.setText("Ninguno")
            self.ui_d.label_ultimo_libro.setText("Ninguno")