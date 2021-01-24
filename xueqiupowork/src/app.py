from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from xueqiupowork.src.basepage import BasePage
from xueqiupowork.src.mainpage import Main_Page


class APP(BasePage):
    def startapp(self):
        if self.basedriver is None:
            Capability={
                    "platformName": "android",
                    "platformVersion":"6.0",
                    "deviceName": "127.0.0.1:7555",
                    "appPackage": "com.xueqiu.android",
                    "appActivity": ".view.WelcomeActivityAlias",
                    "noReset": "true",
                    "dontStopAppOnReset": "true"
            }
            self.basedriver=webdriver.Remote('http://localhost:4723/wd/hub',Capability)
        else:
            self.basedriver.start_activity("com.xueqiu.android",".view.WelcomeActivityAlias")
        self.basedriver.implicitly_wait(10)
        return self

    def stopapp(self):
        self.basedriver

    def Main(self):
        return Main_Page(self.basedriver)