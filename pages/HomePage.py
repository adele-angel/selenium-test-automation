from selenium import webdriver
from config.locators import TestLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_project(self):
        self.driver.find_element_by_xpath(TestLocators.locator_new_project_button_xpath).click()
