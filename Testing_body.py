from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets

import operator

import Test_Body
from testing import Ui_MainWindow
class Testing(QMainWindow,Ui_MainWindow):
    def __init__(self,test,NumLesson):
        super().__init__()
        self.setupUi(self)
        self.NumLesson = NumLesson
        self.FillIn()
    def ReadData(self):
        file = open(r'QuestionsAnswers'+r'\'+str(self.NumLesson)+r\'+'Optional_answers')
        result = []
        for i in range(0,5):
            data = []
            for line in file:
                data.append(line)
            result.append(data)
    def FillIn(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("testing", "Тест 1"))
        self.pushButton_2.setText(_translate("testing", "Тест 2"))
        self.pushButton_3.setText(_translate("testing", "Тест 3"))
        self.pushButton_4.setText(_translate("testing", "Тест 4"))