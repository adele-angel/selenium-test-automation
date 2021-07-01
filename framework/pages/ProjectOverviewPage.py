from config.locators import Locators
from infra.web_driver_extensions import WebDriverExtensions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProjectOverviewPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def click_work_packages(self):
        self.driver_extended.get_enabled_element((By.XPATH, Locators.dd_actions_xpath)).click()
