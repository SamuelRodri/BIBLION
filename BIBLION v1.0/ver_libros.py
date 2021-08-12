# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_libros.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ver_libros(object):
    def setupUi(self, ver_libros):
        ver_libros.setObjectName("ver_libros")
        ver_libros.resize(531, 468)
        self.tableWidget = QtWidgets.QTableWidget(ver_libros)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 481, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(ver_libros)
        QtCore.QMetaObject.connectSlotsByName(ver_libros)

    def retranslateUi(self, ver_libros):
        _translate = QtCore.QCoreApplication.translate
        ver_libros.setWindowTitle(_translate("ver_libros", "TUS LIBROS"))

