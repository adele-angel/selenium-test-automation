from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


class NewProjectPage:
    """
    This class represents the New Project page object model

    Attributes:
        driver (WebDriver): WebDriver instance
        driver_extended (WebDriver): WebDriverExtensions instance
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def set_project_name(self, project_name):
        self.driver_extended.get_enabled_element((By.ID, Locators.input_project_name_id)).send_keys(project_name)

    def click_advanced_settings(self):
        self.driver_extended.get_element((By.XPATH, Locators.btn_advanced_settings_xpath)).click()

    def set_project_description(self, project_desc):
        self.driver_extended.get_enabled_element((By.XPATH, Locators.editor_project_desc_xpath)).send_keys(project_desc)

    def set_status(self, status):
        """
        Opens the project status drop-down menu element and selects a status from the list.

        Args:
            status (str): given project status, status list: On track, At risk, Off track
        """
        # Opening project status drop-down menu
        self.driver_extended.get_element((By.XPATH, Locators.dd_project_status_xpath)).click()
        # Selecting a status from the list
        self.driver_extended.get_visible_element((By.XPATH, Locators.dd_project_selected_status_xpath.format(status))).click()

    def save_new_project(self):
        self.driver_extended.get_element((By.XPATH, Locators.btn_save_project_xpath)).click()
        self.driver_extended.until_not_exists_or_hidden((By.XPATH, Locators.btn_save_project_xpath))

    def get_project_identifier(self):
        """
        Extracts project identifier from current url

        Returns:
            str: project identifier
        """
        return self.driver.current_url.split("/")[4]
