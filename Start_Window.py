# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Start_Window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 600)
        MainWindow.setStyleSheet("background-color: rgb(39, 60, 117);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 120, 401, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Lessons = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Lessons.sizePolicy().hasHeightForWidth())
        self.pushButton_Lessons.setSizePolicy(sizePolicy)
        self.pushButton_Lessons.setStyleSheet("background-color: rgb(0, 151, 230);")
        self.pushButton_Lessons.setObjectName("pushButton_Lessons")
        self.verticalLayout.addWidget(self.pushButton_Lessons)
        self.pushButton_Test = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Test.sizePolicy().hasHeightForWidth())
        self.pushButton_Test.setSizePolicy(sizePolicy)
        self.pushButton_Test.setStyleSheet("background-color: rgb(0, 151, 230);")
        self.pushButton_Test.setObjectName("pushButton_Test")
        self.verticalLayout.addWidget(self.pushButton_Test)
        self.pushButton_Exit = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Exit.sizePolicy().hasHeightForWidth())
        self.pushButton_Exit.setSizePolicy(sizePolicy)
        self.pushButton_Exit.setStyleSheet("background-color: rgb(0, 151, 230);")
        self.pushButton_Exit.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.verticalLayout.addWidget(self.pushButton_Exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Lessons.setText(_translate("MainWindow", "Уроки"))
        self.pushButton_Test.setText(_translate("MainWindow", "Тесты"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Выход"))

