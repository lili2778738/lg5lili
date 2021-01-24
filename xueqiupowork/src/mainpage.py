import time

from appium.webdriver.common.mobileby import MobileBy

from xueqiupowork.src.basepage import BasePage


class Main_Page(BasePage):
    def gotosearch(self):
        time.sleep(2)
        self.find(MobileBy.ID,"com.xueqiu.android:id/post_status").click()
        time.sleep(5)
        self.find(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()