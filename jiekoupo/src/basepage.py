import requests


class Base:
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww626e55c7581a9c95&corpsecret=g3a0LW_Q03yhghbCDmOJnJEG8ju2qMngANUnioVojXA"
        data = requests.request('get', url).json()
        self.token = data.get("access_token")
        self.session = requests.Session()
        self.session.params = {'access_token':self.token}
    def send(self, *args, **kwargs):
        return self.session.request(*args, **kwargs).json()