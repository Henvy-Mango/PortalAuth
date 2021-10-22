from auth.baseAuth import BaseAuth


class cdcAuth(BaseAuth):
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    SIGN_URL = 'http://172.18.8.254:8080/portal/pws?t=li'
    SIGN_BODY = 'userName=liangmingxuan&userPwd=bmFvbWkuKzE%3D&serviceType=&isSavePwd=on&userurl=&userip=&basip=&language=Chinese&portalProxyIP=172.18.8.254&portalProxyPort=50200&dcPwdNeedEncrypt=1&assignIpType=0&appRootUrl=http%3A%2F%2F172.18.8.254%3A8080%2Fportal%2F&manualUrl=&manualUrlEncryptKey=rTCZGLy2wJkfobFEj0JF8A%3D%3D'
    KEEP_ALIVE_URL = 'http://172.18.8.254:8080/portal/pws?t=hb'
    KEEP_ALIVE_BODY = 'userip=&basip=&userDevPort=H3C_WX3024E-vlan-01-0099%40vlan&userStatus=99&serialNo=24846&language=Chinese&e_d='

    def get_header(self):
        header = {
            'Cookie': 'hello1=liangmingxuan; hello2=false; hello3=; hello4=; hello5=; i_p_pl=JTdCJTIyZXJyb3JOdW1iZXIlMjIlM0ExJTJDJTIybmV4dFVybCUyMiUzQSUyMmh0dHAlM0ElMkYlMkYxNzIuMTguOC4yNTQlM0E4MDgwJTJGcG9ydGFsJTJGaW5kZXhfZGVmYXVsdC5qc3AlMjIlMkMlMjJxdWlja0F1dGglMjIlM0FmYWxzZSUyQyUyMmNsaWVudExhbmd1YWdlJTIyJTNBJTIyQ2hpbmVzZSUyMiUyQyUyMmFzc2lnbklwVHlwZSUyMiUzQTAlMkMlMjJpTm9kZVB3ZE5lZWRFbmNyeXB0JTIyJTNBMSUyQyUyMmZpbmRQd2RVcmwlMjIlM0ElMjJodHRwJTNBJTJGJTJGMTcyLjE4LjguMjU0JTNBODA4MCUyRnNlbGZzZXJ2aWNlJTJGbWFpbCUyRmZvcmdldFBhc3N3b3JkLmpzZiUzRmluaXQlM0R0cnVlJTI2dXJsJTNEYUhSMGNEb3ZMekUzTWk0eE9DNDRMakkxTkRvNE1EZ3dMM0J2Y25SaGJDOXBibVJsZUY5a1pXWmhkV3gwTG1wemNBJTIyJTJDJTIybmFzSXAlMjIlM0ElMjIlMjIlMkMlMjJpZlRyeVVzZVBvcHVwV2luZG93JTIyJTNBdHJ1ZSU3RA',
            'User-Agent': self.USER_AGENT,
            'Connection': 'keep-alive',
            'Accept': 'text/plain, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        return header
