import time
from config.locators import Locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_project(self):
        # Click "+ Project" button
        self.driver.find_element_by_xpath(Locators.btn_new_project_xpath).click()

    def select_project(self, project_name):
        # Opening projects drop-down menu
        self.driver.find_element_by_xpath(Locators.dd_project_selector_xpath).click()

        time.sleep(2)
        # TODO: change to time.sleep() function into a waiter
        # TODO: add xpath to locators list
        self.driver.find_element_by_xpath(f"//li[contains(@class,'menu-item')]//a[.='{project_name}']").click()
