# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lecturas.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Proximas_Lecturas(object):
    def setupUi(self, Proximas_Lecturas):
        Proximas_Lecturas.setObjectName("Proximas_Lecturas")
        Proximas_Lecturas.resize(331, 266)
        self.label = QtWidgets.QLabel(Proximas_Lecturas)
        self.label.setGeometry(QtCore.QRect(35, 20, 281, 20))
        self.label.setObjectName("label")
        self.linel_titulo = QtWidgets.QLineEdit(Proximas_Lecturas)
        self.linel_titulo.setGeometry(QtCore.QRect(130, 70, 133, 20))
        self.linel_titulo.setObjectName("linel_titulo")
        self.linel_autor = QtWidgets.QLineEdit(Proximas_Lecturas)
        self.linel_autor.setGeometry(QtCore.QRect(130, 110, 133, 20))
        self.linel_autor.setObjectName("linel_autor")
        self.label_2 = QtWidgets.QLabel(Proximas_Lecturas)
        self.label_2.setGeometry(QtCore.QRect(35, 110, 46, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Proximas_Lecturas)
        self.label_3.setGeometry(QtCore.QRect(35, 70, 46, 13))
        self.label_3.setObjectName("label_3")
        self.lecturas_aniadir = QtWidgets.QPushButton(Proximas_Lecturas)
        self.lecturas_aniadir.setGeometry(QtCore.QRect(60, 170, 75, 23))
        self.lecturas_aniadir.setObjectName("lecturas_aniadir")
        self.pushButton_2 = QtWidgets.QPushButton(Proximas_Lecturas)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_lecturas_mensaje = QtWidgets.QLabel(Proximas_Lecturas)
        self.label_lecturas_mensaje.setGeometry(QtCore.QRect(40, 140, 241, 20))
        self.label_lecturas_mensaje.setText("")
        self.label_lecturas_mensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lecturas_mensaje.setObjectName("label_lecturas_mensaje")
        self.lectura_ver = QtWidgets.QPushButton(Proximas_Lecturas)
        self.lectura_ver.setGeometry(QtCore.QRect(130, 220, 81, 21))
        self.lectura_ver.setObjectName("lectura_ver")

        self.retranslateUi(Proximas_Lecturas)
        self.pushButton_2.clicked.connect(Proximas_Lecturas.close)
        QtCore.QMetaObject.connectSlotsByName(Proximas_Lecturas)
        Proximas_Lecturas.setTabOrder(self.linel_titulo, self.linel_autor)
        Proximas_Lecturas.setTabOrder(self.linel_autor, self.lecturas_aniadir)
        Proximas_Lecturas.setTabOrder(self.lecturas_aniadir, self.pushButton_2)

    def retranslateUi(self, Proximas_Lecturas):
        _translate = QtCore.QCoreApplication.translate
        Proximas_Lecturas.setWindowTitle(_translate("Proximas_Lecturas", "PRÓXIMAS LECTURAS"))
        self.label.setText(_translate("Proximas_Lecturas", "Escriba aquí los libros que le gustaría leer pronto:"))
        self.label_2.setText(_translate("Proximas_Lecturas", "Autor:"))
        self.label_3.setText(_translate("Proximas_Lecturas", "Título:"))
        self.lecturas_aniadir.setText(_translate("Proximas_Lecturas", "Añadir"))
        self.pushButton_2.setText(_translate("Proximas_Lecturas", "Cancelar"))
        self.lectura_ver.setText(_translate("Proximas_Lecturas", "Ver Lecturas"))

