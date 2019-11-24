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
        self.pushButton_1.pressed.connect(self.openLesson_1)
        self.pushButton_2.pressed.connect(self.openLesson_2)
        self.pushButton_3.pressed.connect(self.openLesson_3)
        self.pushButton_4.pressed.connect(self.openLesson_4)
        self.pushButton_5.pressed.connect(self.openLesson_5)
        self.pushButton_6.pressed.connect(self.openLesson_6)
        self.pushButton_7.pressed.connect(self.openLesson_7)
        self.pushButton_8.pressed.connect(self.openLesson_8)
        self.pushButton_9.pressed.connect(self.openLesson_9)
        self.pushButton_10.pressed.connect(self.openLesson_10)
        self.pushButton_11.pressed.connect(self.openLesson_11)
        self.pushButton_12.pressed.connect(self.openLesson_12)
        self.pushButton_13.pressed.connect(self.openLesson_13)
        self.pushButton_14.pressed.connect(self.openLesson_14)
        self.pushButton_15.pressed.connect(self.openLesson_15)
        self.pushButton_16.pressed.connect(self.openLesson_16)
        self.pushButton_17.pressed.connect(self.openLesson_17)
        self.pushButton_18.pressed.connect(self.openLesson_18)
        self.pushButton_back.pressed.connect(self.Back)
        self.MainWindow = MainWindow
    def openLesson_1(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_1.pdf')
    def openLesson_2(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_2.pdf')
    def openLesson_3(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_3.pdf')
    def openLesson_4(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_4.pdf')
    def openLesson_5(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_5.pdf')
    def openLesson_6(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_6.pdf')
    def openLesson_7(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_7.pdf')
    def openLesson_8(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_8.pdf')
    def openLesson_9(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_9.pdf')
    def openLesson_10(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_10.pdf')
    def openLesson_11(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_11.pdf')
    def openLesson_12(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_12.pdf')
    def openLesson_13(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_13.pdf')
    def openLesson_14(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_14.pdf')
    def openLesson_15(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_15.pdf')
    def openLesson_16(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_16.pdf')
    def openLesson_17(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_17.pdf')
    def openLesson_18(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_18.pdf')
    def openLesson_19(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_19.pdf')
    def openLesson_20(self):
        wb.open_new(r'C:\Users\Меднов Александр\Desktop\Project\Lessons\lesson_20.pdf')
    def Back(self):
        self.MainWindow.show()
        self.hide()