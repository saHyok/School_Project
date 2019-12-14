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
        self.options = []
        self.answers = []
        self.questions = []
        self.ReadData()
        self.FillIn()
    def ReadData(self):
        Num = str(self.NumLesson)
        roote = r'QuestionsAnswers'+'\\'+Num+'\Optional_answers.txt'
        file = open(roote)
        for line in file:
           self.options.append(line)
        RightRoote = r'QuestionsAnswers'+'\\'+Num+'\Answers.txt'
        file = open(RightRoote)
        for line in file:
            self.answers.append(line)
        QuestionRoote = r'QuestionsAnswers'+'\\'+Num+'\Questions.txt'
        file = open(QuestionRoote)
        for line in file:
            self.questions.append(line)
    def FillIn(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("testing", self.options[0]))
        self.pushButton_2.setText(_translate("testing", self.options[1]))
        self.pushButton_3.setText(_translate("testing", self.options[2]))
        self.pushButton_4.setText(_translate("testing", self.options[3]))
        self.textBrowser.setHtml(_translate("MainWindow", self.questions[0]))