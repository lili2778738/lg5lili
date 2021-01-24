
from appium.webdriver.webdriver import WebDriver
from xueqiupowork.src.decorator import b


class BasePage:
    def __init__(self,driver: WebDriver=None):
        self.basedriver=driver
    @b
    def find(self,by,locater):
        return self.basedriver.find_element(by, locater)

