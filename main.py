from PyQt5.QtGui import *
from PyQt5.QtWidgets import *   
from PyQt5.QtCore import *
import sys
sys.path.append("/../")
import Lessons_Body
import Test_Body

import MainBody
from Start_Window import Ui_MainWindow
from MainBody import MainWindow



if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("")

    window = MainWindow('')
    app.exec_()
