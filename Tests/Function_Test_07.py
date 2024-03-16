"""
Test the account and connect button.
"""
import unittest
from selenium import webdriver

from Base.base_code import BasePage
from Core.code_center import CorePage
from Page_Data_Locators.page_data import PageData


class LoginURL(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_url(self):
        login_test = CorePage(self.driver)
        actual_url = BasePage(self.driver)

        login_test.open_site()
        login_test.accept_cookies()
        login_test.first_connect_button()

        login_url = PageData.login_url

        assert actual_url.get_current_url() == login_url, f'Unexpected URL'
        print("PASS")