# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/3/23 15:21
# @File    : 20-graduation-project Show.py
# @Software: PyCharm


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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(11, 33, 608, 109))
        self.input.setObjectName("input")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(330, 310, 93, 28))
        self.cancel.setObjectName("cancel")
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(11, 171, 608, 109))
        self.output.setObjectName("output")
        self.in1 = QtWidgets.QLabel(self.centralwidget)
        self.in1.setGeometry(QtCore.QRect(11, 11, 75, 15))
        self.in1.setObjectName("in1")
        self.out = QtWidgets.QLabel(self.centralwidget)
        self.out.setGeometry(QtCore.QRect(11, 149, 60, 16))
        self.out.setObjectName("out")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(170, 310, 93, 28))
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
        self.cancel.setText(_translate("MainWindow", "退出"))
        self.in1.setText(_translate("MainWindow", "请输入句子"))
        self.out.setText(_translate("MainWindow", "显示结果"))
        self.run.setText(_translate("MainWindow", "运行"))
