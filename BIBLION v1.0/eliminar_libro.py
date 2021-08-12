# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eliminar_libro.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Eliminar_Libro(object):
    def setupUi(self, Eliminar_Libro):
        Eliminar_Libro.setObjectName("Eliminar_Libro")
        Eliminar_Libro.resize(409, 230)
        self.label = QtWidgets.QLabel(Eliminar_Libro)
        self.label.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Eliminar_Libro)
        self.pushButton.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Eliminar_Libro)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Eliminar_Libro)
        self.lineEdit.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Eliminar_Libro)
        self.label_2.setGeometry(QtCore.QRect(25, 160, 221, 20))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Eliminar_Libro)
        self.pushButton_2.clicked.connect(Eliminar_Libro.close)
        QtCore.QMetaObject.connectSlotsByName(Eliminar_Libro)

    def retranslateUi(self, Eliminar_Libro):
        _translate = QtCore.QCoreApplication.translate
        Eliminar_Libro.setWindowTitle(_translate("Eliminar_Libro", "Eliminar Libro"))
        self.label.setText(_translate("Eliminar_Libro", "Escoja el libro a eliminar"))
        self.pushButton.setText(_translate("Eliminar_Libro", "Eliminar"))
        self.pushButton_2.setText(_translate("Eliminar_Libro", "Cancelar"))

