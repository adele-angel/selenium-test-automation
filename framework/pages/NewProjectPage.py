import time

from config.locators import Locators


class NewProjectPage:
    def __init__(self, driver):
        self.driver = driver

    def set_project_name(self, project_name):
        time.sleep(1)
        # TODO: change to time.sleep() function into a waiter
        self.driver.find_element_by_id(Locators.btn_new_project_xpath).send_keys(project_name)

    def click_advanced_settings(self):
        time.sleep(1)
        # TODO: change to time.sleep() function into a waiter
        self.driver.find_element_by_xpath(Locators.locator_advanced_settings_xpath).click()

    def set_project_description(self, project_description):
        self.driver.find_element_by_xpath(Locators.locator_description_text_xpath).send_keys(project_description)

    def set_status(self, status):
        self.driver.find_element_by_xpath(Locators.locator_status_selector_xpath).click()
        time.sleep(1)
        # TODO: change to time.sleep() function into a waiter
        # TODO: refactor set_status
        if status == "ON TRACK":
            selected_status = self.driver.find_element_by_xpath(Locators.ddStatusOnTrack_xpath)
        elif status == "AT RISK":
            selected_status = self.driver.find_element_by_xpath(Locators.ddStatusAtRisk_xpath)
        elif status == "OFF TRACK":
            selected_status = self.driver.find_element_by_xpath(Locators.ddStatusOffTrack_xpath)
        else:
            selected_status = self.driver.find_element_by_xpath(Locators.ddStatusOnNone_xpath)
        selected_status.click()

    def save_new_project(self):
        self.driver.find_element_by_xpath(Locators.btnSaveNewProduct_xpath).click()
