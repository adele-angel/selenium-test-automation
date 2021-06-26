import time

from selenium import webdriver
from config.locators import TestLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_project(self):
        self.driver.find_element_by_xpath(TestLocators.locator_new_project_button_xpath).click()

    def select_project(self, project_name):
        self.driver.find_element_by_xpath(TestLocators.locator_project_selector_xpath).click()
        time.sleep(2)
        project_list = self.driver.find_elements_by_link_text("/projects/" + "testproject1")
        for x in range(len(project_list)):
            print(project_list[x].text)
