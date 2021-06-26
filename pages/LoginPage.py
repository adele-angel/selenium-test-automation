from selenium import webdriver
from config.locators import TestLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_menu(self):
        self.driver.find_element_by_xpath(TestLocators.locator_login_xpath).click()

    def set_username(self, username):
        self.driver.find_element_by_id(TestLocators.locator_username_id).clear()
        self.driver.find_element_by_id(TestLocators.locator_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(TestLocators.locator_password_id).clear()
        self.driver.find_element_by_id(TestLocators.locator_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(TestLocators.locator_submit_id).click()
