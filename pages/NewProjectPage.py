import time

from config.locators import TestLocators


class NewProjectPage:
    def __init__(self, driver):
        self.driver = driver

    def set_project_name(self, project_name):
        time.sleep(1)
        self.driver.find_element_by_id(TestLocators.locator_project_name_id).clear()
        self.driver.find_element_by_id(TestLocators.locator_project_name_id).send_keys(project_name)

    def click_advanced_settings(self):
        self.driver.find_element_by_xpath(TestLocators.locator_advanced_settings_xpath).click()

    def set_project_description(self, project_description):
        # self.driver.find_element_by_xpath(TestLocators.locator_description_text_xpath).clear()
        self.driver.find_element_by_xpath(TestLocators.locator_description_text_xpath).send_keys(project_description)

    def set_status(self, status):
        self.driver.find_element_by_xpath(TestLocators.ddStatus_relative_xpath).click()
        time.sleep(1)
        if status == "ON TRACK":
            selected_status = self.driver.find_element_by_xpath(TestLocators.ddStatusOnTrack_xpath)
        elif status == "AT RISK":
            selected_status = self.driver.find_element_by_xpath(TestLocators.ddStatusAtRisk_xpath)
        elif status == "OFF TRACK":
            selected_status = self.driver.find_element_by_xpath(TestLocators.ddStatusOffTrack_xpath)
        else:
            return None
        selected_status.click()

    def save_new_project(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[2]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/div/button').click()
