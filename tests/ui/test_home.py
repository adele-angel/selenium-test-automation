import pytest
from selenium import webdriver

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utils.LogGenerator import LogGenerator
from config.credentials import TestCredentials
from config.settings import TestSettings


class TestHome:
    logger = LogGenerator.log_generator()

    def test_click_new_project(self, setup):
        self.logger.info("*************** Test_003 Home *****************")
        self.driver = setup
        self.logger.info("--- Opening URL")
        self.driver.get(TestCredentials.BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(TestCredentials.USERNAME)
        self.login_page.set_password(TestCredentials.PASSWORD)
        self.login_page.click_login()
        self.logger.info("-- Login successful")

        self.logger.info("--- Clicking the new project button")
        self.home_page = HomePage(self.driver)
        self.home_page.click_new_project()
        actual_title = self.driver.title

        if actual_title == TestCredentials.NEW_PROJECT_PAGE_TITLE:
            self.logger.info("**** New Project Page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** New Project Page title test failed ****")
            self.driver.save_screenshot(TestSettings.SCREENSHOT_PATH + "009_003_new_project_page_title.png")
            self.driver.close()
            assert False
