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
        ver_libros.resize(527, 459)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pixil-frame-0 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ver_libros.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(ver_libros)
        self.tableWidget.setGeometry(QtCore.QRect(20, 230, 491, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.titulobox = QtWidgets.QCheckBox(ver_libros)
        self.titulobox.setGeometry(QtCore.QRect(50, 70, 70, 17))
        self.titulobox.setObjectName("titulobox")
        self.label = QtWidgets.QLabel(ver_libros)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.label.setObjectName("label")
        self.linetitulo = QtWidgets.QLineEdit(ver_libros)
        self.linetitulo.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.linetitulo.setDragEnabled(False)
        self.linetitulo.setReadOnly(False)
        self.linetitulo.setObjectName("linetitulo")
        self.generobox = QtWidgets.QCheckBox(ver_libros)
        self.generobox.setGeometry(QtCore.QRect(290, 70, 70, 17))
        self.generobox.setObjectName("generobox")
        self.autorbox = QtWidgets.QCheckBox(ver_libros)
        self.autorbox.setGeometry(QtCore.QRect(50, 120, 70, 17))
        self.autorbox.setObjectName("autorbox")
        self.lineautor = QtWidgets.QLineEdit(ver_libros)
        self.lineautor.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.lineautor.setDragEnabled(False)
        self.lineautor.setReadOnly(False)
        self.lineautor.setObjectName("lineautor")
        self.puntosbox = QtWidgets.QCheckBox(ver_libros)
        self.puntosbox.setGeometry(QtCore.QRect(290, 120, 91, 17))
        self.puntosbox.setObjectName("puntosbox")
        self.comboBox = QtWidgets.QComboBox(ver_libros)
        self.comboBox.setGeometry(QtCore.QRect(360, 70, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.spinBox = QtWidgets.QSpinBox(ver_libros)
        self.spinBox.setGeometry(QtCore.QRect(381, 120, 91, 22))
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.pushbuscar = QtWidgets.QPushButton(ver_libros)
        self.pushbuscar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.pushbuscar.setObjectName("pushbuscar")
        self.label_box = QtWidgets.QLabel(ver_libros)
        self.label_box.setGeometry(QtCore.QRect(146, 200, 251, 20))
        self.label_box.setText("")
        self.label_box.setAlignment(QtCore.Qt.AlignCenter)
        self.label_box.setObjectName("label_box")
        self.todosBox = QtWidgets.QCheckBox(ver_libros)
        self.todosBox.setGeometry(QtCore.QRect(120, 30, 70, 17))
        self.todosBox.setObjectName("todosBox")

        self.retranslateUi(ver_libros)
        QtCore.QMetaObject.connectSlotsByName(ver_libros)

    def retranslateUi(self, ver_libros):
        _translate = QtCore.QCoreApplication.translate
        ver_libros.setWindowTitle(_translate("ver_libros", "TUS LIBROS"))
        self.titulobox.setText(_translate("ver_libros", "Título:"))
        self.label.setText(_translate("ver_libros", "Búsqueda:"))
        self.generobox.setText(_translate("ver_libros", "Género:"))
        self.autorbox.setText(_translate("ver_libros", "Autor:"))
        self.puntosbox.setText(_translate("ver_libros", "Puntuación:"))
        self.pushbuscar.setText(_translate("ver_libros", "Buscar"))
        self.todosBox.setText(_translate("ver_libros", "Ver Todos"))

