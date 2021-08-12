# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BIBLION(object):
    def setupUi(self, BIBLION):
        BIBLION.setObjectName("BIBLION")
        BIBLION.resize(397, 301)
        self.layoutWidget = QtWidgets.QWidget(BIBLION)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 20, 211, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(BIBLION)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 160, 311, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_aniadir = QtWidgets.QPushButton(self.layoutWidget1)
        self.boton_aniadir.setObjectName("boton_aniadir")
        self.horizontalLayout.addWidget(self.boton_aniadir)
        self.boton_eliminar = QtWidgets.QPushButton(self.layoutWidget1)
        self.boton_eliminar.setObjectName("boton_eliminar")
        self.horizontalLayout.addWidget(self.boton_eliminar)
        self.boton_estadisticas = QtWidgets.QPushButton(self.layoutWidget1)
        self.boton_estadisticas.setObjectName("boton_estadisticas")
        self.horizontalLayout.addWidget(self.boton_estadisticas)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.boton_borrar = QtWidgets.QPushButton(self.layoutWidget1)
        self.boton_borrar.setObjectName("boton_borrar")
        self.horizontalLayout_2.addWidget(self.boton_borrar)
        self.boton_ver = QtWidgets.QPushButton(self.layoutWidget1)
        self.boton_ver.setObjectName("boton_ver")
        self.horizontalLayout_2.addWidget(self.boton_ver)
        self.boton_lecturas = QtWidgets.QPushButton(self.layoutWidget1)
        self.boton_lecturas.setObjectName("boton_lecturas")
        self.horizontalLayout_2.addWidget(self.boton_lecturas)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(BIBLION)
        QtCore.QMetaObject.connectSlotsByName(BIBLION)

    def retranslateUi(self, BIBLION):
        _translate = QtCore.QCoreApplication.translate
        BIBLION.setWindowTitle(_translate("BIBLION", "BIBLION"))
        self.label.setText(_translate("BIBLION", "BIENVENIDO A BIBLION"))
        self.label_2.setText(_translate("BIBLION", "Su base de datos particular de libros"))
        self.label_3.setText(_translate("BIBLION", "¿Qué acción desea realizar?"))
        self.boton_aniadir.setText(_translate("BIBLION", "Añadir Libro"))
        self.boton_eliminar.setText(_translate("BIBLION", "Eliminar Libro"))
        self.boton_estadisticas.setText(_translate("BIBLION", "Estadísticas"))
        self.boton_borrar.setText(_translate("BIBLION", "Borrar Todo"))
        self.boton_ver.setText(_translate("BIBLION", "Ver Libros"))
        self.boton_lecturas.setText(_translate("BIBLION", "Próximas Lecturas"))

