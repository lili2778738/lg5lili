from appium import webdriver
from base_page import BasePage
from src.main_page import MainPage


class APP(BasePage):
    def start_app(self):
        if self.basedriver is None:
            caps={
                "platformName": "android",
                "platformVersion": "6.0",
                "deviceName": "127.0.0.1:7555",
                "appPackage":"com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias"
            }
            self.basedriver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
            self.basedriver.implicitly_wait(10)
        else:
            self.basedriver.launch_app()
        return self
    def stop_app(self):
        self.basedriver.quit()
    def Main(self):
        return MainPage(self.basedriver)