from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Lessons_Body
import Test_Body
import Test

import operator

from Start_Window import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,MainBody):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.MainBody = MainBody
        self.pushButton_Exit.pressed.connect(QCoreApplication.instance().quit)
        self.pushButton_Lessons.pressed.connect(self.openLessons)
        self.pushButton_Test.pressed.connect(self.openTest)
        self.lessons = Lessons_Body.Lessons(self)
        self.test = Test_Body.Test(self)
        self.show()
    def openLessons(self):
        self.lessons.show()
        self.hide()
    def openTest(self):
        self.test.show()
        self.hide()