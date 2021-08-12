# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadisticas.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Estadisticas(object):
    def setupUi(self, Estadisticas):
        Estadisticas.setObjectName("Estadisticas")
        Estadisticas.resize(256, 201)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pixil-frame-0 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Estadisticas.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Estadisticas)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 201, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_libros = QtWidgets.QLabel(self.layoutWidget)
        self.label_libros.setText("")
        self.label_libros.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_libros.setObjectName("label_libros")
        self.verticalLayout.addWidget(self.label_libros)
        self.label_autor_fav = QtWidgets.QLabel(self.layoutWidget)
        self.label_autor_fav.setText("")
        self.label_autor_fav.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_autor_fav.setObjectName("label_autor_fav")
        self.verticalLayout.addWidget(self.label_autor_fav)
        self.label_genero_fav = QtWidgets.QLabel(self.layoutWidget)
        self.label_genero_fav.setText("")
        self.label_genero_fav.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_genero_fav.setObjectName("label_genero_fav")
        self.verticalLayout.addWidget(self.label_genero_fav)
        self.label_libro_fav = QtWidgets.QLabel(self.layoutWidget)
        self.label_libro_fav.setText("")
        self.label_libro_fav.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_libro_fav.setObjectName("label_libro_fav")
        self.verticalLayout.addWidget(self.label_libro_fav)
        self.label_ultimo_libro = QtWidgets.QLabel(self.layoutWidget)
        self.label_ultimo_libro.setText("")
        self.label_ultimo_libro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ultimo_libro.setObjectName("label_ultimo_libro")
        self.verticalLayout.addWidget(self.label_ultimo_libro)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Estadisticas)
        QtCore.QMetaObject.connectSlotsByName(Estadisticas)

    def retranslateUi(self, Estadisticas):
        _translate = QtCore.QCoreApplication.translate
        Estadisticas.setWindowTitle(_translate("Estadisticas", "TUS ESTADÍSTICAS"))
        self.label.setText(_translate("Estadisticas", "Libros leídos:"))
        self.label_2.setText(_translate("Estadisticas", "Autor Favorito:"))
        self.label_3.setText(_translate("Estadisticas", "Género Favorito:"))
        self.label_4.setText(_translate("Estadisticas", "Tu libro favorito:"))
        self.label_5.setText(_translate("Estadisticas", "Último Libro Leido:"))

