# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 400)
        MainWindow.setMinimumSize(QtCore.QSize(640, 400))
        MainWindow.setMaximumSize(QtCore.QSize(640, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("小易.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 40, 608, 109))
        self.input.setObjectName("input")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(330, 320, 93, 28))
        self.cancel.setObjectName("cancel")
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 190, 608, 109))
        self.output.setObjectName("output")
        self.in1 = QtWidgets.QLabel(self.centralwidget)
        self.in1.setGeometry(QtCore.QRect(11, 11, 151, 21))
        self.in1.setObjectName("in1")
        self.out = QtWidgets.QLabel(self.centralwidget)
        self.out.setGeometry(QtCore.QRect(11, 160, 161, 31))
        self.out.setObjectName("out")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(170, 320, 93, 28))
        self.run.setObjectName("run")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "意图识别"))
        self.cancel.setText(_translate("MainWindow", "Quit"))
        self.in1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Input sentence</span></p></body></html>"))
        self.out.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Predict label</span></p></body></html>"))
        self.run.setText(_translate("MainWindow", "Run"))

