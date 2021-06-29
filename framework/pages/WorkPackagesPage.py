import copy
import time

from selenium.webdriver.common.by import By

from config.locators import Locators

# TODO: Put locators in config file
from infra.web_driver_extensions import WebDriverExtensions


class WorkPackagesPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def create_new_task(self):
        # Click "+ Create"
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/header/div[1]/ul/li[2]').click()
        # TODO: change to time.sleep() function into a waiter
        time.sleep(1)
        # Choose work package of type "Task"
        self.driver.find_element_by_xpath('//*[@id="quick-add-menu"]//a[.="Task"]').click()

    def set_task_subject(self, task_subject):
        self.driver.find_element_by_xpath('//*[@id="wp-new-inline-edit--field-subject"]').send_keys(task_subject)

    def set_task_description(self, task_description):
        self.driver.find_element_by_xpath('//*[@class="op-uc-p"]').send_keys(task_description)

    def save_new_task(self):
        self.driver.find_element_by_id("work-packages--edit-actions-save").click()

    def get_table_row_count(self):
        rows = self.driver_extended.get_elements(
            (By.XPATH, "//tbody[contains(@class,'results-tbody work-package--results-tbody')]//tr"))
        return len(rows)

    def get_last_table_row(self):
        # TODO: refactor
        last_row = self.driver.find_elements_by_xpath(
            "//tbody[contains(@class,'results-tbody work-package--results-tbody')]//tr[last()]//span//span")
        last_row_data = {
            "id": last_row[0].find_element_by_tag_name("a").text,
            "subject": last_row[3].text,
            "type": last_row[4].text
        }
        return last_row_data

    def click_go_back_button(self):
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/div/back-button').click()
