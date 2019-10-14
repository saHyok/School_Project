from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import webbrowser as wb

import operator

from Lessons import Ui_MainWindow
class Lessons(QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setupUi(self)
        self.pushButton_1.pressed.connect(self.openLesson)
    def openLesson(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\keyboard-shortcuts-windows.pdf')