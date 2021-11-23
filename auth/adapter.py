from PyQt5.QtCore import QThread, pyqtSignal


class Adapter(QThread):
    status = pyqtSignal(str)

    def __init__(self, auth):
        super().__init__()
        self.auth = auth()

    def run(self):
        while True:
            try:
                re_login = True
                while True:
                    if re_login:
                        sign_status = self.auth._sign_info.status_code
                        self.status.emit(f'LoginStatus: {str(sign_status)}')

                    QThread.sleep(self.auth.KEEP_SLEEP_TIME)

                    keep_status = self.auth._keep_alive_info.status_code

                    if keep_status == 200:
                        re_login = False
                    else:
                        re_login = True
                        self.status.emit(f'KeepStatusError: {str(keep_status)}')
            except Exception:
                pass
