import pytest
import yaml

from apppowork2.src.app_page import App


def get_data():
    data_list=[]
    with open("./testdata.yml",encoding="UTF-8") as f:
        datas = yaml.safe_load(f)
        for data in datas:
            data_list.append(data)
    return data_list

class Testadd:
     @pytest.mark.parametrize('person,sex,phonenum,emailnum,addressnum',get_data())
     def test_addperson(self,person,sex,phonenum,emailnum,addressnum):
         app=App()
         result=app.startapp().Main().goto_record().goto_addmode("添加成员").goto_manualadd().add_name(person).add_sex(sex).num(phonenum).email(emailnum).address(addressnum).addsuccess().toast()
         assert result.text == "添加成功"
         app.stop()
