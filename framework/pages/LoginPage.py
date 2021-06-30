from config.locators import Locators


# TODO: add waiters
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_menu(self):
        self.driver.find_element_by_xpath(Locators.dd_login_menu_xpath).click()

    def set_username(self, username):
        self.driver.find_element_by_id(Locators.input_username_id).clear()
        self.driver.find_element_by_id(Locators.input_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(Locators.input_password_id).clear()
        self.driver.find_element_by_id(Locators.input_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.btn_login_id).click()
