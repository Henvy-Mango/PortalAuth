import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from tray import TrayIcon
from windows import Ui_MainWindow

from auth import Adapter, gmccAuth, cdcAuth


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

    import ico_rc

    mainWin.setWindowIcon(QtGui.QIcon(':/icon.ico'))

    mainWin.close()
    # mainWin.show()

    tray = TrayIcon(mainWin)
    tray.show()

    Adapter(gmccAuth).start()

    sys.exit(app.exec_())
