from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webpotest.Sourcecode.Section_PAGE import *


class addressbookpage(basepage):
    def go_to_section(self):
        time.sleep(2)
        self.find(By.XPATH,"//*[@class='member_colLeft_top_addBtnWrap js_create_dropdown']").click()
        time.sleep(2)
        self.find(By.XPATH,"//*[@class='js_create_party']").click()
        time.sleep(2)
        return section_add(self._driver)
    def get_list_section(self):
        section_lists=self._driver.find_elements_by_xpath("//*[@class='jstree-node js_editable jstree-last jstree-open']//a")
        section_list=[]
        for section in section_lists:
            section_list.append(section.text)
        return section_list
    def dele_section(self):
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@id='1688851049118678']/i")))
        self.find(By.XPATH,"//*[@id='1688851049118678']/i").click()
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='jstree-children']//li[1]//li")))
        self.find(By.XPATH,"//*[@class='jstree-children']//li[1]//li").click()
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@id='1688851049118678']/ul/li/a/span")))
        self.find(By.XPATH,"//*[@id='1688851049118678']/ul/li/a/span").click()
        self.find(By.XPATH,"//*[@class='vakata-context jstree-contextmenu jstree-default-contextmenu']/li[7]/a").click()
        self.find(By.XPATH,"//*[@d_ck='submit']").click()
