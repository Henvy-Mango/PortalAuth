import time

import requests
import requests.utils

from auth.baseAuth import BaseAuth
from auth.utils import request


class gmccAuth(BaseAuth):
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'
    SIGN_URL = 'https://10.251.91.26/dana-na/auth/url_default/login.cgi'
    SIGN_BODY = 'tz_offset=480&username=zsiap&password=password&realm=Portal%E5%B8%90%E5%8F%B7%E7%99%BB%E5%BD%95&btnSubmit=%E7%99%BB%E5%BD%95'
    KEEP_ALIVE_URL = 'https://10.251.91.26/dana/home/infranet.cgi'
    KEEP_ALIVE_BODY = 'heartbeat=1&clientlessEnabled=1&sessionExtension=0&notification_originalmsg=&instruction_originalmsg=3e435aa948d89b878895254336284320'
    KEEP_SLEEP_TIME = 30

    @property
    def get_sign_header(self):
        header = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': self.USER_AGENT,
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': 'lastRealm=Portal%u5E10%u53F7%u767B%u5F55; DSSIGNIN=url_default; DSSignInURL=/'
        }
        return header

    @property
    def get_keep_header(self):
        cookies_str = ''
        for key, value in self._cookie.items():
            cookies_str = f'{cookies_str}{key}={value}; '
        cookies_str = f'{cookies_str}DSLastAccess={int(time.time())}'

        print(cookies_str)

        header = {
            'Connection': 'keep-alive',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': cookies_str,
            'User-Agent': self.USER_AGENT,
        }
        return header

    @property
    def _sign_info(self):
        try:
            response = request(
                'post', self.SIGN_URL, data=self.SIGN_BODY, headers=self.get_sign_header, verify=False)
            self._cookie = requests.utils.dict_from_cookiejar(response.history[0].cookies)
        except Exception as e:
            raise Exception(e)
        return response

    @property
    def _keep_alive_info(self):
        try:
            response = request(
                'post', self.KEEP_ALIVE_URL, data=self.KEEP_ALIVE_BODY, headers=self.get_keep_header, verify=False)
        except Exception as e:
            raise Exception(e)
        return response
