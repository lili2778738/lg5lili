import allure
import pytest


from workpytest2.calculator import Calculator
from workpytest2.conftest import frist


@allure.feature("测试计算器")
class Testcalcultor:
    cal = Calculator()

    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    def test_caladd(self,getdataadd,frist):
        try:
            resadd=self.cal.add(getdataadd[0],getdataadd[1])
            resadd1=round(resadd,4)
            assert resadd==getdataadd[2]
        except TypeError:
            allure.step("这是一个bug")
            print('这是一个bug，请提示只能输入数字')


    @allure.story("测试除法")
    @pytest.mark.run(order=4)
    def test_caldiv(self,getdatadiv):
        try:
            resdiv=self.cal.div(getdatadiv[0],getdatadiv[1])
            resdiv1=round(resdiv,3)
            assert resdiv1==getdatadiv[2]
        except ZeroDivisionError:
            allure.step("这是一个bug")
            print("这是一个bug，应该提示除数不能为0")
        except TypeError:
            allure.step("这是一个bug")
            print("这是一个bug,应提示请输入数字")

    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    def test_calsub(self,getdatasub):
        try:
            with allure.step('传参数'):
                ressub=self.cal.sub(getdatasub[0],getdatasub[1])
                ressub1=round(ressub,4)
            with allure.step('比对结果'):
                assert ressub1==getdatasub[2]
        except TypeError:
            allure.step("这是一个bug")
            print('这是一个Bug,需要提示不能输入空，请输入数字')


    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    def test_calmul(self,getdatamul):
        try:
          if '' in getdatamul:
            allure.step("这是一个bug")
            print('这是一个bug，应该提示请输入数字')
          else:
            resmul = self.cal.mul(getdatamul[0], getdatamul[1])
            resmul1 = round(resmul, 2)
            assert resmul1 == getdatamul[2]
        except TypeError:
            allure.step("这是一个bug")
            print('这是一个bug，应该提示不能输入字符串')
