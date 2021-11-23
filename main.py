import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from auth import cdcAuth, gmccAuth
from mainUI import MainForm
from tray import TrayIcon

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    mainWin = MainForm(gmccAuth)
    # mainWin = MainForm(cdcAuth)

    mainWin.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)

    import ico_rc
    mainWin.setWindowIcon(QtGui.QIcon(':/icon.ico'))

    mainWin.close()
    # mainWin.show()

    tray = TrayIcon(mainWin)
    tray.show()

    sys.exit(app.exec_())
