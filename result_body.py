from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets

import operator
import Test_Body
import MainBody
from result import Ui_MainWindow
class result(QMainWindow,Ui_MainWindow):
    def __init__(self,testing):
        super().__init__()
        self.setupUi(self)
        self.backk = MainBody.MainWindow(self)
        self.pushButton_1.pressed.connect(self.exitt)
        self.showScore(testing)
    def showScore(self,testing):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("MainWindow",'Количество правильных ответов:'+str(testing.score)))
        self.pushButton_1.setText(_translate("testing", "Выход"))
    def exitt(self):
        self.backk.show()
        self.hide()