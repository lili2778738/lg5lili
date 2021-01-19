from appium.webdriver.common.mobileby import MobileBy

from apppowork2.src.addmode_page import Addmode
from apppowork2.src.base_page import Base


class Record(Base):
    def goto_addmode(self,text):
        self.scroll_find_click(text)
        return Addmode(self.basedriver)
