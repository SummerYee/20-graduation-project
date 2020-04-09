# -*- coding: utf-8 -*-
# @Author  : 王小易 / SummerYee
# @Time    : 2020/3/23 16:34
# @File    : 20-graduation-project Show.py
# @Software: PyCharm


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Design import Ui_MainWindow
from main import query_label


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。
        self.run.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        self.cancel.clicked.connect(self.close)


    def display(self):
        # 利用Test Edit控件对象text()函数获取界面输入
        #while(True):
            your_query_sentence = self.input.toPlainText()
            predict_label = query_label(your_query_sentence)
            # 利用text Browser控件对象setText()函数设置界面显示
            self.output.setText( "Predict label: " + predict_label)
            #if your_query_sentence == '0':
               # break


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MainWindow()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

