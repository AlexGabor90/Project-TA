"""
Test if the correct page is accesed.
"""
import unittest
from selenium import webdriver
from Page_Data_Locators.page_data import PageData
from Code_Source.code_center import CorePage
from Base.base_code import BasePage


class TestSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_open(self):
        main_page = CorePage(self.driver)
        cookies = CorePage(self.driver)
        actual_url = BasePage(self.driver)
        page_url = PageData.page_url

        main_page.open_site()
        cookies.accept_cookies()

        assert actual_url.get_current_url() == page_url, f'Unexpected URL'
        print("PASS")