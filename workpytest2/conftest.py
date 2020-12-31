import pytest
import yaml

@pytest.fixture(scope='module')
def frist():
    print("开始计算")
    yield
    print("结束计算")

with open('./testdata1.yml') as f:
    datas = yaml.safe_load(f)
    data_add = datas['add']
    data_sub = datas['sub']
    data_mul = datas['mul']
    data_div = datas['div']


@pytest.fixture(params=data_add)
def getdataadd(request):
    p=request.param
    return p
@pytest.fixture(params=data_sub)
def getdatasub(request):
    sub=request.param
    return sub
@pytest.fixture(params=data_mul)
def getdatamul(request):
    mul=request.param
    return mul
@pytest.fixture(params=data_div)
def getdatadiv(request):
    div=request.param
    return div




