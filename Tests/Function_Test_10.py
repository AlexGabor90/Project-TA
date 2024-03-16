"""
Test login function with valid credentials.
email = nomad60990@yahoo.com
pw = Test2024!
"""
import unittest
from selenium import webdriver

from Base.base_code import BasePage
from Core.code_center import CorePage
from Page_Data_Locators.page_data import PageData


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def goBack(self):
        self.driver.back()

    def test_login(self):
        """
        #Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
            Identificati elementele de tip user si parola si inserati valori incorecte
            (valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)
        #Test 6: Dati click pe butonul "conectare" si verificati urmatoarele:
            1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
        #Test 7: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@"),
            fara sa introduceti si parola si verificati faptul ca butonul de login este dezactivat
        """
        login_test = CorePage(self.driver)
        actual_url = BasePage(self.driver)

        login_test.open_site()
        login_test.accept_cookies()
        login_test.first_connect_button()
        login_test.add_valid_input()
        after_login = PageData.after_login_url

        assert actual_url.get_current_url() == after_login, f'Unexpected URL'
        print("PASS")