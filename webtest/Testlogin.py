import time

import selenium
import pytest
from selenium import webdriver

# 使用chrome debugger登录
class Testlogin():

    def setup(self):
        chrome_args=webdriver.ChromeOptions()
        chrome_args.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=chrome_args)
    def teardown(self):
        self.driver.quit()
    def test_weixin(self):
        self.driver.find_element_by_id('menu_manageTools').click()
        time.sleep(3)
