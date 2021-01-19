from appium.webdriver.common.mobileby import MobileBy

from apppowork2.src.base_page import Base
from apppowork2.src.record_page import Record


class Main(Base):
    def goto_record(self):
        self.find_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        return Record(self.basedriver)

