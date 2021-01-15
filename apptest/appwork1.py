import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testappwork:
    def setup(self):
        desire_cap = {
          "platformName": "android",
          "deviceName": "127.0.0.1:7555",
          "appPackage": "com.tencent.wework",
          "appActivity": ".launch.WwMainActivity",
          "noReset":"true",
          "dontStopAppOnReset": "true",
          "unicodeKeyboard":"true",
          "resetKeyboard":"true",
          "skipDeviceInitialization":"true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_tencentwork(self):
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        #添加成员
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        #手动添加
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/csn").click()
        #输入信息
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ern']//*[@class='android.widget.EditText']").send_keys("张一凡")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/er7").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/boh']/android.widget.RelativeLayout[2]").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys("18072778765")
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/er1']//android.widget.EditText").send_keys("2282@163.com")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/jr").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/js").send_keys("陕西")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ie7").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='设置部门']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/bcz']/android.widget.RelativeLayout[3]//android.widget.FrameLayout[1]").click()
        #保存
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定(2)']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ie7").click()
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable((MobileBy.ID,"com.tencent.wework:id/idp")))
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/idp").click()
        #回到通讯录页面
        time.sleep(3)
        #验证添加成员是否成功
        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.TextView' and contains(@text,'人')]").click()
        personslist=self.driver.find_elements(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/elh']/android.widget.TextView")
        for person in personslist:
            person_list=[]
            person_list.append(person.text)
        assert "张一凡" in person_list


