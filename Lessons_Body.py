from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import webbrowser as wb
import MainBody

import operator

from Lessons import Ui_MainWindow
class Lessons(QMainWindow,Ui_MainWindow):
    def __init__(self, MainWindow):
        super().__init__()
        self.setupUi(self)
        self.pushButton_back.pressed.connect(self.Back)
        self.MainWindow = MainWindow
        self.roote = r"Lessons\lesson_"
        for n in range(1,21):
            getattr(self,"pushButton_%s"%n).pressed.connect(lambda v=n: self.openLesson(v))
    def openLesson(self,v):
        wb.open_new(self.roote+str(v)+'.pdf')
    def Back(self):
        self.MainWindow.show()
        self.hide()