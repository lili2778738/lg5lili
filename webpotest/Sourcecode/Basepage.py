import json
import time

from appium.webdriver.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By


class basepage():
    _url = ''
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            #debugging9222
            # chrome_args = webdriver.ChromeOptions()
            # chrome_args.debugger_address = "127.0.0.1:9222"
            # self._driver = webdriver.Chrome(options=chrome_args)
            self._driver=webdriver.Chrome()
            self._driver.maximize_window()
            self._usecookie()
        else:
            self._driver=driver
        if self._url !='':
            self._driver.get(self._url)


    def _usecookie(self):
        self._driver.get("https://work.weixin.qq.com/")
        with open("../Sourcecode/cookies.json","r") as f:
            cookies=json.load(f)
            for cookie in cookies:
                self._driver.add_cookie(cookie)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)


    def find(self,by,value):
            return self._driver.find_element(by=by,value=value)
