# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_lecturas.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VerLecturas(object):
    def setupUi(self, VerLecturas):
        VerLecturas.setObjectName("VerLecturas")
        VerLecturas.resize(400, 298)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pixil-frame-0 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VerLecturas.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(VerLecturas)
        self.tableWidget.setGeometry(QtCore.QRect(40, 20, 321, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(VerLecturas)
        QtCore.QMetaObject.connectSlotsByName(VerLecturas)

    def retranslateUi(self, VerLecturas):
        _translate = QtCore.QCoreApplication.translate
        VerLecturas.setWindowTitle(_translate("VerLecturas", "TUS LECTURAS"))

