import time

from base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.data("../src/sreach_page_data.yml",'search')
        return True




