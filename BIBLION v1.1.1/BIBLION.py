#Base de datos de libros "BIBLION"

"""Hacemos las importaciones necesarias"""

from PyQt5 import QtCore, QtGui, QtWidgets
from ventana_principal import Ui_BIBLION
from anadir_libro import Ui_Aniadir_Libro
from borrar_todo import Ui_Borrar_Base
from eliminar_libro import Ui_Eliminar_Libro
from ver_libros import Ui_ver_libros
from lecturas import Ui_Proximas_Lecturas
from estadisticas import Ui_Estadisticas
from ver_lecturas import Ui_VerLecturas

"""Importamos los módulos para el funcionamiento de las subventanas"""

from Func_AnadirLibro import AnadirLibro
from Func_BorrarBase import BorrarBase
from Func_Lecturas import Lecturas
from Func_EliminarLibro import EliminarLibro
from Func_Estadisticas import Estadisticas
from Func_VerLibros import VerLibros
from Func_VerLecturas import VerLecturas


import os, sys
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)
    
import sqlite3
if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

"""Conectamos con la base de datos y creamos las tablas LECTURAS y LIBROS (si no lo están)"""

miconexion = sqlite3.connect("BASE DE DATOS.DB")
micursor = miconexion.cursor()
try:
    micursor.execute("CREATE TABLE LECTURAS(TITULO VARCHAR(20), AUTOR VARCHAR(20))")
    micursor.execute("CREATE TABLE LIBROS(TITULO VARCHAR(20), AUTOR VARCHAR(20), GENERO VARCHAR(20), PUNTUACION INTEGER)")
except:
    sqlite3.OperationalError

"""Clase de la ventana principal"""

class VentanaPrincipal(QtWidgets.QDialog):
  
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_d = Ui_BIBLION()
        self.ui_d.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icono.png'))
        self.setWindowTitle("BIBLION v1.1.1")
        QtWidgets.QDialog.setFixedSize(self,397,301)


        """Conectamos los botones con las subventanas"""

        self.ui_d.boton_aniadir.clicked.connect(self.AbrirVentanaAnadir)
        self.ui_d.boton_borrar.clicked.connect(self.AbrirVentanaBorrar)
        self.ui_d.boton_eliminar.clicked.connect(self.AbrirVentanaEliminar)
        self.ui_d.boton_ver.clicked.connect(self.AbrirVentanaVer)
        self.ui_d.boton_lecturas.clicked.connect(self.AbrirVentanaLecturas)
        self.ui_d.boton_estadisticas.clicked.connect(self.AbrirVentanaEstadisticas)

#DEFINIMOS TODAS LAS FUNCIONES QUE ABREN LAS SUBVENTANAS
    
    def AbrirVentanaAnadir(self):
        self.w = AnadirLibro()
        self.w.show()
        
    def AbrirVentanaBorrar(self):
        self.w = BorrarBase()
        self.w.show()

    def AbrirVentanaEliminar(self):
        self.w = EliminarLibro()
        self.w.show()

    def AbrirVentanaVer(self):
        self.w = VerLibros()
        self.w.show()

    def AbrirVentanaLecturas(self):
        self.w = Lecturas()
        self.w.show()

    def AbrirVentanaEstadisticas(self):
        self.w = Estadisticas()
        self.w.show()
    
    miconexion.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    myapp = VentanaPrincipal()
    myapp.show()
    app.exec_()
    