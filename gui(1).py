# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def action(self):
        self.lcdNumber_sensitivity.display(8)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ###Frame sensitivity 
        self.frame_sensitivity = QtWidgets.QFrame(self.centralwidget)
        self.frame_sensitivity.setGeometry(QtCore.QRect(70, 20, 271, 381))
        self.frame_sensitivity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sensitivity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sensitivity.setObjectName("frame_sensitivity")
        self.label_sensitivity = QtWidgets.QLabel(self.frame_sensitivity)
        self.label_sensitivity.setGeometry(QtCore.QRect(90, 30, 74, 16))
        self.label_sensitivity.setObjectName("label_sensitivity")
        ###Choisir la sensitivity  
        self.spinBox_sensitivity = QtWidgets.QSpinBox(self.frame_sensitivity)
        self.spinBox_sensitivity.setGeometry(QtCore.QRect(50, 80, 42, 22))
        self.spinBox_sensitivity.setObjectName("spinBox_sensitivity")
        ###Boutton pour valider la sensitivity choisie
        self.pushButton_sensitivity = QtWidgets.QPushButton(self.frame_sensitivity)
        self.pushButton_sensitivity.setGeometry(QtCore.QRect(130, 80, 93, 28))
        self.pushButton_sensitivity.setObjectName("pushButton_sensitivity")
        ###Boutton pour obtenir la sensitivity
        self.pushButton_getsensitivity = QtWidgets.QPushButton(self.frame_sensitivity)
        self.pushButton_getsensitivity.setGeometry(QtCore.QRect(60, 240, 151, 31))
        self.pushButton_getsensitivity.setObjectName("pushButton_getsensitivity")
        self.pushButton_getsensitivity.clicked.connect(self.action)
        ###LCD pour afficher la valeur de la sensitivity
        self.lcdNumber_sensitivity = QtWidgets.QLCDNumber(self.frame_sensitivity)
        self.lcdNumber_sensitivity.setGeometry(QtCore.QRect(100, 300, 64, 23))
        self.lcdNumber_sensitivity.setObjectName("lcdNumber_sensitivity")

        ###Frame tension 
        self.frame_tension = QtWidgets.QFrame(self.centralwidget)
        self.frame_tension.setGeometry(QtCore.QRect(680, 50, 291, 201))
        self.frame_tension.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tension.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tension.setObjectName("frame_tension")
        self.label_tension = QtWidgets.QLabel(self.frame_tension)
        self.label_tension.setGeometry(QtCore.QRect(120, 20, 55, 16))
        self.label_tension.setObjectName("label_tension")
        ###Boutton pour obtenir la tension
        self.pushButton_gettension = QtWidgets.QPushButton(self.frame_tension)
        self.pushButton_gettension.setGeometry(QtCore.QRect(100, 50, 108, 28))
        self.pushButton_gettension.setObjectName("pushButton_gettension")
        ###LCD pour afficher la tension
        self.lcdNumber_tension = QtWidgets.QLCDNumber(self.frame_tension)
        self.lcdNumber_tension.setGeometry(QtCore.QRect(120, 100, 64, 23))
        self.lcdNumber_tension.setObjectName("lcdNumber_tension")

        ###Frame fréquence 
        self.frame_frequence = QtWidgets.QFrame(self.centralwidget)
        self.frame_frequence.setGeometry(QtCore.QRect(640, 310, 361, 321))
        self.frame_frequence.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_frequence.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_frequence.setObjectName("frame_frequence")
        self.label_frequence = QtWidgets.QLabel(self.frame_frequence)
        self.label_frequence.setGeometry(QtCore.QRect(140, 40, 69, 16))
        self.label_frequence.setObjectName("label_frequence")
        ###Boutton pour obtenir la fréquence 
        self.pushButton_getfrequence = QtWidgets.QPushButton(self.frame_frequence)
        self.pushButton_getfrequence.setGeometry(QtCore.QRect(110, 80, 124, 28))
        self.pushButton_getfrequence.setObjectName("pushButton_getfrequence")
        ###LCD pour afficher la fréquence 
        self.lcdNumber_freq = QtWidgets.QLCDNumber(self.frame_frequence)
        self.lcdNumber_freq.setGeometry(QtCore.QRect(140, 130, 64, 23))
        self.lcdNumber_freq.setObjectName("lcdNumber_freq")

        ###Frame time constant
        self.frame_time = QtWidgets.QFrame(self.centralwidget)
        self.frame_time.setGeometry(QtCore.QRect(380, 20, 241, 371))
        self.frame_time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_time.setObjectName("frame_time")
        self.label_timeconstant = QtWidgets.QLabel(self.frame_time)
        self.label_timeconstant.setGeometry(QtCore.QRect(70, 30, 98, 16))
        self.label_timeconstant.setObjectName("label_timeconstant")
        ###Boutton pour obtenir la time constant
        self.pushButton_gettimeconstant = QtWidgets.QPushButton(self.frame_time)
        self.pushButton_gettimeconstant.setGeometry(QtCore.QRect(50, 240, 130, 28))
        self.pushButton_gettimeconstant.setObjectName("pushButton_gettimeconstant")
        ###LCD pour afficher la time constant  
        self.lcdNumber_time = QtWidgets.QLCDNumber(self.frame_time)
        self.lcdNumber_time.setGeometry(QtCore.QRect(80, 300, 64, 23))
        self.lcdNumber_time.setObjectName("lcdNumber_time")
        ###Spinbox pour choisir la time constant
        self.spinBox_timeconstant = QtWidgets.QSpinBox(self.frame_time)
        self.spinBox_timeconstant.setGeometry(QtCore.QRect(60, 90, 42, 22))
        self.spinBox_timeconstant.setObjectName("spinBox_timeconstant")
        ###Boutton pour valider la time constant 
        self.pushButton_timeconstant = QtWidgets.QPushButton(self.frame_time)
        self.pushButton_timeconstant.setGeometry(QtCore.QRect(130, 90, 93, 28))
        self.pushButton_timeconstant.setObjectName("pushButton_timeconstant")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sensitivity.setText(_translate("MainWindow", "SENSITIVITY"))
        self.pushButton_sensitivity.setText(_translate("MainWindow", "valider"))
        self.pushButton_getsensitivity.setText(_translate("MainWindow", "obtenir la sensitivity"))
        self.label_tension.setText(_translate("MainWindow", "TENSION"))
        self.pushButton_gettension.setText(_translate("MainWindow", "obtenir la tension"))
        self.label_frequence.setText(_translate("MainWindow", "FREQUENCE"))
        self.pushButton_getfrequence.setText(_translate("MainWindow", "obtenir la fréquence"))
        self.label_timeconstant.setText(_translate("MainWindow", "TIME CONSTANT"))
        self.pushButton_gettimeconstant.setText(_translate("MainWindow", "obtenir time constant"))
        self.pushButton_timeconstant.setText(_translate("MainWindow", "valider"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

