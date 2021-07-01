from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


class NewProjectPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def set_project_name(self, project_name):
        self.driver_extended.get_visible_element((By.ID, Locators.input_project_name_id)).send_keys(project_name)

    def click_advanced_settings(self):
        self.driver_extended.get_element((By.XPATH, Locators.btn_advanced_settings_xpath)).click()

    def set_project_description(self, project_desc):
        self.driver_extended.get_visible_element((By.XPATH, Locators.editor_project_desc_xpath)).send_keys(project_desc)

    def set_status(self, status):
        # Opening project status drop-down menu
        self.driver_extended.get_element((By.XPATH, Locators.dd_project_status_xpath)).click()
        # Selecting a status from the list
        self.driver_extended.get_visible_element((By.XPATH, f"//span[text()='{status}']//parent::div")).click()

    def save_new_project(self):
        self.driver_extended.get_element((By.XPATH, Locators.btn_save_project_xpath)).click()

    def get_project_identifier(self):
        url = self.driver.current_url
        identifier = url.split("/")
        return identifier[4]
