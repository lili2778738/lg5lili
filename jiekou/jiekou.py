import json

import requests
class Testjiekou:
    userid= "zhangsan789"
    name= "张三789"
    namenew="李四789"
    def setup(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww626e55c7581a9c95&corpsecret=g3a0LW_Q03yhghbCDmOJnJEG8ju2qMngANUnioVojXA"
        data=requests.get(url)
        self.token=data.json()["access_token"]

    def test_add(self):
        urladd=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        addperson={
                "userid": self.userid,
                "name": self.name,
                "alias": "jackzhang789",
                "mobile": "+86 13810000009",
                "department": [1, 2]
            }
        adddata=requests.post(urladd,json=addperson)
        print(adddata.json())
    def test_read(self):
        readurl=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={self.userid}"
        readperson=requests.get(readurl).json()
        print(readperson)
        assert readperson['errmsg']=='ok' and readperson["name"]==self.name

    def test_updata(self):
        updataurl=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        updata={
            "userid": self.userid,
            "name": self.namenew
                }
        jupdata=json.dumps(updata)
        header={"Content-Type":"text/json"}
        upperson=requests.post(updataurl,data=jupdata,headers=header).json()
        print(upperson)
        assert upperson["errmsg"]=='updated'

    def test_deleter(self):
        deleterurl=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={self.userid}"
        deleterdata=requests.get(deleterurl).json()
        print(deleterdata)
        assert deleterdata["errmsg"]=='deleted'