import pytest
from jiekoupo.src.jiekou import JieKou
from jiekoupo.testcase import readdata
testdata= readdata.data()
class Testmember:
    def setup(self):
        self.member=JieKou()
    @pytest.mark.parametrize('userid,name,mobile,department',testdata)
    def test_addmember(self,userid,name,mobile,department):
        #删除成员
        self.member.deleter(userid)
        #添加成员
        addmember=self.member.add(userid,name,mobile,department)
        assert addmember.get('errmsg')=='created'
        print("创建成员成功")
        #raise Exception("创建成员失败")
        #查询成员
        readperson=self.member.read(userid)
        assert readperson['errmsg']=='ok' and readperson["name"]==name
        print(readperson)

