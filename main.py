# Author: Mohan Ravi
# Vesrion: 1.0
# Dependencies: PyQt4, pyHook, Python2.7
# Description: Caps and Num lock indicator using python
# License: GPL Version 3 https://www.gnu.org/licenses/gpl-3.0.txt

import sys
import threading
from PyQt4 import QtCore

from PyQt4 import QtGui
from win32api import GetKeyState
import pyHook
import pythoncom
from PyQt4.QtCore import pyqtSignal

import about
from win32con import VK_CAPITAL , VK_NUMLOCK

caps = GetKeyState(VK_CAPITAL)
num = GetKeyState(VK_NUMLOCK)
ButtonClicked = ""


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        menu = QtGui.QMenu(parent)

        exitAction= QtGui.QAction("&Quit", self,
                                  triggered=QtGui.QApplication.instance().quit)
        exitAction.setIcon(QtGui.QIcon(':/images/exit.png'))
        exitAction.triggered.connect(parent.close)
        aboutAction = QtGui.QAction("About",self)
        aboutAction.setIcon(QtGui.QIcon(':/images/about.png'))
        menu.addAction(exitAction)
        menu.addAction(aboutAction)
        self.about = aboutPage()
        aboutAction.triggered.connect(self.about.display)
        self.setContextMenu(menu)


class aboutPage(QtGui.QMainWindow,about.Ui_MainWindow):
    def __init__(self, parent=None):
        super(aboutPage,self).__init__(parent)
        self.setupUi(self)
    def display(self):
        self.show()


class windows(QtGui.QWidget):
    def __init__(self):
        super(windows, self).__init__()
        gs = GlobalShortCut()
        gs.start()
        gs.keyCapture.connect(self.changeIcon)

        if caps == 1:
            self.capIcon = SystemTrayIcon(QtGui.QIcon(':/images/capsON.png'),self)
            self.capIcon.show()
            self.capsCount = 1
            self.capIcon.setToolTip("Caps Lock On")
        elif caps == 0:
            self.capIcon = SystemTrayIcon(QtGui.QIcon(':/images/capsOFF.png'), self)
            self.capIcon.show()
            self.capsCount = 2
            self.capIcon.setToolTip("Caps Lock Off")

        if num == 1:
            self.numIcon = SystemTrayIcon(QtGui.QIcon(':/images/numON.png'),self)
            self.numIcon.show()
            self.numCount = 1
            self.numIcon.setToolTip("num Lock On")

        elif num == 0:
            self.numIcon = SystemTrayIcon(QtGui.QIcon(':/images/numOFF.png'), self)
            self.numIcon.show()
            self.numCount = 2
            self.numIcon.setToolTip("num Lock Off")

    def changeIcon(self):
        if ButtonClicked == "Capital":
            self.capsCount += 1
            if self.capsCount%2 == 0:
                self.capIcon.setIcon(QtGui.QIcon(':/images/capsOFF.png'))
                self.capIcon.setToolTip("Caps Lock Off")

            else:
                self.capIcon.setIcon(QtGui.QIcon(':/images/capsON.png'))
                self.capIcon.setToolTip("Caps Lock On")

        elif ButtonClicked == "Numlock":
            self.numCount += 1
            if self.numCount%2 == 0:
                self.numIcon.setIcon(QtGui.QIcon(':/images/numOFF.png'))
                self.numIcon.setToolTip("num Lock Off")
            else:
                self.numIcon.setIcon(QtGui.QIcon(':/images/numON.png'))
                self.numIcon.setToolTip("num Lock On")

class GlobalShortCut(QtCore.QThread):
    keyCapture = pyqtSignal()
    def run(self):
        def OnKeyboardEvent(event):
            global ButtonClicked
            ButtonClicked = str(event.Key)
            self.keyCapture.emit()
            return True
        hm = pyHook.HookManager()
        # watch for all mouse events
        hm.KeyDown = OnKeyboardEvent
        # set the hook
        hm.HookKeyboard()
        pythoncom.PumpMessages()

if __name__ == '__main__':

    app = QtGui.QApplication([])
    window = windows()
    window.setWindowTitle("CapsNumLockIndicator")
    QtGui.QApplication.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec_())

