from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProjectOverviewPage:
    """
    This class represents the Project Overview page object model

    Attributes:
        driver (WebDriver): WebDriver instance
        driver_extended (WebDriver): WebDriverExtensions instance
    """

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def click_work_packages(self):
        """
        Finds the "Work Packages" button from the left side menu element and clicks it.
        """
        self.driver_extended.get_enabled_element((By.ID, Locators.btn_menu_work_packages_id)).click()

    def get_project_name_from_button(self):
        """
        Waits until newly created project is saved, finds the drop-down menu element on the top left corner and extracts the selected project name.

        Returns:
            str: selected project name
        """
        self.driver_extended.until_not_exists_or_hidden((By.XPATH, Locators.btn_save_project_xpath))
        return self.driver_extended.get_element((By.XPATH, Locators.btn_project_name_xpath)).text
