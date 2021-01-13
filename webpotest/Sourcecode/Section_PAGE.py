import time
from selenium.webdriver.common.by import By
from webpotest.Sourcecode.Basepage import basepage


class section_add(basepage):
    def section(self,sectionname):
        self.find(By.XPATH,"//*[@class='qui_inputText ww_inputText' and @name='name']").send_keys(sectionname)
        self.find(By.XPATH,"//*[@class='js_parent_party_name']").click()
        self.find(By.XPATH,"//*[@class='qui_dialog_body ww_dialog_body']//*[@id='1688851049118678_anchor']").click()
        self.find(By.XPATH,"//*[@class='qui_btn ww_btn ww_btn_Blue']").click()
        time.sleep(2)
        from webpotest.Sourcecode.AddressBookPAGE import addressbookpage
        return addressbookpage(self._driver)
    def section_null(self):
        self.find(By.XPATH, "//*[@class='qui_inputText ww_inputText' and @name='name']").send_keys(" ")
        self.find(By.XPATH, "//*[@class='js_parent_party_name']").click()
        self.find(By.XPATH, "//*[@class='qui_dialog_body ww_dialog_body']//*[@id='1688851049118678_anchor']").click()
        self.find(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue']").click()
        message=self.find(By.ID,'js_tips').text
        return message


