# Author: Mohan Ravi
# Vesrion: 1.0
# Dependencies: PyQt4, pyHook, Python2.7
# Description: Caps and Num lock indicator using python
# License: GPL Version 3 https://www.gnu.org/licenses/gpl-3.0.txt


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 275)
        MainWindow.setMinimumSize(QtCore.QSize(600, 275))
        MainWindow.setMaximumSize(QtCore.QSize(600, 275))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "About - CapsNumLockInidicator", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/logo.png\"/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">About CapsNumLockIndicator</span></p><p align=\"justify\">Version: <span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">1.0</span></p><p align=\"justify\">Caps Num Lock indicator helps you to identify present status of caps and Numpad. This software is created because in some keyboards you cannot see led indicators to show the status of caps and numpad ON or OFF. I have created this software because am facing the same problem and decided to share it with everyone. </p><p align=\"justify\"><br/>This Software comes with absolutely no warranty.</p><p align=\"justify\">For More details visit <a href=\"http://www.gnu.org/licenses/gpl-3.0.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU GPL License</span></a></p><p align=\"justify\">For Source code please Visit <a href=\"http://github.com/immohanravi/capsnumlockindicator_windows\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p><p align=\"justify\"><br/></p></body></html>", None))

import images_rc
