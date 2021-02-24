import time

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from base_page import BasePage
from src.sreach_page import SearchPage


class MainPage(BasePage):
    def handle(self):
        self.data("../src/main_page_data.yml",'handle')
        return SearchPage(self.basedriver)
    def goto_search(self):
        self.data("../src/main_page_data.yml",'search')
        return SearchPage(self.basedriver)
