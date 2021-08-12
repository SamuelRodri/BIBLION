#Módulo que controla la subventana "Estadísticas"
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
        self.setWindowIcon(QtGui.QIcon('icono.png'))
        QtWidgets.QDialog.setFixedSize(self,256,201)
        

        """Todas las instrucciones sql necesarias"""

        sql1 = "SELECT TITULO FROM LIBROS"
        sql2 = "SELECT AUTOR FROM LIBROS"
        sql3 = "SELECT GENERO FROM LIBROS"
        sql4 = "SELECT PUNTUACION FROM LIBROS"
        sql5 = "SELECT TITULO FROM LIBROS WHERE PUNTUACION == (?)"


        """Almacenamos todos los libros en "libros" """

        micursor.execute(sql1)
        libros = micursor.fetchall()


        """Rellenamos el campo "Libros Leidos" """

        if len(libros) != 0:

            for libro in libros:
                contador += 1
            self.ui_d.label_libros.setText(str(contador))


            """Rellenamos el campo "Autor Favorito" """

            micursor.execute("SELECT AUTOR FROM LIBROS")
            autores = micursor.fetchall()
            repe = 0
            for autor in autores:
                if autor != None:
                    variable = autores.count(autor)
                    if variable > repe:
                        repe == variable
            self.ui_d.label_autor_fav.setText(autor[0])


            """Rellenamos el campo "Género Favorito" """

            micursor.execute(sql3)
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


            """Rellenamos el campo "Libro Favorito" """

            lista_autores = []
            micursor.execute(sql2)
            autores = micursor.fetchall()
            for autor in autores:
                lista_autores += [autor[0]]
            lista_puntos = []
            
            micursor.execute(sql4)
            puntos = micursor.fetchall()
            for punto in puntos:
                lista_puntos += (punto)

            maximo = max(lista_puntos)
            t = (int(maximo),)
            micursor.execute(sql5,t)
            favorito = micursor.fetchall()
            self.ui_d.label_libro_fav.setText(str(favorito[0][0]))
            
            """Rellenamos el campo "Último Libro" """
            micursor.execute(sql2)     
            autores = micursor.fetchall()
            repe = 0
            micursor.execute(sql1)
            titulos = micursor.fetchall()
            ultimo = len(titulos)
            posicion = ultimo - 1
            self.ui_d.label_ultimo_libro.setText(titulos[posicion][0])
       	else:
            self.ui_d.label_autor_fav.setText("Ninguno")
            self.ui_d.label_genero_fav.setText("Ninguno")
            self.ui_d.label_libro_fav.setText("Ninguno")
            self.ui_d.label_ultimo_libro.setText("Ninguno")