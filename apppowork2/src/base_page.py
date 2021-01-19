import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



class Base:
    _black_list=[()]
    def __init__(self,driver:WebDriver=None):
        self.basedriver=driver
    def find(self,laction):
        try:
            ele=self.basedriver.find_element(*laction)
            return ele
        except:
            for black in self._black_list:
                ele_black=self.basedriver.find_element(*black)
                if len(ele_black) > 0:
                    ele_black[0].click()
                    break
            return self.basedriver.find_element(*laction)
    def find_click(self,laction):
        self.find(laction).click()
    def scroll_find_click(self,context):
        ele=(MobileBy.ANDROID_UIAUTOMATOR,
         'new UiScrollable(new UiSelector().'
         'scrollable(true).instance(0)).'
         'scrollIntoView(new UiSelector().'
         f'text("{context}").instance(0));')
        self.find(ele).click()
    def find_send(self,laction,impro):
        self.find(laction).send_keys(impro)


