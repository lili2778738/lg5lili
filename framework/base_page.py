import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from handle_page import HandlePage


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.basedriver=driver
    # @HandlePage
    def find(self,by,lactor):
        black_list=[(MobileBy.ID,"com.xueqiu.android:id/iv_close")]
        try:
            result=self.basedriver.find_element(by,lactor)
            return result
        except Exception as e:
            for black in black_list:
                print(black)
                eles=self.basedriver.find_elements(black)
                if len(eles)>0:
                    ele=self.basedriver.find_element(*black)
                    ele[0].click()
                    result=self.basedriver.find_element(by,lactor)
                    return result
            raise e


    #显示等待
    def wait_click(self,by,lactor):
        WebDriverWait(self.basedriver,10).until(expected_conditions.element_to_be_clickable((by,lactor)))
    def wait_presence(self,by,lactor):
        WebDriverWait(self.basedriver,10).until(expected_conditions.presence_of_element_located((by, lactor)))
    #操作
    def find_click(self,by,lactor):
        self.find(by, lactor).click()
    def find_sedkeys(self,by,lactor,value):
        self.find(by, lactor).send_keys(value)
    #读取yaml
    def data(self,path,name):
        with open(path, "rb") as f:
            datas = yaml.safe_load(f)
            data=datas[name]
            print(data)
            for everydata in data:
                action = everydata['action']
                print(action)
                if action == 'click':
                    # self.wait_click(everydata['by'], everydata['lactor'])
                    print(everydata['by'], everydata['lactor'])
                    self.find_click(everydata['by'], everydata['lactor'])
                elif action == 'sendkeys':
                    self.wait_presence(everydata['by'], everydata['lactor'])
                    self.find_sedkeys(everydata['by'], everydata['lactor'], everydata['value'])
