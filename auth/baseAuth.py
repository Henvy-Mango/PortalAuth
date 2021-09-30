import time

from auth.utils import request


class BaseAuth(object):
    USER_AGENT = ''
    SIGN_URL = ''
    SIGN_BODY = ''
    KEEP_ALIVE_URL = ''
    KEEP_ALIVE_BODY = ''
    KEEP_SLEEP_TIME = 600

    @property
    def get_sign_header(self):
        header = {
            'Cookie': '',
            'User-Agent': self.USER_AGENT,
            'Accept-Encoding': 'gzip, deflate, br'
        }
        return header

    @property
    def get_keep_header(self):
        return self.get_sign_header

    @property
    def _sign_info(self):
        try:
            response = request(
                'post', self.SIGN_URL, data=self.SIGN_BODY, headers=self.get_sign_header)
        except Exception as e:
            raise Exception(e)
        return response

    @property
    def _keep_alive_info(self):
        try:
            response = request(
                'post', self.KEEP_ALIVE_URL, data=self.KEEP_ALIVE_BODY, headers=self.get_keep_header)
        except Exception as e:
            raise Exception(e)
        return response

    def run(self):
        try:
            timeout = True
            while True:
                if timeout:
                    print(self._sign_info.status_code)
                time.sleep(self.KEEP_SLEEP_TIME)
                keep_status = self._keep_alive_info.status_code
                if keep_status == 200:
                    timeout = False
                else:
                    timeout = True
        except Exception:
            pass
