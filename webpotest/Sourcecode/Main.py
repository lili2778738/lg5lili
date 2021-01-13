
from selenium.webdriver.common.by import By
from webpotest.Sourcecode.AddressBookPAGE import addressbookpage
from webpotest.Sourcecode.Basepage import basepage


class main(basepage):
    def go_to_addressbook(self):
        self.find(By.ID,'menu_contacts').click()
        return addressbookpage(self._driver)