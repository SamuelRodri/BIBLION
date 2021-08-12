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

miconexion = sqlite3.connect("BASE DE DATOS.DB")
micursor = miconexion.cursor()
try:
    micursor.execute("CREATE TABLE LECTURAS(TITULO VARCHAR(20), AUTOR VARCHAR(20))")
    micursor.execute("CREATE TABLE LIBROS(TITULO VARCHAR(20), AUTOR VARCHAR(20), GENERO VARCHAR(20), PUNTUACION INTEGER)")
    
except:
    sqlite3.OperationalError

def repetidas (cont, l1,l2,l3, l4):
    definitiva = l1 + l2 + l3 + l4
    sinrepes = []
    for i in definitiva:
        contador = definitiva.count(i)
        if cont == 1:
            return definitiva
        else:
            if contador != cont:
                definitiva.remove(i)
            else:
                if i not in sinrepes:
                    sinrepes.append(i)
    return sinrepes

class VerLibros(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_ver_libros()
        self.ui_d.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icono.png'))
        QtWidgets.QDialog.setFixedSize(self,527,459)
        self.ui_d.pushbuscar.clicked.connect(self.rellenartabla)
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
        self.ui_d.linetitulo.setEnabled(False)
        self.ui_d.lineautor.setEnabled(False)
        self.ui_d.comboBox.setEnabled(False)
        self.ui_d.spinBox.setEnabled(False)
        self.ui_d.todosBox.clicked.connect(self.inhabilitar)
        self.ui_d.titulobox.clicked.connect(self.inhabilitar2)
        self.ui_d.autorbox.clicked.connect(self.inhabilitar3)
        self.ui_d.generobox.clicked.connect(self.inhabilitar4)
        self.ui_d.puntosbox.clicked.connect(self.inhabilitar5)

    def inhabilitar(self):
        if self.ui_d.todosBox.isChecked():
            self.ui_d.titulobox.setEnabled(False), self.ui_d.autorbox.setEnabled(False), self.ui_d.generobox.setEnabled(False), self.ui_d.puntosbox.setEnabled(False), self.ui_d.linetitulo.setEnabled(False), self.ui_d.lineautor.setEnabled(False),self.ui_d.comboBox.setEnabled(False), self.ui_d.spinBox.setEnabled(False)
        else:
            self.ui_d.titulobox.setEnabled(True), self.ui_d.autorbox.setEnabled(True), self.ui_d.generobox.setEnabled(True), self.ui_d.puntosbox.setEnabled(True), self.ui_d.linetitulo.setEnabled(True), self.ui_d.lineautor.setEnabled(True),self.ui_d.comboBox.setEnabled(True), self.ui_d.spinBox.setEnabled(True)
    
    def inhabilitar2(self):

        if self.ui_d.titulobox.isChecked():
            self.ui_d.linetitulo.setEnabled(True)
        else:
            self.ui_d.linetitulo.setEnabled(False)    

    def inhabilitar3(self):
        if self.ui_d.autorbox.isChecked():
            self.ui_d.lineautor.setEnabled(True)
        else:
            self.ui_d.lineautor.setEnabled(False)

    def inhabilitar4(self):
        if self.ui_d.generobox.isChecked():
            self.ui_d.comboBox.setEnabled(True)
        else:
            self.ui_d.comboBox.setEnabled(False)
    
    def inhabilitar5(self):
        if self.ui_d.puntosbox.isChecked():
            self.ui_d.spinBox.setEnabled(True)
        else:
            self.ui_d.spinBox.setEnabled(False)
    
    


    def rellenartabla(self):
        self.ui_d.tableWidget.clear()
        if self.ui_d.todosBox.isChecked():
            micursor.execute("SELECT TITULO, AUTOR, GENERO, PUNTUACION FROM LIBROS")
            libros = micursor.fetchall()       
            contador = 0
            for libro in libros:
                contador += 1  
            grid = QGridLayout()
            self.setLayout(grid)
            self.ui_d.tableWidget.setRowCount(contador)
            self.ui_d.tableWidget.setColumnCount(4)
            header = ['TITULO','AUTOR','GENERO','PUNTOS']
            self.ui_d.tableWidget.setHorizontalHeaderLabels(header)
            
            micursor.execute("SELECT * FROM LIBROS")
            todos = micursor.fetchall()
            y = 0
            x = 0
            for titulos, autores, generos, puntos in todos:
                new_titulo = QTableWidgetItem(titulos)
                self.ui_d.tableWidget.setItem(x,y, new_titulo)
                y += 1
                new_autor = QTableWidgetItem(autores)
                self.ui_d.tableWidget.setItem(x,y, new_autor)
                y += 1
                new_genero = QTableWidgetItem(generos)
                self.ui_d.tableWidget.setItem(x,y, new_genero)
                y += 1
                new_puntos = QTableWidgetItem(str(puntos))
                self.ui_d.tableWidget.setItem(x,y, new_puntos)
                y = 0
                x += 1
                self.ui_d.tableWidget.show()
        else:
            micursor.execute("SELECT TITULO, AUTOR, GENERO, PUNTUACION FROM LIBROS")
            libros = micursor.fetchall()       
            portitulo = []
            porautor = []
            porgenero = []
            porpuntos = []

            cont =  0
            if self.ui_d.titulobox.isChecked():
                cont += 1
                if self.ui_d.linetitulo.text() == "":
                    self.ui_d.label_box.setText("Hay parámetros sin rellenar")
                else: 
                    micursor.execute("SELECT * FROM LIBROS WHERE TITULO = '{}'".format(self.ui_d.linetitulo.text()))
                    portitulo = micursor.fetchall()

            if self.ui_d.autorbox.isChecked():
                cont += 1
                if self.ui_d.lineautor.text() == "":
                    self.ui_d.label_box.setText("Hay parámetros sin rellenar")
                else: 
                    micursor.execute("SELECT * FROM LIBROS WHERE AUTOR = '{}'".format(self.ui_d.lineautor.text()))
                    porautor = micursor.fetchall()   

            if self.ui_d.generobox.isChecked():
                cont += 1
                micursor.execute("SELECT * FROM LIBROS WHERE GENERO = '{}'".format(self.ui_d.comboBox.currentText()))
                porgenero = micursor.fetchall()     

            if self.ui_d.puntosbox.isChecked():
                cont += 1
                micursor.execute("SELECT * FROM LIBROS WHERE PUNTUACION = {}".format(self.ui_d.spinBox.value()))
                porpuntos = micursor.fetchall()  
            
            libros  = repetidas(cont, portitulo,porautor,porgenero,porpuntos)
            
            if len(libros) != 0:

                contador = 0
                for libro in libros:
                    contador += 1  
                grid = QGridLayout()
                self.setLayout(grid)
                self.ui_d.tableWidget.setRowCount(contador)
                self.ui_d.tableWidget.setColumnCount(4)
                header = ['TITULO','AUTOR','GENERO','PUNTOS']
                self.ui_d.tableWidget.setHorizontalHeaderLabels(header)
                x = 0
                y = 0


                for titulos, autores, generos, puntos in libros:             
                    new_titulo = QTableWidgetItem(titulos)
                    self.ui_d.tableWidget.setItem(x,y, new_titulo)

                    y += 1
                    new_autor = QTableWidgetItem(autores)
                    self.ui_d.tableWidget.setItem(x,y, new_autor)
                    y += 1
                    new_genero = QTableWidgetItem(generos)
                    self.ui_d.tableWidget.setItem(x,y, new_genero)
                    y += 1
                    new_puntos = QTableWidgetItem(str(puntos))
                    self.ui_d.tableWidget.setItem(x,y, new_puntos)
                    y = 0
                    x += 1
                    
                    self.ui_d.tableWidget.show()
            else:
                self.ui_d.label_box.setText("No existen libros con esas características") 
                
            
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    myapp = VerLibros()
    myapp.show()
    app.exec_()
                       