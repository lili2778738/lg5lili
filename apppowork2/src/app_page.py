from appium import webdriver
from apppowork2.src.base_page import Base
from apppowork2.src.main_page import Main


class App(Base):
    def startapp(self):
        if self.basedriver is None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "true",
                "dontStopAppOnReset": "true",
                "unicodeKeyboard": "true",
                "resetKeyboard": "true",
                "skipDeviceInitialization": "true"
            }
            self.basedriver=webdriver.Remote('http://localhost:4723/wd/hub',desire_cap)
        else:
            self.basedriver.start_activity("com.tencent.wework",".launch.WwMainActivity")
        self.basedriver.implicitly_wait(3)
        return self
    def stop(self):
        self.basedriver.quit()
    def Main(self):
        return Main(self.basedriver)