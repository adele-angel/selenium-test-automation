from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProjectOverviewPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def click_work_packages(self):
        self.driver_extended.get_enabled_element((By.ID, Locators.btn_menu_work_packages_id)).click()

    def get_project_name_from_button(self):
        self.driver_extended.until_not_exists_or_hidden((By.XPATH, Locators.btn_save_project_xpath))
        return self.driver_extended.get_element((By.XPATH, Locators.btn_project_name_xpath)).text
