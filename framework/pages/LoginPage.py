from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


class LoginPage:
    """
    This class represents the Login page object model

    Attributes:
        driver (WebDriver): WebDriver instance
        driver_extended (WebDriver): WebDriverExtensions instance
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def open_login_menu(self):
        """
        Finds the "Sign in" drop-down menu element by a given strategy and locator and clicks on it.
        """
        self.driver_extended.get_element((By.XPATH, Locators.dd_login_menu_xpath)).click()

    def set_username(self, username):
        self.driver_extended.force_clear((By.ID, Locators.input_username_id)).send_keys(username)

    def set_password(self, password):
        self.driver_extended.force_clear((By.ID, Locators.input_password_id)).send_keys(password)

    def click_login(self):
        """
        Finds the "Sign in" submit button element by a given strategy and locator and clicks on it.
        """
        self.driver_extended.get_visible_element((By.ID, Locators.btn_login_id)).click()

    def can_sign_out(self):
        """
        Finds the "Sign out" button element by a given strategy and locator.

        Returns:
            bool: True if logged in to OpenProject, else False
        """
        return self.driver_extended.until_not_exists_or_hidden((By.XPATH, Locators.link_sign_out_xpath))
