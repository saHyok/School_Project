from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import testing

import operator

from Test import Ui_MainWindow
class Test(QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setupUi(self)
        # for i in range (1,20):
            # getattr(self,'pushButton_%s'%i).pressed.connect(self.Test)