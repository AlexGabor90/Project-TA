"""
Test : Find the product with the lowest price.
"""
import unittest
from selenium import webdriver
from Core.code_center import CorePage


class TestLowProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_low_product(self):
        main_page = CorePage(self.driver)
        cookies = CorePage(self.driver)
        search_product = CorePage(self.driver)
        lowest_price = CorePage(self.driver)

        main_page.open_site()
        cookies.accept_cookies()
        search_product.execute_find_product()
        lowest_product_price = lowest_price.get_min_price()

        self.assertIsInstance(lowest_product_price, float, "Product price with the lowest price is not a string")
        print("PASS")