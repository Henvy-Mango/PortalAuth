import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from windows import Ui_MainWindow
from tray import TrayIcon


class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.retry.clicked.connect(self.display)

    def display(self):
        self.textBrowser.append(f"重试中！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    mainWin = MainForm()
    mainWin.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    mainWin.setWindowIcon(QtGui.QIcon("icon.png"))

    # mainWin.close()
    mainWin.show()

    ti = TrayIcon(mainWin)
    ti.show()

    sys.exit(app.exec_())
