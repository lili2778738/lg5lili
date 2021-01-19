from appium.webdriver.common.mobileby import MobileBy

from apppowork2.src.base_page import Base


class Manualadd(Base):
    def add_name(self,person):
        self.find_send((MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ern']"
                                 "//*[@class='android.widget.EditText']"),person)
        return self
    def add_sex(self,sex):
        self.find((MobileBy.ID, "com.tencent.wework:id/er7")).click()
        if sex == "男":
            self.find_click((MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/boh']//*[@text='男']"))
        else:
            self.find_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/boh']//*[@text='女']"))
        return self
    def num(self,phone):
        self.find_send((MobileBy.XPATH,"//*[@text='手机号']"),phone)
        return self
    def email(self,emailnum):
        self.find_send((MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/er1']//android.widget.EditText"),emailnum)
        return self
    def address(self,address):
        self.find_click((MobileBy.ID,"com.tencent.wework:id/jr"))
        self.find_send((MobileBy.ID,"com.tencent.wework:id/js"),address)
        self.find_click((MobileBy.ID,"com.tencent.wework:id/ie7"))
        return self
    def department(self):
        self.find_click((MobileBy.XPATH, "//*[@text='设置部门']"))
        self.find_click((MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/bcz']/android.widget.RelativeLayout[3]"
                                 "//android.widget.FrameLayout[1]"))
        return self
    def addsuccess(self):
        self.find_click((MobileBy.XPATH,"//*[@text='保存']"))
        from apppowork2.src.addmode_page import Addmode
        return Addmode(self.basedriver)