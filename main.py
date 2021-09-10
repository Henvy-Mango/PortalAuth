import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt as QtCore

from windows import Ui_MainWindow


class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, MainWindow, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow
        self.createMenu()

    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showAction1 = QtWidgets.QAction(text="显示", triggered=self.show_window)
        self.showAction2 = QtWidgets.QAction(text="通知", triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction(text="退出", triggered=self.quit)

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        # 设置图标
        self.setIcon(QtGui.QIcon("icon.png"))
        self.icon = self.MessageIcon()

        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)

    def showMsg(self):
        self.showMessage("Message", "skr at here", self.icon)

    def show_window(self):
        # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        self.ui.showNormal()
        self.ui.activateWindow()

    def quit(self):
        QtWidgets.qApp.quit()

    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            # self.showMessage("Message", "skr at here", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():
                # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
                self.ui.showNormal()
                self.ui.activateWindow()

                self.ui.show()
            else:
                # 若不是最小化，则最小化
                self.ui.showMinimized()
                self.ui.show()


class MyMainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.login.clicked.connect(self.display)

    def display(self):
        username = self.account.text()
        password = self.password.text()
        self.textBrowser.setText("登录成功!\n" + "用户名是: " + username + ",密码是： " + password)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    myWin = MyMainForm()
    myWin.setWindowFlags(QtCore.WindowSystemMenuHint | QtCore.WindowCloseButtonHint)
    myWin.setWindowIcon(QtGui.QIcon("icon.png"))
    myWin.close()

    ti = TrayIcon(myWin)
    ti.show()

    sys.exit(app.exec_())
