"""
You may find in this file all the methods that are use in the core_page file.
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element = WebDriverWait(self.driver, 10)

    def wait_for_presence_of_element(self, locator: tuple):
        self.wait_for_element.until(EC.presence_of_element_located(locator), "Element is not present on the page")

    def wait_for_clickable_element(self, element: tuple):
        self.wait_for_element.until(EC.element_to_be_clickable(element), "Element is not clickable")

    def wait_for_visibility_element(self, element: tuple):
        self.wait_for_element.until(EC.visibility_of_element_located(element), "Element is not visible")

    def open_url(self, url: str):
        self.driver.get(url)
        self.driver.implicitly_wait(2)

    def get_current_url(self):
        return self.driver.current_url

    def find(self, locator: tuple):
        self.wait_for_presence_of_element(locator)
        return self.driver.find_element(*locator)

    def find_more_elements(self, locator: tuple):
        self.wait_for_presence_of_element(locator)
        return self.driver.find_elements(*locator)

    def type_text(self, input_label, message: str):
        self.wait_for_element.until(EC.presence_of_element_located(input_label), "Element is not present on the page")
        self.find(input_label).send_keys(message)

    def get_text(self, label: tuple):
        self.wait_for_element.until(EC.presence_of_element_located(label), "Element is not present on the page")
        return self.find(label).text

    def is_object_displayed(self, element):
        try:
            return self.find(element).is_displayed()
        except NoSuchElementException:
            return False

    def is_object_enabled(self, element):
        return self.find(element).is_enabled()

    def click(self, button: tuple):
        self.wait_for_element.until(EC.element_to_be_clickable(button), "Element is not clickable")
        self.find(button).click()

    def get_title(self):
        return self.driver.title

    def clear_text(self, element: tuple):
        self.find(element).clear()