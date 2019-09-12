# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 160)
        self.label_input = QtWidgets.QLabel(Dialog)
        self.label_input.setGeometry(QtCore.QRect(30, 20, 101, 31))
        self.label_input.setObjectName("label_input")
        self.label_input_2 = QtWidgets.QLabel(Dialog)
        self.label_input_2.setGeometry(QtCore.QRect(150, 20, 221, 31))
        self.label_input_2.setText("")
        self.label_input_2.setObjectName("label_input_2")
        self.label_this_is = QtWidgets.QLabel(Dialog)
        self.label_this_is.setGeometry(QtCore.QRect(160, 70, 31, 16))
        self.label_this_is.setObjectName("label_this_is")
        self.textbox_year = QtWidgets.QLabel(Dialog)
        self.textbox_year.setGeometry(QtCore.QRect(190, 70, 31, 16))
        self.textbox_year.setText("")
        self.textbox_year.setObjectName("textbox_year")
        self.label_year = QtWidgets.QLabel(Dialog)
        self.label_year.setGeometry(QtCore.QRect(230, 70, 16, 16))
        self.label_year.setObjectName("label_year")
        self.textbox_month = QtWidgets.QLabel(Dialog)
        self.textbox_month.setGeometry(QtCore.QRect(250, 70, 16, 16))
        self.textbox_month.setText("")
        self.textbox_month.setObjectName("textbox_month")
        self.label_month = QtWidgets.QLabel(Dialog)
        self.label_month.setGeometry(QtCore.QRect(270, 70, 16, 16))
        self.label_month.setObjectName("label_month")
        self.textbox_name = QtWidgets.QLabel(Dialog)
        self.textbox_name.setGeometry(QtCore.QRect(290, 70, 31, 16))
        self.textbox_name.setText("")
        self.textbox_name.setObjectName("textbox_name")
        self.label_sche = QtWidgets.QLabel(Dialog)
        self.label_sche.setGeometry(QtCore.QRect(330, 70, 41, 16))
        self.label_sche.setObjectName("label_sche")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 110, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textbox_row = QtWidgets.QLineEdit(Dialog)
        self.textbox_row.setGeometry(QtCore.QRect(30, 70, 113, 21))
        self.textbox_row.setObjectName("textbox_row")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_input.setText(_translate("Dialog", "班表.csv檔路徑："))
        self.label_this_is.setText(_translate("Dialog", "這是"))
        self.label_year.setText(_translate("Dialog", "年"))
        self.label_month.setText(_translate("Dialog", "月"))
        self.label_sche.setText(_translate("Dialog", "的班表"))
        self.pushButton.setText(_translate("Dialog", "讀取檔案"))
        self.pushButton_2.setText(_translate("Dialog", "輸出檔案"))
        self.textbox_row.setText(_translate("Dialog", "請在此輸入列數"))
