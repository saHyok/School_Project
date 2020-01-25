from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets

import operator

import Test_Body
import result_body
from testing import Ui_MainWindow
class Testing(QMainWindow,Ui_MainWindow):
    def __init__(self,test,NumLesson):
        super().__init__()
        self.setupUi(self)
        self.NumLesson = NumLesson
        self.options = []
        self.answers = []
        self.questions = []
<<<<<<< HEAD
        self.score = 0
        self.ReadData()
        self.i = 1
        self.j = 1
=======
        self.ReadData()
>>>>>>> e38375f641006106d54c83e53e0e8df4a69e30aa
        self.FillIn()
        for n in range(1,5):
            getattr(self,"pushButton_%s"%n).pressed.connect(lambda v=n: self.MoveOn(v))
    def ReadData(self):
        Num = str(self.NumLesson)
        roote = r'QuestionsAnswers'+'\\'+Num+'\Optional_answers.txt'
        file = open(roote)
        for line in file:
           self.options.append(line)
<<<<<<< HEAD
        file.close()
=======
>>>>>>> e38375f641006106d54c83e53e0e8df4a69e30aa
        RightRoote = r'QuestionsAnswers'+'\\'+Num+'\Answers.txt'
        file = open(RightRoote)
        for line in file:
            self.answers.append(line)
<<<<<<< HEAD
        file.close()
=======
>>>>>>> e38375f641006106d54c83e53e0e8df4a69e30aa
        QuestionRoote = r'QuestionsAnswers'+'\\'+Num+'\Questions.txt'
        file = open(QuestionRoote)
        for line in file:
            self.questions.append(line)
<<<<<<< HEAD
        file.close()
    def FillIn(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("testing", self.options[1]))
        self.pushButton_2.setText(_translate("testing", self.options[2]))
        self.pushButton_3.setText(_translate("testing", self.options[3]))
        self.pushButton_4.setText(_translate("testing", self.options[4]))
        self.textBrowser.setHtml(_translate("MainWindow", self.questions[1]))
    def chekAnswer(self,v):
        if self.options[v+self.i-1]==self.answers[self.j]:
            self.score += 1
    def MoveOn(self,v):
        self.chekAnswer(v)
        self.i+=4
        self.j+=1
        if self.j == 6:
            self.result = result_body.result(self)
            self.hide()
            self.result.show()
        else:
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_1.setText(_translate("testing", self.options[self.i]))
            self.pushButton_2.setText(_translate("testing", self.options[1+self.i]))
            self.pushButton_3.setText(_translate("testing", self.options[2+self.i]))
            self.pushButton_4.setText(_translate("testing", self.options[3+self.i]))
            self.textBrowser.setHtml(_translate("MainWindow", self.questions[self.j]))
=======
    def FillIn(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_1.setText(_translate("testing", self.options[0]))
        self.pushButton_2.setText(_translate("testing", self.options[1]))
        self.pushButton_3.setText(_translate("testing", self.options[2]))
        self.pushButton_4.setText(_translate("testing", self.options[3]))
        self.textBrowser.setHtml(_translate("MainWindow", self.questions[0]))
>>>>>>> e38375f641006106d54c83e53e0e8df4a69e30aa
