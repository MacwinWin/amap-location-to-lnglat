# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.city_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.city_lineEdit.setEnabled(False)
        self.city_lineEdit.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.city_lineEdit.setFont(font)
        self.city_lineEdit.setText("")
        self.city_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.city_lineEdit.setObjectName("city_lineEdit")
        self.gridLayout_3.addWidget(self.city_lineEdit, 2, 1, 1, 1)
        self.select_file = QtWidgets.QPushButton(self.centralwidget)
        self.select_file.setMaximumSize(QtCore.QSize(83, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.select_file.setFont(font)
        self.select_file.setObjectName("select_file")
        self.gridLayout_3.addWidget(self.select_file, 0, 0, 1, 1)
        self.location_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.location_lineEdit.setEnabled(False)
        self.location_lineEdit.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.location_lineEdit.setFont(font)
        self.location_lineEdit.setText("")
        self.location_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.location_lineEdit.setObjectName("location_lineEdit")
        self.gridLayout_3.addWidget(self.location_lineEdit, 3, 1, 1, 1)
        self.convert_lable = QtWidgets.QLabel(self.centralwidget)
        self.convert_lable.setMaximumSize(QtCore.QSize(83, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.convert_lable.setFont(font)
        self.convert_lable.setText("")
        self.convert_lable.setObjectName("convert_lable")
        self.gridLayout_3.addWidget(self.convert_lable, 3, 3, 1, 1)
        self.select_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.select_textBrowser.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.select_textBrowser.setFont(font)
        self.select_textBrowser.setObjectName("select_textBrowser")
        self.gridLayout_3.addWidget(self.select_textBrowser, 1, 0, 1, 3)
        self.export_lable = QtWidgets.QLabel(self.centralwidget)
        self.export_lable.setMaximumSize(QtCore.QSize(83, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.export_lable.setFont(font)
        self.export_lable.setText("")
        self.export_lable.setObjectName("export_lable")
        self.gridLayout_3.addWidget(self.export_lable, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)
        self.export_file = QtWidgets.QPushButton(self.centralwidget)
        self.export_file.setEnabled(False)
        self.export_file.setMaximumSize(QtCore.QSize(86, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.export_file.setFont(font)
        self.export_file.setObjectName("export_file")
        self.gridLayout_3.addWidget(self.export_file, 4, 0, 1, 1)
        self.start_convert = QtWidgets.QPushButton(self.centralwidget)
        self.start_convert.setEnabled(False)
        self.start_convert.setMaximumSize(QtCore.QSize(83, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.start_convert.setFont(font)
        self.start_convert.setObjectName("start_convert")
        self.gridLayout_3.addWidget(self.start_convert, 3, 2, 1, 1)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setMaximumSize(QtCore.QSize(83, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.gridLayout_3.addWidget(self.clear, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "批量转换经纬度v1.1"))
        self.label_2.setText(_translate("MainWindow", "选择城市列："))
        self.select_file.setText(_translate("MainWindow", "选择文件"))
        self.select_textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "选择地址列："))
        self.export_file.setText(_translate("MainWindow", "导出文件"))
        self.start_convert.setText(_translate("MainWindow", "开始转换"))
        self.clear.setText(_translate("MainWindow", "清空"))

