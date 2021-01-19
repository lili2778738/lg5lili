from appium.webdriver.common.mobileby import MobileBy

from apppowork2.src.base_page import Base
from apppowork2.src.manualadd_page import Manualadd


class Addmode(Base):
    def goto_manualadd(self):
        self.find_click((MobileBy.ID, "com.tencent.wework:id/csn"))
        return Manualadd(self.basedriver)
    def toast(self):
        result=self.find((MobileBy.XPATH,"//*[@class='android.widget.Toast']"))
        return result
