import time

from config.locators import Locators


# TODO: Put locators in config file

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_project(self):
        self.driver.find_element_by_xpath(Locators.locator_new_project_button_xpath).click()

    def select_project(self, project_name):
        # Opening drop-down menu
        self.driver.find_element_by_xpath(Locators.locator_project_selector_xpath).click()
        time.sleep(2)
        # TODO: change to time.sleep() function into a waiter
        self.driver.find_element_by_xpath(f"//li[contains(@class,'menu-item')]//a[.='{project_name}']").click()
