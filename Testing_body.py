from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

import Test_Body
from testing import Ui_MainWindow
class Testing(QMainWindow,Ui_MainWindow):
    def __init__(self,test):
        super().__init__()
        self.setupUi(self)