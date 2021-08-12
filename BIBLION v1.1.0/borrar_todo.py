# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrar_todo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Borrar_Base(object):
    def setupUi(self, Borrar_Base):
        Borrar_Base.setObjectName("Borrar_Base")
        Borrar_Base.resize(273, 116)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pixil-frame-0 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Borrar_Base.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Borrar_Base)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 209, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.layoutWidget1 = QtWidgets.QWidget(Borrar_Base)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 70, 158, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.borrar_borrar = QtWidgets.QPushButton(self.layoutWidget1)
        self.borrar_borrar.setObjectName("borrar_borrar")
        self.horizontalLayout.addWidget(self.borrar_borrar)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Borrar_Base)
        self.pushButton_2.clicked.connect(Borrar_Base.close)
        self.borrar_borrar.clicked.connect(Borrar_Base.close)
        QtCore.QMetaObject.connectSlotsByName(Borrar_Base)

    def retranslateUi(self, Borrar_Base):
        _translate = QtCore.QCoreApplication.translate
        Borrar_Base.setWindowTitle(_translate("Borrar_Base", "BORRAR BASE DE DATOS"))
        self.label.setText(_translate("Borrar_Base", "Si continua borrará TODA su base de datos"))
        self.label_2.setText(_translate("Borrar_Base", "¿Desea continuar?"))
        self.borrar_borrar.setText(_translate("Borrar_Base", "Sí"))
        self.pushButton_2.setText(_translate("Borrar_Base", "No"))

