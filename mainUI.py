from PyQt5 import QtWidgets, QtCore

from auth import Adapter
from windows import Ui_MainWindow


class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, auth, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.retry.clicked.connect(self.repeat)
        self.thread = Adapter(auth)
        self.thread.status.connect(self.print)
        self.thread.start()

    def repeat(self):
        self.textBrowser.clear()
        # self.thread.terminate()
        self.trigger.emit()
        # self.thread.start()

    def print(self, str):
        self.textBrowser.append(f"{str}")
