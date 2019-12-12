from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import testing
import Testing_body
import operator
import MainBody
import Start_Window

from Test import Ui_MainWindow
class Test(QMainWindow,Ui_MainWindow):
    def __init__(self,test):
        super().__init__()
        self.setupUi(self)
        for n in range(1,21):
            getattr(self,"pushButton_%s"%n).pressed.connect(lambda v=n: self.openTesting(v))
        self.pushButton_exit.pressed.connect(self.back)
        self.test = test
    def openTesting(self,v):
        self.testing = Testing_body.Testing(self,v)
        self.testing.show()
        self.hide()
    def back(self):
        self.test.show()
        self.hide()