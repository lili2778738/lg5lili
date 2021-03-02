import json

from jiekoupo.src.basepage import Base


class JieKou(Base):


    def add(self,userid,name,mobile,department:list):
        urladd=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?"
        addperson={
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
            }
        return self.send('post',urladd,json=addperson)

    def read(self,userid):
        readurl=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send('get',readurl)

    def updata(self,userid,namenew=None):
        updataurl=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?"
        updata={
            "userid": userid,
            "name": namenew
                }
        jupdata=json.dumps(updata)
        header={"Content-Type":"application/json"}
        return  self.send('post',updataurl,data=jupdata,headers=header)

        #assert upperson["errmsg"]=='updated'

    def deleter(self,userid):
        deleterurl=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send('get',deleterurl)
        #assert deleterdata["errmsg"]=='deleted'