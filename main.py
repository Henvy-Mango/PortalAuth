import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from auth import Adapter, gmccAuth, cdcAuth
from tray import TrayIcon
from windows import Ui_MainWindow


class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    trigger = QtCore.pyqtSignal()

    def __init__(self, baseAuth, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.retry.clicked.connect(self.repeat)
        self.thread = Adapter(baseAuth)
        self.thread.status.connect(self.print)
        self.thread.start()

    def repeat(self):
        self.textBrowser.clear()
        self.thread.terminate()
        self.trigger.emit()
        self.thread.start()

    def print(self, str):
        self.textBrowser.append(f"{str}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    # mainWin = MainForm(gmccAuth)
    mainWin = MainForm(cdcAuth)

    mainWin.setWindowFlags(QtCore.Qt.WindowType.WindowSystemMenuHint | QtCore.Qt.WindowType.WindowCloseButtonHint)

    mainWin.setWindowIcon(QtGui.QIcon(':/icon.ico'))

    mainWin.close()
    # mainWin.show()

    tray = TrayIcon(mainWin)
    tray.show()

    sys.exit(app.exec_())
