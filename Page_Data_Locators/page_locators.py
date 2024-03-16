"""
In this file you may find all the locators necessary for our tests.
"""
from selenium.webdriver.common.by import By


class PageLocators:

    cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    search_bar = (By.CSS_SELECTOR, 'input[class="form-control searchTerm js-has-overlay"')
    search_button = (By.CSS_SELECTOR, 'button[class="btn-search btn btn-primary"]')
    get_products = (By.CSS_SELECTOR, 'a[class="product-title"]')
    get_product_price = (By.CLASS_NAME, "current-price ")
    get_products_name = (By.XPATH, '//a[@class="product-title"]')
    login_button = (By.XPATH, '//span[@class="login-prompt js-login-prompt"]')
    connect_button = (By.XPATH, '//a[@class="my-account-login btn btn-primary btn-block"]')
    email_field = (By.ID, 'ShopLoginForm_Login')
    password_field = (By.ID, 'ShopLoginForm_Password')
    login_execute = (By.NAME, 'login')
    login_fail = (By.XPATH, '//div[@role = "alert"]')
    title_text = (By.XPATH, '//title[text()="elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"]')
    not_found = (By.CSS_SELECTOR, 'h1[class="h2"]')
    enter_email = (By.XPATH, '//small[text()="Vă rugăm să introduceți o adresă de email."]')
    enter_password = (By.XPATH, '//small[text()="Vă rugăm să introduceți parola."]')