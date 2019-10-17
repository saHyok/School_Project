from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import testing
import Testing_body
import operator

from Test import Ui_MainWindow
class Test(QMainWindow,Ui_MainWindow):
    def __init__(self,MainWindow):
        super().__init__()
        self.setupUi(self)
        self.testing = Testing_body.Testing(self)
        self.pushButton_1.pressed.connect(self.openTesting)
    def openTesting(self):
        self.testing.show()
        self.hide()