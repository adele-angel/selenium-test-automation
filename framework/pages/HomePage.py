from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.common.by import By


class HomePage:
    """
    This class represents the Home page object model

    Attributes:
        driver (WebDriver): WebDriver instance
        driver_extended (WebDriver): WebDriverExtensions instance
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def click_new_project_button(self):
        """
        Finds the "+ Project" button element by a given strategy and locator and clicks on it.
        """
        self.driver_extended.get_element((By.XPATH, Locators.btn_new_project_xpath)).click()

    def select_project(self, project_name):
        """
        Opens the drop-down menu element on the top left corner and selects a project by its name from the list.

        Args:
            project_name (str): given project name
        """
        # Clicks "Select a project" button
        self.driver_extended.get_element((By.XPATH, Locators.dd_project_selector_xpath)).click()
        # Clicks a project from the list
        self.driver_extended.get_visible_element((By.XPATH, Locators.dd_selected_project_xpath.format(project_name))).click()
