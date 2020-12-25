import pytest
import testdata as testdata
import yaml

from workpytest.calculator import Calculator

def data():
    with open('./testdata.yaml') as f:
        datas = yaml.safe_load(f)
        add_data = datas['add']
        add_ids = datas['addids']
        sub_data =datas['sub']
        sub_ids = datas['subids']
        mul_data = datas['mul']
        div_data = datas['div']
        return [add_data,add_ids,sub_data,sub_ids,mul_data,div_data]


class Testcalculator(Calculator):
    def setup_class(self):
        self.rel=Calculator()
    @pytest.mark.parametrize('a,b,expected',data()[0],ids=data()[1])
    def test_add(self,a,b,expected):
        result = self.rel.add(a,b)
        assert result==expected
        print(f"\n{a}加{b}等于{expected}")
    @pytest.mark.parametrize('a,b,expected',data()[2])
    def test_sub(self,a,b,expected):
        result = self.rel.sub(a, b)
        new_res=round(result,4)
        assert new_res== expected
        print(f"\n{a}减{b}等于{expected}")
    @pytest.mark.parametrize('a,b,expected', data()[-2])
    def test_mul(self,a,b,expected):
        res_mul=self.rel.mul(a,b)
        new_mul=round(res_mul,2)
        assert new_mul==expected
        print(f"\n{a}乘以{b}等于{'%e'%expected}")

    @pytest.mark.parametrize('a,b,expected',data()[-1])
    def test_div(self,a,b,expected):
        try:
            r=self.rel.div(a,b)
            resultdiv = self.rel.div(a, b)
            newres=round(resultdiv,3)
        except ZeroDivisionError:
            print('除数不能为0')
        else:
            assert newres==expected
            print(f'\n{a}除以{b}等于{expected}')
            pass
