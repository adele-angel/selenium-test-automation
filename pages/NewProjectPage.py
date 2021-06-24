import time

from config.locators import TestLocators


class NewProjectPage:
    def __init__(self, driver):
        self.driver = driver

    def set_project_name(self, project_name):
        time.sleep(3)
        self.driver.find_element_by_id(TestLocators.locator_project_name_id).clear()
        self.driver.find_element_by_id(TestLocators.locator_project_name_id).send_keys(project_name)

    def click_advanced_settings(self):
        self.driver.find_element_by_xpath(TestLocators.locator_advanced_settings_xpath).click()

    def set_project_description(self, project_description):
        self.driver.find_element_by_xpath(TestLocators.locator_description_text_xpath).clear()
        self.driver.find_element_by_xpath(TestLocators.locator_description_text_xpath).send_keys(project_description)

    def set_status(self, status):
        self.driver.find_element_by_class(TestLocators.locator_status_selector_class).click()

    def create_new_project(self):
        self.driver.find_element_by_xpath(TestLocators.locator_save_button_xpath).click()
