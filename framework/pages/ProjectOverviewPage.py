from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config.locators import Locators


# TODO: Put locators in config file
from infra.web_driver_extensions import WebDriverExtensions


class ProjectOverviewPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.driver_extended = WebDriverExtensions(driver)

    def click_work_packages(self):
        self.driver_extended.get_enabled_element((By.XPATH, "//*[@id='menu-sidebar']/ul/li[2]")).click()
        # self.driver_extended.get_driver().current_url or self.driver.current_url

