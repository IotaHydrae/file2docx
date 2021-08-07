# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 164)
        self.reset = QtWidgets.QPushButton(Dialog)
        self.reset.setGeometry(QtCore.QRect(410, 40, 91, 41))
        self.reset.setObjectName("reset")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.label_2.setObjectName("label_2")
        self.pro_dict = QtWidgets.QLineEdit(Dialog)
        self.pro_dict.setGeometry(QtCore.QRect(90, 40, 271, 21))
        self.pro_dict.setObjectName("pro_dict")
        self.output_dict = QtWidgets.QLineEdit(Dialog)
        self.output_dict.setGeometry(QtCore.QRect(90, 80, 271, 20))
        self.output_dict.setObjectName("output_dict")
        self.generate = QtWidgets.QPushButton(Dialog)
        self.generate.setGeometry(QtCore.QRect(410, 110, 91, 41))
        self.generate.setObjectName("generate")
        self.project = QtWidgets.QPushButton(Dialog)
        self.project.setGeometry(QtCore.QRect(360, 40, 21, 21))
        self.project.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/JessenHua/Pictures/dict.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project.setIcon(icon)
        self.project.setObjectName("project")
        self.output = QtWidgets.QPushButton(Dialog)
        self.output.setGeometry(QtCore.QRect(360, 80, 21, 21))
        self.output.setText("")
        self.output.setIcon(icon)
        self.output.setObjectName("output")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(110, 130, 251, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "文档生成器"))
        self.reset.setText(_translate("Dialog", "重置"))
        self.label.setText(_translate("Dialog", "项目文件夹"))
        self.label_2.setText(_translate("Dialog", "文档生成位置"))
        self.generate.setText(_translate("Dialog", "生成"))
