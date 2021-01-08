import json
import time
from selenium import webdriver

#使用cookie登录
class Testcookie:
    def setup(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_getcookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        time.sleep(20)
        cookies=self.driver.get_cookies()
        with open ("cookies.json","w") as f:
            json.dump(cookies,f)
    def test_usecookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookies.json",'r') as f:
            cookies=json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_manageTools").click()
        time.sleep(5)
        time.sleep(20)