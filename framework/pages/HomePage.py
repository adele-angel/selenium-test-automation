from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


# TODO: add xpath to locators list

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def click_new_project_button(self):
        # Click "+ Project" button
        self.driver_extended.get_element((By.XPATH, Locators.btn_new_project_xpath)).click()

    def select_project(self, project_name):
        # Opening projects drop-down menu
        self.driver_extended.get_element((By.XPATH, Locators.dd_project_selector_xpath)).click()
        # Selecting project from the list
        self.driver_extended.get_visible_element((By.XPATH, Locators.dd_selected_project_xpath.format(project_name))).click()
