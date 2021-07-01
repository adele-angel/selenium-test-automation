from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def open_login_menu(self):
        self.driver_extended.get_element((By.XPATH, Locators.dd_login_menu_xpath)).click()

    def set_username(self, username):
        self.driver_extended.force_clear((By.ID, Locators.input_username_id)).send_keys(username)

    def set_password(self, password):
        self.driver_extended.force_clear((By.ID, Locators.input_password_id)).send_keys(password)

    def click_login(self):
        self.driver_extended.get_visible_element((By.ID, Locators.btn_login_id)).click()
