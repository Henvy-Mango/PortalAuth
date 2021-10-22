from PyQt5.QtCore import QThread, pyqtSignal


class Adapter(QThread):
    status = pyqtSignal(int)

    def __init__(self, auth):
        super().__init__()
        self.auth = auth()

    def run(self):
        while True:
            try:
                timeout = True
                while True:
                    if timeout:
                        sign_status = self.auth._sign_info.status_code
                        self.status.emit(sign_status)

                    QThread.sleep(self.auth.KEEP_SLEEP_TIME)

                    keep_status = self.auth._keep_alive_info.status_code
                    self.status.emit(keep_status)

                    if keep_status == 200:
                        timeout = False
                    else:
                        timeout = True
            except Exception:
                pass
